# l10n_cz — Czech - Accounting

Depends on: account, account_edi_ubl_cii, base_iban, base_vat.

## `account.move` (extends)


Extension points: `_get_accounting_date_source`, `_get_invoice_currency_rate_date`

## `l10n_cz.tax_office` (defines)

Tax office in Czech Republic

- `workplace_code` Integer “Territorial Office” (required)
- `code` Integer “Code” (required)
- `name` Char “Name”
- `region` Char “Region” (required)

## `res.company` (extends)

- `trade_registry` Char
- `l10n_cz_tax_office_id` Many2one → `l10n_cz.tax_office` “Tax Office (CZ)”

## `base.document.layout` (extends)

- `account_fiscal_country_id` Many2one (related=company_id.account_fiscal_country_id)
- `company_registry` Char (related=company_id.company_registry)

## `account.chart.template` (extends)


Extension points: `_get_cz_account_account`, `_get_cz_res_company`, `_get_cz_template_data`, `_get_demo_data_move`
