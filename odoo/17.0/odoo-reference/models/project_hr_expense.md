# project_hr_expense — Project Expenses

Depends on: project_account, hr_expense.

## `hr.expense` (extends)


## `project.project` (extends)

- `expenses_count` Integer “# Expenses” (compute=_compute_expenses_count)

Public methods: `action_profitability_items`

Extension points: `_get_add_purchase_items_domain`, `_get_already_included_profitability_invoice_line_ids`, `_get_expense_action`, `_get_expenses_profitability_items`, `_get_profitability_aal_domain`, `_get_profitability_items`, `_get_profitability_labels`, `_get_profitability_sequence_per_invoice_type`
