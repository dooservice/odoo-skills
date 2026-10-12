# hr_homeworking — Remote Work

Depends on: hr.

## `hr.employee` (extends)

- `monday_location_id` Many2one → `hr.work.location` “Monday”
- `tuesday_location_id` Many2one → `hr.work.location` “Tuesday”
- `wednesday_location_id` Many2one → `hr.work.location` “Wednesday”
- `thursday_location_id` Many2one → `hr.work.location` “Thursday”
- `friday_location_id` Many2one → `hr.work.location` “Friday”
- `saturday_location_id` Many2one → `hr.work.location` “Saturday”
- `sunday_location_id` Many2one → `hr.work.location` “Sunday”
- `exceptional_location_id` Many2one → `hr.work.location` “Current” (compute=_compute_exceptional_location_id)
- `hr_icon_display` Selection
- `today_location_name` Char

Public methods: `get_views`

Extension points: `_get_current_day_location_field`

## `hr.employee.public` (extends)

- `monday_location_id` Many2one → `hr.work.location` “Monday”
- `tuesday_location_id` Many2one → `hr.work.location` “Tuesday”
- `wednesday_location_id` Many2one → `hr.work.location` “Wednesday”
- `thursday_location_id` Many2one → `hr.work.location` “Thursday”
- `friday_location_id` Many2one → `hr.work.location` “Friday”
- `saturday_location_id` Many2one → `hr.work.location` “Saturday”
- `sunday_location_id` Many2one → `hr.work.location` “Sunday”
- `today_location_name` Char

## `hr.employee.location` (defines)

Employee Location

- `work_location_id` Many2one → `hr.work.location` “Location” (required)
- `work_location_name` Char “Location name” (related=work_location_id.name)
- `work_location_type` Selection (related=work_location_id.location_type)
- `employee_id` Many2one → `hr.employee` (required)
- `employee_name` Char (related=employee_id.name)
- `date` Date “Date”
- `day_week_string` Char (compute=_compute_day_week_string)

## `hr.work.location` (extends)


## `res.partner` (extends)


## `res.users` (extends)

- `monday_location_id` Many2one → `hr.work.location` “Mondays” (related=employee_id.monday_location_id)
- `tuesday_location_id` Many2one → `hr.work.location` “Tuesdays” (related=employee_id.tuesday_location_id)
- `wednesday_location_id` Many2one → `hr.work.location` “Wednesdays” (related=employee_id.wednesday_location_id)
- `thursday_location_id` Many2one → `hr.work.location` “Thursdays” (related=employee_id.thursday_location_id)
- `friday_location_id` Many2one → `hr.work.location` “Fridays” (related=employee_id.friday_location_id)
- `saturday_location_id` Many2one → `hr.work.location` “Saturdays” (related=employee_id.saturday_location_id)
- `sunday_location_id` Many2one → `hr.work.location` “Sundays” (related=employee_id.sunday_location_id)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`

Extension points: `_get_employee_fields_to_sync`
