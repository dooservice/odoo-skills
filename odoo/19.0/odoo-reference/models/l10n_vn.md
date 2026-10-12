# l10n_vn — Vietnam - Accounting

Depends on: account_qr_code_emv, base_iban, account.

## `account.move` (extends)

- `l10n_vn_e_invoice_number` Char “eInvoice Number”

## `res.partner.bank` (extends)

- `proxy_type` Selection

Extension points: `_check_for_qr_code_errors`, `_check_vn_proxy`, `_get_additional_data_field`, `_get_error_messages_for_qr`, `_get_merchant_account_info`, `_get_qr_code_vals_list`

## `account.chart.template` (extends)


Extension points: `_get_vn_account_account`, `_get_vn_account_journal`, `_get_vn_res_company`, `_get_vn_template_data`
