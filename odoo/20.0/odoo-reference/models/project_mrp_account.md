# project_mrp_account — MRP Account Project

Depends on: mrp_account, project_mrp, project_stock_account.

## `mrp.production` (extends)

- `has_analytic_account` Boolean (compute=_compute_has_analytic_account)

Public methods: `action_confirm`, `action_view_analytic_accounts`, `write`

## `mrp.workorder` (extends)


Extension points: `_create_or_update_analytic_entry_for_record`

## `stock.move` (extends)


Extension points: `_get_analytic_distribution`, `_prepare_analytic_line_values`, `_prepare_analytic_lines`

## `stock.picking.type` (extends)


## `stock.rule` (extends)


Extension points: `_prepare_mo_vals`
