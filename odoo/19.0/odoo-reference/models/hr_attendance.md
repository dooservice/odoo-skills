# hr_attendance — Attendances

Depends on: hr, barcodes, base_geolocalize.

## `hr.attendance` (defines)

Attendance

Inherits: `mail.thread`

- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `department_id` Many2one → `hr.department` “Department” (readonly, related=employee_id.department_id)
- `manager_id` Many2one → `hr.employee` (readonly, related=employee_id.parent_id)
- `attendance_manager_id` Many2one → `res.users` (related=employee_id.attendance_manager_id)
- `is_manager` Boolean (compute=_compute_is_manager)
- `check_in` Datetime “Check In” (required, index)
- `check_out` Datetime “Check Out”
- `date` Date “Date” (required, store, index, compute=_compute_date)
- `worked_hours` Float “Worked Hours” (readonly, store, compute=_compute_worked_hours)
- `color` Integer (compute=_compute_color)
- `overtime_hours` Float “Worked Extra Hours” (store, compute=_compute_overtime_hours)
- `overtime_status` Selection (store, compute=_compute_overtime_status)
- `validated_overtime_hours` Float “Validated Extra Hours” (readonly, store, compute=_compute_validated_overtime_hours)
- `in_latitude` Float “Latitude” (readonly)
- `in_longitude` Float “Longitude” (readonly)
- `in_location` Char
- `in_ip_address` Char “IP Address” (readonly)
- `in_browser` Char “Browser” (readonly)
- `in_mode` Selection “Mode” (readonly)
- `out_latitude` Float (readonly)
- `out_longitude` Float (readonly)
- `out_location` Char
- `out_ip_address` Char (readonly)
- `out_browser` Char (readonly)
- `out_mode` Selection (readonly)
- `expected_hours` Float “Regular Hours” (store, compute=_compute_expected_hours)
- `device_tracking_enabled` Boolean (related=employee_id.company_id.attendance_device_tracking)
- `linked_overtime_ids` Many2many → `hr.attendance.overtime.line` (compute=_compute_linked_overtime_ids)

Public methods: `action_approve_overtime`, `action_in_attendance_maps`, `action_out_attendance_maps`, `action_refuse_overtime`, `action_try_kiosk`, `copy`, `create`, `get_kiosk_url`, `has_demo_data`, `unlink`, `write`

Extension points: `_check_validity`, `_check_validity_check_in_check_out`, `_get_attendance_by_periods_by_employee`, `_get_dates`, `_get_day_start_and_day`, `_get_employee_calendar`, `_get_localized_times`, `_get_overtime_domain_from_attendance_domain`, `_get_overtimes_to_update_domain`, `_get_week_date_range`, `_get_worked_hours_in_range`

## `hr.attendance.overtime.line` (defines)

Attendance Overtime Line

- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `company_id` Many2one (related=employee_id.company_id)
- `date` Date “Day” (required, index)
- `status` Selection (required, store, compute=_compute_status)
- `duration` Float “Extra Hours” (required)
- `manual_duration` Float “Extra Hours (encoded)” (store, compute=_compute_manual_duration)
- `time_start` Datetime “Start”
- `time_stop` Datetime “Stop”
- `amount_rate` Float “Overtime pay rate” (required)
- `is_manager` Boolean (compute=_compute_is_manager)
- `rule_ids` Many2many → `hr.attendance.overtime.rule` “Applied Rules”

Public methods: `action_approve`, `action_refuse`, `write`

## `hr.attendance.overtime.rule` (defines)

Overtime Rule

- `name` Char (required)
- `description` Html
- `base_off` Selection “Based Off” (required)
- `timing_type` Selection
- `timing_start` Float “From”
- `timing_stop` Float “To”
- `expected_hours_from_contract` Boolean “Hours from employee schedule”
- `resource_calendar_id` Many2one → `resource.calendar` “Schedule”
- `expected_hours` Float “Usual work hours”
- `quantity_period` Selection
- `sequence` Integer
- `ruleset_id` Many2one → `hr.attendance.overtime.ruleset` (required, index)
- `company_id` Many2one (related=ruleset_id.company_id)
- `paid` Boolean “Pay Extra Hours”
- `amount_rate` Float “Rate”
- `employee_tolerance` Float
- `employer_tolerance` Float
- `information_display` Char “Information” (compute=_compute_information_display)

Extension points: `_check_expected_hours`, `_check_work_schedule`, `_get_all_overtime_intervals_for_quantity_rule`, `_get_all_overtime_intervals_for_timing_rule`, `_get_all_overtime_undertime_intervals_for_quantity_rule`, `_get_daterange_overtime_intervals_for_quantity_rule`, `_get_daterange_overtime_undertime_intervals_for_quantity_rule`, `_get_expected_hours_from_contract`, `_get_local_time_start`, `_get_local_time_stop`, `_get_overtime_intervals_by_date`, `_get_overtime_intervals_by_employee_by_attendance`, `_get_overtime_undertime_intervals_by_employee_by_attendance`, `_get_period_keys`, `_get_periods`, `_get_rules_intervals_by_timing_type`

## `hr.attendance.overtime.ruleset` (defines)

Overtime Ruleset

- `name` Char (required)
- `description` Html
- `rule_ids` One2many → `hr.attendance.overtime.rule`
- `company_id` Many2one → `res.company`
- `country_id` Many2one → `res.country`
- `rate_combination_mode` Selection “Rate Combination Mode” (required)
- `rules_count` Integer (compute=_compute_rules_count)
- `active` Boolean

Public methods: `action_regenerate_overtimes`

## `hr.employee` (extends)

- `attendance_manager_id` Many2one → `res.users` “Attendance Approver” (store)
- `attendance_ids` One2many → `hr.attendance`
- `last_attendance_id` Many2one → `hr.attendance` (store, compute=_compute_last_attendance_id)
- `last_check_in` Datetime (store, related=last_attendance_id.check_in)
- `last_check_out` Datetime (store, related=last_attendance_id.check_out)
- `attendance_state` Selection “Attendance Status” (compute=_compute_attendance_state)
- `hours_last_month` Float (compute=_compute_hours_last_month)
- `hours_last_month_overtime` Float (compute=_compute_hours_last_month)
- `hours_today` Float (compute=_compute_hours_today)
- `hours_previously_today` Float (compute=_compute_hours_today)
- `last_attendance_worked_hours` Float (compute=_compute_hours_today)
- `hours_last_month_display` Char (compute=_compute_hours_last_month)
- `overtime_ids` One2many → `hr.attendance.overtime.line`
- `total_overtime` Float (compute=_compute_total_overtime)
- `display_extra_hours` Boolean (related=company_id.hr_attendance_display_overtime)
- `ruleset_id` Many2one (related=version_id.ruleset_id)
- `display_attendances` Boolean (compute=_compute_display_attendances)

Public methods: `action_archive`, `action_open_last_month_attendances`, `create`, `get_overtime_data`, `open_barcode_scanner`, `write`

Extension points: `_get_schedules_by_employee_by_work_type`

## `hr.employee.public` (extends)

- `attendance_state` Selection (readonly, related=employee_id.attendance_state)
- `hours_today` Float (readonly, related=employee_id.hours_today)
- `hours_last_month` Float (related=employee_id.hours_last_month)
- `hours_last_month_overtime` Float (related=employee_id.hours_last_month_overtime)
- `last_attendance_id` Many2one (readonly, related=employee_id.last_attendance_id)
- `total_overtime` Float (readonly, related=employee_id.total_overtime)
- `attendance_manager_id` Many2one (related=employee_id.attendance_manager_id)
- `last_check_in` Datetime (related=employee_id.last_check_in)
- `last_check_out` Datetime (related=employee_id.last_check_out)
- `display_extra_hours` Boolean (related=company_id.hr_attendance_display_overtime)
- `display_attendances` Boolean (related=employee_id.display_attendances)

Public methods: `action_open_last_month_attendances`

## `hr.version` (extends)

- `ruleset_id` Many2one → `hr.attendance.overtime.ruleset`

Extension points: `_get_versions_by_employee_and_date`

## `ir.http` (extends)


Public methods: `lazy_session_info`

## `res.company` (extends)

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
- `attendance_overtime_validation` Selection “Extra Hours Validation”
- `auto_check_out` Boolean “Automatic Check Out”
- `auto_check_out_tolerance` Float
- `absence_management` Boolean “Absence Management”
- `attendance_device_tracking` Boolean “Device & Location Tracking”

Public methods: `write`

Extension points: `_action_open_kiosk_mode`, `_check_hr_presence_control`

## `res.config.settings` (extends)

- `overtime_company_threshold` Integer “Tolerance Time In Favor Of Company”
- `overtime_employee_threshold` Integer “Tolerance Time In Favor Of Employee”
- `hr_attendance_display_overtime` Boolean (related=company_id.hr_attendance_display_overtime)
- `attendance_kiosk_mode` Selection (related=company_id.attendance_kiosk_mode)
- `attendance_barcode_source` Selection (related=company_id.attendance_barcode_source)
- `attendance_kiosk_delay` Integer (related=company_id.attendance_kiosk_delay)
- `attendance_kiosk_url` Char (related=company_id.attendance_kiosk_url)
- `attendance_kiosk_use_pin` Boolean (related=company_id.attendance_kiosk_use_pin)
- `attendance_from_systray` Boolean (related=company_id.attendance_from_systray)
- `attendance_overtime_validation` Selection (related=company_id.attendance_overtime_validation)
- `auto_check_out` Boolean (related=company_id.auto_check_out)
- `auto_check_out_tolerance` Float (related=company_id.auto_check_out_tolerance)
- `absence_management` Boolean (related=company_id.absence_management)
- `attendance_device_tracking` Boolean (related=company_id.attendance_device_tracking)

Public methods: `get_values`, `regenerate_kiosk_key`, `set_values`

## `res.users` (extends)
