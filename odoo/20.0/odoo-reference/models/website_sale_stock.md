# website_sale_stock — Product Availability

Depends on: website_sale, sale_stock, stock_delivery.

## `delivery.carrier` (extends)

Inherits: `website.published.multi.mixin`

- `support_pickup_locations` Boolean (compute=_compute_support_pickup_locations)

Extension points: `_get_pickup_locations`

## `product.product` (extends)


Extension points: `_get_free_qty`

## `product.template` (extends)


## `res.config.settings` (extends)

- `website_warehouse_id` Many2one → `stock.warehouse` (related=website_id.warehouse_id)

## `res.partner` (extends)

- `pickup_delivery_method_id` Many2one → `delivery.carrier`

Extension points: `_get_delivery_address_domain`

## `sale.order` (extends)

- `is_pickup_required` Boolean (related=carrier_id.support_pickup_locations)

Public methods: `action_open_delivery_wizard`, `set_pickup_location`, `write`

Extension points: `_get_checkout_delivery_address`, `_get_shop_warehouse_id`

## `stock.picking` (extends)

- `website_id` Many2one → `website` “Website” (readonly, store, related=sale_id.website_id)
- `is_pickup_required` Boolean (related=carrier_id.support_pickup_locations)

Public methods: `action_confirm`, `button_validate`, `set_pickup_location`, `write`

Extension points: `_check_pickup_location`

## `website` (extends)

- `warehouse_id` Many2one → `stock.warehouse` “Warehouse”

Extension points: `_get_product_available_qty`

## `choose.delivery.carrier` (extends)

- `is_pickup_required` Boolean (related=carrier_id.support_pickup_locations)
- `partner_shipping_id` Many2one → `res.partner` “Pickup Point”

Public methods: `button_confirm`, `set_pickup_location`
