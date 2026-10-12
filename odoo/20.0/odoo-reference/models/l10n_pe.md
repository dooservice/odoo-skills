# l10n_pe — Peru - Accounting

Depends on: l10n_latam_invoice_document, account_debit_note, account.

## `account.chart.template` (extends)


Extension points: `_get_demo_data_move`

## `account.move` (extends)


Extension points: `_get_l10n_latam_documents_domain`

## `account.tax` (extends)

- `l10n_pe_edi_tax_code` Selection “Code”
- `l10n_pe_edi_unece_category` Selection “UNECE Code”
- `l10n_pe_edi_isc_type` Selection

## `res.city` (extends)

- `l10n_pe_code` Char “Code”

## `l10n_pe.res.city.district` (defines)

District

- `name` Char
- `city_id` Many2one → `res.city`
- `code` Char

## `res.company` (extends)


## `res.country` (extends)


Extension points: `_get_address_format_fields_mapping`

## `res.partner` (extends)

- `l10n_pe_district` Many2one → `l10n_pe.res.city.district` “District”
- `l10n_pe_district_name` Char “District name” (related=l10n_pe_district.name)
- `l10n_pe_sunat_id_code` Char “PE Identification Type Code” (readonly, store, compute=_compute_l10n_pe_sunat_identification)
- `l10n_pe_sunat_id_value` Char “PE Identification Number” (readonly, store, compute=_compute_l10n_pe_sunat_identification)

Extension points: `_get_all_additional_identifiers_metadata`, `_get_frontend_writable_fields`, `_get_mandatory_address_fields`

## `account.chart.template` (extends)


Extension points: `_get_pe_account_account`, `_get_pe_account_journal`, `_get_pe_res_company`, `_get_pe_template_data`
