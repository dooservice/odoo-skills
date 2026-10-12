# l10n_mm — Myanmar - Accounting

Depends on: account_qr_code_emv, l10n_account_withholding_tax.

## `res.partner.bank` (extends)

- `proxy_type` Selection
- `l10n_mm_terminal_id` Char “Terminal ID”
- `l10n_mm_merchant_name` Char “Merchant Name (Myanmar Unicode)”
- `l10n_mm_merchant_city` Char “Merchant City (Myanmar Unicode)”

Extension points: `_check_for_qr_code_errors`, `_check_mm_proxy`, `_get_additional_data_field`, `_get_emv_qr_code_names`, `_get_error_messages_for_qr`, `_get_merchant_account_info`, `_get_qr_code_vals_list`

## `account.chart.template` (extends)


Extension points: `_get_mm_account_account`, `_get_mm_account_journal`, `_get_mm_res_company`, `_get_mm_template_data`
