# hr_work_entry — Work Entries

Depends on: hr.

## `hr.employee` (extends)

- `has_work_entries` Boolean (compute=_compute_has_work_entries)

Public methods: `action_open_work_entries`

## `hr.work.entry` (defines)

HR Work Entry

- `name` Char (required, store, compute=_compute_name)
- `active` Boolean
- `employee_id` Many2one → `hr.employee` (required, index)
- `date_start` Datetime “From” (required)
- `date_stop` Datetime “To” (store, compute=_compute_date_stop)
- `duration` Float “Duration” (store, compute=_compute_duration)
- `work_entry_type_id` Many2one → `hr.work.entry.type` (index)
- `code` Char (related=work_entry_type_id.code)
- `external_code` Char (related=work_entry_type_id.external_code)
- `color` Integer (readonly, related=work_entry_type_id.color)
- `state` Selection
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `conflict` Boolean “Conflicts” (store, compute=_compute_conflict)
- `department_id` Many2one → `hr.department` (store, related=employee_id.department_id)

Public methods: `action_validate`, `create`, `init`, `unlink`, `write`

Extension points: `_check_if_error`, `_get_duration_batch`

## `hr.work.entry.type` (defines)

HR Work Entry Type

- `name` Char (required)
- `code` Char “Payroll Code” (required)
- `external_code` Char
- `color` Integer
- `sequence` Integer
- `active` Boolean “Active”

## `hr.user.work.entry.employee` (defines)

Work Entries Employees

- `user_id` Many2one → `res.users` (required)
- `employee_id` Many2one → `hr.employee` (required)
- `active` Boolean “Active”

## `resource.calendar.attendance` (extends)

- `work_entry_type_id` Many2one → `hr.work.entry.type`

## `resource.calendar.leaves` (extends)

- `work_entry_type_id` Many2one → `hr.work.entry.type`
