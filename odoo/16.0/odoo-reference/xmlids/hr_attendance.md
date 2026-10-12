# hr_attendance — XML ids

## ir.actions.act_window

- `hr_attendance.hr_attendance_action`
- `hr_attendance.hr_attendance_action_employee`
- `hr_attendance.hr_attendance_action_overview`
- `hr_attendance.hr_attendance_overtime_action`
- `hr_attendance.hr_attendance_report_action`
- `hr_attendance.hr_attendance_report_action_filtered`
- `hr_attendance.hr_employee_attendance_action_kanban`
- `hr_attendance.action_hr_attendance_settings`

## ir.actions.client

- `hr_attendance.hr_attendance_action_kiosk_mode`
- `hr_attendance.hr_attendance_action_my_attendances`
- `hr_attendance.hr_attendance_action_greeting_message`

## ir.module.category

- `base.module_category_human_resources_attendances`

## ir.rule

- `hr_attendance.hr_attendance_rule_employee_company`
- `hr_attendance.hr_attendance_rule_attendance_manager`
- `hr_attendance.hr_attendance_rule_attendance_manual`
- `hr_attendance.hr_attendance_rule_attendance_employee`
- `hr_attendance.hr_attendance_overtime_rule_employee_company`
- `hr_attendance.hr_attendance_rule_attendance_overtime_manager`
- `hr_attendance.hr_attendance_rule_attendance_overtime_employee`
- `hr_attendance.hr_attendance_report_rule_multi_company`

## ir.ui.menu

- `hr_attendance.menu_hr_attendance_root` — Attendances
- `hr_attendance.menu_hr_attendance_my_attendances` — Check In / Check Out
- `hr_attendance.menu_hr_attendance_attendances_overview` — Attendances
- `hr_attendance.menu_hr_attendance_kiosk_no_user_mode` — Kiosk Mode
- `hr_attendance.menu_hr_attendance_view_attendances` — Attendances
- `hr_attendance.menu_hr_attendance_report` — Reporting
- `hr_attendance.menu_hr_attendance_settings` — Configuration

## ir.ui.view

- `hr_attendance.view_attendance_tree` — on hr.attendance
- `hr_attendance.view_hr_attendance_kanban` — on hr.attendance
- `hr_attendance.hr_attendance_view_form` — on hr.attendance
- `hr_attendance.hr_attendance_view_filter` — on hr.attendance
- `hr_attendance.view_attendance_overtime_tree` — on hr.attendance.overtime
- `hr_attendance.view_attendance_overtime_search` — on hr.attendance.overtime
- `hr_attendance.hr_attendance_report_view_search` — on hr.attendance.report
- `hr_attendance.hr_attendance_report_view_pivot` — on hr.attendance.report
- `hr_attendance.hr_attendance_report_view_graph` — on hr.attendance.report
- `hr_attendance.hr_department_view_kanban` — on hr.department inherits hr.hr_department_view_kanban
- `hr_attendance.view_employee_form_inherit_hr_attendance` — on hr.employee inherits hr.view_employee_form
- `hr_attendance.hr_user_view_form` — on res.users inherits hr.res_users_view_form_profile
- `hr_attendance.hr_employees_view_kanban` — on hr.employee
- `hr_attendance.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form

## res.groups

- `hr_attendance.group_hr_attendance_kiosk`
- `hr.group_hr_user`
- `hr_attendance.group_hr_attendance`
- `hr_attendance.group_hr_attendance_user`
- `hr_attendance.group_hr_attendance_manager`
- `hr_attendance.group_hr_attendance_use_pin`

## res.users

- `base.default_user`
