# l10n_ec — Ecuadorian Accounting

Depends on: base, base_iban, account_debit_note, l10n_latam_invoice_document, l10n_latam_base, account.

## `account.chart.template` (extends)


Extension points: `_get_demo_data_move`

## `account.journal` (extends)

- `l10n_ec_require_emission` Boolean “Require Emission” (compute=_compute_l10n_ec_require_emission)
- `l10n_ec_entity` Char “Emission Entity”
- `l10n_ec_emission` Char “Emission Point”
- `l10n_ec_emission_address_id` Many2one → `res.partner` “Emission address”

## `account.move` (extends)

- `l10n_ec_sri_payment_id` Many2one → `l10n_ec.sri.payment` “Payment Method (SRI)”

Extension points: `_get_ec_formatted_sequence`, `_get_l10n_ec_documents_allowed`, `_get_l10n_latam_documents_domain`, `_get_last_sequence_domain`, `_get_starting_sequence`

## `account.tax` (extends)

- `l10n_ec_code_base` Char “Code base”
- `l10n_ec_code_applied` Char “Code applied”
- `l10n_ec_code_ats` Char “Code ATS”

## `account.tax.group` (extends)

- `l10n_ec_type` Selection “Type Ecuadorian Tax”

## `l10n_ec.sri.payment` (defines)

SRI Payment Method

- `name` Char “Name”
- `code` Char “Code”
- `active` Boolean “Active”

## `l10n_latam.document.type` (extends)

- `internal_type` Selection
- `l10n_ec_check_format` Boolean “Check Number Format EC”

## `res.company` (extends)


## `res.partner` (extends)

- `l10n_ec_vat_validation` Char “VAT Error message validation” (compute=_compute_l10n_ec_vat_validation)

Public methods: `check_vat`

## `account.chart.template` (extends)


Extension points: `_get_ec_account_journal`, `_get_ec_res_company`, `_get_ec_template_data`, `_post_load_data`
