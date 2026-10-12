# payment_authorize — Payment Provider: Authorize.Net

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `authorize_login` Char “API Login ID”
- `authorize_transaction_key` Char “API Transaction Key”
- `authorize_signature_key` Char “API Signature Key”
- `authorize_client_key` Char “API Client Key”
- `authorize_currency_id` Many2one → `res.currency` “Authorize Currency”
- `authorize_payment_method_type` Selection “Allow Payments From”

Public methods: `action_update_merchant_details`

Extension points: `_check_payment_method_type`, `_get_compatible_providers`, `_get_validation_amount`, `_get_validation_currency`

## `payment.token` (extends)

- `authorize_profile` Char “Authorize.Net Profile ID”
- `authorize_payment_method_type` Selection “Authorize.Net Payment Type”

## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`, `_get_tx_from_notification_data`
