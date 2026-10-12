# sale_project_stock — Sale Project - Sale Stock

Depends on: sale_project, sale_stock, project_stock_account.

## `project.project` (extends)


Extension points: `_get_picking_action`

## `sale.order.line` (extends)


Extension points: `_get_action_per_item`

## `stock.move` (extends)


Extension points: `_get_new_picking_values`, `_prepare_procurement_values`

## `stock.picking` (extends)


Public methods: `button_validate`
