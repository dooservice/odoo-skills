# resource — Resource

Depends on: base, web.

## `res.company` (extends)

- `resource_calendar_ids` One2many → `resource.calendar`
- `resource_calendar_id` Many2one → `resource.calendar`

Public methods: `create`

Extension points: `_create_resource_calendar`, `_prepare_resource_calendar_values`

## `res.users` (extends)

- `resource_ids` One2many → `resource.resource`
- `resource_calendar_id` Many2one → `resource.calendar` (related=resource_ids.calendar_id)

Public methods: `write`

## `resource.calendar` (defines)

Resource Working Time

- `name` Char (required)
- `active` Boolean “Active”
- `attendance_ids` One2many → `resource.calendar.attendance` (store, compute=_compute_attendance_ids)
- `attendance_ids_1st_week` One2many → `resource.calendar.attendance` (compute=_compute_two_weeks_attendance)
- `attendance_ids_2nd_week` One2many → `resource.calendar.attendance` (compute=_compute_two_weeks_attendance)
- `company_id` Many2one → `res.company`
- `leave_ids` One2many → `resource.calendar.leaves`
- `schedule_type` Selection “Schedule Type” (required)
- `duration_based` Boolean “Attendance based on duration”
- `flexible_hours` Boolean “Flexible Hours” (store, compute=_compute_flexible_hours)
- `full_time_required_hours` Float “Full Time Equivalent” (store, compute=_compute_full_time_required_hours)
- `global_leave_ids` One2many → `resource.calendar.leaves` (store, compute=_compute_global_leave_ids)
- `hours_per_day` Float “Average Hour per Day” (store, compute=_compute_hours_per_day)
- `hours_per_week` Float “Hours per Week” (store, compute=_compute_hours_per_week)
- `is_fulltime` Boolean “Is Full Time” (compute=_compute_work_time_rate)
- `two_weeks_calendar` Boolean “Calendar in 2 weeks mode”
- `two_weeks_explanation` Char “Explanation” (compute=_compute_two_weeks_explanation)
- `tz` Selection “Timezone” (required)
- `tz_offset` Char “Timezone offset” (compute=_compute_tz_offset)
- `work_resources_count` Integer “Work Resources count” (compute=_compute_work_resources_count)
- `work_time_rate` Float “Work Time Rate” (compute=_compute_work_time_rate)

Public methods: `copy_data`, `create`, `default_get`, `get_work_duration_data`, `get_work_hours_count`, `plan_days`, `plan_hours`, `switch_based_on_duration`, `switch_calendar_type`

Extension points: `_check_attendance_ids`, `_check_overlap`, `_get_attendance_intervals_days_data`, `_get_closest_work_time`, `_get_days_per_week`, `_get_default_attendance_ids`, `_get_global_attendances`, `_get_hours_for_date`, `_get_hours_per_day`, `_get_hours_per_week`, `_get_two_weeks_attendance`, `_get_unusual_days`, `_get_working_hours`

## `resource.calendar.attendance` (defines)

Work Detail

- `name` Char (required)
- `dayofweek` Selection (required, index)
- `hour_from` Float “Work from” (required, index)
- `hour_to` Float “Work to” (required)
- `duration_hours` Float “Duration (hours)” (store, compute=_compute_duration_hours)
- `duration_days` Float “Duration (days)” (store, compute=_compute_duration_days)
- `calendar_id` Many2one → `resource.calendar` “Resource's Calendar” (required, index)
- `duration_based` Boolean (related=calendar_id.duration_based)
- `day_period` Selection (required)
- `week_type` Selection
- `two_weeks_calendar` Boolean “Calendar in 2 weeks mode” (related=calendar_id.two_weeks_calendar)
- `display_type` Selection
- `sequence` Integer

Public methods: `get_week_type`

Extension points: `_check_day_period`

## `resource.calendar.leaves` (defines)

Resource Time Off Detail

- `name` Char “Reason”
- `company_id` Many2one → `res.company` “Company” (readonly, store, compute=_compute_company_id)
- `calendar_id` Many2one → `resource.calendar` (store, index, compute=_compute_calendar_id)
- `date_from` Datetime “Start Date” (required)
- `date_to` Datetime “End Date” (required, store, compute=_compute_date_to)
- `resource_id` Many2one → `resource.resource` (index)
- `time_type` Selection

Public methods: `check_dates`, `default_get`

## `resource.mixin` (defines)

Resource Mixin

- `resource_id` Many2one → `resource.resource` (required, index)
- `company_id` Many2one → `res.company` (store, index, related=resource_id.company_id)
- `resource_calendar_id` Many2one → `resource.calendar` (store, index, related=resource_id.calendar_id)
- `tz` Selection “Timezone” (related=resource_id.tz)

Public methods: `copy_data`, `create`, `list_leaves`

Extension points: `_get_calendars`, `_get_leave_days_data_batch`, `_get_work_days_data_batch`, `_prepare_resource_values`

## `resource.resource` (defines)

Resources

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
- `calendar_id` Many2one → `resource.calendar` “Working Time”
- `tz` Selection “Timezone” (required)

Public methods: `copy_data`, `create`, `default_get`, `write`

Extension points: `_get_calendar_at`, `_get_calendars_validity_within_period`, `_get_flexible_resource_valid_work_intervals`, `_get_flexible_resource_work_hours`, `_get_flexible_resources_calendars_validity_within_period`, `_get_flexible_resources_default_work_intervals`, `_get_unavailable_intervals`, `_get_valid_work_intervals`, `_get_work_interval`
