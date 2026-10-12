# l10n_cz — Czech - Accounting

Depends on: account, account_edi_ubl_cii.

## `account.move` (extends)


Extension points: `_get_accounting_date_source`, `_get_invoice_currency_rate_date`

## `l10n_cz.tax_office` (defines)

Tax office in Czech Republic

- `workplace_code` Integer “Territorial Office” (required)
- `code` Integer “Code” (required)
- `name` Char “Name”
- `region` Char “Region” (required)

## `res.partner.bank` (extends)


Extension points: `_get_available_qr_methods`, `_get_error_messages_for_qr`, `_get_qr_code_generation_params`, `_get_qr_vals`

## `res.company` (extends)

- `trade_registry` Char
- `l10n_cz_tax_office_id` Many2one → `l10n_cz.tax_office` “Tax Office (CZ)”
- `l10n_cz_economic_activity_code` Selection “Economic Activity code”
- `l10n_cz_person_authorized` Many2one → `res.partner`
- `l10n_cz_relationship_person_authorized` Char “Relationship of Authorized Person” (store, compute=_compute_l10n_cz_relationship_person_authorized)

## `base.document.layout` (extends)

- `account_fiscal_country_id` Many2one (related=company_id.account_fiscal_country_id)

## `account.chart.template` (extends)


Extension points: `_get_cz_account_account`, `_get_cz_res_company`, `_get_cz_template_data`, `_get_demo_data_move`
