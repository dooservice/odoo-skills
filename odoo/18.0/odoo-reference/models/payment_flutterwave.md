# payment_flutterwave — Payment Provider: Flutterwave

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `flutterwave_public_key` Char “Flutterwave Public Key”
- `flutterwave_secret_key` Char “Flutterwave Secret Key”
- `flutterwave_webhook_secret` Char “Flutterwave Webhook Secret”

Extension points: `_get_compatible_providers`, `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.token` (extends)

- `flutterwave_customer_email` Char (readonly)

## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`, `_get_specific_rendering_values`, `_get_tx_from_notification_data`
