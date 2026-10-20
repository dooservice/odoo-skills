# Currencies and rates

Every company has one currency (`company.currency_id`), the one its books are kept in.
Other currencies (`res.currency`) are inactive until needed. A document in another
currency is converted with the rate (`res.currency.rate`) in force at its date for that
company: the most recent one before it, or the oldest one when none is older. Wrong rates give wrong journal entries, so
read the direction twice before writing one.

## Read first

```python
company = env.company
company.currency_id.name
env['res.currency'].with_context(active_test=False).search_read([('name', 'in', ['USD', 'EUR', 'MXN', 'INR'])], ['name', 'active', 'rounding', 'decimal_places'])
usd = env.ref('base.USD')
env['res.currency.rate'].search_read([('currency_id', '=', usd.id), ('company_id', 'in', [company.id, False])], ['name', 'company_id', 'rate', 'company_rate', 'inverse_company_rate'], order='name desc', limit=5)
```

## Activate a currency

```python
env.ref('base.USD').write({'active': True})
env.cr.commit()
```

- Activating a second currency turns on the multi-currency group
  (`base.group_multi_currency`) by itself; deactivating back to one turns it off. The
  setting `group_multi_currency` does the same. True from 16.0 to 20.0.
- Do not deactivate a currency used by journals, pricelists or open documents.

## A rate

```python
env['res.currency.rate'].create({
    'currency_id': env.ref('base.USD').id,
    'company_id': company.id,
    'name': '2026-10-20',
    'inverse_company_rate': 18.45,
})
env.cr.commit()
```

That reads "1 USD = 18.45 MXN" for a company in Mexican pesos. Three fields say the same
thing in different directions; write one:

- `inverse_company_rate`: company currency per 1 unit of the foreign currency (1 USD =
  18.45 MXN, 1 EUR = 89.6 INR). The way banks publish most rates; the safest to write.
- `company_rate`: foreign currency per 1 unit of company currency (1 MXN = 0.0542 USD).
- `rate`: the stored technical value, relative to the currency whose rate is 1,
  normally the company currency. Do not write it unless the user gives rates that way.
- `name` is the date. One rate per currency, company and day: update the existing one
  instead of creating a second.
- `company_id`: 16.0 defaults to the current company; from 17.0 on to the root company,
  whose rates its branches share. A rate without company applies to every company that
  has none of its own.

Check a conversion after writing:

```python
usd._convert(100.0, company.currency_id, company, today)
```

where `today` is a `datetime.date`. Rates on past dates change nothing already posted;
they apply to entries created or reconverted afterwards.

## Automatic rates

The setting `module_currency_rate_live` installs `currency_rate_live`, which fetches
rates from an online provider on a schedule. It is an Odoo Enterprise module: in
Community the setting shows as an upgrade. Its provider and interval fields are not in
the Community sources, so do not write them from memory: after installing, list them
with `env['res.config.settings'].fields_get()` (names starting with `currency_`) and
show the user the choices before writing.

## Main currency

The company currency is chosen before the first entry. Once journal items exist, Odoo
refuses to change it (`You cannot change the currency of the company since some
journal items already exist`). A different currency then means a new company.

## Rounding

- `rounding` on the currency (0.01 for USD and EUR, 1.0 for currencies without cents)
  drives every amount; `decimal_places` is computed from it. Change it only with the
  user's yes and never on a currency with posted entries.
- Rounding the total to coins (0.05) is cash rounding: setting `group_cash_rounding`,
  then an `account.cash.rounding` with `rounding`, `strategy` (`biggest_tax` or
  `add_invoice_line`) and `rounding_method` (`UP`, `DOWN`, `HALF-UP`).

## Exchange differences

Payments at a rate different from the invoice's book a difference on the company's
`income_currency_exchange_account_id` / `expense_currency_exchange_account_id`, in
`currency_exchange_journal_id`. The chart of accounts sets them; check they are set
before the first payment in a foreign currency. A bank account in a foreign currency is
a bank journal with its `currency_id` (see `taxes-and-journals.md`).
