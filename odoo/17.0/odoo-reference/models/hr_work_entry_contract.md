# hr_work_entry_contract — Work Entries - Contract

Depends on: hr_work_entry, hr_contract.

## `hr.contract` (extends)

Employee Contract

- `date_generated_from` Datetime “Generated From” (required, readonly)
- `date_generated_to` Datetime “Generated To” (required, readonly)
- `last_generation_date` Date “Last Generation Date” (readonly)
- `work_entry_source` Selection (required)

Public methods: `generate_work_entries`, `has_static_work_entries`, `write`

Extension points: `_get_attendance_intervals`, `_get_bypassing_work_entry_type_codes`, `_get_contract_work_entries_values`, `_get_default_work_entry_type_id`, `_get_fields_that_recompute_we`, `_get_interval_leave_work_entry_type`, `_get_interval_work_entry_type`, `_get_leave_domain`, `_get_leave_work_entry_type`, `_get_leave_work_entry_type_dates`, `_get_lunch_intervals`, `_get_more_vals_attendance_interval`, `_get_more_vals_leave_interval`, `_get_resource_calendar_leaves`, `_get_sub_leave_domain`, `_get_valid_leave_intervals`, `_get_work_entries_values`

## `hr.employee` (extends)


Public methods: `generate_work_entries`

## `hr.work.entry` (extends)

- `contract_id` Many2one → `hr.contract` “Contract” (required)
- `employee_id` Many2one
- `work_entry_source` Selection (related=contract_id.work_entry_source)

Public methods: `create`, `init`

Extension points: `_check_if_error`, `_get_duration_batch`, `_get_duration_is_valid`, `_get_leaves_entries_outside_schedule`

## `hr.work.entry.type` (extends)

HR Work Entry Type

- `is_leave` Boolean “Time Off”

## `resource.calendar` (extends)


Extension points: `_get_global_attendances`

## `hr.work.entry.regeneration.wizard` (defines)

Regenerate Employee Work Entries

- `earliest_available_date` Date “Earliest date” (compute=_compute_earliest_available_date)
- `earliest_available_date_message` Char (readonly)
- `latest_available_date` Date “Latest date” (compute=_compute_latest_available_date)
- `latest_available_date_message` Char (readonly)
- `date_from` Date “From” (required)
- `date_to` Date “To” (required, store, compute=_compute_date_to)
- `employee_ids` Many2many → `hr.employee` “Employees” (required)
- `validated_work_entry_ids` Many2many → `hr.work.entry` “Work Entries Within Interval” (compute=_compute_validated_work_entry_ids)
- `search_criteria_completed` Boolean (compute=_compute_search_criteria_completed)
- `valid` Boolean (compute=_compute_valid)

Public methods: `regenerate_work_entries`

Extension points: `_check_dates`
