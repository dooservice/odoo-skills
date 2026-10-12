# l10n_ke — Kenya - Accounting

Depends on: account.

## `account.move` (extends)

- `l10n_ke_wh_certificate_number` Char “Withholding Certificate Number”
- `l10n_ke_wh_certificate_date` Date “Date of Certificate”

## `account.tax` (extends)

- `l10n_ke_item_code_id` Many2one → `l10n_ke.item.code` “KRA Item Code”

## `l10n_ke.item.code` (defines)

KRA defined codes that justify a given tax rate / exemption

- `code` Char “KRA Item Code”
- `description` Char “Description”
- `tax_rate` Selection

## `res.company` (extends)

- `l10n_ke_oscu_is_active` Boolean “Is OSCU active?” (compute=_compute_l10n_ke_oscu_is_active)

## `account.chart.template` (extends)


Extension points: `_get_ke_res_company`, `_get_ke_template_data`
