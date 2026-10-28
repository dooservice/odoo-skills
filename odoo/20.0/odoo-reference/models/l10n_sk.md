# l10n_sk — Slovak - Accounting

Depends on: account.

## `account.move` (extends)


## `res.partner.bank` (extends)


Extension points: `_check_for_qr_code_errors`, `_get_available_qr_methods`, `_get_error_messages_for_qr`, `_get_qr_code_generation_params`, `_get_qr_vals`

## `res.company` (extends)

- `trade_registry` Char
- `income_tax_id` Char “Income Tax ID”

## `base.document.layout` (extends)

- `account_fiscal_country_id` Many2one (related=company_id.account_fiscal_country_id)
- `income_tax_id` Char (related=company_id.income_tax_id)

## `res.partner` (extends)

- `additional_identifiers` Json

## `account.chart.template` (extends)


Extension points: `_get_sk_account_account`, `_get_sk_res_company`, `_get_sk_template_data`
