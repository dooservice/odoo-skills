# google_calendar — Google Calendar

Depends on: google_account, calendar.

## `calendar.event` (extends)

Inherits: `google.calendar.sync`

- `google_id` Char “Google Calendar Event Id” (store, compute=_compute_google_id)
- `guests_readonly` Boolean “Guests Event Modification Permission”
- `videocall_source` Selection

Public methods: `action_mass_archive`, `create`, `write`

Extension points: `_check_alarm_ids_sync_limit`, `_check_modify_event_permission`, `_check_values_to_sync`, `_get_archive_values`, `_get_event_user`, `_get_google_synced_fields`, `_get_remove_sync_id_values`, `_get_sync_domain`, `_get_update_future_events_values`

## `calendar.alarm_manager` (extends)


Extension points: `_get_notify_alert_extra_conditions`

## `calendar.attendee` (extends)


Public methods: `do_accept`, `do_decline`, `do_tentative`

## `calendar.recurrence` (extends)

Inherits: `google.calendar.sync`


Extension points: `_create_from_google`, `_get_event_google_id`, `_get_event_user`, `_get_google_synced_fields`, `_get_sync_domain`

## `google.calendar.sync` (defines)

Synchronize a record with Google Calendar

- `google_id` Char “Google Calendar Id”
- `need_sync` Boolean
- `active` Boolean

Public methods: `create`, `unlink`, `write`

Extension points: `_check_any_records_to_sync`, `_create_from_google`, `_get_event_user`, `_get_google_synced_fields`, `_get_post_sync_values`, `_get_records_to_sync`, `_get_sync_domain`, `_get_sync_partner`

## `res.config.settings` (extends)

- `cal_client_id` Char “Client_id”
- `cal_client_secret` Char “Client_key”
- `cal_sync_paused` Boolean “Google Synchronization Paused”

## `res.users` (extends)

- `google_calendar_rtoken` Char (related=res_users_settings_id.google_calendar_rtoken)
- `google_calendar_token` Char (related=res_users_settings_id.google_calendar_token)
- `google_calendar_token_validity` Datetime (related=res_users_settings_id.google_calendar_token_validity)
- `google_calendar_sync_token` Char (related=res_users_settings_id.google_calendar_sync_token)
- `google_calendar_cal_id` Char (related=res_users_settings_id.google_calendar_cal_id)
- `google_synchronization_stopped` Boolean (related=res_users_settings_id.google_synchronization_stopped)

Public methods: `check_calendar_credentials`, `check_synchronization_status`, `is_google_calendar_synced`, `pause_google_synchronization`, `restart_google_synchronization`, `stop_google_synchronization`, `unpause_google_synchronization`

Extension points: `_check_pending_odoo_records`, `_get_google_calendar_token`, `_get_google_sync_status`

## `res.users.settings` (extends)

- `google_calendar_rtoken` Char “Refresh Token”
- `google_calendar_token` Char “User token”
- `google_calendar_token_validity` Datetime “Token Validity”
- `google_calendar_sync_token` Char “Next Sync Token”
- `google_calendar_cal_id` Char “Calendar ID”
- `google_synchronization_stopped` Boolean “Google Synchronization stopped”

Extension points: `_get_fields_blacklist`

## `google.calendar.account.reset` (defines)

Google Calendar Account Reset

- `user_id` Many2one → `res.users` (required)
- `delete_policy` Selection “User's Existing Events” (required)
- `sync_policy` Selection “Next Synchronization” (required)

Public methods: `reset_account`
