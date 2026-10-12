# loyalty — Coupons & Loyalty

Depends on: product.

## `loyalty.card` (defines)

Loyalty Coupon

Inherits: `mail.thread`

- `program_id` Many2one → `loyalty.program`
- `program_type` Selection (related=program_id.program_type)
- `company_id` Many2one (store, related=program_id.company_id)
- `currency_id` Many2one (related=program_id.currency_id)
- `partner_id` Many2one → `res.partner` (index)
- `points` Float
- `point_name` Char (readonly, related=program_id.portal_point_name)
- `points_display` Char (compute=_compute_points_display)
- `code` Char (required)
- `expiration_date` Date
- `use_count` Integer (compute=_compute_use_count)

Public methods: `action_coupon_send`, `create`, `write`

Extension points: `_get_default_template`, `_get_mail_author`, `_get_mail_partner`, `_get_signature`

## `loyalty.mail` (defines)

Loyalty Communication

- `active` Boolean
- `program_id` Many2one → `loyalty.program` (required)
- `trigger` Selection “When” (required)
- `points` Float
- `mail_template_id` Many2one → `mail.template` “Email Template” (required)

## `loyalty.program` (defines)

Loyalty Program

- `name` Char “Program Name” (required)
- `active` Boolean
- `sequence` Integer
- `company_id` Many2one → `res.company`
- `currency_id` Many2one → `res.currency` (required, store, compute=_compute_currency_id)
- `currency_symbol` Char (related=currency_id.symbol)
- `pricelist_ids` Many2many → `product.pricelist` “Pricelist”
- `total_order_count` Integer “Total Order Count” (compute=_compute_total_order_count)
- `rule_ids` One2many → `loyalty.rule` (store, compute=_compute_from_program_type)
- `reward_ids` One2many → `loyalty.reward` (store, compute=_compute_from_program_type)
- `communication_plan_ids` One2many → `loyalty.mail` (store, compute=_compute_from_program_type)
- `mail_template_id` Many2one → `mail.template` “Email template” (compute=_compute_mail_template_id)
- `trigger_product_ids` Many2many (related=rule_ids.product_ids)
- `coupon_ids` One2many → `loyalty.card`
- `coupon_count` Integer (compute=_compute_coupon_count)
- `coupon_count_display` Char “Items” (compute=_compute_coupon_count_display)
- `program_type` Selection (required)
- `date_from` Date “Start Date”
- `date_to` Date “End date”
- `limit_usage` Boolean “Limit Usage”
- `max_usage` Integer
- `applies_on` Selection (required, store, compute=_compute_from_program_type)
- `trigger` Selection (store, compute=_compute_from_program_type)
- `portal_visible` Boolean
- `portal_point_name` Char (store, compute=_compute_portal_point_name)
- `is_nominative` Boolean (compute=_compute_is_nominative)
- `is_payment_program` Boolean (compute=_compute_is_payment_program)
- `payment_program_discount_product_id` Many2one → `product.product` “Discount Product” (readonly, compute=_compute_payment_program_discount_product_id)
- `available_on` Boolean “Available On”

Public methods: `action_open_loyalty_cards`, `create`, `create_from_template`, `get_program_templates`, `toggle_active`, `write`

Extension points: `_check_date_from_date_to`, `_check_pricelist_currency`, `_get_template_values`, `_get_valid_products`

## `loyalty.reward` (defines)

Loyalty Reward

- `active` Boolean
- `program_id` Many2one → `loyalty.program` (required)
- `program_type` Selection (related=program_id.program_type)
- `company_id` Many2one (store, related=program_id.company_id)
- `currency_id` Many2one (related=program_id.currency_id)
- `description` Char (store, compute=_compute_description)
- `reward_type` Selection (required)
- `user_has_debug` Boolean (compute=_compute_user_has_debug)
- `discount` Float “Discount”
- `discount_mode` Selection (required)
- `discount_applicability` Selection
- `discount_product_domain` Char
- `discount_product_ids` Many2many → `product.product` “Discounted Products”
- `discount_product_category_id` Many2one → `product.category` “Discounted Prod. Categories”
- `discount_product_tag_id` Many2one → `product.tag` “Discounted Prod. Tag”
- `all_discount_product_ids` Many2many → `product.product` (compute=_compute_all_discount_product_ids)
- `reward_product_domain` Char (compute=_compute_reward_product_domain)
- `discount_max_amount` Monetary “Max Discount”
- `discount_line_product_id` Many2one → `product.product`
- `is_global_discount` Boolean (compute=_compute_is_global_discount)
- `reward_product_id` Many2one → `product.product` “Product”
- `reward_product_tag_id` Many2one → `product.tag` “Product Tag”
- `multi_product` Boolean (compute=_compute_multi_product)
- `reward_product_ids` Many2many → `product.product` “Reward Products” (compute=_compute_multi_product)
- `reward_product_qty` Integer
- `reward_product_uom_id` Many2one → `uom.uom` (compute=_compute_reward_product_uom_id)
- `required_points` Float “Points needed”
- `point_name` Char (readonly, related=program_id.portal_point_name)
- `clear_wallet` Boolean

Public methods: `create`, `default_get`, `unlink`, `write`

Extension points: `_create_missing_discount_line_products`, `_get_active_products_domain`, `_get_discount_mode_select`, `_get_discount_product_domain`, `_get_discount_product_values`

## `loyalty.rule` (defines)

Loyalty Rule

- `active` Boolean
- `program_id` Many2one → `loyalty.program` (required)
- `program_type` Selection (related=program_id.program_type)
- `company_id` Many2one (store, related=program_id.company_id)
- `currency_id` Many2one (related=program_id.currency_id)
- `user_has_debug` Boolean (compute=_compute_user_has_debug)
- `product_domain` Char
- `product_ids` Many2many → `product.product` “Products”
- `product_category_id` Many2one → `product.category` “Categories”
- `product_tag_id` Many2one → `product.tag` “Product Tag”
- `reward_point_amount` Float “Reward”
- `reward_point_split` Boolean “Split per unit”
- `reward_point_name` Char (readonly, related=program_id.portal_point_name)
- `reward_point_mode` Selection (required)
- `minimum_qty` Integer “Minimum Quantity”
- `minimum_amount` Monetary “Minimum Purchase”
- `minimum_amount_tax_mode` Selection (required)
- `mode` Selection “Application” (store, compute=_compute_mode)
- `code` Char “Discount code” (store, compute=_compute_code)

Public methods: `default_get`

Extension points: `_get_reward_point_mode_selection`, `_get_valid_product_domain`, `_get_valid_products`

## `product.pricelist` (extends)


Public methods: `action_archive`

## `product.product` (extends)


Public methods: `write`

## `product.template` (extends)


## `res.partner` (extends)

- `loyalty_card_count` Integer “Active loyalty cards” (compute=_compute_count_active_cards)

Public methods: `action_view_loyalty_cards`

## `loyalty.generate.wizard` (defines)

Generate Coupons

- `program_id` Many2one → `loyalty.program` (required)
- `program_type` Selection (related=program_id.program_type)
- `mode` Selection “For” (required)
- `customer_ids` Many2many → `res.partner` “Customers”
- `customer_tag_ids` Many2many → `res.partner.category` “Customer Tags”
- `coupon_qty` Integer “Quantity” (store, compute=_compute_coupon_qty)
- `points_granted` Float “Grant” (required)
- `points_name` Char (readonly, related=program_id.portal_point_name)
- `valid_until` Date
- `will_send_mail` Boolean (compute=_compute_will_send_mail)

Public methods: `generate_coupons`

Extension points: `_get_coupon_values`, `_get_partners`
