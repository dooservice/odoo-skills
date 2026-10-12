# l10n_sk — Slovak - Accounting

Depends on: base_iban, base_vat, account.

## `account.move` (extends)

- `taxable_supply_date` Date

## `res.company` (extends)

- `trade_registry` Char
- `income_tax_id` Char “Income Tax ID”

## `base.document.layout` (extends)

- `account_fiscal_country_id` Many2one (related=company_id.account_fiscal_country_id)
- `company_registry` Char (related=company_id.company_registry)
- `income_tax_id` Char (related=company_id.income_tax_id)

## `account.chart.template` (extends)


Extension points: `_get_sk_res_company`, `_get_sk_template_data`
