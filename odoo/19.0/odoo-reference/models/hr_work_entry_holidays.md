# hr_work_entry_holidays — Time Off in Payslips

Depends on: hr_holidays, hr_work_entry.

## `hr.leave.type` (extends)

- `work_entry_type_id` Many2one → `hr.work.entry.type` “Work Entry Type”

## `hr.leave` (extends)


Public methods: `action_refuse`, `create`, `write`

Extension points: `_action_user_cancel`, `_get_leaves_on_public_holiday`, `_prepare_resource_leave_vals`

## `hr.version` (extends)

Employee Contract


Extension points: `_get_interval_leave_work_entry_type`, `_get_leave_work_entry_type`, `_get_more_vals_leave_interval`, `_get_sub_leave_domain`

## `hr.work.entry` (extends)

- `leave_id` Many2one → `hr.leave` “Time Off”
- `leave_state` Selection (related=leave_id.state)

Public methods: `action_approve_leave`, `action_refuse_leave`, `write`

Extension points: `_get_leaves_duration_between_two_dates`

## `hr.work.entry.type` (extends)

HR Work Entry Type

- `leave_type_ids` One2many → `hr.leave.type` “Time Off Type”
