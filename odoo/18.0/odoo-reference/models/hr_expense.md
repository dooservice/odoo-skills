# hr_expense — Expenses

Depends on: account, web_tour, hr.

## `account.move` (extends)

- `expense_sheet_id` Many2one → `hr.expense.sheet`
- `show_commercial_partner_warning` Boolean (compute=_compute_show_commercial_partner_warning)

Public methods: `action_open_expense_report`, `button_cancel`

Extension points: `_check_journal_move_type`, `_prepare_product_base_line_for_taxes_computation`

## `account.move.line` (extends)

- `expense_id` Many2one → `hr.expense` “Expense”

Extension points: `_check_payable_receivable`, `_get_attachment_by_record`, `_get_attachment_domains`, `_get_extra_query_base_tax_line_mapping`

## `account.payment` (extends)

- `expense_sheet_id` Many2one (related=move_id.expense_sheet_id)

Public methods: `action_open_expense_report`, `write`

## `account.tax` (extends)

- `hr_expense_ids` Many2many → `hr.expense` (readonly)

Extension points: `_prepare_base_line_for_taxes_computation`, `_prepare_base_line_grouping_key`, `_prepare_tax_line_for_taxes_computation`, `_prepare_tax_line_repartition_grouping_key`

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection

## `account.analytic.account` (extends)


## `hr.department` (extends)

- `expense_sheets_to_approve_count` Integer “Expenses Reports to Approve” (compute=_compute_expense_sheets_to_approve)

## `hr.employee.base` (extends)

- `filter_for_expense` Boolean

Extension points: `_get_expense_managers`

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

Inherits: `mail.thread.main.attachment`, `mail.activity.mixin`, `analytic.mixin`

- `name` Char “Description” (required, store, compute=_compute_name)
- `date` Date “Expense Date”
- `employee_id` Many2one → `hr.employee` “Employee” (required, store, compute=_compute_employee_id)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `product_id` Many2one → `product.product` “Category”
- `product_description` Html (compute=_compute_product_description)
- `product_uom_id` Many2one → `uom.uom` “Unit of Measure” (store, compute=_compute_uom_id)
- `product_uom_category_id` Many2one → `uom.category` “UoM Category” (readonly, related=product_id.uom_id.category_id)
- `product_has_cost` Boolean (compute=_compute_from_product)
- `product_has_tax` Boolean “Whether tax is defined on a selected product” (compute=_compute_from_product)
- `quantity` Float (required)
- `description` Text “Internal Notes”
- `message_main_attachment_checksum` Char (related=message_main_attachment_id.checksum)
- `nb_attachment` Integer “Number of Attachments” (compute=_compute_nb_attachment)
- `attachment_ids` One2many → `ir.attachment` “Attachments”
- `state` Selection “Status” (readonly, store, index, compute=_compute_state)
- `sheet_id` Many2one → `hr.expense.sheet` “Expense Report” (readonly, index)
- `approved_by` Many2one → `res.users` “Approved By” (related=sheet_id.user_id)
- `approved_on` Datetime “Approved On” (related=sheet_id.approval_date)
- `duplicate_expense_ids` Many2many → `hr.expense` (compute=_compute_duplicate_expense_ids)
- `same_receipt_expense_ids` Many2many → `hr.expense` (compute=_compute_same_receipt_expense_ids)
- `tax_amount_currency` Monetary “Tax amount in Currency” (store, compute=_compute_tax_amount_currency)
- `tax_amount` Monetary “Tax amount” (store, compute=_compute_tax_amount)
- `total_amount_currency` Monetary “Total In Currency” (store, compute=_compute_total_amount_currency)
- `untaxed_amount_currency` Monetary “Total Untaxed Amount In Currency” (store, compute=_compute_tax_amount_currency)
- `total_amount` Monetary “Total” (store, compute=_compute_total_amount)
- `price_unit` Float “Unit Price” (required, readonly, store, compute=_compute_price_unit)
- `currency_id` Many2one → `res.currency` “Currency” (required, store, compute=_compute_currency_id)
- `company_currency_id` Many2one → `res.currency` “Report Company Currency” (readonly, related=company_id.currency_id)
- `is_multiple_currency` Boolean “Is currency_id different from the company_currency_id” (compute=_compute_is_multiple_currency)
- `currency_rate` Float (readonly, compute=_compute_currency_rate)
- `label_currency_rate` Char (readonly, compute=_compute_currency_rate)
- `payment_mode` Selection “Paid By” (required)
- `vendor_id` Many2one → `res.partner` “Vendor”
- `account_id` Many2one → `account.account` “Account” (store, compute=_compute_account_id)
- `tax_ids` Many2many → `account.tax` “Included taxes” (store, compute=_compute_tax_ids)
- `accounting_date` Date “Accounting Date” (store, related=sheet_id.accounting_date)
- `is_editable` Boolean “Is Editable By Current User” (compute=_compute_is_editable)

Public methods: `action_approve_duplicates`, `action_get_attachment_view`, `action_show_same_receipt_expense_ids`, `action_split_wizard`, `action_submit_expenses`, `action_view_sheet`, `attach_document`, `check_amount_not_zero`, `create`, `create_expense_from_attachments`, `get_empty_list_help`, `get_expense_attachments`, `get_expense_dashboard`, `get_expenses_to_submit`, `message_new`, `unlink`, `write`

Extension points: `_check_payment_mode`, `_create_sheets_from_expense`, `_get_base_account`, `_get_default_expense_sheet_values`, `_get_employee_from_email`, `_get_empty_list_mail_alias`, `_get_move_line_name`, `_get_split_values`, `_prepare_base_line_for_taxes_computation`, `_prepare_move_lines_vals`, `_prepare_payments_vals`

## `hr.expense.sheet` (defines)

Expense Report

Inherits: `mail.thread.main.attachment`, `mail.activity.mixin`

- `name` Char “Expense Report Summary” (required)
- `expense_line_ids` One2many → `hr.expense` “Expense Lines”
- `nb_expense` Integer “Number of Expenses” (compute=_compute_nb_expense)
- `state` Selection “Status” (required, readonly, store, index, compute=_compute_state)
- `approval_state` Selection
- `approval_date` Datetime “Approval Date” (readonly)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `employee_id` Many2one → `hr.employee` “Employee” (required, readonly)
- `department_id` Many2one → `hr.department` “Department” (store, related=employee_id.department_id)
- `user_id` Many2one → `res.users` “Manager” (readonly, store, compute=_compute_from_employee_id)
- `product_ids` Many2many → `product.product` “Categories” (compute=_compute_product_ids)
- `total_amount` Monetary “Total” (readonly, store, compute=_compute_amount)
- `untaxed_amount` Monetary “Untaxed Amount” (readonly, store, compute=_compute_amount)
- `total_tax_amount` Monetary “Taxes” (readonly, store, compute=_compute_amount)
- `amount_residual` Monetary “Amount Due” (readonly, store, compute=_compute_from_account_move_ids)
- `currency_id` Many2one → `res.currency` “Currency” (readonly, store, compute=_compute_currency_id)
- `company_currency_id` Many2one → `res.currency` “Report Company Currency” (related=company_id.currency_id)
- `is_multiple_currency` Boolean “Handle lines with different currencies” (compute=_compute_is_multiple_currency)
- `payment_state` Selection “Payment Status” (readonly, store, compute=_compute_from_account_move_ids)
- `payment_mode` Selection “Paid By” (readonly, related=expense_line_ids.payment_mode)
- `employee_journal_id` Many2one → `account.journal` “Journal”
- `selectable_payment_method_line_ids` Many2many → `account.payment.method.line` (compute=_compute_selectable_payment_method_line_ids)
- `payment_method_line_id` Many2one → `account.payment.method.line` “Payment Method” (store, compute=_compute_payment_method_line_id)
- `attachment_ids` One2many → `ir.attachment` “Attachments of expenses”
- `message_main_attachment_id` Many2one (store, compute=_compute_main_attachment)
- `accounting_date` Date “Expense Report Date”
- `account_move_ids` One2many → `account.move` “Journal Entries” (readonly)
- `nb_account_move` Integer “Number of Journal Entries” (compute=_compute_nb_account_move)
- `journal_id` Many2one → `account.journal` “Expense Journal” (store, compute=_compute_journal_id)
- `can_reset` Boolean “Can Reset” (compute=_compute_can_reset)
- `can_approve` Boolean “Can Approve” (compute=_compute_can_approve)
- `cannot_approve_reason` Char “Cannot Approve Reason” (compute=_compute_can_approve)
- `is_editable` Boolean “Expense Lines Are Editable By Current User” (compute=_compute_is_editable)

Public methods: `action_approve_expense_sheets`, `action_open_account_moves`, `action_open_expense_view`, `action_refuse_expense_sheets`, `action_register_payment`, `action_reset_expense_sheets`, `action_sheet_move_post`, `action_submit_sheet`, `activity_update`, `create`, `set_to_paid`, `set_to_posted`, `write`

Extension points: `_check_can_approve`, `_check_can_create_move`, `_check_can_refuse`, `_check_can_reset_approval`, `_check_employee`, `_check_expense_lines_company`, `_check_payment_mode`, `_get_default_sheet_name`, `_get_expense_account_destination`, `_get_responsible_for_approval`, `_prepare_bills_vals`, `_prepare_move_vals`

## `ir.actions.report` (extends)


## `ir.attachment` (extends)


Public methods: `create`, `unlink`

## `product.product` (extends)

- `standard_price_update_warning` Char (compute=_compute_standard_price_update_warning)

Public methods: `write`

## `product.template` (extends)

- `can_be_expensed` Boolean “Expenses” (store, compute=_compute_can_be_expensed)

Public methods: `default_get`

## `res.company` (extends)

- `expense_journal_id` Many2one → `account.journal` “Default Expense Journal”
- `expense_outstanding_account_id` Many2one → `account.account` “Outstanding Account”
- `company_expense_allowed_payment_method_line_ids` Many2many → `account.payment.method.line` “Payment methods available for expenses paid by company”

## `res.config.settings` (extends)

- `hr_expense_alias_prefix` Char “Default Alias Name for Expenses” (store, compute=_compute_hr_expense_alias_prefix)
- `hr_expense_alias_domain_id` Many2one → `mail.alias.domain` (compute=_compute_hr_expense_alias_domain_id)
- `hr_expense_use_mailgateway` Boolean “Let your employees record expenses by email”
- `module_hr_payroll_expense` Boolean “Reimburse Expenses in Payslip”
- `module_hr_expense_extract` Boolean “Send bills to OCR to generate expenses”
- `expense_journal_id` Many2one → `account.journal` (related=company_id.expense_journal_id)
- `expense_outstanding_account_id` Many2one → `account.account` (related=company_id.expense_outstanding_account_id)
- `company_expense_allowed_payment_method_line_ids` Many2many → `account.payment.method.line` (related=company_id.company_expense_allowed_payment_method_line_ids)

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
- `sheet_ids` Many2many → `hr.expense.sheet`

Public methods: `action_refuse`, `default_get`

## `hr.expense.split` (defines)

Expense Split

Inherits: `analytic.mixin`

- `name` Char “Description” (required)
- `wizard_id` Many2one → `hr.expense.split.wizard`
- `expense_id` Many2one → `hr.expense` “Expense”
- `product_id` Many2one → `product.product` “Product” (required)
- `tax_ids` Many2many → `account.tax`
- `total_amount_currency` Monetary “Total In Currency” (required, store, compute=_compute_from_product_id)
- `tax_amount_currency` Monetary “Tax amount in Currency” (compute=_compute_tax_amount_currency)
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
- `total_amount_currency` Monetary “Total Amount” (compute=_compute_total_amount_currency)
- `total_amount_currency_original` Monetary “Total amount original” (related=expense_id.total_amount_currency)
- `tax_amount_currency` Monetary “Taxes” (compute=_compute_tax_amount_currency)
- `split_possible` Boolean (compute=_compute_split_possible)
- `currency_id` Many2one → `res.currency` (related=expense_id.currency_id)

Public methods: `action_split_expense`
