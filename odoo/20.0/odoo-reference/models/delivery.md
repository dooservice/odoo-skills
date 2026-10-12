# delivery — Delivery Costs

Depends on: sale, payment_custom.

## `delivery.carrier` (defines)

Delivery Method

- `name` Char “Delivery Method” (required)
- `active` Boolean
- `sequence` Integer
- `delivery_type` Selection “Provider” (required)
- `supports_cash_on_delivery` Boolean (compute=_compute_supports_cash_on_delivery)
- `allow_cash_on_delivery` Boolean “Cash on Delivery”
- `integration_level` Selection
- `prod_environment` Boolean “Environment”
- `debug_logging` Boolean “Debug logging”
- `company_id` Many2one → `res.company` (store, related=product_id.company_id)
- `product_id` Many2one → `product.product` “Delivery Product” (required)
- `tracking_url` Char “Tracking Link”
- `currency_id` Many2one (related=product_id.currency_id)
- `invoice_policy` Selection “Invoicing Policy” (required)
- `country_ids` Many2many → `res.country` “Countries”
- `state_ids` Many2many → `res.country.state` “States”
- `zip_prefix_ids` Many2many → `delivery.zip.prefix` “Zip Prefixes”
- `max_weight` Float
- `weight_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_uom_name)
- `max_volume` Float
- `volume_uom_name` Char “Volume unit of measure label” (compute=_compute_volume_uom_name)
- `must_have_tag_ids` Many2many → `product.tag` “Must Have Tags”
- `excluded_tag_ids` Many2many → `product.tag` “Excluded Tags”
- `carrier_description` Text “Description”
- `margin` Float
- `fixed_margin` Float
- `free_over` Boolean “Free if order amount is above”
- `amount` Float
- `can_generate_return` Boolean (compute=_compute_can_generate_return)
- `return_label_on_delivery` Boolean “Generate Return Label”
- `get_return_label_from_portal` Boolean “Return Label Accessible from Customer Portal”
- `supports_shipping_insurance` Boolean (compute=_compute_supports_shipping_insurance)
- `shipping_insurance` Integer “Insurance Percentage”
- `price_rule_ids` One2many → `delivery.price.rule` “Pricing Rules”
- `delivery_cost` Monetary “Cost” (readonly, compute=_compute_delivery_cost)
- `delivery_currency_id` Many2one → `res.currency` (compute=_compute_delivery_currency_id)
- `fixed_price` Float “Fixed Price” (store, compute=_compute_fixed_price)

Public methods: `available_carriers`, `base_on_rule_rate_shipment`, `fixed_rate_shipment`, `install_more_provider`, `log_xml`, `rate_shipment`, `toggle_debug`, `toggle_prod_environment`, `write`

Extension points: `_check_tags`, `_get_conversion_currencies`, `_get_delivery_type`, `_get_price_available`, `_get_price_dict`, `_get_price_from_picking`

## `delivery.price.rule` (defines)

Delivery Price Rules

- `name` Char (compute=_compute_name)
- `sequence` Integer (required)
- `carrier_id` Many2one → `delivery.carrier` (required, index)
- `currency_id` Many2one (related=carrier_id.currency_id)
- `variable` Selection (required)
- `operator` Selection (required)
- `max_value` Float “Maximum Value” (required)
- `variable_unit` Char (compute=_compute_variable_unit)
- `list_base_price` Float “Sale Base Price” (required)
- `list_price` Float “Sale Price” (required)
- `variable_factor` Selection (required)

## `delivery.zip.prefix` (defines)

Delivery Zip Prefix

- `name` Char “Prefix” (required)

Public methods: `create`, `write`

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `ir.module.module` (extends)


Public methods: `action_view_delivery_methods`

## `payment.method` (extends)


Extension points: `_get_pay_on_delivery_method_codes`

## `payment.provider` (extends)

- `custom_mode` Selection

Public methods: `copy_data`

Extension points: `_get_default_payment_method_codes`, `_get_pay_on_delivery_provider_codes`

## `payment.transaction` (extends)


Extension points: `_post_process`

## `product.category` (extends)


## `res.partner` (extends)

- `property_delivery_carrier_id` Many2one → `delivery.carrier` “Delivery Method” (company_dependent)

## `sale.order` (extends)

- `carrier_id` Many2one → `delivery.carrier` “Delivery Method”
- `delivery_message` Char (readonly)
- `delivery_set` Boolean (compute=_compute_delivery_state)
- `recompute_delivery_price` Boolean “Delivery cost should be recomputed”
- `is_all_service` Boolean “Service Product” (compute=_compute_is_service_products)
- `shipping_weight` Float (store, compute=_compute_shipping_weight)

Public methods: `action_open_delivery_note_wizard`, `action_open_delivery_wizard`, `onchange_order_line`, `set_delivery_line`

Extension points: `_create_delivery_line`, `_get_estimated_weight`, `_get_update_prices_lines`, `_prepare_delivery_line_vals`

## `sale.order.line` (extends)

- `is_delivery` Boolean “Is a Delivery”
- `product_qty` Float “Product Qty” (compute=_compute_product_qty)
- `recompute_delivery_price` Boolean (related=order_id.recompute_delivery_price)

Public methods: `unlink`

Extension points: `_check_line_unlink`, `_get_accrual_domain`, `_get_invalid_delivery_weight_lines`

## `choose.delivery.carrier` (defines)

Delivery Method Selection Wizard

- `order_id` Many2one → `sale.order` (required)
- `partner_id` Many2one → `res.partner` (required, related=order_id.partner_id)
- `carrier_id` Many2one → `delivery.carrier` “Delivery Method” (required)
- `carrier_prices` Json
- `carrier_prices_dumped` Char
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
- `is_loading_prices` Boolean
- `show_delivery_rates_button` Integer “Number of carriers” (compute=_compute_show_delivery_rates_button)

Public methods: `button_confirm`, `get_wizard_carrier_rate`, `update_price`

Extension points: `_get_carrier_delivery_rate`, `_get_default_weight_uom`

## `delivery.note.wizard` (defines)

Delivery Note Wizard

- `name` Char “Note Reference”
- `note_line_ids` One2many → `delivery.note.wizard.line` “Operations”
- `dm_id` Many2one → `delivery.carrier` “Delivery method”
- `tracking_ref` Char “Tracking Reference”
- `tracking_url` Char “Tracking URL” (compute=_compute_tracking_url)
- `shipping_date` Date “Shipping Date”
- `so_id` Many2one → `sale.order` “Sales Order”
- `so_reference` Char “Order reference” (related=so_id.name)
- `company_id` Many2one (related=so_id.company_id)
- `partner_id` Many2one → `res.partner` (related=so_id.partner_id)

Public methods: `action_confirm`

Extension points: `_get_report_lang`

## `delivery.note.wizard.line` (defines)

Delivery Note Line

- `note_id` Many2one → `delivery.note.wizard` “Delivery Note Reference”
- `sol_id` Many2one → `sale.order.line` “Source Sale Order Line”
- `product_id` Many2one → `product.product` (related=sol_id.product_id)
- `product_image` Image (related=product_id.image_128)
- `product_uom_id` Many2one → `uom.uom` (related=sol_id.product_uom_id)
- `product_uom_qty` Float “Quantity” (store, compute=_compute_product_uom_qty)
- `remaining_qty_to_ship` Float (compute=_compute_remaining_qty_to_ship)

## `res.config.settings` (extends)


Public methods: `action_install_more_provider`
