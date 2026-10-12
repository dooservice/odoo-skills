# hr_attendance — Attendances

Depends on: hr, hr_work_entry, barcodes, base_geolocalize.

## `hr.attendance` (defines)

Attendance

Inherits: `mail.thread`, `hr.time.rule.source.mixin`

- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `department_id` Many2one → `hr.department` “Department” (readonly, related=employee_id.department_id)
- `manager_id` Many2one → `hr.employee` (readonly, related=employee_id.parent_id)
- `attendance_manager_id` Many2one → `res.users` (related=employee_id.attendance_manager_id)
- `is_manager` Boolean (compute=_compute_is_manager)
- `is_own` Boolean (compute=_compute_is_manager)
- `can_edit` Boolean (compute=_compute_can_edit)
- `check_in` Datetime “Check In” (required, index)
- `check_out` Datetime “Check Out”
- `date` Date “Date” (required, store, index, compute=_compute_date)
- `worked_hours` Float “Worked Hours” (readonly, store, compute=_compute_worked_hours)
- `color` Integer (compute=_compute_color)
- `in_latitude` Float “Latitude” (readonly)
- `in_longitude` Float “Longitude” (readonly)
- `in_location` Char
- `in_ip_address` Char “IP Address” (readonly)
- `in_browser` Char “Browser” (readonly)
- `in_mode` Selection “Mode” (readonly)
- `in_image` Binary “Check-In Image”
- `out_latitude` Float (readonly)
- `out_longitude` Float (readonly)
- `out_location` Char
- `out_ip_address` Char (readonly)
- `out_browser` Char (readonly)
- `out_mode` Selection (readonly)
- `device_tracking_enabled` Boolean (related=employee_id.company_id.attendance_device_tracking)
- `day_of_date` Selection “Day” (store, index, compute=_compute_day_of_date)
- `resource_calendar_id` Many2one “Working Schedule” (related=employee_id.resource_calendar_id)
- `break_duration` Float “Break Duration”
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type” (required, index)
- `wet_display_code` Char (related=work_entry_type_id.display_code)
- `wet_color` Integer “Work Entry Color” (related=work_entry_type_id.color)
- `state` Selection “Status” (required, readonly, index)
- `time_rule_id` Many2one → `hr.time.rule` (index)
- `source_attendance_id` Many2one → `hr.attendance` (index)
- `overtime_attendance_ids` One2many → `hr.attendance`
- `source_stale` Boolean

Public methods: `action_in_attendance_maps`, `action_mark_reviewed`, `action_out_attendance_maps`, `action_refuse`, `action_reset_to_draft`, `action_try_kiosk`, `action_validate`, `copy`, `create`, `get_kiosk_url`, `get_unusual_days`, `has_demo_data`, `init`, `write`

Extension points: `_check_break_duration`, `_check_validity`, `_check_validity_check_in_check_out`, `_get_break_duration_within_period`, `_get_localized_times`, `_get_source_extra_fields_domain`, `_get_time_rule_break_hours`, `_get_time_rule_deficit_occupied`, `_get_time_rule_output_vals`, `_get_time_rule_remainder_vals`, `_get_write_source_extra_source_fields`

## `hr.employee` (extends)

- `attendance_based` Boolean (related=version_id.attendance_based)
- `attendance_manager_id` Many2one → `res.users` “Attendance Approver” (store, compute=_compute_attendance_manager)
- `attendance_ids` One2many → `hr.attendance`
- `last_attendance_id` Many2one → `hr.attendance` (store, compute=_compute_last_attendance_id)
- `last_check_in` Datetime (store, related=last_attendance_id.check_in)
- `last_check_out` Datetime (store, related=last_attendance_id.check_out)
- `attendance_state` Selection “Attendance Status” (compute=_compute_attendance_state)
- `hours_last_month` Float (compute=_compute_hours_last_month)
- `hours_last_month_overtime` Float (compute=_compute_hours_last_month)
- `hours_today` Float (compute=_compute_hours_today)
- `hours_previously_today` Float (compute=_compute_hours_today)
- `today_attendance_ids` Many2many → `hr.attendance` (compute=_compute_hours_today)
- `last_attendance_worked_hours` Float (compute=_compute_hours_today)
- `hours_last_month_display` Char (compute=_compute_hours_last_month)
- `total_overtime` Float (compute=_compute_total_overtime)
- `display_attendances` Boolean (compute=_compute_display_attendances)

Public methods: `action_archive`, `action_open_last_month_attendances`, `create`, `get_attendance_data_by_employee`, `open_barcode_scanner`, `write`

Extension points: `_get_attendance_manager_domain`, `_get_calendar_attendance_domain`, `_get_work_intervals_by_type`

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
- `display_attendances` Boolean (related=employee_id.display_attendances)

Public methods: `action_open_last_month_attendances`

## `hr.time.rule` (extends)

- `condition_work_entry_type_ids` Many2many

Extension points: `_get_applicable_employees`, `_get_output_attendance_vals`

## `hr.version` (extends)

- `attendance_based` Boolean “Attendance Based”

Extension points: `_get_versions_by_employee_and_date`, `_get_whitelist_fields_from_template`

## `ir.http` (extends)


Public methods: `lazy_session_info`

## `ir.websocket` (extends)


## `res.company` (extends)

- `attendance_kiosk_mode` Selection “Attendance Mode”
- `attendance_barcode_source` Selection “Barcode Source”
- `attendance_kiosk_delay` Integer
- `attendance_kiosk_key` Char
- `attendance_kiosk_url` Char (compute=_compute_attendance_kiosk_url)
- `attendance_kiosk_use_pin` Boolean “Employee PIN Identification”
- `attendance_from_systray` Boolean “Attendance From Systray”
- `auto_check_out` Boolean “Automatic Check Out”
- `single_check_in` Boolean “Single Check-In Attendance System”
- `auto_check_out_mode` Selection
- `auto_check_out_tolerance` Float
- `auto_check_out_specific_time` Float
- `absence_management` Boolean “Absence Management”
- `attendance_validation` Selection “Attendance Validation”
- `attendance_validation_tolerance` Float “Validation Tolerance (Hours)”
- `attendance_work_entry_type_id` Many2one → `hr.work.entry.type` “Attendance Time Type” (store, compute=_compute_attendance_work_entry_type_id)
- `attendance_device_tracking` Boolean “Device & Location Tracking”
- `attendance_capture_check_in` Boolean “Take Pictures on Check-In”
- `attendance_break_management` Boolean “Break Management on Checkout”
- `attendance_based` Boolean

Extension points: `_action_open_kiosk_mode`, `_check_hr_presence_control`

## `res.config.settings` (extends)

- `attendance_kiosk_mode` Selection (related=company_id.attendance_kiosk_mode)
- `attendance_barcode_source` Selection (related=company_id.attendance_barcode_source)
- `attendance_kiosk_delay` Integer (related=company_id.attendance_kiosk_delay)
- `attendance_kiosk_url` Char (related=company_id.attendance_kiosk_url)
- `attendance_kiosk_use_pin` Boolean (related=company_id.attendance_kiosk_use_pin)
- `attendance_from_systray` Boolean (related=company_id.attendance_from_systray)
- `auto_check_out` Boolean (related=company_id.auto_check_out)
- `single_check_in` Boolean (related=company_id.single_check_in)
- `auto_check_out_mode` Selection (related=company_id.auto_check_out_mode)
- `auto_check_out_tolerance` Float (related=company_id.auto_check_out_tolerance)
- `auto_check_out_specific_time` Float (related=company_id.auto_check_out_specific_time)
- `absence_management` Boolean (related=company_id.absence_management)
- `attendance_validation` Selection (related=company_id.attendance_validation)
- `attendance_validation_tolerance` Float (related=company_id.attendance_validation_tolerance)
- `attendance_work_entry_type_id` Many2one (related=company_id.attendance_work_entry_type_id)
- `attendance_device_tracking` Boolean (related=company_id.attendance_device_tracking)
- `attendance_capture_check_in` Boolean (related=company_id.attendance_capture_check_in)
- `attendance_break_management` Boolean (related=company_id.attendance_break_management)
- `attendance_based` Boolean “Default Tracking” (related=company_id.attendance_based)

Public methods: `regenerate_kiosk_key`, `set_values`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.users` (extends)
