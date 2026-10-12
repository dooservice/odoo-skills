# purchase_stock — Purchase Stock

Depends on: stock_account, purchase.

## `account.move.line` (extends)


## `product.template` (extends)


## `product.product` (extends)

- `purchase_order_line_ids` One2many → `purchase.order.line` “PO Lines”
- `monthly_demand` Float (compute=_compute_monthly_demand)
- `suggested_qty` Integer (compute=_compute_suggested_quantity)
- `suggest_estimated_price` Float (compute=_compute_suggest_estimated_price)

Public methods: `get_routes_actions`

Extension points: `_get_lines_domain`, `_get_monthly_demand_moves_location_domain`, `_get_monthly_demand_range`, `_get_quantity_in_progress`

## `product.supplierinfo` (extends)

- `last_purchase_date` Date “Last Purchase” (compute=_compute_last_purchase_date)
- `show_set_supplier_button` Boolean “Show Set Supplier Button” (compute=_compute_show_set_supplier_button)

Public methods: `action_set_supplier`

Extension points: `_get_seller_info_display_name`

## `purchase.order` (extends)

- `incoming_picking_count` Integer “Incoming Shipment count” (compute=_compute_incoming_picking_count)
- `picking_ids` Many2many → `stock.picking` “Receptions” (store, compute=_compute_picking_ids)
- `dest_address_id` Many2one → `res.partner` (store, compute=_compute_dest_address_id)
- `picking_type_id` Many2one → `stock.picking.type` (required, index)
- `default_location_dest_id_usage` Selection “Destination Location Type” (readonly, related=picking_type_id.default_location_dest_id.usage)
- `reference_ids` Many2many → `stock.reference` “References”
- `is_shipped` Boolean (compute=_compute_is_shipped)
- `effective_date` Datetime “Arrival” (store, compute=_compute_effective_date)
- `on_time_rate` Float (related=partner_id.on_time_rate)
- `date_promised` Datetime “Promised Date” (store, index, compute=_compute_date_promised)

Public methods: `action_add_from_catalog`, `action_purchase_order_suggest`, `action_view_picking`, `button_approve`, `button_cancel`, `onchange`, `retrieve_dashboard`, `write`

Extension points: `_create_picking`, `_create_update_date_activity`, `_get_action_add_from_catalog_extra_context`, `_get_action_view_picking`, `_get_allowed_picking_code`, `_get_destination_location`, `_get_domain_is_late`, `_get_final_location_record`, `_get_orders_to_remind`, `_get_picking_type`, `_get_product_catalog_order_line_info`, `_get_product_catalog_product_data`, `_prepare_grouped_data`, `_prepare_reference_vals`

## `purchase.order.line` (extends)

- `qty_received_method` Selection
- `move_ids` One2many → `stock.move` “Reservation” (readonly)
- `orderpoint_id` Many2one → `stock.warehouse.orderpoint`
- `move_dest_ids` Many2many → `stock.move`
- `product_description_variants` Char “Custom Description”
- `propagate_cancel` Boolean “Propagate cancellation”
- `forecasted_issue` Boolean (compute=_compute_forecasted_issue)
- `is_storable` Boolean (related=product_id.is_storable)
- `forecasted_location_id` Many2one → `stock.location`
- `date_promised` Datetime “Promised Date”

Public methods: `action_product_forecast_report`, `create`, `unlink`, `write`

Extension points: `_check_orderpoint_picking_type`, `_create_or_update_picking`, `_create_stock_moves`, `_get_accrual_domain`, `_get_move_dests_initial_demand`, `_get_outgoing_incoming_moves`, `_get_po_line_moves`, `_get_qty_procurement`, `_get_stock_move_price_unit`, `_prepare_account_move_line`, `_prepare_purchase_order_line_from_procurement`, `_prepare_qty_received`, `_prepare_stock_move_vals`, `_prepare_stock_moves`

## `res.company` (extends)

- `days_to_purchase` Integer “Days to Purchase”

## `res.config.settings` (extends)

- `module_stock_dropshipping` Boolean “Dropshipping”
- `days_to_purchase` Integer (related=company_id.days_to_purchase)
- `is_installed_sale` Boolean “Is the Sale Module Installed”

Public methods: `get_values`

## `res.partner` (extends)

- `purchase_line_ids` One2many → `purchase.order.line` “Purchase Lines”
- `on_time_rate` Float “On-Time Delivery Rate” (compute=_compute_on_time_rate)
- `suggest_based_on` Char
- `suggest_days` Integer
- `suggest_percent` Integer
- `group_rfq` Selection “Group RFQ” (required)
- `group_on` Selection “Week Day” (required)

Public methods: `name_search`

## `stock.picking` (extends)

- `purchase_id` Many2one → `purchase.order` “Purchase Orders” (readonly, related=move_ids.purchase_line_id.order_id)
- `days_to_arrive` Datetime (compute=_compute_effective_date)
- `delay_pass` Datetime (index, compute=_compute_date_order)

Extension points: `_action_done`, `_create_return`, `_prepare_return_move_default_values`

## `stock.warehouse` (extends)

- `buy_to_resupply` Boolean “Buy to Resupply” (compute=_compute_buy_to_resupply)
- `buy_pull_id` Many2one → `stock.rule`

Public methods: `get_rules_dict`

Extension points: `_create_or_update_route`, `_get_all_routes`, `_get_routes_values`

## `stock.warehouse.orderpoint` (extends)

- `show_supplier` Boolean “Show supplier column” (compute=_compute_show_supplier)
- `supplier_id` Many2one → `product.supplierinfo` “Vendor Pricelist”
- `supplier_id_placeholder` Char (compute=_compute_supplier_id_placeholder)
- `vendor_ids` One2many “Vendors” (related=product_id.seller_ids)
- `effective_vendor_id` Many2one → `res.partner` (compute=_compute_effective_vendor_id)
- `available_vendor` Many2one → `res.partner` “Available Vendor”

Public methods: `action_view_purchase`

Extension points: `_get_default_route`, `_get_default_supplier`, `_get_lead_days_values`, `_get_po_history_product_ids`, `_get_replenishment_multiple_alternative`, `_get_replenishment_order_notification`, `_prepare_procurement_values`

## `stock.lot` (extends)

- `purchase_order_ids` Many2many → `purchase.order` “Purchase Orders” (readonly, compute=_compute_purchase_order_ids)
- `purchase_order_count` Integer “Purchase order count” (compute=_compute_purchase_order_ids)

Public methods: `action_view_po`

## `stock.move` (extends)

- `purchase_line_id` Many2one → `purchase.order.line` (readonly)
- `created_purchase_line_ids` Many2many → `purchase.order.line`

Public methods: `write`

Extension points: `_action_synch_order`, `_get_cost_ratio`, `_get_description`, `_get_origin_company_domains`, `_get_purchase_line_and_partner_from_chain`, `_get_quantity_from_bill`, `_get_source_document`, `_get_upstream_documents_and_responsibles`, `_get_value_from_account_move`, `_get_value_from_bill`, `_get_value_from_quotation`, `_prepare_merge_moves_distinct_fields`, `_prepare_merge_negative_moves_excluded_distinct_fields`, `_prepare_move_split_vals`

## `stock.reference` (extends)

- `purchase_ids` Many2many → `purchase.order` “Purchases”

## `stock.replenish.mixin` (extends)

- `supplier_id` Many2one → `product.supplierinfo` “Vendor”
- `show_vendor` Boolean (compute=_compute_show_vendor)

Extension points: `_get_show_vendor`

## `stock.rule` (extends)

- `action` Selection

Public methods: `run`

Extension points: `_get_lead_days`, `_get_message_dict`, `_get_procurements_to_merge`, `_get_procurements_to_merge_groupby`, `_post_vendor_notification`, `_prepare_purchase_order`

## `stock.route` (extends)


Extension points: `_get_non_push_pull_rule_actions`

## `purchase.report` (extends)

- `picking_type_id` Many2one → `stock.warehouse` (readonly)
- `effective_date` Datetime “Effective Date”
- `days_to_arrival` Float “Effective Days To Arrival” (readonly)

## `report.stock.report_stock_rule` (extends)


Extension points: `_get_rule_loc`

## `stock.allocation.report` (extends)


Extension points: `_get_record_source`

## `stock.forecasted_product_product` (extends)


Extension points: `_get_report_header`

## `vendor.delay.report` (defines)

Vendor Delay Report

- `partner_id` Many2one → `res.partner` (readonly)
- `product_id` Many2one → `product.product` (readonly)
- `category_id` Many2one → `product.category` (readonly)
- `date` Datetime “Effective Date” (readonly)
- `qty_total` Float “Total Quantity” (readonly)
- `qty_on_time` Float “On-Time Quantity” (readonly)
- `on_time_rate` Float “On-Time Delivery Rate” (readonly)

Public methods: `init`

## `product.replenish` (extends)

- `partner_id` Many2one → `res.partner` “Supplier”

Public methods: `action_stock_replenishment_info`, `default_get`

Extension points: `_get_date_planned`, `_get_record_to_notify`, `_get_replenishment_order_notification_link`, `_get_route_domain`, `_prepare_run_values`

## `stock.replenishment.info` (extends)

Stock supplier replenishment information

- `supplierinfo_id` Many2one (related=orderpoint_id.supplier_id)
- `supplierinfo_ids` Many2many → `product.supplierinfo` (store, compute=_compute_supplierinfo_ids)
- `show_vendor_tab` Boolean (compute=_compute_show_vendor_tab)

## `stock.replenishment.option` (extends)


Public methods: `select_route`
