# sale_mrp — Sales and MRP Management

Depends on: mrp, sale_stock.

## `mrp.bom` (extends)


Public methods: `unlink`, `write`

## `mrp.production` (extends)

- `sale_order_count` Integer “Count of Source SO” (compute=_compute_sale_order_count)
- `sale_line_id` Many2one → `sale.order.line`

Public methods: `action_confirm`, `action_view_sale_orders`

Extension points: `_get_backorder_mo_vals`

## `sale.order` (extends)

- `mrp_production_count` Integer “Count of MO generated” (compute=_compute_mrp_production_ids)
- `mrp_production_ids` Many2many → `mrp.production` “Manufacturing orders associated with this sales order.” (compute=_compute_mrp_production_ids)

Public methods: `action_view_mrp_production`

## `sale.order.line` (extends)


Public methods: `compute_uom_qty`

Extension points: `_get_bom_component_qty`, `_get_incoming_outgoing_moves_filter`, `_get_qty_procurement`, `_prepare_qty_delivered`

## `stock.move` (extends)


Extension points: `_get_source_document`

## `stock.warehouse.orderpoint` (extends)


## `stock.rule` (extends)


Extension points: `_prepare_mo_vals`
