# hr_calendar — Display Working Hours in Calendar

Depends on: hr, calendar.

## `calendar.event` (extends)


Public methods: `get_unusual_days`

Extension points: `_check_employees_availability_for_event`, `_get_events_interval`

## `res.partner` (extends)


Public methods: `get_working_hours_for_all_attendees`

Extension points: `_get_employees_from_attendees`, `_get_schedule`
