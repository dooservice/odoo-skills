# website_sale_loyalty — Coupons, Promotions, Gift Card and Loyalty for eCommerce

Depends on: website_sale, website_links, sale_loyalty.

## `loyalty.card` (extends)


Public methods: `action_coupon_share`

## `loyalty.program` (extends)

Inherits: `website.multi.mixin`

- `ecommerce_ok` Boolean “Available on Website”

Public methods: `action_program_share`

## `loyalty.rule` (extends)

- `website_id` Many2one (store, related=program_id.website_id)

## `payment.provider` (extends)


Extension points: `_get_compatible_providers`

## `sale.order` (extends)

- `disabled_auto_rewards` Many2many → `loyalty.reward`

Public methods: `get_promo_code_error`, `get_promo_code_success_message`

Extension points: `_get_claimable_and_showable_rewards`, `_get_free_shipping_lines`, `_get_non_delivery_lines`, `_get_program_domain`, `_get_program_timezone`, `_get_trigger_domain`, `_get_zero_priced_lines`

## `sale.order.line` (extends)


Public methods: `unlink`

## `coupon.share` (defines)

Create links that apply a coupon and redirect to a specific page

- `website_id` Many2one → `website` (required)
- `coupon_id` Many2one → `loyalty.card`
- `program_id` Many2one → `loyalty.program` (required)
- `program_website_id` Many2one → `website` “Program Website” (related=program_id.website_id)
- `promo_code` Char (compute=_compute_promo_code)
- `share_link` Char (compute=_compute_share_link)
- `redirect` Char (required)

Public methods: `action_generate_short_link`, `create_share_action`

Extension points: `_check_program`, `_check_website`, `_get_default_website_id`
