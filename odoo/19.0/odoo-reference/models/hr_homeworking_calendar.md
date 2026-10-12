# hr_homeworking_calendar — Remote Work with calendar

Depends on: hr_homeworking, calendar.

## `hr.employee` (extends)


Extension points: `_get_worklocation`

## `res.partner` (extends)


Public methods: `get_worklocation`

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

Public methods: `set_employee_location`
