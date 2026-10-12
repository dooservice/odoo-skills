# l10n_id — Indonesian - Accounting

Depends on: account, base_iban, base_vat.

## `account.move` (extends)

- `l10n_id_qris_transaction_ids` Many2many → `l10n_id.qris.transaction`

Public methods: `action_l10n_id_update_payment_status`

## `l10n_id.qris.transaction` (defines)

Record of QRIS transactions

- `model` Char “Model”
- `model_id` Char “Model ID”
- `qris_invoice_id` Char (readonly)
- `qris_amount` Integer (readonly)
- `qris_content` Char (readonly)
- `qris_creation_datetime` Datetime (readonly)
- `bank_id` Many2one → `res.partner.bank`
- `paid` Boolean

Extension points: `_get_latest_transaction`, `_get_record`, `_get_supported_models`

## `res.partner.bank` (extends)

- `l10n_id_qris_api_key` Char “QRIS API Key”
- `l10n_id_qris_mid` Char “QRIS Merchant ID”

Extension points: `_check_for_qr_code_errors`, `_get_available_qr_methods`, `_get_error_messages_for_qr`, `_get_qr_code_generation_params`, `_get_qr_vals`

## `account.chart.template` (extends)


Extension points: `_get_id_account_account`, `_get_id_account_journal`, `_get_id_res_company`, `_get_id_template_data`
