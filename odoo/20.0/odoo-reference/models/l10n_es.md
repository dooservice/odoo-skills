# l10n_es — Spain - Accounting (PGCE 2008)

Depends on: account, account_edi_ubl_cii.

## `account.move` (extends)

- `l10n_es_original_invoice_credited` Char “Original Invoice Credited”
- `l10n_es_invoice_type_available` Char “Invoice Types Available” (compute=_compute_l10n_es_invoice_type_available)
- `l10n_es_invoice_type` Selection (store, compute=_compute_l10n_es_invoice_type)
- `l10n_es_available_regime_codes` Char “Available VAT Regime Codes” (compute=_compute_l10n_es_available_regime_codes)
- `l10n_es_regime_code` Selection “VAT Regime Code” (store, compute=_compute_l10n_es_regime_code)
- `l10n_es_regime_code_additional` Selection “VAT Regime Code (Additional)” (store, compute=_compute_l10n_es_regime_code)

Public methods: `l10n_es_invoice_type_selection`

## `account.tax` (extends)

- `l10n_es_exempt_reason` Selection “Exempt Reason (Spain)”
- `l10n_es_type` Selection “Tax Type (Spain)”
- `l10n_es_bien_inversion` Boolean “Bien de Inversion”
- `l10n_es_applicability` Selection “Applicability (Spain)”
- `l10n_es_available_regime_codes` Char “Available VAT Regime Codes” (compute=_compute_l10n_es_available_regime_codes)
- `l10n_es_regime_code` Selection “VAT Regime Code” (store, compute=_compute_l10n_es_regime_code)

## `res.company` (extends)

- `l10n_es_simplified_invoice_limit` Float “Simplified Invoice limit amount”
- `l10n_es_special_vat_regime` Selection

Public methods: `write`

## `res.config.settings` (extends)

- `l10n_es_simplified_invoice_limit` Float (related=company_id.l10n_es_simplified_invoice_limit)
- `l10n_es_special_vat_regime` Selection (related=company_id.l10n_es_special_vat_regime)
- `module_l10n_es_edi_verifactu` Boolean “Veri*Factu”
- `module_l10n_es_edi_sii` Boolean “SII”
- `module_l10n_es_edi_tbai` Boolean “TicketBai”

Public methods: `set_values`

## `res.partner` (extends)

- `l10n_es_passport` Char “Passport” (compute=_compute_l10n_es_passport)
- `l10n_es_foreign_id` Char “Country of residence ID document” (compute=_compute_l10n_es_foreign_id)
- `l10n_es_res_cert` Char “Residence certificate” (compute=_compute_l10n_es_res_cert)
- `l10n_es_other_id` Char “Other supporting document” (compute=_compute_l10n_es_other_id)

Extension points: `_get_all_additional_identifiers_metadata`

## `account.chart.template` (extends)


Extension points: `_get_es_assec_res_company`, `_get_es_assec_template_data`

## `account.chart.template` (extends)


Extension points: `_get_es_common_account_account`, `_get_es_common_account_journal`, `_get_es_common_res_company`, `_get_es_common_template_data`, `_post_load_data`

## `account.chart.template` (extends)


Extension points: `_get_es_coop_full_res_company`, `_get_es_coop_full_template_data`

## `account.chart.template` (extends)


Extension points: `_get_es_coop_pymes_res_company`, `_get_es_coop_pymes_template_data`

## `account.chart.template` (extends)


Extension points: `_get_es_full_account_account`, `_get_es_full_res_company`, `_get_es_full_template_data`

## `account.chart.template` (extends)


Extension points: `_get_es_pymes_res_company`, `_get_es_pymes_template_data`
