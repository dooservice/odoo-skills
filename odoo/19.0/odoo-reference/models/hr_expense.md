# hr_expense — Expenses

Depends on: account, web_tour, hr.

## `account.move` (extends)

- `expense_ids` One2many → `hr.expense`
- `nb_expenses` Integer “Number of Expenses” (compute=_compute_nb_expenses)

Public methods: `action_open_expense`, `button_cancel`

Extension points: `_check_expense_ids`, `_check_journal_move_type`, `_prepare_product_base_line_for_taxes_computation`

## `account.move.line` (extends)

- `expense_id` Many2one → `hr.expense` “Expense”

Extension points: `_check_payable_receivable`, `_get_attachment_by_record`, `_get_attachment_domains`, `_get_extra_query_base_tax_line_mapping`

## `account.payment` (extends)

- `expense_ids` One2many (related=move_id.expense_ids)

Public methods: `action_open_expense`, `write`

## `account.tax` (extends)

- `hr_expense_ids` Many2many → `hr.expense` (readonly)

Extension points: `_prepare_base_line_for_taxes_computation`, `_prepare_base_line_grouping_key`, `_prepare_tax_line_for_taxes_computation`, `_prepare_tax_line_repartition_grouping_key`

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection

## `account.analytic.account` (extends)


## `hr.department` (extends)

- `expenses_to_approve_count` Integer “Expenses to Approve” (compute=_compute_expenses_to_approve_count)

## `hr.employee` (extends)

- `expense_manager_id` Many2one → `res.users` “Expense Approver” (store, compute=_compute_expense_manager)
- `filter_for_expense` Boolean

Extension points: `_get_expense_managers`, `_get_user_m2o_to_empty_on_archived_employees`

## `hr.employee.public` (extends)

- `expense_manager_id` Many2one → `res.users` (readonly)

## `hr.employee.public` (extends)

- `filter_for_expense` Boolean

## `hr.expense` (defines)

Expense

Inherits: `mail.thread.main.attachment`, `mail.activity.mixin`, `analytic.mixin`

- `name` Char “Description” (required, store, compute=_compute_name)
- `date` Date “Expense Date”
- `employee_id` Many2one → `hr.employee` “Employee” (required, store, index, compute=_compute_employee_id)
- `department_id` Many2one → `hr.department` “Department” (store, compute=_compute_from_employee_id)
- `manager_id` Many2one → `res.users` “Manager” (store, compute=_compute_from_employee_id)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `product_id` Many2one → `product.product` “Category”
- `product_description` Html (compute=_compute_product_description)
- `product_uom_id` Many2one → `uom.uom` “Unit” (store, compute=_compute_uom_id)
- `product_has_cost` Boolean (compute=_compute_from_product)
- `product_has_tax` Boolean “Whether tax is defined on a selected product” (compute=_compute_from_product)
- `quantity` Float (required)
- `description` Text “Internal Notes”
- `message_main_attachment_checksum` Char (related=message_main_attachment_id.checksum)
- `nb_attachment` Integer “Number of Attachments” (compute=_compute_nb_attachment)
- `attachment_ids` One2many → `ir.attachment` “Attachments”
- `state` Selection “Status” (readonly, store, index, compute=_compute_state)
- `approval_state` Selection (readonly)
- `approval_date` Datetime “Approval Date” (readonly)
- `duplicate_expense_ids` Many2many → `hr.expense` (compute=_compute_duplicate_expense_ids)
- `same_receipt_expense_ids` Many2many → `hr.expense` (compute=_compute_same_receipt_expense_ids)
- `split_expense_origin_id` Many2one → `hr.expense` “Origin Split Expense”
- `tax_amount_currency` Monetary “Tax amount in Currency” (store, compute=_compute_tax_amount_currency)
- `tax_amount` Monetary “Tax amount” (store, compute=_compute_tax_amount)
- `total_amount_currency` Monetary “Total In Currency” (store, compute=_compute_total_amount_currency)
- `total_amount` Monetary “Total” (store, compute=_compute_total_amount)
- `untaxed_amount_currency` Monetary “Total Untaxed Amount In Currency” (store, compute=_compute_tax_amount_currency)
- `untaxed_amount` Monetary “Total Untaxed Amount” (store, compute=_compute_tax_amount)
- `amount_residual` Monetary “Amount Due” (readonly, related=account_move_id.amount_residual)
- `price_unit` Float “Unit Price” (required, readonly, store, compute=_compute_price_unit)
- `currency_id` Many2one → `res.currency` “Currency” (required, store, compute=_compute_currency_id)
- `company_currency_id` Many2one → `res.currency` “Report Company Currency” (readonly, related=company_id.currency_id)
- `is_multiple_currency` Boolean “Is currency_id different from the company_currency_id” (compute=_compute_is_multiple_currency)
- `currency_rate` Float (readonly, compute=_compute_currency_rate)
- `label_currency_rate` Char (readonly, compute=_compute_currency_rate)
- `journal_id` Many2one → `account.journal` (readonly, related=payment_method_line_id.journal_id)
- `selectable_payment_method_line_ids` Many2many → `account.payment.method.line` (compute=_compute_selectable_payment_method_line_ids)
- `payment_method_line_id` Many2one → `account.payment.method.line` “Payment Method” (store, compute=_compute_payment_method_line_id)
- `account_move_id` Many2one → `account.move` “Journal Entry” (readonly)
- `payment_mode` Selection “Paid By” (required)
- `vendor_id` Many2one → `res.partner` “Vendor”
- `account_id` Many2one → `account.account` “Account” (store, compute=_compute_account_id)
- `tax_ids` Many2many → `account.tax` “Included taxes” (store, compute=_compute_tax_ids)
- `is_editable` Boolean “Is Editable By Current User” (readonly, compute=_compute_is_editable)
- `can_reset` Boolean “Can Reset” (readonly, compute=_compute_can_reset)
- `can_approve` Boolean “Can Approve” (readonly, compute=_compute_can_approve)
- `former_sheet_id` Integer “Former Report”

Public methods: `action_approve`, `action_approve_duplicates`, `action_open_account_move`, `action_open_split_expense`, `action_pay`, `action_post`, `action_refuse`, `action_reset`, `action_show_same_receipt_expense_ids`, `action_split_wizard`, `action_submit`, `attach_document`, `create`, `create_expense_from_attachments`, `get_empty_list_help`, `get_expense_dashboard`, `message_new`, `update_activities_and_mails`, `write`

Extension points: `_check_can_approve`, `_check_can_create_move`, `_check_can_refuse`, `_check_can_reset_approval`, `_check_non_zero`, `_check_o2o_payment`, `_create_company_paid_moves`, `_get_base_account`, `_get_cannot_approve_reason`, `_get_default_responsible_for_approval`, `_get_employee_from_email`, `_get_empty_list_mail_alias`, `_get_expense_account_destination`, `_get_move_line_name`, `_get_outstanding_account_id`, `_get_split_values`, `_get_untitled_expense_name`, `_post_without_wizard`, `_post_wizard`, `_prepare_base_line_for_taxes_computation`, `_prepare_move_lines_vals`, `_prepare_move_vals`, `_prepare_payments_vals`, `_prepare_receipts_vals`

## `ir.actions.report` (extends)


## `ir.attachment` (extends)


Public methods: `create`

## `product.product` (extends)

- `standard_price_update_warning` Char (compute=_compute_standard_price_update_warning)

Public methods: `write`

## `product.template` (extends)

- `can_be_expensed` Boolean “Expenses” (store, compute=_compute_can_be_expensed)

Public methods: `default_get`

## `res.company` (extends)

- `expense_journal_id` Many2one → `account.journal` “Default Expense Journal”
- `company_expense_allowed_payment_method_line_ids` Many2many → `account.payment.method.line` “Payment methods available for expenses paid by company”

## `res.config.settings` (extends)

- `hr_expense_alias_prefix` Char “Default Alias Name for Expenses” (store, compute=_compute_hr_expense_alias_prefix)
- `hr_expense_alias_domain_id` Many2one → `mail.alias.domain` (compute=_compute_hr_expense_alias_domain_id)
- `hr_expense_use_mailgateway` Boolean “Let your employees record expenses by email”
- `module_hr_payroll_expense` Boolean “Reimburse Expenses in Payslip”
- `module_hr_expense_extract` Boolean “Send bills to OCR to generate expenses”
- `module_hr_expense_stripe` Boolean “Link your stripe issuing account to manage company credit cards for your employees through Odoo”
- `expense_journal_id` Many2one → `account.journal` (related=company_id.expense_journal_id)
- `company_expense_allowed_payment_method_line_ids` Many2many → `account.payment.method.line` (related=company_id.company_expense_allowed_payment_method_line_ids)

Public methods: `get_values`, `set_values`

## `account.payment.register` (extends)


Extension points: `_get_line_batch_key`

## `hr.expense.approve.duplicate` (defines)

Expense Approve Duplicate

- `expense_ids` Many2many → `hr.expense` (readonly)

Public methods: `action_approve`, `action_refuse`, `default_get`

## `hr.expense.post.wizard` (defines)

Expense Posting Wizard

- `company_id` Many2one → `res.company` “Company” (readonly)
- `accounting_date` Date “Accounting Date”
- `employee_journal_id` Many2one → `account.journal` “Journal”

Public methods: `action_post_entry`

## `hr.expense.refuse.wizard` (defines)

Expense Refuse Reason Wizard

- `reason` Char “Reason” (required)
- `expense_ids` Many2many → `hr.expense`

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
- `approval_state` Selection (readonly)
- `approval_date` Datetime “Approval Date” (readonly)
- `manager_id` Many2one → `res.users` “Manager” (readonly)

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
