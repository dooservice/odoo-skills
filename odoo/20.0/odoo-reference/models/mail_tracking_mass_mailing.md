# mail_tracking_mass_mailing — Mass Mailing Tracking

Depends on: mail_tracking, mass_mailing.

## `mail.message` (extends)

- `source_mailing_id` Many2one → `mailing.mailing`

## `mail.thread` (extends)


Extension points: `_get_log_valid_parameters`, `_get_message_create_valid_field_names`

## `mail.compose.message` (extends)


Extension points: `_prepare_mail_values_static`
