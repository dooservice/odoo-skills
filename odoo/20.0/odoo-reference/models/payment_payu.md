# payment_payu — Payment Provider: PayU

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `payu_key_id` Char “PayU Key Id”
- `payu_merchant_salt` Char “PayU Merchant Salt”

Public methods: `action_start_onboarding`

Extension points: `_check_payu_credentials_are_set_if_live`, `_get_default_payment_method_codes`, `_get_reset_values`, `_get_supported_currencies`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`
