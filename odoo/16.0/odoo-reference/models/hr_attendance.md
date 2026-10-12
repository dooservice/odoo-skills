# hr_attendance — Attendances

Depends on: hr, barcodes.

## `hr.attendance` (defines)

Attendance

- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `department_id` Many2one → `hr.department` “Department” (readonly, related=employee_id.department_id)
- `check_in` Datetime “Check In” (required)
- `check_out` Datetime “Check Out”
- `worked_hours` Float “Worked Hours” (readonly, store, compute=_compute_worked_hours)

Public methods: `copy`, `create`, `name_get`, `unlink`, `write`

Extension points: `_check_validity`, `_check_validity_check_in_check_out`, `_get_attendances_dates`, `_get_day_start_and_day`, `_get_overtime_leave_domain`

## `hr.attendance.overtime` (defines)

Attendance Overtime

- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `company_id` Many2one (related=employee_id.company_id)
- `date` Date “Day”
- `duration` Float “Extra Hours” (required)
- `duration_real` Float “Extra Hours (Real)”
- `adjustment` Boolean

Public methods: `init`

## `hr.employee` (extends)

- `attendance_ids` One2many → `hr.attendance`
- `last_attendance_id` Many2one → `hr.attendance` (store, compute=_compute_last_attendance_id)
- `last_check_in` Datetime (store, related=last_attendance_id.check_in)
- `last_check_out` Datetime (store, related=last_attendance_id.check_out)
- `attendance_state` Selection “Attendance Status” (compute=_compute_attendance_state)
- `hours_last_month` Float (compute=_compute_hours_last_month)
- `hours_today` Float (compute=_compute_hours_today)
- `hours_last_month_display` Char (compute=_compute_hours_last_month)
- `overtime_ids` One2many → `hr.attendance.overtime`
- `total_overtime` Float (compute=_compute_total_overtime)

Public methods: `attendance_manual`, `attendance_scan`, `read_group`

## `hr.employee.public` (extends)

- `attendance_state` Selection (readonly, related=employee_id.attendance_state)
- `hours_today` Float (readonly, related=employee_id.hours_today)
- `last_attendance_id` Many2one (readonly, related=employee_id.last_attendance_id)
- `total_overtime` Float (readonly, related=employee_id.total_overtime)

Public methods: `action_employee_kiosk_confirm`

## `ir.ui.menu` (extends)


## `res.company` (extends)

- `hr_attendance_overtime` Boolean “Count Extra Hours”
- `overtime_start_date` Date “Extra Hours Starting Date”
- `overtime_company_threshold` Integer “Tolerance Time In Favor Of Company”
- `overtime_employee_threshold` Integer “Tolerance Time In Favor Of Employee”
- `attendance_kiosk_mode` Selection “Attendance Mode”
- `attendance_barcode_source` Selection “Barcode Source”
- `attendance_kiosk_delay` Integer

Public methods: `write`

## `res.config.settings` (extends)

- `group_attendance_use_pin` Boolean “Employee PIN”
- `hr_attendance_overtime` Boolean “Count Extra Hours”
- `overtime_start_date` Date “Extra Hours Starting Date”
- `overtime_company_threshold` Integer “Tolerance Time In Favor Of Company”
- `overtime_employee_threshold` Integer “Tolerance Time In Favor Of Employee”
- `attendance_kiosk_mode` Selection (related=company_id.attendance_kiosk_mode)
- `attendance_barcode_source` Selection (related=company_id.attendance_barcode_source)
- `attendance_kiosk_delay` Integer (related=company_id.attendance_kiosk_delay)

Public methods: `get_values`, `set_values`

## `res.users` (extends)

- `hours_last_month` Float (related=employee_id.hours_last_month)
- `hours_last_month_display` Char (related=employee_id.hours_last_month_display)
- `attendance_state` Selection (related=employee_id.attendance_state)
- `last_check_in` Datetime (related=employee_id.last_attendance_id.check_in)
- `last_check_out` Datetime (related=employee_id.last_attendance_id.check_out)
- `total_overtime` Float (related=employee_id.total_overtime)

Public methods: `SELF_READABLE_FIELDS`

## `hr.attendance.report` (defines)

Attendance Statistics

- `department_id` Many2one → `hr.department` “Department” (readonly)
- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `check_in` Date “Check In” (readonly)
- `worked_hours` Float “Hours Worked” (readonly)
- `overtime_hours` Float “Extra Hours” (readonly)

Public methods: `init`
