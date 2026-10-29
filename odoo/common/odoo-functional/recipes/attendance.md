# Attendances, extra hours and presence

An attendance (`hr.attendance`) is one check-in and check-out of an employee; its worked
hours are compared with the employee's working schedule to count extra hours. Employees
check in from the systray, from a kiosk (badge or PIN) or are encoded by an officer.
Extra hours can be approved, given back as time off (`hr_holidays_attendance`) and
compared with timesheets (`hr_timesheet_attendance`). Presence control (`hr_presence`)
and remote work locations (`hr_homeworking`, in `hr` from 20.0) show who is at work
today. Employees, departments and time off themselves are in
[employees-and-expenses.md](employees-and-expenses.md); timesheets in
[projects-and-timesheets.md](projects-and-timesheets.md). Payroll and the Enterprise
work entry views are left out. Extra hours changed model three times (16.0-17.0, 18.0,
19.0, 20.0): check `## Versions` before every step.

## Before you start

- Apps: `hr_attendance`; `hr_holidays_attendance` (installed by itself with Time Off) to
  take time off from extra hours; `hr_timesheet_attendance` (with Timesheets) for the
  comparison report; `hr_presence` for presence by email and IP; `hr_homeworking` for
  remote work (17.0-19.0; part of `hr` in 20.0).
- Settings (Attendances ‣ Configuration; 19.0+: Configuration ‣ Settings):
  - Check-in: `attendance_from_systray` (17.0+), `attendance_kiosk_mode` (`barcode`,
    `barcode_manual`, `manual`), `attendance_barcode_source` (`scanner`, `front`, `back`),
    `attendance_kiosk_use_pin` (17.0+; 16.0: `group_attendance_use_pin`),
    `attendance_kiosk_delay`.
  - Extra hours: `hr_attendance_overtime` and `overtime_start_date` (16.0, 17.0 only: no
    extra hours before that date); `overtime_company_threshold` and
    `overtime_employee_threshold` in minutes (16.0-19.0); `attendance_overtime_validation`
    (`no_validation`, `by_manager`; 18.0, 19.0); `attendance_validation` (20.0, see
    step 6).
  - Automation (18.0+): `auto_check_out` with `auto_check_out_tolerance` (hours after the
    schedule; 20.0 also `auto_check_out_mode`), `absence_management` (a day without
    attendance counts as negative extra hours). 19.0+: `attendance_device_tracking`
    (location and device of each check-in); 20.0: `attendance_capture_check_in`,
    `attendance_break_management`, `single_check_in`.
  - Presence (Employees ‣ Configuration ‣ Settings): `hr_presence_control_login`,
    `hr_presence_control_email` with `hr_presence_control_email_amount`,
    `hr_presence_control_ip` with `hr_presence_control_ip_list`, and
    `module_hr_presence` (installs `hr_presence`: ask first). 18.0, 19.0:
    `module_hr_attendance` (based on attendances); 20.0: `hr_presence_control_attendance`.
- Read first:

20.0:

```python
company = env.company
print(company.read(['attendance_kiosk_mode', 'attendance_barcode_source', 'attendance_kiosk_delay', 'attendance_kiosk_use_pin',
                    'attendance_from_systray', 'attendance_validation', 'attendance_work_entry_type_id',
                    'auto_check_out', 'absence_management', 'hr_presence_control_login', 'hr_presence_control_email',
                    'hr_presence_control_ip']))
print(env['hr.employee'].search_read([('company_id', '=', company.id)], ['name', 'user_id', 'resource_calendar_id', 'attendance_state', 'total_overtime', 'hr_presence_state']))
print(env['hr.attendance'].search_read([('check_out', '=', False)], ['employee_id', 'check_in', 'state']))
```

18.0, 19.0: read `attendance_overtime_validation`, `overtime_company_threshold` and
`overtime_employee_threshold` in place of `attendance_validation` and
`attendance_work_entry_type_id`, and drop `state`. 16.0, 17.0:

```python
company = env.company
print(company.read(['attendance_kiosk_mode', 'attendance_barcode_source', 'attendance_kiosk_delay',
                    'hr_attendance_overtime', 'overtime_start_date', 'overtime_company_threshold',
                    'overtime_employee_threshold']))
print(env['hr.employee'].search_read([('company_id', '=', company.id)], ['name', 'user_id', 'resource_calendar_id', 'attendance_state', 'total_overtime', 'hr_presence_state']))
print(env['hr.attendance'].search_read([('check_out', '=', False)], ['employee_id', 'check_in']))
```

17.0 also has `attendance_kiosk_use_pin` and `attendance_from_systray`. In 16.0 and
17.0 the presence settings are system parameters (`hr.hr_presence_control_login`,
`hr_presence.hr_presence_control_email`, `hr_presence.hr_presence_control_ip`).

## The standard flow

The order of Odoo's Attendances documentation: settings, badges and PINs, daily check-in
and check-out, corrections, extra hours, then reporting.

1. **Configure the check-in.** Attendances ‣ Configuration (19.0+: Configuration ‣
   Settings).

   20.0:

   ```python
   env['res.config.settings'].create({
       'attendance_kiosk_mode': 'barcode_manual', 'attendance_barcode_source': 'front', 'attendance_kiosk_delay': 10,
       'attendance_kiosk_use_pin': True, 'attendance_validation': 'manual_validation',
   }).execute()
   env.cr.commit()
   ```

   18.0, 19.0: the same with `'attendance_overtime_validation': 'by_manager'` in place of
   `attendance_validation`. 16.0, 17.0:

   ```python
   env['res.config.settings'].create({
       'attendance_kiosk_mode': 'barcode_manual', 'attendance_barcode_source': 'front', 'attendance_kiosk_delay': 10,
       'attendance_kiosk_use_pin': True,
       'hr_attendance_overtime': True, 'overtime_start_date': '<YYYY-MM-DD>',
   }).execute()
   env.cr.commit()
   ```

   In 16.0 the PIN switch is `group_attendance_use_pin` instead of
   `attendance_kiosk_use_pin`.
   In 16.0 and 17.0 extra hours are counted only with `hr_attendance_overtime` and only
   from `overtime_start_date`; from 18.0 they are always counted.

2. **Give each employee a badge, a PIN and a schedule.** Employees ‣ employee ‣ HR
   Settings tab (18.0+: Settings tab): Badge ID (Generate), PIN; Working Hours on Work
   Information. From 17.0 the Attendance approver (`attendance_manager_id`) is set
   there too.

   ```python
   employee.write({'pin': '<4 digits>', 'resource_calendar_id': calendar.id})
   employee.generate_random_barcode()
   employee.attendance_manager_id = manager_user.id
   env.cr.commit()
   ```

   16.0 has no `attendance_manager_id`: leave that line out.

   Extra hours are measured against `resource_calendar_id`; an employee without one
   counts every hour as worked time.

3. **Check in and check out.** The employee uses the check-in button in the systray
   (17.0+; 16.0: Attendances ‣ Check In / Check Out) or the kiosk: Attendances ‣ Kiosk
   Mode opens it (17.0+ a public URL, `attendance_kiosk_url`, to open on the shared
   device), where the employee scans the badge or picks their name and types the PIN.

   ```python
   employee = employee.with_user(user)
   attendance = employee._attendance_action_change({'mode': 'manual'})
   print(employee.attendance_state, attendance.check_in)
   attendance = employee._attendance_action_change({'mode': 'manual'})
   env.cr.commit()
   print(employee.attendance_state, attendance.check_out, attendance.worked_hours)
   ```

   The first call checks in, the second checks out. 16.0 takes no argument:
   `employee._attendance_action_change()`.

   Leaves the employee `checked_in`, then `checked_out` with `worked_hours` stored.
   17.0+ records how (`in_mode`/`out_mode`: `kiosk`, `systray`, `manual`, and
   `auto_check_out` from 18.0) and, with device tracking, where.

4. **Correct or encode attendances.** Attendances ‣ Attendances (17.0: Overview; 18.0,
   19.0: Management; 20.0: Management ‣ Attendances) ‣ New, by an attendance officer.

   ```python
   attendance = env['hr.attendance'].create({
       'employee_id': employee.id,
       'check_in': '<YYYY-MM-DD> 08:00:00', 'check_out': '<YYYY-MM-DD> 18:00:00',   # UTC
   })
   env.cr.commit()
   ```

   Datetimes are stored in UTC: convert from the employee's time zone. An employee has
   at most one open attendance and attendances never overlap; Odoo refuses otherwise.

5. **Read the extra hours.** The attendance shows Worked Extra Hours (`overtime_hours`,
   17.0+); the employee's balance is `total_overtime`.

   20.0, the output attendances of the automatic rules:

   ```python
   print(env['hr.attendance'].search_read([('source_attendance_id', '=', attendance.id)], ['work_entry_type_id', 'worked_hours', 'time_rule_id', 'state']))
   print(employee.total_overtime)
   ```

   19.0, the overtime lines:

   ```python
   print(attendance.overtime_hours)
   print(env['hr.attendance.overtime.line'].search_read([('employee_id', '=', employee.id)], ['date', 'status', 'duration', 'manual_duration', 'rule_ids', 'amount_rate']))
   print(employee.total_overtime)
   ```

   16.0-18.0, one row per day:

   ```python
   print(env['hr.attendance.overtime'].search_read([('employee_id', '=', employee.id)], ['date', 'duration', 'adjustment']))
   print(employee.total_overtime)
   ```

   17.0 and 18.0 also show `attendance.overtime_hours`.
   - 16.0-18.0: the difference between worked and scheduled hours of the day, within
     the company's tolerances.
   - 19.0: the rules of the employee's Overtime Ruleset (Attendances ‣ Configuration ‣
     Overtime Rulesets; `ruleset_id` on the employee's version, default `Default Ruleset`
     with an Employee Schedule Rule and a Non Working Days Rule). Each rule is based on
     quantity (hours beyond the schedule or a fixed amount per day or week) or timing
     (non-working days, time off, outside a schedule), with a pay rate and tolerances.
   - 20.0: Automatic Rules (Attendances ‣ Configuration ‣ Automatic Rules,
     `hr.time.rule`, default `Employee Schedule Rule`) run on validated attendances and
     create output attendances of the Overtime time type; `total_overtime` sums them.

6. **Approve.** Only when approval is on: 18.0, 19.0 with `attendance_overtime_validation =
   'by_manager'`, 20.0 with `attendance_validation` other than `no_validation`.
   Attendances ‣ Management, filter To Approve, Approve or Refuse; by the attendance
   approver or an attendance manager.

   20.0:

   ```python
   attendance.with_user(manager_user).action_validate()
   env.cr.commit()
   ```

   Refuse with `action_refuse()`, back to draft with `action_reset_to_draft()`. 18.0,
   19.0:

   ```python
   attendance.with_user(manager_user).action_approve_overtime()
   env.cr.commit()
   ```

   Refuse with `action_refuse_overtime()`.

   18.0 leaves `overtime_status` `approved` and `validated_overtime_hours` (editable) in
   the balance; 19.0 approves the attendance's overtime lines (`status` `approved`).
   20.0 leaves the attendance `validated`, which runs the automatic rules; with
   `tolerance_validation` only attendances outside `attendance_validation_tolerance`
   wait, and with `no_validation` attendances are created `validated`. 16.0, 17.0 have
   no approval: extra hours count at once.

7. **Compare attendances with timesheets.** Timesheets ‣ Reporting ‣ Timesheets /
   Attendance Analysis (16.0: Timesheet / Attendance), with `hr_timesheet_attendance`.

   ```python
   print(env['hr.timesheet.attendance.report'].search_read(
       [('date', '>=', '<YYYY-MM-DD>')],
       ['employee_id', 'date', 'total_attendance', 'total_timesheet', 'total_difference', 'cost_difference']))
   ```

   16.0 groups by user: read `user_id` in place of `employee_id`.

   One row per employee (16.0: user) and day; a positive `total_difference` means hours
   present but not logged on any task.

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

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Check in | Check In / Check Out menu, kiosk | systray, kiosk URL | same | same, systray off by default | same, systray on by default |
| Extra hours counted | with `hr_attendance_overtime`, from `overtime_start_date` | same | always | always, by ruleset | by automatic rules (`hr.time.rule`) |
| Extra hours stored in | `hr.attendance.overtime` | same | same | `hr.attendance.overtime.line` | output `hr.attendance` (`source_attendance_id`) |
| Approval | none | none | `attendance_overtime_validation`, `overtime_status` | same, on the lines | `attendance_validation`, attendance `state` |
| Auto check-out, absences | no | no | yes | yes | yes, also at a fixed time |
| Time off from extra hours | `Extra Hours` type | same | same | same, compensable rules only | allocation from the rule |
| Remote work | none | `hr_homeworking` | same, calendar wizard | same | in `hr` and `hr_calendar` |
| Presence report | Employees ‣ Reporting ‣ Presence | same | filters on employees | same | same |

## Verify

```python
employee.invalidate_recordset()
print(employee.attendance_state, employee.total_overtime, employee.hr_presence_state)
print(env['hr.attendance'].search_read([('employee_id', '=', employee.id)],
      ['check_in', 'check_out', 'worked_hours', 'state', 'time_rule_id'], limit=10, order='check_in desc'))
```

18.0, 19.0: read `overtime_hours`, `overtime_status` and `validated_overtime_hours` in
place of `state` and `time_rule_id`; 17.0: `overtime_hours` only; 16.0: none of them.

## Pitfalls

- An employee stays `checked_in` overnight when they forget to check out: 18.0+ turn on
  `auto_check_out`; otherwise an officer sets `check_out` on the open attendance.
- Extra hours look wrong after a schedule change: they are computed when the attendance
  is written. 19.0 regenerates them per ruleset (`action_regenerate_overtimes`); on
  other versions rewrite the attendances' times through the interface.
- 16.0, 17.0: no extra hours appear until `hr_attendance_overtime` is on, and never
  before `overtime_start_date`; the Extra Hours time off type stays archived meanwhile.
- 19.0: `attendance_from_systray` defaults to off; employees see no check-in button
  until it is turned on.
- The shell runs as superuser: check-ins and approvals made there skip the access rules.
  Act `with_user()` as the employee and the approver, as above.
- Attendances feed payroll and time off: refuse or reset them with Odoo's buttons, never
  delete validated ones or write `state` directly.
