# l10n_cl — Chile - Accounting

Depends on: contacts, base_vat, l10n_latam_base, l10n_latam_invoice_document, uom, account.

## `account.chart.template` (extends)


Extension points: `_get_demo_data`, `_get_demo_data_move`

## `account.move` (extends)

- `partner_id_vat` Char “VAT No” (related=partner_id.vat)
- `l10n_latam_internal_type` Selection “L10n Latam Internal Type” (related=l10n_latam_document_type_id.internal_type)

Extension points: `_check_document_types_post`, `_get_l10n_latam_documents_domain`, `_get_last_sequence_domain`, `_get_name_invoice_report`, `_get_starting_sequence`

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

- `l10n_cl_sii_taxpayer_type` Selection
- `l10n_cl_activity_description` Char “Activity Description”

Public methods: `create`, `write`

## `res.bank` (extends)

- `l10n_cl_sbif_code` Char “Cod. SBIF”

## `account.chart.template` (extends)


Extension points: `_get_cl_res_company`, `_get_cl_template_data`

## `uom.uom` (extends)

- `l10n_cl_sii_code` Char “SII Code”
