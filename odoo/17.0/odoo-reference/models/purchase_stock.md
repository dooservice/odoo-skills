# purchase_stock — Purchase Stock

Depends on: stock_account, purchase.

## `account.move` (extends)


## `account.move.line` (extends)


Extension points: `_get_out_and_not_invoiced_qty`, `_get_price_unit_val_dif_and_relevant_qty`, `_get_valued_in_moves`, `_prepare_pdiff_aml_vals`, `_prepare_pdiff_svl_vals`

## `product.category` (extends)

- `property_account_creditor_price_difference_categ` Many2one → `account.account` “Price Difference Account” (company_dependent)

## `product.template` (extends)

- `property_account_creditor_price_difference` Many2one → `account.account` “Price Difference Account” (company_dependent)
- `route_ids` Many2many

Extension points: `_get_buy_route`

## `product.product` (extends)

- `purchase_order_line_ids` One2many → `purchase.order.line` “PO Lines”

Extension points: `_get_lines_domain`, `_get_quantity_in_progress`

## `product.supplierinfo` (extends)

- `last_purchase_date` Date “Last Purchase” (compute=_compute_last_purchase_date)
- `show_set_supplier_button` Boolean “Show Set Supplier Button” (compute=_compute_show_set_supplier_button)

Public methods: `action_set_supplier`

## `purchase.order` (extends)

- `incoterm_location` Char “Incoterm Location”
- `incoming_picking_count` Integer “Incoming Shipment count” (compute=_compute_incoming_picking_count)
- `picking_ids` Many2many → `stock.picking` “Receptions” (store, compute=_compute_picking_ids)
- `dest_address_id` Many2one → `res.partner` (store, compute=_compute_dest_address_id)
- `picking_type_id` Many2one → `stock.picking.type` (required)
- `default_location_dest_id_usage` Selection “Destination Location Type” (readonly, related=picking_type_id.default_location_dest_id.usage)
- `group_id` Many2one → `procurement.group` “Procurement Group”
- `is_shipped` Boolean (compute=_compute_is_shipped)
- `effective_date` Datetime “Arrival” (store, compute=_compute_effective_date)
- `on_time_rate` Float (related=partner_id.on_time_rate)
- `receipt_status` Selection “Receipt Status” (store, compute=_compute_receipt_status)

Public methods: `action_add_from_catalog`, `action_view_picking`, `button_approve`, `button_cancel`, `write`

Extension points: `_create_picking`, `_create_update_date_activity`, `_get_action_view_picking`, `_get_destination_location`, `_get_orders_to_remind`, `_get_picking_type`, `_prepare_invoice`, `_prepare_picking`

## `purchase.order.line` (extends)

- `qty_received_method` Selection
- `move_ids` One2many → `stock.move` “Reservation” (readonly)
- `orderpoint_id` Many2one → `stock.warehouse.orderpoint`
- `move_dest_ids` Many2many → `stock.move`
- `product_description_variants` Char “Custom Description”
- `propagate_cancel` Boolean “Propagate cancellation”
- `forecasted_issue` Boolean (compute=_compute_forecasted_issue)

Public methods: `action_product_forecast_report`, `create`, `unlink`, `write`

Extension points: `_check_orderpoint_picking_type`, `_create_or_update_picking`, `_create_stock_moves`, `_get_move_dests_initial_demand`, `_get_outgoing_incoming_moves`, `_get_po_line_invoice_lines_su`, `_get_po_line_moves`, `_get_qty_procurement`, `_get_stock_move_price_unit`, `_prepare_account_move_line`, `_prepare_purchase_order_line_from_procurement`, `_prepare_stock_move_vals`, `_prepare_stock_moves`

## `res.company` (extends)

- `days_to_purchase` Float “Days to Purchase”

## `res.config.settings` (extends)

- `module_stock_dropshipping` Boolean “Dropshipping”
- `days_to_purchase` Float (related=company_id.days_to_purchase)
- `is_installed_sale` Boolean “Is the Sale Module Installed”

Public methods: `get_values`

## `res.partner` (extends)

- `purchase_line_ids` One2many → `purchase.order.line` “Purchase Lines”
- `on_time_rate` Float “On-Time Delivery Rate” (compute=_compute_on_time_rate)

## `stock.picking` (extends)

- `purchase_id` Many2one → `purchase.order` “Purchase Orders” (readonly, related=move_ids.purchase_line_id.order_id)

## `stock.warehouse` (extends)

- `buy_to_resupply` Boolean “Buy to Resupply”
- `buy_pull_id` Many2one → `stock.rule`

Public methods: `get_rules_dict`

Extension points: `_get_all_routes`, `_get_routes_values`

## `stock.return.picking` (extends)


Extension points: `_create_returns`, `_prepare_move_default_values`

## `stock.warehouse.orderpoint` (extends)

- `show_supplier` Boolean “Show supplier column” (compute=_compute_show_suppplier)
- `supplier_id` Many2one → `product.supplierinfo` “Product Supplier”
- `vendor_id` Many2one “Vendor” (store, related=supplier_id.partner_id)
- `purchase_visibility_days` Float

Public methods: `action_view_purchase`

Extension points: `_get_lead_days_values`, `_get_replenishment_order_notification`, `_prepare_procurement_values`

## `stock.lot` (extends)

- `purchase_order_ids` Many2many → `purchase.order` “Purchase Orders” (readonly, compute=_compute_purchase_order_ids)
- `purchase_order_count` Integer “Purchase order count” (compute=_compute_purchase_order_ids)

Public methods: `action_view_po`

## `procurement.group` (extends)


Public methods: `run`

## `stock.move` (extends)

- `purchase_line_id` Many2one → `purchase.order.line` (readonly)
- `created_purchase_line_ids` Many2many → `purchase.order.line`

Extension points: `_get_all_related_aml`, `_get_all_related_sm`, `_get_currency_convert_date`, `_get_price_unit`, `_get_purchase_line_and_partner_from_chain`, `_get_qty_received_without_self`, `_get_related_invoices`, `_get_source_document`, `_get_upstream_documents_and_responsibles`, `_get_valuation_price_and_qty`, `_prepare_extra_move_vals`, `_prepare_merge_moves_distinct_fields`, `_prepare_merge_negative_moves_excluded_distinct_fields`, `_prepare_move_split_vals`

## `stock.rule` (extends)

- `action` Selection

Extension points: `_get_lead_days`, `_get_message_dict`, `_get_partner_id`, `_get_procurements_to_merge`, `_get_procurements_to_merge_groupby`, `_prepare_purchase_order`

## `stock.valuation.layer` (extends)


Extension points: `_get_layer_price_unit`, `_get_related_product`

## `purchase.order` (extends)


## `purchase.report` (extends)

- `picking_type_id` Many2one → `stock.warehouse` (readonly)
- `effective_date` Datetime “Effective Date”

## `report.stock.report_stock_rule` (extends)


Extension points: `_get_rule_loc`

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

- `supplier_id` Many2one → `product.supplierinfo` “Vendor”
- `show_vendor` Boolean (compute=_compute_show_vendor)

Public methods: `action_stock_replenishment_info`, `default_get`

Extension points: `_get_date_planned`, `_get_record_to_notify`, `_get_replenishment_order_notification_link`, `_get_route_domain`, `_get_show_vendor`, `_prepare_run_values`

## `stock.replenishment.info` (extends)

Stock supplier replenishment information

- `supplierinfo_id` Many2one (related=orderpoint_id.supplier_id)
- `supplierinfo_ids` Many2many → `product.supplierinfo` (store, compute=_compute_supplierinfo_ids)

## `stock.replenishment.option` (extends)


Public methods: `select_route`
