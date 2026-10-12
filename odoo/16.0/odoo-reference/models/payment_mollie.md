# payment_mollie — Payment Provider: Mollie

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `mollie_api_key` Char “Mollie API Key”

Extension points: `_get_compatible_providers`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
