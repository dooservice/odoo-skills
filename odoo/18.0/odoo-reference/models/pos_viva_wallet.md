# pos_viva_wallet — POS Viva Wallet

Depends on: point_of_sale.

## `pos.payment.method` (extends)

- `viva_wallet_merchant_id` Char “Merchant ID”
- `viva_wallet_api_key` Char “API Key”
- `viva_wallet_client_id` Char “Client ID”
- `viva_wallet_client_secret` Char “Client secret”
- `viva_wallet_terminal_id` Char “Terminal ID”
- `viva_wallet_bearer_token` Char
- `viva_wallet_webhook_verification_key` Char
- `viva_wallet_latest_response` Json
- `viva_wallet_test_mode` Boolean “Test mode”
- `viva_wallet_webhook_endpoint` Char (readonly, compute=_compute_viva_wallet_webhook_endpoint)

Public methods: `create`, `get_latest_viva_wallet_status`, `viva_wallet_get_payment_status`, `viva_wallet_send_payment_cancel`, `viva_wallet_send_payment_request`, `write`

Extension points: `_check_viva_wallet_credentials`, `_get_payment_terminal_selection`, `_get_verification_key`
