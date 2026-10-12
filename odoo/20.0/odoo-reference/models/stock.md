# stock — Inventory

Depends on: product, barcodes_gs1_nomenclature, digest.

## `barcode.rule` (extends)

- `type` Selection

## `digest.digest` (extends)

- `kpi_stock_delivery_count` Boolean “Deliveries”
- `kpi_stock_delivery_count_value` Integer (compute=_compute_kpi_stock_delivery_count_value)
- `kpi_stock_receipt_count` Boolean “Receipts”
- `kpi_stock_receipt_count_value` Integer (compute=_compute_kpi_stock_receipt_count_value)

Extension points: `_get_kpi_custom_settings`

## `ir.actions.report` (extends)


Extension points: `_get_rendering_context`

## `product.product` (extends)

- `stock_quant_ids` One2many → `stock.quant`
- `stock_move_ids` One2many → `stock.move`
- `qty_available` Float “Quantity On Hand” (compute=_compute_quantities)
- `virtual_available` Float
- `free_qty` Float “Free To Use Quantity ” (compute=_compute_quantities)
- `incoming_qty` Float
- `outgoing_qty` Float
- `orderpoint_ids` One2many → `stock.warehouse.orderpoint`
- `nbr_moves_in` Integer (compute=_compute_nbr_moves)
- `nbr_moves_out` Integer (compute=_compute_nbr_moves)
- `nbr_reordering_rules` Integer “Reordering Rules” (compute=_compute_nbr_reordering_rules)
- `reordering_min_qty` Float (compute=_compute_nbr_reordering_rules)
- `reordering_max_qty` Float (compute=_compute_nbr_reordering_rules)
- `putaway_rule_ids` One2many → `stock.putaway.rule`
- `storage_category_capacity_ids` One2many → `stock.storage.category.capacity`
- `show_on_hand_qty_status_button` Boolean (compute=_compute_show_qty_status_button)
- `show_forecasted_qty_status_button` Boolean (compute=_compute_show_qty_status_button)
- `show_qty_update_button` Boolean (compute=_compute_show_qty_update_button)
- `valid_ean` Boolean “Barcode is valid EAN” (compute=_compute_valid_ean)
- `lot_properties_definition` PropertiesDefinition “Lot Properties”

Public methods: `action_open_product_lot`, `action_open_quants`, `action_product_forecast_report`, `action_view_orderpoints`, `action_view_related_putaway_rules`, `action_view_routes`, `action_view_stock_move_lines`, `action_view_storage_category_capacity`, `fields_get`, `filter_has_routes`, `get_components`, `get_routes_actions`, `view_header_get`, `write`

Extension points: `_get_dates_info`, `_get_description`, `_get_domain_locations`, `_get_domain_locations_new`, `_get_only_qty_available`, `_get_picking_description`, `_get_quantity_in_progress`, `_get_rules_from_location`

## `product.template` (extends)

- `responsible_id` Many2one → `res.users` “Responsible” (company_dependent)
- `property_stock_production` Many2one → `stock.location` (company_dependent)
- `property_stock_inventory` Many2one → `stock.location` (company_dependent)
- `tracking` Selection “Tracking Method” (store, compute=_compute_tracking)
- `store_by` Selection “Tracking” (required, compute=_compute_store_by)
- `lot_sequence_id` Many2one → `ir.sequence`
- `serial_prefix_format` Char “Custom Lot/Serial” (compute=_compute_serial_prefix_format)
- `next_serial` Char (compute=_compute_next_serial)
- `description_picking` Text “Description on Picking”
- `description_pickingout` Text “Description on Delivery Orders”
- `description_pickingin` Text “Description on Receptions”
- `qty_available` Float “Quantity On Hand” (compute=_compute_quantities)
- `location_id` Many2one → `stock.location`
- `warehouse_id` Many2one → `stock.warehouse`
- `has_available_route_ids` Boolean “Routes can be selected on this product” (compute=_compute_has_available_route_ids)
- `route_ids` Many2many → `stock.route`
- `nbr_moves_in` Integer (compute=_compute_nbr_moves)
- `nbr_moves_out` Integer (compute=_compute_nbr_moves)
- `nbr_reordering_rules` Integer “Reordering Rules” (compute=_compute_nbr_reordering_rules)
- `reordering_min_qty` Float (compute=_compute_nbr_reordering_rules)
- `reordering_max_qty` Float (compute=_compute_nbr_reordering_rules)
- `route_from_categ_ids` Many2many “Category Routes” (related=categ_id.total_route_ids)
- `show_on_hand_qty_status_button` Boolean (compute=_compute_show_qty_status_button)
- `show_forecasted_qty_status_button` Boolean (compute=_compute_show_qty_status_button)

Public methods: `action_open_product_lot`, `action_open_quants`, `action_open_routes_diagram`, `action_product_tmpl_forecast_report`, `action_view_orderpoints`, `action_view_related_putaway_rules`, `action_view_stock_move_lines`, `action_view_storage_category_capacity`, `copy`, `create`, `write`

Extension points: `_get_action_view_related_putaway_rules`

## `product.category` (extends)

- `route_ids` Many2many → `stock.route`
- `removal_strategy_id` Many2one → `product.removal`
- `parent_route_ids` Many2many → `stock.route` “Parent Routes” (compute=_compute_parent_route_ids)
- `total_route_ids` Many2many → `stock.route` “Total routes” (readonly, compute=_compute_total_route_ids)
- `putaway_rule_ids` One2many → `stock.putaway.rule`
- `packaging_reserve_method` Selection “Reserve Packagings”
- `filter_for_stock_putaway_rule` Boolean “stock.putaway.rule”

## `uom.uom` (extends)

- `package_type_id` Many2one → `stock.package.type` “Package Type”
- `route_ids` Many2many “Routes” (related=package_type_id.route_ids)

Public methods: `write`

## `product.removal` (defines)

Removal Strategy

- `name` Char “Name” (required)
- `method` Char “Method” (required)

## `stock.putaway.rule` (defines)

Putaway Rule

- `product_id` Many2one → `product.product`
- `category_id` Many2one → `product.category`
- `location_in_id` Many2one → `stock.location` (required, index)
- `location_out_id` Many2one → `stock.location` (required)
- `sequence` Integer “Priority”
- `company_id` Many2one → `res.company` (required, index)
- `package_type_ids` Many2many → `stock.package.type` “Package Type”
- `storage_category_id` Many2one → `stock.storage.category` (store, compute=_compute_storage_category)
- `active` Boolean “Active”
- `sublocation` Selection

Public methods: `create`, `write`

Extension points: `_get_last_used_location`, `_get_last_used_search_domain`, `_get_putaway_location`

## `res.company` (extends)

- `internal_transit_location_id` Many2one → `stock.location`
- `scrap_location_id` Many2one → `stock.location` (compute=_compute_scrap_location_id)
- `default_stock_location_id` Many2one → `stock.location` (compute=_compute_default_stock_location_id)
- `stock_move_email_validation` Boolean “Email Confirmation picking”
- `stock_mail_confirmation_template_id` Many2one → `mail.template` “Email Template confirmation picking”
- `annual_inventory_month` Selection “Annual Inventory Month”
- `annual_inventory_day` Integer “Day of the month”
- `horizon_days` Integer “Replenishment Horizon” (required)
- `stock_text_confirmation` Boolean “Stock Text Confirmation”
- `stock_confirmation_type` Selection
- `picking_policy` Selection (required)

Public methods: `create`, `create_missing_inventory_loss_location`, `create_missing_production_location`, `create_missing_scrap_location`, `create_missing_scrap_sequence`, `create_missing_transit_location`, `create_missing_warehouse`

Extension points: `_create_inventory_loss_location`, `_create_per_company_locations`, `_create_per_company_picking_types`, `_create_per_company_rules`, `_create_per_company_sequences`, `_create_production_location`, `_create_scrap_location`, `_create_scrap_sequence`, `_create_transit_location`, `_get_text_validation`

## `res.config.settings` (extends)

- `module_product_expiry` Boolean “Expiration Dates”
- `group_stock_production_lot` Boolean “Lots & Serial Numbers”
- `group_stock_lot_print_gs1` Boolean “Print GS1 Barcodes for Lots & Serial Numbers”
- `group_lot_on_delivery_slip` Boolean “Display Lots & Serial Numbers on Delivery Slips”
- `group_stock_picking_batch` Boolean “Batch, Wave & Cluster Transfers”
- `group_stock_tracking_lot` Boolean “Packages”
- `group_stock_tracking_owner` Boolean “Consignment”
- `group_stock_adv_location` Boolean “Multi-Step Routes”
- `group_warning_stock` Boolean “Warnings for Stock”
- `group_stock_sign_delivery` Boolean “Signature”
- `module_stock_barcode` Boolean “Barcode Scanner”
- `module_stock_barcode_barcodelookup` Boolean “Stock Barcode Database”
- `stock_move_email_validation` Boolean (related=company_id.stock_move_email_validation)
- `module_stock_sms` Boolean “SMS Confirmation”
- `module_delivery` Boolean “Delivery Methods”
- `module_quality_control` Boolean “Quality”
- `module_quality_control_worksheet` Boolean “Quality Worksheet”
- `group_stock_multi_locations` Boolean “Storage Locations”
- `annual_inventory_month` Selection (related=company_id.annual_inventory_month)
- `annual_inventory_day` Integer (related=company_id.annual_inventory_day)
- `module_stock_dropshipping` Boolean “Dropshipping”
- `barcode_separator` Char “Separator”
- `module_stock_fleet` Boolean “Transport Management”
- `replenish_on_order` Boolean “Replenish on Order (MTO)” (compute=_compute_replenish_on_order)
- `stock_text_confirmation` Boolean “Stock Text Validation with stock move” (related=company_id.stock_text_confirmation)
- `stock_confirmation_type` Selection “Stock Text Validation type” (related=company_id.stock_confirmation_type)
- `horizon_days` Integer (related=company_id.horizon_days)
- `picking_policy` Selection (required, related=company_id.picking_policy)

Public methods: `action_view_delivery_methods`, `onchange_adv_location`, `onchange_module_product_barcodelookup`, `onchange_module_stock_barcode_barcodelookup`, `set_values`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.partner` (extends)

- `property_stock_customer` Many2one → `stock.location` “Customer Location” (company_dependent)
- `property_stock_supplier` Many2one → `stock.location` “Vendor Location” (company_dependent)
- `picking_warn_msg` Text “Message for Stock Picking”

Public methods: `action_view_stock_serial`, `write`

## `res.users` (extends)


Extension points: `_get_default_warehouse_id`

## `stock.location` (defines)

Inventory Location

- `name` Char “Location Name” (required)
- `complete_name` Char “Full Location Name” (store, compute=_compute_complete_name)
- `active` Boolean “Active”
- `usage` Selection “Location Type” (required, index)
- `location_id` Many2one → `stock.location` (index)
- `child_ids` One2many → `stock.location`
- `child_internal_location_ids` Many2many → `stock.location` “Internal locations among descendants” (compute=_compute_child_internal_location_ids)
- `parent_path` Char (index)
- `company_id` Many2one → `res.company` (index)
- `replenish_location` Boolean “Replenishments” (store, compute=_compute_replenish_location)
- `removal_strategy_id` Many2one → `product.removal`
- `putaway_rule_ids` One2many → `stock.putaway.rule`
- `barcode` Char “Barcode”
- `quant_ids` One2many → `stock.quant`
- `cyclic_inventory_frequency` Integer “Inventory Frequency”
- `last_inventory_date` Date “Last Inventory” (readonly)
- `next_inventory_date` Date “Next Expected” (store, compute=_compute_next_inventory_date)
- `warehouse_view_ids` One2many → `stock.warehouse` (readonly)
- `warehouse_id` Many2one → `stock.warehouse` (store, compute=_compute_warehouse_id)
- `storage_category_id` Many2one → `stock.storage.category` “Storage Category”
- `outgoing_move_line_ids` One2many → `stock.move.line`
- `incoming_move_line_ids` One2many → `stock.move.line`
- `net_weight` Float “Net Weight” (compute=_compute_weight)
- `forecast_weight` Float “Forecasted Weight” (compute=_compute_weight)
- `is_empty` Boolean “Is Empty” (compute=_compute_is_empty)

Public methods: `create`, `default_get`, `name_create`, `should_bypass_reservation`, `unlink`, `write`

Extension points: `_check_access_putaway`, `_check_can_be_used`, `_check_replenish_location`, `_check_scrap_location`, `_get_next_inventory_date`, `_get_putaway_strategy`, `_get_weight`

## `stock.route` (defines)

Inventory Route

- `name` Char “Route” (required)
- `active` Boolean “Active”
- `sequence` Integer “Sequence”
- `rule_ids` One2many → `stock.rule`
- `product_selectable` Boolean “Applicable on Product”
- `product_categ_selectable` Boolean “Applicable on Product Category”
- `warehouse_selectable` Boolean “Applicable on Warehouse”
- `package_type_selectable` Boolean “Applicable on Package Type”
- `supplied_wh_id` Many2one → `stock.warehouse`
- `supplier_wh_id` Many2one → `stock.warehouse`
- `company_id` Many2one → `res.company` (index)
- `product_ids` Many2many → `product.template`
- `categ_ids` Many2many → `product.category`
- `warehouse_domain_ids` One2many → `stock.warehouse` (compute=_compute_warehouses)
- `warehouse_ids` Many2many → `stock.warehouse`

Public methods: `write`

Extension points: `_check_company_consistency`, `_get_non_push_pull_rule_actions`, `_get_routes_with_no_warehouse`

## `stock.lot` (defines)

Lot/Serial

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Lot/Serial Number” (required, store, compute=_compute_name)
- `ref` Char “Internal Reference”
- `product_id` Many2one → `product.product` (required, index)
- `uom_id` Many2one → `uom.uom` (related=product_id.uom_id)
- `quant_ids` One2many → `stock.quant` (readonly)
- `product_qty` Float “On Hand Quantity” (compute=_product_qty)
- `note` Html “Description”
- `display_complete` Boolean (compute=_compute_display_complete)
- `company_id` Many2one → `res.company` (store, index, compute=_compute_company_id)
- `delivery_ids` Many2many → `stock.picking` “Transfers” (compute=_compute_delivery_ids)
- `delivery_count` Integer “Delivery order count” (compute=_compute_delivery_ids)
- `partner_ids` Many2many → `res.partner`
- `lot_properties` Properties “Properties”
- `location_id` Many2one → `stock.location` (store, compute=_compute_single_location)
- `is_scrap` Boolean “Is Scrapped” (compute=_compute_is_scrap)

Public methods: `action_lot_open_quants`, `action_lot_open_transfers`, `action_open_scrap_moves`, `action_scrap`, `copy_data`, `create`, `default_get`, `generate_lot_names`, `write`

Extension points: `_check_create`, `_check_unique_lot`, `_get_delivery_move_lines_by_lot`, `_get_next_serial`, `_get_outgoing_domain`

## `stock.move` (defines)

Stock Move

Inherits: `product.catalog.line.mixin`

- `sequence` Integer “Sequence”
- `priority` Selection (store, compute=_compute_priority)
- `date` Datetime “Date Scheduled” (required, index)
- `date_deadline` Datetime “Deadline” (readonly)
- `company_id` Many2one → `res.company` (required, index)
- `product_id` Many2one → `product.product` (required, index)
- `product_category_id` Many2one → `product.category` (related=product_id.categ_id)
- `never_product_template_attribute_value_ids` Many2many → `product.template.attribute.value` “Never attribute Values”
- `description_picking` Text “Description Of Picking” (compute=_compute_description_picking)
- `description_picking_manual` Text (readonly)
- `product_qty` Float “Demand in Product UoM” (store, compute=_compute_product_qty)
- `product_uom_qty` Float “Demand” (required)
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `uom_id` Many2one → `uom.uom` (required, store, compute=_compute_uom_id)
- `product_tmpl_id` Many2one → `product.template` (related=product_id.product_tmpl_id)
- `location_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_dest_id)
- `forecasted_location_id` Many2one → `stock.location` (store, index)
- `location_usage` Selection “Source Location Type” (related=location_id.usage)
- `location_dest_usage` Selection “Destination Location Type” (related=location_dest_id.usage)
- `partner_id` Many2one → `res.partner` (store, compute=_compute_partner_id)
- `move_dest_ids` Many2many → `stock.move`
- `move_orig_ids` Many2many → `stock.move`
- `picking_id` Many2one → `stock.picking` (index)
- `state` Selection “Status” (readonly, index)
- `picked` Boolean “Picked” (store, compute=_compute_picked)
- `price_unit` Float “Unit Price”
- `origin` Char “Source Document”
- `procure_method` Selection “Supply Method” (required)
- `is_scrap` Boolean (readonly)
- `procurement_values` Json
- `reference_ids` Many2many → `stock.reference` “References”
- `rule_id` Many2one → `stock.rule`
- `propagate_cancel` Boolean “Propagate cancel and split”
- `delay_alert_date` Datetime “Delay Alert Date” (store, compute=_compute_delay_alert_date)
- `picking_type_id` Many2one → `stock.picking.type` (store, compute=_compute_picking_type_id)
- `is_inventory` Boolean “Inventory”
- `inventory_name` Char (readonly)
- `move_line_ids` One2many → `stock.move.line`
- `package_ids` One2many → `stock.package` “Packages” (compute=_compute_package_ids)
- `origin_returned_move_id` Many2one → `stock.move` (index)
- `returned_move_ids` One2many → `stock.move`
- `availability` Float “Forecasted Quantity” (readonly, compute=_compute_product_availability)
- `restrict_partner_id` Many2one → `res.partner`
- `route_ids` Many2many → `stock.route`
- `warehouse_id` Many2one → `stock.warehouse`
- `has_tracking` Selection “Product with Tracking” (related=product_id.tracking)
- `has_lines_without_result_package` Boolean (compute=_compute_has_lines_without_result_package)
- `quantity` Float “Quantity” (store, compute=_compute_quantity)
- `quantity_product_uom` Float “Quantity in Product UoM” (store, compute=_compute_quantity_product_uom)
- `picking_code` Selection (readonly, related=picking_type_id.code)
- `show_details_visible` Boolean “Details Visible” (compute=_compute_show_details_visible)
- `is_storable` Boolean (related=product_id.is_storable)
- `additional` Boolean “Whether the move was added after the picking's confirmation”
- `is_locked` Boolean (readonly, compute=_compute_is_locked)
- `is_initial_demand_editable` Boolean “Is initial demand editable” (compute=_compute_is_initial_demand_editable)
- `is_date_editable` Boolean “Is Date Editable” (compute=_compute_is_date_editable)
- `is_quantity_done_editable` Boolean “Is quantity done editable” (compute=_compute_is_quantity_done_editable)
- `reference` Char “Reference” (store, compute=_compute_reference)
- `move_lines_count` Integer (compute=_compute_move_lines_count)
- `display_assign_serial` Boolean (compute=_compute_display_assign_serial)
- `display_import_lot` Boolean (compute=_compute_display_assign_serial)
- `next_serial` Char “First SN/Lot”
- `next_serial_count` Integer “Number of SN/Lots”
- `orderpoint_id` Many2one → `stock.warehouse.orderpoint` (index)
- `forecast_availability` Float “Forecast Availability” (compute=_compute_forecast_information)
- `forecast_expected_date` Datetime “Forecasted Expected date” (compute=_compute_forecast_information)
- `lot_ids` Many2many → `stock.lot` “Serial Numbers” (compute=_compute_lot_ids)
- `reservation_date` Date “Date to Reserve” (store, compute=_compute_reservation_date)
- `packaging_uom_id` Many2one → `uom.uom` (store, compute=_compute_packaging_uom_id)
- `packaging_uom_qty` Float “Packaging Quantity” (store, compute=_compute_packaging_uom_qty)
- `show_quant` Boolean “Show Quant” (compute=_compute_show_info)
- `show_lots_m2o` Boolean “Show lot_id” (compute=_compute_show_info)
- `show_lots_text` Boolean “Show lot_name” (compute=_compute_show_info)
- `scrap_reason_tag_ids` Many2many → `stock.scrap.reason.tag` “Scrap Reason”
- `should_replenish_scrapped` Boolean “Should Replenish”

Public methods: `action_add_packages`, `action_generate_lot_line_vals`, `action_open_label_layout`, `action_open_reference`, `action_print_reception_report`, `action_product_forecast_report`, `action_scrap`, `action_show_details`, `check_available_qty`, `create`, `default_get`, `split_lots`, `unlink`, `write`

Extension points: `_action_assign`, `_action_cancel`, `_action_confirm`, `_action_done`, `_action_replenish`, `_action_reset_to_draft`, `_action_reset_to_progress`, `_action_scrap`, `_action_synch_order`, `_check_quantity`, `_create_backorder`, `_create_lot_ids_from_move_line_vals`, `_get_available_move_lines`, `_get_available_move_lines_in`, `_get_available_move_lines_out`, `_get_available_quantity`, `_get_description`, `_get_forecast_availability_outgoing`, `_get_formating_options`, `_get_lang`, `_get_mto_procurement_date`, `_get_new_picking_values`, `_get_orderpoints_to_update`, `_get_partner_id`, `_get_picked_quantity`, `_get_picking_partner`, `_get_product_uom_field`, `_get_quantity_field`, `_get_relevant_state_among_moves`, `_get_report_description_picking`, `_get_source_document`, `_get_upstream_documents_and_responsibles`, `_post_process_created_moves`, `_prepare_merge_moves_distinct_fields`, `_prepare_merge_negative_moves_excluded_distinct_fields`, `_prepare_move_line_vals`, `_prepare_move_split_vals`, `_prepare_procurement_origin`, `_prepare_procurement_qty`, `_prepare_procurement_values`, `_prepare_scrap_move_vals`

## `stock.move.line` (defines)

Product Moves (Stock Move Line)

- `picking_id` Many2one → `stock.picking` (index)
- `batch_id` Many2one (related=picking_id.batch_id)
- `move_id` Many2one → `stock.move` (index)
- `company_id` Many2one → `res.company` “Company” (required, readonly, index)
- `product_id` Many2one → `product.product` (index)
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `uom_id` Many2one → `uom.uom` (required, store, compute=_compute_uom_id)
- `product_category_id` Many2one “Product Category” (related=product_id.categ_id)
- `quantity` Float “Quantity” (store, compute=_compute_quantity)
- `quantity_product_uom` Float “Quantity in Product UoM” (store, compute=_compute_quantity_product_uom)
- `picked` Boolean “Picked” (store, compute=_compute_picked)
- `package_id` Many2one → `stock.package`
- `lot_id` Many2one → `stock.lot` (index)
- `lot_name` Char “Lot/Serial Number Name”
- `result_package_id` Many2one → `stock.package`
- `result_package_dest_name` Char “Destination Package Name” (related=result_package_id.dest_complete_name)
- `package_history_id` Many2one → `stock.package.history` “Package History”
- `is_entire_pack` Boolean “Is added through entire package”
- `date` Datetime “Date” (store, related=move_id.date)
- `owner_id` Many2one → `res.partner`
- `location_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_dest_id)
- `location_usage` Selection “Source Location Type” (related=location_id.usage)
- `location_dest_usage` Selection “Destination Location Type” (related=location_dest_id.usage)
- `lots_visible` Boolean (compute=_compute_lots_visible)
- `picking_partner_id` Many2one (readonly, related=picking_id.partner_id)
- `move_partner_id` Many2one (readonly, related=move_id.partner_id)
- `picking_code` Selection (readonly, related=picking_type_id.code)
- `picking_type_id` Many2one → `stock.picking.type` (compute=_compute_picking_type_id)
- `picking_type_use_create_lots` Boolean (readonly, related=picking_type_id.use_create_lots)
- `picking_type_use_existing_lots` Boolean (readonly, related=picking_type_id.use_existing_lots)
- `state` Selection (store, related=move_id.state)
- `is_inventory` Boolean (related=move_id.is_inventory)
- `is_locked` Boolean (readonly, related=move_id.is_locked)
- `is_scrap` Boolean (readonly, related=move_id.is_scrap)
- `consume_line_ids` Many2many → `stock.move.line`
- `produce_line_ids` Many2many → `stock.move.line`
- `reference` Char (related=move_id.reference)
- `tracking` Selection (readonly, related=product_id.tracking)
- `origin` Char “Source” (related=move_id.origin)
- `description_picking` Text (related=move_id.description_picking)
- `quant_id` Many2one → `stock.quant`
- `picking_location_id` Many2one (related=picking_id.location_id)
- `picking_location_dest_id` Many2one (related=picking_id.location_dest_id)

Public methods: `action_open_add_to_wave`, `action_open_reference`, `action_put_in_pack`, `action_revert`, `action_send_recall_email`, `create`, `get_move_line_quant_match`, `unlink`, `write`

Extension points: `_action_done`, `_action_reset_to_progress`, `_check_destinations`, `_check_lot_product`, `_check_positive_quantity`, `_create_and_assign_production_lot`, `_get_aggregated_product_quantities`, `_get_aggregated_properties`, `_get_auto_wave_description`, `_get_default_dest_location`, `_get_lines_and_packages_to_pack`, `_get_lines_not_entire_pack`, `_get_linkable_moves`, `_get_lot_partner`, `_get_potential_existing_waves_extra_domain`, `_get_potential_new_waves_extra_domain`, `_get_putaway_additional_qty`, `_get_revert_inventory_move_values`, `_get_similar_move_lines`, `_post_put_in_pack_hook`, `_prepare_merge_distinct_fields`, `_prepare_new_lot_vals`, `_prepare_package_history_vals`, `_prepare_stock_move_vals`

## `stock.warehouse.orderpoint` (defines)

Minimum Inventory Rule

- `name` Char “Name” (required, readonly)
- `trigger` Selection “Trigger” (required)
- `active` Boolean “Active”
- `snoozed_until` Date “Snoozed”
- `warehouse_id` Many2one → `stock.warehouse` (required, store, index, compute=_compute_warehouse_id)
- `location_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_id)
- `product_tmpl_id` Many2one → `product.template` (related=product_id.product_tmpl_id)
- `product_id` Many2one → `product.product` (required, index)
- `product_category_id` Many2one → `product.category` (related=product_id.categ_id)
- `uom_id` Many2one → `uom.uom` (related=product_id.uom_id)
- `product_uom_name` Char “Product unit of measure label” (readonly, related=uom_id.display_name)
- `product_min_qty` Float “Min Quantity” (required)
- `product_max_qty` Float “Max Quantity” (required, store, compute=_compute_product_max_qty)
- `daily_demand` Float “Daily Demand” (required, store)
- `min_max_based_on` Selection “Based on” (required)
- `min_max_based_on_factor` Integer (required)
- `allowed_replenishment_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_replenishment_uom_ids)
- `replenishment_uom_id` Many2one → `uom.uom`
- `replenishment_uom_id_placeholder` Char (compute=_compute_replenishment_uom_id_placeholder)
- `company_id` Many2one → `res.company` (required, index)
- `allowed_location_ids` One2many → `stock.location` (compute=_compute_allowed_location_ids)
- `rule_ids` Many2many → `stock.rule` “Rules used” (compute=_compute_rules)
- `lead_horizon_date` Date (compute=_compute_lead_days)
- `lead_days` Float (compute=_compute_lead_days)
- `route_id` Many2one → `stock.route` “Route”
- `route_id_placeholder` Char (compute=_compute_route_id_placeholder)
- `effective_route_id` Many2one → `stock.route` (compute=_compute_effective_route_id)
- `qty_on_hand` Float “On Hand” (readonly, compute=_compute_qty)
- `qty_forecast` Float “Forecast” (readonly, compute=_compute_qty)
- `qty_to_order` Float “To Order” (compute=_compute_qty_to_order)
- `qty_to_order_computed` Float “To Order Computed” (store, compute=_compute_qty_to_order_computed)
- `qty_to_order_manual` Float “To Order Manual”
- `qty_to_order_to_max` Float “To Order to Reach Max” (compute=_compute_qty_to_order_to_max)
- `days_to_order` Float (compute=_compute_days_to_order)
- `unwanted_replenish` Boolean “Unwanted Replenish” (compute=_compute_unwanted_replenish)
- `show_supply_warning` Boolean (compute=_compute_show_supply_warning)
- `deadline_date` Date “Deadline” (readonly, store, compute=_compute_deadline_date)

Public methods: `action_open_orderpoints`, `action_product_forecast_report`, `action_remove_manual_qty_to_order`, `action_replenish`, `action_replenish_auto`, `action_stock_replenishment_info`, `create`, `get_horizon_days`, `write`

Extension points: `_check_min_max_qty`, `_get_daily_demand`, `_get_default_route`, `_get_default_rule`, `_get_lead_days_values`, `_get_multiple_rounded_qty`, `_get_orderpoint_action`, `_get_orderpoint_locations`, `_get_orderpoint_procurement_date`, `_get_orderpoint_products`, `_get_orderpoint_values`, `_get_period_of_time`, `_get_product_context`, `_get_qty_to_order`, `_get_replenishment_multiple_alternative`, `_get_replenishment_order_notification`, `_post_process_scheduler`, `_prepare_procurement_values`

## `stock.package` (defines)

Package

- `name` Char “Package Reference” (required)
- `complete_name` Char “Full Package Name” (store, compute=_compute_complete_name)
- `dest_complete_name` Char “Package Name At Destination” (compute=_compute_dest_complete_name)
- `quant_ids` One2many → `stock.quant` (readonly)
- `contained_quant_ids` One2many → `stock.quant` (compute=_compute_contained_quant_ids)
- `content_description` Char “Contents” (compute=_compute_content_description)
- `package_type_id` Many2one → `stock.package.type` (index)
- `location_id` Many2one → `stock.location` (store, index, compute=_compute_package_info)
- `location_dest_id` Many2one → `stock.location` (compute=_compute_location_dest_id)
- `company_id` Many2one → `res.company` (readonly, store, index, compute=_compute_package_info)
- `owner_id` Many2one → `res.partner` (readonly, compute=_compute_owner_id)
- `parent_package_id` Many2one → `stock.package`
- `child_package_ids` One2many → `stock.package` “Contained Packages”
- `all_children_package_ids` One2many → `stock.package` (compute=_compute_all_children_package_ids)
- `package_dest_id` Many2one → `stock.package`
- `outermost_package_id` Many2one → `stock.package` (compute=_compute_outermost_package_id)
- `child_package_dest_ids` One2many → `stock.package`
- `move_line_ids` One2many → `stock.move.line` (compute=_compute_move_line_ids)
- `picking_ids` Many2many → `stock.picking` “Transfers” (compute=_compute_picking_ids)
- `shipping_weight` Float “Shipping Weight”
- `valid_sscc` Boolean “Package name is valid SSCC” (compute=_compute_valid_sscc)
- `pack_date` Date “Pack Date”
- `parent_path` Char (index)
- `json_popover` Char “JSON data for popover widget” (compute=_compute_json_popover)

Public methods: `action_add_to_picking`, `action_put_in_pack`, `action_remove_package`, `action_view_picking`, `create`, `unpack`, `write`

Extension points: `_check_move_lines_map_quant`, `_get_all_children_package_dest_ids`, `_get_all_package_dest_ids`, `_get_package_vals`, `_get_weight`, `_post_put_in_pack_hook`

## `stock.package.history` (defines)

Stock Package History

- `company_id` Many2one → `res.company` (required)
- `location_id` Many2one → `stock.location`
- `location_dest_id` Many2one → `stock.location`
- `move_line_ids` One2many → `stock.move.line` “Move Lines” (required)
- `package_id` Many2one → `stock.package` (required, index)
- `package_name` Char “Package Name” (required)
- `package_type_id` Many2one → `stock.package.type` (related=package_id.package_type_id)
- `parent_orig_id` Many2one → `stock.package`
- `parent_orig_name` Char “Origin Container Name”
- `parent_dest_id` Many2one → `stock.package`
- `parent_dest_name` Char “Destination Container Name”
- `outermost_dest_id` Many2one → `stock.package`
- `picking_ids` Many2many → `stock.picking` “Transfers”

Public methods: `action_show_package`

Extension points: `_get_complete_dest_name_except_outermost`

## `stock.package.type` (defines)

Stock package type

- `name` Char “Package Type” (required)
- `sequence` Integer “Sequence”
- `sequence_id` Many2one → `ir.sequence`
- `sequence_code` Char “Sequence Prefix” (related=sequence_id.code)
- `height` Float “Height”
- `width` Float “Width”
- `packaging_length` Float “Length”
- `base_weight` Float “Weight”
- `max_weight` Float “Max Weight”
- `barcode` Char “Barcode”
- `weight_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_uom_name)
- `length_uom_name` Char “Length unit of measure label” (compute=_compute_length_uom_name)
- `company_id` Many2one → `res.company` (index)
- `package_use` Selection “Package Use” (required)
- `has_quants` Boolean “Has Contents” (compute=_compute_has_quants)
- `storage_category_capacity_ids` One2many → `stock.storage.category.capacity`
- `route_ids` Many2many → `stock.route` “Routes”

Public methods: `create`, `write`

Extension points: `_get_default_length_uom`, `_get_default_weight_uom`, `_get_next_name_by_sequence`

## `stock.picking` (defines)

Transfer

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Reference” (readonly)
- `origin` Char “Source Document”
- `note` Html “Notes”
- `backorder_id` Many2one → `stock.picking` (readonly)
- `backorder_ids` One2many → `stock.picking`
- `return_id` Many2one → `stock.picking` (readonly)
- `return_ids` One2many → `stock.picking`
- `return_count` Integer “# Returns” (compute=_compute_return_count)
- `move_type` Selection (required, store, compute=_compute_move_type)
- `state` Selection “Status” (readonly, store, index, compute=_compute_state)
- `reference_ids` Many2many → `stock.reference` “References” (readonly, related=move_ids.reference_ids)
- `priority` Selection “Priority”
- `scheduled_date` Datetime “Scheduled Date” (store, index, compute=_compute_scheduled_date)
- `date_deadline` Datetime “Deadline” (store, compute=_compute_date_deadline)
- `has_deadline_issue` Boolean “Is late” (store, compute=_compute_has_deadline_issue)
- `date_done` Datetime “Date of Transfer”
- `delay_alert_date` Datetime “Delay Alert Date” (compute=_compute_delay_alert_date)
- `json_popover` Char “JSON data for the popover widget” (compute=_compute_json_popover)
- `location_id` Many2one → `stock.location` (required, store, compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (required, store, compute=_compute_location_dest_id)
- `move_ids` One2many → `stock.move` “Stock Moves”
- `has_scrap_move` Boolean “Has Scrap Moves” (compute=_has_scrap_move)
- `picking_type_id` Many2one → `stock.picking.type` (required, index)
- `warehouse_address_id` Many2one → `res.partner` (related=picking_type_id.warehouse_id.partner_id)
- `picking_type_code` Selection (readonly, related=picking_type_id.code)
- `picking_type_entire_packs` Boolean (related=picking_type_id.show_entire_packs)
- `use_create_lots` Boolean (related=picking_type_id.use_create_lots)
- `use_existing_lots` Boolean (related=picking_type_id.use_existing_lots)
- `partner_id` Many2one → `res.partner`
- `company_id` Many2one → `res.company` “Company” (readonly, store, index, related=picking_type_id.company_id)
- `user_id` Many2one → `res.users`
- `move_line_ids` One2many → `stock.move.line`
- `packages_count` Integer “Packages Count” (compute=_compute_packages_count)
- `package_history_ids` Many2many → `stock.package.history` “Transfered Packages”
- `show_check_availability` Boolean (compute=_compute_show_check_availability)
- `show_allocation` Boolean (compute=_compute_show_allocation)
- `owner_id` Many2one → `res.partner`
- `printed` Boolean “Printed”
- `signature` Image “Signature”
- `is_signed` Boolean “Is Signed” (compute=_compute_is_signed)
- `is_locked` Boolean
- `is_date_editable` Boolean “Is Scheduled Date Editable” (compute=_compute_is_date_editable)
- `weight_bulk` Float “Bulk Weight” (compute=_compute_bulk_weight)
- `shipping_weight` Float “Weight for Shipping” (store, compute=_compute_shipping_weight)
- `shipping_volume` Float “Volume for Shipping” (compute=_compute_shipping_volume)
- `batch_id` Many2one → `stock.picking.batch` “Batch Transfer” (index)
- `batch_sequence` Integer “Sequence”
- `product_id` Many2one → `product.product` (readonly, related=move_ids.product_id)
- `lot_id` Many2one → `stock.lot` (readonly, related=move_line_ids.lot_id)
- `show_lots_text` Boolean (compute=_compute_show_lots_text)
- `has_tracking` Boolean (compute=_compute_has_tracking)
- `products_availability` Char “Product Availability” (compute=_compute_products_availability)
- `products_availability_state` Selection (compute=_compute_products_availability)
- `picking_properties` Properties “Properties”
- `show_next_pickings` Boolean (compute=_compute_show_next_pickings)
- `search_date_category` Selection “Date Category” (readonly)
- `partner_country_id` Many2one → `res.country` (related=partner_id.country_id)
- `picking_warning_text` Text “Picking Instructions” (compute=_compute_picking_warning_text)
- `show_return` Boolean “Show return button”
- `validate_button_style` Selection (compute=_compute_validate_button_style)

Public methods: `action_add_entire_packs`, `action_add_operations`, `action_assign`, `action_cancel`, `action_clear_return`, `action_confirm`, `action_detailed_operations`, `action_exchange`, `action_next_transfer`, `action_open_label_layout`, `action_open_label_type`, `action_picking_move_tree`, `action_put_in_pack`, `action_return`, `action_return_all`, `action_scrap`, `action_see_move_scrap`, `action_see_package_histories`, `action_see_packages`, `action_see_returns`, `action_split_transfer`, `action_toggle_is_locked`, `action_view_allocation_report`, `action_view_batch`, `assign_batch_user`, `button_validate`, `calculate_date_category`, `create`, `date_category_to_domain`, `do_print_picking`, `do_unreserve`, `get_action_click_graph`, `get_action_picking_tree_incoming`, `get_action_picking_tree_internal`, `get_action_picking_tree_outgoing`, `get_empty_list_help`, `should_print_delivery_address`, `unlink`, `write`

Extension points: `_action_done`, `_action_generate_backorder_wizard`, `_action_generate_zero_demand_wizard`, `_check_backorder`, `_check_entire_pack`, `_check_move_lines_map_quant_package`, `_create_backorder`, `_create_backorder_picking`, `_create_return`, `_get_action`, `_get_auto_batch_description`, `_get_autoprint_report_actions`, `_get_deliveryslip_report_title`, `_get_entire_pack_location_dest`, `_get_impacted_pickings`, `_get_lot_move_lines_for_sanity_check`, `_get_moves_to_backorder`, `_get_next_transfers`, `_get_packages_for_print`, `_get_possible_batches_domain`, `_get_possible_pickings_domain`, `_get_report_lang`, `_get_show_allocation`, `_get_without_quantities_error_message`, `_prepare_entire_pack_move_line_vals`, `_prepare_return_move_default_values`, `_prepare_return_picking_default_values`

## `stock.picking.batch` (defines)

Batch Transfer

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Batch Transfer” (required, readonly)
- `description` Char “Description”
- `user_id` Many2one → `res.users` “Responsible”
- `company_id` Many2one → `res.company` “Company” (required, readonly, index)
- `picking_ids` One2many → `stock.picking` “Transfers”
- `show_check_availability` Boolean “Show Reserve Button” (compute=_compute_show_check_availability)
- `show_allocation` Boolean “Show Allocation Button” (compute=_compute_show_allocation)
- `allowed_picking_ids` One2many → `stock.picking` (compute=_compute_allowed_picking_ids)
- `move_ids` One2many → `stock.move` “Stock moves” (compute=_compute_move_ids)
- `move_line_ids` One2many → `stock.move.line` “Stock move lines” (compute=_compute_move_line_ids)
- `state` Selection (required, readonly, store, index, compute=_compute_state)
- `priority` Selection “Priority”
- `picking_type_id` Many2one → `stock.picking.type` (index)
- `warehouse_id` Many2one → `stock.warehouse` (related=picking_type_id.warehouse_id)
- `picking_type_code` Selection (related=picking_type_id.code)
- `scheduled_date` Datetime “Scheduled Date” (store, compute=_compute_scheduled_date)
- `is_wave` Boolean “This batch is a wave”
- `show_lots_text` Boolean (compute=_compute_show_lots_text)
- `estimated_shipping_weight` Float “shipping_weight” (compute=_compute_estimated_shipping_capacity)
- `estimated_shipping_volume` Float “shipping_volume” (compute=_compute_estimated_shipping_capacity)
- `properties` Properties “Properties”

Public methods: `action_assign`, `action_batch_detailed_operations`, `action_cancel`, `action_confirm`, `action_done`, `action_merge`, `action_open_label_layout`, `action_print`, `action_put_in_pack`, `action_see_packages`, `action_view_allocation_report`, `create`, `fields_get`, `onchange_scheduled_date`, `write`

Extension points: `_get_merged_batch_vals`, `_prepare_name`

## `stock.picking.type` (defines)

Picking Type

- `name` Char “Operation Type” (required)
- `color` Integer “Color”
- `sequence` Integer “Sequence”
- `sequence_id` Many2one → `ir.sequence`
- `sequence_code` Char “Sequence Prefix” (related=sequence_id.prefix)
- `default_location_src_id` Many2one → `stock.location` (required, store, compute=_compute_default_location_src_id)
- `default_location_dest_id` Many2one → `stock.location` (required, store, compute=_compute_default_location_dest_id)
- `allocated_location_id` Many2one → `stock.location`
- `code` Selection (required)
- `return_picking_type_id` Many2one → `stock.picking.type`
- `show_entire_packs` Boolean “Move Entire Packages”
- `set_package_type` Boolean “Set Package Type”
- `warehouse_id` Many2one → `stock.warehouse` (store, compute=_compute_warehouse_id)
- `active` Boolean “Active”
- `use_create_lots` Boolean “Create New Lots/Serial Numbers” (store, compute=_compute_use_create_lots)
- `use_existing_lots` Boolean “Use Existing Lots/Serial Numbers” (store, compute=_compute_use_existing_lots)
- `print_label` Boolean “Generate Shipping Labels” (store, compute=_compute_print_label)
- `reservation_method` Selection (required)
- `reservation_days_before` Integer “Days”
- `reservation_days_before_priority` Integer “Days when starred”
- `auto_show_allocation_report` Boolean “Show Allocation”
- `auto_print_delivery_slip` Boolean “Auto Print Delivery Slip”
- `auto_print_return_slip` Boolean “Auto Print Return Slip”
- `auto_print_product_labels` Boolean “Auto Print Product Labels”
- `product_label_format` Selection “Product Label Format to auto-print”
- `auto_print_lot_labels` Boolean “Auto Print Lot/SN Labels”
- `lot_label_format` Selection “Lot Label Format to auto-print”
- `auto_print_reception_report` Boolean “Auto Print Reception Report”
- `auto_print_reception_report_labels` Boolean “Auto Print Reception Report Labels”
- `auto_print_packages` Boolean “Auto Print Packages”
- `auto_print_package_label` Boolean “Auto Print Package Label”
- `package_label_to_print` Selection
- `count_picking_draft` Integer (compute=_compute_picking_count)
- `count_picking_ready` Integer (compute=_compute_picking_count)
- `count_picking` Integer (compute=_compute_picking_count)
- `count_picking_waiting` Integer (compute=_compute_picking_count)
- `count_picking_late` Integer (compute=_compute_picking_count)
- `count_picking_backorders` Integer (compute=_compute_picking_count)
- `hide_reservation_method` Boolean (compute=_compute_hide_reservation_method)
- `barcode` Char “Barcode”
- `company_id` Many2one → `res.company` (required, index)
- `create_backorder` Selection (required)
- `open_button_style` Selection (compute=_compute_open_button_style)
- `show_picking_type` Boolean (compute=_compute_show_picking_type)
- `show_return_picking_type` Boolean (compute=_compute_show_return_picking_type)
- `picking_properties_definition` PropertiesDefinition “Picking Properties”
- `favorite_user_ids` Many2many → `res.users`
- `is_favorite` Boolean “Show Operation in Overview” (compute=_compute_is_favorite)
- `kanban_dashboard_graph` Text (compute=_compute_kanban_dashboard_graph)
- `move_type` Selection (required)
- `count_picking_batch` Integer (compute=_compute_picking_count)
- `auto_batch` Boolean “Automatic Batches”
- `batch_creation_type` Selection “Batch Creation” (compute=_compute_batch_creation_type)
- `batch_group_by_partner` Boolean “Contact”
- `batch_group_by_destination` Boolean “Destination Country”
- `batch_group_by_src_loc` Boolean “Group by Source Location”
- `batch_group_by_dest_loc` Boolean “Group by Destination Location”
- `wave_group_by_product` Boolean “Product”
- `wave_group_by_category` Boolean “Product Category”
- `wave_category_ids` Many2many → `product.category` “Wave Product Categories”
- `wave_group_by_location` Boolean “Location”
- `wave_location_ids` Many2many → `stock.location` “Wave Locations”
- `wave_group_by_date` Boolean “Group by Date”
- `wave_date_granularity` Selection “Date Precision”
- `batch_max_lines` Integer “Maximum lines”
- `batch_max_pickings` Integer “Maximum transfers”
- `batch_auto_confirm` Boolean “Auto-confirm”
- `batch_properties_definition` PropertiesDefinition “Batch Properties”

Public methods: `action_batch`, `action_detailed_moves`, `action_redirect_to_barcode_installation`, `copy_data`, `create`, `get_action_picking_tree_backorder`, `get_action_picking_tree_late`, `get_action_picking_tree_ready`, `get_action_picking_tree_waiting`, `get_action_picking_type_moves_analysis`, `get_stock_picking_action_picking_type`, `write`

Extension points: `_check_auto_batch_options`, `_get_action`, `_get_aggregated_records_by_date`, `_get_batch_and_wave_group_by_keys`, `_get_batch_group_by_keys`, `_get_code_report_name`, `_get_lot_label_format_selection`, `_get_product_label_format_options`, `_get_product_label_format_selection`, `_get_wave_group_by_keys`, `_prepare_graph_data`

## `stock.quant` (defines)

Quant

- `product_id` Many2one → `product.product` (required, index)
- `product_tmpl_id` Many2one → `product.template` “Product Template” (related=product_id.product_tmpl_id)
- `uom_id` Many2one → `uom.uom` (readonly, related=product_id.uom_id)
- `is_favorite` Boolean (related=product_tmpl_id.is_favorite)
- `company_id` Many2one “Company” (readonly, store, related=location_id.company_id)
- `location_id` Many2one → `stock.location` (required, index)
- `warehouse_id` Many2one → `stock.warehouse` (related=location_id.warehouse_id)
- `storage_category_id` Many2one (related=location_id.storage_category_id)
- `cyclic_inventory_frequency` Integer (related=location_id.cyclic_inventory_frequency)
- `lot_id` Many2one → `stock.lot` (index)
- `lot_properties` Properties (readonly, related=lot_id.lot_properties)
- `sn_duplicated` Boolean “Duplicated Serial Number” (compute=_compute_sn_duplicated)
- `package_id` Many2one → `stock.package` (index)
- `owner_id` Many2one → `res.partner`
- `quantity` Float “Quantity” (readonly)
- `reserved_quantity` Float “Reserved Quantity” (required, readonly)
- `available_quantity` Float “Available Quantity” (compute=_compute_available_quantity)
- `in_date` Datetime “Incoming Date” (required, readonly)
- `tracking` Selection (readonly, related=product_id.tracking)
- `on_hand` Boolean “On Hand”
- `product_categ_id` Many2one (related=product_tmpl_id.categ_id)
- `inventory_quantity` Float “Counted”
- `inventory_quantity_auto_apply` Float “Inventoried Quantity” (compute=_compute_inventory_quantity_auto_apply)
- `inventory_diff_quantity` Float “Difference” (readonly, store, compute=_compute_inventory_diff_quantity)
- `inventory_date` Date “Scheduled” (store, compute=_compute_inventory_date)
- `last_count_date` Date (compute=_compute_last_count_date)
- `inventory_quantity_set` Boolean (store, compute=_compute_inventory_quantity_set)
- `is_outdated` Boolean “Quantity has been moved since last count” (compute=_compute_is_outdated)
- `user_id` Many2one → `res.users`

Public methods: `action_apply_all`, `action_apply_inventory`, `action_clear_inventory_quantity`, `action_inventory_history`, `action_reset`, `action_set_inventory_quantity`, `action_set_inventory_quantity_zero`, `action_stock_quant_relocate`, `action_view_inventory`, `action_view_orderpoints`, `action_view_quants`, `action_view_stock_moves`, `check_location_id`, `check_lot_id`, `check_product_id`, `check_quantity`, `copy`, `create`, `get_aggregate_barcodes`, `get_import_templates`, `move_quants`, `name_create`, `write`

Extension points: `_check_serial_number`, `_get_available_quantity`, `_get_forbidden_fields_write`, `_get_gather_domain`, `_get_gs1_barcode`, `_get_inventory_fields_create`, `_get_inventory_fields_write`, `_get_inventory_move_values`, `_get_quants_action`, `_get_quants_by_products_locations`, `_get_removal_strategy`, `_get_removal_strategy_order`, `_get_reserve_quantity`

## `stock.reference` (defines)

Reference between stock documents

- `name` Char “Reference” (required, readonly)
- `move_ids` Many2many → `stock.move` “Stock Moves”
- `picking_ids` Many2many → `stock.picking` “Transfers” (readonly, compute=_compute_picking_ids)

## `stock.replenish.mixin` (defines)

Product Replenish Mixin

- `route_id` Many2one → `stock.route` “Preferred Route”
- `allowed_route_ids` Many2many → `stock.route` (compute=_compute_allowed_route_ids)

Extension points: `_get_allowed_route_domain`

## `stock.rule` (defines)

Stock Rule

- `name` Char “Name” (required)
- `active` Boolean “Active”
- `action` Selection “Action” (required, index)
- `sequence` Integer “Sequence”
- `company_id` Many2one → `res.company` (index)
- `location_dest_id` Many2one → `stock.location` (required, index)
- `location_src_id` Many2one → `stock.location` (index)
- `location_dest_from_rule` Boolean “Destination location origin from rule”
- `route_id` Many2one → `stock.route` (required, index)
- `route_company_id` Many2one “Route Company” (related=route_id.company_id)
- `procure_method` Selection “Supply Method” (required)
- `route_sequence` Integer “Route Sequence” (store, related=route_id.sequence)
- `picking_type_id` Many2one → `stock.picking.type` (required)
- `picking_type_code_domain` Json (compute=_compute_picking_type_code_domain)
- `delay` Integer “Lead Time”
- `partner_address_id` Many2one → `res.partner`
- `propagate_cancel` Boolean “Cancel Next Move”
- `propagate_carrier` Boolean “Propagation of carrier”
- `warehouse_id` Many2one → `stock.warehouse` (index)
- `auto` Selection “Automatic Move” (required)
- `rule_message` Html (compute=_compute_action_message)
- `push_domain` Char “Push Applicability”

Public methods: `default_get`, `run`, `run_scheduler`

Extension points: `_check_company_consistency`, `_check_intercomp_location`, `_create_mto_rule_if_not_exist`, `_get_custom_move_fields`, `_get_lead_days`, `_get_message_dict`, `_get_message_values`, `_get_moves_to_assign_domain`, `_get_orderpoint_domain`, `_get_push_new_date`, `_get_push_rule`, `_get_rule`, `_get_rule_domain`, `_get_scheduler_tasks_to_do`, `_get_stock_move_values`

## `stock.scrap.reason.tag` (defines)

Scrap Reason Tag

- `name` Char “Name” (required)
- `sequence` Integer
- `color` Integer “Color”

## `stock.storage.category` (defines)

Storage Category

- `name` Char “Storage Category” (required)
- `max_weight` Float “Max Weight”
- `capacity_ids` One2many → `stock.storage.category.capacity`
- `product_capacity_ids` One2many → `stock.storage.category.capacity` (compute=_compute_storage_capacity_ids)
- `package_capacity_ids` One2many → `stock.storage.category.capacity` (compute=_compute_storage_capacity_ids)
- `allow_new_product` Selection (required)
- `location_ids` One2many → `stock.location`
- `company_id` Many2one → `res.company`
- `weight_uom_name` Char “Weight unit” (compute=_compute_weight_uom_name)

## `stock.storage.category.capacity` (defines)

Storage Category Capacity

- `storage_category_id` Many2one → `stock.storage.category` (required, index)
- `product_id` Many2one → `product.product`
- `package_type_id` Many2one → `stock.package.type`
- `quantity` Float “Quantity” (required)
- `uom_id` Many2one (related=product_id.uom_id)
- `company_id` Many2one → `res.company` (related=storage_category_id.company_id)

## `stock.warehouse` (defines)

Warehouse

- `name` Char “Warehouse” (required)
- `active` Boolean “Active”
- `company_id` Many2one → `res.company` (required, readonly)
- `partner_id` Many2one → `res.partner`
- `view_location_id` Many2one → `stock.location` (required, index)
- `lot_stock_id` Many2one → `stock.location` (required)
- `code` Char “Short Name” (required)
- `route_ids` Many2many → `stock.route`
- `reception_steps` Selection (required)
- `delivery_steps` Selection (required)
- `wh_input_stock_loc_id` Many2one → `stock.location`
- `wh_qc_stock_loc_id` Many2one → `stock.location`
- `wh_output_stock_loc_id` Many2one → `stock.location`
- `wh_pack_stock_loc_id` Many2one → `stock.location`
- `mto_pull_id` Many2one → `stock.rule`
- `pick_type_id` Many2one → `stock.picking.type`
- `pack_type_id` Many2one → `stock.picking.type`
- `out_type_id` Many2one → `stock.picking.type`
- `in_type_id` Many2one → `stock.picking.type`
- `int_type_id` Many2one → `stock.picking.type`
- `qc_type_id` Many2one → `stock.picking.type`
- `store_type_id` Many2one → `stock.picking.type`
- `xdock_type_id` Many2one → `stock.picking.type`
- `reception_route_id` Many2one → `stock.route`
- `delivery_route_id` Many2one → `stock.route`
- `resupply_wh_ids` Many2many → `stock.warehouse`
- `resupply_route_ids` One2many → `stock.route`
- `sequence` Integer

Public methods: `action_open_internal_locations`, `action_view_all_routes`, `create`, `create_resupply_routes`, `get_current_warehouses`, `get_rules_dict`, `unlink`, `write`

Extension points: `_check_delivery_resupply`, `_check_multiwarehouse_group`, `_check_reception_resupply`, `_create_missing_locations`, `_create_or_update_global_routes_rules`, `_create_or_update_route`, `_create_or_update_sequences_and_picking_types`, `_get_all_routes`, `_get_global_route_rules_values`, `_get_input_output_locations`, `_get_inter_warehouse_route_values`, `_get_locations_values`, `_get_partner_locations`, `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_receive_routes_values`, `_get_receive_rules_dict`, `_get_route_name`, `_get_routes_values`, `_get_rule_values`, `_get_sequence_values`, `_get_supply_pull_rules_values`, `_get_transit_locations`

## `report.stock.quantity` (defines)

Stock Quantity Report

- `date` Date “Date” (readonly)
- `product_tmpl_id` Many2one → `product.template` (readonly)
- `product_id` Many2one → `product.product` “Product” (readonly)
- `state` Selection “State” (readonly)
- `product_qty` Float “Quantity” (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `warehouse_id` Many2one → `stock.warehouse` (readonly)

Public methods: `init`

Extension points: `_get_product_qty_col`

## `report.stock.report_stock_rule` (defines)

Stock rule report


Extension points: `_get_report_values`, `_get_route_colors`, `_get_routes`, `_get_rule_loc`

## `stock.allocation.report` (defines)

Stock Allocation Report


Public methods: `action_assign`, `action_assign_all`, `action_unassign`, `get_report_data`

Extension points: `_check_all_records_are_either_done_or_not`, `_get_doc_partner`, `_get_docs`, `_get_docs_type`, `_get_extra_domain`, `_get_moves`, `_get_out_move_values`, `_get_product_lines`, `_get_record_source`, `_get_report_values`

## `stock.forecasted_product_product` (defines)

Stock Replenishment Report


Public methods: `action_reserve_linked_picks`, `action_unreserve_linked_picks`, `get_report_values`

Extension points: `_get_product_leadtime`, `_get_product_quantities`, `_get_products`, `_get_quant_domain`, `_get_report_data`, `_get_report_header`, `_get_report_lines`, `_get_report_moves_fields`, `_get_reservation_data`, `_get_warehouse`, `_prepare_report_line`

## `stock.forecasted_product_template` (defines)

Stock Replenishment Report

Inherits: `stock.forecasted_product_product`


Public methods: `get_report_values`

## `stock.traceability.report` (defines)

Traceability Report


Public methods: `get_expanded_lines`, `get_lines`, `get_main_lines`, `get_pdf`, `get_pdf_lines`

Extension points: `_get_linked_move_lines`, `_get_location_names`, `_get_lot_lines`, `_get_move_lines`, `_get_picking_lines`, `_get_reference`, `_get_related_move_lines`

## `product.label.layout` (extends)

- `move_ids` Many2many → `stock.move`
- `print_packaging` Boolean “Print Packaging”
- `move_quantity` Selection “Quantity to print” (required)

Extension points: `_get_label_requests`, `_get_move_label_packaging`

## `product.replenish` (defines)

Product Replenish

Inherits: `stock.replenish.mixin`

- `product_id` Many2one → `product.product` “Product” (required)
- `product_tmpl_id` Many2one → `product.template` “Product Template” (required)
- `product_has_variants` Boolean “Has variants” (required)
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `uom_id` Many2one → `uom.uom` “Unity of measure” (required)
- `forecast_uom_id` Many2one (related=product_id.uom_id)
- `quantity` Float “Quantity” (required)
- `date_planned` Datetime “Scheduled Date” (required, store, compute=_compute_date_planned)
- `warehouse_id` Many2one → `stock.warehouse` “Warehouse” (required)
- `company_id` Many2one → `res.company`
- `forecasted_quantity` Float “Forecasted Quantity” (compute=_compute_forecasted_quantity)

Public methods: `default_get`, `launch_replenishment`

Extension points: `_get_date_planned`, `_get_record_to_notify`, `_get_replenishment_order_notification`, `_get_replenishment_order_notification_link`, `_get_route_domain`, `_prepare_run_values`

## `stock.add.to.wave` (defines)

Batch Transfer Line

- `wave_id` Many2one → `stock.picking.batch` “Batch Transfer”
- `picking_ids` Many2many → `stock.picking`
- `line_ids` Many2many → `stock.move.line`
- `mode` Selection
- `user_id` Many2one → `res.users` “Responsible”

Public methods: `attach_pickings`, `default_get`

## `stock.backorder.confirmation.line` (defines)

Backorder Confirmation Line

- `backorder_confirmation_id` Many2one → `stock.backorder.confirmation`
- `picking_id` Many2one → `stock.picking`
- `to_backorder` Boolean “To Backorder”

## `stock.backorder.confirmation` (defines)

Backorder Confirmation

- `pick_ids` Many2many → `stock.picking`
- `show_transfers` Boolean
- `backorder_confirmation_line_ids` One2many → `stock.backorder.confirmation.line` “Backorder Confirmation Lines”

Public methods: `default_get`, `process`, `process_cancel_backorder`

Extension points: `_check_less_quantities_than_expected`

## `stock.inventory.adjustment.name` (defines)

Inventory Adjustment Reference / Reason

- `quant_ids` Many2many → `stock.quant`
- `inventory_adjustment_name` Char “Inventory Reason”
- `counting_date` Datetime

Public methods: `action_apply`

Extension points: `_get_quants_context`

## `stock.inventory.conflict` (defines)

Conflict in Inventory

- `quant_ids` Many2many → `stock.quant` “Quants”
- `quant_to_fix_ids` Many2many → `stock.quant` “Conflicts”

Public methods: `action_keep_counted_quantity`, `action_keep_difference`

## `stock.inventory.warning` (defines)

Inventory Adjustment Warning

- `quant_ids` Many2many → `stock.quant`

Public methods: `action_reset`, `action_set`

## `picking.label.type` (defines)

Choose whether to print product or lot/sn labels

- `picking_ids` Many2many → `stock.picking`
- `label_type` Selection “Labels to print” (required)

Public methods: `process`

## `stock.location.label.layout` (defines)

Prepare Location Labels


Extension points: `_prepare_report_data_for_locations`

## `lot.label.layout` (defines)

Choose the sheet layout to print lot labels

- `lot_ids` Many2many → `stock.lot`
- `move_line_ids` Many2many → `stock.move.line`
- `custom_quantity` Integer
- `label_quantity` Selection “Quantity to print” (required)
- `print_format` Selection “Format” (required)

Public methods: `process`

Extension points: `_get_report_xml_ids`, `_prepare_label_values`, `_prepare_lot_gs1_barcode`, `_prepare_lot_gs1_barcode_extra_data`, `_prepare_lot_quantities`, `_prepare_report_data`

## `stock.orderpoint.snooze` (defines)

Snooze Orderpoint

- `orderpoint_ids` Many2many → `stock.warehouse.orderpoint`
- `predefined_date` Selection “Snooze for”
- `snoozed_until` Date “Snooze Date”

Public methods: `action_snooze`

## `stock.orderpoint.suggest` (defines)

Stock Orderpoint Min-Max Suggestion

- `orderpoint_ids` Many2many → `stock.warehouse.orderpoint`
- `based_on` Selection “Based on” (required)
- `percent_factor` Integer (required)

Public methods: `action_apply`

## `stock.package.destination` (defines)

Stock Package Destination

- `move_line_ids` Many2many → `stock.move.line` “Products” (required)
- `location_dest_id` Many2one → `stock.location` (required)
- `filtered_location` One2many → `stock.location` (compute=_compute_filtered_location)

Public methods: `action_done`

## `stock.package.label.layout` (defines)

Prepare Package Labels


Extension points: `_prepare_package_label_values`, `_prepare_report_data_for_packages`

## `stock.picking.to.batch` (defines)

Batch Transfer Line

- `batch_id` Many2one → `stock.picking.batch` “Batch Transfer”
- `mode` Selection
- `user_id` Many2one → `res.users` “Responsible”
- `is_create_draft` Boolean “Draft”
- `description` Char “Description”

Public methods: `attach_pickings`

## `stock.picking.type.label.layout` (defines)

Prepare Operation Type Labels


Extension points: `_prepare_report_data_for_picking_types`

## `stock.put.in.pack` (defines)

Put In Pack Wizard

- `location_dest_id` Many2one → `stock.location`
- `move_line_ids` Many2many → `stock.move.line` “Move lines”
- `package_ids` Many2many → `stock.package` “Packages”
- `package_type_id` Many2one → `stock.package.type` (store, compute=_compute_package_type_id)
- `result_package_id` Many2one → `stock.package` (store, compute=_compute_result_package_id)
- `origin_package_ids` Many2many → `stock.package` (compute=_compute_origin_package_ids)
- `package_capacity` Float “Package Size” (store, compute=_compute_package_capacity)
- `package_uom` Char “Unit” (compute=_compute_package_uom)
- `show_package_capacity` Boolean (compute=_compute_show_package_capacity)

Public methods: `action_put_in_pack`

Extension points: `_get_put_in_pack_context`

## `stock.quant.relocate` (defines)

Stock Quantity Relocation

- `quant_ids` Many2many → `stock.quant`
- `company_id` Many2one (related=quant_ids.company_id)
- `dest_location_id` Many2one → `stock.location`
- `dest_package_id_domain` Char (compute=_compute_dest_package_id_domain)
- `dest_package_id` Many2one → `stock.package` (store, compute=_compute_dest_package_id)
- `message` Text “Reason for relocation”
- `is_partial_package` Boolean (compute=_compute_is_partial_package)
- `partial_package_names` Char (compute=_compute_is_partial_package)
- `is_multi_location` Boolean (compute=_compute_is_multi_location)

Public methods: `action_relocate_quants`

## `stock.replenishment.info` (defines)

Stock supplier replenishment information

- `orderpoint_id` Many2one → `stock.warehouse.orderpoint`
- `product_id` Many2one → `product.product` (related=orderpoint_id.product_id)
- `product_uom_name` Char (related=orderpoint_id.product_uom_name)
- `product_min_qty` Float “Min” (required, related=orderpoint_id.product_min_qty)
- `product_max_qty` Float “Max” (required, related=orderpoint_id.product_max_qty)
- `daily_demand` Float “Demand is” (required, related=orderpoint_id.daily_demand)
- `min_coverage` Integer (compute=_compute_min_coverage)
- `replenish_frequency` Integer (compute=_compute_replenish_frequency)
- `qty_to_order` Float (related=orderpoint_id.qty_to_order)
- `json_lead_days` Char (compute=_compute_json_lead_days)
- `json_replenishment_graph` Char (compute=_compute_json_replenishment_graph)
- `based_on` Selection “Based on” (required)
- `percent_factor` Integer (required)
- `danger_level` Char (compute=_compute_danger_level)
- `warehouseinfo_ids` One2many (related=orderpoint_id.warehouse_id.resupply_route_ids)
- `wh_replenishment_option_ids` One2many → `stock.replenishment.option` (compute=_compute_wh_replenishment_options)

Public methods: `get_daily_demand`

Extension points: `_get_lead_days_and_description`, `_get_warning_days`

## `stock.replenishment.option` (defines)

Stock warehouse replenishment option

- `route_id` Many2one → `stock.route`
- `product_id` Many2one → `product.product`
- `replenishment_info_id` Many2one → `stock.replenishment.info`
- `location_id` Many2one → `stock.location` (related=warehouse_id.lot_stock_id)
- `warehouse_id` Many2one → `stock.warehouse` (related=route_id.supplier_wh_id)
- `uom` Char (related=product_id.uom_name)
- `qty_to_order` Float (related=replenishment_info_id.qty_to_order)
- `free_qty` Float (compute=_compute_free_qty)
- `lead_time` Char (compute=_compute_lead_time)
- `warning_message` Char (compute=_compute_warning_message)

Public methods: `order_all`, `order_avbl`, `select_route`

## `stock.request.count` (defines)

Stock Request an Inventory Count

- `inventory_date` Date “Scheduled at” (required)
- `user_id` Many2one → `res.users` “Assign to”
- `quant_ids` Many2many → `stock.quant`
- `show_expected_quantity` Boolean (compute=_compute_show_expected_quantity)

Public methods: `action_request_count`

Extension points: `_get_quants_to_count`, `_get_values_to_write`

## `stock.rules.report` (defines)

Stock Rules report

- `product_id` Many2one → `product.product` “Product” (required)
- `product_tmpl_id` Many2one → `product.template` “Product Template” (required)
- `warehouse_ids` Many2many → `stock.warehouse` “Warehouses” (required)
- `product_has_variants` Boolean “Has variants” (required)

Public methods: `default_get`, `print_report`

Extension points: `_prepare_report_data`

## `stock.warn.insufficient.qty` (defines)

Warn Insufficient Quantity

- `product_id` Many2one → `product.product` (required)
- `location_id` Many2one → `stock.location` (required)
- `quant_ids` Many2many → `stock.quant` (compute=_compute_quant_ids)
- `quantity` Float “Quantity” (required)
- `product_uom_name` Char “Unit” (required)

Public methods: `action_done`

Extension points: `_get_reference_document_company_id`

## `stock.warn.insufficient.qty.scrap` (defines)

Warn Insufficient Scrap Quantity

Inherits: `stock.warn.insufficient.qty`

- `scrap_move_id` Many2one → `stock.move`

Public methods: `action_cancel`, `action_done`

Extension points: `_get_reference_document_company_id`

## `stock.zero.demand.confirmation` (defines)

Zero Demand Confirmation

- `picking_ids` Many2many → `stock.picking`

Public methods: `process`, `process_without_zero_moves`
