# sale_loyalty — Sale Loyalty

Depends on: sale, loyalty.

## `account.move.line` (extends)


Extension points: `_get_discount_lines`

## `loyalty.card` (extends)

- `order_id` Many2one → `sale.order` “Order Reference” (readonly)
- `order_id_partner_id` Many2one → `res.partner` “Sale Order Customer” (related=order_id.partner_id)

Public methods: `action_archive`

Extension points: `_get_default_template`, `_get_mail_author`, `_get_signature`

## `loyalty.history` (extends)


Extension points: `_get_order_portal_url`

## `loyalty.program` (extends)

- `order_count` Integer (compute=_compute_order_count)
- `sale_ok` Boolean “Sales”

## `loyalty.reward` (extends)


Public methods: `unlink`

Extension points: `_get_discount_product_values`

## `sale.order` (extends)

- `applied_coupon_ids` Many2many → `loyalty.card` “Manually Applied Coupons”
- `code_enabled_rule_ids` Many2many → `loyalty.rule` “Manually Triggered Rules”
- `coupon_point_ids` One2many → `sale.order.coupon.points`
- `reward_amount` Float (compute=_compute_reward_total)
- `gift_card_count` Integer (compute=_compute_gift_card_count)

Public methods: `action_confirm`, `action_open_reward_wizard`, `action_view_gift_cards`, `copy`

Extension points: `_action_cancel`, `_get_applicable_program_points`, `_get_applied_global_discount`, `_get_applied_global_discount_lines`, `_get_applied_programs`, `_get_claimable_rewards`, `_get_confirmed_tx_create_date`, `_get_discount_amount`, `_get_loyalty_data`, `_get_no_effect_on_threshold_lines`, `_get_not_rewarded_order_lines`, `_get_order_line_price`, `_get_point_changes`, `_get_points_programs`, `_get_program_domain`, `_get_program_timezone`, `_get_real_points_for_coupon`, `_get_reward_coupons`, `_get_reward_line_values`, `_get_reward_programs`, `_get_reward_values_discount`, `_get_reward_values_product`, `_get_specific_discountable_lines`, `_get_trigger_domain`

## `sale.order.coupon.points` (defines)

Sale Order Coupon Points - Keeps track of how a sale order impacts a coupon

- `order_id` Many2one → `sale.order` (required, index)
- `coupon_id` Many2one → `loyalty.card` (required)
- `points` Float (required)

## `sale.order.line` (extends)

- `is_reward_line` Boolean “Is a program reward line” (compute=_compute_is_reward_line)
- `reward_id` Many2one → `loyalty.reward` (readonly)
- `coupon_id` Many2one → `loyalty.card` (readonly)
- `reward_identifier_code` Char
- `points_cost` Float

Public methods: `create`, `unlink`, `write`

Extension points: `_get_display_price`, `_prepare_base_line_for_taxes_computation`

## `sale.loyalty.coupon.wizard` (defines)

Sale Loyalty - Apply Coupon Wizard

- `order_id` Many2one → `sale.order` (required)
- `coupon_code` Char (required)

Public methods: `action_apply`

## `sale.loyalty.reward.wizard` (defines)

Sale Loyalty - Reward Selection Wizard

- `order_id` Many2one → `sale.order` (required)
- `reward_ids` Many2many → `loyalty.reward` (compute=_compute_claimable_reward_ids)
- `selected_reward_id` Many2one → `loyalty.reward`
- `multi_product_reward` Boolean (related=selected_reward_id.multi_product)
- `reward_product_ids` Many2many (related=selected_reward_id.reward_product_ids)
- `selected_product_id` Many2one → `product.product` (store, compute=_compute_selected_product_id)

Public methods: `action_apply`, `action_cancel`
