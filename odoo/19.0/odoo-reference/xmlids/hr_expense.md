# hr_expense — XML ids

## digest.tip

- `hr_expense.digest_tip_hr_expense_0`

## ir.actions.act_window

- `hr_expense.hr_expense_refuse_wizard_action`
- `hr_expense.hr_expense_approve_duplicate_action`
- `hr_expense.hr_expense_product`
- `hr_expense.hr_expense_actions_my_all`
- `hr_expense.hr_expense_actions_to_process`
- `hr_expense.hr_expense_actions_all`
- `hr_expense.action_hr_expense_account`
- `hr_expense.action_hr_expense_department_to_approve`
- `hr_expense.action_hr_expense_department_filtered`
- `hr_expense.mail_activity_type_action_config_hr_expense`
- `hr_expense.action_hr_expense_configuration`

## ir.actions.act_window.view

- `hr_expense.hr_expense_product_tree`
- `hr_expense.hr_expense_product_kanban`
- `hr_expense.hr_expense_product_form`
- `hr_expense.hr_expense_actions_my_all_tree`
- `hr_expense.hr_expense_actions_my_all_kanban`
- `hr_expense.hr_expense_actions_all_graph`
- `hr_expense.hr_expense_actions_all_pivot`
- `hr_expense.hr_expense_actions_all_tree`

## ir.actions.report

- `hr_expense.action_report_hr_expense`
- `hr_expense.action_report_expense_img`

## ir.cron

- `hr_expense.ir_cron_send_submitted_expenses_mail`

## ir.rule

- `hr_expense.ir_rule_hr_expense_manager`
- `hr_expense.ir_rule_hr_expense_approver`
- `hr_expense.ir_rule_hr_expense_employee`
- `hr_expense.ir_rule_hr_expense_employee_not_draft`
- `hr_expense.hr_expense_comp_rule`
- `hr_expense.hr_expense_team_approver_account_move_rule`
- `hr_expense.hr_expense_team_approver_account_move_line_rule`
- `hr_expense.ir_rule_hr_expense_split_employee`
- `hr_expense.ir_rule_hr_expense_split_approver`
- `hr_expense.ir_rule_hr_expense_split_user`
- `hr_expense.ir_rule_hr_expense_split_manager`
- `hr_expense.ir_rule_hr_expense_split_accountant`

## ir.sequence

- `hr_expense.seq_hr_expense_invoice`

## ir.ui.menu

- `hr_expense.menu_hr_expense_root` — Expenses
- `hr_expense.menu_hr_expense_my_expenses` — My Expenses
- `hr_expense.menu_hr_expense_my_expenses_all` — My Expenses
- `hr_expense.menu_hr_expense_expenses_to_process` — Expenses to Process
- `hr_expense.menu_hr_expense_reports` — Reporting
- `hr_expense.menu_hr_expense_all_expenses` — Expenses Analysis
- `hr_expense.menu_hr_expense_configuration` — Configuration
- `hr_expense.menu_hr_product` — Expense Categories
- `hr_expense.menu_hr_expense_account_employee_expenses` — Employee Expenses
- `hr_expense.hr_expense_menu_config_activity_type`
- `hr_expense.menu_hr_expense_global_settings` — Settings

## ir.ui.view

- `hr_expense.hr_expense_template_refuse_reason`
- `hr_expense.hr_expense_template_register`
- `hr_expense.hr_expense_template_submitted_expenses`
- `hr_expense.hr_expense_template_register_no_user`
- `hr_expense.hr_expense_refuse_wizard_view_form` — on hr.expense.refuse.wizard
- `hr_expense.hr_expense_approve_duplicate_view_form` — on hr.expense.approve.duplicate
- `hr_expense.hr_expense_split` — on hr.expense.split.wizard
- `hr_expense.hr_expense_post_wizard_view` — on hr.expense.post.wizard
- `hr_expense.view_product_hr_expense_form` — on product.template inherits product.product_template_form_view
- `hr_expense.product_template_search_view_inherit_hr_expense` — on product.template inherits product.product_template_search_view
- `hr_expense.product_product_expense_form_view` — on product.product
- `hr_expense.product_product_expense_kanban_view` — on product.product inherits product.product_kanban_view
- `hr_expense.product_product_expense_tree_view` — on product.product
- `hr_expense.product_product_expense_categories_tree_view` — on product.product
- `hr_expense.hr_expense_view_expenses_analysis_tree` — on hr.expense
- `hr_expense.view_expenses_tree` — on hr.expense inherits hr_expense_view_expenses_analysis_tree
- `hr_expense.view_my_expenses_tree` — on hr.expense inherits hr_expense.view_expenses_tree
- `hr_expense.hr_expense_view_form` — on hr.expense
- `hr_expense.hr_expense_view_form_without_header` — on hr.expense inherits hr_expense.hr_expense_view_form
- `hr_expense.hr_expense_view_expenses_analysis_kanban` — on hr.expense
- `hr_expense.hr_expense_kanban_view_minimal` — on hr.expense inherits hr_expense_view_expenses_analysis_kanban
- `hr_expense.hr_expense_kanban_view` — on hr.expense inherits hr_expense_view_expenses_analysis_kanban
- `hr_expense.hr_expense_kanban_view_header` — on hr.expense inherits hr_expense_view_expenses_analysis_kanban
- `hr_expense.hr_expense_view_pivot` — on hr.expense
- `hr_expense.hr_expense_view_graph` — on hr.expense
- `hr_expense.hr_expense_view_search` — on hr.expense
- `hr_expense.hr_expense_view_activity` — on hr.expense
- `hr_expense.hr_expense_view_search_with_panel` — on hr.expense inherits hr_expense_view_search
- `hr_expense.report_expense`
- `hr_expense.report_expense_img`
- `hr_expense.view_move_form_inherit_expense` — on account.move inherits account.view_move_form
- `hr_expense.view_move_list_expense` — on account.move
- `hr_expense.view_payment_form_inherit_expense` — on account.payment inherits account.view_account_payment_form
- `hr_expense.hr_department_view_kanban` — on hr.department inherits hr.hr_department_view_kanban
- `hr_expense.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form
- `hr_expense.hr_employee_view_form_inherit_expense` — on hr.employee inherits hr.view_employee_form
- `hr_expense.view_employee_tree_inherit_expense` — on hr.employee inherits hr.view_employee_tree
- `hr_expense.hr_employee_search_view` — on hr.employee inherits hr.view_employee_filter

## mail.activity.type

- `hr_expense.mail_act_expense_approval`

## mail.alias

- `hr_expense.mail_alias_expense`

## mail.message.subtype

- `hr_expense.mt_expense_approved`
- `hr_expense.mt_expense_refused`
- `hr_expense.mt_expense_paid`
- `hr_expense.mt_expense_reset`
- `hr_expense.mt_expense_entry_delete`
- `hr_expense.mt_expense_entry_draft`

## product.product

- `hr_expense.expense_product_meal`
- `hr_expense.expense_product_travel_accommodation`
- `hr_expense.expense_product_mileage`
- `hr_expense.expense_product_gift`
- `hr_expense.expense_product_communication`
- `hr_expense.product_product_no_cost`

## res.groups

- `hr_expense.group_hr_expense_team_approver`
- `hr_expense.group_hr_expense_user`
- `hr_expense.group_hr_expense_manager`

## res.groups.privilege

- `hr_expense.res_groups_privilege_expenses`

## uom.uom

- `uom.product_uom_km`

## web_tour.tour

- `hr_expense.hr_expense_tour`
