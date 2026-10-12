# sale_timesheet — XML ids

## ir.actions.act_window

- `sale_timesheet.timesheet_action_billing_report`
- `sale_timesheet.action_timesheet_from_invoice`
- `sale_timesheet.product_template_action_default_services`
- `sale_timesheet.timesheet_action_from_sales_order`
- `sale_timesheet.timesheet_action_from_sales_order_item`
- `sale_timesheet.timesheet_action_plan_pivot`
- `sale_timesheet.timesheet_action_from_plan`
- `sale_timesheet.project_project_action_multi_create_sale_order`
- `sale_timesheet.project_project_action_multi_create_invoice`

## ir.actions.act_window.view

- `sale_timesheet.timesheet_action_view_report_by_billing_rate_pivot`
- `sale_timesheet.timesheet_action_view_report_by_billing_rate_graph`
- `sale_timesheet.action_timesheet_from_invoice_view_tree`
- `sale_timesheet.action_timesheet_from_invoice_view_form`
- `sale_timesheet.action_timesheet_from_invoice_view_kanban`
- `sale_timesheet.action_timesheet_from_invoice_view_pivot`
- `sale_timesheet.action_timesheet_from_invoice_view_graph`
- `sale_timesheet.timesheet_action_from_sales_order_tree`
- `sale_timesheet.timesheet_action_from_sales_order_form`
- `sale_timesheet.timesheet_action_from_sales_order_item_tree`
- `sale_timesheet.timesheet_action_from_sales_order_item_kanban`
- `sale_timesheet.timesheet_action_from_sales_order_item_pivot`
- `sale_timesheet.timesheet_action_from_sales_order_item_graph`
- `sale_timesheet.timesheet_action_from_sales_order_item_form`

## ir.actions.report

- `sale_timesheet.timesheet_report_sale_order`
- `sale_timesheet.timesheet_report_account_move`

## ir.rule

- `account.account_analytic_line_rule_readonly_user`
- `account.account_analytic_line_rule_billing_user`

## ir.ui.menu

- `sale_timesheet.menu_timesheet_billing_analysis` — By Billing Type

## ir.ui.view

- `sale_timesheet.timesheets_analysis_report_pivot_inherit` — on timesheets.analysis.report inherits hr_timesheet.timesheets_analysis_report_pivot_employee
- `sale_timesheet.timesheets_analysis_report_graph_inherit` — on timesheets.analysis.report inherits hr_timesheet.timesheets_analysis_report_pivot_employee
- `sale_timesheet.timesheets_analysis_report_graph_timesheet_grid` — on timesheets.analysis.report inherits hr_timesheet.timesheets_analysis_report_graph_employee
- `sale_timesheet.timesheets_analysis_report_pivot_project_inherit` — on timesheets.analysis.report inherits hr_timesheet.timesheets_analysis_report_pivot_project
- `sale_timesheet.timesheets_analysis_report_graph_project_inherit` — on timesheets.analysis.report inherits hr_timesheet.timesheets_analysis_report_graph_project
- `sale_timesheet.timesheets_analysis_report_pivot_task_inherit` — on timesheets.analysis.report inherits hr_timesheet.timesheets_analysis_report_pivot_task
- `sale_timesheet.timesheets_analysis_report_graph_task_inherit` — on timesheets.analysis.report inherits hr_timesheet.timesheets_analysis_report_graph_task
- `sale_timesheet.timesheets_analysis_report_pivot_invoice_type` — on timesheets.analysis.report
- `sale_timesheet.timesheets_analysis_report_graph_invoice_type` — on timesheets.analysis.report
- `sale_timesheet.hr_timesheet_report_search_sale_timesheet` — on timesheets.analysis.report inherits hr_timesheet.hr_timesheet_report_search
- `sale_timesheet.account_invoice_view_form_inherit_sale_timesheet` — on account.move inherits account.view_move_form
- `sale_timesheet.view_order_form_inherit_sale_timesheet` — on sale.order inherits sale_project.view_order_form_inherit_sale_project
- `sale_timesheet.view_product_timesheet_form` — on product.template inherits sale.product_template_form_view
- `sale_timesheet.product_template_view_search_sale_timesheet` — on product.template inherits product.product_template_search_view
- `sale_timesheet.project_project_view_form` — on project.project inherits hr_timesheet.project_invoice_form
- `sale_timesheet.project_project_view_form_simplified_inherit` — on project.project inherits hr_timesheet.project_project_view_form_simplified_inherit_timesheet
- `sale_timesheet.project_project_view_kanban_inherit_sale_timesheet` — on project.project inherits hr_timesheet.view_project_kanban_inherited
- `sale_timesheet.project_project_view_kanban_inherit_sale_timesheet_so_button` — on project.project inherits project.view_project_kanban
- `sale_timesheet.view_sale_service_inherit_form2` — on project.task inherits hr_timesheet.view_task_form2_inherited
- `sale_timesheet.view_task_tree2_inherited` — on project.task inherits hr_timesheet.view_task_tree2_inherited
- `sale_timesheet.project_task_view_form_inherit_sale_timesheet` — on project.task inherits project.view_task_form2
- `sale_timesheet.view_task_form2_inherit_sale_timesheet` — on project.task inherits sale_project.view_sale_project_inherit_form
- `sale_timesheet.project_update_default_description` — inherits project.project_update_default_description
- `sale_timesheet.timesheet_view_search` — on account.analytic.line inherits hr_timesheet.hr_timesheet_line_search
- `sale_timesheet.hr_timesheet_line_tree_inherit` — on account.analytic.line inherits hr_timesheet.hr_timesheet_line_tree
- `sale_timesheet.hr_timesheet_line_form_inherit` — on account.analytic.line inherits hr_timesheet.hr_timesheet_line_form
- `sale_timesheet.view_hr_timesheet_line_pivot_billing_rate` — on account.analytic.line
- `sale_timesheet.view_hr_timesheet_line_graph_employee_per_date` — on account.analytic.line
- `sale_timesheet.res_config_settings_view_form` — on res.config.settings inherits hr_timesheet.res_config_settings_view_form
- `sale_timesheet.sale_order_portal_content_inherit` — inherits sale.sale_order_portal_template
- `sale_timesheet.portal_my_timesheets_inherit` — inherits hr_timesheet.portal_my_timesheets
- `sale_timesheet.portal_invoice_page_inherit` — inherits account.portal_invoice_page
- `sale_timesheet.portal_my_task_inherit` — inherits project.portal_my_task
- `sale_timesheet.portal_timesheet_table_inherit` — inherits hr_timesheet.portal_timesheet_table
- `sale_timesheet.project_sharing_inherit_project_task_view_form` — on project.task inherits project.project_sharing_project_task_view_form
- `sale_timesheet.project_sharing_inherit_project_task_view_tree_sale_timesheet` — on project.task inherits hr_timesheet.project_sharing_inherit_project_task_view_tree
- `sale_timesheet.timesheet_sale_page`
- `sale_timesheet.report_timesheet_sale_order`
- `sale_timesheet.report_timesheet_account_move`
- `sale_timesheet.project_create_sale_order_view_form` — on project.create.sale.order
- `sale_timesheet.project_create_invoice_view_form` — on project.create.invoice
- `sale_timesheet.sale_advance_payment_inv_timesheet_view_form` — on sale.advance.payment.inv inherits sale.view_sale_advance_payment_inv

## product.product

- `sale_timesheet.time_product`

## res.groups

- `base.group_user`
