# l10n_cz — Czech - Accounting

Depends on: account, base_iban, base_vat.

## `account.move` (extends)

- `taxable_supply_date` Date

## `account.move.line` (extends)


Extension points: `_get_rate_date`

## `res.company` (extends)

- `trade_registry` Char

## `base.document.layout` (extends)

- `account_fiscal_country_id` Many2one (related=company_id.account_fiscal_country_id)
- `company_registry` Char (related=company_id.company_registry)

## `account.chart.template` (extends)


Extension points: `_get_cz_res_company`, `_get_cz_template_data`
