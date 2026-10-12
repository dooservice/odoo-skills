# hr_work_entry — Work Entries

Depends on: hr.

## `hr.employee` (extends)

- `external_code` Char “External Code”

Public methods: `generate_work_entries`

## `hr.time.rule` (defines)

Time Rule

- `name` Char (required)
- `description` Text
- `condition_label` Char “Condition” (compute=_compute_condition_label)
- `active` Boolean
- `sequence` Integer
- `country_id` Many2one → `res.country` (store, compute=_compute_country_id)
- `country_code` Char (related=country_id.code)
- `company_id` Many2one → `res.company`
- `employee_domain` Char “Employees”
- `threshold_operator` Selection (required)
- `working_hours_mode` Selection “Working Hours Mode” (required)
- `calendar_source` Selection “Calendar Source” (store, compute=_compute_calendar_source)
- `resource_calendar_id` Many2one → `resource.calendar` “Schedule”
- `expected_hours` Float “Usual work hours” (store, compute=_compute_expected_hours)
- `quantity_period` Selection (store, compute=_compute_quantity_period)
- `week_start` Selection “Week Starts On”
- `apply_monday` Boolean
- `apply_tuesday` Boolean
- `apply_wednesday` Boolean
- `apply_thursday` Boolean
- `apply_friday` Boolean
- `apply_saturday` Boolean
- `apply_sunday` Boolean
- `apply_on_public_holidays` Boolean
- `timing_start` Float “From”
- `timing_stop` Float “To”
- `employee_tolerance` Float
- `employer_tolerance` Float
- `condition_work_entry_type_ids` Many2many → `hr.work.entry.type` “Time Type” (required)
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Set Excess to”
- `country_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_country_work_entry_type_ids)
- `amount_rate` Float “Salary Rate” (store, compute=_compute_amount_rate)

Public methods: `copy_data`

Extension points: `_check_employee_domain`, `_get_applicable_employees`, `_get_pp_frozenset`, `_get_record_interval_local`, `_get_schedule_calendar`, `_get_source_annotation_vals`, `_get_work_intervals`

## `hr.time.rule.source.mixin` (defines)

Time Rule Source Mixin


Public methods: `create`, `write`

Extension points: `_get_pipeline_intervals_local`, `_get_source_extra_fields_domain`, `_get_source_records_for_time_rules`, `_get_time_rule_break_hours`, `_get_time_rule_deficit_already_covered`, `_get_time_rule_deficit_occupied`, `_get_time_rule_end_write_vals`, `_get_time_rule_output_vals`, `_get_time_rule_remainder_vals`, `_get_write_source_extra_source_fields`

## `hr.user.work.entry.employee` (defines)

Work Entries Employee

- `user_id` Many2one → `res.users` (required)
- `employee_id` Many2one → `hr.employee` (required)
- `active` Boolean “Active”
- `is_checked` Boolean

## `hr.version` (extends)


Public methods: `generate_work_entries`, `has_static_work_entries`

Extension points: `_get_attendance_intervals`, `_get_bypassing_work_entry_type_codes`, `_get_default_work_entry_type_id`, `_get_interval_leave_work_entry_type`, `_get_interval_work_entry_type`, `_get_leave_domain`, `_get_leave_work_entry_type`, `_get_leave_work_entry_type_dates`, `_get_more_vals_attendance_interval`, `_get_more_vals_leave_interval`, `_get_no_wet_or_wet_match`, `_get_real_attendance_work_entry_vals`, `_get_real_attendances`, `_get_real_leaves_static`, `_get_real_leaves_static_attendance`, `_get_real_worked_leaves`, `_get_resource_calendar_leaves`, `_get_sub_leave_domain`, `_get_valid_leave_intervals`, `_get_version_work_entries_values`, `_get_work_entries_values`, `_get_work_entry_merge_key`, `_get_work_entry_source_fields`

## `hr.work.entry.type` (defines)

Time Type

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char (required)
- `display_code` Char “Display Code”
- `code` Char “Payroll Code” (required)
- `external_code` Char
- `color` Integer
- `sequence` Integer
- `active` Boolean “Active”
- `country_id` Many2one → `res.country` “Country”
- `country_code` Char (related=country_id.code)
- `count_as` Selection (required)
- `amount_rate` Float “Rate”
- `description` Text
- `resource_calendar_attendance_ids` One2many → `resource.calendar.attendance` (readonly)
- `resource_calendar_selectable` Boolean “Selectable in Working Schedule” (store, compute=_compute_resource_calendar_selectable)

Public methods: `copy_data`

Extension points: `_check_code_unicity`, `_check_country_id`

## `res.company` (extends)

- `external_code` Char “External Code”
- `allowed_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_allowed_work_entry_type_ids)

Extension points: `_get_default_attendance_work_entry_type`

## `res.config.settings` (extends)

- `external_code` Char “External Code” (related=company_id.external_code)

## `resource.calendar` (extends)


Extension points: `_get_reference_hours_per_day`

## `resource.calendar.attendance` (extends)

- `work_entry_type_id` Many2one → `hr.work.entry.type`
- `allowed_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_allowed_work_entry_type_ids)
- `display_code` Char (related=work_entry_type_id.display_code)
- `color` Integer (related=work_entry_type_id.color)

Extension points: `_check_work_entry_type_id`

## `resource.calendar.leaves` (extends)

- `work_entry_type_id` Many2one → `hr.work.entry.type` (store, compute=_compute_work_entry_type_id)
- `allowed_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_allowed_work_entry_type_ids)

## `hr.export.work.entries` (defines)

Export Work Entries

- `reference_year` Integer “Year” (required)
- `reference_month` Selection “Month” (required)
- `company_id` Many2one → `res.company` (required)
- `eligible_employee_line_ids` One2many → `hr.export.work.entries.employee` “Eligible Employees”
- `period_start` Date “Period Start” (store, compute=_compute_period_dates)
- `period_stop` Date “Period Stop” (store, compute=_compute_period_dates)

Public methods: `default_get`, `download_export`

Extension points: `_get_columns`, `_get_contracts_by_employee`, `_get_default_period_dates`, `_get_eligible_employee_lines`, `_get_employees`

## `hr.export.work.entries.employee` (defines)

Work Entry Export Employee

- `export_id` Many2one → `hr.export.work.entries` (required, index)
- `employee_id` Many2one → `hr.employee` (required)
- `version_ids` Many2many → `hr.version` (required, store, compute=_compute_version_ids)

Extension points: `_get_work_entries_by_day_and_code`
