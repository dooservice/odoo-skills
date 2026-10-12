# sale_management — Sales

Depends on: sale, digest.

## `digest.digest` (extends)

- `kpi_all_sale_total` Boolean “All Sales”
- `kpi_all_sale_total_value` Monetary (compute=_compute_kpi_sale_total_value)

Extension points: `_get_kpi_custom_settings`

## `product.attribute.custom.value` (extends)

- `sale_order_template_line_id` Many2one → `sale.order.template.line` “Quotation Template Line”

## `sale.order` (extends)

- `sale_order_template_id` Many2one → `sale.order.template` “Template” (store)

Public methods: `action_confirm`, `action_create_quotation_template`

Extension points: `_get_confirmation_template`, `_prepare_template_order_values`

## `sale.order.line` (extends)

- `is_optional` Boolean “Optional Line”

Public methods: `save_section_template`

Extension points: `_prepare_template_line_values`

## `sale.order.template` (defines)

Order Templates

Inherits: `product.catalog.mixin`

- `active` Boolean
- `company_id` Many2one → `res.company`
- `currency_id` Many2one → `res.currency` “Currency”
- `name` Char “Template” (required)
- `note` Html “Terms and conditions”
- `sequence` Integer
- `template_type` Selection “Type” (required)
- `mail_template_id` Many2one → `mail.template` “Confirmation Mail”
- `number_of_days` Integer “Quotation Duration”
- `require_signature` Boolean “Online Signature” (store, compute=_compute_require_signature)
- `prepayment_percent` Float “Prepayment” (store, compute=_compute_prepayment_percent)
- `sale_order_template_line_ids` One2many → `sale.order.template.line` “Lines”
- `journal_id` Many2one → `account.journal` “Journal” (company_dependent)
- `share_template` Boolean “Share”
- `team_ids` Many2many → `crm.team` “Sales Team”
- `user_has_access` Boolean “Can User access” (compute=_compute_user_has_access)
- `has_productless_lines` Boolean (compute=_compute_has_productless_lines)

Public methods: `get_section_templates`, `prepare_section_template_order_lines`, `unlink_section_template`

Extension points: `_check_company_id`, `_check_prepayment_percent`, `_get_catalog_currency`, `_get_product_catalog_domain`

## `sale.order.template.line` (defines)

Quotation Template Line

Inherits: `product.catalog.line.mixin`

- `sale_order_template_id` Many2one → `sale.order.template` “Quotation Template Reference” (required, index)
- `sequence` Integer “Sequence”
- `company_id` Many2one (store, index, related=sale_order_template_id.company_id)
- `product_id` Many2one → `product.product`
- `product_template_id` Many2one → `product.template` “Product Template” (compute=_compute_product_template_id)
- `product_template_attribute_value_ids` Many2many (related=product_id.product_template_attribute_value_ids)
- `product_custom_attribute_value_ids` One2many → `product.attribute.custom.value` “Custom Values” (store, compute=_compute_custom_attribute_values)
- `product_no_variant_attribute_value_ids` Many2many → `product.template.attribute.value` “Extra Values” (store, compute=_compute_no_variant_attribute_values)
- `is_configurable_product` Boolean “Is the product configurable?” (related=product_template_id.has_configurable_attributes)
- `name` Text “Description” (store, compute=_compute_name)
- `label` Text “Label” (compute=_compute_label)
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `product_uom_id` Many2one → `uom.uom` “Unit” (store, compute=_compute_product_uom_id)
- `product_uom_qty` Float “Quantity” (required)
- `display_type` Selection
- `parent_id` Many2one → `sale.order.template.line` “Parent Section Line” (compute=_compute_parent_id)
- `is_optional` Boolean “Optional Line”
- `collapse_composition` Boolean
- `collapse_prices` Boolean
- `section_qty` Float “Section Quantity” (store, compute=_compute_section_qty)
- `section_uom_id` Many2one → `uom.uom` “Section Unit of Measure” (store, compute=_compute_section_uom_id)
- `discount` Float “Discount (%)”
- `price_unit` Float “Unit Price”
- `tax_ids` Many2many → `account.tax` “Taxes”
- `mandatory_product` Boolean “Is Product Mandatory” (compute=_compute_mandatory_product)

Public methods: `action_add_from_catalog`, `create`, `write`

Extension points: `_get_default_description`, `_get_product_uom_field`, `_get_quantity_field`, `_get_sale_order_line_multiline_description_variants`, `_get_section_lines`, `_prepare_order_line_values`

## `res.config.settings` (extends)


Public methods: `set_values`
