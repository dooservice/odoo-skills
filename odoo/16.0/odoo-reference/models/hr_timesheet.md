# hr_timesheet — Task Logs

Depends on: hr, hr_hourly_cost, analytic, project, uom.

## `account.analytic.line` (extends)

- `task_id` Many2one → `project.task` (store, compute=_compute_task_id)
- `ancestor_task_id` Many2one → `project.task` (store, related=task_id.ancestor_id)
- `project_id` Many2one → `project.project` (store, index, compute=_compute_project_id)
- `user_id` Many2one (store, compute=_compute_user_id)
- `employee_id` Many2one → `hr.employee`
- `job_title` Char (related=employee_id.job_title)
- `department_id` Many2one → `hr.department` (store, compute=_compute_department_id)
- `manager_id` Many2one → `hr.employee` (store, related=employee_id.parent_id)
- `encoding_uom_id` Many2one → `uom.uom` (compute=_compute_encoding_uom_id)
- `partner_id` Many2one (store, compute=_compute_partner_id)

Public methods: `create`, `default_get`, `name_get`, `write`

Extension points: `_get_favorite_project_id`, `_get_favorite_project_id_domain`, `_get_report_base_filename`, `_get_timesheet_time_day`, `_get_view`, `_get_view_cache_key`

## `ir.http` (extends)


Public methods: `get_timesheet_uoms`, `session_info`

## `ir.ui.menu` (extends)


## `project.project` (extends)

- `allow_timesheets` Boolean “Timesheets” (store, compute=_compute_allow_timesheets)
- `analytic_account_id` Many2one
- `timesheet_ids` One2many → `account.analytic.line`
- `timesheet_count` Integer (compute=_compute_timesheet_count)
- `timesheet_encode_uom_id` Many2one → `uom.uom` (related=company_id.timesheet_encode_uom_id)
- `total_timesheet_time` Integer (compute=_compute_total_timesheet_time)
- `encode_uom_in_days` Boolean (compute=_compute_encode_uom_in_days)
- `is_internal_project` Boolean (compute=_compute_is_internal_project)
- `remaining_hours` Float “Remaining Invoiced Time” (compute=_compute_remaining_hours)
- `is_project_overtime` Boolean “Project in Overtime” (compute=_compute_remaining_hours)
- `allocated_hours` Float “Allocated Hours”

Public methods: `action_project_timesheets`, `create`, `name_get`, `write`

Extension points: `_check_allow_timesheet`, `_get_view`, `_get_view_cache_key`

## `project.task` (extends)

- `analytic_account_active` Boolean “Active Analytic Account” (compute=_compute_analytic_account_active)
- `allow_timesheets` Boolean “Allow timesheets” (readonly, compute=_compute_allow_timesheets)
- `remaining_hours` Float “Remaining Hours” (readonly, store, compute=_compute_remaining_hours)
- `remaining_hours_percentage` Float (compute=_compute_remaining_hours_percentage)
- `effective_hours` Float “Hours Spent” (store, compute=_compute_effective_hours)
- `total_hours_spent` Float “Total Hours” (store, compute=_compute_total_hours_spent)
- `progress` Float “Progress” (store, compute=_compute_progress_hours)
- `overtime` Float (store, compute=_compute_progress_hours)
- `subtask_effective_hours` Float “Sub-tasks Hours Spent” (store, compute=_compute_subtask_effective_hours)
- `timesheet_ids` One2many → `account.analytic.line`
- `encode_uom_in_days` Boolean (compute=_compute_encode_uom_in_days)

Public methods: `SELF_READABLE_FIELDS`, `action_view_subtask_timesheet`, `name_get`, `write`

Extension points: `_get_timesheet`, `_get_view`, `_get_view_cache_key`

## `project.collaborator` (extends)


## `res.company` (extends)

- `project_time_mode_id` Many2one → `uom.uom` “Project Time Unit”
- `timesheet_encode_uom_id` Many2one → `uom.uom` “Timesheet Encoding Unit”
- `internal_project_id` Many2one → `project.project` “Internal Project”

Public methods: `create`

Extension points: `_check_internal_project_id_company`, `_create_internal_project_task`

## `res.config.settings` (extends)

- `module_project_timesheet_synchro` Boolean “Awesome Timesheet” (store, compute=_compute_timesheet_modules)
- `module_project_timesheet_holidays` Boolean “Time Off” (store, compute=_compute_timesheet_modules)
- `reminder_user_allow` Boolean “Employee Reminder”
- `reminder_manager_allow` Boolean “Manager Reminder”
- `project_time_mode_id` Many2one → `uom.uom` “Project Time Unit” (related=company_id.project_time_mode_id)
- `timesheet_encode_uom_id` Many2one → `uom.uom` “Encoding Unit” (related=company_id.timesheet_encode_uom_id)
- `is_encode_uom_days` Boolean (compute=_compute_is_encode_uom_days)

## `uom.uom` (extends)

- `timesheet_widget` Char “Widget”

## `report.project.task.user` (extends)

- `hours_planned` Float “Planned Hours” (readonly)
- `hours_effective` Float “Effective Hours” (readonly)
- `remaining_hours` Float “Remaining Hours” (readonly)
- `progress` Float “Progress” (readonly)
- `overtime` Float (readonly)

Extension points: `_get_view`, `_get_view_cache_key`

## `timesheets.analysis.report` (defines)

Timesheets Analysis Report

- `name` Char “Description” (readonly)
- `user_id` Many2one → `res.users` “User” (readonly)
- `project_id` Many2one → `project.project` “Project” (readonly)
- `task_id` Many2one → `project.task` “Task” (readonly)
- `ancestor_task_id` Many2one → `project.task` “Ancestor Task” (readonly)
- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `manager_id` Many2one → `hr.employee` (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `department_id` Many2one → `hr.department` “Department” (readonly)
- `currency_id` Many2one → `res.currency` “Currency” (readonly)
- `date` Date “Date” (readonly)
- `amount` Monetary “Amount” (readonly)
- `unit_amount` Float “Hours Spent” (readonly)

Public methods: `init`

Extension points: `_get_view`, `_get_view_cache_key`
