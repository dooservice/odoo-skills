# resource — Resource

Depends on: base, web.

## `res.company` (extends)

- `resource_calendar_ids` One2many → `resource.calendar`
- `resource_calendar_id` Many2one → `resource.calendar`
- `tz` Selection “Timezone” (store, compute=_compute_tz)

Public methods: `create`

Extension points: `_create_resource_calendar`, `_prepare_resource_calendar_values`

## `res.users` (extends)

- `resource_ids` One2many → `resource.resource`
- `resource_calendar_id` Many2one → `resource.calendar` (related=resource_ids.calendar_id)

## `resource.calendar` (defines)

Resource Working Time

- `name` Char (required)
- `active` Boolean “Active”
- `attendance_ids` One2many → `resource.calendar.attendance` (store, compute=_compute_attendance_ids)
- `company_id` Many2one → `res.company`
- `country_id` Many2one (related=company_id.country_id)
- `country_code` Char (related=country_id.code)
- `leave_ids` One2many → `resource.calendar.leaves`
- `full_time_required_hours` Float “Full Time Equivalent” (store, compute=_compute_full_time_required_hours)
- `global_leave_ids` One2many → `resource.calendar.leaves` (store, compute=_compute_global_leave_ids)
- `days_per_week` Float “Days per Week” (store, compute=_compute_days_per_week)
- `hours_per_day` Float “Average Hour per Day” (store, compute=_compute_hours_per_day)
- `hours_per_week` Float “Hours per Week” (store, compute=_compute_hours_per_week)
- `is_fulltime` Boolean “Is Full Time” (compute=_compute_is_fulltime)
- `work_resources_count` Integer “Work Resources count” (compute=_compute_work_resources_count)
- `work_time_rate` Float “Work Time Rate” (store, compute=_compute_work_time_rate)
- `calendar_type` Selection “Calendar Type” (required)
- `reference_calendar_id` Many2one → `resource.calendar` “Reference Calendar”

Public methods: `create`, `default_get`, `get_attendances`, `get_work_duration_data`, `get_work_hours_count`, `is_calendar_referenced`, `plan_days`, `plan_hours`, `write`

Extension points: `_get_attendance_intervals_days_data`, `_get_attendances_by_date`, `_get_attendances_to_unlink`, `_get_closest_work_time`, `_get_default_attendance_ids`, `_get_reference_hours_per_day`, `_get_unusual_days`

## `resource.calendar.attendance` (defines)

Work Detail

- `hour_from` Float “Work from” (required, store, index, compute=_compute_hours)
- `hour_to` Float “Work to” (required, store, compute=_compute_hours)
- `duration_hours` Float “Hours” (store, compute=_compute_duration_hours)
- `calendar_id` Many2one → `resource.calendar` “Resource's Calendar” (required, index)
- `calendar_type` Selection (readonly, related=calendar_id.calendar_type)
- `duration_based` Boolean (store, compute=_compute_duration_based)
- `day_period` Selection (store, compute=_compute_day_period)
- `sequence` Integer
- `dayofweek` Selection (required, store, index, compute=_compute_dayofweek)
- `date` Date
- `recurrency` Boolean
- `recurrency_excluded_occurences` Json
- `recurrency_type` Selection
- `recurrency_interval` Integer “Interval”
- `recurrency_end_type` Selection “Recurrence End Condition”
- `recurrency_count` Integer “Number of Repetitions”
- `recurrency_until` Date “Recurrence End Date” (store, compute=_compute_recurrency_until)

Public methods: `create_ad_hoc`, `create_new_recurrency`, `exclude_multiple_occurences`, `exclude_occurence`, `stop_recurrency`

Extension points: `_check_attendance_for_date`, `_check_attendances`, `_check_attendances_fixed_for_calendar`, `_check_attendances_variable_for_calendar`, `_check_prevent_date_on_excluded_occurences`

## `resource.calendar.leaves` (defines)

Resource Time Off Detail

- `name` Char “Reason”
- `company_id` Many2one → `res.company` “Company” (readonly, store, compute=_compute_company_id)
- `calendar_id` Many2one → `resource.calendar` (store, index, compute=_compute_calendar_id)
- `date_from` Datetime “Start Date” (required)
- `date_to` Datetime “End Date” (required, store, compute=_compute_date_to)
- `resource_id` Many2one → `resource.resource` (index)
- `count_as` Selection

Public methods: `check_dates`, `default_get`

## `resource.mixin` (defines)

Resource Mixin

- `resource_id` Many2one → `resource.resource` (required, index)
- `company_id` Many2one → `res.company` (store, index, related=resource_id.company_id)
- `resource_calendar_id` Many2one → `resource.calendar` (store, index, related=resource_id.calendar_id)
- `tz` Selection “Timezone” (related=resource_id.tz)

Public methods: `copy_data`, `create`

Extension points: `_get_calendars`, `_get_hours_per_day_batch`, `_get_hours_per_week_batch`, `_get_leave_days_data_batch`, `_get_work_days_data_batch`, `_prepare_resource_values`

## `resource.resource` (defines)

Resource

- `name` Char (required)
- `active` Boolean “Active”
- `company_id` Many2one → `res.company` “Company”
- `resource_type` Selection “Type” (required)
- `user_id` Many2one → `res.users` “User”
- `avatar_128` Image (compute=_compute_avatar_128)
- `share` Boolean (related=user_id.share)
- `email` Char (related=user_id.email)
- `phone` Char (related=user_id.phone)
- `time_efficiency` Float “Efficiency Factor” (required)
- `calendar_id` Many2one → `resource.calendar` “Working Time” (required)
- `hours_per_week` Float “Hours per Week” (readonly, related=calendar_id.hours_per_week)
- `hours_per_day` Float “Hours per Day” (readonly, related=calendar_id.hours_per_day)
- `tz` Selection “Timezone” (required)
- `color` Integer

Public methods: `create`, `default_get`, `write`

Extension points: `_get_calendar_data_at`, `_get_calendars_validity_within_period`, `_get_flexible_resource_valid_work_intervals`, `_get_flexible_resource_work_hours`, `_get_flexible_resources_calendars_validity_within_period`, `_get_flexible_resources_default_work_intervals`, `_get_resources_per_tz`, `_get_unavailable_intervals`, `_get_valid_work_intervals`, `_get_work_interval`
