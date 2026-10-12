# project_stock_account — Project Stock Account

Depends on: stock_account, project_stock.

## `account.analytic.line` (extends)

- `category` Selection

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection

## `project.project` (extends)


Extension points: `_get_items_from_aal_picking`, `_get_profitability_items`, `_get_profitability_labels`, `_get_profitability_sequence_per_invoice_type`

## `stock.move` (extends)


Extension points: `_create_analytic_move`, `_get_analytic_distribution`, `_get_valid_moves_domain`, `_prepare_analytic_line_values`, `_prepare_analytic_lines`

## `stock.picking.type` (extends)

- `analytic_costs` Boolean
