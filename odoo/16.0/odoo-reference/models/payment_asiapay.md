# payment_asiapay — Payment Provider: AsiaPay

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `asiapay_merchant_id` Char “AsiaPay Merchant ID”
- `asiapay_currency_id` Many2one → `res.currency` “AsiaPay Currency”
- `asiapay_secure_hash_secret` Char “AsiaPay Secure Hash Secret”
- `asiapay_secure_hash_function` Selection “AsiaPay Secure Hash Function”

Extension points: `_get_compatible_providers`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
