# pos_safaricom — POS Safaricom

Depends on: point_of_sale.

## `pos.payment` (extends)

- `safaricom_transaction_id` Char “Safaricom transaction id”

## `pos.payment.method` (extends)

- `consumer_key` Char “Consumer Key”
- `consumer_secret` Char “Consumer Secret”
- `business_short_code` Char “Business Short Code”
- `safaricom_till_number` Char “Till number”
- `safaricom_paybill_number` Char “Paybill number”
- `passkey` Char “Passkey”
- `safaricom_test_mode` Boolean “Test Mode”
- `safaricom_payment_type` Selection “Payment Type”
- `safaricom_identifier_type` Selection “Identifier Type”

Public methods: `create`, `generate_qr_code`, `lipa_na_mpesa_register_urls`, `mark_transaction_used`, `mpesa_express_send_payment_request`

Extension points: `_create_payment_transaction`, `_get_bearer_token`, `_get_business_shortcode`, `_get_express_stkpush_endpoint`, `_get_lipa_na_mpesa_register_endpoint`, `_get_oauth_endpoint`, `_get_password`, `_get_qr_code_endpoint`, `_get_terminal_provider_selection`, `_get_till_number`

## `transaction.lipa.na.mpesa` (defines)

Transaction Lipa na M-PESA

- `trans_id` Char “Transaction ID”
- `name` Char “Name”
- `amount` Integer “Amount”
- `number` Char “Number”
- `received_at` Datetime “Received At”

## `pos.order.receipt` (extends)
