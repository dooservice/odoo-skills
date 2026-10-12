# pos_mercado_pago — POS Mercado Pago

Depends on: point_of_sale.

## `pos.payment.method` (extends)

- `mp_bearer_token` Char “Production user token”
- `mp_webhook_secret_key` Char “Production secret key”
- `mp_id_point_smart` Char “Terminal S/N”
- `mp_id_point_smart_complet` Char
- `mp_webhook_endpoint` Char “Mercado Pago Webhook Endpoint” (readonly, compute=_compute_mp_webhook_endpoint)

Public methods: `create`, `force_pdv`, `mp_order_create`, `mp_order_get`, `mp_order_refund`, `write`

Extension points: `_check_special_access`, `_get_terminal_provider_selection`
