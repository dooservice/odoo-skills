# base_vat — VAT Number Validation

Depends on: account.

## `res.company` (extends)

- `vat_check_vies` Boolean “Verify VAT Numbers”

## `res.config.settings` (extends)

- `vat_check_vies` Boolean “Verify VAT Numbers” (related=company_id.vat_check_vies)

## `res.country` (extends)

- `has_foreign_fiscal_position` Boolean (compute=_compute_has_foreign_fiscal_position)

## `res.partner` (extends)

- `vies_valid` Boolean “Intra-Community Valid” (store, compute=_compute_vies_valid)
- `perform_vies_validation` Boolean (compute=_compute_perform_vies_validation)
- `country_id` Many2one (store)
- `vat` Char (store)

Public methods: `check_vat_al`, `check_vat_br`, `check_vat_ch`, `check_vat_cr`, `check_vat_de`, `check_vat_do`, `check_vat_ec`, `check_vat_gr`, `check_vat_gt`, `check_vat_hu`, `check_vat_id`, `check_vat_ie`, `check_vat_il`, `check_vat_in`, `check_vat_jp`, `check_vat_ma`, `check_vat_mx`, `check_vat_no`, `check_vat_pe`, `check_vat_ph`, `check_vat_ro`, `check_vat_rs`, `check_vat_ru`, `check_vat_sa`, `check_vat_th`, `check_vat_tr`, `check_vat_tw`, `check_vat_ua`, `check_vat_uy`, `check_vat_uz`, `check_vat_ve`, `check_vat_vn`, `create`, `format_vat_al`, `format_vat_ch`, `format_vat_cl`, `format_vat_co`, `format_vat_eu`, `format_vat_hu`, `format_vat_is`, `format_vat_sm`, `format_vat_vn`, `is_valid_ruc_ec`, `write`

Extension points: `_check_vat_number`, `_check_vies_iap`, `_check_vies_update_iap`, `_create_contact_parent_company`, `_get_country_specific_vat_variants`, `_get_iap_vies_credentials`, `_get_iap_vies_endpoint`, `_get_vat_required_valid`, `_get_vat_validation_method`
