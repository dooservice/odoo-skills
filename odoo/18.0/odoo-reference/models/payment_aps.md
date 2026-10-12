# payment_aps — Payment Provider: Amazon Payment Services

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `aps_merchant_identifier` Char “APS Merchant Identifier”
- `aps_access_code` Char “APS Access Code”
- `aps_sha_request` Char “APS SHA Request Phrase”
- `aps_sha_response` Char “APS SHA Response Phrase”

Extension points: `_get_default_payment_method_codes`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
