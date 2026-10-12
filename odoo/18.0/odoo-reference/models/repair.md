# repair — Repairs

Depends on: sale_stock, sale_management.

## `mail.compose.message` (extends)


Extension points: `_action_send_mail`

## `product.product` (extends)

- `product_catalog_product_is_in_repair` Boolean (compute=_compute_product_is_in_repair)

## `product.template` (extends)

- `create_repair` Boolean “Create Repair”

Public methods: `copy_data`

## `repair.order` (defines)

Repair Order

Inherits: `mail.thread`, `mail.activity.mixin`, `product.catalog.mixin`

- `name` Char “Repair Reference” (required, readonly)
- `company_id` Many2one → `res.company` (required, readonly, index)
- `state` Selection “Status” (readonly, index)
- `priority` Selection “Priority”
- `partner_id` Many2one → `res.partner` (store, index, compute=_compute_partner_id)
- `user_id` Many2one → `res.users` “Responsible”
- `internal_notes` Html “Internal Notes”
- `tag_ids` Many2many → `repair.tags` “Tags”
- `under_warranty` Boolean “Under Warranty”
- `schedule_date` Datetime “Scheduled Date” (required, index)
- `search_date_category` Selection “Date Category” (readonly)
- `repair_properties` Properties “Properties”
- `move_id` Many2one → `stock.move` (readonly)
- `product_id` Many2one → `product.product` “Product to Repair”
- `product_qty` Float “Product Quantity” (store, compute=_compute_product_qty)
- `product_uom` Many2one → `uom.uom` (store, compute=compute_product_uom)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `lot_id` Many2one → `stock.lot` (store, compute=compute_lot_id)
- `tracking` Selection “Product Tracking” (related=product_id.tracking)
- `picking_type_id` Many2one → `stock.picking.type` (required, store, index, compute=_compute_picking_type_id)
- `procurement_group_id` Many2one → `procurement.group`
- `location_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_id)
- `product_location_src_id` Many2one → `stock.location` (required, store, index, compute=_compute_product_location_src_id)
- `product_location_dest_id` Many2one → `stock.location` (required, store, index, compute=_compute_product_location_dest_id)
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
- `picking_product_ids` One2many → `product.product` (compute=_compute_picking_product_ids)
- `picking_product_id` Many2one (related=picking_id.product_id)
- `allowed_lot_ids` One2many → `stock.lot` (compute=_compute_allowed_lot_ids)
- `has_uncomplete_moves` Boolean (compute=_compute_has_uncomplete_moves)
- `unreserve_visible` Boolean “Allowed to Unreserve Production” (compute=_compute_unreserve_visible)
- `reserve_visible` Boolean “Allowed to Reserve Production” (compute=_compute_unreserve_visible)

Public methods: `action_add_from_catalog`, `action_assign`, `action_create_sale_order`, `action_repair_cancel`, `action_repair_cancel_draft`, `action_repair_done`, `action_repair_end`, `action_repair_start`, `action_unreserve`, `action_validate`, `action_view_sale_order`, `compute_lot_id`, `compute_product_uom`, `create`, `default_get`, `onchange_product_uom`, `print_repair_order`, `write`

Extension points: `_action_repair_confirm`, `_get_location`, `_get_picking_type`, `_get_product_catalog_domain`, `_get_product_catalog_order_data`, `_get_product_catalog_record_lines`, `_get_product_price_and_data`

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

Public methods: `action_add_from_catalog_repair`, `action_show_details`, `copy_data`, `create`, `unlink`, `write`

Extension points: `_action_cancel`, `_create_repair_sale_order_line`, `_get_repair_locations`, `_get_source_document`, `_prepare_repair_so_line_vals`

## `stock.move.line` (extends)


## `stock.picking.type` (extends)

- `code` Selection
- `count_repair_confirmed` Integer “Number of Repair Orders Confirmed” (compute=_compute_count_repair)
- `count_repair_under_repair` Integer “Number of Repair Orders Under Repair” (compute=_compute_count_repair)
- `count_repair_ready` Integer “Number of Repair Orders to Process” (compute=_compute_count_repair)
- `count_repair_late` Integer “Number of Late Repair Orders” (compute=_compute_count_repair)
- `default_product_location_src_id` Many2one → `stock.location` (store, compute=_compute_default_product_location_id)
- `default_product_location_dest_id` Many2one → `stock.location` (store, compute=_compute_default_product_location_id)
- `default_remove_location_dest_id` Many2one → `stock.location` (store, compute=_compute_default_remove_location_dest_id)
- `default_recycle_location_dest_id` Many2one → `stock.location` (store, compute=_compute_default_recycle_location_dest_id)
- `is_repairable` Boolean “Create Repair Orders from Returns” (store, compute=_compute_is_repairable)
- `return_type_of_ids` One2many → `stock.picking.type`
- `repair_properties_definition` PropertiesDefinition “Repair Properties”

Public methods: `action_repair_overview`, `get_repair_stock_picking_action_picking_type`

Extension points: `_get_aggregated_records_by_date`

## `stock.picking` (extends)

- `is_repairable` Boolean (compute=_compute_is_repairable)
- `repair_ids` One2many → `repair.order`
- `nbr_repairs` Integer “Number of repairs linked to this picking” (compute=_compute_nbr_repairs)

Public methods: `action_repair_return`, `action_view_repairs`, `get_action_click_graph`

## `stock.traceability.report` (extends)


Extension points: `_get_linked_move_lines`, `_get_reference`

## `stock.warehouse` (extends)

- `repair_type_id` Many2one → `stock.picking.type`
- `repair_mto_pull_id` Many2one → `stock.rule`

Extension points: `_create_missing_locations`, `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_production_location`, `_get_sequence_values`

## `stock.forecasted_product_product` (extends)


Extension points: `_get_reservation_data`

## `stock.warn.insufficient.qty.repair` (defines)

Warn Insufficient Repair Quantity

Inherits: `stock.warn.insufficient.qty`

- `repair_id` Many2one → `repair.order` “Repair”

Public methods: `action_done`

Extension points: `_get_reference_document_company_id`
