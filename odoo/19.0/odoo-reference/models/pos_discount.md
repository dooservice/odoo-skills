# pos_discount — Point of Sale Discounts

Depends on: point_of_sale.

## `account.move.line` (extends)


Extension points: `_get_discount_lines`

## `pos.config` (extends)

- `iface_discount` Boolean “Order Discounts”
- `discount_pc` Float “Discount Percentage”
- `discount_product_id` Many2one → `product.product` “Discount Product”

Public methods: `open_ui`

Extension points: `_get_special_products`

## `product.template` (extends)


## `res.config.settings` (extends)

- `pos_discount_pc` Float (related=pos_config_id.discount_pc)
- `pos_discount_product_id` Many2one → `product.product` (store, compute=_compute_pos_discount_product_id)
