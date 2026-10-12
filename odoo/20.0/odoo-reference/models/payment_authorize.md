# payment_authorize — Payment Provider: Authorize.Net

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `authorize_login` Char “Authorize API Login ID”
- `authorize_transaction_key` Char “Authorize API Transaction Key”
- `authorize_signature_key` Char “Authorize API Signature Key”
- `authorize_client_key` Char “Authorize API Client Key”
- `authorize_webhook_id` Char “Authorize Webhook ID”

Public methods: `action_authorize_create_webhook`, `action_update_merchant_details`

Extension points: `_get_default_payment_method_codes`, `_get_validation_amount`

## `payment.token` (extends)

- `authorize_profile` Char “Authorize.Net Profile ID”

## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`
