# Companies, branches and the chart of accounts

A company (`res.company`) is a legal entity with its own currency, country, taxes,
journals, accounts and numbering. Most configuration records carry a `company_id`, and a
user sees the records of the companies they are allowed in. A branch (17.0 and later) is
a subdivision of one legal entity under a parent company. The chart of accounts is loaded
per company from the country's fiscal localization, once, before the first entry. A
company needs only `base`; the chart, taxes and journals need `account` (Invoicing).
Inter-company transactions are Enterprise and left out.

## Before you start

- Apps: `base`; `account` for the chart of accounts. Branches from 17.0.
- Settings: none to switch on. A user given a second company, or a branch, gets
  multi-company (`base.group_multi_company`) by itself. In an Odoo subscription a
  second company can change the plan: ask first.
- Read first:

```python
for c in env['res.company'].search([]):
    print(c.id, c.name, c.country_id.code, c.currency_id.name, c.parent_id.name,
          c.chart_template if 'chart_template' in c else c.chart_template_id.name)   # 17.0+ / 16.0
print(env['account.move'].search_count([('state', '=', 'posted')]))
```

## The standard flow

Odoo's order: the company's details, its users and their access, its document layout;
with Accounting, the fiscal localization package before the first entry. Branches are
added from the parent company once it exists.

1. **Create the company.** Settings ‣ Companies section ‣ Manage Companies ‣ New, which
   opens Settings ‣ Users & Companies ‣ Companies. Name, address, currency, email; the
   logo on the same form.

   ```python
   company = env['res.company'].create({
       'name': '<company name>',
       'country_id': env.ref('base.<country code>').id,       # lower-case ISO code, see res.country
       'currency_id': env.ref('base.<currency code>').id,     # ISO code, see res.currency
       'street': '<street>',
       'city': '<city>',
       'email': 'billing@<domain>',
   })
   env.cr.commit()
   ```

   Leaves an active company, allowed to the user who created it, with its currency
   activated if it was inactive.

   - Address, VAT and email live on the company's partner; the company fields write
     through to it.
   - From 18.0, with Accounting installed, a company created with a country (or given
     one when it had none) gets that country's localization modules installed at once,
     and its chart of accounts loaded at commit, when the country has its own chart.
     Installing a module cannot be rolled back: ask before creating the company. Up to
     17.0 the chart is step 4.
   - Fiscal year end is on the company: `fiscalyear_last_day`, `fiscalyear_last_month`
     (`'12'` for December).

2. **Give users access to it.** Settings ‣ Users & Companies ‣ Users ‣ the user, fields
   Companies and Default Company.

   ```python
   user = env['res.users'].search([('login', '=', 'maria@example.com')])
   user.write({'company_ids': [(4, company.id)], 'company_id': company.id})
   env.cr.commit()
   ```

   Leaves the user able to work in the company, and landing in it at login.

   - `company_ids` are the companies the user may work in; `company_id` is the one they
     land in, and must be among the allowed.
   - A user with more than one company gets the multi-company group
     (`base.group_multi_company`) on their own, and the company switcher appears.
   - In the web client the user sees the records of the companies ticked in the
     switcher, not of all allowed ones.
   - Groups and access rights: `users-and-access.md`.

3. **Set the document layout.** Settings ‣ Companies section ‣ Configure Document
   Layout, with the company selected in the switcher. Logo, layout and footer:
   `reports-and-layout.md`.

4. **Verify the fiscal localization package (the chart of accounts).** Invoicing ‣
   Configuration ‣ Settings ‣ Fiscal Localization ‣ Package, with the company selected
   in the switcher, then Save. The chart comes from the country's localization module
   (`l10n_<country code>`, see `odoo-reference/addons.md`); which chart and what it
   contains is for the country's localization to decide; see its localization skill if
   installed. Ask before loading: on a company without journal entries, loading a
   different chart through the setting deletes the accounts, taxes and journals already
   there.

   17.0 and later: templates have a code. List them, then save the setting for that
   company:

   ```python
   Chart = env['account.chart.template']
   print({code: t['name'] for code, t in Chart._get_chart_template_mapping().items()})
   code = Chart._guess_chart_template(company.country_id)      # the country's default code
   env['res.config.settings'].with_company(company).create({'chart_template': code}).execute()
   env.cr.commit()
   ```

   The setting calls `Chart.try_loading(code, company)`, which installs the localization
   module when it is missing (which cannot be rolled back). It only loads for the
   company the settings run in: keep `with_company(company)`.

   16.0: the Package field lists the charts of installed modules only. Install the
   localization first (Apps, or `odoo-bin -d <db> -i l10n_<country code> --stop-after-init`),
   then, in a new shell, list the template records and save the setting:

   ```python
   print(env['account.chart.template'].search([]).mapped(lambda t: (t.id, t.name, t.country_id.code)))
   template = env['account.chart.template'].browse(<template id>)
   env['res.config.settings'].with_company(company).create({'chart_template_id': template.id}).execute()
   env.cr.commit()
   ```

   `l10n_generic_coa.configurable_chart_template` is the generic one.

   Leaves the company with its accounts, taxes, journals and fiscal positions, and with
   the currency the chart sets (the generic chart sets USD): read the currency again. Then
   adjust what came with the chart: `taxes-and-journals.md`,
   `payment-terms-and-fiscal-positions.md`, `currencies-and-rates.md`.

5. **Add branches (17.0 and later).** Settings ‣ Users & Companies ‣ Companies ‣ the
   parent company ‣ Branches tab ‣ Add a line. Create the parent first: a company
   created as a parent cannot become a branch later.

   ```python
   branch = env['res.company'].create({'name': '<branch name>', 'parent_id': company.id})
   env.cr.commit()
   ```

   Leaves a branch that takes the parent's currency and fiscal year end, gets the
   parent's chart of accounts loaded at commit, and can use the parent's taxes. Everything else
   (pricelists, warehouses, loyalty) is set per branch.

## Variations

- **Branch or company.** Branches for establishments of one legal entity (offices, shops
  with their own journals); separate companies for separate legal entities, and for any
  entity in another country: a branch always follows the parent's localization.
- **Loading the chart from a script.** `try_loading` without the setting, for a company
  other than the current one:
  `Chart.try_loading(code, company, install_demo=False)` (17.0+), or
  `template.try_loading(company, install_demo=False)` (16.0). In 16.0 `try_loading` does
  nothing when the company already has a chart (`chart_template_id`) or entries; the
  16.0 setting replaces a chart without entries and refuses with entries.
- **Records shared or per company.** A record with `company_id` empty is shared by all
  companies (partners and products by default). Set `company_id` to restrict it to one.
  Taxes, journals, fiscal positions and payment terms with a company belong to it: a
  document of company A cannot use those of company B. Accounts carry `company_id` up to
  17.0 and `company_ids` from 18.0 (one account can serve several companies).
- **Company-dependent fields.** A partner's payment terms, receivable account, fiscal
  position and pricelist, and a product's income and expense accounts, hold one value
  per company. Write them with `with_company()`:

  ```python
  partner = env['res.partner'].search([('name', '=', '<partner name>')], limit=1)
  partner.with_company(company).write({
      'property_payment_term_id': env.ref('account.account_payment_term_30days').id,
  })
  env.cr.commit()
  ```

- **A second currency.** Invoicing ‣ Configuration ‣ Accounting ‣ Currencies, toggle Active:

  ```python
  env.ref('base.<currency code>').active = True     # ISO code, see res.currency
  env.cr.commit()
  ```

  Activating a second currency turns on the multi-currency group
  (`base.group_multi_currency`) by itself. Rates and their automatic update:
  `currencies-and-rates.md`.
- **Archiving a company.** Settings ‣ Companies section ‣ Manage Companies, select it,
  Actions ‣ Archive; `company.active = False` does the same. Its records stay.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Companies | Settings ‣ Users & Companies ‣ Companies | same | same | same | same |
| Users | Settings ‣ Users & Companies ‣ Users | same | same | same | same |
| Fiscal Localization | Invoicing ‣ Configuration ‣ Settings | same | same | same | same |
| Chart template | record; `chart_template_id` on company and setting | code; `chart_template` | same as 17.0 | same as 17.0 | same as 17.0 |
| Setting with a chart already loaded, no entries | replaces it | replaces it | replaces it | replaces it | replaces it |
| `try_loading` with a chart already loaded | does nothing | adds on top | adds on top | adds on top | adds on top |
| Localization installed when a company gets a country | no | no | yes | yes | yes |
| Branches (`parent_id`) | only arranges the list | branches | branches | branches | branches |
| Accounts per company | `company_id` | `company_id` | `company_ids` | `company_ids` | `company_ids` |

The menu root is Invoicing with Community's `account`, and Accounting when the
Enterprise accounting app is installed; Odoo's documentation writes Accounting.

## Verify

```python
print(company.name, company.country_id.code, company.currency_id.name, company.parent_id.name,
      company.chart_template if 'chart_template' in company else company.chart_template_id.name)
print(env['account.journal'].search_count([('company_id', '=', company.id)]),
      env['account.tax'].search_count([('company_id', '=', company.id)]))
print(env['res.users'].search([('company_ids', 'in', company.ids)]).mapped('login'))
```

Then select the company in the switcher and create a draft invoice.

## Pitfalls

- **A chart over a used company.** A company with journal entries keeps its chart: say
  so and stop. In 17.0 and later `try_loading` does not refuse; it adds the other
  chart's records on top of the old ones. Missing accounts are added one by one
  (`taxes-and-journals.md`), never by reloading.
- **The setting loads for the current company only.** Without `with_company(company)`
  the chart goes to the user's current company, or nowhere.
- **The chart changes the company currency.** Loading a chart writes the currency it
  defines on the company (the generic chart: USD, whatever the company had). Read it
  after loading and correct it before the first entry.
- **The company currency is fixed by the first entry.** It cannot change once the
  company has journal items: choose it at creation.
- **Modules cannot be rolled back.** From 18.0 giving a company a country can install a
  localization; the chart setting installs a missing module. Ask before both.
- **A parent cannot become a branch.** Decide the structure before creating companies.
- **Archiving refused.** Odoo refuses while it is the default company of active users:
  move them first, and remove it from their `company_ids`.
