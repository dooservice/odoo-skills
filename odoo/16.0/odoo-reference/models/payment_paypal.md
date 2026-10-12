# payment_paypal — Payment Provider: Paypal

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `paypal_email_account` Char “Email”
- `paypal_seller_account` Char “Merchant Account ID”
- `paypal_pdt_token` Char “PDT Identity Token”
- `paypal_use_ipn` Boolean “Use IPN”

Extension points: `_get_compatible_providers`

## `payment.transaction` (extends)

- `paypal_type` Char “PayPal Transaction Type”

Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
