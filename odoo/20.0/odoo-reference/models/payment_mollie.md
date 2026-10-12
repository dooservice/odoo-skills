# payment_mollie — Payment Provider: Mollie

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `mollie_api_key` Char “Mollie API Key”

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.token` (extends)

- `mollie_customer_id` Char “Mollie Customer ID” (readonly)

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`
