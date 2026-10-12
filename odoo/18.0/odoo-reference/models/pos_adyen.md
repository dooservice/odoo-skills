# pos_adyen — POS Adyen

Depends on: point_of_sale.

## `pos.config` (extends)

- `adyen_ask_customer_for_tip` Boolean “Ask Customers For Tip”

Extension points: `_check_adyen_ask_customer_for_tip`

## `pos.payment.method` (extends)

- `adyen_api_key` Char “Adyen API key”
- `adyen_terminal_identifier` Char
- `adyen_test_mode` Boolean
- `adyen_latest_response` Char
- `adyen_event_url` Char “Event URL” (readonly)

Public methods: `get_latest_adyen_status`, `proxy_adyen_request`

Extension points: `_check_adyen_terminal_identifier`, `_get_adyen_endpoints`, `_get_expected_message_header`, `_get_expected_payment_request`, `_get_hmac`, `_get_payment_terminal_selection`, `_get_valid_acquirer_data`

## `res.config.settings` (extends)

- `pos_adyen_ask_customer_for_tip` Boolean (store, compute=_compute_pos_adyen_ask_customer_for_tip)
