# hr_timesheet — Task Logs

Depends on: hr, analytic, project, uom.

## `account.analytic.line` (extends)

- `task_id` Many2one → `project.task` (store, compute=_compute_task_id)
- `parent_task_id` Many2one → `project.task` (store, related=task_id.parent_id)
- `project_id` Many2one → `project.project` (store, index, compute=_compute_project_id)
- `user_id` Many2one (store, compute=_compute_user_id)
- `employee_id` Many2one → `hr.employee` (index)
- `job_title` Char (related=employee_id.job_title)
- `department_id` Many2one → `hr.department` (store, compute=_compute_department_id)
- `manager_id` Many2one → `hr.employee` (store, related=employee_id.parent_id)
- `encoding_uom_id` Many2one → `uom.uom` (compute=_compute_encoding_uom_id)
- `partner_id` Many2one (store, compute=_compute_partner_id)
- `readonly_timesheet` Boolean (compute=_compute_readonly_timesheet)
- `milestone_id` Many2one → `project.milestone` (related=task_id.milestone_id)
- `message_partner_ids` Many2many → `res.partner` (compute=_compute_message_partner_ids)
- `calendar_display_name` Char (compute=_compute_calendar_display_name)
- `color` Integer (related=project_id.color)
- `sequence` Integer “Sequence”

Public methods: `action_open_timesheet_view_portal`, `create`, `default_get`, `get_import_templates`, `get_unusual_days`, `get_views`, `write`

Extension points: `_check_can_create`, `_check_can_write`, `_get_favorite_project_id`, `_get_favorite_project_id_domain`, `_get_report_base_filename`, `_get_timesheet_time_day`

## `account.analytic.line.calendar.employee` (defines)

Personal Filters on Employees for the Calendar view

- `user_id` Many2one → `res.users` (required)
- `employee_id` Many2one → `hr.employee`
- `checked` Boolean
- `active` Boolean

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection

## `hr.employee` (extends)

- `has_timesheet` Boolean (compute=_compute_has_timesheet)

Public methods: `action_timesheet_from_employee`, `action_unlink_wizard`

## `hr.employee.departure` (extends)


Public methods: `action_register`

Extension points: `_get_future_timesheets`

## `hr.employee.public` (extends)

- `has_timesheet` Boolean (related=employee_id.has_timesheet)

Public methods: `action_timesheet_from_employee`

## `ir.http` (extends)


Public methods: `get_timesheet_uoms`, `session_info`

## `ir.ui.menu` (extends)


## `project.collaborator` (extends)


## `project.project` (extends)

- `allow_timesheets` Boolean “Timesheets” (store, compute=_compute_allow_timesheets)
- `account_id` Many2one
- `analytic_account_active` Boolean “Active Account” (related=account_id.active)
- `timesheet_ids` One2many → `account.analytic.line`
- `timesheet_encode_uom_id` Many2one → `uom.uom` (compute=_compute_timesheet_encode_uom_id)
- `total_timesheet_time` Float “Total amount of time (in the proper unit) recorded in the project, rounded to the unit.” (compute=_compute_total_timesheet_time)
- `encode_uom_in_days` Boolean (compute=_compute_encode_uom_in_days)
- `is_internal_project` Boolean (compute=_compute_is_internal_project)
- `remaining_hours` Float “Time Remaining” (compute=_compute_remaining_hours)
- `is_project_overtime` Boolean “Project in Overtime” (compute=_compute_remaining_hours)
- `allocated_hours` Float “Allocated Time”
- `effective_hours` Float “Time Spent” (compute=_compute_remaining_hours)
- `stat_timesheet_value` Char (compute=_compute_timesheet_stat_values)
- `stat_extra_time_value` Char (compute=_compute_timesheet_stat_values)
- `stat_success_rate` Float (compute=_compute_timesheet_stat_values)

Public methods: `action_print_timesheets`, `action_project_timesheets`, `action_view_tasks`, `create`, `get_create_edit_project_ids`, `write`

Extension points: `_check_allow_timesheet`, `_get_processed_analytic_account_vals`

## `project.task` (extends)

- `project_id` Many2one
- `analytic_account_active` Boolean “Active Analytic Account” (related=project_id.analytic_account_active)
- `allow_timesheets` Boolean “Allow timesheets” (readonly, compute=_compute_allow_timesheets)
- `remaining_hours` Float “Time Remaining” (readonly, store, compute=_compute_remaining_hours)
- `remaining_hours_percentage` Float (compute=_compute_remaining_hours_percentage)
- `effective_hours` Float “Time Spent” (store, compute=_compute_effective_hours)
- `total_hours_spent` Float “Total Time Spent” (store, compute=_compute_total_hours_spent)
- `progress` Float “Progress” (store, compute=_compute_progress_hours)
- `overtime` Float (store, compute=_compute_progress_hours)
- `subtask_effective_hours` Float “Time Spent on Sub-tasks” (store, compute=_compute_subtask_effective_hours)
- `timesheet_ids` One2many → `account.analytic.line`
- `portal_timesheet_ids` One2many → `account.analytic.line`
- `encode_uom_in_days` Boolean (compute=_compute_encode_uom_in_days)
- `display_name` Char
- `show_portal_timesheets` Boolean

Public methods: `TASK_PORTAL_READABLE_FIELDS`, `action_print_timesheets`, `action_view_subtask_timesheet`

Extension points: `_check_project_root`, `_get_cannot_start_with_patterns`, `_get_domain_effective_hours`, `_get_group_pattern`, `_get_groups`, `_get_portal_total_hours_dict`, `_get_template_field_blacklist`, `_get_timesheet`, `_get_timesheet_report_data`, `_prepare_pattern_groups`

## `project.update` (extends)

- `display_timesheet_stats` Boolean (compute=_compute_display_timesheet_stats)
- `allocated_time` Integer “Allocated Time” (readonly)
- `timesheet_time` Integer “Timesheet Time” (readonly)
- `timesheet_percentage` Integer (compute=_compute_timesheet_percentage)
- `uom_id` Many2one → `uom.uom` (readonly)

Public methods: `create`

## `res.company` (extends)

- `project_time_mode_id` Many2one → `uom.uom` “Project Time Unit”
- `timesheet_encode_uom_id` Many2one → `uom.uom` “Timesheet Encoding Unit”
- `internal_project_id` Many2one → `project.project` “Internal Project”

Public methods: `create`

Extension points: `_check_internal_project_id_company`, `_create_internal_project_task`

## `res.config.settings` (extends)

- `module_project_timesheet_holidays` Boolean “Time Off” (store, compute=_compute_timesheet_modules)
- `reminder_user_allow` Boolean “Employee Reminder”
- `reminder_allow` Boolean “Approver Reminder”
- `project_time_mode_id` Many2one → `uom.uom` “Project Time Unit” (related=company_id.project_time_mode_id)
- `is_encode_uom_days` Boolean (compute=_compute_is_encode_uom_days)
- `timesheet_encode_method` Selection “Encoding Method” (required, compute=_compute_timesheet_encode_method)

## `uom.uom` (extends)

- `timesheet_widget` Char “Widget”

## `report.project.task.user` (extends)

- `allocated_hours` Float “Allocated Time” (readonly)
- `effective_hours` Float “Time Spent” (readonly)
- `remaining_hours` Float “Time Remaining” (readonly)
- `remaining_hours_percentage` Float “Time Remaining Percentage” (readonly)
- `progress` Float “Progress” (readonly)
- `overtime` Float (readonly)

## `timesheets.analysis.report` (defines)

Timesheets Analysis Report

Inherits: `hr.manager.department.report`

- `name` Char “Description” (readonly)
- `user_id` Many2one → `res.users` “User” (readonly)
- `project_id` Many2one → `project.project` “Project” (readonly)
- `task_id` Many2one → `project.task` “Task” (readonly)
- `parent_task_id` Many2one → `project.task` “Parent Task” (readonly)
- `manager_id` Many2one → `hr.employee` (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `department_id` Many2one → `hr.department` “Department” (readonly)
- `currency_id` Many2one → `res.currency` “Currency” (readonly)
- `date` Date “Date” (readonly)
- `amount` Monetary “Amount” (readonly)
- `unit_amount` Float “Time Spent” (readonly)
- `partner_id` Many2one → `res.partner` “Partner” (readonly)
- `milestone_id` Many2one → `project.milestone` (related=task_id.milestone_id)
- `message_partner_ids` Many2many → `res.partner` (readonly, compute=_compute_message_partner_ids)

Public methods: `init`

## `hr.employee.delete.wizard` (defines)

Employee Delete Wizard

- `employee_ids` Many2many → `hr.employee` “Employees”
- `has_active_employee` Boolean “Has Active Employee” (compute=_compute_has_active_employee)
- `has_timesheet` Boolean “Has Timesheet” (compute=_compute_has_timesheet)

Public methods: `action_archive`, `action_confirm_delete`, `action_open_timesheets`
