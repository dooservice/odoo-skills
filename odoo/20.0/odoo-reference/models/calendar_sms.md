# calendar_sms — Calendar - SMS

Depends on: calendar, sms.

## `calendar.alarm` (extends)

- `alarm_type` Selection
- `sms_template_id` Many2one → `sms.template` “SMS Template” (store, compute=_compute_sms_template_id)

## `calendar.alarm_manager` (extends)


## `calendar.event` (extends)


Public methods: `action_send_sms`

Extension points: `_get_trigger_alarm_types`
