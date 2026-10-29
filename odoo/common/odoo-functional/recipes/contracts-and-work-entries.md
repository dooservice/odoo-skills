# Contracts and work entries

The employment terms of each employee (start and end, wage, contract type, working
schedule) and the work entries that turn that schedule and the approved time off into
the days and hours payroll reads. Up to 18.0 the terms are an `hr.contract` record
(`hr_contract`); from 19.0 they are fields of the employee, kept as dated versions
(`hr.version`, in `hr`). Work entries (`hr_work_entry`) are generated from the contract
or version; in Community they are read from the employee and validated, payslips and
the Work Entries app are Enterprise and left out. 20.0 Community keeps only the work
entry types (Time Types). Employees and time off are in
[employees-and-expenses.md](employees-and-expenses.md); overtime and attendance in
[attendance.md](attendance.md).

## Before you start

- Apps: `hr_contract` (16.0-18.0), `hr_work_entry` with `hr_work_entry_contract`
  (16.0-18.0) and `hr_work_entry_holidays` (16.0-19.0, installed with Time Off). From
  19.0 contracts are in `hr` and generation is in `hr_work_entry`.
- Access: the contract manager group (`hr_contract.group_hr_contract_manager`, 16.0-18.0)
  or Employees: Administrator (`hr.group_hr_manager`, 19.0+: the Payroll tab).
- Settings: Employees ‣ Configuration ‣ Settings, Contract Expiry Notice Period
  (`contract_expiration_notice_period`, days, 17.0+; 16.0 fixed at 7) and Work Permit
  Expiry Notice Period (`work_permit_expiration_notice_period`).
- Read first:

19.0, 20.0:

```python
employee = env['hr.employee'].search([('name', '=', '<employee>')])
print(employee.resource_calendar_id.name, employee.department_id.name, employee.job_id.name)
print(employee.version_ids.read(['date_version', 'contract_date_start', 'contract_date_end', 'wage', 'contract_type_id']))
print(env['hr.contract.type'].search_read([], ['name']))
```

16.0-18.0:

```python
employee = env['hr.employee'].search([('name', '=', '<employee>')])
print(employee.resource_calendar_id.name, employee.department_id.name, employee.job_id.name)
print(env['hr.contract'].search_read([('employee_id', '=', employee.id)],
      ['name', 'state', 'kanban_state', 'date_start', 'date_end', 'wage', 'resource_calendar_id']))
print(env['hr.contract.type'].search_read([], ['name']))
```

## The standard flow

1. **Contract (16.0-18.0).** Employees ‣ the employee ‣ Contract smart button ‣ New, or
   Employees ‣ Employees ‣ Contracts (18.0: Employees ‣ Contracts) ‣ New.

   ```python
   contract = env['hr.contract'].create({
       'name': '<employee> contract', 'employee_id': employee.id,
       'date_start': '<YYYY-MM-DD>', 'date_end': False,
       'wage': <monthly wage>, 'contract_type_id': contract_type.id,
       'resource_calendar_id': employee.resource_calendar_id.id,
       'hr_responsible_id': env.user.id,
   })
   ```

   Leaves it `draft` (New). Department and job come from the employee.

2. **Start it.** Click Running on the status bar.

   ```python
   contract.write({'state': 'open'})
   env.cr.commit()
   print(employee.contract_id == contract)
   ```

   Leaves it `open`; it becomes the employee's current contract (`contract_id`) and its
   working schedule becomes the employee's. A contract that starts later: leave it New
   and set the kanban state to green (`kanban_state='done'`, 18.0 Ready); the daily
   scheduled action opens it on `date_start`. One employee cannot have two contracts
   that overlap outside New and Cancelled.

3. **Terms of the employee (19.0+).** Employees ‣ the employee ‣ Payroll tab ‣ Contract
   Overview: Contract start and end dates, Wage, Contract Type, Working Hours. Load a
   Template fills them from Employees ‣ Configuration ‣ Recruitment ‣ Contract Templates.

   ```python
   employee.write({
       'contract_date_start': '<YYYY-MM-DD>', 'contract_date_end': False,
       'wage': <monthly wage>, 'contract_type_id': contract_type.id,
   })
   ```

   Writes the employee's current version. An employee without `contract_date_start` is
   shown as Not Employed.

4. **A change from a date (19.0+).** On the versions timeline at the top of the employee
   form, add a version with its effective date, then change the fields; earlier dates
   keep the old values.

   ```python
   version = employee.create_version({'date_version': '<YYYY-MM-DD>', 'wage': <new wage>})
   env.cr.commit()
   print(employee.version_ids.mapped(lambda v: (v.date_version, v.wage)))
   ```

   `create_version` copies the version in force on that date. If a version already has
   that exact date, it returns it unchanged: write on it instead. Up to 18.0 a change of
   terms is a new contract: close the current one (step 6) and start another.

5. **Work entries (16.0-19.0).** Nothing to do by hand: the daily scheduled action
   "Generate Missing Work Entries" fills the current month for every running contract
   (19.0: every version in contract), one entry per working period of the schedule
   (`WORK100`, Attendance). Open them from the employee's Work Entries smart button
   (calendar, list).

   ```python
   entries = employee.generate_work_entries('<YYYY-MM-01>', '<YYYY-MM-31>')
   env.cr.commit()
   print(entries.read(['date', 'work_entry_type_id', 'duration', 'state']))
   ```

   The block is for 19.0; in 16.0-18.0 read `date_start` and `date_stop` instead of
   `date`. Leaves the entries `draft`.

6. **Time off in work entries (16.0-19.0).** Set Work Entry Type
   (`work_entry_type_id`) on each time off type (Time Off ‣ Configuration ‣ Time Off
   Types). Approving a request replaces the attendance entries of those hours with
   entries of that type; refusing or cancelling it puts them back.

   ```python
   leave_type.work_entry_type_id = env['hr.work.entry.type'].search([('code', '=', 'LEAVE100')], limit=1)
   ```

   20.0 has no separate field: the time type is itself a work entry type, set up under
   Employees ‣ Configuration ‣ Time Management ‣ Time Types.

7. **Check and validate.** Community has no validate button: Payroll (Enterprise)
   validates the entries of a period when it computes payslips. Check them in the
   employee's work entries, conflicts first; without Payroll, validate from the shell.

   ```python
   ok = entries.action_validate()
   print(ok, entries.filtered(lambda e: e.state == 'conflict').read(['work_entry_type_id', 'duration']))
   ```

   Leaves them `validated`, or `conflict` when entries overlap (19.0: more than 24 hours
   on one day), a type is missing or a time off falls outside the schedule; resolve the
   conflicting entries and validate again.

8. **End the contract.** 16.0-18.0: set End Date. The daily scheduled action warns the
   HR responsible with an activity and turns the kanban state red (`blocked`) when the
   end is within the notice period, and sets `close` (Expired) on `date_end`; Expired on
   the status bar does it at once. 19.0+: set `contract_date_end` on the Payroll tab; the
   same notice period schedules the reminder.

## Variations

- Org chart: the hierarchy comes from each employee's Manager (`parent_id`). The
  employee form shows the manager chain and the direct reports; Employees ‣ Employees ‣
  Org Chart (17.0, 18.0) and the hierarchy view of Employees (19.0, 20.0) show the whole
  tree, where dragging a card changes the manager.
- Contract history (16.0-18.0): Employees ‣ Employees ‣ Contracts groups the contracts by
  employee (`hr.contract.history`).
- Regenerate work entries after a schedule change (16.0-19.0): the regeneration wizard
  (`hr.work.entry.regeneration.wizard`) is opened from the Enterprise Work Entries
  view; in Community call `employee.generate_work_entries(start, stop, force=True)`
  for entries that are not validated.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Contract record | `hr.contract` (`hr_contract`) | same | same | fields of `hr.version`, on the employee | same |
| Contracts menu | Employees ‣ Employees ‣ Contracts (history) | Employees ‣ Employees ‣ Contracts | Employees ‣ Contracts | Payroll tab, Contract Templates | same |
| Change from a date | new contract | same | same | `create_version` | same |
| Expiry notice | 7 days, fixed | setting | setting | setting | setting |
| Kanban state labels | Grey, Green, Red | same | Ongoing, Ready, Warning | none | none |
| Work entry dates | `date_start`, `date_stop` | same | same | `date`, `duration` | no work entries in Community |
| Work entry states | `draft`, `validated`, `conflict`, `cancelled` | same | same | same, labelled New, In Payslip | none |
| Generation module | `hr_work_entry_contract` | same | same | `hr_work_entry` | none |
| Time off work entry type | on time off type | same | same | same | the time type is a work entry type |
| Org chart | employee form only | menu and hierarchy view | same | hierarchy view (`hr_org_chart`) | hierarchy view (`hr`) |

## Verify

20.0:

```python
print(employee.version_id.read(['date_version', 'contract_date_start', 'contract_date_end', 'wage']))
```

19.0:

```python
print(employee.version_id.read(['date_version', 'contract_date_start', 'contract_date_end', 'wage']))
for entry in env['hr.work.entry'].search([('employee_id', '=', employee.id)]):
    print(entry.date, entry.work_entry_type_id.code, entry.duration, entry.state)
```

16.0-18.0:

```python
print(employee.contract_id.read(['name', 'state', 'kanban_state', 'date_start', 'date_end', 'wage']))
for entry in env['hr.work.entry'].search([('employee_id', '=', employee.id)]):
    print(entry.date_start, entry.work_entry_type_id.code, entry.duration, entry.state)
```

## Pitfalls

- "An employee can only have one contract at the same time" (16.0-18.0): an Expired
  contract without end date overlaps the new one. Set `date_end` on the old contract.
- 16.0-18.0: changing the contract's working schedule also changes the employee's;
  editing the employee's schedule does not change the contract, and the contract shows
  a calendar mismatch warning. Change it on the contract.
- No work entries on the employee: the contract is not Running (or Expired), or the
  version has no contract start date (19.0+). Work entries are only generated inside
  the contract dates.
- Validated work entries cannot be deleted ("This work entry is validated") and
  generation skips them. Change them only through Payroll (Enterprise), never by
  writing `state`.
- 19.0+: writing on the employee changes the version in force today, not the history;
  for a change from another date use `create_version`.
