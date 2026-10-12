# project_sale_expense — Project - Sale - Expense

Depends on: sale_project, sale_expense, project_hr_expense.

## `account.analytic.line` (extends)

- `category` Selection

Extension points: `_get_billable_types`, `_get_invoice_type`

## `account.move.line` (extends)


Extension points: `_prepare_analytic_distribution_line`

## `hr.expense` (extends)


Extension points: `_create_move`
