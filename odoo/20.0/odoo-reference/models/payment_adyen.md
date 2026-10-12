# payment_adyen — Payment Provider: Adyen

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `adyen_merchant_account` Char “Adyen Merchant Account”
- `adyen_api_key` Char “Adyen API Key”
- `adyen_client_key` Char “Adyen Client Key”
- `adyen_hmac_key` Char “Adyen HMAC Key”
- `adyen_api_url_prefix` Char “Adyen API URL Prefix”

Public methods: `create`, `write`

Extension points: `_get_default_payment_method_codes`

## `payment.token` (extends)

- `adyen_shopper_reference` Char “Shopper Reference” (readonly)

## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`

## `payment.capture.wizard` (extends)

- `has_adyen_tx` Boolean (compute=_compute_has_adyen_tx)
