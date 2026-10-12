# pos_stock — PoS - Stock

Depends on: point_of_sale, stock_account.

## `account.move` (extends)


Extension points: `_get_invoiced_lot_values`, `_get_stock_lot_from_pos_lot`

## `account.move.line` (extends)


Extension points: `_get_cogs_value`

## `pos.config` (extends)

- `picking_type_id` Many2one → `stock.picking.type` “Operation Type” (required)
- `ship_later` Boolean “Ship Later”
- `warehouse_id` Many2one → `stock.warehouse` (store, compute=_compute_warehouse_id)
- `route_id` Many2one → `stock.route` “Specific route for products delivered later.”
- `picking_policy` Selection “Shipping Policy” (required)

Public methods: `create`

## `pos.order` (extends)

- `picking_ids` One2many → `stock.picking`
- `picking_count` Integer (compute=_compute_picking_count)
- `failed_pickings` Boolean (compute=_compute_picking_count)
- `picking_type_id` Many2one → `stock.picking.type` “Operation Type” (related=session_id.config_id.picking_type_id)
- `stock_reference_ids` Many2many → `stock.reference` “Reference”
- `shipping_date` Date “Shipping Date”

Public methods: `action_stock_picking`, `get_stock_reports_to_print`, `process_saved_payments`, `read_pos_data`

Extension points: `_create_order_picking`, `_get_pos_anglo_saxon_price_unit`, `_get_total_cost_in_real_time_lines`, `_prepare_missing_invoice_moves`

## `pos.order.line` (extends)

- `pack_lot_ids` One2many → `pos.pack.operation.lot` “Lot/serial Number”

Public methods: `get_existing_lots`, `write`

Extension points: `_get_product_cost`, `_get_product_cost_with_moves`, `_get_qty_to_move`, `_get_stock_moves_to_consider`, `_prepare_procurement_values`, `_prepare_refund_data`

## `pos.pack.operation.lot` (defines)

Specify product lot/serial number in pos order line

Inherits: `pos.load.mixin`

- `pos_order_line_id` Many2one → `pos.order.line`
- `order_id` Many2one → `pos.order` (related=pos_order_line_id.order_id)
- `lot_name` Char “Lot Name”
- `product_id` Many2one → `product.product` (related=pos_order_line_id.product_id)

## `pos.session` (extends)

- `failed_pickings` Boolean (compute=_compute_picking_count)
- `picking_count` Integer (compute=_compute_picking_count)
- `picking_ids` One2many → `stock.picking`
- `update_stock_at_closing` Boolean “Stock should be updated at closing”

Public methods: `action_stock_picking`, `close_session_from_ui`

Extension points: `_create_partial_reversal_move_from_session_closing`, `_create_picking_at_end_of_session`, `_create_stock_valuation_lines`, `_get_default_session_vals`, `_get_related_account_moves`, `_get_rounding_difference_vals`, `_get_stock_expense_vals`, `_get_stock_valuation_vals`, `_prepare_session_closing_extra_line_commands`

## `product.category` (extends)


## `product.removal` (extends)

Inherits: `pos.load.mixin`


## `product.template` (extends)


Public methods: `get_product_info_pos`

Extension points: `_get_load_product_template_sql`

## `res.company` (extends)

- `point_of_sale_update_stock_quantities` Selection “Update quantities in stock”

## `res.config.settings` (extends)

- `update_stock_quantities` Selection (related=company_id.point_of_sale_update_stock_quantities)
- `pos_picking_policy` Selection (related=pos_config_id.picking_policy)
- `pos_picking_type_id` Many2one (related=pos_config_id.picking_type_id)
- `pos_route_id` Many2one (related=pos_config_id.route_id)
- `pos_warehouse_id` Many2one “Warehouse (PoS)” (related=pos_config_id.warehouse_id)
- `pos_ship_later` Boolean (related=pos_config_id.ship_later)

## `stock.move` (extends)


Extension points: `_create_production_lots_for_pos_order`, `_get_lot_line_qty`, `_get_new_picking_values`, `_prepare_lines_data_dict`

## `stock.picking` (extends)

- `pos_session_id` Many2one → `pos.session` (index)
- `pos_order_id` Many2one → `pos.order` (index)

Extension points: `_create_move_from_pos_order_lines`, `_create_picking_from_pos_order_lines`, `_prepare_picking_vals`, `_prepare_stock_move_vals`

## `stock.picking.type` (extends)

Inherits: `pos.load.mixin`

- `has_stock_reports_to_print` Boolean (compute=_compute_has_stock_reports_to_print)

Extension points: `_check_active`

## `stock.reference` (extends)

- `pos_order_ids` Many2many → `pos.order` “PoS Orders”

## `stock.rule` (extends)


Extension points: `_get_scheduler_tasks_to_do`

## `stock.warehouse` (extends)

- `pos_type_id` Many2one → `stock.picking.type` “Point of Sale Operation Type”

Extension points: `_create_missing_pos_picking_types`, `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_sequence_values`

## `pos.order.receipt` (extends)


Public methods: `order_receipt_generate_data`
