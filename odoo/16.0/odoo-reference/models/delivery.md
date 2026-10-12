# delivery — Delivery Costs

Depends on: sale_stock, sale_management.

## `delivery.carrier` (defines)

Shipping Methods

- `name` Char “Delivery Method” (required)
- `active` Boolean
- `sequence` Integer
- `delivery_type` Selection “Provider” (required)
- `integration_level` Selection “Integration Level”
- `prod_environment` Boolean “Environment”
- `debug_logging` Boolean “Debug logging”
- `company_id` Many2one → `res.company` “Company” (store, related=product_id.company_id)
- `product_id` Many2one → `product.product` “Delivery Product” (required)
- `invoice_policy` Selection “Invoicing Policy” (required)
- `country_ids` Many2many → `res.country`
- `state_ids` Many2many → `res.country.state`
- `zip_prefix_ids` Many2many → `delivery.zip.prefix`
- `carrier_description` Text “Carrier Description”
- `margin` Float
- `free_over` Boolean “Free if order amount is above”
- `amount` Float “Amount”
- `can_generate_return` Boolean (compute=_compute_can_generate_return)
- `return_label_on_delivery` Boolean “Generate Return Label”
- `get_return_label_from_portal` Boolean “Return Label Accessible from Customer Portal”
- `supports_shipping_insurance` Boolean (compute=_compute_supports_shipping_insurance)
- `shipping_insurance` Integer “Insurance Percentage”
- `fixed_price` Float “Fixed Price” (store, compute=_compute_fixed_price)

Public methods: `available_carriers`, `cancel_shipment`, `fixed_cancel_shipment`, `fixed_get_tracking_link`, `fixed_rate_shipment`, `fixed_send_shipping`, `get_return_label`, `get_return_label_prefix`, `get_tracking_link`, `install_more_provider`, `log_xml`, `onchange_countries`, `onchange_states`, `rate_shipment`, `send_shipping`, `toggle_debug`, `toggle_prod_environment`

Extension points: `_get_commodities_from_order`, `_get_commodities_from_stock_move_lines`, `_get_default_custom_package_code`, `_get_delivery_type`, `_get_packages_from_order`, `_get_packages_from_picking`

## `delivery.price.rule` (defines)

Delivery Price Rules

- `name` Char (compute=_compute_name)
- `sequence` Integer (required)
- `carrier_id` Many2one → `delivery.carrier` (required)
- `variable` Selection (required)
- `operator` Selection (required)
- `max_value` Float “Maximum Value” (required)
- `list_base_price` Float “Sale Base Price” (required)
- `list_price` Float “Sale Price” (required)
- `variable_factor` Selection (required)

## `delivery.carrier` (extends)

- `delivery_type` Selection
- `price_rule_ids` One2many → `delivery.price.rule`

Public methods: `base_on_rule_cancel_shipment`, `base_on_rule_get_tracking_link`, `base_on_rule_rate_shipment`, `base_on_rule_send_shipping`

Extension points: `_get_conversion_currencies`, `_get_price_available`, `_get_price_dict`, `_get_price_from_picking`

## `delivery.zip.prefix` (defines)

Delivery Zip Prefix

- `name` Char “Prefix” (required)

Public methods: `create`, `write`

## `res.partner` (extends)

- `property_delivery_carrier_id` Many2one → `delivery.carrier` “Delivery Method” (company_dependent)

## `product.category` (extends)


## `product.template` (extends)

- `hs_code` Char “HS Code”
- `country_of_origin` Many2one → `res.country`

## `sale.order` (extends)

- `carrier_id` Many2one → `delivery.carrier` “Delivery Method”
- `delivery_message` Char (readonly)
- `delivery_rating_success` Boolean
- `delivery_set` Boolean (compute=_compute_delivery_state)
- `recompute_delivery_price` Boolean “Delivery cost should be recomputed”
- `is_all_service` Boolean “Service Product” (compute=_compute_is_service_products)

Public methods: `action_open_delivery_wizard`, `onchange_order_line`, `set_delivery_line`

Extension points: `_create_delivery_line`, `_get_estimated_weight`, `_get_lines_impacting_invoice_status`, `_get_update_prices_lines`, `_prepare_delivery_line_vals`

## `sale.order.line` (extends)

- `is_delivery` Boolean “Is a Delivery”
- `product_qty` Float “Product Qty” (compute=_compute_product_qty)
- `recompute_delivery_price` Boolean (related=order_id.recompute_delivery_price)

Public methods: `unlink`

Extension points: `_check_line_unlink`

## `stock.move` (extends)

- `weight` Float (store, compute=_cal_move_weight)

Extension points: `_get_new_picking_values`

## `stock.move.line` (extends)

- `sale_price` Float (compute=_compute_sale_price)
- `destination_country_code` Char (related=picking_id.destination_country_code)
- `carrier_id` Many2one (related=picking_id.carrier_id)
- `carrier_name` Char “Carrier Name” (readonly, store, related=picking_id.carrier_id.name)

Extension points: `_get_aggregated_product_quantities`

## `stock.package.type` (extends)

- `shipper_package_code` Char “Carrier Code”
- `package_carrier_type` Selection “Carrier”

## `stock.quant.package` (extends)

- `weight` Float (compute=_compute_weight)
- `weight_uom_name` Char “Weight unit of measure label” (readonly, compute=_compute_weight_uom_name)
- `weight_is_kg` Boolean “Technical field indicating whether weight uom is kg or not (i.e. lb)” (compute=_compute_weight_is_kg)
- `weight_uom_rounding` Float “Technical field indicating weight's number of decimal places” (compute=_compute_weight_is_kg)
- `shipping_weight` Float “Shipping Weight”

Extension points: `_get_default_weight_uom`

## `stock.picking` (extends)

- `carrier_price` Float “Shipping Cost”
- `delivery_type` Selection (readonly, related=carrier_id.delivery_type)
- `carrier_id` Many2one → `delivery.carrier` “Carrier”
- `weight` Float (store, compute=_cal_weight)
- `carrier_tracking_ref` Char “Tracking Reference”
- `carrier_tracking_url` Char “Tracking URL” (compute=_compute_carrier_tracking_url)
- `weight_uom_name` Char “Weight unit of measure label” (readonly, compute=_compute_weight_uom_name)
- `package_ids` Many2many → `stock.quant.package` “Packages” (compute=_compute_packages)
- `weight_bulk` Float “Bulk Weight” (compute=_compute_bulk_weight)
- `shipping_weight` Float “Weight for Shipping” (compute=_compute_shipping_weight)
- `is_return_picking` Boolean (compute=_compute_return_picking)
- `return_label_ids` One2many → `ir.attachment` (compute=_compute_return_label)
- `destination_country_code` Char “Destination Country” (related=partner_id.country_id.code)

Public methods: `cancel_shipment`, `get_multiple_carrier_tracking`, `open_website_url`, `print_return_label`, `send_to_shipper`

Extension points: `_check_carrier_details_compliance`, `_get_default_weight_uom`, `_get_estimated_weight`, `_get_matching_delivery_lines`, `_prepare_sale_delivery_line_vals`

## `stock.return.picking` (extends)


Extension points: `_create_returns`

## `choose.delivery.carrier` (defines)

Delivery Carrier Selection Wizard

- `order_id` Many2one → `sale.order` (required)
- `partner_id` Many2one → `res.partner` (required, related=order_id.partner_id)
- `carrier_id` Many2one → `delivery.carrier` “Shipping Method” (required)
- `delivery_type` Selection (related=carrier_id.delivery_type)
- `delivery_price` Float
- `display_price` Float “Cost” (readonly)
- `currency_id` Many2one → `res.currency` (related=order_id.currency_id)
- `company_id` Many2one → `res.company` (related=order_id.company_id)
- `available_carrier_ids` Many2many → `delivery.carrier` “Available Carriers” (compute=_compute_available_carrier)
- `invoicing_message` Text (compute=_compute_invoicing_message)
- `delivery_message` Text (readonly)

Public methods: `button_confirm`, `update_price`

Extension points: `_get_shipment_rate`

## `choose.delivery.package` (defines)

Delivery Package Selection Wizard

- `picking_id` Many2one → `stock.picking`
- `delivery_package_type_id` Many2one → `stock.package.type`
- `shipping_weight` Float “Shipping Weight” (store, compute=_compute_shipping_weight)
- `weight_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_uom_name)
- `company_id` Many2one (related=picking_id.company_id)

Public methods: `action_put_in_pack`
