# pos_loyalty — Point of Sale - Coupons & Loyalty

Depends on: loyalty, point_of_sale.

## `account.move.line` (extends)


Extension points: `_get_discount_lines`

## `barcode.rule` (extends)

- `type` Selection

## `loyalty.card` (extends)

Inherits: `pos.load.mixin`

- `source_pos_order_id` Many2one → `pos.order`

Extension points: `_get_default_template`, `_get_mail_partner`, `_get_signature`

## `loyalty.mail` (extends)

- `pos_report_print_id` Many2one → `ir.actions.report` “Print Report”

## `loyalty.program` (extends)

Inherits: `pos.load.mixin`

- `pos_config_ids` Many2many → `pos.config` “Point of Sales” (store, compute=_compute_pos_config_ids)
- `pos_order_count` Integer “PoS Order Count” (compute=_compute_pos_order_count)
- `pos_ok` Boolean “Point of Sale”
- `pos_report_print_id` Many2one → `ir.actions.report` “Print Report” (compute=_compute_pos_report_print_id)

## `loyalty.reward` (extends)

Inherits: `pos.load.mixin`


Public methods: `unlink`

Extension points: `_get_discount_product_values`, `_get_reward_product_domain_fields`

## `loyalty.rule` (extends)

Inherits: `pos.load.mixin`

- `valid_product_ids` Many2many → `product.product` (compute=_compute_valid_product_ids)
- `any_product` Boolean (compute=_compute_valid_product_ids)
- `promo_barcode` Char “Barcode” (store, compute=_compute_promo_barcode)

## `pos.config` (extends)


Public methods: `use_coupon_code`

Extension points: `_check_before_creating_new_session`, `_get_program_ids`

## `pos.order` (extends)


Public methods: `add_loyalty_history_lines`, `confirm_coupon_programs`, `get_ticket_screen_order_data`, `validate_coupon_programs`

Extension points: `_check_existing_loyalty_cards`, `_get_fields_for_order_line`

## `pos.order.line` (extends)

- `is_reward_line` Boolean
- `reward_id` Many2one → `loyalty.reward`
- `coupon_id` Many2one → `loyalty.card`
- `reward_identifier_code` Char
- `points_cost` Float

Public methods: `isRefund`

## `pos.session` (extends)


## `product.product` (extends)


## `res.partner` (extends)

- `loyalty_card_count` Integer
