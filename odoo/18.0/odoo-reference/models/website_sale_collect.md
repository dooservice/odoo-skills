# website_sale_collect — Click & Collect

Depends on: base_geolocalize, payment_custom, website_sale_stock.

## `delivery.carrier` (extends)

- `delivery_type` Selection
- `warehouse_ids` Many2many → `stock.warehouse` “Stores”

Public methods: `create`, `in_store_rate_shipment`, `write`

Extension points: `_check_in_store_dm_has_warehouses_when_published`, `_check_warehouses_have_same_company`

## `payment.provider` (extends)

- `custom_mode` Selection

Extension points: `_get_compatible_providers`, `_get_default_payment_method_codes`

## `payment.transaction` (extends)


Extension points: `_post_process`

## `product.template` (extends)


Extension points: `_get_additionnal_combination_info`

## `res.config.settings` (extends)


Public methods: `action_view_in_store_delivery_methods`

## `sale.order` (extends)


Extension points: `_check_cart_is_ready_to_be_paid`, `_get_cart_and_free_qty`, `_get_pickup_locations`, `_get_unavailable_order_lines`

## `stock.picking` (extends)


Public methods: `write`

## `stock.warehouse` (extends)

- `opening_hours` Many2one → `resource.calendar` “Opening Hours”

## `website` (extends)

- `in_store_dm_id` Many2one → `delivery.carrier` “In-store Delivery Method” (compute=_compute_in_store_dm_id)

Extension points: `_get_max_in_store_product_available_qty`, `_get_product_available_qty`
