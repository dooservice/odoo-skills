# pos_discount — Point of Sale Discounts

Depends on: point_of_sale.

## `pos.config` (extends)

- `iface_discount` Boolean “Order Discounts”
- `discount_pc` Float “Discount Percentage”
- `discount_product_id` Many2one → `product.product` “Discount Product”

Public methods: `open_ui`

Extension points: `_get_available_product_domain`, `_get_special_products`

## `pos.session` (extends)


Extension points: `_get_pos_ui_product_product`

## `res.config.settings` (extends)

- `pos_discount_pc` Float (related=pos_config_id.discount_pc)
- `pos_discount_product_id` Many2one → `product.product` (store, compute=_compute_pos_discount_product_id)
