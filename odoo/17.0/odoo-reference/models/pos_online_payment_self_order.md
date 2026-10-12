# pos_online_payment_self_order — POS Self-Order / Online Payment

Depends on: pos_online_payment, pos_self_order.

## `pos.config` (extends)

- `self_order_online_payment_method_id` Many2one → `pos.payment.method` “Self Online Payment” (store)

Extension points: `_check_self_order_online_payment_method_id`, `_get_allowed_payment_methods`, `_get_self_ordering_data`

## `pos.order` (extends)

- `use_self_order_online_payment` Boolean (readonly, store, compute=_compute_use_self_order_online_payment)

Public methods: `create`, `get_and_set_online_payments_data`, `write`

## `res.config.settings` (extends)

- `pos_self_order_online_payment_method_id` Many2one (related=pos_config_id.self_order_online_payment_method_id)
