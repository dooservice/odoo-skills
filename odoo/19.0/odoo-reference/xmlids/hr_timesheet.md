# hr_timesheet — XML ids

## digest.tip

- `hr_timesheet.digest_tip_hr_timesheet_0`

## ir.actions.act_window

- `hr_timesheet.act_hr_timesheet_line`
- `hr_timesheet.timesheet_action_task`
- `hr_timesheet.timesheet_action_project`
- `hr_timesheet.timesheet_action_all`
- `hr_timesheet.timesheet_action_from_employee`
- `hr_timesheet.act_hr_timesheet_line_by_project`
- `hr_timesheet.hr_timesheet_config_settings_action`
- `project.open_view_project_all`
- `project.open_view_project_all_group_stage`
- `hr_timesheet.act_hr_timesheet_report`
- `hr_timesheet.timesheet_action_report_by_project`
- `hr_timesheet.timesheet_action_report_by_task`

## ir.actions.act_window.view

- `hr_timesheet.act_hr_timesheet_line_view_tree`
- `hr_timesheet.act_hr_timesheet_line_view_form`
- `hr_timesheet.act_hr_timesheet_line_view_calendar`
- `hr_timesheet.act_hr_timesheet_line_view_kanban`
- `hr_timesheet.act_hr_timesheet_line_view_pivot`
- `hr_timesheet.act_hr_timesheet_line_view_graph`
- `hr_timesheet.timesheet_action_view_all_tree`
- `hr_timesheet.timesheet_action_view_all_form`
- `hr_timesheet.timesheet_action_view_all_calendar`
- `hr_timesheet.timesheet_action_view_all_kanban`
- `hr_timesheet.timesheet_action_view_all_pivot`
- `hr_timesheet.timesheet_action_view_all_graph`
- `hr_timesheet.act_hr_timesheet_line_by_project_view_tree`
- `hr_timesheet.act_hr_timesheet_line_by_project_view_kanban`
- `hr_timesheet.act_hr_timesheet_line_by_project_view_pivot`
- `hr_timesheet.act_hr_timesheet_line_by_project_view_graph`
- `hr_timesheet.act_hr_timesheet_line_by_project_view_form`
- `hr_timesheet.act_hr_timesheet_report_pivot`
- `hr_timesheet.timesheet_action_view_report_by_employee_graph`
- `hr_timesheet.timesheet_action_view_report_by_employee_list`
- `hr_timesheet.timesheet_action_view_report_by_project_pivot`
- `hr_timesheet.timesheet_action_view_report_by_project_graph`
- `hr_timesheet.timesheet_action_view_report_by_project_list`
- `hr_timesheet.timesheet_action_view_report_by_task_pivot`
- `hr_timesheet.timesheet_action_view_report_by_task_graph`
- `hr_timesheet.timesheet_action_view_report_by_task_list`
- `hr_timesheet.timesheet_action_view_from_employee_form`

## ir.actions.report

- `hr_timesheet.timesheet_report`
- `hr_timesheet.timesheet_report_task`
- `hr_timesheet.timesheet_report_project`
- `hr_timesheet.timesheet_report_task_timesheets`

## ir.actions.server

- `hr_timesheet.unlink_employee_action`

## ir.embedded.actions

- `hr_timesheet.project_embedded_action_timesheets`
- `hr_timesheet.project_embedded_action_timesheets_dashboard`

## ir.exports

- `hr_timesheet.account_analytic_line_export_template`

## ir.exports.line

- `hr_timesheet.project_task_export_template_line_allocated_hours`
- `hr_timesheet.account_analytic_line_export_template_line_id`
- `hr_timesheet.account_analytic_line_export_template_line_date`
- `hr_timesheet.account_analytic_line_export_template_line_employee_id`
- `hr_timesheet.account_analytic_line_export_template_line_project_id`
- `hr_timesheet.account_analytic_line_export_template_line_task_id`
- `hr_timesheet.account_analytic_line_export_template_line_name`
- `hr_timesheet.account_analytic_line_export_template_line_unit_amount`

## ir.model.access

- `hr_timesheet.access_account_analytic_line_portal_user`

## ir.rule

- `hr_timesheet.timesheet_line_rule_portal_user`
- `hr_timesheet.timesheet_line_rule_user`
- `hr_timesheet.timesheet_line_rule_approver`
- `hr_timesheet.timesheet_line_rule_manager`
- `hr_timesheet.timesheets_analysis_report_comp_rule`
- `hr_timesheet.timesheet_analysis_report_department_manager`
- `hr_timesheet.timesheet_analysis_report_user`
- `hr_timesheet.timesheet_analysis_report_approver`
- `hr_timesheet.timesheet_analysis_report_manager`

## ir.ui.menu

- `hr_timesheet.timesheet_menu_root` — Timesheets
- `hr_timesheet.timesheet_menu_activity_user` — My Timesheets
- `hr_timesheet.menu_hr_time_tracking` — Timesheets
- `hr_timesheet.timesheet_menu_activity_mine` — My Timesheets
- `hr_timesheet.timesheet_menu_activity_all` — All Timesheets
- `hr_timesheet.menu_timesheets_reports` — Reporting
- `hr_timesheet.menu_timesheets_reports_timesheet` — Timesheets
- `hr_timesheet.menu_hr_activity_analysis` — By Employee
- `hr_timesheet.timesheet_menu_report_timesheet_by_project` — By Project
- `hr_timesheet.timesheet_menu_report_timesheet_by_task` — By Task
- `hr_timesheet.hr_timesheet_menu_configuration` — Configuration

## ir.ui.view

- `hr_timesheet.hr_timesheet_line_tree` — on account.analytic.line
- `hr_timesheet.hr_timesheet_line_portal_tree` — on account.analytic.line inherits hr_timesheet_line_tree
- `hr_timesheet.timesheet_view_tree_user` — on account.analytic.line inherits hr_timesheet_line_tree
- `hr_timesheet.view_hr_timesheet_line_pivot` — on account.analytic.line
- `hr_timesheet.view_my_timesheet_line_pivot` — on account.analytic.line
- `hr_timesheet.view_hr_timesheet_line_graph` — on account.analytic.line
- `hr_timesheet.view_hr_timesheet_line_graph_my` — on account.analytic.line
- `hr_timesheet.view_hr_timesheet_line_graph_all` — on account.analytic.line
- `hr_timesheet.view_hr_timesheet_line_by_project` — on account.analytic.line inherits hr_timesheet.view_hr_timesheet_line_graph_all
- `hr_timesheet.view_hr_timesheet_line_graph_by_employee` — on account.analytic.line inherits hr_timesheet.view_hr_timesheet_line_graph_all
- `hr_timesheet.hr_timesheet_line_form` — on account.analytic.line
- `hr_timesheet.timesheet_view_form_user` — on account.analytic.line inherits hr_timesheet.hr_timesheet_line_form
- `hr_timesheet.hr_timesheet_line_search` — on account.analytic.line inherits analytic.view_account_analytic_line_filter
- `hr_timesheet.timesheet_view_form_portal_user` — on account.analytic.line inherits hr_timesheet.timesheet_view_form_user
- `hr_timesheet.hr_timesheet_line_my_timesheet_search` — on account.analytic.line inherits hr_timesheet_line_search
- `hr_timesheet.view_kanban_account_analytic_line` — on account.analytic.line
- `hr_timesheet.view_calendar_account_analytic_line` — on account.analytic.line
- `hr_timesheet.view_calendar_account_analytic_line_multi_create` — on account.analytic.line
- `hr_timesheet.view_calendar_account_analytic_line_my_timesheets` — on account.analytic.line inherits hr_timesheet.view_calendar_account_analytic_line
- `hr_timesheet.view_kanban_account_analytic_line_portal_user` — on account.analytic.line inherits hr_timesheet.view_kanban_account_analytic_line
- `hr_timesheet.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form
- `hr_timesheet.project_project_view_form_simplified_inherit_timesheet` — on project.project inherits project.project_project_view_form_simplified
- `hr_timesheet.project_invoice_form` — on project.project inherits project.edit_project
- `hr_timesheet.project_project_view_tree_inherit_sale_project` — on project.project inherits project.view_project
- `hr_timesheet.view_project_kanban_inherited` — on project.project inherits project.view_project_kanban
- `hr_timesheet.view_project_project_filter_inherit_timesheet` — on project.project inherits project.view_project_project_filter
- `hr_timesheet.project_templates_view_list_inherit_timesheet` — on project.project inherits project.project_templates_view_list
- `hr_timesheet.view_task_form2_inherited` — on project.task inherits project.view_task_form2
- `hr_timesheet.view_task_tree2_inherited` — on project.task inherits project.project_task_view_tree_main_base
- `hr_timesheet.view_task_kanban_inherited_progress` — on project.task inherits project.view_task_kanban
- `hr_timesheet.project_task_view_search` — on project.task inherits project.view_task_search_form_project_fsm_base
- `hr_timesheet.project_task_view_graph` — on project.task inherits project.view_project_task_graph
- `hr_timesheet.project_task_view_pivot` — on project.task inherits project.view_project_task_pivot
- `hr_timesheet.portal_my_task` — inherits project.portal_my_task
- `hr_timesheet.portal_my_task_allocated_hours_template`
- `hr_timesheet.portal_tasks_list_inherit` — inherits project.portal_tasks_list
- `hr_timesheet.portal_layout` — inherits portal.portal_breadcrumbs
- `hr_timesheet.portal_my_home_timesheet` — inherits portal.portal_my_home
- `hr_timesheet.portal_my_timesheets`
- `hr_timesheet.portal_timesheet_table`
- `hr_timesheet.timesheets_analysis_report_list` — on timesheets.analysis.report
- `hr_timesheet.timesheets_analysis_report_form` — on timesheets.analysis.report
- `hr_timesheet.timesheets_analysis_report_pivot_employee` — on timesheets.analysis.report
- `hr_timesheet.timesheets_analysis_report_graph_employee` — on timesheets.analysis.report
- `hr_timesheet.timesheets_analysis_report_pivot_project` — on timesheets.analysis.report
- `hr_timesheet.timesheets_analysis_report_graph_project` — on timesheets.analysis.report
- `hr_timesheet.timesheets_analysis_report_pivot_task` — on timesheets.analysis.report
- `hr_timesheet.timesheets_analysis_report_graph_task` — on timesheets.analysis.report
- `hr_timesheet.hr_timesheet_report_search` — on timesheets.analysis.report inherits hr_timesheet.hr_timesheet_line_search
- `hr_timesheet.view_task_project_user_graph_inherited` — on report.project.task.user inherits project.view_task_project_user_graph
- `hr_timesheet.view_task_project_user_pivot_inherited` — on report.project.task.user inherits project.view_task_project_user_pivot
- `hr_timesheet.timesheet_table`
- `hr_timesheet.timesheet_project_task_page`
- `hr_timesheet.timesheet_report_subtask`
- `hr_timesheet.report_timesheet`
- `hr_timesheet.report_timesheet_task`
- `hr_timesheet.report_project_task_timesheet`
- `hr_timesheet.report_timesheet_project`
- `hr_timesheet.hr_department_view_kanban` — on hr.department inherits hr.hr_department_view_kanban
- `hr_timesheet.hr_employee_view_form_inherit_timesheet` — on hr.employee inherits hr_hourly_cost.view_employee_form
- `hr_timesheet.view_employee_tree_inherit_timesheet` — on hr.employee inherits hr.view_employee_tree
- `hr_timesheet.hr_employee_view_kanban_inherit_timesheet` — on hr.employee inherits hr.hr_kanban_view_employees
- `hr_timesheet.hr_employee_public_view_form` — on hr.employee.public inherits hr.hr_employee_public_view_form
- `hr_timesheet.project_sharing_inherit_project_task_view_form` — on project.task inherits project.project_sharing_project_task_view_form
- `hr_timesheet.project_sharing_kanban_inherit_project_task_view_kanban` — on project.task inherits project.project_sharing_project_task_view_kanban
- `hr_timesheet.project_update_view_search_inherit` — on project.update inherits project.project_update_view_search
- `hr_timesheet.project_update_view_kanban_inherit` — on project.update inherits project.project_update_view_kanban
- `hr_timesheet.hr_employee_delete_wizard_form` — on hr.employee.delete.wizard

## project.task.type

- `hr_timesheet.internal_project_default_stage`

## res.groups

- `hr_timesheet.group_hr_timesheet_user`
- `hr_timesheet.group_hr_timesheet_approver`
- `hr_timesheet.group_timesheet_manager`
- `project.group_project_manager`

## res.groups.privilege

- `hr_timesheet.res_groups_privilege_timesheets`

## uom.uom

- `uom.product_uom_day`
- `uom.product_uom_hour`
