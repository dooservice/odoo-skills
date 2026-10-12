# l10n_pe — Peru - Accounting

Depends on: base_vat, base_address_extended, l10n_latam_base, l10n_latam_invoice_document, account_debit_note, account.

## `account.chart.template` (extends)


Extension points: `_get_demo_data_move`

## `account.move` (extends)


Extension points: `_get_l10n_latam_documents_domain`

## `account.move.line` (extends)

- `l10n_pe_group_id` Many2one → `account.group` (store, related=account_id.group_id)

Extension points: `_get_rate_date`

## `account.tax` (extends)

- `l10n_pe_edi_tax_code` Selection “Code”
- `l10n_pe_edi_unece_category` Selection “UNECE Code”
- `l10n_pe_edi_isc_type` Selection

## `l10n_latam.identification.type` (extends)

- `l10n_pe_vat_code` Char

## `res.city` (extends)

- `l10n_pe_code` Char “Code”

## `l10n_pe.res.city.district` (defines)

District

- `name` Char
- `city_id` Many2one → `res.city`
- `code` Char

## `res.company` (extends)


## `res.partner` (extends)

- `l10n_pe_district` Many2one → `l10n_pe.res.city.district` “District”
- `l10n_pe_district_name` Char “District name” (related=l10n_pe_district.name)

## `account.chart.template` (extends)


Extension points: `_get_pe_res_company`, `_get_pe_template_data`
