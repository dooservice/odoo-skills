# hr_calendar — Display Working Hours in Calendar

Depends on: hr, calendar.

## `calendar.event` (extends)


Public methods: `get_unusual_days`

Extension points: `_check_employees_availability_for_event`, `_get_events_interval`

## `hr.employee` (extends)


Extension points: `_get_worklocation`

## `res.partner` (extends)


Public methods: `get_working_days_for_all_attendees`, `get_working_hours_for_all_attendees`, `get_worklocation`

Extension points: `_get_employees_from_attendees`, `_get_schedule`, `_get_unusual_days`

## `homework.location.wizard` (defines)

Set Homework Location Wizard

- `work_location_id` Many2one → `hr.work.location` “Location” (required)
- `work_location_name` Char “Location name” (related=work_location_id.name)
- `work_location_type` Selection (related=work_location_id.location_type)
- `employee_id` Many2one → `hr.employee` (required)
- `employee_name` Char (related=employee_id.name)
- `weekly` Boolean
- `date` Date “Date”
- `day_week_string` Char (compute=_compute_day_week_string)

Public methods: `delete_employee_location`, `get_employee_location_info`, `set_employee_location`
