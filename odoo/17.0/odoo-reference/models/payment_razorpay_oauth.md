# payment_razorpay_oauth — Razorpay OAuth Integration

Depends on: payment_razorpay.

## `payment.provider` (extends)

- `razorpay_key_id` Char
- `razorpay_key_secret` Char
- `razorpay_webhook_secret` Char
- `razorpay_account_id` Char “Razorpay Account ID”
- `razorpay_refresh_token` Char “Razorpay Refresh Token”
- `razorpay_public_token` Char “Razorpay Public Token”
- `razorpay_access_token` Char “Razorpay Access Token”
- `razorpay_access_token_expiry` Datetime “Razorpay Access Token Expiry”

Public methods: `action_razorpay_create_webhook`, `action_razorpay_redirect_to_oauth_url`, `action_razorpay_reset_oauth_account`

Extension points: `_check_razorpay_credentials_are_set_before_enabling`
