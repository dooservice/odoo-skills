# payment_payumoney — Payment Provider: PayUmoney

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `payumoney_merchant_key` Char “Merchant Key”
- `payumoney_merchant_salt` Char “Merchant Salt”

Extension points: `_get_compatible_providers`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
