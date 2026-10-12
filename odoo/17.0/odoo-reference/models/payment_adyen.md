# payment_adyen — Payment Provider: Adyen

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `adyen_merchant_account` Char “Merchant Account”
- `adyen_api_key` Char “API Key”
- `adyen_client_key` Char “Client Key”
- `adyen_hmac_key` Char “HMAC Key”
- `adyen_api_url_prefix` Char “API URL Prefix”

Public methods: `create`, `write`

Extension points: `_get_default_payment_method_codes`

## `payment.token` (extends)

- `adyen_shopper_reference` Char “Shopper Reference” (readonly)

## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`, `_get_tx_from_notification_data`

## `payment.capture.wizard` (extends)

- `has_adyen_tx` Boolean (compute=_compute_has_adyen_tx)
