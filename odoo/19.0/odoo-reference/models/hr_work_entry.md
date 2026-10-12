# hr_work_entry — Work Entries

Depends on: hr.

## `hr.employee` (extends)

- `has_work_entries` Boolean (compute=_compute_has_work_entries)
- `work_entry_source` Selection (related=version_id.work_entry_source)
- `work_entry_source_calendar_invalid` Boolean (related=version_id.work_entry_source_calendar_invalid)

Public methods: `action_open_work_entries`, `create_version`, `generate_work_entries`

## `hr.user.work.entry.employee` (defines)

Work Entries Employees

- `user_id` Many2one → `res.users` (required)
- `employee_id` Many2one → `hr.employee` (required)
- `active` Boolean “Active”
- `is_checked` Boolean

## `hr.version` (extends)

- `date_generated_from` Datetime “Generated From” (required, readonly)
- `date_generated_to` Datetime “Generated To” (required, readonly)
- `last_generation_date` Date “Last Generation Date” (readonly)
- `work_entry_source` Selection (required)
- `work_entry_source_calendar_invalid` Boolean (compute=_compute_work_entry_source_calendar_invalid)

Public methods: `generate_work_entries`, `has_static_work_entries`, `unlink`, `write`

Extension points: `_get_attendance_intervals`, `_get_bypassing_work_entry_type_codes`, `_get_default_work_entry_type_id`, `_get_default_work_entry_type_overtime_id`, `_get_fields_that_recompute_we`, `_get_interval_leave_work_entry_type`, `_get_interval_work_entry_type`, `_get_leave_domain`, `_get_leave_work_entry_type`, `_get_leave_work_entry_type_dates`, `_get_lunch_intervals`, `_get_more_vals_attendance_interval`, `_get_more_vals_leave_interval`, `_get_real_attendance_work_entry_vals`, `_get_real_attendances`, `_get_resource_calendar_leaves`, `_get_sub_leave_domain`, `_get_valid_leave_intervals`, `_get_version_work_entries_values`, `_get_whitelist_fields_from_template`, `_get_work_entries_values`

## `hr.work.entry` (defines)

HR Work Entry

- `name` Char
- `active` Boolean
- `employee_id` Many2one → `hr.employee` (required, index)
- `version_id` Many2one → `hr.version` “Employee Record” (required, index)
- `work_entry_source` Selection (related=version_id.work_entry_source)
- `date` Date (required)
- `duration` Float “Duration”
- `work_entry_type_id` Many2one → `hr.work.entry.type` (index)
- `display_code` Char (related=work_entry_type_id.display_code)
- `code` Char (related=work_entry_type_id.code)
- `external_code` Char (related=work_entry_type_id.external_code)
- `color` Integer (readonly, related=work_entry_type_id.color)
- `state` Selection
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `conflict` Boolean “Conflicts” (store, compute=_compute_conflict)
- `department_id` Many2one → `hr.department` (store, related=employee_id.department_id)
- `amount_rate` Float “Pay rate”
- `country_id` Many2one → `res.country` (related=employee_id.company_id.country_id)

Public methods: `action_split`, `action_validate`, `create`, `get_unusual_days`, `unlink`, `write`

Extension points: `_check_duration`, `_check_if_error`, `_get_leaves_entries_outside_schedule`, `_get_work_entry_type_domain`

## `hr.work.entry.type` (defines)

HR Work Entry Type

- `name` Char (required)
- `display_code` Char “Display Code”
- `code` Char “Payroll Code” (required)
- `external_code` Char
- `color` Integer
- `sequence` Integer
- `active` Boolean “Active”
- `country_id` Many2one → `res.country` “Country”
- `country_code` Char (related=country_id.code)
- `is_leave` Boolean “Time Off”
- `is_work` Boolean “Working Time” (compute=_compute_is_work)
- `amount_rate` Float “Rate”
- `is_extra_hours` Boolean “Added to Monthly Pay”

Extension points: `_check_code_unicity`, `_check_work_entry_type_country`

## `resource.calendar` (extends)


Extension points: `_get_global_attendances`

## `resource.calendar.attendance` (extends)

- `work_entry_type_id` Many2one → `hr.work.entry.type`

## `resource.calendar.leaves` (extends)

- `work_entry_type_id` Many2one → `hr.work.entry.type`

## `hr.work.entry.regeneration.wizard` (defines)

Regenerate Employee Work Entries

- `earliest_available_date` Date “Earliest date” (compute=_compute_earliest_available_date)
- `earliest_available_date_message` Char (readonly)
- `latest_available_date` Date “Latest date” (compute=_compute_latest_available_date)
- `latest_available_date_message` Char (readonly)
- `date_from` Date “From” (required)
- `date_to` Date “To” (required, store, compute=_compute_date_to)
- `employee_ids` Many2many → `hr.employee` “Employees” (required)
- `validated_work_entry_employee_ids` Many2many → `hr.employee` (compute=_compute_validated_work_entry_employee_ids)
- `search_criteria_completed` Boolean (compute=_compute_search_criteria_completed)
- `valid` Boolean (compute=_compute_valid)

Public methods: `regenerate_work_entries`

Extension points: `_check_dates`
