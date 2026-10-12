# website_sale_picking — On site Payment & Picking

Depends on: website_sale_delivery, payment_custom.

## `delivery.carrier` (extends)

- `delivery_type` Selection
- `warehouse_id` Many2one → `stock.warehouse`

Public methods: `onsite_cancel_shipment`, `onsite_rate_shipment`, `onsite_send_shipping`

Extension points: `_check_warehouse_company`

## `payment.provider` (extends)

- `custom_mode` Selection

Extension points: `_get_compatible_providers`

## `res.config.settings` (extends)

- `picking_site_ids` Many2many → `delivery.carrier` (related=website_id.picking_site_ids)

## `website` (extends)

- `picking_site_ids` Many2many → `delivery.carrier` “Picking sites” (compute=_compute_picking_sites)
