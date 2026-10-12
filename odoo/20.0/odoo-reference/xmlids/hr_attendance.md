# hr_attendance — XML ids

## ir.actions.act_window

- `hr_attendance.hr_attendance_action`
- `hr_attendance.hr_attendance_my_action`
- `hr_attendance.hr_attendance_reporting`
- `hr_attendance.hr_attendance_management_action`
- `hr_attendance.hr_employee_attendance_action_kanban`
- `hr_attendance.action_hr_attendance_settings`

## ir.actions.client

- `hr_attendance.hr_attendance_action_greeting_message`

## ir.actions.server

- `hr_attendance.action_try_kiosk`
- `hr_attendance.action_load_demo_data`
- `hr_attendance.open_kiosk_url`
- `hr_attendance.action_attendance_validate`
- `hr_attendance.action_attendance_refuse`

## ir.cron

- `hr_attendance.hr_attendance_check_out_cron`
- `hr_attendance.hr_attendance_absence_cron`
- `hr_attendance.hr_attendance_day_undertime_rules_cron`
- `hr_attendance.hr_attendance_week_time_rules_cron`

## ir.ui.menu

- `hr_attendance.menu_hr_attendance_root` — Attendances
- `hr_attendance.menu_action_open_form` — Kiosk Mode
- `hr_attendance.menu_hr_attendance_reporting` — Reporting
- `hr_attendance.menu_hr_attendance_attendance_reporting` — Attendances
- `hr_attendance.menu_hr_attendance_my_attendances` — My Attendances
- `hr_attendance.menu_hr_attendance_view_attendances_management` — Management
- `hr_attendance.menu_hr_attendance_view_dashboard` — Dashboard
- `hr_attendance.menu_hr_attendance_management_list` — Attendances
- `hr_attendance.menu_hr_attendance_configuration` — Configuration
- `hr_attendance.menu_hr_attendance_onboarding` — Onboarding
- `hr_attendance.menu_hr_attendance_work_entry_type` — Time Types
- `hr_attendance.menu_hr_attendance_time_rules` — Automatic Rules
- `hr_attendance.menu_hr_attendance_employee` — Employees
- `hr_attendance.menu_hr_attendance_settings` — Settings

## ir.ui.view

- `hr_attendance.view_attendance_tree` — on hr.attendance
- `hr_attendance.view_hr_attendance_kanban` — on hr.attendance
- `hr_attendance.hr_attendance_view_form` — on hr.attendance
- `hr_attendance.hr_attendance_create_view_form` — on hr.attendance inherits hr_attendance.hr_attendance_view_form
- `hr_attendance.hr_attendance_my_form_view` — on hr.attendance inherits hr_attendance_view_form
- `hr_attendance.hr_attendance_my_calendar_view` — on hr.attendance
- `hr_attendance.hr_attendance_view_graph` — on hr.attendance
- `hr_attendance.hr_attendance_view_pivot` — on hr.attendance
- `hr_attendance.hr_attendance_view_filter` — on hr.attendance
- `hr_attendance.hr_attendance_management_view_filter` — on hr.attendance
- `hr_attendance.view_attendance_tree_management` — on hr.attendance
- `hr_attendance.hr_department_view_kanban` — on hr.department inherits hr.hr_department_view_kanban
- `hr_attendance.hr_employee_search_view` — on hr.employee inherits hr.view_employee_filter
- `hr_attendance.view_employee_form_inherit_hr_attendance` — on hr.employee inherits hr.view_employee_form
- `hr_attendance.hr_employees_view_kanban` — on hr.employee
- `hr_attendance.view_employee_tree_inherit_leave` — on hr.employee inherits hr.view_employee_tree
- `hr_attendance.hr_attendance_employee_calendar_view` — on hr.attendance
- `hr_attendance.hr_attendance_employee_simple_form_view` — on hr.attendance inherits hr_attendance.hr_attendance_view_form
- `hr_attendance.hr_employee_public_view_form` — on hr.employee.public inherits hr.hr_employee_public_view_form
- `hr_attendance.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form
- `hr_attendance.public_kiosk_mode`
- `hr_attendance.hr_version_list_view_enhanced_hr_attendance_base` — on hr.version inherits hr.hr_version_list_view_enhanced
- `hr_attendance.hr_version_search_view_enhanced_hr_attendance` — on hr.version inherits hr.hr_version_search_view_enhanced
- `hr_attendance.hr_contract_template_view_form` — on hr.version inherits hr.hr_contract_template_form_view

## res.groups

- `hr_attendance.group_hr_attendance_own_reader`
- `base.group_user`
- `hr_attendance.group_hr_attendance_own`
- `hr_attendance.group_hr_attendance_officer`
- `hr_attendance.group_hr_attendance_user`
- `hr_attendance.group_hr_attendance_manager`
- `base.default_user_group`

## res.groups.privilege

- `hr_attendance.res_groups_privilege_attendances`
