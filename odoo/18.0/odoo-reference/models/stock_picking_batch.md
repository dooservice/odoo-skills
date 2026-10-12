# stock_picking_batch — Warehouse Management: Batch Transfer

Depends on: stock.

## `stock.move` (extends)


Public methods: `write`

Extension points: `_action_assign`, `_action_cancel`, `_get_batch_moves`

## `stock.move.line` (extends)

- `batch_id` Many2one (store, related=picking_id.batch_id)

Public methods: `action_open_add_to_wave`

Extension points: `_get_auto_wave_description`, `_get_potential_existing_waves_extra_domain`, `_get_potential_new_waves_extra_domain`

## `stock.picking.type` (extends)

- `count_picking_batch` Integer (compute=_compute_picking_count)
- `count_picking_wave` Integer (compute=_compute_picking_count)
- `auto_batch` Boolean “Automatic Batches”
- `batch_group_by_partner` Boolean “Contact”
- `batch_group_by_destination` Boolean “Destination Country”
- `batch_group_by_src_loc` Boolean “Group by Source Location”
- `batch_group_by_dest_loc` Boolean “Group by Destination Location”
- `wave_group_by_product` Boolean “Product”
- `wave_group_by_category` Boolean “Product Category”
- `wave_category_ids` Many2many → `product.category` “Wave Product Categories”
- `wave_group_by_location` Boolean “Location”
- `wave_location_ids` Many2many → `stock.location` “Wave Locations”
- `batch_max_lines` Integer “Maximum lines”
- `batch_max_pickings` Integer “Maximum transfers”
- `batch_auto_confirm` Boolean “Auto-confirm”
- `batch_properties_definition` PropertiesDefinition “Batch Properties”

Public methods: `action_batch`

Extension points: `_get_batch_and_wave_group_by_keys`, `_get_batch_group_by_keys`, `_get_wave_group_by_keys`

## `stock.picking` (extends)

- `batch_id` Many2one → `stock.picking.batch` “Batch Transfer” (index)
- `batch_sequence` Integer “Sequence”

Public methods: `action_add_operations`, `action_cancel`, `action_confirm`, `action_view_batch`, `assign_batch_user`, `button_validate`, `create`, `write`

Extension points: `_create_backorder`, `_get_auto_batch_description`, `_get_possible_batches_domain`, `_get_possible_pickings_domain`

## `stock.picking.batch` (defines)

Batch Transfer

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Batch Transfer” (required, readonly)
- `description` Char “Description”
- `user_id` Many2one → `res.users` “Responsible”
- `company_id` Many2one → `res.company` “Company” (required, readonly, index)
- `picking_ids` One2many → `stock.picking` “Transfers”
- `show_check_availability` Boolean “Show Check Availability” (compute=_compute_move_ids)
- `show_allocation` Boolean “Show Allocation Button” (compute=_compute_show_allocation)
- `allowed_picking_ids` One2many → `stock.picking` (compute=_compute_allowed_picking_ids)
- `move_ids` One2many → `stock.move` “Stock moves” (compute=_compute_move_ids)
- `move_line_ids` One2many → `stock.move.line` “Stock move lines” (compute=_compute_move_line_ids)
- `state` Selection (required, readonly, store, index, compute=_compute_state)
- `picking_type_id` Many2one → `stock.picking.type` (index)
- `warehouse_id` Many2one → `stock.warehouse` (related=picking_type_id.warehouse_id)
- `picking_type_code` Selection (related=picking_type_id.code)
- `scheduled_date` Datetime “Scheduled Date” (store, compute=_compute_scheduled_date)
- `is_wave` Boolean “This batch is a wave”
- `show_lots_text` Boolean (compute=_compute_show_lots_text)
- `estimated_shipping_weight` Float “shipping_weight” (compute=_compute_estimated_shipping_capacity)
- `estimated_shipping_volume` Float “shipping_volume” (compute=_compute_estimated_shipping_capacity)
- `properties` Properties “Properties”

Public methods: `action_assign`, `action_cancel`, `action_confirm`, `action_done`, `action_open_label_layout`, `action_print`, `action_put_in_pack`, `action_view_reception_report`, `create`, `onchange_scheduled_date`, `write`

## `stock.warehouse` (extends)


Extension points: `_get_picking_type_create_values`

## `stock.add.to.wave` (defines)

Wave Transfer Lines

- `wave_id` Many2one → `stock.picking.batch` “Wave Transfer”
- `picking_ids` Many2many → `stock.picking`
- `line_ids` Many2many → `stock.move.line`
- `mode` Selection
- `user_id` Many2one → `res.users` “Responsible”

Public methods: `attach_pickings`, `default_get`

## `stock.package.destination` (extends)


Public methods: `action_done`

## `stock.picking.to.batch` (defines)

Batch Transfer Lines

- `batch_id` Many2one → `stock.picking.batch` “Batch Transfer”
- `mode` Selection
- `user_id` Many2one → `res.users` “Responsible”
- `is_create_draft` Boolean “Draft”
- `description` Char “Description”

Public methods: `attach_pickings`
