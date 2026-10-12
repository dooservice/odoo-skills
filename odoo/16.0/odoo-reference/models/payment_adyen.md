# payment_adyen — Payment Provider: Adyen

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `adyen_merchant_account` Char “Merchant Account”
- `adyen_api_key` Char “API Key”
- `adyen_client_key` Char “Client Key”
- `adyen_hmac_key` Char “HMAC Key”
- `adyen_checkout_api_url` Char “Checkout API URL”
- `adyen_recurring_api_url` Char “Recurring API URL”

Public methods: `create`, `write`

## `payment.token` (extends)

- `adyen_shopper_reference` Char “Shopper Reference” (readonly)

## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`, `_get_tx_from_notification_data`
