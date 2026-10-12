# hr_holidays_attendance — HR Attendance Holidays

Depends on: hr_attendance, hr_holidays.

## `hr.attendance` (extends)


Extension points: `_get_overtime_leave_domain`

## `hr.leave` (extends)

- `overtime_id` Many2one → `hr.attendance.overtime` “Extra Hours”
- `employee_overtime` Float (related=employee_id.total_overtime)
- `overtime_deductible` Boolean (compute=_compute_overtime_deductible)

Public methods: `action_confirm`, `action_draft`, `action_refuse`, `create`, `unlink`, `write`

Extension points: `_check_overtime_deductible`

## `hr.leave.allocation` (extends)

- `overtime_deductible` Boolean (compute=_compute_overtime_deductible)
- `overtime_id` Many2one → `hr.attendance.overtime` “Extra Hours”
- `employee_overtime` Float (related=employee_id.total_overtime)
- `hr_attendance_overtime` Boolean (related=employee_company_id.hr_attendance_overtime)

Public methods: `action_draft`, `action_refuse`, `create`, `default_get`, `write`

## `hr.leave.type` (extends)

- `hr_attendance_overtime` Boolean (compute=_compute_hr_attendance_overtime)
- `overtime_deductible` Boolean “Deduct Extra Hours”

Public methods: `get_employees_days`, `name_get`

Extension points: `_get_days_request`

## `res.company` (extends)


Public methods: `write`

Extension points: `_check_extra_hours_time_off`

## `res.users` (extends)

- `request_overtime` Boolean (compute=_compute_request_overtime)

Public methods: `SELF_READABLE_FIELDS`
