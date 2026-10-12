# payment_paypal — Payment Provider: Paypal

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `paypal_email_account` Char “Email”
- `paypal_pdt_token` Char “PDT Identity Token”

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)

- `paypal_type` Char “PayPal Transaction Type”

Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
