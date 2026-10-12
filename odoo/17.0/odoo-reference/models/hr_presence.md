# hr_presence — Employee Presence Control

Depends on: hr, hr_holidays, sms.

## `hr.employee.base` (extends)

- `email_sent` Boolean
- `ip_connected` Boolean
- `manually_set_present` Boolean
- `hr_presence_state_display` Selection

Public methods: `action_open_leave_request`, `action_send_mail`, `action_send_sms`, `action_set_absent`, `action_set_present`, `write`

Extension points: `_action_open_presence_view`, `_action_set_manual_presence`, `_check_presence`

## `hr.employee.base` (extends)


## `ir.websocket` (extends)


## `res.company` (extends)

- `hr_presence_last_compute_date` Datetime

## `res.users.log` (extends)

- `create_uid` Integer (index)
- `ip` Char “IP Address”
