# pos_safaricom — POS Safaricom

Depends on: point_of_sale.

## `pos.payment.method` (extends)

- `consumer_key` Char “Consumer Key”
- `consumer_secret` Char “Consumer Secret”
- `business_short_code` Char “Business Short Code”
- `passkey` Char “Passkey”
- `safaricom_test_mode` Boolean “Test Mode”
- `safaricom_payment_type` Selection “Payment Type”

Public methods: `create`, `generate_qr_code`, `lipa_na_mpesa_register_urls`, `mark_transaction_used`, `mpesa_express_send_payment_request`

Extension points: `_check_business_short_code`, `_create_payment_transaction`, `_get_bearer_token`, `_get_business_shortcode`, `_get_express_stkpush_endpoint`, `_get_lipa_na_mpesa_register_endpoint`, `_get_oauth_endpoint`, `_get_password`, `_get_payment_terminal_selection`, `_get_qr_code_endpoint`, `_get_till_number`, `_get_transaction_type`

## `transaction.lipa.na.mpesa` (defines)

Transaction Lipa na M-PESA

- `trans_id` Char “Transaction ID”
- `name` Char “Name”
- `amount` Integer “Amount”
- `number` Char “Number”
- `received_at` Datetime “Received At”
