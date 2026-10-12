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

Public methods: `action_confirm`

Extension points: `_get_confirmation_template`

## `sale.order.line` (extends)

Sales Order Line

- `is_optional` Boolean “Optional Line”

## `sale.order.template` (defines)

Quotation Template

- `active` Boolean
- `company_id` Many2one → `res.company`
- `name` Char “Quotation Template” (required)
- `note` Html “Terms and conditions”
- `sequence` Integer
- `mail_template_id` Many2one → `mail.template` “Confirmation Mail”
- `number_of_days` Integer “Quotation Duration”
- `require_signature` Boolean “Online Signature” (store, compute=_compute_require_signature)
- `require_payment` Boolean “Online Payment” (store, compute=_compute_require_payment)
- `prepayment_percent` Float “Prepayment percentage” (store, compute=_compute_prepayment_percent)
- `sale_order_template_line_ids` One2many → `sale.order.template.line` “Lines”
- `journal_id` Many2one → `account.journal` “Invoicing Journal” (company_dependent)

Public methods: `create`, `write`

Extension points: `_check_company_id`, `_check_prepayment_percent`

## `sale.order.template.line` (defines)

Quotation Template Line

- `sale_order_template_id` Many2one → `sale.order.template` “Quotation Template Reference” (required, index)
- `sequence` Integer “Sequence”
- `company_id` Many2one (store, index, related=sale_order_template_id.company_id)
- `product_id` Many2one → `product.product`
- `name` Text “Description”
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `product_uom_id` Many2one → `uom.uom` “Unit” (store, compute=_compute_product_uom_id)
- `product_uom_qty` Float “Quantity” (required)
- `display_type` Selection
- `parent_id` Many2one → `sale.order.template.line` “Parent Section Line” (compute=_compute_parent_id)
- `is_optional` Boolean “Optional Line”

Public methods: `create`, `write`

Extension points: `_prepare_order_line_values`
