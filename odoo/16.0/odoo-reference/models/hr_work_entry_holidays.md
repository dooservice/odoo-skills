# hr_work_entry_holidays — Time Off in Payslips

Depends on: hr_holidays, hr_work_entry_contract.

## `hr.contract` (extends)

Employee Contract


Public methods: `write`

Extension points: `_check_contracts`, `_get_interval_leave_work_entry_type`, `_get_leave_work_entry_type`, `_get_leaves`, `_get_more_vals_leave_interval`, `_get_sub_leave_domain`

## `hr.leave.type` (extends)

- `work_entry_type_id` Many2one → `hr.work.entry.type` “Work Entry Type”

## `hr.leave` (extends)


Public methods: `action_confirm`, `action_refuse`, `create`, `write`

Extension points: `_action_user_cancel`, `_check_contracts`, `_create_resource_leave`, `_get_calendar`, `_get_leaves_on_public_holiday`, `_get_number_of_days`, `_get_overlapping_contracts`

## `hr.work.entry` (extends)

- `leave_id` Many2one → `hr.leave` “Time Off”
- `leave_state` Selection (related=leave_id.state)

Public methods: `action_approve_leave`, `action_refuse_leave`, `write`

Extension points: `_check_if_error`

## `hr.work.entry.type` (extends)

HR Work Entry Type

- `leave_type_ids` One2many → `hr.leave.type` “Time Off Type”
