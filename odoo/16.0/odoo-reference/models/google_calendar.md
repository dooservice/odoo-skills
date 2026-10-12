# google_calendar — Google Calendar

Depends on: google_account, calendar.

## `calendar.event` (extends)

Inherits: `google.calendar.sync`

- `google_id` Char “Google Calendar Event Id” (store, compute=_compute_google_id)

Public methods: `action_mass_archive`, `create`, `write`

Extension points: `_check_values_to_sync`, `_get_archive_values`, `_get_event_user`, `_get_google_synced_fields`, `_get_remove_sync_id_values`, `_get_sync_domain`, `_get_update_future_events_values`

## `calendar.alarm_manager` (extends)


Extension points: `_get_notify_alert_extra_conditions`

## `calendar.attendee` (extends)


Public methods: `do_accept`, `do_decline`, `do_tentative`

## `calendar.recurrence` (extends)

Inherits: `google.calendar.sync`


Extension points: `_create_from_google`, `_get_event_google_id`, `_get_event_user`, `_get_google_synced_fields`, `_get_sync_domain`

## `google.calendar.credentials` (defines)

Google Calendar Account Data

- `user_ids` One2many → `res.users` (required)
- `calendar_rtoken` Char “Refresh Token”
- `calendar_token` Char “User token”
- `calendar_token_validity` Datetime “Token Validity”
- `calendar_sync_token` Char “Next Sync Token”
- `calendar_cal_id` Char “Calendar ID”
- `synchronization_stopped` Boolean “Google Synchronization stopped”

## `google.calendar.sync` (defines)

Synchronize a record with Google Calendar

- `google_id` Char “Google Calendar Id”
- `need_sync` Boolean
- `active` Boolean

Public methods: `create`, `unlink`, `write`

Extension points: `_create_from_google`, `_get_event_user`, `_get_google_synced_fields`, `_get_records_to_sync`, `_get_sync_domain`, `_get_sync_partner`

## `res.config.settings` (extends)

- `cal_client_id` Char “Client_id”
- `cal_client_secret` Char “Client_key”

## `res.users` (extends)

- `google_calendar_account_id` Many2one → `google.calendar.credentials`
- `google_calendar_rtoken` Char (related=google_calendar_account_id.calendar_rtoken)
- `google_calendar_token` Char (related=google_calendar_account_id.calendar_token)
- `google_calendar_token_validity` Datetime (related=google_calendar_account_id.calendar_token_validity)
- `google_calendar_sync_token` Char (related=google_calendar_account_id.calendar_sync_token)
- `google_calendar_cal_id` Char (related=google_calendar_account_id.calendar_cal_id)
- `google_synchronization_stopped` Boolean (related=google_calendar_account_id.synchronization_stopped)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`, `restart_google_synchronization`, `stop_google_synchronization`

Extension points: `_get_google_calendar_token`

## `google.calendar.account.reset` (defines)

Google Calendar Account Reset

- `user_id` Many2one → `res.users` (required)
- `delete_policy` Selection “User's Existing Events” (required)
- `sync_policy` Selection “Next Synchronization” (required)

Public methods: `reset_account`
