# sale_management — Sales

Depends on: sale, digest.

## `digest.digest` (extends)

- `kpi_all_sale_total` Boolean “All Sales”
- `kpi_all_sale_total_value` Monetary (compute=_compute_kpi_sale_total_value)

## `res.company` (extends)

- `sale_order_template_id` Many2one → `sale.order.template` “Default Sale Template”

## `res.config.settings` (extends)

- `group_sale_order_template` Boolean “Quotation Templates”
- `company_so_template_id` Many2one “Default Template” (related=company_id.sale_order_template_id)

Public methods: `set_values`

## `sale.order` (extends)

- `sale_order_template_id` Many2one → `sale.order.template` “Quotation Template” (store, compute=_compute_sale_order_template_id)
- `sale_order_option_ids` One2many → `sale.order.option` “Optional Products Lines”

Public methods: `action_confirm`

Extension points: `_check_optional_product_company_id`, `_get_confirmation_template`

## `sale.order.line` (extends)

Sales Order Line

- `sale_order_option_ids` One2many → `sale.order.option`

## `sale.order.option` (defines)

Sale Options

- `order_id` Many2one → `sale.order` (index)
- `product_id` Many2one → `product.product` (required)
- `line_id` Many2one → `sale.order.line`
- `sequence` Integer “Sequence”
- `name` Text “Description” (required, store, compute=_compute_name)
- `quantity` Float “Quantity” (required)
- `uom_id` Many2one → `uom.uom` “Unit of Measure” (required, store, compute=_compute_uom_id)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `price_unit` Float “Unit Price” (required, store, compute=_compute_price_unit)
- `discount` Float “Discount (%)” (store, compute=_compute_discount)
- `is_present` Boolean “Present on Quotation” (compute=_compute_is_present)

Public methods: `add_option_to_order`, `button_add_to_order`

Extension points: `_get_values_to_add_to_order`

## `sale.order.template` (defines)

Quotation Template

- `active` Boolean
- `company_id` Many2one → `res.company`
- `name` Char “Quotation Template” (required)
- `note` Html “Terms and conditions”
- `mail_template_id` Many2one → `mail.template` “Confirmation Mail”
- `number_of_days` Integer “Quotation Duration”
- `require_signature` Boolean “Online Signature” (store, compute=_compute_require_signature)
- `require_payment` Boolean “Online Payment” (store, compute=_compute_require_payment)
- `prepayment_percent` Float “Prepayment percentage” (store, compute=_compute_prepayment_percent)
- `sale_order_template_line_ids` One2many → `sale.order.template.line` “Lines”
- `sale_order_template_option_ids` One2many → `sale.order.template.option` “Optional Products”
- `journal_id` Many2one → `account.journal` “Invoicing Journal” (company_dependent)

Public methods: `create`, `write`

Extension points: `_check_company_id`, `_check_prepayment_percent`

## `sale.order.template.line` (defines)

Quotation Template Line

- `sale_order_template_id` Many2one → `sale.order.template` “Quotation Template Reference” (required, index)
- `sequence` Integer “Sequence”
- `company_id` Many2one (store, index, related=sale_order_template_id.company_id)
- `product_id` Many2one → `product.product`
- `name` Text “Description” (required, store, compute=_compute_name)
- `product_uom_id` Many2one → `uom.uom` “Unit of Measure” (store, compute=_compute_product_uom_id)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `product_uom_qty` Float “Quantity” (required)
- `display_type` Selection

Public methods: `create`, `write`

Extension points: `_prepare_order_line_values`

## `sale.order.template.option` (defines)

Quotation Template Option

- `sale_order_template_id` Many2one → `sale.order.template` “Quotation Template Reference” (required, index)
- `company_id` Many2one (store, index, related=sale_order_template_id.company_id)
- `product_id` Many2one → `product.product` (required)
- `name` Text “Description” (required, store, compute=_compute_name)
- `uom_id` Many2one → `uom.uom` “Unit of Measure” (required, store, compute=_compute_uom_id)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `quantity` Float “Quantity” (required)

Extension points: `_prepare_option_line_values`
