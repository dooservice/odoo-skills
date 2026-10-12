# payment_razorpay — Payment Provider: Razorpay

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `razorpay_key_id` Char “Razorpay Key Id”
- `razorpay_key_secret` Char “Razorpay Key Secret”
- `razorpay_webhook_secret` Char “Razorpay Webhook Secret”
- `razorpay_account_id` Char “Razorpay Account ID”
- `razorpay_refresh_token` Char “Razorpay Refresh Token”
- `razorpay_public_token` Char “Razorpay Public Token”
- `razorpay_access_token` Char “Razorpay Access Token”
- `razorpay_access_token_expiry` Datetime “Razorpay Access Token Expiry”

Public methods: `action_razorpay_create_webhook`, `action_start_onboarding`

Extension points: `_check_razorpay_credentials_are_set_before_enabling`, `_get_default_payment_method_codes`, `_get_reset_values`, `_get_supported_currencies`, `_get_validation_amount`

## `payment.token` (extends)


## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`
