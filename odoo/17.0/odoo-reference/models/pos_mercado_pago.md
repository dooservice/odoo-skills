# pos_mercado_pago — POS Mercado Pago

Depends on: point_of_sale.

## `pos.payment.method` (extends)

- `mp_bearer_token` Char “Production user token”
- `mp_webhook_secret_key` Char “Production secret key”
- `mp_id_point_smart` Char “Terminal S/N”
- `mp_id_point_smart_complet` Char

Public methods: `create`, `force_pdv`, `mp_get_payment_status`, `mp_payment_intent_cancel`, `mp_payment_intent_create`, `mp_payment_intent_get`, `write`

Extension points: `_check_access`, `_get_payment_terminal_selection`

## `pos.session` (extends)
