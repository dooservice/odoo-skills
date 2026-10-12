# google_calendar — Google Calendar

Depends on: google_account, calendar.

## `calendar.alarm_manager` (extends)


Extension points: `_get_notify_alert_extra_conditions`

## `calendar.attendee` (extends)


Public methods: `do_accept`, `do_decline`, `do_tentative`

## `calendar.calendar` (extends)

Inherits: `google.sync`

- `google_sync_token` Char (related=calendar_user_id.google_sync_token)
- `google_sync_enabled` Boolean (related=calendar_user_id.google_sync_enabled)
- `is_import_pending` Boolean “Needs Import” (readonly)

Public methods: `create`, `get_google_path`, `unlink`, `write`

Extension points: `_get_default_calendar_user_values`, `_get_google_synced_fields_map`, `_get_odoo_access_role`, `_get_public_writable_fields`, `_get_sync_domain`

## `calendar.event` (extends)

Inherits: `google.event.sync`

- `google_id` Char “Google Calendar Event Id” (store, compute=_compute_google_id)
- `guests_readonly` Boolean “Guests Event Modification Permission”
- `videocall_source` Selection

Public methods: `action_mass_archive`, `create`, `write`

Extension points: `_check_alarm_ids_sync_limit`, `_check_modify_event_permission`, `_check_private_event_conditions`, `_check_values_to_sync`, `_get_archive_values`, `_get_calendar_id_domain`, `_get_event_owner`, `_get_event_user`, `_get_google_synced_fields`, `_get_remove_sync_id_values`, `_get_sync_domain`, `_get_update_future_events_values`

## `calendar.recurrence` (extends)

Inherits: `google.event.sync`


Extension points: `_create_from_google`, `_get_event_google_id`, `_get_event_owner`, `_get_event_user`, `_get_google_synced_fields`, `_get_sync_domain`

## `calendar.user` (extends)

- `access_role` Selection
- `google_sync_enabled` Boolean “Google Sync”
- `google_sync_token` Char “Sync Token”
- `is_filter_active` Boolean “Shown in Filters List” (store, compute=_compute_filters)
- `is_filter_checked` Boolean “Filter Enabled” (store, compute=_compute_filters)

Public methods: `create`, `write`

Extension points: `_get_writeable_fields`

## `google.event.sync` (defines)

Google Event Sync

Inherits: `google.sync`

- `last_google_calendar_sync_path` Char
- `active` Boolean

Public methods: `create`, `unlink`, `write`

Extension points: `_check_any_records_to_sync`, `_create_from_google`, `_get_event_owner`, `_get_event_user`, `_get_google_calendar_path`, `_get_post_sync_values`, `_get_records_to_sync`, `_get_skipped_google_events`, `_get_sync_partner`

## `google.sync` (defines)

Synchronize a record with Google Calendar

- `google_id` Char “Google Calendar Id”
- `need_sync` Boolean

Extension points: `_get_google_synced_fields`, `_get_sync_domain`

## `res.config.settings` (extends)

- `cal_client_id` Char “Client_id”
- `cal_client_secret` Char “Client_key”
- `cal_sync_paused` Boolean “Google Synchronization Paused”
- `cal_google_disable_auto_videocall_link` Boolean “Disable videocall generation”

## `res.users` (extends)

- `google_account_email` Char (related=res_users_settings_id.google_account_email)
- `google_calendar_rtoken` Char (related=res_users_settings_id.google_calendar_rtoken)
- `google_calendar_token` Char (related=res_users_settings_id.google_calendar_token)
- `google_calendar_token_validity` Datetime (related=res_users_settings_id.google_calendar_token_validity)
- `google_calendar_sync_token` Char (related=res_users_settings_id.google_calendar_sync_token)
- `google_synchronization_stopped` Boolean (related=res_users_settings_id.google_synchronization_stopped)

Public methods: `check_calendar_credentials`, `check_synchronization_status`, `get_calendar_sync_email`, `is_google_calendar_synced`, `pause_google_synchronization`, `restart_google_synchronization`, `stop_google_synchronization`, `unpause_google_synchronization`

Extension points: `_check_pending_odoo_records`, `_get_google_calendar_token`, `_get_google_sync_status`

## `res.users.settings` (extends)

- `google_account_email` Char “Google Calendar Email”
- `google_calendar_rtoken` Char “Refresh Token”
- `google_calendar_token` Char “User token”
- `google_calendar_token_validity` Datetime “Token Validity”
- `google_calendar_sync_token` Char “Next Calendar Sync Token”
- `google_synchronization_stopped` Boolean “Google Synchronization stopped”

Extension points: `_get_email_from_google`, `_get_fields_blacklist`

## `google.calendar.account.reset` (defines)

Google Calendar Account Reset

- `user_id` Many2one → `res.users` (required)
- `delete_events` Boolean “Delete synced events from Odoo”

Public methods: `reset_account`
