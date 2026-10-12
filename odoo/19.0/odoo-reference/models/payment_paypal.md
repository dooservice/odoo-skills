# payment_paypal — Payment Provider: Paypal

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `paypal_email_account` Char “Email”
- `paypal_client_id` Char “PayPal Client ID”
- `paypal_client_secret` Char “PayPal Client Secret”
- `paypal_access_token` Char “PayPal Access Token”
- `paypal_access_token_expiry` Datetime “PayPal Access Token Expiry”
- `paypal_webhook_id` Char “PayPal Webhook ID”

Public methods: `action_paypal_create_webhook`

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)

- `paypal_type` Char “PayPal Transaction Type”

Extension points: `_get_specific_processing_values`
