# sale_purchase — Sale Purchase

Depends on: sale, purchase.

## `product.template` (extends)

- `service_tracking` Selection

Public methods: `create`, `write`

Extension points: `_check_vendor_for_service_tracking_subcontract`, `_get_saleable_tracking_types`, `_prepare_service_tracking_tooltip`

## `purchase.order` (extends)

- `sale_order_count` Integer “Number of Source Sale” (compute=_compute_sale_order_count)
- `has_sale_order` Boolean “Technical field for whether the purchase order has associated sale orders” (compute=_compute_sale_order_count)

Public methods: `action_view_sale_orders`, `button_cancel`

Extension points: `_get_sale_orders`

## `purchase.order.line` (extends)

- `sale_order_id` Many2one “Sale Order” (related=sale_line_id.order_id)
- `sale_line_id` Many2one → `sale.order.line` “Origin Sale Item”

## `sale.order` (extends)

- `purchase_order_count` Integer “Number of Purchase Order Generated” (compute=_compute_purchase_order_count)

Public methods: `action_view_purchase_orders`

Extension points: `_action_cancel`, `_action_confirm`, `_get_purchase_orders`

## `sale.order.line` (extends)

- `purchase_line_ids` One2many → `purchase.order.line` “Generated Purchase Lines” (readonly)
- `purchase_line_count` Integer “Number of generated purchase items” (compute=_compute_purchase_count)

Public methods: `create`, `write`

Extension points: `_create_purchase_order`, `_get_additional_domain_for_purchase_order_line`
