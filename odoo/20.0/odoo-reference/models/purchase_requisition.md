# purchase_requisition — Purchase Agreements

Depends on: purchase.

## `product.supplierinfo` (extends)

- `purchase_requisition_id` Many2one → `purchase.requisition` “Agreement” (related=purchase_requisition_line_id.requisition_id)
- `purchase_requisition_line_id` Many2one → `purchase.requisition.line`

## `product.product` (extends)


Extension points: `_prepare_sellers`

## `purchase.order` (extends)

- `requisition_id` Many2one → `purchase.requisition` “Agreement”
- `requisition_type` Selection (related=requisition_id.requisition_type)

Public methods: `create`, `write`

Extension points: `_prepare_grouped_data`

## `purchase.order.line` (extends)


## `purchase.requisition` (defines)

Purchase Requisition

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Agreement” (required, readonly)
- `active` Boolean “Active”
- `reference` Char “Reference”
- `order_count` Integer “Number of Orders” (compute=_compute_orders_number)
- `vendor_id` Many2one → `res.partner` “Vendor”
- `requisition_type` Selection “Agreement Type” (required)
- `date_start` Date “Start Date”
- `date_end` Date “End Date”
- `user_id` Many2one → `res.users` “Purchase Representative”
- `description` Html
- `company_id` Many2one → `res.company` “Company” (required)
- `purchase_ids` One2many → `purchase.order` “Purchase Orders”
- `line_ids` One2many → `purchase.requisition.line` “Products to Purchase”
- `product_id` Many2one → `product.product` “Product” (related=line_ids.product_id)
- `state` Selection “Status” (required)
- `currency_id` Many2one → `res.currency` (required, store, compute=_compute_currency_id)

Public methods: `action_cancel`, `action_confirm`, `action_done`, `action_draft`, `create`, `unlink`, `write`

Extension points: `_check_dates`

## `purchase.requisition.line` (defines)

Purchase Requisition Line

Inherits: `analytic.mixin`

- `sequence` Integer “Sequence”
- `display_type` Selection
- `name` Text “Line Description”
- `product_id` Many2one → `product.product` “Product”
- `uom_id` Many2one → `uom.uom` (store, compute=_compute_uom_id)
- `product_qty` Float “Quantity”
- `product_description_variants` Char “Description”
- `price_unit` Float “Unit Price” (store, compute=_compute_price_unit)
- `price_subtotal` Monetary “Amount” (store, compute=_compute_price_subtotal)
- `qty_ordered` Float “Ordered” (compute=_compute_ordered_qty)
- `requisition_id` Many2one → `purchase.requisition` “Purchase Agreement” (required, index)
- `currency_id` Many2one → `res.currency` (related=requisition_id.currency_id)
- `company_id` Many2one → `res.company` “Company” (readonly, store, related=requisition_id.company_id)
- `supplier_info_ids` One2many → `product.supplierinfo`
- `parent_id` Many2one → `purchase.requisition.line` “Parent Section Line” (compute=_compute_parent_id)

Public methods: `create`, `unlink`, `write`

Extension points: `_check_line_type`, `_create_supplier_info`, `_get_display_line_vals`, `_get_section_lines`, `_get_section_totals`, `_prepare_purchase_order_line`
