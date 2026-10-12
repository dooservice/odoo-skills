# repair — Repairs

Depends on: sale_stock, sale_management.

## `account.move` (extends)

- `repair_order_id` Many2one → `repair.order` “Repair Order”

Public methods: `action_show_repair`

## `account.move.line` (extends)

- `repair_order_id` Many2one (related=move_id.repair_order_id)
- `repair_service_line_id` Many2one → `repair.service.line`

## `product.product` (extends)


## `product.template` (extends)

- `service_tracking` Selection

Extension points: `_get_saleable_tracking_types`

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
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `uom_id` Many2one → `uom.uom` (store, compute=_compute_uom_id)
- `lot_id` Many2one → `stock.lot` (store, compute=_compute_lot_id)
- `tracking` Selection “Product Tracking” (related=product_id.tracking)
- `picking_type_id` Many2one → `stock.picking.type` (required, store, index, compute=_compute_picking_type_id)
- `reference_ids` Many2many → `stock.reference` “References”
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
- `repair_service_line_ids` One2many → `repair.service.line`
- `sale_order_id` Many2one → `sale.order` (readonly)
- `sale_order_line_id` Many2one → `sale.order.line` (readonly)
- `repair_request` Text “Repair Request” (related=sale_order_line_id.name)
- `picking_id` Many2one → `stock.picking`
- `picking_product_ids` One2many → `product.product` (compute=_compute_picking_product_ids)
- `picking_product_id` Many2one (related=picking_id.product_id)
- `allowed_lot_ids` One2many → `stock.lot` (compute=_compute_allowed_lot_ids)
- `invoice_count` Integer “Invoice Count” (compute=_compute_invoice_count)
- `invoice_ids` One2many → `account.move` “Invoice” (store, compute=_compute_invoice_ids)
- `can_create_extra_invoice` Boolean (compute=_compute_can_create_sale_or_invoice)
- `has_uncomplete_moves` Boolean (compute=_compute_has_uncomplete_moves)
- `unreserve_visible` Boolean “Allowed to Unreserve Production” (compute=_compute_unreserve_visible)
- `reserve_visible` Boolean “Allowed to Reserve Production” (compute=_compute_unreserve_visible)
- `picking_type_visible` Boolean (compute=_compute_picking_type_visible)
- `can_create_sale_or_invoice` Boolean (compute=_compute_can_create_sale_or_invoice)
- `validate_button_style` Selection (compute=_compute_validate_button_style)

Public methods: `action_add_from_catalog`, `action_assign`, `action_create_invoice`, `action_create_sale_order`, `action_generate_serial`, `action_repair_cancel`, `action_repair_cancel_draft`, `action_repair_done`, `action_repair_end`, `action_unreserve`, `action_validate`, `action_view_invoice`, `action_view_sale_order`, `create`, `default_get`, `message_post`, `onchange_uom_id`, `print_repair_order`, `write`

Extension points: `_action_repair_confirm`, `_create_sale_order`, `_get_action_add_from_catalog_extra_context`, `_get_location`, `_get_picking_type`, `_get_product_catalog_domain`, `_get_sale_order_values`

## `repair.tags` (defines)

Repair Tag

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”

Extension points: `_get_default_color`

## `repair.service.line` (defines)

Repair Service Line

Inherits: `product.catalog.line.mixin`

- `repair_id` Many2one → `repair.order`
- `product_id` Many2one → `product.product` “Service”
- `uom_id` Many2one → `uom.uom` (required, store, compute=_compute_uom_id)
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `quantity` Float “Quantity” (required)
- `company_id` Many2one (related=repair_id.company_id)
- `sale_line_id` One2many → `sale.order.line`
- `invoice_line_ids` One2many → `account.move.line` “Invoice Line”
- `sequence` Integer “Sequence”
- `description` Text “Description”

Public methods: `action_add_service_from_repair_catalog`, `create`, `write`

Extension points: `_create_repair_invoice_line`, `_create_repair_linked_line`, `_create_repair_sale_order_line`, `_get_product_uom_field`, `_get_quantity_field`, `_prepare_repair_service_line_common_vals`

## `res.partner` (extends)

- `repair_order_count` Integer “Repair Order Count” (compute=_compute_repair_order_count)

## `sale.order` (extends)

- `repair_order_ids` One2many → `repair.order` “Repair Order”
- `repair_count` Integer “Repair Order(s)” (compute=_compute_repair_count)

Public methods: `action_show_repair`

Extension points: `_action_cancel`, `_action_confirm`

## `sale.order.line` (extends)

- `repair_service_line_id` Many2one → `repair.service.line`

Public methods: `create`, `has_valued_move_ids`, `write`

Extension points: `_action_launch_stock_rule`, `_create_repair_order`, `_prepare_qty_delivered`

## `stock.lot` (extends)

- `repair_line_ids` Many2many → `repair.order` “Repair Orders” (compute=_compute_repair_line_ids)
- `repair_part_count` Integer “Repair part count” (compute=_compute_repair_line_ids)
- `in_repair_count` Integer “In repair count” (compute=_compute_in_repair_count)
- `repaired_count` Integer “Repaired count” (compute=_compute_repaired_count)

Public methods: `action_lot_open_repairs`, `action_view_ro`

Extension points: `_check_create`

## `stock.move` (extends)

- `repair_id` Many2one → `repair.order`
- `repair_line_type` Selection (store, index)

Public methods: `action_add_from_catalog_repair`, `action_show_details`, `copy_data`, `create`, `unlink`, `write`

Extension points: `_action_cancel`, `_create_repair_invoice_line`, `_create_repair_linked_line`, `_create_repair_sale_order_line`, `_get_repair_locations`, `_get_source_document`

## `stock.move.line` (extends)


## `stock.picking.type` (extends)

- `code` Selection
- `count_repair_confirmed` Integer “Number of Repair Orders Confirmed” (compute=_compute_count_repair)
- `count_repair_ready` Integer “Number of Repair Orders to Process” (compute=_compute_count_repair)
- `count_repair_late` Integer “Number of Late Repair Orders” (compute=_compute_count_repair)
- `default_product_location_src_id` Many2one → `stock.location` (store, compute=_compute_default_product_location_id)
- `default_product_location_dest_id` Many2one → `stock.location` (store, compute=_compute_default_product_location_id)
- `default_remove_location_dest_id` Many2one → `stock.location` (store, compute=_compute_default_remove_location_dest_id)
- `default_recycle_location_dest_id` Many2one → `stock.location` (store, compute=_compute_default_recycle_location_dest_id)
- `repair_properties_definition` PropertiesDefinition “Repair Properties”

Public methods: `get_repair_stock_picking_action_picking_type`

Extension points: `_get_aggregated_records_by_date`

## `stock.picking` (extends)

- `repair_ids` One2many → `repair.order`
- `nbr_repairs` Integer “Number of repairs linked to this picking” (compute=_compute_nbr_repairs)

Public methods: `action_repair_return`, `action_view_repairs`, `get_action_click_graph`

## `stock.warehouse` (extends)

- `repair_type_id` Many2one → `stock.picking.type`
- `repair_mto_pull_id` Many2one → `stock.rule`

Extension points: `_create_missing_locations`, `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_production_location`, `_get_sequence_values`

## `stock.forecasted_product_product` (extends)


Extension points: `_get_reservation_data`

## `stock.traceability.report` (extends)


Extension points: `_get_linked_move_lines`, `_get_reference`

## `repair.consumption.warning` (defines)

Wizard for warning about mismatching expected vs actual component consumption quantities for ROs

- `repair_id` Many2one → `repair.order`
- `repair_consumption_warning_line_ids` One2many → `repair.consumption.warning.line`

Public methods: `action_cancel`, `action_confirm`, `action_set_qty`

## `repair.consumption.warning.line` (defines)

Line of issue consumption

- `repair_consumption_warning_id` Many2one → `repair.consumption.warning` (required, readonly)
- `product_id` Many2one → `product.product` (required, readonly)
- `uom_id` Many2one → `uom.uom` (readonly)
- `product_consumed_qty_uom` Float “Consumed” (readonly)
- `product_expected_qty_uom` Float “To Consume” (readonly)
- `move_id` Many2one → `stock.move` (readonly)
