# website_sale_stock — Product Availability

Depends on: website_sale, sale_stock, stock_delivery.

## `product.combo` (extends)


Extension points: `_get_max_quantity`

## `product.product` (extends)

- `stock_notification_partner_ids` Many2many → `res.partner` “Back in stock Notifications”

Extension points: `_get_cart_qty`, `_get_max_quantity`

## `product.template` (extends)

- `allow_out_of_stock_order` Boolean “Continue selling when out-of-stock”
- `available_threshold` Float “Show Threshold”
- `show_availability` Boolean “Show availability Qty”
- `out_of_stock_message` Html “Out-of-Stock Message”

Extension points: `_get_additional_configurator_data`, `_get_additionnal_combination_info`

## `res.config.settings` (extends)

- `allow_out_of_stock_order` Boolean “Continue selling when out-of-stock”
- `available_threshold` Float “Show Threshold”
- `show_availability` Boolean “Show availability Qty”
- `website_warehouse_id` Many2one → `stock.warehouse` (related=website_id.warehouse_id)

Public methods: `get_values`, `set_values`

## `sale.order` (extends)


Extension points: `_check_cart_is_ready_to_be_paid`, `_get_cart_and_free_qty`, `_get_common_product_lines`, `_get_warehouse_available`

## `sale.order.line` (extends)


Extension points: `_get_max_available_qty`, `_get_max_line_qty`

## `stock.picking` (extends)

- `website_id` Many2one → `website` “Website” (readonly, store, related=sale_id.website_id)

## `website` (extends)

- `warehouse_id` Many2one → `stock.warehouse` “Warehouse”

Extension points: `_get_product_available_qty`, `_get_warehouse_available`
