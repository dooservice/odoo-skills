# payment_redsys — Payment Provider: Redsys

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `redsys_merchant_code` Char “Redsys Merchant Code”
- `redsys_merchant_terminal` Char “Redsys Merchant Terminal”
- `redsys_secret_key` Char “Redsys Secret Key”

Extension points: `_get_default_payment_method_codes`

## `payment.transaction` (extends)


Public methods: `create`

Extension points: `_get_specific_rendering_values`
