# payment_stripe — Payment Provider: Stripe

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `stripe_publishable_key` Char “Publishable Key”
- `stripe_secret_key` Char “Secret Key”
- `stripe_webhook_secret` Char “Webhook Signing Secret”

Public methods: `action_start_onboarding`, `action_stripe_create_webhook`, `action_stripe_verify_apple_pay_domain`

Extension points: `_check_connected_account_is_live`, `_check_onboarding_of_live_provider_is_completed`, `_get_default_payment_method_codes`, `_get_stripe_extra_request_headers`, `_get_stripe_webhook_url`

## `payment.token` (extends)

- `stripe_payment_method` Char “Stripe Payment Method ID” (readonly)
- `stripe_mandate` Char “Stripe Mandate” (readonly)

## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`
