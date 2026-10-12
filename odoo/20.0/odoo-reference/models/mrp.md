# mrp — Manufacturing

Depends on: product, stock, resource.

## `mrp.bom` (defines)

Bill of Material

Inherits: `mail.thread`, `product.catalog.mixin`

- `code` Char “Reference”
- `active` Boolean “Active”
- `type` Selection (required)
- `product_tmpl_id` Many2one → `product.template` (required, index)
- `product_id` Many2one → `product.product` (index)
- `bom_line_ids` One2many → `mrp.bom.line`
- `byproduct_ids` One2many → `mrp.bom.byproduct`
- `product_qty` Float “Quantity” (required)
- `uom_id` Many2one → `uom.uom` (required)
- `sequence` Integer “Sequence”
- `operation_ids` One2many → `mrp.routing.workcenter`
- `operation_count` Integer “Operations Count” (compute=_compute_operation_count)
- `component_count` Integer (compute=_compute_component_count)
- `subassembly_count` Integer (compute=_compute_subassembly_count)
- `show_copy_operations_button` Boolean (compute=_compute_show_copy_operations_button)
- `ready_to_produce` Selection “Manufacturing Readiness” (required)
- `picking_type_id` Many2one → `stock.picking.type`
- `company_id` Many2one → `res.company` (index)
- `possible_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` (compute=_compute_possible_product_template_attribute_value_ids)
- `allow_operation_dependencies` Boolean “Custom Operation Dependencies”
- `produce_delay` Integer “Manufacturing Lead Time”
- `days_to_prepare_mo` Integer “Days to prepare”
- `show_set_bom_button` Boolean (compute=_compute_show_set_bom_button)
- `batch_size` Float “Batch Size Value”
- `enable_batch_size` Boolean “Batch Size”
- `json_popover` Char “JSON data for the popover widget” (compute=_compute_json_popover)
- `note` Html “Additional Notes”
- `continuous` Boolean “Continuous Production”

Public methods: `action_archive`, `action_copy_existing_operations`, `action_open_exploded_bom_lines`, `action_open_operation_form`, `action_set_bom_on_orderpoint`, `action_unarchive`, `check_kit_has_not_orderpoint`, `copy`, `create`, `explode`, `get_import_templates`, `name_create`, `onchange_bom_structure`, `onchange_product_tmpl_id`, `write`

Extension points: `_check_bom_cycle`, `_check_bom_lines`, `_check_valid_batch_size`, `_get_exploded_bom_data`

## `mrp.bom.line` (defines)

Bill of Material Line

Inherits: `product.catalog.line.mixin`

- `product_id` Many2one → `product.product` (required, index)
- `product_tmpl_id` Many2one → `product.template` (store, index, related=product_id.product_tmpl_id)
- `company_id` Many2one (readonly, store, index, related=bom_id.company_id)
- `product_qty` Float “Quantity” (required)
- `uom_id` Many2one → `uom.uom` (required)
- `sequence` Integer “Sequence”
- `bom_id` Many2one → `mrp.bom` (required, index)
- `parent_product_tmpl_id` Many2one → `product.template` (related=bom_id.product_tmpl_id)
- `possible_bom_product_template_attribute_value_ids` Many2many (related=bom_id.possible_product_template_attribute_value_ids)
- `bom_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` “Apply on Variants”
- `allowed_operation_ids` One2many → `mrp.routing.workcenter` (related=bom_id.operation_ids)
- `operation_id` Many2one → `mrp.routing.workcenter`
- `child_bom_id` Many2one → `mrp.bom` (compute=_compute_child_bom_id)
- `child_line_ids` One2many → `mrp.bom.line` “BOM lines of the referred bom” (compute=_compute_child_line_ids)
- `tracking` Selection (related=product_id.tracking)
- `bom_code` Char (related=bom_id.code)
- `bom_type` Selection (related=bom_id.type)
- `bom_product_tmpl_id` Many2one (related=bom_id.product_tmpl_id)

Public methods: `action_add_from_catalog`, `action_open_parent_bom`, `action_open_product`, `create`, `onchange_product_id`, `search_fetch`, `write`

Extension points: `_check_bom_product_template_attribute_value_ids`, `_get_product_uom_field`, `_get_quantity_field`, `_prepare_bom_done_values`, `_prepare_line_done_values`

## `mrp.bom.byproduct` (defines)

Byproduct

Inherits: `product.catalog.line.mixin`

- `product_id` Many2one → `product.product` (required)
- `company_id` Many2one (readonly, store, index, related=bom_id.company_id)
- `product_qty` Float “Quantity” (required)
- `uom_id` Many2one → `uom.uom` (required, store, compute=_compute_uom_id)
- `bom_id` Many2one → `mrp.bom` (index)
- `allowed_operation_ids` One2many → `mrp.routing.workcenter` (related=bom_id.operation_ids)
- `operation_id` Many2one → `mrp.routing.workcenter`
- `possible_bom_product_template_attribute_value_ids` Many2many (related=bom_id.possible_product_template_attribute_value_ids)
- `bom_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` “Apply on Variants”
- `sequence` Integer “Sequence”
- `cost_share` Float “Cost Share (%)”

Public methods: `action_add_from_catalog`

Extension points: `_get_product_uom_field`, `_get_quantity_field`

## `mrp.production.group` (defines)

Production Group

- `name` Char “Name” (required)
- `production_ids` One2many → `mrp.production` “Productions”
- `child_ids` Many2many → `mrp.production.group` “Child Manufacturing Orders”
- `parent_ids` Many2many → `mrp.production.group` “Parent Manufacturing Orders”

## `mrp.production` (defines)

Manufacturing Order

Inherits: `mail.thread`, `mail.activity.mixin`, `product.catalog.mixin`

- `name` Char “Reference” (readonly)
- `priority` Selection “Priority”
- `backorder_sequence` Integer “Backorder Sequence”
- `origin` Char “Source”
- `product_id` Many2one → `product.product` (required, store, index, compute=_compute_product_id)
- `product_name` Char (compute=_compute_product_name)
- `product_default_code` Char (related=product_id.default_code)
- `production_group_id` Many2one → `mrp.production.group` (index)
- `product_variant_attributes` Many2many → `product.template.attribute.value` (related=product_id.product_template_attribute_value_ids)
- `valid_product_template_attribute_line_ids` Many2many (related=product_tmpl_id.valid_product_template_attribute_line_ids)
- `never_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` “Never attribute values”
- `workcenter_id` Many2one → `mrp.workcenter`
- `product_tracking` Selection (related=product_id.tracking)
- `product_tmpl_id` Many2one → `product.template` (related=product_id.product_tmpl_id)
- `product_qty` Float “Quantity To Produce” (required, store, compute=_compute_product_qty)
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `uom_id` Many2one → `uom.uom` (required, store, compute=_compute_uom_id)
- `lot_producing_ids` Many2many → `stock.lot` “Lot/Serial Number”
- `qty_producing` Float “Quantity Producing”
- `product_uom_qty` Float “Total Quantity” (store, compute=_compute_product_uom_qty)
- `picking_type_id` Many2one → `stock.picking.type` (required, store, index, compute=_compute_picking_type_id)
- `use_create_components_lots` Boolean (related=picking_type_id.use_create_components_lots)
- `location_src_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_src_id)
- `warehouse_id` Many2one (related=location_src_id.warehouse_id)
- `location_dest_id` Many2one → `stock.location` (required, store, compute=_compute_location_dest_id)
- `forecasted_location_id` Many2one → `stock.location`
- `date_deadline` Datetime “Deadline” (store, compute=_compute_date_deadline)
- `date_start` Datetime “Start” (required, index)
- `previous_date_start` Datetime
- `date_finished` Datetime “End” (store, compute=_compute_date_finished)
- `duration_expected` Float “Expected Duration” (store, compute=_compute_duration_expected)
- `duration` Float “Real Duration” (store, compute=_compute_duration)
- `bom_id` Many2one → `mrp.bom` (store, index, compute=_compute_bom_id)
- `state` Selection “State” (readonly, store, index, compute=_compute_state)
- `reservation_state` Selection “MO Readiness” (readonly, store, index, compute=_compute_reservation_state)
- `move_raw_ids` One2many → `stock.move` (store, compute=_compute_move_raw_ids)
- `move_finished_ids` One2many → `stock.move` (store, compute=_compute_move_finished_ids)
- `all_move_raw_ids` One2many → `stock.move`
- `all_move_ids` One2many → `stock.move`
- `move_byproduct_ids` One2many → `stock.move` (compute=_compute_move_byproduct_ids)
- `finished_move_line_ids` One2many → `stock.move.line` “Finished Product” (compute=_compute_lines)
- `workorder_ids` One2many → `mrp.workorder` (store, compute=_compute_workorder_ids)
- `move_dest_ids` One2many → `stock.move` “Stock Movements of Produced Goods”
- `unreserve_visible` Boolean “Allowed to Unreserve Production” (compute=_compute_unreserve_visible)
- `reserve_visible` Boolean “Allowed to Reserve Production” (compute=_compute_unreserve_visible)
- `user_id` Many2one → `res.users`
- `company_id` Many2one → `res.company` (required, index)
- `qty_produced` Float “Quantity Produced” (compute=_get_produced_qty)
- `reference_ids` Many2many → `stock.reference`
- `product_description_variants` Char “Custom Description”
- `orderpoint_id` Many2one → `stock.warehouse.orderpoint`
- `propagate_cancel` Boolean “Propagate cancel and split”
- `delay_alert_date` Datetime “Delay Alert Date” (compute=_compute_delay_alert_date)
- `json_popover` Char “JSON data for the popover widget” (compute=_compute_json_popover)
- `scrap_count` Integer “Scrap Move” (compute=_compute_scrap_move_count)
- `unbuild_ids` One2many → `mrp.unbuild`
- `unbuild_count` Integer “Number of Unbuilds” (compute=_compute_unbuild_count)
- `is_locked` Boolean “Is Locked”
- `is_planned` Boolean “Its Operations are Planned” (store, compute=_compute_is_planned)
- `show_final_lots` Boolean “Show Final Lots” (compute=_compute_show_lots)
- `production_location_id` Many2one → `stock.location` (store, compute=_compute_production_location)
- `picking_ids` Many2many → `stock.picking` “Picking associated to this manufacturing order” (compute=_compute_picking_ids)
- `delivery_count` Integer “Delivery Orders” (compute=_compute_picking_ids)
- `mrp_production_child_count` Integer “Number of generated MO” (compute=_compute_mrp_production_child_count)
- `mrp_production_all_child_count` Integer “Number of all generated MO” (compute=_compute_mrp_production_all_child_count)
- `mrp_production_all_child_done_count` Integer “Number of done all generated MO” (compute=_compute_mrp_production_all_child_count)
- `mrp_production_source_count` Integer “Number of source MO” (compute=_compute_mrp_production_source_count)
- `mrp_production_backorder_count` Integer “Count of linked backorder” (compute=_compute_mrp_production_backorder)
- `show_lock` Boolean “Show Lock/unlock buttons” (compute=_compute_show_lock)
- `components_availability` Char “Component Status” (compute=_compute_components_availability)
- `components_availability_state` Selection (compute=_compute_components_availability)
- `production_capacity` Float (compute=_compute_production_capacity)
- `show_lot_ids` Boolean “Display the serial number shortcut on the moves” (compute=_compute_show_lot_ids)
- `forecasted_issue` Boolean (compute=_compute_forecasted_issue)
- `show_allocation` Boolean (compute=_compute_show_allocation)
- `allow_workorder_dependencies` Boolean “Allow Work Order Dependencies”
- `show_generate_bom` Boolean “Show Generate BOM” (compute=_compute_show_generate_bom)
- `is_outdated_bom` Boolean “Outdated BoM”
- `is_delayed` Boolean (compute=_compute_is_delayed)
- `is_due_today` Boolean (compute=_compute_is_delayed)
- `search_date_category` Selection “Date Category” (readonly)
- `serial_numbers_count` Integer “Count of serial numbers” (compute=_compute_serial_numbers_count)
- `note` Html “Additional Notes” (store, compute=_compute_note)
- `remaining_time` Float “Remaining Working Time” (compute=_compute_remaining_time)
- `active_workcenter_ids` Many2many → `mrp.workcenter` (compute=_compute_active_workcenter_ids)
- `packages_count` Integer “Packages Count” (compute=_compute_packages_count)
- `package_history_ids` One2many → `stock.package.history` “Package History”
- `validate_button_style` Selection (compute=_compute_validate_button_style)

Public methods: `action_assign`, `action_cancel`, `action_clear_lot_producing_ids`, `action_confirm`, `action_detailed_operations`, `action_generate_bom`, `action_generate_serial`, `action_merge`, `action_open_label_layout`, `action_open_label_type`, `action_product_forecast_report`, `action_reset_to_draft`, `action_reset_to_progress`, `action_scrap`, `action_see_move_scrap`, `action_split`, `action_start`, `action_toggle_is_locked`, `action_update_bom`, `action_view_allocation_report`, `action_view_mo_delivery`, `action_view_mrp_production_all_childs`, `action_view_mrp_production_backorders`, `action_view_mrp_production_childs`, `action_view_mrp_production_sources`, `action_view_mrp_production_unbuilds`, `action_view_packages`, `action_view_serial_numbers`, `button_mark_done`, `button_plan`, `button_unbuild`, `button_unplan`, `copy_data`, `create`, `default_get`, `do_unreserve`, `get_empty_list_help`, `pre_button_mark_done`, `set_qty_producing`, `unlink`, `write`

Extension points: `_action_confirm_mo_backorders`, `_action_generate_backorder_wizard`, `_action_generate_consumption_wizard`, `_check_byproducts`, `_check_lot_producing_ids`, `_check_sn_uniqueness`, `_create_update_move_finished`, `_get_action_add_from_catalog_extra_context`, `_get_all_children`, `_get_autoprint_done_report_actions`, `_get_backorder_mo_vals`, `_get_bom_values`, `_get_children`, `_get_consumption_issues`, `_get_default_date_finished`, `_get_default_date_start`, `_get_default_is_locked`, `_get_default_picking_type_id`, `_get_document_iterate_key`, `_get_move_finished_values`, `_get_move_raw_values`, `_get_moves_finished_values`, `_get_moves_raw_values`, `_get_name_backorder`, `_get_origin`, `_get_packages_for_print`, `_get_produced_qty`, `_get_product_catalog_domain`, `_get_quantity_produced_issues`, `_get_quantity_to_backorder`, `_get_ratio_between_mo_and_bom_quantities`, `_get_ready_to_produce_state`, `_get_sources`, `_post_inventory`, `_post_run_manufacture`, `_prepare_finished_extra_vals`, `_prepare_merge_orig_links`, `_prepare_stock_lot_values`

## `mrp.routing.workcenter` (defines)

Work Center Usage

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Operation” (required)
- `active` Boolean
- `workcenter_id` Many2one → `mrp.workcenter` (required, index)
- `sequence` Integer “Sequence”
- `bom_id` Many2one → `mrp.bom` (required, index)
- `company_id` Many2one → `res.company` (related=bom_id.company_id)
- `time_mode` Selection “Duration Computation”
- `time_mode_batch` Integer “Based on”
- `time_computed_on` Char “Computed on last” (compute=_compute_time_computed_on)
- `time_cycle_manual` Float “Manual Duration”
- `time_cycle` Float “Cycles” (compute=_compute_time_cycle)
- `workorder_count` Integer “# Work Orders” (compute=_compute_workorder_count)
- `workorder_ids` One2many → `mrp.workorder` “Work Orders”
- `possible_bom_product_template_attribute_value_ids` Many2many (related=bom_id.possible_product_template_attribute_value_ids)
- `bom_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` “Apply on Variants”
- `allow_operation_dependencies` Boolean (related=bom_id.allow_operation_dependencies)
- `blocked_by_operation_ids` Many2many → `mrp.routing.workcenter` “Blocked By”
- `needed_by_operation_ids` Many2many → `mrp.routing.workcenter` “Blocks”
- `cycle_number` Integer “Repetitions” (compute=_compute_time_cycle)
- `time_total` Float “Total Duration” (compute=_compute_time_cycle)
- `show_time_total` Boolean “Show Total Duration?” (compute=_compute_time_cycle)
- `cost_mode` Selection “Cost based on”
- `cost` Float “Cost” (compute=_compute_cost)

Public methods: `action_archive`, `action_open_operation_form`, `action_unarchive`, `copy_existing_operations`, `copy_to_bom`, `create`, `write`

Extension points: `_check_no_cyclic_dependencies`

## `mrp.unbuild` (defines)

Unbuild Order

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Reference” (readonly)
- `product_id` Many2one → `product.product` (required, store, compute=_compute_product_id)
- `company_id` Many2one → `res.company` (required, index)
- `product_qty` Float “Quantity” (required, store, compute=_compute_product_qty)
- `uom_id` Many2one → `uom.uom` (required, store, compute=_compute_uom_id)
- `bom_id` Many2one → `mrp.bom` (store, compute=_compute_bom_id)
- `mo_id` Many2one → `mrp.production`
- `mo_bom_id` Many2one → `mrp.bom` (related=mo_id.bom_id)
- `lot_producing_ids` Many2many → `stock.lot` “Lot/Serial Numbers” (related=mo_id.lot_producing_ids)
- `lot_ids` Many2many → `stock.lot` “Lot/Serial Number”
- `has_tracking` Selection (readonly, related=product_id.tracking)
- `location_id` Many2one → `stock.location` (required, store, compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (required, store, compute=_compute_location_dest_id)
- `consume_line_ids` One2many → `stock.move` “Consumed Disassembly Lines” (readonly)
- `produce_line_ids` One2many → `stock.move` “Processed Disassembly Lines” (readonly)
- `state` Selection “Status”

Public methods: `action_clear_lots`, `action_unbuild`, `action_validate`, `create`

Extension points: `_prepare_finished_move_line_vals`, `_prepare_move_line_vals`

## `mrp.workcenter` (defines)

Work Center

Inherits: `mail.thread`, `resource.mixin`

- `name` Char “Work Center” (store, related=resource_id.name)
- `barcode` Char “Barcode”
- `time_efficiency` Float “Time Efficiency” (store, related=resource_id.time_efficiency)
- `active` Boolean “Active” (store, related=resource_id.active)
- `code` Char “Code”
- `note` Html “Description”
- `sequence` Integer “Sequence” (required)
- `color` Integer “Color”
- `currency_id` Many2one → `res.currency` (required, readonly, related=company_id.currency_id)
- `costs_hour` Float “Cost per hour”
- `time_start` Float “Setup Time”
- `time_stop` Float “Cleanup Time”
- `routing_line_ids` One2many → `mrp.routing.workcenter`
- `has_routing_lines` Boolean (compute=_compute_has_routing_lines)
- `order_ids` One2many → `mrp.workorder`
- `workorder_count` Integer “# Work Orders” (compute=_compute_workorder_count)
- `workorder_ready_count` Integer “# To Do Work Orders” (compute=_compute_workorder_count)
- `workorder_progress_count` Integer “Total Running Orders” (compute=_compute_workorder_count)
- `workorder_blocked_count` Integer “Total Pending Orders” (compute=_compute_workorder_count)
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
- `kanban_dashboard_graph` Text (compute=_compute_kanban_dashboard_graph)
- `resource_calendar_id` Many2one

Public methods: `action_archive`, `action_show_operations`, `action_work_order`, `action_work_order_alternatives`, `create`, `unblock`, `write`

Extension points: `_check_alternative_workcenter`, `_get_capacity`, `_get_first_available_slot`, `_get_unavailability_intervals`, `_get_week_range_and_first_last_days`, `_get_workcenter_load_per_week`, `_prepare_graph_data`

## `mrp.workcenter.tag` (defines)

Add tag for the workcenter

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”

Extension points: `_get_default_color`

## `mrp.workcenter.productivity.loss.type` (defines)

Workorder Productivity Loss Type

- `loss_type` Selection “Category” (required)

## `mrp.workcenter.productivity.loss` (defines)

Workcenter Productivity Loss

- `name` Char “Blocking Reason” (required)
- `sequence` Integer “Sequence”
- `manual` Boolean “Is a Blocking Reason”
- `loss_id` Many2one → `mrp.workcenter.productivity.loss.type` “Category”
- `loss_type` Selection “Effectiveness Category” (related=loss_id.loss_type)

## `mrp.workcenter.productivity` (defines)

Workcenter Productivity Log

- `production_id` Many2one → `mrp.production` “Manufacturing Order” (readonly, related=workorder_id.production_id)
- `workcenter_id` Many2one → `mrp.workcenter` (required, index)
- `company_id` Many2one → `res.company` (required, index)
- `workorder_id` Many2one → `mrp.workorder` (index)
- `user_id` Many2one → `res.users`
- `loss_id` Many2one → `mrp.workcenter.productivity.loss` (required)
- `loss_type` Selection “Effectiveness” (related=loss_id.loss_type)
- `description` Text “Description”
- `date_start` Datetime “Start Date” (required)
- `date_end` Datetime “End Date”
- `duration` Float “Duration” (store, compute=_compute_duration)

Public methods: `button_block`

Extension points: `_check_open_time_ids`, `_get_default_company_id`

## `mrp.workcenter.capacity` (defines)

Work Center Capacity

- `workcenter_id` Many2one → `mrp.workcenter` “Work Center” (required, index)
- `product_id` Many2one → `product.product` “Product”
- `uom_id` Many2one → `uom.uom` “Unit” (required, store, compute=_compute_uom_id)
- `capacity` Float “Capacity”
- `time_start` Float “Setup Time”
- `time_stop` Float “Cleanup Time”

## `mrp.workorder` (defines)

Work Order

Inherits: `mail.thread`, `mail.activity.mixin`, `product.catalog.mixin`

- `name` Char “Work Order” (required)
- `sequence` Integer “Sequence” (store, compute=_compute_sequence)
- `barcode` Char (store, compute=_compute_barcode)
- `workcenter_id` Many2one → `mrp.workcenter` (required, index)
- `working_state` Selection “Workcenter Status” (related=workcenter_id.working_state)
- `product_id` Many2one (related=production_id.product_id)
- `product_tracking` Selection (related=product_id.tracking)
- `uom_id` Many2one (related=production_id.uom_id)
- `product_variant_attributes` Many2many → `product.template.attribute.value` (related=product_id.product_template_attribute_value_ids)
- `production_id` Many2one → `mrp.production` (required, readonly)
- `production_lot_producing_id` Many2many → `stock.lot` (related=production_id.lot_producing_ids)
- `production_availability` Selection “Stock Availability” (readonly, store, related=production_id.reservation_state)
- `production_state` Selection “Production State” (readonly, related=production_id.state)
- `production_bom_id` Many2one → `mrp.bom` (related=production_id.bom_id)
- `qty_production` Float “Original Production Quantity” (readonly, related=production_id.product_qty)
- `company_id` Many2one (related=production_id.company_id)
- `priority` Selection (related=production_id.priority)
- `qty_producing` Float “Currently Produced Quantity” (compute=_compute_qty_producing)
- `qty_remaining` Float “Quantity To Be Produced” (compute=_compute_qty_remaining)
- `qty_produced` Float “Quantity Done”
- `qty_ready` Float “Quantity Ready” (compute=_compute_qty_ready)
- `is_produced` Boolean “Has Been Produced” (compute=_compute_is_produced)
- `state` Selection “Status” (store, index, compute=_compute_state)
- `leave_id` Many2one → `resource.calendar.leaves`
- `date_start` Datetime “Planned Date” (store, compute=_compute_dates)
- `date_finished` Datetime “End” (store, compute=_compute_dates)
- `duration_expected` Float “Expected Duration” (store, compute=_compute_duration_expected)
- `duration` Float “Real Duration” (store, compute=_compute_duration)
- `duration_unit` Float “Duration Per Unit” (readonly, store, compute=_compute_duration)
- `duration_percent` Integer “Duration Deviation (%)” (readonly, store, compute=_compute_duration)
- `progress` Float “Progress Done (%)” (compute=_compute_progress)
- `operation_id` Many2one → `mrp.routing.workcenter`
- `move_raw_ids` One2many → `stock.move`
- `move_finished_ids` One2many → `stock.move`
- `move_line_ids` One2many → `stock.move.line`
- `time_ids` One2many → `mrp.workcenter.productivity`
- `is_user_working` Boolean “Is the Current User Working” (compute=_compute_working_users)
- `working_user_ids` One2many → `res.users` “Working user on this work order.” (compute=_compute_working_users)
- `last_working_user_id` Many2one → `res.users` “Last user that worked on this work order.” (compute=_compute_working_users)
- `costs_hour` Float “Cost per hour”
- `cost_mode` Selection
- `cost` Float “Cost” (store, compute=_compute_cost)
- `production_date` Datetime “Production Date” (store, compute=_compute_production_date)
- `qty_reported_from_previous_wo` Float “Carried Quantity”
- `is_planned` Boolean (compute=_compute_is_planned)
- `allow_workorder_dependencies` Boolean (related=production_id.allow_workorder_dependencies)
- `blocked_by_workorder_ids` Many2many → `mrp.workorder` “Blocked By”
- `needed_by_workorder_ids` Many2many → `mrp.workorder` “Blocks”
- `remaining_time` Float “Remaining Working Time” (compute=_compute_remaining_time)
- `color` Integer “Color” (related=production_id.id)
- `has_conflicts` Boolean “Has conflicts” (compute=_compute_has_conflicts)
- `has_planning_issues` Boolean “Has planning issues” (compute=_compute_has_planning_issues)
- `production_reference_ids` Many2many “References” (readonly, related=production_id.reference_ids)
- `decoration_dates` Char (compute=_compute_decoration_dates)
- `picking_type_id` Many2one (related=production_id.picking_type_id)
- `properties` Properties “Properties”
- `qty_to_produce` Float “Quantity To Produce” (compute=_compute_qty_to_produce)
- `backorder_count` Integer “Count of linked backorders” (compute=_compute_backorder)

Public methods: `action_cancel`, `action_mark_as_done`, `action_plan`, `action_replan`, `action_scrap`, `action_select_mo_to_plan`, `action_unplan`, `action_view_backorders`, `button_finish`, `button_pending`, `button_start`, `button_unblock`, `create`, `end_all`, `end_previous`, `get_duration`, `set_state`, `unlink`, `web_resequence`, `write`

Extension points: `_action_confirm`, `_action_plan`, `_action_reset_to_draft`, `_action_reset_to_progress`, `_check_no_cyclic_dependencies`, `_get_action_add_from_catalog_extra_context`, `_get_backorders`, `_get_conflicted_workorder_ids`, `_get_duration_expected`, `_get_operation_values`, `_get_product_catalog_domain`, `_prepare_timeline_vals`

## `product.template` (extends)

- `bom_line_ids` One2many → `mrp.bom.line`
- `bom_ids` One2many → `mrp.bom`
- `bom_count` Integer “# Bill of Material” (compute=_compute_bom_count)
- `used_in_bom_count` Integer “# of BoM Where is Used” (compute=_compute_used_in_bom_count)
- `mrp_product_qty` Float “Manufactured” (compute=_compute_mrp_product_qty)
- `is_kits` Boolean (compute=_compute_is_kits)

Public methods: `action_archive`, `action_used_in_bom`, `action_view_mos`, `write`

Extension points: `_get_backend_root_menu_ids`

## `product.product` (extends)

- `variant_bom_ids` One2many → `mrp.bom`
- `bom_line_ids` One2many → `mrp.bom.line`
- `bom_count` Integer “# Bill of Material” (compute=_compute_bom_count)
- `used_in_bom_count` Integer “# BoM Where Used” (compute=_compute_used_in_bom_count)
- `mrp_product_qty` Float “Manufactured” (compute=_compute_mrp_product_qty)
- `is_kits` Boolean (compute=_compute_is_kits)

Public methods: `action_archive`, `action_open_quants`, `action_used_in_bom`, `action_view_bom`, `action_view_mos`, `get_components`, `get_routes_actions`, `write`

Extension points: `_get_backend_root_menu_ids`

## `product.uom` (extends)

- `allowed_uom_ids` Many2many

## `res.company` (extends)


Public methods: `create_missing_unbuild_sequences`

Extension points: `_create_per_company_sequences`, `_create_unbuild_sequence`

## `res.config.settings` (extends)

- `group_mrp_byproducts` Boolean “By-Products”
- `module_mrp_mps` Boolean “Master Production Schedule”
- `module_mrp_plm` Boolean “Product Lifecycle Management (PLM)”
- `module_quality_control` Boolean “Quality”
- `module_quality_control_worksheet` Boolean “Quality Worksheet”
- `module_mrp_subcontracting` Boolean “Subcontracting”
- `group_mrp_routings` Boolean “MRP Work Orders”
- `group_unlocked_by_default` Boolean “Unlock Manufacturing Orders”

Public methods: `set_values`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `stock.lot` (extends)


Extension points: `_check_create`

## `stock.move` (extends)

- `created_production_id` Many2one → `mrp.production` (index)
- `production_id` Many2one → `mrp.production`
- `raw_material_production_id` Many2one → `mrp.production`
- `production_group_id` Many2one → `mrp.production.group`
- `unbuild_id` Many2one → `mrp.unbuild`
- `consume_unbuild_id` Many2one → `mrp.unbuild`
- `allowed_operation_ids` One2many → `mrp.routing.workcenter` (related=raw_material_production_id.bom_id.operation_ids)
- `operation_id` Many2one → `mrp.routing.workcenter`
- `workorder_id` Many2one → `mrp.workorder`
- `bom_line_id` Many2one → `mrp.bom.line`
- `byproduct_id` Many2one → `mrp.bom.byproduct`
- `unit_factor` Float “Unit Factor” (store, compute=_compute_unit_factor)
- `should_consume_qty` Float “Quantity To Consume” (compute=_compute_should_consume_qty)
- `cost_share` Float “Cost Share (%)”
- `product_qty_available` Float “Product On Hand Quantity” (related=product_id.qty_available)
- `product_virtual_available` Float “Product Forecasted Quantity” (related=product_id.virtual_available)

Public methods: `action_add_from_catalog_byproduct`, `action_add_from_catalog_raw`, `action_add_from_catalog_wo`, `action_explode`, `action_open_reference`, `action_show_details`, `create`, `default_get`, `write`

Extension points: `_action_assign`, `_action_cancel`, `_action_confirm`, `_action_done`, `_action_replenish`, `_action_reset_to_progress`, `_check_negative_quantity`, `_get_backorder_move_vals`, `_get_production_assignation_domain`, `_get_relevant_state_among_moves`, `_get_source_document`, `_get_upstream_documents_and_responsibles`, `_prepare_merge_moves_distinct_fields`, `_prepare_merge_negative_moves_excluded_distinct_fields`, `_prepare_move_line_vals`, `_prepare_move_split_vals`, `_prepare_phantom_move_values`, `_prepare_procurement_origin`, `_prepare_procurement_values`, `_prepare_scrap_move_vals`

## `stock.move.line` (extends)

- `workorder_id` Many2one → `mrp.workorder`
- `production_id` Many2one → `mrp.production`
- `visual_lot_name` Char “Visual Pre-generated Lot” (compute=_compute_visual_lot_name)

Public methods: `create`, `write`

Extension points: `_get_aggregated_product_quantities`, `_get_aggregated_properties`, `_get_linkable_moves`, `_get_similar_move_lines`, `_prepare_stock_move_vals`

## `stock.warehouse.orderpoint` (extends)

- `show_bom` Boolean “Show BoM column” (compute=_compute_show_bom)
- `bom_id` Many2one → `mrp.bom` “Bill of Materials”
- `bom_id_placeholder` Char (compute=_compute_bom_id_placeholder)
- `effective_bom_id` Many2one → `mrp.bom` “Effective Bill of Materials” (compute=_compute_effective_bom_id)

Extension points: `_get_default_bom`, `_get_default_route`, `_get_lead_days_values`, `_get_replenishment_multiple_alternative`, `_get_replenishment_order_notification`, `_post_process_scheduler`, `_prepare_procurement_values`

## `stock.package` (extends)


Extension points: `_get_package_vals`

## `stock.package.history` (extends)

- `production_id` Many2one → `mrp.production` (index)

## `stock.picking.type` (extends)

- `code` Selection
- `count_mo_todo` Integer “Number of Manufacturing Orders to Process” (compute=_get_mo_count)
- `count_mo_waiting` Integer “Number of Manufacturing Orders Waiting” (compute=_get_mo_count)
- `count_mo_late` Integer “Number of Manufacturing Orders Late” (compute=_get_mo_count)
- `count_mo_in_progress` Integer “Number of Manufacturing Orders In Progress” (compute=_get_mo_count)
- `count_mo_to_close` Integer “Number of Manufacturing Orders To Close” (compute=_get_mo_count)
- `use_create_components_lots` Boolean “Create New Lots/Serial Numbers for Components”
- `auto_confirm_production` Boolean “Auto Confirm Production”
- `auto_print_done_production_order` Boolean “Auto Print Done Production Order”
- `auto_print_done_mrp_product_labels` Boolean “Auto Print Produced Product Labels”
- `mrp_product_label_to_print` Selection “Product Label to Print”
- `auto_print_done_mrp_lot` Boolean “Auto Print Produced Lot Label”
- `done_mrp_lot_label_to_print` Selection “Lot/SN Label to Print”
- `auto_print_mrp_reception_report` Boolean “Auto Print Allocation Report”
- `auto_print_mrp_reception_report_labels` Boolean “Auto Print Allocation Report Labels”
- `auto_print_generated_mrp_lot` Boolean “Auto Print Generated Lot/SN Label”
- `generated_mrp_lot_label_to_print` Selection “Generated Lot/SN Label to Print”
- `wo_properties_definition` PropertiesDefinition “Workorder Properties”

Public methods: `get_mrp_stock_picking_action_picking_type`

Extension points: `_check_default_location`, `_get_aggregated_records_by_date`, `_get_mo_count`, `_get_mrp_product_label_to_print_selection`

## `stock.picking` (extends)

- `has_kits` Boolean (compute=_compute_has_kits)
- `production_count` Integer “Count of MO generated” (compute=_compute_mrp_production_ids)
- `production_ids` One2many → `mrp.production` “Manufacturing Orders” (compute=_compute_production_ids)
- `production_group_id` Many2one → `mrp.production.group` “Production Group” (related=move_ids.production_group_id)

Public methods: `action_detailed_operations`, `action_view_mrp_production`, `get_action_click_graph`

## `stock.quant` (extends)


Extension points: `_check_kits`

## `stock.reference` (extends)

- `production_ids` Many2many → `mrp.production` “Productions”

## `stock.replenish.mixin` (extends)

- `bom_id` Many2one → `mrp.bom` “Bill of Material”
- `show_bom` Boolean (compute=_compute_show_bom)

Extension points: `_get_show_bom`

## `stock.rule` (extends)

- `action` Selection

Public methods: `run`

Extension points: `_get_custom_move_fields`, `_get_date_planned`, `_get_lead_days`, `_get_matching_bom`, `_get_message_dict`, `_get_moves_to_assign_domain`, `_get_stock_move_values`, `_prepare_mo_vals`

## `stock.route` (extends)


Extension points: `_get_non_push_pull_rule_actions`

## `stock.warehouse` (extends)

- `manufacture_to_resupply` Boolean “Manufacture to Resupply” (compute=_compute_manufacture_to_resupply)
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

Extension points: `_create_missing_locations`, `_create_or_update_route`, `_get_all_routes`, `_get_locations_values`, `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_production_location`, `_get_route_name`, `_get_routes_values`, `_get_sequence_values`

## `stock.warehouse.orderpoint` (extends)


Public methods: `check_product_is_not_kit`

Extension points: `_get_orderpoint_products`

## `report.mrp.report_bom_structure` (defines)

BOM Overview Report


Public methods: `get_html`, `get_warehouses`

Extension points: `_get_availabilities`, `_get_bom_array_lines`, `_get_bom_data`, `_get_byproducts_lines`, `_get_component_available_qty`, `_get_component_data`, `_get_component_forecast_available_qty`, `_get_components_closest_forecasted`, `_get_last_availability`, `_get_max_component_delay`, `_get_operation_line`, `_get_pdf_doc`, `_get_pdf_line`, `_get_quantities_info`, `_get_report_data`, `_get_report_values`, `_get_resupply_availability`, `_get_resupply_route_info`, `_get_stock_availability`

## `report.mrp.report_mo_overview` (defines)

MO Overview Report


Public methods: `get_report_values`

Extension points: `_check_planned_start`, `_get_byproducts_data`, `_get_comparison_decorator`, `_get_component_real_cost`, `_get_component_receipt`, `_get_components_data`, `_get_cost_breakdown_data`, `_get_display_context`, `_get_extra_replenishments`, `_get_finished_operation_data`, `_get_location_ids`, `_get_mo_cost_sum`, `_get_mo_summary`, `_get_operations_data`, `_get_origin`, `_get_replenish_data`, `_get_replenishment_from_moves`, `_get_replenishment_lines`, `_get_replenishment_mo_cost`, `_get_replenishment_receipt`, `_get_replenishments_from_forecast`, `_get_report_data`, `_get_report_extra_lines`, `_get_report_values`, `_get_reserved_qty`, `_get_resupply_data`, `_get_resupply_rules`, `_get_unit_cost`, `_get_uom_precision`

## `report.stock.report_stock_rule` (extends)


Extension points: `_get_rule_loc`

## `stock.allocation.report` (extends)


Extension points: `_get_docs`, `_get_docs_type`, `_get_moves`

## `stock.forecasted_product_product` (extends)


Extension points: `_get_report_header`, `_get_reservation_data`, `_prepare_report_line`

## `stock.traceability.report` (extends)


Public methods: `get_lines`

Extension points: `_get_linked_move_lines`, `_get_production_lines`, `_get_reference`

## `change.production.qty` (defines)

Change Production Qty

- `mo_id` Many2one → `mrp.production` (required)
- `product_qty` Float “Quantity To Produce” (required)

Public methods: `change_prod_qty`, `default_get`

## `mrp.consumption.warning` (defines)

Wizard for warning about mismatching expected vs actual component consumption quantities for MOs

- `mrp_production_ids` Many2many → `mrp.production`
- `mrp_production_count` Integer (compute=_compute_mrp_production_count)
- `mrp_consumption_warning_line_ids` One2many → `mrp.consumption.warning.line`

Public methods: `action_cancel`, `action_confirm`, `action_set_qty`

## `mrp.consumption.warning.line` (defines)

Line of issue consumption

- `mrp_consumption_warning_id` Many2one → `mrp.consumption.warning` (required, readonly)
- `mrp_production_id` Many2one → `mrp.production` (required, readonly)
- `product_id` Many2one → `product.product` (required, readonly)
- `uom_id` Many2one → `uom.uom` (readonly)
- `product_consumed_qty_uom` Float “Consumed” (readonly)
- `product_expected_qty_uom` Float “To Consume” (readonly)
- `move_id` Many2one → `stock.move` (readonly)

## `mrp.finished.product.label.layout` (defines)

Finished Product Label Layout

Inherits: `product.label.layout`


Extension points: `_get_label_requests`, `_get_label_template_xml_id`

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

## `mrp.production.serials` (defines)

Assign serial numbers to production order

- `production_id` Many2one → `mrp.production`
- `workorder_id` Many2one → `mrp.workorder`
- `qty_produced` Float “Quantity Produced”
- `lot_name` Char “First SN” (store, compute=_compute_lot_name)
- `lot_quantity` Integer “Number of SN” (store, compute=_compute_lot_quantity)
- `serial_numbers` Text “Produced Serial Numbers” (store, compute=_compute_lot_name)

Public methods: `action_apply`, `action_generate_serial_numbers`, `action_split_and_assign_serials`

## `mrp.production.split.multi` (defines)

Wizard to Split Multiple Productions

- `production_ids` One2many → `mrp.production.split`

## `mrp.production.split` (defines)

Wizard to Split a Production

- `production_split_multi_id` Many2one → `mrp.production.split.multi`
- `production_id` Many2one → `mrp.production` (readonly)
- `product_id` Many2one (related=production_id.product_id)
- `product_qty` Float (related=production_id.product_qty)
- `uom_id` Many2one (related=production_id.uom_id)
- `production_capacity` Float (related=production_id.production_capacity)
- `production_detailed_vals_ids` One2many → `mrp.production.split.line` (store, compute=_compute_details)
- `valid_details` Boolean “Valid” (compute=_compute_valid_details)
- `max_batch_size` Float “Max Batch Size” (compute=_compute_max_batch_size)
- `num_splits` Integer “# Splits” (readonly, compute=_compute_num_splits)

Public methods: `action_prepare_split`, `action_return_to_list`, `action_split`

## `mrp.production.split.line` (defines)

Split Production Detail

- `mrp_production_split_id` Many2one → `mrp.production.split` (required)
- `quantity` Float “Quantity To Produce” (required)
- `user_id` Many2one → `res.users`
- `date` Datetime “Schedule Date”

## `product.replenish` (extends)


Extension points: `_get_date_planned`, `_get_record_to_notify`, `_get_replenishment_order_notification_link`, `_get_route_domain`

## `picking.label.type` (extends)

- `production_ids` Many2many → `mrp.production`

Public methods: `process`

## `stock.replenishment.info` (extends)

Stock supplier replenishment information

- `bom_id` Many2one (related=orderpoint_id.bom_id)
- `bom_ids` Many2many → `mrp.bom` (store, compute=_compute_bom_ids)
- `show_bom_tab` Boolean (compute=_compute_show_bom_tab)

## `stock.warn.insufficient.qty.unbuild` (defines)

Warn Insufficient Unbuild Quantity

Inherits: `stock.warn.insufficient.qty`

- `unbuild_id` Many2one → `mrp.unbuild`

Public methods: `action_done`

Extension points: `_get_reference_document_company_id`
