# repair — Repairs

Depends on: stock, sale_management, account.

## `account.move` (extends)

- `repair_ids` One2many → `repair.order` (readonly)

Public methods: `unlink`

## `account.move.line` (extends)

- `repair_line_ids` One2many → `repair.line` (readonly)
- `repair_fee_ids` One2many → `repair.fee` (readonly)

## `mail.compose.message` (extends)


Extension points: `_action_send_mail`

## `product.product` (extends)


## `stock.move` (extends)

- `repair_id` Many2one → `repair.order`

## `repair.order` (defines)

Repair Order

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Repair Reference” (required, readonly)
- `description` Char “Repair Description”
- `product_id` Many2one → `product.product` “Product to Repair” (required, readonly)
- `product_qty` Float “Product Quantity” (required, readonly)
- `product_uom` Many2one → `uom.uom` (required, readonly, store, compute=_compute_product_uom)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `partner_id` Many2one → `res.partner` (index)
- `address_id` Many2one → `res.partner`
- `default_address_id` Many2one → `res.partner` (compute=_compute_default_address_id)
- `state` Selection “Status” (readonly)
- `schedule_date` Date “Scheduled Date”
- `location_id` Many2one → `stock.location` (required, readonly, store, index, compute=_compute_location_id)
- `lot_id` Many2one → `stock.lot`
- `guarantee_limit` Date “Warranty Expiration”
- `operations` One2many → `repair.line`
- `pricelist_id` Many2one → `product.pricelist`
- `currency_id` Many2one (related=pricelist_id.currency_id)
- `partner_invoice_id` Many2one → `res.partner`
- `invoice_method` Selection “Invoice Method” (required, readonly, index)
- `invoice_id` Many2one → `account.move` (readonly)
- `move_id` Many2one → `stock.move` (readonly)
- `fees_lines` One2many → `repair.fee`
- `internal_notes` Html “Internal Notes”
- `quotation_notes` Html “Quotation Notes”
- `user_id` Many2one → `res.users` “Responsible”
- `company_id` Many2one → `res.company` (required, readonly, index)
- `sale_order_id` Many2one → `sale.order`
- `picking_id` Many2one → `stock.picking`
- `allowed_picking_type_ids` Many2many → `stock.picking.type` (compute=_compute_allowed_picking_type_ids)
- `is_returned` Boolean “Returned” (compute=_compute_is_returned)
- `tag_ids` Many2many → `repair.tags` “Tags”
- `invoiced` Boolean “Invoiced” (readonly)
- `repaired` Boolean “Repaired” (readonly)
- `amount_untaxed` Float “Untaxed Amount” (store, compute=_amount_untaxed)
- `amount_tax` Float “Taxes” (store, compute=_amount_tax)
- `amount_total` Float “Total” (store, compute=_amount_total)
- `tracking` Selection “Product Tracking” (related=product_id.tracking)
- `invoice_state` Selection “Invoice State” (related=invoice_id.state)
- `priority` Selection “Priority”

Public methods: `action_created_invoice`, `action_repair_cancel`, `action_repair_cancel_draft`, `action_repair_confirm`, `action_repair_done`, `action_repair_end`, `action_repair_invoice_create`, `action_repair_ready`, `action_repair_start`, `action_send_mail`, `action_validate`, `button_dummy`, `create`, `onchange_partner_id`, `onchange_product_id`, `onchange_product_uom`, `print_repair_order`

Extension points: `_check_product_tracking`, `_create_invoices`

## `repair.line` (defines)

Repair Line (parts)

- `name` Text “Description” (required)
- `repair_id` Many2one → `repair.order` (required, index)
- `company_id` Many2one (store, index, related=repair_id.company_id)
- `currency_id` Many2one (related=repair_id.currency_id)
- `type` Selection (required)
- `product_id` Many2one → `product.product` (required)
- `invoiced` Boolean “Invoiced” (readonly)
- `price_unit` Float “Unit Price” (required)
- `price_subtotal` Float “Subtotal” (store, compute=_compute_price_total_and_subtotal)
- `price_total` Float “Total” (store, compute=_compute_price_total_and_subtotal)
- `tax_id` Many2many → `account.tax`
- `product_uom_qty` Float “Quantity” (required)
- `product_uom` Many2one → `uom.uom` (required, store, compute=_compute_product_uom)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `invoice_line_id` Many2one → `account.move.line` (readonly)
- `location_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_id)
- `move_id` Many2one → `stock.move` (readonly)
- `lot_id` Many2one → `stock.lot`
- `state` Selection (required, readonly)
- `tracking` Selection “Product Tracking” (related=product_id.tracking)

Public methods: `onchange_operation_type`, `onchange_product_id`

## `repair.fee` (defines)

Repair Fees

- `repair_id` Many2one → `repair.order` (required, index)
- `company_id` Many2one (store, index, related=repair_id.company_id)
- `currency_id` Many2one (related=repair_id.currency_id)
- `name` Text “Description” (required, index)
- `product_id` Many2one → `product.product`
- `product_uom_qty` Float “Quantity” (required)
- `price_unit` Float “Unit Price” (required)
- `product_uom` Many2one → `uom.uom` (required)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `price_subtotal` Float “Subtotal” (store, compute=_compute_price_total_and_subtotal)
- `price_total` Float “Total” (store, compute=_compute_price_total_and_subtotal)
- `tax_id` Many2many → `account.tax`
- `invoice_line_id` Many2one → `account.move.line` (readonly)
- `invoiced` Boolean “Invoiced” (readonly)

Public methods: `create`, `onchange_product_id`, `write`

## `repair.tags` (defines)

Repair Tags

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”

Extension points: `_get_default_color`

## `stock.lot` (extends)

- `repair_order_ids` Many2many → `repair.order` “Repair Orders” (compute=_compute_repair_order_ids)
- `repair_order_count` Integer “Repair order count” (compute=_compute_repair_order_ids)

Public methods: `action_view_ro`

## `stock.picking.type` (extends)

- `is_repairable` Boolean “Create Repair Orders from Returns” (store, compute=_compute_is_repairable)
- `return_type_of_ids` One2many → `stock.picking.type`

## `stock.picking` (extends)

- `is_repairable` Boolean (related=picking_type_id.is_repairable)
- `repair_ids` One2many → `repair.order`
- `nbr_repairs` Integer “Number of repairs linked to this picking” (compute=_compute_nbr_repairs)

Public methods: `action_repair_return`, `action_view_repairs`

## `stock.traceability.report` (extends)


Extension points: `_get_linked_move_lines`, `_get_reference`

## `repair.order.make_invoice` (defines)

Create Mass Invoice (repair)

- `group` Boolean “Group by partner invoice address”

Public methods: `make_invoices`

## `stock.warn.insufficient.qty.repair` (defines)

Warn Insufficient Repair Quantity

Inherits: `stock.warn.insufficient.qty`

- `repair_id` Many2one → `repair.order` “Repair”

Public methods: `action_done`

Extension points: `_get_reference_document_company_id`
