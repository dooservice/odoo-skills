# sale_project_stock — Sale Project - Sale Stock

Depends on: sale_project, sale_stock, project_stock_account.

## `account.analytic.line` (extends)


Extension points: `_get_billable_types`, `_get_invoice_type`

## `project.project` (extends)


Extension points: `_get_picking_action`

## `stock.move` (extends)


Extension points: `_get_new_picking_values`, `_prepare_procurement_values`

## `stock.picking` (extends)


Public methods: `button_validate`
