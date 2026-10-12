# payment_worldline — Payment Provider: Worldline

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `worldline_pspid` Char “Worldline PSPID”
- `worldline_api_key` Char “Worldline API Key”
- `worldline_api_secret` Char “Worldline API Secret”
- `worldline_webhook_key` Char “Worldline Webhook Key”
- `worldline_webhook_secret` Char “Worldline Webhook Secret”

Extension points: `_get_default_payment_method_codes`

## `payment.transaction` (extends)


Extension points: `_get_specific_processing_values`, `_get_specific_rendering_values`
