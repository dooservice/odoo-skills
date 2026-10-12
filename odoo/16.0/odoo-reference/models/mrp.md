# mrp — Manufacturing

Depends on: product, stock, resource.

## `mrp.bom` (defines)

Bill of Material

Inherits: `mail.thread`

- `code` Char “Reference”
- `active` Boolean “Active”
- `type` Selection (required)
- `product_tmpl_id` Many2one → `product.template` (required, index)
- `product_id` Many2one → `product.product` (index)
- `bom_line_ids` One2many → `mrp.bom.line`
- `byproduct_ids` One2many → `mrp.bom.byproduct`
- `product_qty` Float “Quantity” (required)
- `product_uom_id` Many2one → `uom.uom` (required)
- `product_uom_category_id` Many2one (related=product_tmpl_id.uom_id.category_id)
- `sequence` Integer “Sequence”
- `operation_ids` One2many → `mrp.routing.workcenter`
- `ready_to_produce` Selection “Manufacturing Readiness” (required)
- `picking_type_id` Many2one → `stock.picking.type`
- `company_id` Many2one → `res.company` (index)
- `consumption` Selection “Flexible Consumption” (required)
- `possible_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` (compute=_compute_possible_product_template_attribute_value_ids)
- `allow_operation_dependencies` Boolean “Operation Dependencies”

Public methods: `check_kit_has_not_orderpoint`, `copy`, `explode`, `get_import_templates`, `name_create`, `name_get`, `onchange_bom_structure`, `onchange_product_tmpl_id`, `onchange_product_uom_id`, `toggle_active`, `write`

Extension points: `_check_bom_cycle`, `_check_bom_lines`, `_get_default_product_uom_id`

## `mrp.bom.line` (defines)

Bill of Material Line

- `product_id` Many2one → `product.product` (required)
- `product_tmpl_id` Many2one → `product.template` (store, index, related=product_id.product_tmpl_id)
- `company_id` Many2one (readonly, store, index, related=bom_id.company_id)
- `product_qty` Float “Quantity” (required)
- `product_uom_id` Many2one → `uom.uom` (required)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `sequence` Integer “Sequence”
- `bom_id` Many2one → `mrp.bom` (required, index)
- `parent_product_tmpl_id` Many2one → `product.template` (related=bom_id.product_tmpl_id)
- `possible_bom_product_template_attribute_value_ids` Many2many (related=bom_id.possible_product_template_attribute_value_ids)
- `bom_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` “Apply on Variants”
- `allowed_operation_ids` One2many → `mrp.routing.workcenter` (related=bom_id.operation_ids)
- `operation_id` Many2one → `mrp.routing.workcenter`
- `child_bom_id` Many2one → `mrp.bom` (compute=_compute_child_bom_id)
- `child_line_ids` One2many → `mrp.bom.line` “BOM lines of the referred bom” (compute=_compute_child_line_ids)
- `attachments_count` Integer “Attachments Count” (compute=_compute_attachments_count)
- `tracking` Selection (related=product_id.tracking)
- `manual_consumption` Boolean “Manual Consumption” (store, compute=_compute_manual_consumption)
- `manual_consumption_readonly` Boolean “Manual Consumption Readonly” (compute=_compute_manual_consumption_readonly)

Public methods: `action_see_attachments`, `create`, `onchange_product_id`, `onchange_product_uom_id`

Extension points: `_get_default_product_uom_id`

## `mrp.bom.byproduct` (defines)

Byproduct

- `product_id` Many2one → `product.product` (required)
- `company_id` Many2one (readonly, store, index, related=bom_id.company_id)
- `product_qty` Float “Quantity” (required)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `product_uom_id` Many2one → `uom.uom` (required, store, compute=_compute_product_uom_id)
- `bom_id` Many2one → `mrp.bom` (index)
- `allowed_operation_ids` One2many → `mrp.routing.workcenter` (related=bom_id.operation_ids)
- `operation_id` Many2one → `mrp.routing.workcenter`
- `possible_bom_product_template_attribute_value_ids` Many2many (related=bom_id.possible_product_template_attribute_value_ids)
- `bom_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` “Apply on Variants”
- `sequence` Integer “Sequence”
- `cost_share` Float “Cost Share (%)”

## `mrp.document` (defines)

Production Document

- `ir_attachment_id` Many2one → `ir.attachment` “Related attachment” (required)
- `active` Boolean “Active”
- `priority` Selection “Priority”

Public methods: `copy`, `unlink`

## `mrp.production` (defines)

Production Order

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Reference” (readonly)
- `priority` Selection “Priority”
- `backorder_sequence` Integer “Backorder Sequence”
- `origin` Char “Source”
- `product_id` Many2one → `product.product` (required, readonly, store, compute=_compute_product_id)
- `product_variant_attributes` Many2many → `product.template.attribute.value` (related=product_id.product_template_attribute_value_ids)
- `product_tracking` Selection (related=product_id.tracking)
- `product_tmpl_id` Many2one → `product.template` (related=product_id.product_tmpl_id)
- `product_qty` Float “Quantity To Produce” (required, store, compute=_compute_product_qty)
- `product_uom_id` Many2one → `uom.uom` (required, store, compute=_compute_uom_id)
- `lot_producing_id` Many2one → `stock.lot` “Lot/Serial Number”
- `qty_producing` Float “Quantity Producing”
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `product_uom_qty` Float “Total Quantity” (store, compute=_compute_product_uom_qty)
- `picking_type_id` Many2one → `stock.picking.type` (required, store, index, compute=_compute_picking_type_id)
- `use_create_components_lots` Boolean (related=picking_type_id.use_create_components_lots)
- `use_auto_consume_components_lots` Boolean (related=picking_type_id.use_auto_consume_components_lots)
- `location_src_id` Many2one → `stock.location` (required, store, compute=_compute_locations)
- `warehouse_id` Many2one (related=location_src_id.warehouse_id)
- `location_dest_id` Many2one → `stock.location` (required, store, compute=_compute_locations)
- `date_planned_start` Datetime “Scheduled Date” (required, index)
- `date_planned_finished` Datetime “Scheduled End Date” (store, compute=_compute_date_planned_finished)
- `date_deadline` Datetime “Deadline” (readonly, store, compute=_compute_date_deadline)
- `date_start` Datetime “Start Date” (readonly)
- `date_finished` Datetime “End Date” (readonly)
- `production_duration_expected` Float “Expected Duration” (compute=_compute_production_duration_expected)
- `production_real_duration` Float “Real Duration” (compute=_compute_production_real_duration)
- `bom_id` Many2one → `mrp.bom` (store, compute=_compute_bom_id)
- `state` Selection “State” (readonly, store, index, compute=_compute_state)
- `reservation_state` Selection “MO Readiness” (readonly, store, index, compute=_compute_reservation_state)
- `move_raw_ids` One2many → `stock.move` (store, compute=_compute_move_raw_ids)
- `move_finished_ids` One2many → `stock.move` (store, compute=_compute_move_finished_ids)
- `move_byproduct_ids` One2many → `stock.move` (compute=_compute_move_byproduct_ids)
- `finished_move_line_ids` One2many → `stock.move.line` “Finished Product” (compute=_compute_lines)
- `workorder_ids` One2many → `mrp.workorder` (store, compute=_compute_workorder_ids)
- `move_dest_ids` One2many → `stock.move` “Stock Movements of Produced Goods”
- `unreserve_visible` Boolean “Allowed to Unreserve Production” (compute=_compute_unreserve_visible)
- `reserve_visible` Boolean “Allowed to Reserve Production” (compute=_compute_unreserve_visible)
- `user_id` Many2one → `res.users`
- `company_id` Many2one → `res.company` (required, index)
- `qty_produced` Float “Quantity Produced” (compute=_get_produced_qty)
- `procurement_group_id` Many2one → `procurement.group`
- `product_description_variants` Char “Custom Description”
- `orderpoint_id` Many2one → `stock.warehouse.orderpoint`
- `propagate_cancel` Boolean “Propagate cancel and split”
- `delay_alert_date` Datetime “Delay Alert Date” (compute=_compute_delay_alert_date)
- `json_popover` Char “JSON data for the popover widget” (compute=_compute_json_popover)
- `scrap_ids` One2many → `stock.scrap`
- `scrap_count` Integer “Scrap Move” (compute=_compute_scrap_move_count)
- `unbuild_ids` One2many → `mrp.unbuild`
- `unbuild_count` Integer “Number of Unbuilds” (compute=_compute_unbuild_count)
- `is_locked` Boolean “Is Locked”
- `is_planned` Boolean “Its Operations are Planned” (store, compute=_compute_is_planned)
- `show_final_lots` Boolean “Show Final Lots” (compute=_compute_show_lots)
- `production_location_id` Many2one → `stock.location` (store, compute=_compute_production_location)
- `picking_ids` Many2many → `stock.picking` “Picking associated to this manufacturing order” (compute=_compute_picking_ids)
- `delivery_count` Integer “Delivery Orders” (compute=_compute_picking_ids)
- `confirm_cancel` Boolean (compute=_compute_confirm_cancel)
- `consumption` Selection (required, readonly)
- `mrp_production_child_count` Integer “Number of generated MO” (compute=_compute_mrp_production_child_count)
- `mrp_production_source_count` Integer “Number of source MO” (compute=_compute_mrp_production_source_count)
- `mrp_production_backorder_count` Integer “Count of linked backorder” (compute=_compute_mrp_production_backorder)
- `show_lock` Boolean “Show Lock/unlock buttons” (compute=_compute_show_lock)
- `components_availability` Char “Component Status” (compute=_compute_components_availability)
- `components_availability_state` Selection (compute=_compute_components_availability)
- `production_capacity` Float (compute=_compute_production_capacity)
- `show_lot_ids` Boolean “Display the serial number shortcut on the moves” (compute=_compute_show_lot_ids)
- `forecasted_issue` Boolean (compute=_compute_forecasted_issue)
- `show_serial_mass_produce` Boolean “Display the serial mass produce wizard action” (compute=_compute_show_serial_mass_produce)
- `show_allocation` Boolean (compute=_compute_show_allocation)
- `allow_workorder_dependencies` Boolean “Allow Work Order Dependencies”

Public methods: `action_assign`, `action_cancel`, `action_confirm`, `action_generate_serial`, `action_merge`, `action_product_forecast_report`, `action_see_move_scrap`, `action_serial_mass_produce_wizard`, `action_split`, `action_toggle_is_locked`, `action_view_mo_delivery`, `action_view_mrp_production_backorders`, `action_view_mrp_production_childs`, `action_view_mrp_production_sources`, `action_view_mrp_production_unbuilds`, `action_view_reception_report`, `button_mark_done`, `button_plan`, `button_scrap`, `button_unbuild`, `button_unplan`, `copy`, `copy_data`, `create`, `do_unreserve`, `get_empty_list_help`, `unlink`, `write`

Extension points: `_action_cancel`, `_action_confirm_mo_backorders`, `_action_generate_backorder_wizard`, `_action_generate_consumption_wizard`, `_action_generate_immediate_wizard`, `_check_byproducts`, `_check_immediate`, `_check_sn_uniqueness`, `_create_update_move_finished`, `_get_backorder_mo_vals`, `_get_children`, `_get_consumption_issues`, `_get_date_planned_finished`, `_get_default_date_planned_start`, `_get_default_is_locked`, `_get_default_picking_type_id`, `_get_document_iterate_key`, `_get_move_finished_values`, `_get_move_raw_values`, `_get_moves_finished_values`, `_get_moves_raw_values`, `_get_name_backorder`, `_get_origin`, `_get_produced_qty`, `_get_quantity_produced_issues`, `_get_quantity_to_backorder`, `_get_ready_to_produce_state`, `_get_sources`, `_post_inventory`, `_prepare_finished_extra_vals`, `_prepare_merge_orig_links`, `_prepare_procurement_group_vals`, `_prepare_stock_lot_values`

## `mrp.routing.workcenter` (defines)

Work Center Usage

- `name` Char “Operation” (required)
- `active` Boolean
- `workcenter_id` Many2one → `mrp.workcenter` (required)
- `sequence` Integer “Sequence”
- `bom_id` Many2one → `mrp.bom` (required, index)
- `company_id` Many2one → `res.company` (related=bom_id.company_id)
- `worksheet_type` Selection “Worksheet”
- `note` Html “Description”
- `worksheet` Binary “PDF”
- `worksheet_google_slide` Char “Google Slide”
- `time_mode` Selection “Duration Computation”
- `time_mode_batch` Integer “Based on”
- `time_computed_on` Char “Computed on last” (compute=_compute_time_computed_on)
- `time_cycle_manual` Float “Manual Duration”
- `time_cycle` Float “Duration” (compute=_compute_time_cycle)
- `workorder_count` Integer “# Work Orders” (compute=_compute_workorder_count)
- `workorder_ids` One2many → `mrp.workorder` “Work Orders”
- `possible_bom_product_template_attribute_value_ids` Many2many (related=bom_id.possible_product_template_attribute_value_ids)
- `bom_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` “Apply on Variants”
- `allow_operation_dependencies` Boolean (related=bom_id.allow_operation_dependencies)
- `blocked_by_operation_ids` Many2many → `mrp.routing.workcenter` “Blocked By”
- `needed_by_operation_ids` Many2many → `mrp.routing.workcenter` “Blocks”

Public methods: `action_archive`, `copy_existing_operations`, `copy_to_bom`, `write`

Extension points: `_check_no_cyclic_dependencies`, `_get_comparison_values`

## `mrp.unbuild` (defines)

Unbuild Order

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Reference” (readonly)
- `product_id` Many2one → `product.product` (required)
- `company_id` Many2one → `res.company` (required, index)
- `product_qty` Float “Quantity” (required)
- `product_uom_id` Many2one → `uom.uom` (required, store, compute=_compute_product_uom_id)
- `bom_id` Many2one → `mrp.bom`
- `mo_id` Many2one → `mrp.production`
- `mo_bom_id` Many2one → `mrp.bom` (related=mo_id.bom_id)
- `lot_id` Many2one → `stock.lot`
- `has_tracking` Selection (readonly, related=product_id.tracking)
- `location_id` Many2one → `stock.location` (required, store, compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (required, store, compute=_compute_location_id)
- `consume_line_ids` One2many → `stock.move` “Consumed Disassembly Lines” (readonly)
- `produce_line_ids` One2many → `stock.move` “Processed Disassembly Lines” (readonly)
- `state` Selection “Status”

Public methods: `action_unbuild`, `action_validate`, `create`

Extension points: `_check_qty`, `_prepare_finished_move_line_vals`, `_prepare_move_line_vals`

## `mrp.workcenter` (defines)

Work Center

Inherits: `resource.mixin`

- `name` Char “Work Center” (store, related=resource_id.name)
- `time_efficiency` Float “Time Efficiency” (store, related=resource_id.time_efficiency)
- `active` Boolean “Active” (store, related=resource_id.active)
- `code` Char “Code”
- `note` Html “Description”
- `default_capacity` Float “Capacity”
- `sequence` Integer “Sequence” (required)
- `color` Integer “Color”
- `currency_id` Many2one → `res.currency` (required, readonly, related=company_id.currency_id)
- `costs_hour` Float “Cost per hour”
- `time_start` Float “Setup Time”
- `time_stop` Float “Cleanup Time”
- `routing_line_ids` One2many → `mrp.routing.workcenter`
- `order_ids` One2many → `mrp.workorder`
- `workorder_count` Integer “# Work Orders” (compute=_compute_workorder_count)
- `workorder_ready_count` Integer “# Read Work Orders” (compute=_compute_workorder_count)
- `workorder_progress_count` Integer “Total Running Orders” (compute=_compute_workorder_count)
- `workorder_pending_count` Integer “Total Pending Orders” (compute=_compute_workorder_count)
- `workorder_late_count` Integer “Total Late Orders” (compute=_compute_workorder_count)
- `time_ids` One2many → `mrp.workcenter.productivity`
- `working_state` Selection (store, compute=_compute_working_state)
- `blocked_time` Float “Blocked Time” (compute=_compute_blocked_time)
- `productive_time` Float “Productive Time” (compute=_compute_productive_time)
- `oee` Float (compute=_compute_oee)
- `oee_target` Float “OEE Target”
- `performance` Integer “Performance” (compute=_compute_performance)
- `workcenter_load` Float “Work Center Load” (compute=_compute_workorder_count)
- `alternative_workcenter_ids` Many2many → `mrp.workcenter` “Alternative Workcenters”
- `tag_ids` Many2many → `mrp.workcenter.tag`
- `capacity_ids` One2many → `mrp.workcenter.capacity` “Product Capacities”

Public methods: `action_archive`, `action_show_operations`, `action_work_order`, `create`, `unblock`, `write`

Extension points: `_check_alternative_workcenter`, `_check_capacity`, `_get_capacity`, `_get_expected_duration`, `_get_first_available_slot`, `_get_unavailability_intervals`

## `mrp.workcenter.tag` (defines)

Add tag for the workcenter

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”

Extension points: `_get_default_color`

## `mrp.workcenter.productivity.loss.type` (defines)

MRP Workorder productivity losses

- `loss_type` Selection “Category” (required)

Public methods: `name_get`

## `mrp.workcenter.productivity.loss` (defines)

Workcenter Productivity Losses

- `name` Char “Blocking Reason” (required)
- `sequence` Integer “Sequence”
- `manual` Boolean “Is a Blocking Reason”
- `loss_id` Many2one → `mrp.workcenter.productivity.loss.type` “Category”
- `loss_type` Selection “Effectiveness Category” (store, related=loss_id.loss_type)

## `mrp.workcenter.productivity` (defines)

Workcenter Productivity Log

- `production_id` Many2one → `mrp.production` “Manufacturing Order” (readonly, related=workorder_id.production_id)
- `workcenter_id` Many2one → `mrp.workcenter` (required, index)
- `company_id` Many2one → `res.company` (required, index)
- `workorder_id` Many2one → `mrp.workorder` (index)
- `user_id` Many2one → `res.users`
- `loss_id` Many2one → `mrp.workcenter.productivity.loss` (required)
- `loss_type` Selection “Effectiveness” (store, related=loss_id.loss_type)
- `description` Text “Description”
- `date_start` Datetime “Start Date” (required)
- `date_end` Datetime “End Date”
- `duration` Float “Duration” (store, compute=_compute_duration)

Public methods: `button_block`

Extension points: `_check_open_time_ids`, `_get_default_company_id`

## `mrp.workcenter.capacity` (defines)

Work Center Capacity

- `workcenter_id` Many2one → `mrp.workcenter` “Work Center” (required)
- `product_id` Many2one → `product.product` “Product” (required)
- `product_uom_id` Many2one → `uom.uom` “Product UoM” (related=product_id.uom_id)
- `capacity` Float “Capacity”
- `time_start` Float “Setup Time (minutes)”
- `time_stop` Float “Cleanup Time (minutes)”

## `mrp.workorder` (defines)

Work Order

- `name` Char “Work Order” (required)
- `workcenter_id` Many2one → `mrp.workcenter` (required)
- `working_state` Selection “Workcenter Status” (related=workcenter_id.working_state)
- `product_id` Many2one (readonly, store, related=production_id.product_id)
- `product_tracking` Selection (related=product_id.tracking)
- `product_uom_id` Many2one → `uom.uom` (required, readonly)
- `production_id` Many2one → `mrp.production` (required, readonly)
- `production_availability` Selection “Stock Availability” (readonly, store, related=production_id.reservation_state)
- `production_state` Selection “Production State” (readonly, related=production_id.state)
- `production_bom_id` Many2one → `mrp.bom` (related=production_id.bom_id)
- `qty_production` Float “Original Production Quantity” (readonly, related=production_id.product_qty)
- `company_id` Many2one (related=production_id.company_id)
- `qty_producing` Float “Currently Produced Quantity” (compute=_compute_qty_producing)
- `qty_remaining` Float “Quantity To Be Produced” (compute=_compute_qty_remaining)
- `qty_produced` Float “Quantity” (readonly)
- `is_produced` Boolean “Has Been Produced” (compute=_compute_is_produced)
- `state` Selection “Status” (readonly, store, index, compute=_compute_state)
- `leave_id` Many2one → `resource.calendar.leaves`
- `date_planned_start` Datetime “Scheduled Start Date” (store, compute=_compute_dates_planned)
- `date_planned_finished` Datetime “Scheduled End Date” (store, compute=_compute_dates_planned)
- `date_start` Datetime “Start Date”
- `date_finished` Datetime “End Date”
- `duration_expected` Float “Expected Duration” (store, compute=_compute_duration_expected)
- `duration` Float “Real Duration” (store, compute=_compute_duration)
- `duration_unit` Float “Duration Per Unit” (readonly, store, compute=_compute_duration)
- `duration_percent` Integer “Duration Deviation (%)” (readonly, store, compute=_compute_duration)
- `progress` Float “Progress Done (%)” (compute=_compute_progress)
- `operation_id` Many2one → `mrp.routing.workcenter`
- `worksheet` Binary “Worksheet” (readonly, related=operation_id.worksheet)
- `worksheet_type` Selection “Worksheet Type” (readonly, related=operation_id.worksheet_type)
- `worksheet_google_slide` Char “Worksheet URL” (readonly, related=operation_id.worksheet_google_slide)
- `operation_note` Html “Description” (readonly, related=operation_id.note)
- `move_raw_ids` One2many → `stock.move`
- `move_finished_ids` One2many → `stock.move`
- `move_line_ids` One2many → `stock.move.line`
- `finished_lot_id` Many2one → `stock.lot` “Lot/Serial Number” (compute=_compute_finished_lot_id)
- `time_ids` One2many → `mrp.workcenter.productivity`
- `is_user_working` Boolean “Is the Current User Working” (compute=_compute_working_users)
- `working_user_ids` One2many → `res.users` “Working user on this work order.” (compute=_compute_working_users)
- `last_working_user_id` One2many → `res.users` “Last user that worked on this work order.” (compute=_compute_working_users)
- `costs_hour` Float “Cost per hour”
- `scrap_ids` One2many → `stock.scrap`
- `scrap_count` Integer “Scrap Move” (compute=_compute_scrap_move_count)
- `production_date` Datetime “Production Date” (store, related=production_id.date_planned_start)
- `json_popover` Char “Popover Data JSON” (compute=_compute_json_popover)
- `show_json_popover` Boolean “Show Popover?” (compute=_compute_json_popover)
- `consumption` Selection (related=production_id.consumption)
- `qty_reported_from_previous_wo` Float “Carried Quantity”
- `is_planned` Boolean (related=production_id.is_planned)
- `allow_workorder_dependencies` Boolean (related=production_id.allow_workorder_dependencies)
- `blocked_by_workorder_ids` Many2many → `mrp.workorder` “Blocked By”
- `needed_by_workorder_ids` Many2many → `mrp.workorder` “Blocks”

Public methods: `action_cancel`, `action_open_wizard`, `action_replan`, `action_see_move_scrap`, `button_done`, `button_finish`, `button_pending`, `button_scrap`, `button_start`, `button_unblock`, `create`, `end_all`, `end_previous`, `gantt_unavailability`, `get_working_duration`, `name_get`, `unlink`, `write`

Extension points: `_action_confirm`, `_check_no_cyclic_dependencies`, `_check_sn_uniqueness`, `_get_byproduct_move_to_update`, `_get_conflicted_workorder_ids`, `_get_duration_expected`, `_prepare_timeline_vals`

## `product.template` (extends)

- `bom_line_ids` One2many → `mrp.bom.line`
- `bom_ids` One2many → `mrp.bom`
- `bom_count` Integer “# Bill of Material” (compute=_compute_bom_count)
- `used_in_bom_count` Integer “# of BoM Where is Used” (compute=_compute_used_in_bom_count)
- `mrp_product_qty` Float “Manufactured” (compute=_compute_mrp_product_qty)
- `produce_delay` Float “Manufacturing Lead Time”
- `is_kits` Boolean (compute=_compute_is_kits)
- `days_to_prepare_mo` Float “Days to prepare Manufacturing Order”

Public methods: `action_archive`, `action_compute_bom_days`, `action_used_in_bom`, `action_view_mos`, `write`

## `product.product` (extends)

- `variant_bom_ids` One2many → `mrp.bom`
- `bom_line_ids` One2many → `mrp.bom.line`
- `bom_count` Integer “# Bill of Material” (compute=_compute_bom_count)
- `used_in_bom_count` Integer “# BoM Where Used” (compute=_compute_used_in_bom_count)
- `mrp_product_qty` Float “Manufactured” (compute=_compute_mrp_product_qty)
- `is_kits` Boolean (compute=_compute_is_kits)

Public methods: `action_archive`, `action_compute_bom_days`, `action_open_quants`, `action_used_in_bom`, `action_view_bom`, `action_view_mos`, `get_components`, `write`

## `res.company` (extends)

- `manufacturing_lead` Float “Manufacturing Lead Time” (required)

Public methods: `create_missing_unbuild_sequences`

Extension points: `_create_per_company_sequences`, `_create_unbuild_sequence`, `_get_security_by_rule_action`

## `res.config.settings` (extends)

- `manufacturing_lead` Float “Manufacturing Lead Time” (related=company_id.manufacturing_lead)
- `use_manufacturing_lead` Boolean “Default Manufacturing Lead Time”
- `group_mrp_byproducts` Boolean “By-Products”
- `module_mrp_mps` Boolean “Master Production Schedule”
- `module_mrp_plm` Boolean “Product Lifecycle Management (PLM)”
- `module_mrp_workorder` Boolean “Work Orders”
- `module_quality_control` Boolean “Quality”
- `module_quality_control_worksheet` Boolean “Quality Worksheet”
- `module_mrp_subcontracting` Boolean “Subcontracting”
- `group_mrp_routings` Boolean “MRP Work Orders”
- `group_unlocked_by_default` Boolean “Unlock Manufacturing Orders”
- `group_mrp_reception_report` Boolean “Allocation Report for Manufacturing Orders”
- `group_mrp_workorder_dependencies` Boolean “Work Order Dependencies”

Public methods: `set_values`

## `stock.lot` (extends)


Extension points: `_check_create`

## `stock.move.line` (extends)

- `workorder_id` Many2one → `mrp.workorder`
- `production_id` Many2one → `mrp.production`
- `description_bom_line` Char (related=move_id.description_bom_line)

Public methods: `create`, `write`

Extension points: `_get_aggregated_product_quantities`, `_get_aggregated_properties`, `_get_similar_move_lines`

## `stock.move` (extends)

- `created_production_id` Many2one → `mrp.production` (index)
- `production_id` Many2one → `mrp.production`
- `raw_material_production_id` Many2one → `mrp.production`
- `unbuild_id` Many2one → `mrp.unbuild`
- `consume_unbuild_id` Many2one → `mrp.unbuild`
- `allowed_operation_ids` One2many → `mrp.routing.workcenter` (related=raw_material_production_id.bom_id.operation_ids)
- `operation_id` Many2one → `mrp.routing.workcenter`
- `workorder_id` Many2one → `mrp.workorder`
- `bom_line_id` Many2one → `mrp.bom.line`
- `byproduct_id` Many2one → `mrp.bom.byproduct`
- `unit_factor` Float “Unit Factor” (store, compute=_compute_unit_factor)
- `is_done` Boolean “Done” (store, compute=_compute_is_done)
- `order_finished_lot_id` Many2one → `stock.lot` “Finished Lot/Serial Number” (store, related=raw_material_production_id.lot_producing_id)
- `should_consume_qty` Float “Quantity To Consume” (compute=_compute_should_consume_qty)
- `cost_share` Float “Cost Share (%)”
- `product_qty_available` Float “Product On Hand Quantity” (related=product_id.qty_available)
- `product_virtual_available` Float “Product Forecasted Quantity” (related=product_id.virtual_available)
- `description_bom_line` Char “Kit” (compute=_compute_description_bom_line)
- `manual_consumption` Boolean “Manual Consumption” (store, compute=_compute_manual_consumption)

Public methods: `action_explode`, `action_open_reference`, `action_show_details`, `create`, `default_get`, `write`

Extension points: `_action_assign`, `_action_cancel`, `_action_confirm`, `_get_backorder_move_vals`, `_get_source_document`, `_get_upstream_documents_and_responsibles`, `_prepare_merge_moves_distinct_fields`, `_prepare_merge_negative_moves_excluded_distinct_fields`, `_prepare_move_split_vals`, `_prepare_phantom_move_values`, `_prepare_procurement_origin`, `_prepare_procurement_values`

## `stock.warehouse.orderpoint` (extends)

- `show_bom` Boolean “Show BoM column” (compute=_compute_show_bom)
- `bom_id` Many2one → `mrp.bom` “Bill of Materials”
- `manufacturing_visibility_days` Float

Extension points: `_get_qty_multiple_to_order`, `_get_replenishment_order_notification`, `_post_process_scheduler`, `_prepare_procurement_values`

## `stock.picking.type` (extends)

- `code` Selection
- `count_mo_todo` Integer “Number of Manufacturing Orders to Process” (compute=_get_mo_count)
- `count_mo_waiting` Integer “Number of Manufacturing Orders Waiting” (compute=_get_mo_count)
- `count_mo_late` Integer “Number of Manufacturing Orders Late” (compute=_get_mo_count)
- `use_create_components_lots` Boolean “Create New Lots/Serial Numbers for Components”
- `use_auto_consume_components_lots` Boolean “Consume Reserved Lots/Serial Numbers automatically”

Public methods: `get_mrp_stock_picking_action_picking_type`

Extension points: `_get_mo_count`

## `stock.picking` (extends)

- `has_kits` Boolean (compute=_compute_has_kits)

## `stock.quant` (extends)


Public methods: `action_apply_inventory`

## `stock.rule` (extends)

- `action` Selection

Extension points: `_get_custom_move_fields`, `_get_date_planned`, `_get_lead_days`, `_get_matching_bom`, `_get_message_dict`, `_prepare_mo_vals`

## `procurement.group` (extends)

- `mrp_production_ids` One2many → `mrp.production`

Public methods: `run`

Extension points: `_get_moves_to_assign_domain`

## `stock.scrap` (extends)

- `production_id` Many2one → `mrp.production`
- `workorder_id` Many2one → `mrp.workorder`

Extension points: `_prepare_move_values`

## `stock.traceability.report` (extends)


Extension points: `_get_linked_move_lines`, `_get_reference`

## `stock.warehouse` (extends)

- `manufacture_to_resupply` Boolean “Manufacture to Resupply”
- `manufacture_pull_id` Many2one → `stock.rule`
- `manufacture_mto_pull_id` Many2one → `stock.rule`
- `pbm_mto_pull_id` Many2one → `stock.rule`
- `sam_rule_id` Many2one → `stock.rule`
- `manu_type_id` Many2one → `stock.picking.type`
- `pbm_type_id` Many2one → `stock.picking.type`
- `sam_type_id` Many2one → `stock.picking.type`
- `manufacture_steps` Selection (required)
- `pbm_route_id` Many2one → `stock.route`
- `pbm_loc_id` Many2one → `stock.location`
- `sam_loc_id` Many2one → `stock.location`

Public methods: `get_rules_dict`, `write`

Extension points: `_create_missing_locations`, `_get_all_routes`, `_get_global_route_rules_values`, `_get_locations_values`, `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_production_location`, `_get_route_name`, `_get_routes_values`, `_get_sequence_values`

## `stock.warehouse.orderpoint` (extends)


Public methods: `check_product_is_not_kit`

Extension points: `_get_orderpoint_products`

## `res.company` (extends)


## `product.product` (extends)


## `stock.warehouse` (extends)


## `mrp.bom` (extends)


## `mrp.bom.line` (extends)


## `mrp.workcenter` (extends)


## `mrp.routing.workcenter` (extends)


## `mrp.bom.byproduct` (extends)


## `mrp.production` (extends)


## `stock.move` (extends)


## `report.mrp.report_bom_structure` (defines)

BOM Overview Report


Public methods: `get_html`, `get_warehouses`

Extension points: `_get_availabilities`, `_get_bom_array_lines`, `_get_bom_data`, `_get_byproducts_lines`, `_get_component_data`, `_get_components_closest_forecasted`, `_get_max_component_delay`, `_get_operation_cost`, `_get_operation_line`, `_get_pdf_doc`, `_get_pdf_line`, `_get_quantities_info`, `_get_report_data`, `_get_report_values`, `_get_resupply_availability`, `_get_resupply_route_info`, `_get_stock_availability`

## `report.stock.report_reception` (extends)


Extension points: `_action_assign`, `_action_unassign`, `_get_doc_model`, `_get_doc_types`, `_get_docs`, `_get_extra_domain`, `_get_formatted_scheduled_date`, `_get_moves`

## `report.stock.report_stock_rule` (extends)


Extension points: `_get_rule_loc`

## `report.stock.report_product_product_replenishment` (extends)


## `change.production.qty` (defines)

Change Production Qty

- `mo_id` Many2one → `mrp.production` (required)
- `product_qty` Float “Quantity To Produce” (required)

Public methods: `change_prod_qty`, `default_get`

## `mrp.consumption.warning` (defines)

Wizard in case of consumption in warning/strict and more component has been used for a MO (related to the bom)

- `mrp_production_ids` Many2many → `mrp.production`
- `mrp_production_count` Integer (compute=_compute_mrp_production_count)
- `consumption` Selection (compute=_compute_consumption)
- `mrp_consumption_warning_line_ids` One2many → `mrp.consumption.warning.line`

Public methods: `action_cancel`, `action_confirm`, `action_set_qty`

## `mrp.consumption.warning.line` (defines)

Line of issue consumption

- `mrp_consumption_warning_id` Many2one → `mrp.consumption.warning` (required, readonly)
- `mrp_production_id` Many2one → `mrp.production` (required, readonly)
- `consumption` Selection (related=mrp_production_id.consumption)
- `product_id` Many2one → `product.product` (required, readonly)
- `product_uom_id` Many2one → `uom.uom` (readonly, related=product_id.uom_id)
- `product_consumed_qty_uom` Float “Consumed” (readonly)
- `product_expected_qty_uom` Float “To Consume” (readonly)

## `mrp.immediate.production.line` (defines)

Immediate Production Line

- `immediate_production_id` Many2one → `mrp.immediate.production` (required)
- `production_id` Many2one → `mrp.production` (required)
- `to_immediate` Boolean “To Process”

## `mrp.immediate.production` (defines)

Immediate Production

- `mo_ids` Many2many → `mrp.production`
- `show_productions` Boolean (compute=_compute_show_production)
- `immediate_production_line_ids` One2many → `mrp.immediate.production.line` “Immediate Production Lines”

Public methods: `default_get`, `process`

## `mrp.production.backorder.line` (defines)

Backorder Confirmation Line

- `mrp_production_backorder_id` Many2one → `mrp.production.backorder` (required)
- `mrp_production_id` Many2one → `mrp.production` (required, readonly)
- `to_backorder` Boolean “To Backorder”

## `mrp.production.backorder` (defines)

Wizard to mark as done or create back order

- `mrp_production_ids` Many2many → `mrp.production`
- `mrp_production_backorder_line_ids` One2many → `mrp.production.backorder.line` “Backorder Confirmation Lines”
- `show_backorder_lines` Boolean “Show backorder lines” (compute=_compute_show_backorder_lines)

Public methods: `action_backorder`, `action_close_mo`

## `mrp.production.split.multi` (defines)

Wizard to Split Multiple Productions

- `production_ids` One2many → `mrp.production.split`

## `mrp.production.split` (defines)

Wizard to Split a Production

- `production_split_multi_id` Many2one → `mrp.production.split.multi`
- `production_id` Many2one → `mrp.production` (readonly)
- `product_id` Many2one (related=production_id.product_id)
- `product_qty` Float (related=production_id.product_qty)
- `product_uom_id` Many2one (related=production_id.product_uom_id)
- `production_capacity` Float (related=production_id.production_capacity)
- `counter` Integer “Split #” (store, compute=_compute_counter)
- `production_detailed_vals_ids` One2many → `mrp.production.split.line` (store, compute=_compute_details)
- `valid_details` Boolean “Valid” (compute=_compute_valid_details)

Public methods: `action_prepare_split`, `action_return_to_list`, `action_split`

## `mrp.production.split.line` (defines)

Split Production Detail

- `mrp_production_split_id` Many2one → `mrp.production.split` (required)
- `quantity` Float “Quantity To Produce” (required)
- `user_id` Many2one → `res.users`
- `date` Datetime “Schedule Date”

## `stock.assign.serial` (extends)

- `production_id` Many2one → `mrp.production`
- `expected_qty` Float “Expected Quantity”
- `serial_numbers` Text “Produced Serial Numbers”
- `produced_qty` Float “Produced Quantity”
- `show_apply` Boolean
- `show_backorders` Boolean
- `multiple_lot_components_names` Text

Public methods: `apply`, `create_backorder`, `generate_serial_numbers_production`, `no_backorder`

Extension points: `_get_serial_numbers`

## `stock.warn.insufficient.qty.unbuild` (defines)

Warn Insufficient Unbuild Quantity

Inherits: `stock.warn.insufficient.qty`

- `unbuild_id` Many2one → `mrp.unbuild`

Public methods: `action_done`

Extension points: `_get_reference_document_company_id`
