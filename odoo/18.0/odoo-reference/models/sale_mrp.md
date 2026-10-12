# sale_mrp — Sales and MRP Management

Depends on: mrp, sale_stock.

## `account.move.line` (extends)


## `mrp.bom` (extends)


Public methods: `toggle_active`, `unlink`, `write`

## `mrp.production` (extends)

- `sale_order_count` Integer “Count of Source SO” (compute=_compute_sale_order_count)
- `sale_line_id` Many2one → `sale.order.line`

Public methods: `action_confirm`, `action_view_sale_orders`, `get_linked_sale_orders`

Extension points: `_post_run_manufacture`

## `sale.order` (extends)

- `mrp_production_count` Integer “Count of MO generated” (compute=_compute_mrp_production_ids)
- `mrp_production_ids` Many2many → `mrp.production` “Manufacturing orders associated with this sales order.” (compute=_compute_mrp_production_ids)

Public methods: `action_view_mrp_production`

## `sale.order.line` (extends)


Public methods: `compute_uom_qty`

Extension points: `_get_bom_component_qty`, `_get_incoming_outgoing_moves_filter`, `_get_qty_procurement`

## `stock.move.line` (extends)


## `stock.rule` (extends)


Extension points: `_get_stock_move_values`, `_prepare_mo_vals`
