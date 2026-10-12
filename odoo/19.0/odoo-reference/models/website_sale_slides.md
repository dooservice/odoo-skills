# website_sale_slides — Sell Courses

Depends on: website_slides, website_sale.

## `product.product` (extends)

- `channel_ids` One2many → `slide.channel` “Courses”

Public methods: `get_product_multiline_description_sale`

## `product.template` (extends)

- `service_tracking` Selection

Extension points: `_get_product_types_allow_zero_price`, `_prepare_service_tracking_tooltip`

## `sale.order` (extends)


Extension points: `_action_confirm`

## `sale.order.line` (extends)


## `slide.channel` (extends)

- `enroll` Selection
- `product_id` Many2one → `product.product`
- `product_sale_revenues` Monetary “Total revenues” (compute=_compute_product_sale_revenues)
- `currency_id` Many2one (related=product_id.currency_id)

Public methods: `action_view_sales`, `create`, `write`

Extension points: `_get_default_product_id`
