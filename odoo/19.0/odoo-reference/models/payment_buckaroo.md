# payment_buckaroo — Payment Provider: Buckaroo

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `buckaroo_website_key` Char “Website Key”
- `buckaroo_secret_key` Char “Buckaroo Secret Key”

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`
