# project_timesheet_holidays — Timesheet when on Time Off

Depends on: hr_timesheet, hr_holidays.

## `account.analytic.line` (extends)

- `holiday_id` Many2one → `hr.leave` “Leave Request”
- `global_leave_id` Many2one → `resource.calendar.leaves` “Global Time Off”
- `task_id` Many2one

Public methods: `create`, `write`

Extension points: `_check_can_update_timesheet`, `_get_favorite_project_id_domain`

## `hr.employee` (extends)


Public methods: `create`, `write`

Extension points: `_create_future_public_holidays_timesheets`

## `hr.leave.type` (extends)

- `timesheet_generate` Boolean “Generate Timesheet” (store, compute=_compute_timesheet_generate)
- `timesheet_project_id` Many2one → `project.project` “Project”
- `timesheet_task_id` Many2one → `project.task` “Task” (store, compute=_compute_timesheet_task_id)

Extension points: `_check_timesheet_generate`

## `hr.leave` (extends)

- `timesheet_ids` One2many → `account.analytic.line` “Analytic Lines”

Public methods: `action_refuse`

Extension points: `_action_user_cancel`, `_check_missing_global_leave_timesheets`

## `project.task` (extends)

- `leave_types_count` Integer (compute=_compute_leave_types_count)
- `is_timeoff_task` Boolean “Is Time off Task” (compute=_compute_is_timeoff_task)

## `res.company` (extends)

- `leave_timesheet_task_id` Many2one → `project.task` “Time Off Task”

Extension points: `_create_internal_project_task`

## `res.config.settings` (extends)

- `internal_project_id` Many2one “Internal Project” (required, related=company_id.internal_project_id)
- `leave_timesheet_task_id` Many2one “Time Off Task” (related=company_id.leave_timesheet_task_id)

## `resource.calendar.leaves` (extends)

- `timesheet_ids` One2many → `account.analytic.line` “Analytic Lines”

Public methods: `create`, `write`
