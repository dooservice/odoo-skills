# sale_expense — Sales Expense

Depends on: sale_management, hr_expense.

## `account.move` (extends)


Public methods: `button_draft`, `unlink`

## `account.move.line` (extends)


Extension points: `_get_so_mapping_from_expense`

## `hr.expense` (extends)

- `sale_order_id` Many2one → `sale.order` “Reinvoice to” (store, compute=_compute_sale_order_id)
- `sale_order_line_id` Many2one → `sale.order.line` (readonly, store, compute=_compute_sale_order_id)
- `can_be_reinvoiced` Boolean “Can be reinvoiced” (compute=_compute_can_be_reinvoiced)
- `attach_receipts_to_invoice` Boolean “Attach receipts to future customer invoices”

Public methods: `action_open_sale_order`

Extension points: `_get_split_values`

## `hr.expense.split` (extends)

- `sale_order_id` Many2one → `sale.order` “Reinvoice to” (store, compute=_compute_sale_order_id)
- `can_be_reinvoiced` Boolean “Can be reinvoiced” (compute=_compute_can_be_reinvoiced)

Extension points: `_get_values`

## `product.template` (extends)

- `expense_policy_tooltip` Char (compute=_compute_expense_policy_tooltip)

## `sale.order` (extends)

- `expense_ids` One2many → `hr.expense` “Expenses” (readonly)
- `expense_count` Integer “# of Expenses” (compute=_compute_expense_count)
- `is_linked_to_expense_with_attachment` Boolean (compute=_compute_is_linked_to_expense_with_attachment)

Public methods: `action_copy_reinvoiced_expense_receipts`

Extension points: `_get_expense_attachments_not_linked_yet`

## `sale.order.line` (extends)

- `expense_ids` One2many → `hr.expense` “Expenses” (readonly)

## `expense.attachment.selection.wizard` (defines)

Attachment Selection

- `sale_order_id` Many2one → `sale.order`
- `selected_attachments` Json (store, compute=_compute_selected_attachments)

Public methods: `action_import_attachments`
