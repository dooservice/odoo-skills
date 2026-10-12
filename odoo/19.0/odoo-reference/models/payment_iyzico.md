# payment_iyzico — Payment Provider: Iyzico

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `iyzico_key_id` Char “Iyzico API Key”
- `iyzico_key_secret` Char “Iyzico Secret Key”

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`
