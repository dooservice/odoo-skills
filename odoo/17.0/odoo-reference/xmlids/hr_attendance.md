# hr_attendance — XML ids

## ir.actions.act_window

- `hr_attendance.hr_attendance_action`
- `hr_attendance.hr_attendance_reporting`
- `hr_attendance.hr_attendance_overtime_action`
- `hr_attendance.hr_employee_attendance_action_kanban`
- `hr_attendance.action_hr_attendance_settings`

## ir.actions.client

- `hr_attendance.hr_attendance_action_greeting_message`

## ir.actions.server

- `hr_attendance.open_kiosk_url`

## ir.module.category

- `base.module_category_human_resources_attendances`

## ir.rule

- `hr_attendance.hr_attendance_rule_employee_company`
- `hr_attendance.hr_attendance_rule_attendance_admin`
- `hr_attendance.hr_attendance_rule_attendance_manager_restrict`
- `hr_attendance.hr_attendance_rule_attendance_simple_user`
- `hr_attendance.hr_attendance_overtime_rule_employee_company`
- `hr_attendance.hr_attendance_rule_attendance_officer_overtime_restrict`
- `hr_attendance.hr_attendance_rule_attendance_overtime_admin`
- `hr_attendance.hr_attendance_rule_attendance_overtime_simple_user`

## ir.ui.menu

- `hr_attendance.menu_hr_attendance_root` — Attendances
- `hr_attendance.menu_hr_attendance_kiosk_no_user_mode` — Kiosk Mode
- `hr_attendance.menu_hr_attendance_reporting` — Reporting
- `hr_attendance.menu_hr_attendance_view_attendances` — Overview
- `hr_attendance.menu_hr_attendance_settings` — Configuration

## ir.ui.view

- `hr_attendance.view_attendance_tree` — on hr.attendance
- `hr_attendance.view_hr_attendance_kanban` — on hr.attendance
- `hr_attendance.hr_attendance_view_form` — on hr.attendance
- `hr_attendance.hr_attendance_view_graph` — on hr.attendance
- `hr_attendance.hr_attendance_view_pivot` — on hr.attendance
- `hr_attendance.hr_attendance_view_filter` — on hr.attendance
- `hr_attendance.view_attendance_overtime_tree` — on hr.attendance.overtime
- `hr_attendance.view_attendance_overtime_search` — on hr.attendance.overtime
- `hr_attendance.hr_department_view_kanban` — on hr.department inherits hr.hr_department_view_kanban
- `hr_attendance.view_employee_form_inherit_hr_attendance` — on hr.employee inherits hr.view_employee_form
- `hr_attendance.hr_user_view_form` — on res.users inherits hr.res_users_view_form_profile
- `hr_attendance.hr_employees_view_kanban` — on hr.employee
- `hr_attendance.view_employee_tree_inherit_leave` — on hr.employee inherits hr.view_employee_tree
- `hr_attendance.hr_attendance_employee_simple_tree_view` — on hr.attendance
- `hr_attendance.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form
- `hr_attendance.public_kiosk_mode`

## res.groups

- `hr_attendance.group_hr_attendance_own_reader`
- `base.group_user`
- `hr_attendance.group_hr_attendance_officer`
- `hr_attendance.group_hr_attendance_manager`

## res.users

- `base.default_user`
