# payment_nuvei — Payment Provider: Nuvei

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `nuvei_merchant_identifier` Char “Nuvei Merchant Identifier”
- `nuvei_site_identifier` Char “Nuvei Site Identifier”
- `nuvei_secret_key` Char “Nuvei Secret Key”

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`
