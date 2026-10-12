# calendar — Calendar

Depends on: base, mail.

## `calendar.alarm` (defines)

Event Alarm

- `name` Char “Name” (required)
- `alarm_type` Selection “Type” (required)
- `duration` Integer “Remind Before” (required)
- `interval` Selection (required)
- `duration_minutes` Integer “Duration in minutes” (store, compute=_compute_duration_minutes)
- `mail_template_id` Many2one → `mail.template` “Email Template” (store, compute=_compute_mail_template_id)
- `body` Text “Additional Message”

## `calendar.alarm_manager` (defines)

Event Alarm Manager


Public methods: `do_check_alarm_for_one_date`, `do_notif_reminder`, `get_next_notif`

Extension points: `_get_events_by_alarm_to_notify`, `_get_next_potential_limit_alarm`, `_get_notify_alert_extra_conditions`

## `calendar.attendee` (defines)

Calendar Attendee Information

- `event_id` Many2one → `calendar.event` (required)
- `recurrence_id` Many2one → `calendar.recurrence` (related=event_id.recurrence_id)
- `partner_id` Many2one → `res.partner` (required, readonly)
- `email` Char “Email” (related=partner_id.email)
- `phone` Char “Phone” (related=partner_id.phone)
- `common_name` Char “Common name” (store, compute=_compute_common_name)
- `access_token` Char “Invitation Token”
- `mail_tz` Selection (compute=_compute_mail_tz)
- `state` Selection “Status” (readonly)
- `availability` Selection (readonly)

Public methods: `copy`, `create`, `do_accept`, `do_decline`, `do_tentative`, `unlink`, `write`

## `calendar.event` (defines)

Calendar Event

Inherits: `mail.thread`

- `name` Char “Meeting Subject” (required)
- `description` Html “Description”
- `user_id` Many2one → `res.users`
- `partner_id` Many2one → `res.partner` “Scheduled by” (readonly, related=user_id.partner_id)
- `location` Char “Location”
- `videocall_location` Char “Meeting URL” (store, compute=_compute_videocall_location)
- `access_token` Char “Invitation Token” (store, index)
- `videocall_source` Selection (compute=_compute_videocall_source)
- `videocall_channel_id` Many2one → `mail.channel`
- `privacy` Selection (required)
- `show_as` Selection (required)
- `is_highlighted` Boolean “Is the Event Highlighted” (compute=_compute_is_highlighted)
- `is_organizer_alone` Boolean “Is the Organizer Alone” (compute=_compute_is_organizer_alone)
- `active` Boolean “Active”
- `categ_ids` Many2many → `calendar.event.type`
- `start` Datetime “Start” (required)
- `stop` Datetime “Stop” (required, store, compute=_compute_stop)
- `display_time` Char “Event Time” (compute=_compute_display_time)
- `allday` Boolean “All Day”
- `start_date` Date “Start Date” (store, compute=_compute_dates)
- `stop_date` Date “End Date” (store, compute=_compute_dates)
- `duration` Float “Duration” (store, compute=_compute_duration)
- `res_id` Many2oneReference “Document ID”
- `res_model_id` Many2one → `ir.model`
- `res_model` Char “Document Model Name” (readonly, store, related=res_model_id.model)
- `activity_ids` One2many → `mail.activity` “Activities”
- `attendee_ids` One2many → `calendar.attendee`
- `attendee_status` Selection “Attendee Status” (compute=_compute_attendee)
- `partner_ids` Many2many → `res.partner` “Attendees”
- `invalid_email_partner_ids` Many2many → `res.partner` (compute=_compute_invalid_email_partner_ids)
- `alarm_ids` Many2many → `calendar.alarm` “Reminders”
- `recurrency` Boolean “Recurrent”
- `recurrence_id` Many2one → `calendar.recurrence` “Recurrence Rule”
- `follow_recurrence` Boolean
- `recurrence_update` Selection
- `rrule` Char “Recurrent Rule” (compute=_compute_recurrence)
- `rrule_type` Selection “Recurrence” (compute=_compute_recurrence)
- `event_tz` Selection “Timezone” (compute=_compute_recurrence)
- `end_type` Selection “Recurrence Termination” (compute=_compute_recurrence)
- `interval` Integer “Repeat Every” (compute=_compute_recurrence)
- `count` Integer “Repeat” (compute=_compute_recurrence)
- `mon` Boolean (compute=_compute_recurrence)
- `tue` Boolean (compute=_compute_recurrence)
- `wed` Boolean (compute=_compute_recurrence)
- `thu` Boolean (compute=_compute_recurrence)
- `fri` Boolean (compute=_compute_recurrence)
- `sat` Boolean (compute=_compute_recurrence)
- `sun` Boolean (compute=_compute_recurrence)
- `month_by` Selection “Option” (compute=_compute_recurrence)
- `day` Integer “Date of month” (compute=_compute_recurrence)
- `weekday` Selection (compute=_compute_recurrence)
- `byday` Selection “By day” (compute=_compute_recurrence)
- `until` Date (compute=_compute_recurrence)
- `display_description` Boolean (compute=_compute_display_description)

Public methods: `action_join_meeting`, `action_join_video_call`, `action_mass_archive`, `action_mass_deletion`, `action_open_calendar_event`, `action_open_composer`, `action_sendmail`, `change_attendee_status`, `clear_videocall_location`, `convert_online_event_desc_to_text`, `copy`, `create`, `default_get`, `find_partner_customer`, `get_discuss_videocall_location`, `get_display_time_tz`, `name_get`, `read`, `read_group`, `set_discuss_videocall_location`, `unlink`, `write`

Extension points: `_check_closing_date`, `_check_private_event_conditions`, `_check_values_to_sync`, `_create_videocall_channel`, `_create_videocall_channel_id`, `_get_archive_values`, `_get_attendee_emails`, `_get_custom_fields`, `_get_date_formats`, `_get_display_time`, `_get_duration`, `_get_ics_file`, `_get_mail_tz`, `_get_public_fields`, `_get_recurrence_params`, `_get_recurrence_params_by_date`, `_get_recurrent_fields`, `_get_remove_sync_id_values`, `_get_start_date`, `_get_time_fields`, `_get_time_update_dict`, `_get_trigger_alarm_types`, `_get_update_future_events_values`, `_get_updated_recurrence_values`

## `calendar.event.type` (defines)

Event Meeting Type

- `name` Char “Name” (required)
- `color` Integer “Color”

## `calendar.filters` (defines)

Calendar Filters

- `user_id` Many2one → `res.users` (required, index)
- `partner_id` Many2one → `res.partner` (required, index)
- `active` Boolean “Active”
- `partner_checked` Boolean “Checked”

Public methods: `unlink_from_partner_id`

## `calendar.recurrence` (defines)

Event Recurrence Rule

- `name` Char (store, compute=_compute_name)
- `base_event_id` Many2one → `calendar.event`
- `calendar_event_ids` One2many → `calendar.event`
- `event_tz` Selection “Timezone”
- `rrule` Char (store, compute=_compute_rrule)
- `dtstart` Datetime (compute=_compute_dtstart)
- `rrule_type` Selection
- `end_type` Selection
- `interval` Integer
- `count` Integer
- `mon` Boolean
- `tue` Boolean
- `wed` Boolean
- `thu` Boolean
- `fri` Boolean
- `sat` Boolean
- `sun` Boolean
- `month_by` Selection
- `day` Integer
- `weekday` Selection “Weekday”
- `byday` Selection “By day”
- `until` Date “Repeat Until”

Public methods: `get_recurrence_name`

Extension points: `_get_daily_recurrence_name`, `_get_events_from`, `_get_first_event`, `_get_lang_week_start`, `_get_monthly_recurrence_name`, `_get_occurrences`, `_get_outliers`, `_get_ranges`, `_get_rrule`, `_get_start_of_period`, `_get_timezone`, `_get_week_days`, `_get_weekly_recurrence_name`, `_get_yearly_recurrence_name`

## `ir.http` (extends)


## `mail.activity` (extends)

- `calendar_event_id` Many2one → `calendar.event` “Calendar Meeting”

Public methods: `action_create_calendar_event`, `unlink_w_meeting`

Extension points: `_action_done`

## `mail.activity.mixin` (extends)

- `activity_calendar_event_id` Many2one → `calendar.event` “Next Activity Calendar Event” (compute=_compute_activity_calendar_event_id)

## `mail.activity.type` (extends)

- `category` Selection

## `res.partner` (extends)

- `meeting_count` Integer “# Meetings” (compute=_compute_meeting_count)
- `meeting_ids` Many2many → `calendar.event` “Meetings”
- `calendar_last_notif_ack` Datetime “Last notification marked as read from base Calendar”

Public methods: `get_attendee_detail`, `schedule_meeting`

## `res.users` (extends)


Public methods: `systray_get_activities`

## `calendar.alarm` (extends)


## `calendar.provider.config` (defines)

Calendar Provider Configuration Wizard

- `external_calendar_provider` Selection
- `cal_client_id` Char “Google Client_id”
- `cal_client_secret` Char “Google Client_key”
- `microsoft_outlook_client_identifier` Char “Outlook Client Id”
- `microsoft_outlook_client_secret` Char “Outlook Client Secret”

Public methods: `action_calendar_prepare_external_provider_sync`
