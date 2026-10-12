# payment_xendit — Payment Provider: Xendit

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `xendit_secret_key` Char “Xendit Secret Key”
- `xendit_webhook_token` Char “Xendit Webhook Token”

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
