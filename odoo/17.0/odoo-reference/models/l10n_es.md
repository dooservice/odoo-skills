# l10n_es — Spain - Accounting (PGCE 2008)

Depends on: account, base_iban, base_vat.

## `account.move` (extends)

- `l10n_es_is_simplified` Boolean “Is Simplified” (store, compute=_compute_l10n_es_is_simplified)

## `account.tax` (extends)

- `l10n_es_exempt_reason` Selection “Exempt Reason (Spain)”
- `l10n_es_type` Selection “Tax Type (Spain)”
- `l10n_es_bien_inversion` Boolean “Bien de Inversion”

## `res.company` (extends)


## `res.partner` (extends)


## `account.chart.template` (extends)


Extension points: `_get_es_assec_res_company`, `_get_es_assec_template_data`

## `account.chart.template` (extends)


Extension points: `_get_es_common_res_company`, `_get_es_common_template_data`, `_get_product`

## `account.chart.template` (extends)


Extension points: `_get_es_coop_full_res_company`, `_get_es_coop_full_template_data`

## `account.chart.template` (extends)


Extension points: `_get_es_coop_pymes_res_company`, `_get_es_coop_pymes_template_data`

## `account.chart.template` (extends)


Extension points: `_get_es_full_res_company`, `_get_es_full_template_data`

## `account.chart.template` (extends)


Extension points: `_get_es_pymes_res_company`, `_get_es_pymes_template_data`
