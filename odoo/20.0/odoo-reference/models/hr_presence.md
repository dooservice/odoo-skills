# hr_presence — Employee Presence Control

Depends on: hr, hr_holidays, sms.

## `hr.employee` (extends)

- `email_sent` Boolean
- `ip_connected` Boolean
- `manually_set_present` Boolean
- `manually_set_presence` Boolean

Public methods: `action_open_leave_request`, `action_send_sms`, `action_set_absent`, `action_set_present`, `get_presence_server_action_data`

Extension points: `_action_set_manual_presence`, `_check_presence`

## `hr.employee.public` (extends)

- `email_sent` Boolean
- `ip_connected` Boolean
- `manually_set_present` Boolean
- `manually_set_presence` Boolean

## `ir.websocket` (extends)


## `res.company` (extends)

- `hr_presence_last_compute_date` Datetime

## `res.config.settings` (extends)


Public methods: `create`

## `res.users.log` (extends)

- `ip` Char “IP Address”
