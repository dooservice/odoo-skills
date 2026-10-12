# hr_attendance — Attendances

Depends on: hr, barcodes.

## `hr.attendance` (defines)

Attendance

Inherits: `mail.thread`

- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `department_id` Many2one → `hr.department` “Department” (readonly, related=employee_id.department_id)
- `check_in` Datetime “Check In” (required)
- `check_out` Datetime “Check Out”
- `worked_hours` Float “Worked Hours” (readonly, store, compute=_compute_worked_hours)
- `color` Integer (compute=_compute_color)
- `overtime_hours` Float “Over Time” (store, compute=_compute_overtime_hours)
- `in_latitude` Float “Latitude” (readonly)
- `in_longitude` Float “Longitude” (readonly)
- `in_country_name` Char “Country” (readonly)
- `in_city` Char “City” (readonly)
- `in_ip_address` Char “IP Address” (readonly)
- `in_browser` Char “Browser” (readonly)
- `in_mode` Selection “Mode” (readonly)
- `out_latitude` Float (readonly)
- `out_longitude` Float (readonly)
- `out_country_name` Char (readonly)
- `out_city` Char (readonly)
- `out_ip_address` Char (readonly)
- `out_browser` Char (readonly)
- `out_mode` Selection (readonly)

Public methods: `action_in_attendance_maps`, `action_out_attendance_maps`, `copy`, `create`, `unlink`, `write`

Extension points: `_check_validity`, `_check_validity_check_in_check_out`, `_get_attendances_dates`, `_get_day_start_and_day`, `_get_employee_calendar`, `_get_overtime_leave_domain`, `_get_pre_post_work_time`, `_get_worked_hours_in_range`

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

- `attendance_manager_id` Many2one → `res.users` (store)
- `attendance_ids` One2many → `hr.attendance`
- `last_attendance_id` Many2one → `hr.attendance` (store, compute=_compute_last_attendance_id)
- `last_check_in` Datetime (store, related=last_attendance_id.check_in)
- `last_check_out` Datetime (store, related=last_attendance_id.check_out)
- `attendance_state` Selection “Attendance Status” (compute=_compute_attendance_state)
- `hours_last_month` Float (compute=_compute_hours_last_month)
- `hours_today` Float (compute=_compute_hours_today)
- `hours_previously_today` Float (compute=_compute_hours_today)
- `last_attendance_worked_hours` Float (compute=_compute_hours_today)
- `hours_last_month_display` Char (compute=_compute_hours_last_month)
- `overtime_ids` One2many → `hr.attendance.overtime`
- `total_overtime` Float (compute=_compute_total_overtime)

Public methods: `action_archive`, `action_open_last_month_attendances`, `action_open_last_month_overtime`, `create`, `write`

## `hr.employee.base` (extends)


## `hr.employee.public` (extends)

- `attendance_state` Selection (readonly, related=employee_id.attendance_state)
- `hours_today` Float (readonly, related=employee_id.hours_today)
- `last_attendance_id` Many2one (readonly, related=employee_id.last_attendance_id)
- `total_overtime` Float (readonly, related=employee_id.total_overtime)
- `attendance_manager_id` Many2one (related=employee_id.attendance_manager_id)
- `last_check_in` Datetime (related=employee_id.last_check_in)
- `last_check_out` Datetime (related=employee_id.last_check_out)

## `res.company` (extends)

- `hr_attendance_overtime` Boolean “Count Extra Hours”
- `overtime_start_date` Date “Extra Hours Starting Date”
- `overtime_company_threshold` Integer “Tolerance Time In Favor Of Company”
- `overtime_employee_threshold` Integer “Tolerance Time In Favor Of Employee”
- `hr_attendance_display_overtime` Boolean “Display Extra Hours”
- `attendance_kiosk_mode` Selection “Attendance Mode”
- `attendance_barcode_source` Selection “Barcode Source”
- `attendance_kiosk_delay` Integer
- `attendance_kiosk_key` Char
- `attendance_kiosk_url` Char (compute=_compute_attendance_kiosk_url)
- `attendance_kiosk_use_pin` Boolean “Employee PIN Identification”
- `attendance_from_systray` Boolean “Attendance From Systray”

Public methods: `write`

Extension points: `_action_open_kiosk_mode`

## `res.config.settings` (extends)

- `hr_attendance_overtime` Boolean “Count Extra Hours”
- `overtime_start_date` Date “Extra Hours Starting Date”
- `overtime_company_threshold` Integer “Tolerance Time In Favor Of Company”
- `overtime_employee_threshold` Integer “Tolerance Time In Favor Of Employee”
- `hr_attendance_display_overtime` Boolean (related=company_id.hr_attendance_display_overtime)
- `attendance_kiosk_mode` Selection (related=company_id.attendance_kiosk_mode)
- `attendance_barcode_source` Selection (related=company_id.attendance_barcode_source)
- `attendance_kiosk_delay` Integer (related=company_id.attendance_kiosk_delay)
- `attendance_kiosk_url` Char (related=company_id.attendance_kiosk_url)
- `attendance_kiosk_use_pin` Boolean (related=company_id.attendance_kiosk_use_pin)
- `attendance_from_systray` Boolean (related=company_id.attendance_from_systray)

Public methods: `get_values`, `regenerate_kiosk_key`, `set_values`

## `res.users` (extends)

- `hours_last_month` Float (related=employee_id.hours_last_month)
- `hours_last_month_display` Char (related=employee_id.hours_last_month_display)
- `attendance_state` Selection (related=employee_id.attendance_state)
- `last_check_in` Datetime (related=employee_id.last_attendance_id.check_in)
- `last_check_out` Datetime (related=employee_id.last_attendance_id.check_out)
- `total_overtime` Float (related=employee_id.total_overtime)
- `attendance_manager_id` Many2one (related=employee_id.attendance_manager_id)
- `display_extra_hours` Boolean (related=company_id.hr_attendance_display_overtime)

Public methods: `SELF_READABLE_FIELDS`, `action_open_last_month_attendances`, `action_open_last_month_overtime`

## `resource.calendar.leaves` (extends)


Public methods: `create`, `unlink`, `write`

Extension points: `_get_employee_dates`
