# Attendances: variations

Less common attendance cases, after the standard flow of [attendance.md](attendance.md).
Its `## Versions` table and settings apply here too.

**At a glance**

- Apps: `hr_holidays_attendance`, `hr_presence`, `hr_homeworking` (17.0-19.0; in `hr`
  from 20.0), `hr_homeworking_calendar` (18.0, 19.0), `hr_calendar` (18.0+).
- Names that change by version: Extra Hours time off type
  `hr_holidays_attendance.holiday_status_extra_hours` (16.0-18.0),
  `hr_holidays.holiday_status_extra_hours` (19.0), none and an allocation from the rule
  (20.0); accrual `frequency_hourly_source = 'attendance'` (17.0, 18.0), `frequency =
  'worked_hours'` (19.0+).
- Sections: Variations (time off from extra hours, accrual on worked hours, adjust the
  balance by hand, presence control, remote work).

## Variations

- **Take time off from extra hours** (`hr_holidays_attendance`):
  - 16.0-19.0: the time off type `Extra Hours` (16.0-18.0
    `hr_holidays_attendance.holiday_status_extra_hours`, 19.0
    `hr_holidays.holiday_status_extra_hours`) has Deduct Extra Hours
    (`overtime_deductible`) and no allocation; requesting it, in hours, takes the hours
    from `total_overtime` and is refused beyond the balance. In 16.0, 17.0 it is archived
    while no company counts extra hours. In 19.0 only overtime lines of rules with Give
    back as time off (`compensable_as_leave`) and `approved` can be taken.
  - A type with Deduct Extra Hours that needs an allocation turns extra hours into an
    allocation instead: the allocated hours come off the balance at creation.
  - 20.0: no deductible type. Set Allocate % (`leave_compensation_rate`) and Allocate to
    (`allocation_type_id`, a time type that requires an allocation) on an automatic rule:
    validated extra hours create or increase an allocation of that type.

  20.0, on the automatic rule:

  ```python
  rule.write({'leave_compensation_rate': 1.0, 'allocation_type_id': comp_type.id})
  ```

  19.0, a request of the Extra Hours type:

  ```python
  leave = env['hr.leave'].with_user(user).create({
      'holiday_status_id': env.ref('hr_holidays.holiday_status_extra_hours').id, 'employee_id': employee.id,
      'request_date_from': '<YYYY-MM-DD>', 'request_date_to': '<YYYY-MM-DD>',
      'request_hour_from': 8.0, 'request_hour_to': 12.0,
  })
  ```

  16.0-18.0:

  ```python
  leave = env['hr.leave'].with_user(user).create({
      'holiday_status_id': env.ref('hr_holidays_attendance.holiday_status_extra_hours').id, 'employee_id': employee.id,
      'request_date_from': '<YYYY-MM-DD>', 'request_date_to': '<YYYY-MM-DD>',
      'request_unit_hours': True, 'request_hour_from': 8.0, 'request_hour_to': 12.0,
  })
  ```

  16.0 and 17.0 take the hours as selection values: `'8'` and `'12'`.

- **Accrual on worked hours**: an accrual plan level accrues per hour attended
  (17.0, 18.0 `frequency_hourly_source = 'attendance'`; 19.0+ `frequency = 'worked_hours'`).
- **Adjust the balance by hand** (16.0-18.0): an `hr.attendance.overtime` with
  `adjustment=True` and a signed `duration`, from the employee's extra hours smart
  button. 19.0 edits `manual_duration` on the line; 20.0 edits or refuses the output
  attendance.
- **Presence control** (`hr_presence`): the employee's presence (`hr_presence_state`)
  comes from login, attendance, emails sent or IP. The managers' presence report
  (16.0, 17.0: Employees ‣ Reporting ‣ Presence; 18.0+: the Presence filters on the
  employees list) lists absent employees and gives actions to mark them present or
  absent (`action_set_present`, `action_set_absent`), send an SMS, log a note (18.0+;
  16.0, 17.0: send an email) or open a time off request.
- **Remote work** (`hr_homeworking` 17.0-19.0; `hr` in 20.0): create work locations
  (Employees ‣ Configuration ‣ Work Locations, `location_type` `home`, `office`,
  `other`), set each weekday on the employee (Remote Work group, 19.0+: Usual Work
  Location: `monday_location_id` to `sunday_location_id`) and exceptions for one date
  (`hr.employee.location`). The employee's icon and `work_location_name` show today's
  location. With Calendar (`hr_homeworking_calendar` 18.0, 19.0; `hr_calendar` in 20.0)
  the location is set from the calendar's day header for that day or every week, and
  `hr_calendar` (18.0+) marks attendees outside their working hours in the event form.

  ```python
  home = env['hr.work.location'].create({'name': 'Home', 'location_type': 'home', 'address_id': employee.address_id.id})
  employee.write({'friday_location_id': home.id})
  env['hr.employee.location'].create({'employee_id': employee.id, 'work_location_id': home.id, 'date': '<YYYY-MM-DD>'})
  ```
