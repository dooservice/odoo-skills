# sale_stock — Sales and Warehouse Management

Depends on: sale, stock_account.

## `account.move` (extends)


Extension points: `_get_invoiced_lot_values`, `_get_protected_vals`

## `account.move.line` (extends)


## `product.template` (extends)


## `res.company` (extends)

- `allow_spontaneous_returns` Boolean “Allow Spontaneous Returns”
- `return_validity_days` Integer “Return Validity Days”
- `security_lead` Integer “Sales Safety Days” (required)

## `res.config.settings` (extends)

- `allow_spontaneous_returns` Boolean (related=company_id.allow_spontaneous_returns)
- `return_validity_days` Integer (related=company_id.return_validity_days)
- `security_lead` Integer “Security Lead Time” (related=company_id.security_lead)
- `use_security_lead` Boolean “Security Lead Time for Sales”

## `res.users` (extends)

- `property_warehouse_id` Many2one → `stock.warehouse` “Default Warehouse” (company_dependent)

Extension points: `_get_default_warehouse_id`

## `return.reason` (defines)

Return Reason

- `name` Char “Reason” (required)
- `sequence` Integer

## `sale.order` (extends)

- `picking_policy` Selection “Shipping Policy” (required)
- `warehouse_id` Many2one → `stock.warehouse` “Warehouse” (store, compute=_compute_warehouse_id)
- `picking_ids` One2many → `stock.picking` “Transfers”
- `delivery_count` Integer “Delivery Orders” (compute=_compute_picking_ids)
- `late_availability` Boolean “Late Availability” (compute=_compute_late_availability)
- `stock_reference_ids` Many2many → `stock.reference` “References”
- `effective_date` Datetime “Effective Date” (store, compute=_compute_effective_date)
- `expected_date` Datetime
- `json_popover` Char “JSON data for the popover widget” (compute=_compute_json_popover)
- `show_json_popover` Boolean “Has late picking” (compute=_compute_json_popover)

Public methods: `action_view_delivery`, `write`

Extension points: `_action_cancel`, `_action_confirm`, `_check_warehouse`, `_get_action_add_from_catalog_extra_context`, `_get_action_view_picking`, `_get_product_catalog_product_data`, `_prepare_invoice`

## `sale.order.line` (extends)

- `qty_delivered_method` Selection
- `route_ids` Many2many → `stock.route` “Routes”
- `move_ids` One2many → `stock.move` “Stock Moves”
- `forecast_expected_date` Datetime (compute=_compute_qty_at_date)
- `free_qty_today` Float (compute=_compute_qty_at_date)
- `warehouse_id` Many2one → `stock.warehouse` (store, compute=_compute_warehouse_id)
- `qty_to_deliver` Float (compute=_compute_qty_to_deliver)
- `is_mto` Boolean (compute=_compute_is_mto)
- `display_qty_widget` Boolean (compute=_compute_qty_to_deliver)
- `customer_lead` Integer (store)

Public methods: `create`, `has_valued_move_ids`, `write`

Extension points: `_action_launch_stock_rule`, `_create_procurements`, `_get_accrual_domain`, `_get_consu_qty_delivered_method`, `_get_location_final`, `_get_outgoing_incoming_moves`, `_get_product_catalog_lines_data`, `_get_qty_procurement`, `_prepare_procurement_values`, `_prepare_qty_delivered`, `_prepare_reference_vals`

## `stock.route` (extends)

- `sale_selectable` Boolean “Selectable on Sales Order Line”

## `stock.move` (extends)

- `sale_line_id` Many2one → `sale.order.line`

Public methods: `write`

Extension points: `_action_synch_order`, `_get_origin_company_domains`, `_get_sale_order_lines`, `_get_source_document`, `_prepare_merge_moves_distinct_fields`, `_prepare_procurement_values`, `_prepare_return_data`

## `stock.move.line` (extends)


## `stock.rule` (extends)


Extension points: `_get_custom_move_fields`

## `stock.picking` (extends)

- `allow_spontaneous_returns` Boolean (related=company_id.allow_spontaneous_returns)
- `sale_id` Many2one → `sale.order` “Sales Order” (store, compute=_compute_sale_id)
- `return_reason_id` Many2one → `return.reason`

Extension points: `_action_done`, `_create_return`, `_prepare_return_move_default_values`, `_prepare_return_picking_default_values`

## `stock.lot` (extends)

- `sale_order_ids` Many2many → `sale.order` “Sales Orders” (compute=_compute_sale_order_ids)
- `sale_order_count` Integer “Sale order count” (compute=_compute_sale_order_ids)

Public methods: `action_view_so`

## `stock.reference` (extends)

- `sale_ids` Many2many → `sale.order` “Sales”

## `report.stock.report_stock_rule` (extends)


Extension points: `_get_routes`

## `sale.report` (extends)

- `warehouse_id` Many2one → `stock.warehouse` (readonly)

## `stock.forecasted_product_product` (extends)


Extension points: `_get_report_header`, `_prepare_report_line`

## `stock.replenishment.info` (extends)

Stock delivery time information

- `sale_delay` Integer “Availability Time” (required, related=product_id.sale_delay)

Extension points: `_get_warning_days`

## `stock.rules.report` (extends)

- `so_route_ids` Many2many → `stock.route` “Apply specific routes”

Extension points: `_prepare_report_data`
