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
- `company_id` Many2one → `res.company`
- `attendance_ids` One2many → `resource.calendar.attendance` (store, compute=_compute_attendance_ids)
- `leave_ids` One2many → `resource.calendar.leaves`
- `global_leave_ids` One2many → `resource.calendar.leaves` (store, compute=_compute_global_leave_ids)
- `hours_per_day` Float “Average Hour per Day”
- `tz` Selection “Timezone” (required)
- `tz_offset` Char “Timezone offset” (compute=_compute_tz_offset)
- `two_weeks_calendar` Boolean “Calendar in 2 weeks mode”
- `two_weeks_explanation` Char “Explanation” (compute=_compute_two_weeks_explanation)

Public methods: `copy`, `default_get`, `get_work_duration_data`, `get_work_hours_count`, `plan_days`, `plan_hours`, `switch_calendar_type`

Extension points: `_check_attendance`, `_check_attendance_ids`, `_check_overlap`, `_get_closest_work_time`, `_get_days_data`, `_get_global_attendances`, `_get_max_number_of_hours`, `_get_resources_day_total`, `_get_unusual_days`

## `resource.calendar.attendance` (defines)

Work Detail

- `name` Char (required)
- `dayofweek` Selection (required, index)
- `date_from` Date “Starting Date”
- `date_to` Date “End Date”
- `hour_from` Float “Work from” (required, index)
- `hour_to` Float “Work to” (required)
- `calendar_id` Many2one → `resource.calendar` “Resource's Calendar” (required)
- `day_period` Selection (required)
- `resource_id` Many2one → `resource.resource`
- `week_type` Selection
- `two_weeks_calendar` Boolean “Calendar in 2 weeks mode” (related=calendar_id.two_weeks_calendar)
- `display_type` Selection
- `sequence` Integer

Public methods: `get_week_type`

## `resource.resource` (defines)

Resources

- `name` Char (required)
- `active` Boolean “Active”
- `company_id` Many2one → `res.company` “Company”
- `resource_type` Selection “Type” (required)
- `user_id` Many2one → `res.users` “User”
- `time_efficiency` Float “Efficiency Factor” (required)
- `calendar_id` Many2one → `resource.calendar` “Working Time” (required)
- `tz` Selection “Timezone” (required)

Public methods: `copy`, `create`, `default_get`, `write`

Extension points: `_get_calendars_validity_within_period`, `_get_unavailable_intervals`, `_get_valid_work_intervals`, `_get_work_interval`

## `resource.calendar.leaves` (defines)

Resource Time Off Detail

- `name` Char “Reason”
- `company_id` Many2one → `res.company` “Company” (readonly, store, compute=_compute_company_id)
- `calendar_id` Many2one → `resource.calendar` (store, index, compute=_compute_calendar_id)
- `date_from` Datetime “Start Date” (required)
- `date_to` Datetime “End Date” (required)
- `resource_id` Many2one → `resource.resource` (index)
- `time_type` Selection

Public methods: `check_dates`, `default_get`, `onchange_resource`

## `resource.mixin` (defines)

Resource Mixin

- `resource_id` Many2one → `resource.resource` (required, index)
- `company_id` Many2one → `res.company` (store, index, related=resource_id.company_id)
- `resource_calendar_id` Many2one → `resource.calendar` (store, index, related=resource_id.calendar_id)
- `tz` Selection “Timezone” (related=resource_id.tz)

Public methods: `copy_data`, `create`, `list_leaves`, `list_work_time_per_day`

Extension points: `_get_leave_days_data_batch`, `_get_work_days_data_batch`, `_prepare_resource_values`

## `resource.calendar` (extends)
