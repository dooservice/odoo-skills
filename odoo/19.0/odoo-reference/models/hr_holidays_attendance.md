# hr_holidays_attendance — HR Attendance Holidays

Depends on: hr_attendance, hr_holidays.

## `hr.attendance` (extends)


Public methods: `init`

## `hr.attendance.overtime.line` (extends)

- `compensable_as_leave` Boolean “Compensable as Time Off”

## `hr.attendance.overtime.rule` (extends)

- `compensable_as_leave` Boolean “Give back as time off”

## `hr.employee` (extends)


Public methods: `get_overtime_data_by_employee`

Extension points: `_get_deductible_employee_overtime`

## `hr.leave` (extends)

- `employee_overtime` Float (compute=_compute_employee_overtime)
- `overtime_deductible` Boolean (compute=_compute_overtime_deductible)

Public methods: `action_approve`, `action_reset_confirm`, `create`, `write`

Extension points: `_check_overtime_deductible`, `_get_deductible_employee_overtime`

## `hr.leave.accrual.level` (extends)

- `frequency` Selection (store, compute=_compute_frequency)

Extension points: `_check_worked_hours`, `_get_hourly_frequencies`

## `hr.leave.allocation` (extends)

- `overtime_deductible` Boolean (compute=_compute_overtime_deductible)
- `employee_overtime` Float (compute=_compute_employee_overtime)

Public methods: `action_refuse`, `create`, `default_get`, `write`

Extension points: `_check_employee_overtime_balance`, `_get_accrual_plan_level_work_entry_prorata`

## `hr.leave.type` (extends)

- `overtime_deductible` Boolean “Deduct Extra Hours”

Public methods: `get_allocation_data`

## `ir.ui.menu` (extends)


## `resource.calendar.leaves` (extends)


Public methods: `create`, `unlink`, `write`

Extension points: `_get_attendance_domain`

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
- `leave_type_names` Char “Time Off Types” (compute=_compute_leave_attendance_fields)
- `leave_ids` Many2many → `hr.leave` “Time Offs” (compute=_compute_leave_attendance_fields)
- `attendance_ids` Many2many → `hr.attendance` “Attendances” (compute=_compute_leave_attendance_fields)

Public methods: `init`
