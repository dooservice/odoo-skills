# website_sale_picking — On site Payment & Picking

Depends on: website_sale, stock, payment_custom.

## `delivery.carrier` (extends)

- `delivery_type` Selection
- `warehouse_id` Many2one → `stock.warehouse`

Public methods: `onsite_cancel_shipment`, `onsite_rate_shipment`, `onsite_send_shipping`

Extension points: `_check_warehouse_company`

## `payment.provider` (extends)

- `custom_mode` Selection

Extension points: `_get_compatible_providers`, `_get_default_payment_method_codes`

## `res.config.settings` (extends)

- `picking_site_ids` Many2many → `delivery.carrier` (related=website_id.picking_site_ids)

## `sale.order` (extends)


## `website` (extends)

- `picking_site_ids` Many2many → `delivery.carrier` “Picking sites” (compute=_compute_picking_sites)
