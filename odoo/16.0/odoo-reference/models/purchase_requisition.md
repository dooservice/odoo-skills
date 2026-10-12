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

- `requisition_id` Many2one → `purchase.requisition` “Purchase Agreement”
- `is_quantity_copy` Selection (related=requisition_id.is_quantity_copy)
- `purchase_group_id` Many2one → `purchase.order.group`
- `alternative_po_ids` One2many → `purchase.order` “Alternative POs” (related=purchase_group_id.order_ids)
- `has_alternatives` Boolean “Has Alternatives” (compute=_compute_has_alternatives)

Public methods: `action_compare_alternative_lines`, `action_create_alternative`, `button_confirm`, `create`, `get_tender_best_lines`, `write`

## `purchase.order.line` (extends)


Public methods: `action_choose`, `action_clear_quantities`

## `purchase.requisition.type` (defines)

Purchase Requisition Type

- `name` Char “Agreement Type” (required)
- `sequence` Integer
- `exclusive` Selection “Agreement Selection Type” (required)
- `quantity_copy` Selection “Quantities” (required)
- `line_copy` Selection “Lines” (required)
- `active` Boolean

## `purchase.requisition` (defines)

Purchase Requisition

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Reference” (required, readonly)
- `origin` Char “Source Document”
- `order_count` Integer “Number of Orders” (compute=_compute_orders_number)
- `vendor_id` Many2one → `res.partner` “Vendor”
- `type_id` Many2one → `purchase.requisition.type` “Agreement Type” (required)
- `ordering_date` Date “Ordering Date”
- `date_end` Datetime “Agreement Deadline”
- `schedule_date` Date “Delivery Date” (index)
- `user_id` Many2one → `res.users` “Purchase Representative”
- `description` Html
- `company_id` Many2one → `res.company` “Company” (required)
- `purchase_ids` One2many → `purchase.order` “Purchase Orders”
- `line_ids` One2many → `purchase.requisition.line` “Products to Purchase”
- `product_id` Many2one → `product.product` “Product” (related=line_ids.product_id)
- `state` Selection (required)
- `state_blanket_order` Selection (compute=_set_state)
- `is_quantity_copy` Selection (readonly, related=type_id.quantity_copy)
- `currency_id` Many2one → `res.currency` (required)

Public methods: `action_cancel`, `action_done`, `action_draft`, `action_in_progress`, `action_open`, `unlink`

Extension points: `_get_type_id`

## `purchase.requisition.line` (defines)

Purchase Requisition Line

Inherits: `analytic.mixin`

- `product_id` Many2one → `product.product` “Product” (required)
- `product_uom_id` Many2one → `uom.uom` “Product Unit of Measure”
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `product_qty` Float “Quantity”
- `product_description_variants` Char “Custom Description”
- `price_unit` Float “Unit Price”
- `qty_ordered` Float “Ordered Quantities” (compute=_compute_ordered_qty)
- `requisition_id` Many2one → `purchase.requisition` “Purchase Agreement” (required)
- `company_id` Many2one → `res.company` “Company” (readonly, store, related=requisition_id.company_id)
- `schedule_date` Date “Scheduled Date”
- `supplier_info_ids` One2many → `product.supplierinfo`

Public methods: `create`, `create_supplier_info`, `unlink`, `write`

Extension points: `_prepare_purchase_order_line`

## `purchase.requisition.alternative.warning` (defines)

Wizard in case PO still has open alternative requests for quotation

- `po_ids` Many2many → `purchase.order` “POs to Confirm”
- `alternative_po_ids` Many2many → `purchase.order` “Alternative POs”
- `alternative_po_count` Integer (compute=_compute_alternative_po_count)

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

Extension points: `_get_alternative_values`
