# hr_holidays_attendance — HR Attendance Holidays

Depends on: hr_attendance, hr_holidays.

## `hr.attendance` (extends)


Extension points: `_get_overtime_leave_domain`

## `hr.leave` (extends)

- `overtime_id` Many2one → `hr.attendance.overtime` “Extra Hours”
- `employee_overtime` Float (related=employee_id.total_overtime)
- `overtime_deductible` Boolean (compute=_compute_overtime_deductible)

Public methods: `action_approve`, `action_refuse`, `action_reset_confirm`, `create`, `unlink`, `write`

Extension points: `_check_overtime_deductible`

## `hr.leave.accrual.level` (extends)

- `frequency_hourly_source` Selection (store, compute=_compute_frequency_hourly_source)

## `hr.leave.allocation` (extends)

- `overtime_deductible` Boolean (compute=_compute_overtime_deductible)
- `overtime_id` Many2one → `hr.attendance.overtime` “Extra Hours”
- `employee_overtime` Float (related=employee_id.total_overtime)

Public methods: `action_refuse`, `action_set_to_confirm`, `create`, `default_get`, `write`

Extension points: `_get_accrual_plan_level_work_entry_prorata`

## `hr.leave.type` (extends)

- `overtime_deductible` Boolean “Deduct Extra Hours”

Public methods: `get_allocation_data`

## `res.users` (extends)

- `request_overtime` Boolean (compute=_compute_request_overtime)

Public methods: `SELF_READABLE_FIELDS`
