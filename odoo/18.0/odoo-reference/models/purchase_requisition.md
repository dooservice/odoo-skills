# purchase_requisition — Purchase Agreements

Depends on: purchase.

## `product.supplierinfo` (extends)

- `purchase_requisition_id` Many2one → `purchase.requisition` “Agreement” (related=purchase_requisition_line_id.requisition_id)
- `purchase_requisition_line_id` Many2one → `purchase.requisition.line`

## `product.product` (extends)


Extension points: `_prepare_sellers`

## `purchase.order.group` (defines)

Technical model to group PO for call to tenders

- `order_ids` One2many → `purchase.order`

Public methods: `write`

## `purchase.order` (extends)

- `requisition_id` Many2one → `purchase.requisition` “Agreement”
- `requisition_type` Selection (related=requisition_id.requisition_type)
- `purchase_group_id` Many2one → `purchase.order.group`
- `alternative_po_ids` One2many → `purchase.order` “Alternative POs” (related=purchase_group_id.order_ids)
- `has_alternatives` Boolean “Has Alternatives” (compute=_compute_has_alternatives)

Public methods: `action_compare_alternative_lines`, `action_create_alternative`, `button_confirm`, `create`, `get_tender_best_lines`, `write`

Extension points: `_prepare_grouped_data`

## `purchase.order.line` (extends)

- `price_total_cc` Monetary “Company Subtotal” (store, compute=_compute_price_total_cc)
- `company_currency_id` Many2one “Company Currency” (related=company_id.currency_id)

Public methods: `action_choose`, `action_clear_quantities`

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

- `product_id` Many2one → `product.product` “Product” (required)
- `product_uom_id` Many2one → `uom.uom` (store, compute=_compute_product_uom_id)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `product_qty` Float “Quantity”
- `product_description_variants` Char “Description”
- `price_unit` Float “Unit Price” (store, compute=_compute_price_unit)
- `qty_ordered` Float “Ordered” (compute=_compute_ordered_qty)
- `requisition_id` Many2one → `purchase.requisition` “Purchase Agreement” (required)
- `company_id` Many2one → `res.company` “Company” (readonly, store, related=requisition_id.company_id)
- `supplier_info_ids` One2many → `product.supplierinfo`

Public methods: `create`, `unlink`, `write`

Extension points: `_create_supplier_info`, `_prepare_purchase_order_line`

## `res.config.settings` (extends)

- `group_purchase_alternatives` Boolean “Purchase Alternatives”

## `purchase.requisition.alternative.warning` (defines)

Wizard in case PO still has open alternative requests for quotation

- `po_ids` Many2many → `purchase.order` “POs to Confirm”
- `alternative_po_ids` Many2many → `purchase.order` “Alternative POs”

Public methods: `action_cancel_alternatives`, `action_keep_alternatives`

Extension points: `_action_done`

## `purchase.requisition.create.alternative` (defines)

Wizard to preset values for alternative PO

- `origin_po_id` Many2one → `purchase.order`
- `partner_id` Many2one → `res.partner` “Vendor” (required)
- `creation_blocked` Boolean (compute=_compute_purchase_warn)
- `purchase_warn_msg` Text “Warning Messages” (compute=_compute_purchase_warn)
- `copy_products` Boolean “Copy Products”

Public methods: `action_create_alternative`

Extension points: `_get_alternative_line_value`, `_get_alternative_values`
