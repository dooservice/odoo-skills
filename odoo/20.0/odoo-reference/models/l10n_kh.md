# l10n_kh — Cambodia - Accounting

Depends on: account_qr_code_emv, l10n_account_withholding_tax.

## `res.partner.bank` (extends)

- `proxy_type` Selection
- `l10n_kh_merchant_id` Char “Merchant ID”

Extension points: `_check_for_qr_code_errors`, `_check_kh_proxy`, `_get_additional_data_field`, `_get_emv_qr_code_names`, `_get_error_messages_for_qr`, `_get_merchant_account_info`, `_get_merchant_category_code`, `_get_qr_code_vals_list`

## `account.chart.template` (extends)


Extension points: `_get_kh_account_journal`, `_get_kh_res_company`, `_get_kh_template_data`
