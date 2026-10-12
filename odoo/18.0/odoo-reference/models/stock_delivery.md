# stock_delivery — Delivery - Stock

Depends on: sale_stock, delivery.

## `delivery.carrier` (extends)

- `invoice_policy` Selection
- `route_ids` Many2many → `stock.route`

Public methods: `base_on_rule_cancel_shipment`, `base_on_rule_get_tracking_link`, `base_on_rule_send_shipping`, `cancel_shipment`, `fixed_cancel_shipment`, `fixed_get_tracking_link`, `fixed_send_shipping`, `get_return_label`, `get_return_label_prefix`, `get_tracking_link`, `send_shipping`

Extension points: `_get_commodities_from_order`, `_get_commodities_from_stock_move_lines`, `_get_default_custom_package_code`, `_get_delivery_doc_prefix`, `_get_delivery_label_prefix`, `_get_packages_from_order`, `_get_packages_from_picking`

## `product.template` (extends)

- `hs_code` Char “HS Code”
- `country_of_origin` Many2one → `res.country`

## `sale.order` (extends)


Public methods: `set_delivery_line`

Extension points: `_create_delivery_line`

## `sale.order.line` (extends)


Extension points: `_get_protected_fields`, `_prepare_procurement_values`

## `stock.route` (extends)

- `shipping_selectable` Boolean “Applicable on Shipping Methods”

## `stock.move` (extends)

- `weight` Float (store, compute=_cal_move_weight)

Extension points: `_get_new_picking_values`

## `stock.move.line` (extends)

- `sale_price` Float (compute=_compute_sale_price)
- `destination_country_code` Char (related=picking_id.destination_country_code)
- `carrier_id` Many2one (store, related=picking_id.carrier_id)

Extension points: `_get_aggregated_product_quantities`

## `stock.package.type` (extends)

- `shipper_package_code` Char “Carrier Code”
- `package_carrier_type` Selection “Carrier”

## `stock.picking` (extends)

- `carrier_price` Float “Shipping Cost”
- `delivery_type` Selection (readonly, related=carrier_id.delivery_type)
- `carrier_id` Many2one → `delivery.carrier` “Carrier”
- `weight` Float (store, compute=_cal_weight)
- `carrier_tracking_ref` Char “Tracking Reference”
- `carrier_tracking_url` Char “Tracking URL” (compute=_compute_carrier_tracking_url)
- `weight_uom_name` Char “Weight unit of measure label” (readonly, compute=_compute_weight_uom_name)
- `is_return_picking` Boolean (compute=_compute_return_picking)
- `return_label_ids` One2many → `ir.attachment` (compute=_compute_return_label)
- `destination_country_code` Char “Destination Country” (related=partner_id.country_id.code)

Public methods: `button_validate`, `cancel_shipment`, `get_multiple_carrier_tracking`, `open_website_url`, `print_return_label`, `send_to_shipper`

Extension points: `_check_carrier_details_compliance`, `_get_default_weight_uom`, `_get_estimated_weight`, `_get_matching_delivery_lines`, `_prepare_sale_delivery_line_vals`

## `stock.quant.package` (extends)

- `weight` Float (compute=_compute_weight)
- `weight_uom_name` Char “Weight unit of measure label” (readonly, compute=_compute_weight_uom_name)
- `weight_is_kg` Boolean “Technical field indicating whether weight uom is kg or not (i.e. lb)” (compute=_compute_weight_is_kg)
- `weight_uom_rounding` Float “Technical field indicating weight's number of decimal places” (compute=_compute_weight_is_kg)

Extension points: `_get_default_weight_uom`

## `choose.delivery.carrier` (extends)


## `choose.delivery.package` (defines)

Delivery Package Selection Wizard

- `picking_id` Many2one → `stock.picking`
- `delivery_package_type_id` Many2one → `stock.package.type`
- `shipping_weight` Float “Shipping Weight” (store, compute=_compute_shipping_weight)
- `weight_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_uom_name)
- `company_id` Many2one (related=picking_id.company_id)

Public methods: `action_put_in_pack`

## `stock.return.picking` (extends)


Extension points: `_create_return`
