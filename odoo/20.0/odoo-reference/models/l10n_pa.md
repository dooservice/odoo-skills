# l10n_pa — Panama - Accounting

Depends on: account, base_address_extended, contacts, l10n_latam_invoice_document.

## `account.chart.template` (extends)


Extension points: `_get_demo_data_move`, `_post_load_demo_data`

## `res.city` (extends)

- `l10n_pa_code` Char “DGI Code”

## `l10n_pa.res.city.corregimiento` (defines)

Corregimiento

- `name` Char (required)
- `city_id` Many2one → `res.city` “District” (required)
- `l10n_pa_code` Char “DGI Code” (required)

## `res.company` (extends)

- `l10n_pa_corregimiento` Many2one (related=partner_id.l10n_pa_corregimiento)
- `l10n_pa_dv` Char (related=partner_id.l10n_pa_dv)

## `res.partner` (extends)

- `l10n_pa_corregimiento` Many2one → `l10n_pa.res.city.corregimiento` “Corregimiento”
- `l10n_pa_corregimiento_name` Char “Corregimiento name” (related=l10n_pa_corregimiento.name)
- `l10n_pa_dv` Char “DV”

Extension points: `_get_all_additional_identifiers_metadata`

## `account.chart.template` (extends)


Extension points: `_get_pa_account_account`, `_get_pa_res_company`, `_get_pa_template_data`
