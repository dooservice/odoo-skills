# payment_paypal — Payment Provider: Paypal

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `paypal_email_account` Char “PayPal Email”
- `paypal_account_id` Char “PayPal Seller Account ID”
- `paypal_client_id` Char “PayPal Client ID”
- `paypal_client_secret` Char “PayPal Client Secret”
- `paypal_webhook_id` Char “PayPal Webhook ID”
- `paypal_seller_nonce` Char
- `paypal_is_oauth_onboarded` Boolean
- `paypal_payments_receivable` Boolean
- `paypal_email_confirmed` Boolean
- `paypal_access_token` Char “PayPal Access Token”
- `paypal_access_token_expiry` Datetime “PayPal Access Token Expiry”

Public methods: `action_paypal_create_webhook`, `action_paypal_update_onboarding_status`, `action_reset_credentials`, `action_start_onboarding`

Extension points: `_check_paypal_credentials_are_set_if_published`, `_get_default_payment_method_codes`, `_get_reset_values`, `_get_supported_currencies`

## `payment.token` (extends)


## `payment.transaction` (extends)

- `paypal_setup_token_ref` Char “PayPal Setup Token ID”
- `paypal_type` Char “PayPal Transaction Type”

Extension points: `_get_paypal_3ds_policy`, `_get_specific_processing_values`, `_get_specific_rendering_values`
