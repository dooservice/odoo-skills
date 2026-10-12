# payment_razorpay — Payment Provider: Razorpay

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `razorpay_key_id` Char “Razorpay Key Id”
- `razorpay_key_secret` Char “Razorpay Key Secret”
- `razorpay_webhook_secret` Char “Razorpay Webhook Secret”

Extension points: `_get_compatible_providers`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
