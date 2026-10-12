# project_stock_account — Project Stock Account

Depends on: stock_account, project_stock.

## `account.analytic.line` (extends)

- `category` Selection

## `account.analytic.applicability` (extends)

- `business_domain` Selection

## `stock.move` (extends)


Extension points: `_create_analytic_move`, `_get_analytic_distribution`, `_get_valid_moves_domain`, `_prepare_analytic_line_values`, `_prepare_analytic_lines`

## `stock.picking.type` (extends)

- `analytic_costs` Boolean (store, compute=_compute_analytic_costs)
