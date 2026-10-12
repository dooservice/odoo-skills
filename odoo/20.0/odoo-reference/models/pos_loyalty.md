# pos_loyalty — Point of Sale - Coupons & Loyalty

Depends on: loyalty, point_of_sale.

## `account.move.line` (extends)


Extension points: `_get_discount_lines`

## `barcode.rule` (extends)

- `type` Selection

## `loyalty.card` (extends)

Inherits: `pos.load.mixin`

- `source_pos_order_id` Many2one → `pos.order` “POS Order Reference” (readonly)

Public methods: `get_card_status`

Extension points: `_get_or_create_pos_card`

## `loyalty.mail` (extends)

- `pos_report_print_id` Many2one → `ir.actions.report` “Print Report”

## `loyalty.program` (extends)

Inherits: `pos.load.mixin`

- `pos_config_ids` Many2many → `pos.config` “Point of Sales” (store, compute=_compute_pos_config_ids)
- `pos_order_count` Integer “PoS Order Count” (compute=_compute_pos_order_count)
- `pos_ok` Boolean “Point of sale”
- `pos_report_print_id` Many2one → `ir.actions.report` “Print Report” (compute=_compute_pos_report_print_id)

Extension points: `_get_pos_order_points`

## `loyalty.reward` (extends)

Inherits: `pos.load.mixin`


Public methods: `unlink`

Extension points: `_get_pos_points_cost`, `_get_reward_product_domain_fields`

## `loyalty.rule` (extends)

Inherits: `pos.load.mixin`

- `any_product` Boolean (compute=_compute_valid_product_ids)
- `valid_product_ids` Many2many → `product.product` (compute=_compute_valid_product_ids)
- `promo_barcode` Char “Barcode” (store, compute=_compute_promo_barcode)

Extension points: `_get_pos_order_points`

## `pos.config` (extends)


Extension points: `_get_program_ids`

## `pos.order` (extends)

- `applied_codes` Json
- `active_rewards` Json
- `active_payment_programs` Json
- `disabled_program_ids` Json

Public methods: `read_pos_data`

Extension points: `_get_loyalty_cards_to_credit`, `_get_mail_attachments`, `_get_refund_reversal_cards`, `_get_refund_reversal_points`

## `pos.order.line` (extends)

- `is_reward_line` Boolean
- `reward_id` Many2one → `loyalty.reward`
- `card_id` Many2one → `loyalty.card`
- `points_cost` Float
- `gift_card_vals` Json

Extension points: `_get_discount_amount_for_report`, `_get_loyalty_program`

## `pos.session` (extends)


Public methods: `filter_local_data`

## `product.product` (extends)


## `product.template` (extends)


## `pos.order.receipt` (extends)


Public methods: `order_receipt_generate_data`
