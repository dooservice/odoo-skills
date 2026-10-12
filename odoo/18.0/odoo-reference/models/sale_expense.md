# sale_expense — Sales Expense

Depends on: sale_management, hr_expense.

## `account.move.line` (extends)


Extension points: `_get_so_mapping_from_expense`

## `account.move` (extends)


Public methods: `button_draft`

## `hr.expense` (extends)

- `sale_order_id` Many2one → `sale.order` “Customer to Reinvoice” (store, compute=_compute_sale_order_id)
- `can_be_reinvoiced` Boolean “Can be reinvoiced” (compute=_compute_can_be_reinvoiced)

Extension points: `_get_split_values`

## `hr.expense.sheet` (extends)

- `sale_order_count` Integer (compute=_compute_sale_order_count)

Public methods: `action_open_sale_orders`, `action_reset_expense_sheets`

Extension points: `_get_sale_order_lines`

## `hr.expense.split` (extends)

- `sale_order_id` Many2one → `sale.order` “Customer to Reinvoice” (store, compute=_compute_sale_order_id)
- `can_be_reinvoiced` Boolean “Can be reinvoiced” (compute=_compute_can_be_reinvoiced)

Public methods: `default_get`

Extension points: `_get_values`

## `product.template` (extends)

- `expense_policy_tooltip` Char (compute=_compute_expense_policy_tooltip)

## `sale.order` (extends)

- `expense_ids` One2many → `hr.expense` “Expenses” (readonly)
- `expense_count` Integer “# of Expenses” (compute=_compute_expense_count)
