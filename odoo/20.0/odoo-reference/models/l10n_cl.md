# l10n_cl — Chile - Accounting

Depends on: contacts, l10n_latam_invoice_document, uom, account.

## `account.chart.template` (extends)


Extension points: `_get_demo_data_move`, `_post_load_demo_data`

## `account.move` (extends)

- `partner_id_vat` Char “VAT No” (related=partner_id.vat)

Extension points: `_check_document_types_post`, `_check_l10n_latam_document_number_is_numeric`, `_get_l10n_latam_documents_domain`, `_get_last_sequence_domain`, `_get_name_invoice_report`, `_get_starting_sequence`

## `account.move.line` (extends)


## `account.tax` (extends)

- `l10n_cl_sii_code` Integer “SII Code”

## `l10n_latam.document.type` (extends)

- `internal_type` Selection
- `l10n_cl_active` Boolean “Active in localization”

## `res.company` (extends)

- `l10n_cl_activity_description` Char “Company Activity Description” (related=partner_id.l10n_cl_activity_description)

## `res.country` (extends)

- `l10n_cl_customs_code` Char “Customs Code”
- `l10n_cl_customs_name` Char “Customs Name”
- `l10n_cl_customs_abbreviation` Char “Customs Abbreviation”

## `res.currency` (extends)

- `l10n_cl_currency_code` Char “Currency Code”
- `l10n_cl_short_name` Char “Short Name”

## `res.partner` (extends)

- `l10n_cl_sii_taxpayer_type` Selection “Taxpayer Type”
- `l10n_cl_activity_description` Char “Activity Description”

Extension points: `_get_all_additional_identifiers_metadata`

## `account.chart.template` (extends)


Extension points: `_get_cl_account_account`, `_get_cl_account_journal`, `_get_cl_res_company`, `_get_cl_template_data`

## `uom.uom` (extends)

- `l10n_cl_sii_code` Char “SII Code”
