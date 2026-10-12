# pos_viva_com — PoS Viva.com

Depends on: point_of_sale.

## `pos.payment` (extends)

- `viva_com_session_id` Char

## `pos.payment.method` (extends)

- `viva_com_merchant_id` Char “Merchant ID”
- `viva_com_api_key` Char “API Key”
- `viva_com_client_id` Char “Client ID”
- `viva_com_client_secret` Char “Client secret”
- `viva_com_terminal_id` Char “Terminal ID”
- `viva_com_bearer_token` Char
- `viva_com_webhook_verification_key` Char
- `viva_com_latest_response` Json
- `viva_com_test_mode` Boolean “Test mode”
- `viva_com_webhook_endpoint` Char (readonly, compute=_compute_viva_com_webhook_endpoint)

Public methods: `create`, `get_latest_viva_com_status`, `viva_com_get_payment_status`, `viva_com_send_payment_cancel`, `viva_com_send_payment_request`, `viva_com_send_refund_request`, `write`

Extension points: `_check_viva_com_credentials`, `_get_payment_terminal_selection`
