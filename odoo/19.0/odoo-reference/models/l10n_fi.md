# l10n_fi — Finland - Accounting

Depends on: base_iban, base_vat, account, account_edi_ubl_cii.

## `account.journal` (extends)

- `invoice_reference_model` Selection

## `account.move` (extends)


Public methods: `compute_payment_reference_finnish`, `compute_payment_reference_finnish_rf`, `get_finnish_check_digit`, `get_rf_check_digits`, `number2numeric`

Extension points: `_get_invoice_reference_fi_invoice`, `_get_invoice_reference_fi_partner`, `_get_invoice_reference_fi_rf_invoice`, `_get_invoice_reference_fi_rf_partner`

## `res.partner` (extends)


Extension points: `_get_company_registry_labels`

## `account.chart.template` (extends)


Extension points: `_get_fi_account_account`, `_get_fi_res_company`, `_get_fi_template_data`
