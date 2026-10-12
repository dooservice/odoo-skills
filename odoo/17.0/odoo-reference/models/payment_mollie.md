# payment_mollie — Payment Provider: Mollie

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `mollie_api_key` Char “Mollie API Key”

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
