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
- `notify_responsible` Boolean “Notify Responsible”

## `calendar.alarm_manager` (defines)

Event Alarm Manager


Public methods: `do_check_alarm_for_one_date`, `do_notif_reminder`, `get_next_notif`

Extension points: `_get_events_by_alarm_to_notify`, `_get_next_potential_limit_alarm`, `_get_notify_alert_extra_conditions`

## `calendar.attendee` (defines)

Calendar Attendee Information

- `event_id` Many2one → `calendar.event` (required, index)
- `recurrence_id` Many2one → `calendar.recurrence` (related=event_id.recurrence_id)
- `partner_id` Many2one → `res.partner` (required, readonly, index)
- `email` Char “Email” (related=partner_id.email)
- `phone` Char “Phone” (related=partner_id.phone)
- `common_name` Char “Common name” (store, compute=_compute_common_name)
- `access_token` Char “Invitation Token”
- `mail_tz` Selection (compute=_compute_mail_tz)
- `state` Selection “Status”
- `availability` Selection (readonly)

Public methods: `copy`, `create`, `do_accept`, `do_decline`, `do_tentative`, `unlink`, `write`

## `calendar.calendar` (defines)

User Calendar

- `name` Char “Name”
- `event_ids` One2many → `calendar.event`
- `recurrence_ids` One2many → `calendar.recurrence`
- `calendar_default_privacy` Selection (required)
- `calendar_user_ids` One2many → `calendar.user` “Users”
- `owner_id` Many2one → `res.users` (compute=_compute_owner_id)
- `share_user_ids` Many2many → `res.users` “Shared with” (compute=_compute_share_user_ids)
- `calendar_user_id` Many2one → `calendar.user` “Current Membership Record” (compute=_compute_calendar_user)
- `color` Integer (related=calendar_user_id.filter_color)
- `is_primary` Boolean (related=calendar_user_id.is_primary)
- `user_access_role` Selection (related=calendar_user_id.access_role)

Public methods: `add_filter_to_list`, `unlink`, `write`

Extension points: `_get_default_calendar_user_values`, `_get_public_writable_fields`

## `calendar.event` (defines)

Calendar Event

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Meeting Subject” (required)
- `calendar_id` Many2one → `calendar.calendar` “Calendar” (store, compute=_compute_calendar_id)
- `calendar_color` Integer (related=calendar_id.color)
- `description` Html “Description”
- `is_draft` Boolean “Is draft”
- `user_id` Many2one → `res.users`
- `partner_id` Many2one → `res.partner` “Scheduled by” (readonly, related=user_id.partner_id)
- `location` Char “Location”
- `notes` Html “Notes”
- `videocall_location` Char “Meeting URL” (store, compute=_compute_videocall_location)
- `access_token` Char “Invitation Token” (readonly)
- `google_calendar_url` Char “Google Calendar URL” (compute=_compute_google_calendar_url)
- `videocall_source` Selection (compute=_compute_videocall_source)
- `videocall_channel_id` Many2one → `discuss.channel`
- `privacy` Selection
- `privacy_placeholder` Char (compute=_compute_privacy_placeholder)
- `effective_privacy` Selection (compute=_compute_effective_privacy)
- `show_as` Selection (required)
- `is_highlighted` Boolean “Is the Event Highlighted” (compute=_compute_is_highlighted)
- `is_organizer_alone` Boolean “Is the Organizer Alone” (compute=_compute_is_organizer_alone)
- `active` Boolean “Active”
- `categ_ids` Many2many → `calendar.event.type`
- `start` Datetime “Start” (required, index)
- `stop` Datetime “Stop” (required, store, compute=_compute_stop)
- `display_time` Char “Event Time” (compute=_compute_display_time)
- `allday` Boolean “All Day Duration”
- `start_date` Date “Start Date” (store, compute=_compute_dates)
- `stop_date` Date “End Date” (store, compute=_compute_dates)
- `duration` Float “Duration” (store, compute=_compute_duration)
- `res_id` Many2oneReference “Document ID”
- `res_model_id` Many2one → `ir.model` (index)
- `res_model` Char “Document Model Name” (readonly, store, related=res_model_id.model)
- `res_model_name` Char (related=res_model_id.name)
- `res_record` Reference “Linked to” (compute=_compute_res_record)
- `meeting_activity_ids` One2many → `mail.activity` “Meeting Activities”
- `attendee_ids` One2many → `calendar.attendee`
- `current_attendee` Many2one → `calendar.attendee` (compute=_compute_current_attendee)
- `current_status` Selection “Attending?” (related=current_attendee.state)
- `should_show_status` Boolean (compute=_compute_should_show_status)
- `partner_ids` Many2many → `res.partner` “Attendees”
- `invalid_email_partner_ids` Many2many → `res.partner` (compute=_compute_invalid_email_partner_ids)
- `unavailable_partner_ids` Many2many → `res.partner` “Unavailable Attendees” (compute=_compute_unavailable_partner_ids)
- `alarm_ids` Many2many → `calendar.alarm` “Reminders” (store, compute=_compute_alarm_ids)
- `recurrency` Boolean “Recurrent”
- `recurrence_id` Many2one → `calendar.recurrence` “Recurrence Rule”
- `follow_recurrence` Boolean
- `recurrence_update` Selection
- `rrule` Char “Recurrent Rule” (compute=_compute_recurrence)
- `rrule_type_ui` Selection “Repeat” (compute=_compute_rrule_type_ui)
- `rrule_type` Selection “Recurrence” (compute=_compute_recurrence)
- `event_tz` Selection “Timezone” (compute=_compute_recurrence)
- `end_type` Selection “Recurrence Termination” (compute=_compute_recurrence)
- `interval` Integer “Repeat On” (compute=_compute_recurrence)
- `count` Integer “Number of Repetitions” (compute=_compute_recurrence)
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
- `attendees_count` Integer (compute=_compute_attendees_count)
- `accepted_count` Integer (compute=_compute_attendees_count)
- `declined_count` Integer (compute=_compute_attendees_count)
- `tentative_count` Integer (compute=_compute_attendees_count)
- `awaiting_count` Integer (compute=_compute_attendees_count)
- `user_can_edit` Boolean (compute=_compute_user_can_edit)

Public methods: `action_confirm`, `action_join_meeting`, `action_join_video_call`, `action_mass_archive`, `action_mass_deletion`, `action_open_archive_or_unlink_wizard`, `action_open_calendar_event`, `action_open_composer`, `action_sendmail`, `change_attendee_status`, `clear_videocall_location`, `copy`, `create`, `default_get`, `find_partner_customer`, `get_default_duration`, `get_discuss_videocall_location`, `get_display_time_tz`, `get_formatted_date_and_time`, `get_next_alarm_date`, `get_state_selections`, `set_discuss_videocall_location`, `unlink`, `write`

Extension points: `_check_closing_date`, `_check_organizer_validation_conditions`, `_check_private_event_conditions`, `_check_values_to_sync`, `_create_videocall_channel`, `_create_videocall_channel_id`, `_get_activity_deadline_from_start`, `_get_activity_excluded_models`, `_get_archive_values`, `_get_calendar_id_domain`, `_get_contact_details_description`, `_get_custom_fields`, `_get_customer_description`, `_get_customer_summary`, `_get_default_privacy_domain`, `_get_display_time`, `_get_duration`, `_get_ics_file`, `_get_mail_tz`, `_get_model_selection`, `_get_new_invited_attendees`, `_get_public_fields`, `_get_recurrence_params`, `_get_recurrence_params_by_date`, `_get_recurrent_fields`, `_get_remove_sync_id_values`, `_get_start_date`, `_get_time_fields`, `_get_time_update_dict`, `_get_today_domain`, `_get_trigger_alarm_types`, `_get_update_future_events_values`, `_get_updated_recurrence_values`, `_get_valid_event_domain`, `_get_videocall_channel_description`, `_prepare_partner_contact_details_html`

## `calendar.event.type` (defines)

Event Meeting Type

- `name` Char “Name” (required)
- `color` Integer “Color”

## `calendar.filters` (defines)

Calendar Filter

- `active` Boolean “Active”
- `user_id` Many2one → `res.users` (required, index)
- `partner_id` Many2one → `res.partner` (required, index)

Public methods: `init_partner_filters`, `update_partner_filters`

## `calendar.recurrence` (defines)

Event Recurrence Rule

- `name` Char (store, compute=_compute_name)
- `base_event_id` Many2one → `calendar.event`
- `calendar_event_ids` One2many → `calendar.event`
- `calendar_id` Many2one “Calendar” (related=base_event_id.calendar_id)
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
- `trigger_id` Many2one → `ir.cron.trigger`

Public methods: `get_recurrence_name`

Extension points: `_get_daily_recurrence_name`, `_get_events_from`, `_get_first_event`, `_get_lang_week_start`, `_get_monthly_recurrence_name`, `_get_occurrences`, `_get_outliers`, `_get_ranges`, `_get_rrule`, `_get_start_of_period`, `_get_timezone`, `_get_week_days`, `_get_weekly_recurrence_name`, `_get_yearly_recurrence_name`

## `calendar.user` (defines)

Calendar User Manager

- `calendar_id` Many2one → `calendar.calendar` “Calendar” (required, readonly)
- `calendar_share_user_ids` Many2many (readonly, related=calendar_id.share_user_ids)
- `calendar_owner_id` Many2one (related=calendar_id.owner_id)
- `user_id` Many2one → `res.users` “User” (required, readonly)
- `is_primary` Boolean “Primary” (readonly)
- `name` Char “Label”
- `access_role` Selection (required, readonly)
- `filter_color` Integer “Color”
- `is_filter_active` Boolean “Shown in Filters List”
- `is_filter_checked` Boolean “Filter Enabled”

Public methods: `unlink`, `write`

Extension points: `_get_default_color`, `_get_writeable_fields`

## `discuss.channel` (extends)

- `calendar_event_ids` One2many → `calendar.event`

Extension points: `_get_meeting_ongoing_domain`, `_get_meeting_today_domain`

## `ir.http` (extends)


## `mail.activity` (extends)

- `calendar_event_id` Many2one → `calendar.event` “Calendar Meeting”

Public methods: `action_create_calendar_event`, `unlink_w_meeting`, `write`

Extension points: `_action_done`, `_get_activity_done_message_extra_values`

## `mail.activity.mixin` (extends)

- `activity_calendar_event_id` Many2one → `calendar.event` “Next Activity Calendar Event” (compute=_compute_activity_calendar_event_id)

## `mail.activity.type` (extends)

- `category` Selection

## `res.partner` (extends)

- `meeting_count` Integer “# Meetings” (compute=_compute_meeting_count)
- `meeting_ids` Many2many → `calendar.event` “Meetings”
- `meeting_next_date` Date “Next Meeting” (compute=_compute_meeting_display)
- `meeting_display_label` Char (compute=_compute_meeting_display)
- `calendar_last_notif_ack` Datetime “Last notification marked as read from base Calendar”

Public methods: `action_schedule_meeting`, `get_attendee_detail`

Extension points: `_get_busy_calendar_events`

## `res.users` (extends)

- `calendar_user_ids` One2many → `calendar.user`
- `calendar_ids` One2many → `calendar.calendar` (compute=_compute_calendar_ids)
- `owned_calendar_ids` One2many → `calendar.calendar` (compute=_compute_calendar_ids)
- `writable_calendar_ids` One2many → `calendar.calendar` (compute=_compute_calendar_ids)
- `primary_calendar_id` Many2one → `calendar.calendar` (store, compute=_compute_primary_calendar)

Public methods: `check_calendar_credentials`, `check_synchronization_status`, `create`, `get_calendar_model_data`, `get_calendar_sync_email`, `get_selected_calendars_partner_ids`, `unlink`

Extension points: `_get_activity_groups`

## `res.users.settings` (extends)

- `calendar_show_activities` Boolean “Show Activities in Calendar”

## `calendar.event.archive.or.unlink.wizard` (defines)

Calendar Event Archive Or Unlink Wizard

Inherits: `mail.composer.mixin`

- `block_mail` Boolean
- `calendar_event_id` Many2one → `calendar.event` (required)
- `recipient_ids` Many2many → `res.partner` “Recipients” (store, compute=_compute_recipient_ids)
- `recurrency` Boolean “Recurrent” (related=calendar_event_id.recurrency)
- `recurrence_choice` Selection
- `requested_action` Selection (required)
- `template_id` Many2one (compute=_compute_template_id)

Public methods: `action_archive`, `action_send_mail_and_archive`, `action_send_mail_and_unlink`, `action_unlink`

Extension points: `_get_calendar_events`

## `calendar.event.multi.archive.or.unlink.wizard` (defines)

Calendar Event Multi Archive Or Unlink Wizard

- `block_mail` Boolean
- `calendar_event_ids` Many2many → `calendar.event` (required)
- `has_recurrent_events` Boolean (compute=_compute_has_recurrent_events)
- `requested_action` Selection (required)

Public methods: `action_archive`, `action_send_mails_and_archive`, `action_send_mails_and_unlink`, `action_unlink`

## `mail.activity.schedule` (extends)


Public methods: `action_create_calendar_event`
