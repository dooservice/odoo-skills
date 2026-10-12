# sale_mrp — Sales and MRP Management

Depends on: mrp, sale_stock.

## `account.move.line` (extends)


## `mrp.bom` (extends)


Public methods: `toggle_active`, `unlink`, `write`

## `mrp.production` (extends)

- `sale_order_count` Integer “Count of Source SO” (compute=_compute_sale_order_count)

Public methods: `action_view_sale_orders`

## `sale.order` (extends)

- `mrp_production_count` Integer “Count of MO generated” (compute=_compute_mrp_production_ids)
- `mrp_production_ids` Many2many → `mrp.production` “Manufacturing orders associated with this sales order.” (compute=_compute_mrp_production_ids)

Public methods: `action_view_mrp_production`

## `sale.order.line` (extends)


Public methods: `compute_uom_qty`

Extension points: `_get_bom_component_qty`, `_get_qty_procurement`

## `stock.move` (extends)


Extension points: `_prepare_procurement_values`

## `stock.move.line` (extends)
