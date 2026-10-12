# base_vat — VAT Number Validation

Depends on: account.

## `account.fiscal.position` (extends)


Public methods: `adjust_vals_country_id`, `create`, `raise_vat_error_message`, `write`

## `res.company` (extends)

- `vat_check_vies` Boolean “Verify VAT Numbers”

## `res.config.settings` (extends)

- `vat_check_vies` Boolean “Verify VAT Numbers” (related=company_id.vat_check_vies)

## `res.partner` (extends)

- `vies_failed_message` Char “Technical field display a message to the user if the VIES check fails.”

Public methods: `check_vat`, `check_vat_al`, `check_vat_au`, `check_vat_br`, `check_vat_ch`, `check_vat_cr`, `check_vat_de`, `check_vat_ec`, `check_vat_hu`, `check_vat_id`, `check_vat_ie`, `check_vat_il`, `check_vat_in`, `check_vat_mx`, `check_vat_nl`, `check_vat_no`, `check_vat_nz`, `check_vat_pe`, `check_vat_ph`, `check_vat_ru`, `check_vat_sa`, `check_vat_t`, `check_vat_tr`, `check_vat_tw`, `check_vat_ua`, `check_vat_uy`, `check_vat_ve`, `check_vat_vn`, `check_vat_xi`, `create`, `fix_eu_vat_number`, `format_vat_ch`, `format_vat_eu`, `format_vat_sm`, `is_valid_ruc_ec`, `simple_vat_check`, `vies_vat_check`, `write`

Extension points: `_check_vies`
