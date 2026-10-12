# payment_razorpay — Payment Provider: Razorpay

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `razorpay_key_id` Char “Razorpay Key Id”
- `razorpay_key_secret` Char “Razorpay Key Secret”
- `razorpay_webhook_secret` Char “Razorpay Webhook Secret”

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`, `_get_validation_amount`

## `payment.token` (extends)


## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`, `_get_tx_from_notification_data`
