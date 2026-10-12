# mail_tracking_sms — SMS Message Tracking

Depends on: mail_tracking, sms.

## `mail.message` (extends)

- `source_sms_template_id` Many2one → `sms.template`

## `mail.thread` (extends)


Extension points: `_get_log_valid_parameters`, `_get_message_create_valid_field_names`

## `sms.composer` (extends)


Extension points: `_action_send_sms_comment_prepare_values`, `_prepare_mass_log_values`
