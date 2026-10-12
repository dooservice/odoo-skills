# payment_toss_payments — Payment Provider: Toss Payments

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `toss_payments_client_key` Char “Toss Payments Client Key”
- `toss_payments_secret_key` Char “Toss Payments Secret Key”
- `toss_payments_webhook_url` Char “Toss Payments Webhook URL” (readonly, compute=_compute_toss_payments_webhook_url)

Extension points: `_check_available_currency_ids_only_contains_supported_currencies`, `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)

- `toss_payments_payment_secret` Char “Toss Payments Payment Secret”

Extension points: `_get_specific_processing_values`
