# payment_authorize — Payment Provider: Authorize.Net

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `authorize_login` Char “API Login ID”
- `authorize_transaction_key` Char “API Transaction Key”
- `authorize_signature_key` Char “API Signature Key”
- `authorize_client_key` Char “API Client Key”

Public methods: `action_update_merchant_details`

Extension points: `_get_default_payment_method_codes`, `_get_validation_amount`

## `payment.token` (extends)

- `authorize_profile` Char “Authorize.Net Profile ID”

## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`, `_get_tx_from_notification_data`
