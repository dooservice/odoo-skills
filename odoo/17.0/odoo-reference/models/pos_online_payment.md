# pos_online_payment — Point of Sale online payment

Depends on: point_of_sale, account_payment.

## `account.payment` (extends)

- `pos_order_id` Many2one → `pos.order` “POS Order” (readonly)

Public methods: `action_view_pos_order`

## `payment.transaction` (extends)

- `pos_order_id` Many2one → `pos.order` “POS Order” (readonly)

Public methods: `action_view_pos_order`

## `pos.config` (extends)


Extension points: `_check_online_payment_methods`, `_get_cashier_online_payment_method`

## `pos.order` (extends)

- `online_payment_method_id` Many2one → `pos.payment.method` (compute=_compute_online_payment_method_id)
- `next_online_payment_amount` Float “Next online payment amount to pay”

Public methods: `get_amount_unpaid`, `get_and_set_online_payments_data`

Extension points: `_check_next_online_payment_amount`, `_get_checked_next_online_payment_amount`

## `pos.payment` (extends)

- `online_account_payment_id` Many2one → `account.payment` “Online accounting payment” (readonly)

Public methods: `create`, `write`

Extension points: `_check_payment_method_id`

## `pos.payment.method` (extends)

- `is_online_payment` Boolean “Online Payment”
- `online_payment_provider_ids` Many2many → `payment.provider` “Allowed Providers”
- `has_an_online_payment_provider` Boolean (readonly, compute=_compute_has_an_online_payment_provider)
- `type` Selection

Public methods: `create`, `write`

Extension points: `_get_online_payment_providers`, `_get_or_create_online_payment_method`, `_get_payment_terminal_selection`

## `pos.session` (extends)


Extension points: `_create_bank_payment_moves`, `_get_split_receivable_op_vals`
