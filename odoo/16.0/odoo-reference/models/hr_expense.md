# hr_expense — Expenses

Depends on: hr_contract, account, web_tour.

## `account.journal` (extends)


Public methods: `get_journal_dashboard_datas`, `open_expenses_action`

Extension points: `_get_expense_to_pay_query`, `_get_expenses_to_pay_query`, `_prepare_expense_sheet_data_domain`

## `account.move` (extends)

- `expense_sheet_id` One2many → `hr.expense.sheet`

Public methods: `action_open_expense_report`, `button_draft`, `unlink`

Extension points: `_check_journal_move_type`

## `account.move.line` (extends)

- `expense_id` Many2one → `hr.expense` “Expense”

Public methods: `reconcile`

Extension points: `_check_payable_receivable`, `_get_attachment_domains`, `_get_extra_query_base_tax_line_mapping`

## `account.payment` (extends)


Public methods: `action_cancel`, `action_draft`, `action_open_expense_report`

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection

## `account.analytic.account` (extends)


## `hr.department` (extends)

- `expense_sheets_to_approve_count` Integer “Expenses Reports to Approve” (compute=_compute_expense_sheets_to_approve)

## `hr.employee` (extends)

- `expense_manager_id` Many2one → `res.users` “Expense” (store, compute=_compute_expense_manager)

Extension points: `_get_user_m2o_to_empty_on_archived_employees`

## `hr.employee.public` (extends)

- `expense_manager_id` Many2one → `res.users` (readonly)

## `res.users` (extends)

- `expense_manager_id` Many2one (related=employee_id.expense_manager_id)

Public methods: `SELF_READABLE_FIELDS`

## `hr.expense` (defines)

Expense

Inherits: `mail.thread`, `mail.activity.mixin`, `analytic.mixin`

- `name` Char “Description” (required, store, compute=_compute_name)
- `date` Date “Expense Date”
- `accounting_date` Date “Accounting Date” (store, related=sheet_id.accounting_date)
- `employee_id` Many2one → `hr.employee` “Employee” (required, store, compute=_compute_employee_id)
- `product_id` Many2one → `product.product` “Category”
- `product_description` Html (compute=_compute_product_description)
- `product_uom_id` Many2one → `uom.uom` “Unit of Measure” (readonly, store, compute=_compute_product_uom_id)
- `product_uom_category_id` Many2one “UoM Category” (readonly, related=product_id.uom_id.category_id)
- `unit_amount` Float “Unit Price” (required, store, compute=_compute_unit_amount)
- `unit_amount_display` Float “Unit Price Display” (compute=_compute_unit_amount_display)
- `quantity` Float (required)
- `tax_ids` Many2many → `account.tax` “Included taxes” (store, compute=_compute_tax_ids)
- `amount_tax` Monetary “Tax amount in Currency” (store, compute=_compute_amount_tax)
- `amount_tax_company` Monetary “Tax amount” (store, compute=_compute_total_amount_company)
- `amount_residual` Monetary “Amount Due” (compute=_compute_amount_residual)
- `total_amount` Monetary “Total In Currency” (store, compute=_compute_amount)
- `untaxed_amount` Monetary “Total Untaxed Amount In Currency” (store, compute=_compute_amount_tax)
- `company_currency_id` Many2one → `res.currency` “Report Company Currency” (readonly, related=company_id.currency_id)
- `total_amount_company` Monetary “Total” (store, compute=_compute_total_amount_company)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `currency_id` Many2one → `res.currency` “Currency” (required, store, compute=_compute_currency_id)
- `currency_rate` Float (compute=_compute_currency_rate)
- `account_id` Many2one → `account.account` “Account” (store, compute=_compute_account_id)
- `description` Text “Internal Notes” (readonly)
- `payment_mode` Selection “Paid By”
- `attachment_number` Integer “Number of Attachments” (compute=_compute_attachment_number)
- `attachment_ids` One2many → `ir.attachment` “Attachments”
- `state` Selection “Status” (readonly, store, index, compute=_compute_state)
- `sheet_id` Many2one → `hr.expense.sheet` “Expense Report” (readonly)
- `sheet_is_editable` Boolean (compute=_compute_sheet_is_editable)
- `approved_by` Many2one → `res.users` “Approved By” (related=sheet_id.user_id)
- `approved_on` Datetime “Approved On” (related=sheet_id.approval_date)
- `reference` Char “Bill Reference”
- `is_refused` Boolean “Explicitly Refused by manager or accountant” (readonly)
- `is_editable` Boolean “Is Editable By Current User” (compute=_compute_is_editable)
- `is_ref_editable` Boolean “Reference Is Editable By Current User” (compute=_compute_is_ref_editable)
- `product_has_cost` Boolean “Is product with non zero cost selected” (compute=_compute_product_has_cost)
- `product_has_tax` Boolean “Whether tax is defined on a selected product” (compute=_compute_product_has_cost)
- `same_currency` Boolean “Is currency_id different from the company_currency_id” (compute=_compute_same_currency)
- `duplicate_expense_ids` Many2many → `hr.expense` (compute=_compute_duplicate_expense_ids)
- `sample` Boolean
- `label_convert_rate` Char (compute=_compute_label_convert_rate)

Public methods: `action_approve_duplicates`, `action_get_attachment_view`, `action_move_create`, `action_split_wizard`, `action_submit_expenses`, `action_view_sheet`, `attach_document`, `create_expense_from_attachments`, `get_empty_list_help`, `get_expense_dashboard`, `get_expenses_to_submit`, `message_new`, `refuse_expense`, `unlink`, `write`

Extension points: `_check_payment_mode`, `_check_product_uom_category`, `_get_default_expense_sheet_values`, `_get_employee_from_email`, `_get_employee_id_domain`, `_get_empty_list_mail_alias`, `_get_expense_account_destination`, `_get_split_values`, `_get_taxes`, `_prepare_move_line_vals`

## `hr.expense.sheet` (defines)

Expense Report

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Expense Report Summary” (required)
- `expense_line_ids` One2many → `hr.expense` “Expense Lines”
- `product_ids` Many2many → `product.product` “Categories” (compute=_compute_product_ids)
- `is_editable` Boolean “Expense Lines Are Editable By Current User” (compute=_compute_is_editable)
- `expense_number` Integer “Number of Expenses” (compute=_compute_expense_number)
- `state` Selection “Status” (required, readonly, index)
- `payment_state` Selection “Payment Status” (readonly, store, compute=_compute_payment_state)
- `employee_id` Many2one → `hr.employee` “Employee” (required, readonly)
- `address_id` Many2one → `res.partner` “Employee Home Address” (store, compute=_compute_from_employee_id)
- `payment_mode` Selection “Paid By” (readonly, related=expense_line_ids.payment_mode)
- `user_id` Many2one → `res.users` (readonly, store, compute=_compute_from_employee_id)
- `total_amount` Monetary “Total Amount” (store, compute=_compute_amount)
- `untaxed_amount` Monetary “Untaxed Amount” (store, compute=_compute_amount)
- `total_amount_taxes` Monetary “Taxes” (store, compute=_compute_amount)
- `amount_residual` Monetary “Amount Due” (store, related=account_move_id.amount_residual)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `currency_id` Many2one → `res.currency` “Currency” (readonly, store, compute=_compute_currency_id)
- `attachment_number` Integer “Number of Attachments” (compute=_compute_attachment_number)
- `attachment_ids` One2many → `ir.attachment` “Attachments of expenses”
- `message_main_attachment_id` Many2one (store, compute=_compute_main_attachment)
- `journal_displayed_id` Many2one → `account.journal` “Journal” (compute=_compute_journal_displayed_id)
- `journal_id` Many2one → `account.journal` “Expense Journal”
- `bank_journal_id` Many2one → `account.journal` “Bank Journal”
- `accounting_date` Date “Accounting Date” (store, compute=_compute_accounting_date)
- `account_move_id` Many2one → `account.move` “Journal Entry” (readonly)
- `department_id` Many2one → `hr.department` “Department” (store, compute=_compute_from_employee_id)
- `is_multiple_currency` Boolean “Handle lines with different currencies” (compute=_compute_is_multiple_currency)
- `can_reset` Boolean “Can Reset” (compute=_compute_can_reset)
- `can_approve` Boolean “Can Approve” (compute=_compute_can_approve)
- `approval_date` Datetime “Approval Date” (readonly)

Public methods: `action_get_attachment_view`, `action_get_expense_view`, `action_open_account_move`, `action_register_payment`, `action_sheet_move_create`, `action_submit_sheet`, `action_unpost`, `activity_update`, `approve_expense_sheets`, `create`, `paid_expense_sheets`, `refuse_sheet`, `reset_expense_sheets`, `set_to_paid`, `write`

Extension points: `_check_can_approve`, `_check_can_refuse`, `_check_employee`, `_check_expense_lines_company`, `_check_payment_mode`, `_get_responsible_for_approval`, `_prepare_bill_vals`, `_prepare_move_vals`, `_prepare_payment_vals`

## `ir.attachment` (extends)


Public methods: `create`, `unlink`

## `product.product` (extends)

- `standard_price_update_warning` Char (compute=_compute_standard_price_update_warning)

## `product.template` (extends)

- `can_be_expensed` Boolean “Can be Expensed” (store, compute=_compute_can_be_expensed)

Public methods: `default_get`

## `res.company` (extends)

- `expense_journal_id` Many2one → `account.journal` “Default Expense Journal”
- `company_expense_journal_id` Many2one → `account.journal` “Default Company Expense Journal”

## `res.config.settings` (extends)

- `expense_alias_prefix` Char “Default Alias Name for Expenses” (store, compute=_compute_expense_alias_prefix)
- `use_mailgateway` Boolean “Let your employees record expenses by email”
- `module_hr_payroll_expense` Boolean “Reimburse Expenses in Payslip”
- `module_hr_expense_extract` Boolean “Send bills to OCR to generate expenses”
- `expense_journal_id` Many2one → `account.journal` (related=company_id.expense_journal_id)
- `company_expense_journal_id` Many2one → `account.journal` (related=company_id.company_expense_journal_id)

Public methods: `get_values`, `set_values`

## `account.payment.register` (extends)


Extension points: `_get_line_batch_key`

## `hr.expense.approve.duplicate` (defines)

Expense Approve Duplicate

- `sheet_ids` Many2many → `hr.expense.sheet`
- `expense_ids` Many2many → `hr.expense` (readonly)

Public methods: `action_approve`, `action_refuse`, `default_get`

## `hr.expense.refuse.wizard` (defines)

Expense Refuse Reason Wizard

- `reason` Char “Reason” (required)
- `hr_expense_ids` Many2many → `hr.expense`
- `hr_expense_sheet_id` Many2one → `hr.expense.sheet`

Public methods: `default_get`, `expense_refuse_reason`

## `hr.expense.split` (defines)

Expense Split

Inherits: `analytic.mixin`

- `name` Char “Description” (required)
- `wizard_id` Many2one → `hr.expense.split.wizard`
- `expense_id` Many2one → `hr.expense` “Expense”
- `product_id` Many2one → `product.product` “Product” (required)
- `tax_ids` Many2many → `account.tax`
- `total_amount` Monetary “Total In Currency” (required, store, compute=_compute_from_product_id)
- `amount_tax` Monetary “Tax amount in Currency” (compute=_compute_amount_tax)
- `employee_id` Many2one → `hr.employee` “Employee” (required)
- `company_id` Many2one → `res.company`
- `currency_id` Many2one → `res.currency`
- `product_has_tax` Boolean “Whether tax is defined on a selected product” (compute=_compute_product_has_tax)
- `product_has_cost` Boolean “Is product with non zero cost selected” (store, compute=_compute_from_product_id)

Public methods: `default_get`

Extension points: `_get_values`

## `hr.expense.split.wizard` (defines)

Expense Split Wizard

- `expense_id` Many2one → `hr.expense` “Expense” (required)
- `expense_split_line_ids` One2many → `hr.expense.split`
- `total_amount` Monetary “Total Amount” (compute=_compute_total_amount)
- `total_amount_original` Monetary “Total amount original” (related=expense_id.total_amount)
- `total_amount_taxes` Monetary “Taxes” (compute=_compute_total_amount_taxes)
- `split_possible` Boolean (compute=_compute_split_possible)
- `currency_id` Many2one → `res.currency` (related=expense_id.currency_id)

Public methods: `action_split_expense`
