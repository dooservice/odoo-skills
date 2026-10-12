# sale_stock — Sales and Warehouse Management

Depends on: sale, stock_account.

## `account.move` (extends)


Extension points: `_get_anglo_saxon_price_ctx`, `_get_invoiced_lot_values`, `_get_protected_vals`

## `account.move.line` (extends)


## `product.template` (extends)


## `res.company` (extends)

- `security_lead` Float “Sales Safety Days” (required)

## `res.config.settings` (extends)

- `security_lead` Float “Security Lead Time” (related=company_id.security_lead)
- `use_security_lead` Boolean “Security Lead Time for Sales”
- `default_picking_policy` Selection (required)

## `res.users` (extends)

- `property_warehouse_id` Many2one → `stock.warehouse` “Default Warehouse” (company_dependent)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`

Extension points: `_get_default_warehouse_id`

## `sale.order` (extends)

- `incoterm` Many2one → `account.incoterms`
- `incoterm_location` Char “Incoterm Location”
- `picking_policy` Selection “Shipping Policy” (required)
- `warehouse_id` Many2one → `stock.warehouse` “Warehouse” (store, compute=_compute_warehouse_id)
- `picking_ids` One2many → `stock.picking` “Transfers”
- `delivery_count` Integer “Delivery Orders” (compute=_compute_picking_ids)
- `delivery_status` Selection “Delivery Status” (store, compute=_compute_delivery_status)
- `procurement_group_id` Many2one → `procurement.group`
- `effective_date` Datetime “Effective Date” (store, compute=_compute_effective_date)
- `expected_date` Datetime
- `json_popover` Char “JSON data for the popover widget” (compute=_compute_json_popover)
- `show_json_popover` Boolean “Has late picking” (compute=_compute_json_popover)

Public methods: `action_view_delivery`, `write`

Extension points: `_action_cancel`, `_action_confirm`, `_check_warehouse`, `_get_action_view_picking`, `_prepare_invoice`

## `sale.order.line` (extends)

- `qty_delivered_method` Selection
- `route_id` Many2one → `stock.route` “Route”
- `move_ids` One2many → `stock.move` “Stock Moves”
- `virtual_available_at_date` Float (compute=_compute_qty_at_date)
- `scheduled_date` Datetime (compute=_compute_qty_at_date)
- `forecast_expected_date` Datetime (compute=_compute_qty_at_date)
- `free_qty_today` Float (compute=_compute_qty_at_date)
- `qty_available_today` Float (compute=_compute_qty_at_date)
- `warehouse_id` Many2one → `stock.warehouse` (store, compute=_compute_warehouse_id)
- `qty_to_deliver` Float (compute=_compute_qty_to_deliver)
- `is_mto` Boolean (compute=_compute_is_mto)
- `display_qty_widget` Boolean (compute=_compute_qty_to_deliver)
- `is_storable` Boolean (related=product_id.is_storable)
- `customer_lead` Float (store, compute=_compute_customer_lead)

Public methods: `create`, `has_valued_move_ids`, `write`

Extension points: `_action_launch_stock_rule`, `_create_procurements`, `_get_action_add_from_catalog_extra_context`, `_get_location_final`, `_get_outgoing_incoming_moves`, `_get_procurement_group`, `_get_product_catalog_lines_data`, `_get_qty_procurement`, `_prepare_procurement_group_vals`, `_prepare_procurement_values`

## `stock.route` (extends)

- `sale_selectable` Boolean “Selectable on Sales Order Line”

## `stock.move` (extends)

- `sale_line_id` Many2one → `sale.order.line`

Public methods: `write`

Extension points: `_get_all_related_sm`, `_get_related_invoices`, `_get_sale_order_lines`, `_get_source_document`, `_prepare_merge_moves_distinct_fields`, `_prepare_procurement_values`

## `stock.move.line` (extends)


## `procurement.group` (extends)

- `sale_id` Many2one → `sale.order`

## `stock.rule` (extends)


Extension points: `_get_custom_move_fields`

## `stock.picking` (extends)

- `sale_id` Many2one → `sale.order` “Sales Order” (store, compute=_compute_sale_id)

Extension points: `_action_done`

## `stock.lot` (extends)

- `sale_order_ids` Many2many → `sale.order` “Sales Orders” (compute=_compute_sale_order_ids)
- `sale_order_count` Integer “Sale order count” (compute=_compute_sale_order_ids)

Public methods: `action_view_so`

## `stock.valuation.layer` (extends)


Extension points: `_get_related_product`

## `stock.warehouse` (extends)


Extension points: `_get_routes_values`

## `report.stock.report_stock_rule` (extends)


Extension points: `_get_routes`

## `sale.report` (extends)

- `warehouse_id` Many2one → `stock.warehouse` (readonly)

## `stock.forecasted_product_product` (extends)


Extension points: `_get_report_header`, `_prepare_report_line`

## `sale.order.cancel` (extends)

- `display_delivery_alert` Boolean “Delivery Alert” (compute=_compute_display_delivery_alert)

## `stock.return.picking` (extends)


Extension points: `_get_proc_values`

## `stock.rules.report` (extends)

- `so_route_ids` Many2many → `stock.route` “Apply specific routes”

Extension points: `_prepare_report_data`
