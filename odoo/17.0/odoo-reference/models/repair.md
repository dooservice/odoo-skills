# repair — Repairs

Depends on: sale_stock, sale_management.

## `mail.compose.message` (extends)


Extension points: `_action_send_mail`

## `product.product` (extends)


## `product.template` (extends)

- `create_repair` Boolean “Create Repair”

Public methods: `copy_data`

## `repair.order` (defines)

Repair Order

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Repair Reference” (required, readonly)
- `company_id` Many2one → `res.company` (required, readonly, index)
- `state` Selection “Status” (readonly, index)
- `priority` Selection “Priority”
- `partner_id` Many2one → `res.partner` (index)
- `user_id` Many2one → `res.users` “Responsible”
- `internal_notes` Html “Internal Notes”
- `tag_ids` Many2many → `repair.tags` “Tags”
- `under_warranty` Boolean “Under Warranty”
- `schedule_date` Datetime “Scheduled Date” (required, index)
- `move_id` Many2one → `stock.move` (readonly)
- `product_id` Many2one → `product.product` “Product to Repair”
- `product_qty` Float “Product Quantity”
- `product_uom` Many2one → `uom.uom` (store, compute=compute_product_uom)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `lot_id` Many2one → `stock.lot` (store, compute=compute_lot_id)
- `tracking` Selection “Product Tracking” (related=product_id.tracking)
- `picking_type_id` Many2one → `stock.picking.type` (required, store, index, compute=_compute_picking_type_id)
- `procurement_group_id` Many2one → `procurement.group`
- `location_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (required, readonly, store, index, related=picking_type_id.default_location_dest_id)
- `parts_location_id` Many2one → `stock.location` (required, readonly, store, index, related=picking_type_id.default_remove_location_dest_id)
- `recycle_location_id` Many2one → `stock.location` (required, store, index, compute=_compute_recycle_location_id)
- `move_ids` One2many → `stock.move`
- `parts_availability` Char “Component Status” (compute=_compute_parts_availability)
- `parts_availability_state` Selection (compute=_compute_parts_availability)
- `is_parts_available` Boolean “All Parts are available” (store, compute=_compute_availability_boolean)
- `is_parts_late` Boolean “Any Part is late” (store, compute=_compute_availability_boolean)
- `sale_order_id` Many2one → `sale.order` (readonly)
- `sale_order_line_id` Many2one → `sale.order.line` (readonly)
- `repair_request` Text “Repair Request” (related=sale_order_line_id.name)
- `picking_id` Many2one → `stock.picking`
- `is_returned` Boolean “Returned” (compute=_compute_is_returned)
- `picking_product_ids` One2many → `product.product` (compute=compute_picking_product_ids)
- `picking_product_id` Many2one (related=picking_id.product_id)
- `show_set_qty_button` Boolean (compute=_compute_show_qty_button)
- `show_clear_qty_button` Boolean (compute=_compute_show_qty_button)
- `unreserve_visible` Boolean “Allowed to Unreserve Production” (compute=_compute_unreserve_visible)
- `reserve_visible` Boolean “Allowed to Reserve Production” (compute=_compute_unreserve_visible)

Public methods: `action_assign`, `action_create_sale_order`, `action_repair_cancel`, `action_repair_cancel_draft`, `action_repair_done`, `action_repair_end`, `action_repair_start`, `action_unreserve`, `action_validate`, `action_view_sale_order`, `compute_lot_id`, `compute_picking_product_ids`, `compute_product_uom`, `create`, `default_get`, `onchange_product_uom`, `print_repair_order`, `write`

Extension points: `_action_repair_confirm`, `_get_location`, `_get_picking_type`

## `repair.tags` (defines)

Repair Tags

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”

Extension points: `_get_default_color`

## `sale.order` (extends)

- `repair_order_ids` One2many → `repair.order` “Repair Order”
- `repair_count` Integer “Repair Order(s)” (compute=_compute_repair_count)

Public methods: `action_show_repair`

Extension points: `_action_cancel`, `_action_confirm`

## `sale.order.line` (extends)


Public methods: `create`, `has_valued_move_ids`, `write`

Extension points: `_action_launch_stock_rule`, `_create_repair_order`

## `stock.lot` (extends)

- `repair_line_ids` Many2many → `repair.order` “Repair Orders” (compute=_compute_repair_line_ids)
- `repair_part_count` Integer “Repair part count” (compute=_compute_repair_line_ids)
- `in_repair_count` Integer “In repair count” (compute=_compute_in_repair_count)
- `repaired_count` Integer “Repaired count” (compute=_compute_repaired_count)

Public methods: `action_lot_open_repairs`, `action_view_ro`

## `stock.move` (extends)

- `repair_id` Many2one → `repair.order`
- `repair_line_type` Selection (store, index)

Public methods: `action_show_details`, `copy_data`, `create`, `unlink`, `write`

Extension points: `_action_cancel`, `_create_extra_move`, `_create_repair_sale_order_line`, `_get_repair_locations`, `_get_source_document`, `_prepare_repair_so_line_vals`

## `stock.move.line` (extends)


## `stock.picking.type` (extends)

- `code` Selection
- `count_repair_confirmed` Integer “Number of Repair Orders Confirmed” (compute=_compute_count_repair)
- `count_repair_under_repair` Integer “Number of Repair Orders Under Repair” (compute=_compute_count_repair)
- `count_repair_ready` Integer “Number of Repair Orders to Process” (compute=_compute_count_repair)
- `default_remove_location_dest_id` Many2one → `stock.location` (store, compute=_compute_default_remove_location_dest_id)
- `default_recycle_location_dest_id` Many2one → `stock.location` (store, compute=_compute_default_recycle_location_dest_id)
- `is_repairable` Boolean “Create Repair Orders from Returns” (store, compute=_compute_is_repairable)
- `return_type_of_ids` One2many → `stock.picking.type`

Public methods: `get_repair_stock_picking_action_picking_type`

## `stock.picking` (extends)

- `is_repairable` Boolean (compute=_compute_is_repairable)
- `repair_ids` One2many → `repair.order`
- `nbr_repairs` Integer “Number of repairs linked to this picking” (compute=_compute_nbr_repairs)

Public methods: `action_repair_return`, `action_view_repairs`

## `stock.traceability.report` (extends)


Extension points: `_get_linked_move_lines`, `_get_reference`

## `stock.warehouse` (extends)

- `repair_type_id` Many2one → `stock.picking.type`

Extension points: `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_sequence_values`

## `stock.forecasted_product_product` (extends)


Extension points: `_get_reservation_data`

## `repair.warn.uncomplete.move` (defines)

Warn Uncomplete Move(s)

- `repair_ids` Many2many → `repair.order` “Repair Orders”

Public methods: `action_validate`

## `stock.warn.insufficient.qty.repair` (defines)

Warn Insufficient Repair Quantity

Inherits: `stock.warn.insufficient.qty`

- `repair_id` Many2one → `repair.order` “Repair”

Public methods: `action_done`

Extension points: `_get_reference_document_company_id`
