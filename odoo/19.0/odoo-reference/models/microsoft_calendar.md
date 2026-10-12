# microsoft_calendar — Outlook Calendar

Depends on: microsoft_account, calendar.

## `calendar.event` (extends)

Inherits: `microsoft.calendar.sync`

- `microsoft_recurrence_master_id` Char “Microsoft Recurrence Master Id”

Public methods: `action_mass_archive`, `create`, `unlink`, `write`

Extension points: `_check_microsoft_sync_status`, `_check_organizer_validation`, `_check_recurrence_overlapping`, `_get_attendee_status_o2m`, `_get_event_user_m`, `_get_microsoft_sync_domain`, `_get_microsoft_synced_fields`, `_get_organizer`, `_get_organizer_user_change_info`

## `calendar.alarm_manager` (extends)


Extension points: `_get_notify_alert_extra_conditions`

## `calendar.attendee` (extends)


Public methods: `do_accept`, `do_decline`, `do_tentative`

## `calendar.recurrence` (extends)

Inherits: `microsoft.calendar.sync`

- `need_sync_m` Boolean

Extension points: `_get_event_user_m`, `_get_microsoft_sync_domain`, `_get_microsoft_synced_fields`, `_get_organizer`, `_get_rrule`

## `microsoft.calendar.sync` (defines)

Synchronize a record with Microsoft Calendar

- `microsoft_id` Char “Organizer event Id” (index)
- `ms_universal_event_id` Char “Universal event Id” (index)
- `need_sync_m` Boolean
- `active` Boolean

Public methods: `create`, `unlink`, `write`

Extension points: `_check_old_event_update_required`, `_create_from_microsoft`, `_get_event_user_m`, `_get_microsoft_graph_timeout`, `_get_microsoft_records_to_sync`, `_get_microsoft_service`, `_get_microsoft_sync_domain`, `_get_microsoft_synced_fields`, `_get_synced_events`

## `res.config.settings` (extends)

- `cal_microsoft_client_id` Char “Microsoft Client_id”
- `cal_microsoft_client_secret` Char “Microsoft Client_key”
- `cal_microsoft_sync_paused` Boolean “Microsoft Synchronization Paused”

## `res.users` (extends)

- `microsoft_calendar_sync_token` Char (related=res_users_settings_id.microsoft_calendar_sync_token)
- `microsoft_synchronization_stopped` Boolean (related=res_users_settings_id.microsoft_synchronization_stopped)
- `microsoft_last_sync_date` Datetime (related=res_users_settings_id.microsoft_last_sync_date)

Public methods: `check_calendar_credentials`, `check_synchronization_status`, `pause_microsoft_synchronization`, `restart_microsoft_synchronization`, `stop_microsoft_synchronization`, `unpause_microsoft_synchronization`

Extension points: `_get_microsoft_calendar_token`, `_get_microsoft_sync_status`

## `res.users.settings` (extends)

- `microsoft_calendar_sync_token` Char “Microsoft Next Sync Token”
- `microsoft_synchronization_stopped` Boolean “Outlook Synchronization stopped”
- `microsoft_last_sync_date` Datetime “Last Sync Date”

Extension points: `_get_fields_blacklist`

## `microsoft.calendar.account.reset` (defines)

Microsoft Calendar Account Reset

- `user_id` Many2one → `res.users` (required)
- `delete_policy` Selection “User's Existing Events” (required)
- `sync_policy` Selection “Next Synchronization” (required)

Public methods: `reset_account`
