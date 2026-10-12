# payment_xendit — Payment Provider: Xendit

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `xendit_public_key` Char “Xendit Public Key”
- `xendit_secret_key` Char “Xendit Secret Key”
- `xendit_webhook_token` Char “Xendit Webhook Token”

Extension points: `_get_default_payment_method_codes`, `_get_redirect_form_view`, `_get_supported_currencies`, `_get_validation_currency`

## `payment.transaction` (extends)


Extension points: `_get_rounded_amount`, `_get_specific_processing_values`, `_get_specific_rendering_values`
