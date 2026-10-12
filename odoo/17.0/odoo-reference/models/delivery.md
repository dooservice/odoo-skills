# delivery — Delivery Costs

Depends on: sale.

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
- `currency_id` Many2one (related=product_id.currency_id)
- `invoice_policy` Selection “Invoicing Policy” (required)
- `country_ids` Many2many → `res.country`
- `state_ids` Many2many → `res.country.state`
- `zip_prefix_ids` Many2many → `delivery.zip.prefix`
- `carrier_description` Text “Carrier Description”
- `margin` Float
- `fixed_margin` Float
- `free_over` Boolean “Free if order amount is above”
- `amount` Float “Amount”
- `can_generate_return` Boolean (compute=_compute_can_generate_return)
- `return_label_on_delivery` Boolean “Generate Return Label”
- `get_return_label_from_portal` Boolean “Return Label Accessible from Customer Portal”
- `supports_shipping_insurance` Boolean (compute=_compute_supports_shipping_insurance)
- `shipping_insurance` Integer “Insurance Percentage”
- `price_rule_ids` One2many → `delivery.price.rule`
- `fixed_price` Float “Fixed Price” (store, compute=_compute_fixed_price)

Public methods: `available_carriers`, `base_on_rule_rate_shipment`, `copy`, `fixed_rate_shipment`, `install_more_provider`, `log_xml`, `rate_shipment`, `toggle_debug`, `toggle_prod_environment`

Extension points: `_get_conversion_currencies`, `_get_delivery_type`, `_get_price_available`, `_get_price_dict`, `_get_price_from_picking`

## `delivery.price.rule` (defines)

Delivery Price Rules

- `name` Char (compute=_compute_name)
- `sequence` Integer (required)
- `carrier_id` Many2one → `delivery.carrier` (required)
- `currency_id` Many2one (related=carrier_id.currency_id)
- `variable` Selection (required)
- `operator` Selection (required)
- `max_value` Float “Maximum Value” (required)
- `list_base_price` Float “Sale Base Price” (required)
- `list_price` Float “Sale Price” (required)
- `variable_factor` Selection “Variable Factor” (required)

## `delivery.zip.prefix` (defines)

Delivery Zip Prefix

- `name` Char “Prefix” (required)

Public methods: `create`, `write`

## `product.category` (extends)


## `res.partner` (extends)

- `property_delivery_carrier_id` Many2one → `delivery.carrier` “Delivery Method” (company_dependent)

## `sale.order` (extends)

- `carrier_id` Many2one → `delivery.carrier` “Delivery Method”
- `delivery_message` Char (readonly)
- `delivery_rating_success` Boolean
- `delivery_set` Boolean (compute=_compute_delivery_state)
- `recompute_delivery_price` Boolean “Delivery cost should be recomputed”
- `is_all_service` Boolean “Service Product” (compute=_compute_is_service_products)
- `shipping_weight` Float “Shipping Weight” (store, compute=_compute_shipping_weight)

Public methods: `action_open_delivery_wizard`, `onchange_order_line`, `set_delivery_line`

Extension points: `_create_delivery_line`, `_get_estimated_weight`, `_get_update_prices_lines`, `_prepare_delivery_line_vals`

## `sale.order.line` (extends)

- `is_delivery` Boolean “Is a Delivery”
- `product_qty` Float “Product Qty” (compute=_compute_product_qty)
- `recompute_delivery_price` Boolean (related=order_id.recompute_delivery_price)

Public methods: `unlink`

Extension points: `_check_line_unlink`

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
- `total_weight` Float “Total Order Weight” (related=order_id.shipping_weight)
- `weight_uom_name` Char (readonly)

Public methods: `button_confirm`, `update_price`

Extension points: `_get_default_weight_uom`, `_get_shipment_rate`
