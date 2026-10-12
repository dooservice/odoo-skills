# stock — Inventory

Depends on: product, barcodes_gs1_nomenclature, digest.

## `barcode.rule` (extends)

- `type` Selection

## `ir.actions.report` (extends)


Extension points: `_get_rendering_context`

## `product.product` (extends)

- `stock_quant_ids` One2many → `stock.quant`
- `stock_move_ids` One2many → `stock.move`
- `qty_available` Float “Quantity On Hand” (compute=_compute_quantities)
- `virtual_available` Float “Forecasted Quantity” (compute=_compute_quantities)
- `free_qty` Float “Free To Use Quantity ” (compute=_compute_quantities)
- `incoming_qty` Float “Incoming” (compute=_compute_quantities)
- `outgoing_qty` Float “Outgoing” (compute=_compute_quantities)
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
- `valid_ean` Boolean “Barcode is valid EAN” (compute=_compute_valid_ean)
- `lot_properties_definition` PropertiesDefinition “Lot Properties”

Public methods: `action_open_product_lot`, `action_open_quants`, `action_product_forecast_report`, `action_update_quantity_on_hand`, `action_view_orderpoints`, `action_view_related_putaway_rules`, `action_view_routes`, `action_view_stock_move_lines`, `action_view_storage_category_capacity`, `fields_get`, `filter_has_routes`, `get_components`, `view_header_get`, `write`

Extension points: `_get_dates_info`, `_get_description`, `_get_domain_locations`, `_get_domain_locations_new`, `_get_only_qty_available`, `_get_quantity_in_progress`, `_get_rules_from_location`

## `product.template` (extends)

- `responsible_id` Many2one → `res.users` “Responsible” (company_dependent)
- `detailed_type` Selection
- `type` Selection
- `property_stock_production` Many2one → `stock.location` (company_dependent)
- `property_stock_inventory` Many2one → `stock.location` (company_dependent)
- `sale_delay` Integer “Customer Lead Time”
- `tracking` Selection “Tracking” (required, store, compute=_compute_tracking)
- `description_picking` Text “Description on Picking”
- `description_pickingout` Text “Description on Delivery Orders”
- `description_pickingin` Text “Description on Receptions”
- `qty_available` Float “Quantity On Hand” (compute=_compute_quantities)
- `virtual_available` Float “Forecasted Quantity” (compute=_compute_quantities)
- `incoming_qty` Float “Incoming” (compute=_compute_quantities)
- `outgoing_qty` Float “Outgoing” (compute=_compute_quantities)
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

Public methods: `action_open_product_lot`, `action_open_quants`, `action_open_routes_diagram`, `action_product_tmpl_forecast_report`, `action_update_quantity_on_hand`, `action_view_orderpoints`, `action_view_related_putaway_rules`, `action_view_stock_move_lines`, `action_view_storage_category_capacity`, `copy`, `write`

Extension points: `_get_action_view_related_putaway_rules`

## `product.category` (extends)

- `route_ids` Many2many → `stock.route`
- `removal_strategy_id` Many2one → `product.removal`
- `total_route_ids` Many2many → `stock.route` “Total routes” (readonly, compute=_compute_total_route_ids)
- `putaway_rule_ids` One2many → `stock.putaway.rule`
- `packaging_reserve_method` Selection “Reserve Packagings”
- `filter_for_stock_putaway_rule` Boolean “stock.putaway.rule”

## `product.packaging` (extends)

- `package_type_id` Many2one → `stock.package.type`
- `route_ids` Many2many → `stock.route`

## `uom.uom` (extends)


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
- `storage_category_id` Many2one → `stock.storage.category`
- `active` Boolean “Active”

Public methods: `create`, `write`

Extension points: `_get_putaway_location`

## `res.company` (extends)

- `internal_transit_location_id` Many2one → `stock.location`
- `stock_move_email_validation` Boolean “Email Confirmation picking”
- `stock_mail_confirmation_template_id` Many2one → `mail.template` “Email Template confirmation picking”
- `annual_inventory_month` Selection “Annual Inventory Month”
- `annual_inventory_day` Integer “Day of the month”

Public methods: `create`, `create_missing_inventory_loss_location`, `create_missing_production_location`, `create_missing_scrap_location`, `create_missing_scrap_sequence`, `create_missing_transit_location`, `create_missing_warehouse`

Extension points: `_create_inventory_loss_location`, `_create_per_company_locations`, `_create_per_company_picking_types`, `_create_per_company_rules`, `_create_per_company_sequences`, `_create_production_location`, `_create_scrap_location`, `_create_scrap_sequence`, `_create_transit_location`

## `res.config.settings` (extends)

- `module_product_expiry` Boolean “Expiration Dates”
- `group_stock_production_lot` Boolean “Lots & Serial Numbers”
- `group_stock_lot_print_gs1` Boolean “Print GS1 Barcodes for Lots & Serial Numbers”
- `group_lot_on_delivery_slip` Boolean “Display Lots & Serial Numbers on Delivery Slips”
- `group_stock_tracking_lot` Boolean “Packages”
- `group_stock_tracking_owner` Boolean “Consignment”
- `group_stock_adv_location` Boolean “Multi-Step Routes”
- `group_warning_stock` Boolean “Warnings for Stock”
- `group_stock_sign_delivery` Boolean “Signature”
- `module_stock_picking_batch` Boolean “Batch Transfers”
- `group_stock_picking_wave` Boolean “Wave Transfers”
- `module_stock_barcode` Boolean “Barcode Scanner”
- `stock_move_email_validation` Boolean (related=company_id.stock_move_email_validation)
- `module_stock_sms` Boolean “SMS Confirmation”
- `module_delivery` Boolean “Delivery Methods”
- `module_delivery_dhl` Boolean “DHL Express Connector”
- `module_delivery_fedex` Boolean “FedEx Connector”
- `module_delivery_ups` Boolean “UPS Connector”
- `module_delivery_usps` Boolean “USPS Connector”
- `module_delivery_bpost` Boolean “bpost Connector”
- `module_delivery_easypost` Boolean “Easypost Connector”
- `module_delivery_sendcloud` Boolean “Sendcloud Connector”
- `module_delivery_shiprocket` Boolean “Shiprocket Connector”
- `module_quality_control` Boolean “Quality”
- `module_quality_control_worksheet` Boolean “Quality Worksheet”
- `group_stock_multi_locations` Boolean “Storage Locations”
- `group_stock_storage_categories` Boolean “Storage Categories”
- `annual_inventory_month` Selection (related=company_id.annual_inventory_month)
- `annual_inventory_day` Integer (related=company_id.annual_inventory_day)
- `group_stock_reception_report` Boolean “Reception Report”
- `module_stock_dropshipping` Boolean “Dropshipping”

Public methods: `onchange_adv_location`, `set_values`

## `res.partner` (extends)

- `property_stock_customer` Many2one → `stock.location` “Customer Location” (company_dependent)
- `property_stock_supplier` Many2one → `stock.location` “Vendor Location” (company_dependent)
- `picking_warn` Selection
- `picking_warn_msg` Text “Message for Stock Picking”

## `res.users` (extends)


Extension points: `_get_default_warehouse_id`

## `stock.location` (defines)

Inventory Locations

- `name` Char “Location Name” (required)
- `complete_name` Char “Full Location Name” (store, compute=_compute_complete_name)
- `active` Boolean “Active”
- `usage` Selection “Location Type” (required, index)
- `location_id` Many2one → `stock.location` (index)
- `child_ids` One2many → `stock.location`
- `child_internal_location_ids` Many2many → `stock.location` “Internal locations among descendants” (compute=_compute_child_internal_location_ids)
- `comment` Html “Additional Information”
- `posx` Integer “Corridor (X)”
- `posy` Integer “Shelves (Y)”
- `posz` Integer “Height (Z)”
- `parent_path` Char (index)
- `company_id` Many2one → `res.company` (index)
- `scrap_location` Boolean “Is a Scrap Location?”
- `return_location` Boolean “Is a Return Location?”
- `replenish_location` Boolean “Replenish Location” (store, compute=_compute_replenish_location)
- `removal_strategy_id` Many2one → `product.removal`
- `putaway_rule_ids` One2many → `stock.putaway.rule`
- `barcode` Char “Barcode”
- `quant_ids` One2many → `stock.quant`
- `cyclic_inventory_frequency` Integer “Inventory Frequency (Days)”
- `last_inventory_date` Date “Last Effective Inventory” (readonly)
- `next_inventory_date` Date “Next Expected Inventory” (store, compute=_compute_next_inventory_date)
- `warehouse_view_ids` One2many → `stock.warehouse` (readonly)
- `warehouse_id` Many2one → `stock.warehouse` (store, compute=_compute_warehouse_id)
- `storage_category_id` Many2one → `stock.storage.category` “Storage Category”
- `outgoing_move_line_ids` One2many → `stock.move.line`
- `incoming_move_line_ids` One2many → `stock.move.line`
- `net_weight` Float “Net Weight” (compute=_compute_weight)
- `forecast_weight` Float “Forecasted Weight” (compute=_compute_weight)

Public methods: `copy`, `create`, `default_get`, `name_create`, `should_bypass_reservation`, `write`

Extension points: `_check_access_putaway`, `_check_can_be_used`, `_check_replenish_location`, `_check_scrap_location`, `_get_next_inventory_date`, `_get_putaway_strategy`, `_get_weight`

## `stock.route` (defines)

Inventory Routes

- `name` Char “Route” (required)
- `active` Boolean “Active”
- `sequence` Integer “Sequence”
- `rule_ids` One2many → `stock.rule`
- `product_selectable` Boolean “Applicable on Product”
- `product_categ_selectable` Boolean “Applicable on Product Category”
- `warehouse_selectable` Boolean “Applicable on Warehouse”
- `packaging_selectable` Boolean “Applicable on Packaging”
- `supplied_wh_id` Many2one → `stock.warehouse`
- `supplier_wh_id` Many2one → `stock.warehouse`
- `company_id` Many2one → `res.company` (index)
- `product_ids` Many2many → `product.template`
- `categ_ids` Many2many → `product.category`
- `packaging_ids` Many2many → `product.packaging`
- `warehouse_domain_ids` One2many → `stock.warehouse` (compute=_compute_warehouses)
- `warehouse_ids` Many2many → `stock.warehouse`

Public methods: `copy`, `toggle_active`

Extension points: `_check_company_consistency`

## `stock.lot` (defines)

Lot/Serial

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Lot/Serial Number” (required)
- `ref` Char “Internal Reference”
- `product_id` Many2one → `product.product` (required, index)
- `product_uom_id` Many2one → `uom.uom` (store, related=product_id.uom_id)
- `quant_ids` One2many → `stock.quant` (readonly)
- `product_qty` Float “On Hand Quantity” (compute=_product_qty)
- `note` Html “Description”
- `display_complete` Boolean (compute=_compute_display_complete)
- `company_id` Many2one → `res.company` (required, index)
- `delivery_ids` Many2many → `stock.picking` “Transfers” (compute=_compute_delivery_ids)
- `delivery_count` Integer “Delivery order count” (compute=_compute_delivery_ids)
- `last_delivery_partner_id` Many2one → `res.partner` (compute=_compute_last_delivery_partner_id)
- `lot_properties` Properties “Properties”
- `location_id` Many2one → `stock.location` (store, compute=_compute_single_location)

Public methods: `action_lot_open_quants`, `action_lot_open_transfers`, `copy`, `create`, `generate_lot_names`, `write`

Extension points: `_check_create`, `_check_unique_lot`, `_get_next_serial`, `_get_outgoing_domain`

## `stock.move` (defines)

Stock Move

- `name` Char “Description” (required)
- `sequence` Integer “Sequence”
- `priority` Selection (store, compute=_compute_priority)
- `date` Datetime “Date Scheduled” (required, index)
- `date_deadline` Datetime “Deadline” (readonly)
- `company_id` Many2one → `res.company` (required, index)
- `product_id` Many2one → `product.product` (required, index)
- `description_picking` Text “Description of Picking”
- `product_qty` Float “Real Quantity” (store, compute=_compute_product_qty)
- `product_uom_qty` Float “Demand” (required)
- `product_uom` Many2one → `uom.uom` (required, store, compute=_compute_product_uom)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `product_tmpl_id` Many2one → `product.template` (related=product_id.product_tmpl_id)
- `location_id` Many2one → `stock.location` (required, index)
- `location_dest_id` Many2one → `stock.location` (required, index)
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
- `scrapped` Boolean “Scrapped” (readonly, store, related=location_dest_id.scrap_location)
- `scrap_id` Many2one → `stock.scrap` (readonly)
- `group_id` Many2one → `procurement.group` (index)
- `rule_id` Many2one → `stock.rule`
- `propagate_cancel` Boolean “Propagate cancel and split”
- `delay_alert_date` Datetime “Delay Alert Date” (store, compute=_compute_delay_alert_date)
- `picking_type_id` Many2one → `stock.picking.type` (store, compute=_compute_picking_type_id)
- `is_inventory` Boolean “Inventory”
- `move_line_ids` One2many → `stock.move.line`
- `origin_returned_move_id` Many2one → `stock.move` (index)
- `returned_move_ids` One2many → `stock.move`
- `availability` Float “Forecasted Quantity” (readonly, compute=_compute_product_availability)
- `restrict_partner_id` Many2one → `res.partner`
- `route_ids` Many2many → `stock.route`
- `warehouse_id` Many2one → `stock.warehouse`
- `has_tracking` Selection “Product with Tracking” (related=product_id.tracking)
- `quantity` Float “Quantity” (store, compute=_compute_quantity)
- `show_operations` Boolean (related=picking_id.picking_type_id.show_operations)
- `picking_code` Selection (readonly, related=picking_id.picking_type_id.code)
- `show_details_visible` Boolean “Details Visible” (compute=_compute_show_details_visible)
- `product_type` Selection (readonly, related=product_id.detailed_type)
- `additional` Boolean “Whether the move was added after the picking's confirmation”
- `is_locked` Boolean (readonly, compute=_compute_is_locked)
- `is_initial_demand_editable` Boolean “Is initial demand editable” (compute=_compute_is_initial_demand_editable)
- `is_quantity_done_editable` Boolean “Is quantity done editable” (compute=_compute_is_quantity_done_editable)
- `reference` Char “Reference” (store, compute=_compute_reference)
- `move_lines_count` Integer (compute=_compute_move_lines_count)
- `package_level_id` Many2one → `stock.package_level`
- `picking_type_entire_packs` Boolean (readonly, related=picking_type_id.show_entire_packs)
- `display_assign_serial` Boolean (compute=_compute_display_assign_serial)
- `display_import_lot` Boolean (compute=_compute_display_assign_serial)
- `next_serial` Char “First SN”
- `next_serial_count` Integer “Number of SN”
- `orderpoint_id` Many2one → `stock.warehouse.orderpoint` (index)
- `forecast_availability` Float “Forecast Availability” (compute=_compute_forecast_information)
- `forecast_expected_date` Datetime “Forecasted Expected date” (compute=_compute_forecast_information)
- `lot_ids` Many2many → `stock.lot` “Serial Numbers” (compute=_compute_lot_ids)
- `reservation_date` Date “Date to Reserve” (store, compute=_compute_reservation_date)
- `product_packaging_id` Many2one → `product.packaging`
- `product_packaging_qty` Float “Reserved Packaging Quantity” (compute=_compute_product_packaging_qty)
- `product_packaging_quantity` Float “Done Packaging Quantity” (compute=_compute_product_packaging_quantity)
- `show_reserved` Boolean (compute=_compute_show_reserved)
- `show_quant` Boolean “Show Quant” (compute=_compute_show_info)
- `show_lots_m2o` Boolean “Show lot_id” (compute=_compute_show_info)
- `show_lots_text` Boolean “Show lot_name” (compute=_compute_show_info)

Public methods: `action_assign_serial`, `action_generate_lot_line_vals`, `action_open_reference`, `action_product_forecast_report`, `action_show_details`, `create`, `default_get`, `init`, `split_lots`, `unlink`, `write`

Extension points: `_action_assign`, `_action_cancel`, `_action_confirm`, `_action_done`, `_check_quantity`, `_check_unlink_move_dest`, `_check_uom`, `_create_extra_move`, `_create_lot_ids_from_move_line_vals`, `_get_available_move_lines`, `_get_available_move_lines_in`, `_get_available_move_lines_out`, `_get_available_quantity`, `_get_forecast_availability_outgoing`, `_get_formating_options`, `_get_lang`, `_get_moves_to_propagate_date_deadline`, `_get_mto_procurement_date`, `_get_new_picking_values`, `_get_picked_quantity`, `_get_relevant_state_among_moves`, `_get_source_document`, `_get_upstream_documents_and_responsibles`, `_post_process_created_moves`, `_prepare_extra_move_vals`, `_prepare_merge_moves_distinct_fields`, `_prepare_merge_negative_moves_excluded_distinct_fields`, `_prepare_move_line_vals`, `_prepare_move_split_vals`, `_prepare_procurement_origin`, `_prepare_procurement_values`

## `stock.move.line` (defines)

Product Moves (Stock Move Line)

- `picking_id` Many2one → `stock.picking` (index)
- `move_id` Many2one → `stock.move` (index)
- `company_id` Many2one → `res.company` “Company” (required, readonly, index)
- `product_id` Many2one → `product.product` (index)
- `product_uom_id` Many2one → `uom.uom` (required, store, compute=_compute_product_uom_id)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `product_category_name` Char “Product Category” (store, related=product_id.categ_id.complete_name)
- `quantity` Float “Quantity” (store, compute=_compute_quantity)
- `quantity_product_uom` Float “Quantity in Product UoM” (store, compute=_compute_quantity_product_uom)
- `picked` Boolean “Picked” (store, compute=_compute_picked)
- `package_id` Many2one → `stock.quant.package`
- `package_level_id` Many2one → `stock.package_level`
- `lot_id` Many2one → `stock.lot`
- `lot_name` Char “Lot/Serial Number Name”
- `result_package_id` Many2one → `stock.quant.package`
- `date` Datetime “Date” (required)
- `owner_id` Many2one → `res.partner`
- `location_id` Many2one → `stock.location` (required, store, compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (required, store, compute=_compute_location_id)
- `location_usage` Selection “Source Location Type” (related=location_id.usage)
- `location_dest_usage` Selection “Destination Location Type” (related=location_dest_id.usage)
- `lots_visible` Boolean (compute=_compute_lots_visible)
- `picking_partner_id` Many2one (readonly, related=picking_id.partner_id)
- `picking_code` Selection (readonly, related=picking_type_id.code)
- `picking_type_id` Many2one → `stock.picking.type` (compute=_compute_picking_type_id)
- `picking_type_use_create_lots` Boolean (readonly, related=picking_type_id.use_create_lots)
- `picking_type_use_existing_lots` Boolean (readonly, related=picking_type_id.use_existing_lots)
- `picking_type_entire_packs` Boolean (readonly, related=picking_id.picking_type_id.show_entire_packs)
- `state` Selection (store, related=move_id.state)
- `is_inventory` Boolean (related=move_id.is_inventory)
- `is_locked` Boolean (readonly, related=move_id.is_locked)
- `consume_line_ids` Many2many → `stock.move.line`
- `produce_line_ids` Many2many → `stock.move.line`
- `reference` Char (store, related=move_id.reference)
- `tracking` Selection (readonly, related=product_id.tracking)
- `origin` Char “Source” (related=move_id.origin)
- `description_picking` Text “Description picking”
- `quant_id` Many2one → `stock.quant`
- `product_packaging_qty` Float “Reserved Packaging Quantity” (compute=_compute_product_packaging_qty)
- `picking_location_id` Many2one (related=picking_id.location_id)
- `picking_location_dest_id` Many2one (related=picking_id.location_dest_id)

Public methods: `action_open_reference`, `action_put_in_pack`, `action_revert_inventory`, `create`, `get_move_line_quant_match`, `init`, `unlink`, `write`

Extension points: `_action_done`, `_check_lot_product`, `_check_positive_quantity`, `_create_and_assign_production_lot`, `_get_aggregated_product_quantities`, `_get_aggregated_properties`, `_get_default_dest_location`, `_get_linkable_moves`, `_get_putaway_additional_qty`, `_get_revert_inventory_move_values`, `_get_similar_move_lines`, `_prepare_new_lot_vals`, `_prepare_stock_move_vals`

## `stock.warehouse.orderpoint` (defines)

Minimum Inventory Rule

- `name` Char “Name” (required, readonly)
- `trigger` Selection “Trigger” (required)
- `active` Boolean “Active”
- `snoozed_until` Date “Snoozed”
- `warehouse_id` Many2one → `stock.warehouse` (required, store, index, compute=_compute_warehouse_id)
- `location_id` Many2one → `stock.location` (required, store, index, compute=_compute_location_id)
- `product_tmpl_id` Many2one → `product.template` (related=product_id.product_tmpl_id)
- `product_id` Many2one → `product.product` (required)
- `product_category_id` Many2one → `product.category` (store, related=product_id.categ_id)
- `product_uom` Many2one → `uom.uom` (related=product_id.uom_id)
- `product_uom_name` Char “Product unit of measure label” (readonly, related=product_uom.display_name)
- `product_min_qty` Float “Min Quantity” (required)
- `product_max_qty` Float “Max Quantity” (required)
- `qty_multiple` Float “Multiple Quantity” (required)
- `group_id` Many2one → `procurement.group`
- `company_id` Many2one → `res.company` (required, index)
- `allowed_location_ids` One2many → `stock.location` (compute=_compute_allowed_location_ids)
- `rule_ids` Many2many → `stock.rule` “Rules used” (compute=_compute_rules)
- `lead_days_date` Date (compute=_compute_lead_days)
- `route_id` Many2one → `stock.route` “Route”
- `qty_on_hand` Float “On Hand” (readonly, compute=_compute_qty)
- `qty_forecast` Float “Forecast” (readonly, compute=_compute_qty)
- `qty_to_order` Float “To Order” (store, compute=_compute_qty_to_order)
- `days_to_order` Float (compute=_compute_days_to_order)
- `visibility_days` Float (compute=_compute_visibility_days)
- `unwanted_replenish` Boolean “Unwanted Replenish” (compute=_compute_unwanted_replenish)

Public methods: `action_open_orderpoints`, `action_product_forecast_report`, `action_replenish`, `action_replenish_auto`, `action_stock_replenishment_info`, `create`, `write`

Extension points: `_check_product_uom`, `_get_lead_days_values`, `_get_orderpoint_action`, `_get_orderpoint_locations`, `_get_orderpoint_procurement_date`, `_get_orderpoint_products`, `_get_orderpoint_values`, `_get_product_context`, `_get_qty_multiple_to_order`, `_get_replenishment_order_notification`, `_post_process_scheduler`, `_prepare_procurement_values`

## `stock.package_level` (defines)

Stock Package Level

- `package_id` Many2one → `stock.quant.package` (required)
- `picking_id` Many2one → `stock.picking`
- `move_ids` One2many → `stock.move`
- `move_line_ids` One2many → `stock.move.line`
- `location_id` Many2one → `stock.location` (compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (store, compute=_compute_location_dest_id)
- `is_done` Boolean “Done” (compute=_compute_is_done)
- `state` Selection “State” (compute=_compute_state)
- `is_fresh_package` Boolean (compute=_compute_fresh_pack)
- `picking_type_code` Selection (related=picking_id.picking_type_code)
- `show_lots_m2o` Boolean (compute=_compute_show_lot)
- `show_lots_text` Boolean (compute=_compute_show_lot)
- `company_id` Many2one → `res.company` (required, index)

Public methods: `action_show_package_details`, `create`, `unlink`, `write`

Extension points: `_check_move_lines_map_quant_package`

## `stock.package.type` (defines)

Stock package type

- `name` Char “Package Type” (required)
- `sequence` Integer “Sequence”
- `height` Float “Height”
- `width` Float “Width”
- `packaging_length` Float “Length”
- `base_weight` Float “Weight”
- `max_weight` Float “Max Weight”
- `barcode` Char “Barcode”
- `weight_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_uom_name)
- `length_uom_name` Char “Length unit of measure label” (compute=_compute_length_uom_name)
- `company_id` Many2one → `res.company` (index)
- `storage_category_capacity_ids` One2many → `stock.storage.category.capacity`

Public methods: `copy`

Extension points: `_get_default_length_uom`, `_get_default_weight_uom`

## `stock.picking.type` (defines)

Picking Type

- `name` Char “Operation Type” (required)
- `color` Integer “Color”
- `sequence` Integer “Sequence”
- `sequence_id` Many2one → `ir.sequence`
- `sequence_code` Char “Sequence Prefix” (required)
- `default_location_src_id` Many2one → `stock.location` (store, compute=_compute_default_location_src_id)
- `default_location_dest_id` Many2one → `stock.location` (store, compute=_compute_default_location_dest_id)
- `default_location_return_id` Many2one → `stock.location`
- `code` Selection (required)
- `return_picking_type_id` Many2one → `stock.picking.type`
- `show_entire_packs` Boolean “Move Entire Packages”
- `warehouse_id` Many2one → `stock.warehouse` (store, compute=_compute_warehouse_id)
- `active` Boolean “Active”
- `use_create_lots` Boolean “Create New Lots/Serial Numbers” (store, compute=_compute_use_create_lots)
- `use_existing_lots` Boolean “Use Existing Lots/Serial Numbers” (store, compute=_compute_use_existing_lots)
- `print_label` Boolean “Print Label” (store, compute=_compute_print_label)
- `show_operations` Boolean “Show Detailed Operations”
- `show_reserved` Boolean “Pre-fill Detailed Operations” (store, compute=_compute_show_reserved)
- `reservation_method` Selection (required)
- `reservation_days_before` Integer “Days”
- `reservation_days_before_priority` Integer “Days when starred”
- `auto_show_reception_report` Boolean “Show Reception Report at Validation”
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
- `show_picking_type` Boolean (compute=_compute_show_picking_type)
- `picking_properties_definition` PropertiesDefinition “Picking Properties”

Public methods: `copy`, `create`, `get_action_picking_tree_backorder`, `get_action_picking_tree_late`, `get_action_picking_tree_ready`, `get_action_picking_tree_waiting`, `get_action_picking_type_operations`, `get_stock_picking_action_picking_type`, `write`

Extension points: `_check_default_location`, `_get_action`

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
- `move_type` Selection (required)
- `state` Selection “Status” (readonly, store, index, compute=_compute_state)
- `group_id` Many2one → `procurement.group` (readonly, store, related=move_ids.group_id)
- `priority` Selection “Priority”
- `scheduled_date` Datetime “Scheduled Date” (store, index, compute=_compute_scheduled_date)
- `date_deadline` Datetime “Deadline” (store, compute=_compute_date_deadline)
- `has_deadline_issue` Boolean “Is late” (store, compute=_compute_has_deadline_issue)
- `date` Datetime “Creation Date”
- `date_done` Datetime “Date of Transfer” (readonly)
- `delay_alert_date` Datetime “Delay Alert Date” (compute=_compute_delay_alert_date)
- `json_popover` Char “JSON data for the popover widget” (compute=_compute_json_popover)
- `location_id` Many2one → `stock.location` (required, store, compute=_compute_location_id)
- `location_dest_id` Many2one → `stock.location` (required, store, compute=_compute_location_id)
- `move_ids` One2many → `stock.move` “Stock Moves”
- `move_ids_without_package` One2many → `stock.move` “Stock move”
- `has_scrap_move` Boolean “Has Scrap Moves” (compute=_has_scrap_move)
- `picking_type_id` Many2one → `stock.picking.type` (required, index)
- `picking_type_code` Selection (readonly, related=picking_type_id.code)
- `picking_type_entire_packs` Boolean (related=picking_type_id.show_entire_packs)
- `use_create_lots` Boolean (related=picking_type_id.use_create_lots)
- `use_existing_lots` Boolean (related=picking_type_id.use_existing_lots)
- `hide_picking_type` Boolean (compute=_compute_hide_picking_type)
- `partner_id` Many2one → `res.partner`
- `company_id` Many2one → `res.company` “Company” (readonly, store, index, related=picking_type_id.company_id)
- `user_id` Many2one → `res.users`
- `move_line_ids` One2many → `stock.move.line`
- `move_line_ids_without_package` One2many → `stock.move.line`
- `move_line_exist` Boolean “Has Pack Operations” (compute=_compute_move_line_exist)
- `has_packages` Boolean “Has Packages” (compute=_compute_has_packages)
- `show_check_availability` Boolean (compute=_compute_show_check_availability)
- `show_allocation` Boolean (compute=_compute_show_allocation)
- `owner_id` Many2one → `res.partner`
- `printed` Boolean “Printed”
- `signature` Image “Signature”
- `is_signed` Boolean “Is Signed” (compute=_compute_is_signed)
- `is_locked` Boolean
- `product_id` Many2one → `product.product` (readonly, related=move_ids.product_id)
- `lot_id` Many2one → `stock.lot` (readonly, related=move_line_ids.lot_id)
- `show_operations` Boolean (related=picking_type_id.show_operations)
- `show_reserved` Boolean (related=picking_type_id.show_reserved)
- `show_lots_text` Boolean (compute=_compute_show_lots_text)
- `has_tracking` Boolean (compute=_compute_has_tracking)
- `package_level_ids` One2many → `stock.package_level`
- `package_level_ids_details` One2many → `stock.package_level`
- `products_availability` Char “Product Availability” (compute=_compute_products_availability)
- `products_availability_state` Selection (compute=_compute_products_availability)
- `show_set_qty_button` Boolean (compute=_compute_show_qty_button)
- `show_clear_qty_button` Boolean (compute=_compute_show_qty_button)
- `picking_properties` Properties “Properties”

Public methods: `action_assign`, `action_cancel`, `action_confirm`, `action_detailed_operations`, `action_open_label_layout`, `action_open_label_type`, `action_picking_move_tree`, `action_put_in_pack`, `action_see_move_scrap`, `action_see_packages`, `action_see_returns`, `action_toggle_is_locked`, `action_view_reception_report`, `button_scrap`, `button_validate`, `create`, `do_print_picking`, `do_unreserve`, `should_print_delivery_address`, `unlink`, `write`

Extension points: `_action_done`, `_action_generate_backorder_wizard`, `_check_backorder`, `_check_destinations`, `_check_entire_pack`, `_check_move_lines_map_quant_package`, `_create_backorder`, `_create_backorder_picking`, `_get_autoprint_report_actions`, `_get_entire_pack_location_dest`, `_get_impacted_pickings`, `_get_lot_move_lines_for_sanity_check`, `_get_moves_to_backorder`, `_get_report_lang`, `_get_show_allocation`, `_get_without_quantities_error_message`, `_post_put_in_pack_hook`

## `stock.quant` (defines)

Quants

- `product_id` Many2one → `product.product` (required, index)
- `product_tmpl_id` Many2one → `product.template` “Product Template” (related=product_id.product_tmpl_id)
- `product_uom_id` Many2one → `uom.uom` (readonly, related=product_id.uom_id)
- `priority` Selection (related=product_tmpl_id.priority)
- `company_id` Many2one “Company” (readonly, store, related=location_id.company_id)
- `location_id` Many2one → `stock.location` (required, index)
- `warehouse_id` Many2one → `stock.warehouse` (related=location_id.warehouse_id)
- `storage_category_id` Many2one (store, related=location_id.storage_category_id)
- `cyclic_inventory_frequency` Integer (related=location_id.cyclic_inventory_frequency)
- `lot_id` Many2one → `stock.lot` (index)
- `lot_properties` Properties (readonly, related=lot_id.lot_properties)
- `sn_duplicated` Boolean “Duplicated Serial Number” (compute=_compute_sn_duplicated)
- `package_id` Many2one → `stock.quant.package` (index)
- `owner_id` Many2one → `res.partner`
- `quantity` Float “Quantity” (readonly)
- `reserved_quantity` Float “Reserved Quantity” (required, readonly)
- `available_quantity` Float “Available Quantity” (compute=_compute_available_quantity)
- `in_date` Datetime “Incoming Date” (required, readonly)
- `tracking` Selection (readonly, related=product_id.tracking)
- `on_hand` Boolean “On Hand”
- `product_categ_id` Many2one (related=product_tmpl_id.categ_id)
- `inventory_quantity` Float “Counted Quantity”
- `inventory_quantity_auto_apply` Float “Inventoried Quantity” (compute=_compute_inventory_quantity_auto_apply)
- `inventory_diff_quantity` Float “Difference” (readonly, store, compute=_compute_inventory_diff_quantity)
- `inventory_date` Date “Scheduled Date” (store, compute=_compute_inventory_date)
- `last_count_date` Date (compute=_compute_last_count_date)
- `inventory_quantity_set` Boolean (store, compute=_compute_inventory_quantity_set)
- `is_outdated` Boolean “Quantity has been moved since last count” (compute=_compute_is_outdated)
- `user_id` Many2one → `res.users`

Public methods: `action_apply_inventory`, `action_clear_inventory_quantity`, `action_inventory_at_date`, `action_inventory_history`, `action_reset`, `action_set_inventory_quantity`, `action_set_inventory_quantity_zero`, `action_stock_quant_relocate`, `action_view_inventory`, `action_view_orderpoints`, `action_view_quants`, `action_view_stock_moves`, `action_warning_duplicated_sn`, `check_location_id`, `check_lot_id`, `check_product_id`, `check_quantity`, `copy`, `create`, `get_import_templates`, `move_quants`, `name_create`, `read_group`, `write`

Extension points: `_check_serial_number`, `_get_available_quantity`, `_get_forbidden_fields_write`, `_get_gather_domain`, `_get_inventory_fields_create`, `_get_inventory_fields_write`, `_get_inventory_move_values`, `_get_quants_action`, `_get_quants_by_products_locations`, `_get_quants_cache_by_products_locations`, `_get_removal_strategy`, `_get_removal_strategy_domain_order`, `_get_removal_strategy_sort_key`, `_get_reserve_quantity`

## `stock.quant.package` (defines)

Packages

- `name` Char “Package Reference” (required)
- `quant_ids` One2many → `stock.quant` (readonly)
- `package_type_id` Many2one → `stock.package.type` (index)
- `location_id` Many2one → `stock.location` (readonly, store, index, compute=_compute_package_info)
- `company_id` Many2one → `res.company` (readonly, store, index, compute=_compute_package_info)
- `owner_id` Many2one → `res.partner` (readonly, compute=_compute_owner_id)
- `package_use` Selection “Package Use” (required)
- `valid_sscc` Boolean “Package name is valid SSCC” (compute=_compute_valid_sscc)
- `pack_date` Date “Pack Date”

Public methods: `action_view_picking`, `unpack`

Extension points: `_check_move_lines_map_quant`

## `stock.rule` (defines)

Stock Rule

- `name` Char “Name” (required)
- `active` Boolean “Active”
- `group_propagation_option` Selection “Propagation of Procurement Group”
- `group_id` Many2one → `procurement.group`
- `action` Selection “Action” (required, index)
- `sequence` Integer “Sequence”
- `company_id` Many2one → `res.company` (index)
- `location_dest_id` Many2one → `stock.location` (required, index)
- `location_src_id` Many2one → `stock.location` (index)
- `route_id` Many2one → `stock.route` (required, index)
- `route_company_id` Many2one “Route Company” (related=route_id.company_id)
- `procure_method` Selection “Supply Method” (required)
- `route_sequence` Integer “Route Sequence” (store, related=route_id.sequence)
- `picking_type_id` Many2one → `stock.picking.type` (required)
- `picking_type_code_domain` Char (compute=_compute_picking_type_code_domain)
- `delay` Integer “Lead Time”
- `partner_address_id` Many2one → `res.partner`
- `propagate_cancel` Boolean “Cancel Next Move”
- `propagate_carrier` Boolean “Propagation of carrier”
- `warehouse_id` Many2one → `stock.warehouse` (index)
- `propagate_warehouse_id` Many2one → `stock.warehouse`
- `auto` Selection “Automatic Move” (required)
- `rule_message` Html (compute=_compute_action_message)

Public methods: `copy`, `default_get`

Extension points: `_check_company_consistency`, `_get_custom_move_fields`, `_get_lead_days`, `_get_message_dict`, `_get_message_values`, `_get_stock_move_values`

## `procurement.group` (defines)

Procurement Group

- `partner_id` Many2one → `res.partner`
- `name` Char “Reference” (required)
- `move_type` Selection “Delivery Type” (required)
- `stock_move_ids` One2many → `stock.move` “Related Stock Moves”

Public methods: `run`, `run_scheduler`

Extension points: `_get_moves_to_assign_domain`, `_get_orderpoint_domain`, `_get_rule`, `_get_rule_domain`

## `stock.scrap` (defines)

Scrap

Inherits: `mail.thread`

- `name` Char “Reference” (required, readonly)
- `company_id` Many2one → `res.company` “Company” (required)
- `origin` Char “Source Document”
- `product_id` Many2one → `product.product` (required)
- `product_uom_id` Many2one → `uom.uom` (required, store, compute=_compute_product_uom_id)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `tracking` Selection “Product Tracking” (readonly, related=product_id.tracking)
- `lot_id` Many2one → `stock.lot`
- `package_id` Many2one → `stock.quant.package`
- `owner_id` Many2one → `res.partner`
- `move_ids` One2many → `stock.move`
- `picking_id` Many2one → `stock.picking`
- `location_id` Many2one → `stock.location` (required, store, compute=_compute_location_id)
- `scrap_location_id` Many2one → `stock.location` (required, store, compute=_compute_scrap_location_id)
- `scrap_qty` Float “Quantity” (required, store, compute=_compute_scrap_qty)
- `state` Selection “Status” (readonly)
- `date_done` Datetime “Date” (readonly)
- `should_replenish` Boolean “Replenish Quantities”

Public methods: `action_get_stock_move_lines`, `action_get_stock_picking`, `action_validate`, `check_available_qty`, `do_replenish`, `do_scrap`

Extension points: `_prepare_move_values`

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

Public methods: `copy`

## `stock.storage.category.capacity` (defines)

Storage Category Capacity

- `storage_category_id` Many2one → `stock.storage.category` (required, index)
- `product_id` Many2one → `product.product`
- `package_type_id` Many2one → `stock.package.type`
- `quantity` Float “Quantity” (required)
- `product_uom_id` Many2one (related=product_id.uom_id)
- `company_id` Many2one → `res.company` (related=storage_category_id.company_id)

## `stock.warehouse` (defines)

Warehouse

- `name` Char “Warehouse” (required)
- `active` Boolean “Active”
- `company_id` Many2one → `res.company` (required, readonly)
- `partner_id` Many2one → `res.partner`
- `view_location_id` Many2one → `stock.location` (required)
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
- `crossdock_route_id` Many2one → `stock.route`
- `reception_route_id` Many2one → `stock.route`
- `delivery_route_id` Many2one → `stock.route`
- `resupply_wh_ids` Many2many → `stock.warehouse`
- `resupply_route_ids` One2many → `stock.route`
- `sequence` Integer

Public methods: `action_view_all_routes`, `copy`, `create`, `create_resupply_routes`, `get_current_warehouses`, `get_rules_dict`, `unlink`, `write`

Extension points: `_check_delivery_resupply`, `_check_multiwarehouse_group`, `_check_reception_resupply`, `_create_missing_locations`, `_create_or_update_global_routes_rules`, `_create_or_update_route`, `_create_or_update_sequences_and_picking_types`, `_get_all_routes`, `_get_global_route_rules_values`, `_get_input_output_locations`, `_get_inter_warehouse_route_values`, `_get_locations_values`, `_get_partner_locations`, `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_receive_routes_values`, `_get_receive_rules_dict`, `_get_route_name`, `_get_routes_values`, `_get_rule_values`, `_get_sequence_values`, `_get_supply_pull_rules_values`, `_get_transit_locations`, `_get_warehouse_id_from_context`

## `product.product` (extends)


## `stock.warehouse` (extends)


## `stock.storage.category` (extends)


## `stock.location` (extends)


## `stock.putaway.rule` (extends)


## `stock.warehouse.orderpoint` (extends)


## `stock.quant` (extends)


## `stock.picking.type` (extends)


## `stock.picking` (extends)


## `stock.move` (extends)


## `report.stock.label_product_product_view` (defines)

Product Label Report


Extension points: `_get_report_values`

## `report.stock.label_lot_template_view` (defines)

Lot Label Report


Extension points: `_get_report_values`

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

## `report.stock.report_reception` (defines)

Stock Reception Report


Public methods: `action_assign`, `action_unassign`, `get_report_data`

Extension points: `_action_assign`, `_action_unassign`, `_get_doc_model`, `_get_doc_types`, `_get_docs`, `_get_extra_domain`, `_get_formatted_scheduled_date`, `_get_moves`, `_get_report_values`, `_prepare_report_line`

## `report.stock.report_stock_rule` (defines)

Stock rule report


Extension points: `_get_report_values`, `_get_route_colors`, `_get_routes`, `_get_rule_loc`

## `stock.forecasted_product_product` (defines)

Stock Replenishment Report


Public methods: `action_reserve_linked_picks`, `action_unreserve_linked_picks`, `get_report_values`

Extension points: `_get_report_data`, `_get_report_header`, `_get_report_lines`, `_get_report_moves_fields`, `_get_reservation_data`, `_prepare_report_line`

## `stock.forecasted_product_template` (defines)

Stock Replenishment Report

Inherits: `stock.forecasted_product_product`


Public methods: `get_report_values`

## `stock.traceability.report` (defines)

Traceability Report


Public methods: `get_lines`, `get_main_lines`, `get_pdf`, `get_pdf_lines`

Extension points: `_get_linked_move_lines`, `_get_main_lines`, `_get_move_lines`, `_get_reference`, `_get_usage`

## `product.label.layout` (extends)

- `move_ids` Many2many → `stock.move`
- `move_quantity` Selection “Quantity to print” (required)
- `print_format` Selection

Extension points: `_prepare_report_data`

## `product.replenish` (defines)

Product Replenish

- `product_id` Many2one → `product.product` “Product” (required)
- `product_tmpl_id` Many2one → `product.template` “Product Template” (required)
- `product_has_variants` Boolean “Has variants” (required)
- `product_uom_category_id` Many2one → `uom.category` (required, readonly, related=product_id.uom_id.category_id)
- `product_uom_id` Many2one → `uom.uom` “Unity of measure” (required)
- `forecast_uom_id` Many2one (related=product_id.uom_id)
- `quantity` Float “Quantity” (required)
- `date_planned` Datetime “Scheduled Date” (required, store, compute=_compute_date_planned)
- `warehouse_id` Many2one → `stock.warehouse` “Warehouse” (required)
- `route_id` Many2one → `stock.route` “Preferred Route”
- `company_id` Many2one → `res.company`
- `forecasted_quantity` Float “Forecasted Quantity” (compute=_compute_forecasted_quantity)
- `allowed_route_ids` Many2many → `stock.route` (compute=_compute_allowed_route_ids)

Public methods: `default_get`, `launch_replenishment`

Extension points: `_get_allowed_route_domain`, `_get_date_planned`, `_get_record_to_notify`, `_get_replenishment_order_notification`, `_get_replenishment_order_notification_link`, `_get_route_domain`, `_prepare_orderpoint_values`, `_prepare_run_values`

## `stock.assign.serial` (defines)

Stock Assign Serial Numbers

- `product_id` Many2one → `product.product` (related=move_id.product_id)
- `move_id` Many2one → `stock.move`
- `next_serial_number` Char “First SN” (required)
- `next_serial_count` Integer “Number of SN” (required)

Public methods: `generate_serial_numbers`

Extension points: `_check_next_serial_count`

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

## `stock.change.product.qty` (defines)

Change Product Quantity

- `product_id` Many2one → `product.product` (required)
- `product_tmpl_id` Many2one → `product.template` (required)
- `product_variant_count` Integer “Variant Count” (related=product_tmpl_id.product_variant_count)
- `new_quantity` Float “New Quantity on Hand” (required)
- `product_uom_id` Many2one (related=product_tmpl_id.uom_id)

Public methods: `change_product_qty`, `check_new_quantity`

## `stock.inventory.adjustment.name` (defines)

Inventory Adjustment Reference / Reason

- `quant_ids` Many2many → `stock.quant`
- `inventory_adjustment_name` Char “Inventory Reason”

Public methods: `action_apply`

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

## `lot.label.layout` (defines)

Choose the sheet layout to print lot labels

- `move_line_ids` Many2many → `stock.move.line`
- `label_quantity` Selection “Quantity to print” (required)
- `print_format` Selection “Format” (required)

Public methods: `process`

## `stock.orderpoint.snooze` (defines)

Snooze Orderpoint

- `orderpoint_ids` Many2many → `stock.warehouse.orderpoint`
- `predefined_date` Selection “Snooze for”
- `snoozed_until` Date “Snooze Date”

Public methods: `action_snooze`

## `stock.package.destination` (defines)

Stock Package Destination

- `picking_id` Many2one → `stock.picking` (required)
- `move_line_ids` Many2many → `stock.move.line` (required, compute=_compute_move_line_ids)
- `location_dest_id` Many2one → `stock.location` (required)
- `filtered_location` One2many → `stock.location` (compute=_filter_location)

Public methods: `action_done`

## `stock.return.picking.line` (defines)

Return Picking Line

- `product_id` Many2one → `product.product` “Product” (required)
- `quantity` Float “Quantity” (required)
- `uom_id` Many2one → `uom.uom` “Unit of Measure” (related=product_id.uom_id)
- `wizard_id` Many2one → `stock.return.picking` “Wizard”
- `move_id` Many2one → `stock.move`

## `stock.return.picking` (defines)

Return Picking

- `picking_id` Many2one → `stock.picking`
- `product_return_moves` One2many → `stock.return.picking.line` (store, compute=_compute_moves_locations)
- `move_dest_exists` Boolean “Chained Move Exists” (store, compute=_compute_moves_locations)
- `original_location_id` Many2one → `stock.location` (store, compute=_compute_moves_locations)
- `parent_location_id` Many2one → `stock.location` (store, compute=_compute_moves_locations)
- `company_id` Many2one (related=picking_id.company_id)
- `location_id` Many2one → `stock.location` (store, compute=_compute_moves_locations)

Public methods: `create_returns`, `default_get`

Extension points: `_create_returns`, `_prepare_move_default_values`, `_prepare_picking_default_values`, `_prepare_stock_return_picking_line_vals_from_move`

## `stock.quant.relocate` (defines)

Stock Quantity Relocation

- `quant_ids` Many2many → `stock.quant`
- `company_id` Many2one (related=quant_ids.company_id)
- `dest_location_id` Many2one → `stock.location`
- `dest_package_id_domain` Char (compute=_compute_dest_package_id_domain)
- `dest_package_id` Many2one → `stock.quant.package` (store, compute=_compute_dest_package_id)
- `message` Text “Reason for relocation”
- `is_partial_package` Boolean (compute=_compute_is_partial_package)
- `partial_package_names` Char (compute=_compute_is_partial_package)
- `is_multi_location` Boolean (compute=_compute_is_multi_location)

Public methods: `action_relocate_quants`

## `stock.quantity.history` (defines)

Stock Quantity History

- `inventory_datetime` Datetime “Inventory at Date”

Public methods: `open_at_date`

## `stock.replenishment.info` (defines)

Stock supplier replenishment information

- `orderpoint_id` Many2one → `stock.warehouse.orderpoint`
- `product_id` Many2one → `product.product` (related=orderpoint_id.product_id)
- `qty_to_order` Float (related=orderpoint_id.qty_to_order)
- `json_lead_days` Char (compute=_compute_json_lead_days)
- `json_replenishment_history` Char (compute=_compute_json_replenishment_history)
- `warehouseinfo_ids` One2many (related=orderpoint_id.warehouse_id.resupply_route_ids)
- `wh_replenishment_option_ids` One2many → `stock.replenishment.option` (compute=_compute_wh_replenishment_options)

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

- `inventory_date` Date “Inventory Date” (required)
- `user_id` Many2one → `res.users` “User”
- `quant_ids` Many2many → `stock.quant`
- `set_count` Selection “Count”

Public methods: `action_request_count`

Extension points: `_get_values_to_write`

## `stock.rules.report` (defines)

Stock Rules report

- `product_id` Many2one → `product.product` “Product” (required)
- `product_tmpl_id` Many2one → `product.template` “Product Template” (required)
- `warehouse_ids` Many2many → `stock.warehouse` “Warehouses” (required)
- `product_has_variants` Boolean “Has variants” (required)

Public methods: `default_get`, `print_report`

Extension points: `_prepare_report_data`

## `stock.scheduler.compute` (defines)

Run Scheduler Manually


Public methods: `procure_calculation`

## `stock.track.confirmation` (defines)

Stock Track Confirmation

- `tracking_line_ids` One2many → `stock.track.line`
- `quant_ids` Many2many → `stock.quant` “Quants”
- `product_ids` Many2many → `product.product` “Products”

Public methods: `action_confirm`

## `stock.track.line` (defines)

Stock Track Line

- `product_display_name` Char “Name” (readonly, compute=_compute_product_display_name)
- `product_id` Many2one → `product.product` (readonly)
- `tracking` Selection (related=product_id.tracking)
- `wizard_id` Many2one → `stock.track.confirmation` (readonly)

## `stock.warn.insufficient.qty` (defines)

Warn Insufficient Quantity

- `product_id` Many2one → `product.product` (required)
- `location_id` Many2one → `stock.location` (required)
- `quant_ids` Many2many → `stock.quant` (compute=_compute_quant_ids)
- `quantity` Float “Quantity” (required)
- `product_uom_name` Char “Unit of Measure” (required)

Public methods: `action_done`

Extension points: `_get_reference_document_company_id`

## `stock.warn.insufficient.qty.scrap` (defines)

Warn Insufficient Scrap Quantity

Inherits: `stock.warn.insufficient.qty`

- `scrap_id` Many2one → `stock.scrap`

Public methods: `action_cancel`, `action_done`

Extension points: `_get_reference_document_company_id`
