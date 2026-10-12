# account_qr_code_emv — account_qr_code_emv

Depends on: account.

## `res.partner.bank` (extends)

- `display_qr_setting` Boolean (compute=_compute_display_qr_setting)
- `include_reference` Boolean “Include Reference”
- `proxy_type` Selection “Proxy Type”
- `country_proxy_keys` Char (compute=_compute_country_proxy_keys)
- `proxy_value` Char “Proxy Value”

Extension points: `_check_for_qr_code_errors`, `_get_additional_data_field`, `_get_available_qr_methods`, `_get_crc16`, `_get_error_messages_for_qr`, `_get_merchant_account_info`, `_get_merchant_category_code`, `_get_qr_code_generation_params`, `_get_qr_code_vals_list`, `_get_qr_vals`
