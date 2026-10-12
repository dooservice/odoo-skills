# payment_mercado_pago — Payment Provider: Mercado Pago

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `mercado_pago_access_token` Char “Mercado Pago Access Token”

Extension points: `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`
