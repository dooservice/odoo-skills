# pos_loyalty — Point of Sale - Coupons & Loyalty

Depends on: loyalty, point_of_sale.

## `barcode.rule` (extends)

- `type` Selection

## `loyalty.card` (extends)

- `source_pos_order_id` Many2one → `pos.order`

Extension points: `_get_default_template`, `_get_mail_partner`, `_get_signature`

## `loyalty.mail` (extends)

- `pos_report_print_id` Many2one → `ir.actions.report` “Print Report”

## `loyalty.program` (extends)

- `pos_config_ids` Many2many → `pos.config` “Point of Sales” (store, compute=_compute_pos_config_ids)
- `pos_order_count` Integer “PoS Order Count” (compute=_compute_pos_order_count)
- `pos_ok` Boolean “Point of Sale”
- `pos_report_print_id` Many2one → `ir.actions.report` “Print Report” (compute=_compute_pos_report_print_id)

## `loyalty.reward` (extends)


Public methods: `unlink`

Extension points: `_get_discount_product_values`

## `loyalty.rule` (extends)

- `valid_product_ids` Many2many → `product.product` (compute=_compute_valid_product_ids)
- `any_product` Boolean (compute=_compute_valid_product_ids)
- `promo_barcode` Char “Barcode” (store, compute=_compute_promo_barcode)

## `pos.config` (extends)

- `gift_card_settings` Selection “Gift Cards settings”

Public methods: `use_coupon_code`

Extension points: `_check_before_creating_new_session`, `_get_program_ids`

## `pos.order` (extends)


Public methods: `confirm_coupon_programs`, `validate_coupon_programs`

Extension points: `_check_existing_loyalty_cards`, `_get_fields_for_order_line`

## `pos.order.line` (extends)

- `is_reward_line` Boolean
- `reward_id` Many2one → `loyalty.reward`
- `coupon_id` Many2one → `loyalty.card`
- `reward_identifier_code` Char
- `points_cost` Float

## `pos.session` (extends)


Public methods: `get_pos_ui_res_partner_by_params`

Extension points: `_get_pos_ui_loyalty_program`, `_get_pos_ui_loyalty_reward`, `_get_pos_ui_loyalty_rule`, `_get_pos_ui_product_product`, `_get_pos_ui_res_partner`

## `res.config.settings` (extends)

- `pos_gift_card_settings` Selection (related=pos_config_id.gift_card_settings)
