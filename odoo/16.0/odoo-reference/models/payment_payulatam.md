# payment_payulatam — Payment Provider: PayU Latam

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `payulatam_merchant_id` Char “PayU Latam Merchant ID”
- `payulatam_account_id` Char “PayU Latam Account ID”
- `payulatam_api_key` Char “PayU Latam API Key”

Extension points: `_get_compatible_providers`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
