# payment_sips — Payment Provider: Worldline SIPS

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `sips_merchant_id` Char “Merchant ID”
- `sips_secret` Char “SIPS Secret Key”
- `sips_key_version` Integer “Secret Key Version”
- `sips_test_url` Char “Test URL”
- `sips_prod_url` Char “Production URL”
- `sips_version` Char “Interface Version”

Extension points: `_get_compatible_providers`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
