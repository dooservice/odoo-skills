# hr_holidays_attendance — HR Attendance Holidays

Depends on: hr_attendance, hr_holidays.

## `hr.attendance` (extends)


Public methods: `write`

## `hr.employee` (extends)


Public methods: `get_attendance_data_by_employee`

Extension points: `_get_calendar_attendance_domain`

## `hr.leave` (extends)


## `hr.leave.accrual.level` (extends)

- `frequency` Selection (store, compute=_compute_frequency)

Extension points: `_check_worked_hours`, `_get_hourly_frequencies`

## `hr.leave.allocation` (extends)


Extension points: `_get_accrual_plan_level_work_entry_prorata`

## `hr.time.rule` (extends)


## `hr.version` (extends)


Public methods: `has_static_work_entries`

Extension points: `_get_attendance_intervals`, `_get_more_vals_attendance_interval`, `_get_real_attendances`, `_get_valid_leave_intervals`, `_get_version_work_entries_values`, `_get_work_entry_source_fields`

## `ir.ui.menu` (extends)


## `res.company` (extends)

- `attendance_work_entry_type_id` Many2one

## `resource.calendar.leaves` (extends)


Public methods: `create`, `unlink`, `write`

Extension points: `_get_time_rule_affected`

## `hr.leave.attendance.report` (defines)

Attendance and Leave Analysis Report

- `date` Date “Date”
- `employee_id` Many2one → `hr.employee` “Employee”
- `active` Boolean (related=employee_id.active)
- `department_id` Many2one “Department” (related=employee_id.department_id)
- `job_id` Many2one “Job Position” (related=employee_id.job_id)
- `schedule_id` Many2one → `resource.calendar` “Working Schedule”
- `expected_hours` Float “Expected Hours”
- `worked_hours` Float “Worked Hours”
- `leave_hours` Float “Approved Time Off”
- `difference_hours` Float “Difference”
- `work_entry_type_names` Char “Time Types” (compute=_compute_leave_attendance_fields)
- `leave_ids` Many2many → `hr.leave` “Time Offs” (compute=_compute_leave_attendance_fields)
- `attendance_ids` Many2many → `hr.attendance` “Attendances” (compute=_compute_leave_attendance_fields)

Public methods: `init`
