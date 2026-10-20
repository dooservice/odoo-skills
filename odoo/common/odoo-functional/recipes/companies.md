# Companies, multi-company and the chart of accounts

A company (`res.company`) is a legal entity with its own currency, country, taxes,
journals, accounts and numbering. Most configuration records carry a `company_id`, and a
user sees the records of the companies they are allowed in. The chart of accounts is
loaded per company from the country's localization, once, before the first entry.

Read first:

```python
for c in env['res.company'].search([]):
    print(c.id, c.name, c.country_id.code, c.currency_id.name, c.parent_id.name,
          c.chart_template if 'chart_template' in c else c.chart_template_id.name)   # 17.0+ / 16.0
print(env['account.move'].search_count([('state', '=', 'posted')]))
```

## A new company

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

- Creating a company gives it to the user who creates it, and activates its currency if
  it was inactive.
- From 18.0, with Accounting installed, a company created with a country (or given one
  when it had none) gets that country's localization modules installed at once, and its
  chart of accounts loaded at commit, when the country has its own chart. Installing a
  module cannot be rolled back: ask before creating the company. Up to 17.0, load the
  chart yourself (below).
- Address, VAT and email live on the company's partner; the company fields write
  through to it.
- Logo, document layout and footer: see `reports-and-layout.md`.
- Fiscal year end is on the company: `fiscalyear_last_day`, `fiscalyear_last_month`
  (`'12'` for December).

## Branches (17.0 and later)

A branch is a company with `parent_id` set. It takes the parent's currency and fiscal
year end, gets the parent's chart of accounts loaded, and can use the parent's taxes.
Use branches for establishments of one legal entity (offices, shops with their own
journals); use separate companies for separate legal entities.

```python
branch = env['res.company'].create({'name': '<branch name>', 'parent_id': company.id})
env.cr.commit()
```

In 16.0 `parent_id` exists but only arranges the company list; each company is
configured on its own.

## Users and companies

```python
user = env['res.users'].search([('login', '=', 'maria@example.com')])
user.write({'company_ids': [(4, company.id)], 'company_id': company.id})
env.cr.commit()
```

- `company_ids` are the companies the user may work in; `company_id` is the one they
  land in, and must be among the allowed.
- A user with more than one company gets the multi-company group
  (`base.group_multi_company`) on their own, and the company switcher appears.
- In the web client the user sees the records of the companies ticked in the switcher,
  not of all allowed ones.

## Records shared or per company

- A record with `company_id` empty is shared by all companies (partners and products by
  default). Set `company_id` to restrict it to one.
- Taxes, journals, fiscal positions and payment terms with a company belong to it. A
  document of company A cannot use those of company B.
- Accounts carry `company_id` up to 17.0 and `company_ids` from 18.0 (one account can
  serve several companies).
- Company-dependent fields (a partner's payment terms, receivable account, fiscal
  position and pricelist; a product's income and expense accounts) hold one value per
  company. Write them with `with_company()`:

```python
partner = env['res.partner'].search([('name', '=', '<partner name>')], limit=1)
partner.with_company(company).write({
    'property_payment_term_id': env.ref('account.account_payment_term_30days').id,
})
env.cr.commit()
```

## Currencies

```python
env.ref('base.<currency code>').active = True     # ISO code, see res.currency
env.cr.commit()
```

Activating a second currency turns on the multi-currency group
(`base.group_multi_currency`) by itself. Rates and their automatic update: see
`currencies-and-rates.md`. The company currency cannot change once the company has
journal items.

## Chart of accounts

The chart comes from the country's localization module (`l10n_<country code>`, see
`odoo-reference/addons.md`) and is loaded on a company with no journal entries. Which
chart and what it contains is for the country's localization to decide; see its
localization skill if installed. Ask before loading: in 17.0 and later, on a company
without journal entries, loading a different chart deletes the accounts, taxes and
journals already there.

17.0 and later: templates have a code. List them, then load one:

```python
Chart = env['account.chart.template']
print({code: t['name'] for code, t in Chart._get_chart_template_mapping().items()})
code = Chart._guess_chart_template(company.country_id)      # the country's default code
Chart.try_loading(code, company, install_demo=False)          # or another code from the list
env.cr.commit()
```

`try_loading` installs the localization module when it is missing (which cannot be
rolled back). The setting does the same:
`env['res.config.settings'].with_company(company).create({'chart_template': code}).execute()`.

16.0: install the localization first (Apps, or `odoo-bin -d <db> -i l10n_<country code> --stop-after-init`),
then, in a new shell, list the template records and load one:

```python
print(env['account.chart.template'].search([]).mapped(lambda t: (t.id, t.name, t.country_id.code)))
template = env['account.chart.template'].browse(<template id>)
template.try_loading(company, install_demo=False)
env.cr.commit()
```

`l10n_generic_coa.configurable_chart_template` is the generic one. 16.0 does nothing
when the company already has a chart (`chart_template_id`) or entries.

A company with journal entries keeps its chart: say so and stop. In 17.0 and later
`try_loading` does not refuse; it adds the other chart's records on top of the old
ones. Missing accounts are added one by one (`taxes-and-journals.md`), never by
reloading.

## Archiving a company

`company.active = False` hides it; its records stay. Odoo refuses while it is the
default company of active users: move them first, and remove it from their
`company_ids`.

## Versions

- 16.0: chart templates are records (`chart_template_id` on the company); no branches.
- 17.0: templates by code (`chart_template`), `try_loading(code, company)`; branches.
- 18.0: localization and chart installed when a company gets a country; accounts shared
  between companies (`company_ids`).
