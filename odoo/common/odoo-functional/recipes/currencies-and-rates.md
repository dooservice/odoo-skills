# Currencies and rates

Every company has one currency (`company.currency_id`), the one its books are kept in.
Other currencies (`res.currency`) are inactive until needed. A document in another
currency is converted with the rate (`res.currency.rate`) in force at its date for that
company: the most recent one before it, or the oldest one when none is older. It needs
`account` (Invoicing). Automatic rates (`currency_rate_live`) are Enterprise and only
pointed to. Wrong rates give wrong journal entries, so read the direction twice before
writing one.

## Before you start

- Apps: `account`.
- Settings: `group_multi_currency` turns on by itself with a second active currency.
- Read first:

```python
company = env.company
company.currency_id.name
env['res.currency'].with_context(active_test=False).search_read([('name', 'in', ['<currency code>'])], ['name', 'active', 'rounding', 'decimal_places'])
foreign = env.ref('base.<currency code>')
env['res.currency.rate'].search_read([('currency_id', '=', foreign.id), ('company_id', 'in', [company.id, False])], ['name', 'company_id', 'rate', 'company_rate', 'inverse_company_rate'], order='name desc', limit=5)
```

A currency's XML id is `base.` followed by its ISO code in capitals (`name`); look it up
with `env['res.currency'].with_context(active_test=False).search([('full_name', 'ilike', '<currency name>')]).mapped('name')`.

## The standard flow

Odoo's order: check the main currency, activate the foreign ones, give them rates (by
hand or automatically), then check the exchange difference accounts and the journals in
that currency.

1. **Check the main currency.** Invoicing ‣ Configuration ‣ Settings ‣ Currencies ‣ Main
   Currency (the setting `currency_id`, the company's `currency_id`).

   ```python
   env['res.config.settings'].with_company(company).create({'currency_id': env.ref('base.<currency code>').id}).execute()
   env.cr.commit()
   ```

   Leaves the company's books in that currency. It is chosen before the first entry:
   once journal items exist, Odoo refuses to change it (`You cannot change the currency
   of the company since some journal items already exist`), and a different currency
   then means a new company.

2. **Activate the foreign currency.** Invoicing ‣ Configuration ‣ Accounting ‣ Currencies, toggle
   Active.

   ```python
   env.ref('base.<currency code>').write({'active': True})
   env.cr.commit()
   ```

   Leaves the currency selectable on documents, journals and pricelists.

   - Activating a second currency turns on the multi-currency group
     (`base.group_multi_currency`) by itself; deactivating back to one turns it off. The
     setting `group_multi_currency` does the same. True from 16.0 to 20.0.
   - Do not deactivate a currency used by journals, pricelists or open documents.

3. **Enter a rate.** Invoicing ‣ Configuration ‣ Accounting ‣ Currencies ‣ the currency ‣ Rates tab ‣
   Add a line.

   ```python
   env['res.currency.rate'].create({
       'currency_id': env.ref('base.<currency code>').id,
       'company_id': company.id,
       'name': '2026-10-20',
       'inverse_company_rate': 18.45,
   })
   env.cr.commit()
   ```

   Leaves a rate that reads "1 unit of the foreign currency = 18.45 units of the company
   currency" from that date. Three fields say the same thing in different directions;
   write one:

   - `inverse_company_rate`: company currency per 1 unit of the foreign currency (the
     18.45 above). The way banks publish most rates; the safest to write.
   - `company_rate`: foreign currency per 1 unit of company currency
     (1 / 18.45 = 0.0542).
   - `rate`: the stored technical value, relative to the currency whose rate is 1,
     normally the company currency. Do not write it unless the user gives rates that
     way.
   - `name` is the date. One rate per currency, company and day: update the existing one
     instead of creating a second.
   - `company_id`: 16.0 defaults to the current company; from 17.0 on to the root
     company, whose rates its branches share. A rate without company applies to every
     company that has none of its own; a company's own rates win over it, even older
     ones.

   Check a conversion after writing, with `today` a `datetime.date`:

   ```python
   foreign._convert(100.0, company.currency_id, company, today)
   ```

   Rates on past dates change nothing already posted; they apply to entries created or
   reconverted afterwards.

4. **Check the exchange difference accounts.** Invoicing ‣ Configuration ‣ Settings ‣
   Default Accounts: Journal, Gain and Loss accounts.

   ```python
   settings = env['res.config.settings'].with_company(company).create({})
   print(settings.currency_exchange_journal_id.name, settings.income_currency_exchange_account_id.code, settings.expense_currency_exchange_account_id.code)
   ```

   Payments at a rate different from the invoice's book a difference on the company's
   `income_currency_exchange_account_id` / `expense_currency_exchange_account_id`, in
   `currency_exchange_journal_id`. The chart of accounts sets them; check they are set
   before the first payment in a foreign currency, and set them through the same
   setting fields when they are not.

5. **Set the currency on a journal.** Invoicing ‣ Configuration ‣ Accounting ‣ Journals ‣ the journal
   ‣ Currency. A bank account in a foreign currency is a bank journal with its
   `currency_id`, and that journal only handles that currency: see
   `taxes-and-journals.md`.

## Variations

- **Automatic rates.** Once a second currency is active, Invoicing ‣ Configuration ‣
  Settings ‣ Currencies shows Automatic Currency Rates: the setting
  `module_currency_rate_live` installs `currency_rate_live`, which fetches rates from an
  online provider on a schedule. It is an Odoo Enterprise module: in Community the
  setting shows as an upgrade. Its provider and interval fields are not in the
  Community sources, so do not write them from memory: after installing, list them with
  `env['res.config.settings'].fields_get()` (names starting with `currency_`) and show
  the user the choices before writing.
- **Cash rounding.** Rounding the total to coins (0.05): the setting
  `group_cash_rounding`, then an `account.cash.rounding` (the Cash Roundings menu, see
  `## Versions`) with `rounding`, `strategy` (`biggest_tax` or `add_invoice_line`) and
  `rounding_method` (`UP`, `DOWN`, `HALF-UP`).
- **Currency rounding.** `rounding` on the currency (0.01 for currencies with cents, 1.0
  for those without) drives every amount; `decimal_places` is computed from it. Change
  it only with the user's yes and never on a currency with posted entries.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Currencies | Invoicing ‣ Configuration ‣ Accounting ‣ Currencies | same | same | same | same |
| Main Currency, Default Accounts | Invoicing ‣ Configuration ‣ Settings | same | same | same | same |
| Cash roundings | Invoicing ‣ Configuration ‣ Management ‣ Cash Roundings | same as 16.0 | same as 16.0 | Invoicing ‣ Configuration ‣ Accounting ‣ Cash Roundings | Invoicing ‣ Configuration ‣ Accounting ‣ Rounding Methods |
| Default `company_id` of a rate | current company | root company | root company | root company | root company |

The fields of `res.currency.rate` and the multi-currency group behave the same from 16.0
to 20.0. The Cash Roundings menu shows only with `group_cash_rounding`. The menu root is
Invoicing in Community and Accounting with the Enterprise accounting app.

## Verify

```python
import datetime
today = datetime.date.today()
print(foreign.active, env.user.has_group('base.group_multi_currency'))
print(foreign._convert(100.0, company.currency_id, company, today))
print(env['res.currency.rate'].search_read([('currency_id', '=', foreign.id), ('company_id', 'in', [company.id, False])], ['name', 'company_id', 'inverse_company_rate'], order='name desc', limit=1))
```

## Pitfalls

- **The rate written backwards.** `company_rate` and `inverse_company_rate` are each
  other's inverse: a rate entered in the wrong field converts 100 into 5.42 instead of
  1845. Convert one amount after writing.
- **Two rates on one day.** One rate per currency, company and day: update the existing
  one.
- **A shared rate that does not apply.** A company with rates of its own ignores the
  rates without company, even newer ones.
- **The company currency after the first entry.** It cannot change: a new company is
  the only way.
- **Exchange accounts not checked.** A chart that does not set them leaves exchange
  differences without their accounts: read them (step 4) before the first payment in a
  foreign currency.
