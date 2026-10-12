# stock_picking_batch — Warehouse Management: Batch Transfer

Depends on: stock.

## `stock.move` (extends)


Extension points: `_action_cancel`

## `stock.move.line` (extends)

- `batch_id` Many2one (store, related=picking_id.batch_id)

Public methods: `action_open_add_to_wave`

## `stock.picking.type` (extends)

- `count_picking_batch` Integer (compute=_compute_picking_count)
- `count_picking_wave` Integer (compute=_compute_picking_count)
- `auto_batch` Boolean “Automatic Batches”
- `batch_group_by_partner` Boolean “Contact”
- `batch_group_by_destination` Boolean “Destination Country”
- `batch_group_by_src_loc` Boolean “Source Location”
- `batch_group_by_dest_loc` Boolean “Destination Location”
- `batch_max_lines` Integer “Maximum lines per batch”
- `batch_max_pickings` Integer “Maximum transfers per batch”
- `batch_auto_confirm` Boolean “Auto-confirm”

Public methods: `get_action_picking_tree_batch`, `get_action_picking_tree_wave`

Extension points: `_get_batch_group_by_keys`

## `stock.picking` (extends)

- `batch_id` Many2one → `stock.picking.batch` “Batch Transfer” (index)

Public methods: `action_add_operations`, `action_cancel`, `action_confirm`, `action_view_batch`, `assign_batch_user`, `button_validate`, `create`, `write`

Extension points: `_get_possible_batches_domain`, `_get_possible_pickings_domain`

## `stock.picking.batch` (defines)

Batch Transfer

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Batch Transfer” (required, readonly)
- `user_id` Many2one → `res.users` “Responsible” (readonly)
- `company_id` Many2one → `res.company` “Company” (required, readonly, index)
- `picking_ids` One2many → `stock.picking` “Transfers” (readonly)
- `show_check_availability` Boolean “Show Check Availability” (compute=_compute_move_ids)
- `show_validate` Boolean “Show Validate Button” (compute=_compute_show_validate)
- `show_allocation` Boolean “Show Allocation Button” (compute=_compute_show_allocation)
- `allowed_picking_ids` One2many → `stock.picking` (compute=_compute_allowed_picking_ids)
- `move_ids` One2many → `stock.move` “Stock moves” (compute=_compute_move_ids)
- `move_line_ids` One2many → `stock.move.line` “Stock move lines” (readonly, compute=_compute_move_ids)
- `state` Selection (required, readonly, store, index, compute=_compute_state)
- `picking_type_id` Many2one → `stock.picking.type` (readonly, index)
- `picking_type_code` Selection (related=picking_type_id.code)
- `scheduled_date` Datetime “Scheduled Date” (store, compute=_compute_scheduled_date)
- `is_wave` Boolean “This batch is a wave”
- `show_set_qty_button` Boolean (compute=_compute_show_qty_button)
- `show_clear_qty_button` Boolean (compute=_compute_show_qty_button)
- `show_lots_text` Boolean (compute=_compute_show_lots_text)

Public methods: `action_assign`, `action_cancel`, `action_clear_quantities_to_zero`, `action_confirm`, `action_done`, `action_open_label_layout`, `action_print`, `action_put_in_pack`, `action_set_quantities_to_reservation`, `action_view_reception_report`, `create`, `onchange`, `onchange_scheduled_date`, `write`

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

Public methods: `attach_pickings`
