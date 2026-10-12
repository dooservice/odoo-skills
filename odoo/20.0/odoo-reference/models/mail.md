# mail — Discuss

Depends on: base, base_setup, bus, web_tour, html_editor.

## `bus.bus` (extends)


Extension points: `_prepare_payload`

## `bus.listener.mixin` (extends)


## `bus.sync.mixin` (defines)

Mixin for Bus Sync


Public methods: `write`

## `discuss.call.history` (defines)

Keep the call history

- `channel_id` Many2one → `discuss.channel` (required, index)
- `artifact_ids` One2many → `mail.call.artifact` “Artifacts”
- `duration_hour` Float (compute=_compute_duration_hour)
- `has_recording` Boolean (compute=_compute_recording_media)
- `has_audio` Boolean (compute=_compute_recording_media)
- `has_video` Boolean (compute=_compute_recording_media)
- `start_dt` Datetime (required, index)
- `end_dt` Datetime
- `start_call_message_id` Many2one → `mail.message` (index)

## `discuss.category` (defines)

Discussion Category

Inherits: `bus.sync.mixin`, `bus.listener.mixin`

- `name` Char “Name” (required)
- `channel_ids` One2many → `discuss.channel` “Channels”
- `sequence` Integer “Sequence”

Extension points: `_get_bus_channel_access_token`

## `discuss.channel` (defines)

Discussion Channel

Inherits: `mail.thread`, `bus.sync.mixin`

- `name` Char “Name” (required)
- `active` Boolean
- `can_join` Boolean “Can Join” (compute=_compute_can_join)
- `can_leave` Boolean “Can Leave” (compute=_compute_can_leave)
- `channel_type` Selection “Conversation Type” (required, readonly)
- `is_editable` Boolean “Is Editable” (compute=_compute_is_editable)
- `is_readonly` Boolean “Read-only”
- `default_display_mode` Selection “Default Display Mode”
- `description` Text “Description”
- `image_128` Image “Image”
- `avatar_128` Image “Avatar” (compute=_compute_avatar_128)
- `avatar_cache_key` Char (compute=_compute_avatar_cache_key)
- `discuss_category_id` Many2one → `discuss.category` “Category” (index)
- `channel_partner_ids` Many2many → `res.partner` “Partners” (compute=_compute_channel_partner_ids)
- `channel_member_ids` One2many → `discuss.channel.member` “Members”
- `member_indices` Char (store, compute=_compute_member_indices)
- `parent_channel_id` Many2one → `discuss.channel` (readonly, index)
- `sub_channel_ids` One2many → `discuss.channel` “Sub Channels” (readonly)
- `from_message_id` Many2one → `mail.message` (readonly)
- `sfu_channel_uuid` Char
- `sfu_server_url` Char
- `rtc_session_ids` One2many → `discuss.channel.rtc.session`
- `call_history_ids` One2many → `discuss.call.history`
- `is_member` Boolean “Is Member” (compute=_compute_is_member)
- `self_member_id` Many2one → `discuss.channel.member` (compute=_compute_self_member_id)
- `can_self_edit_readonly_channel` Boolean (compute=_compute_can_self_edit_readonly_channel)
- `invited_member_ids` One2many → `discuss.channel.member` (compute=_compute_invited_member_ids)
- `meeting_start_dt` Datetime “Meeting Start” (compute=_compute_meeting_dt)
- `meeting_stop_dt` Datetime “Meeting End” (compute=_compute_meeting_dt)
- `member_count` Integer “Member Count” (compute=_compute_member_count)
- `message_count` Integer “# Messages” (readonly, compute=_compute_message_count)
- `last_interest_dt` Datetime “Last Activity” (index)
- `group_ids` Many2many → `res.groups` “Auto Subscription”
- `uuid` Char “UUID”
- `group_public_id` Many2one → `res.groups` “Authorized Group” (store, compute=_compute_group_public_id)
- `invitation_url` Char “Invitation URL” (compute=_compute_invitation_url)
- `channel_name_member_ids` One2many → `discuss.channel.member` (compute=_compute_channel_name_member_ids)

Public methods: `action_reset_invitation_uuid`, `action_unfollow`, `action_view_recordings`, `channel_change_description`, `channel_join`, `channel_rename`, `create`, `execute_command_help`, `execute_command_who`, `get_invite_partner_domain`, `invite_by_email`, `message_post`, `open_chat_window_action`, `set_message_pin`, `web_read_group`, `write`

Extension points: `_check_can_update_message_content`, `_create_attachments_for_post`, `_create_channel`, `_create_group`, `_create_sub_channel`, `_get_access_action`, `_get_allowed_channel_member_create_params`, `_get_allowed_message_params`, `_get_allowed_message_partner_ids`, `_get_avatar_128_access_token`, `_get_call_notification_tag`, `_get_invite_urls_by_emails`, `_get_last_messages`, `_get_last_needaction_messages`, `_get_meeting_ongoing_domain`, `_get_meeting_today_domain`, `_get_member_join_notification`, `_get_notify_valid_parameters`, `_get_or_create_chat`, `_get_recording_address`, `_get_today_bounds`

## `discuss.channel.last.interest.update` (defines)

Pending Channel Last Interest Update

- `channel_id` Many2one → `discuss.channel` (required, index)
- `last_interest_dt` Datetime (required)

## `discuss.channel.member` (defines)

Channel Member

Inherits: `bus.listener.mixin`, `bus.sync.mixin`

- `partner_id` Many2one → `res.partner` (index)
- `guest_id` Many2one → `mail.guest` (index)
- `is_self` Boolean (compute=_compute_is_self)
- `can_unlink` Boolean (compute=_compute_can_unlink)
- `channel_id` Many2one → `discuss.channel` (required)
- `channel_role` Selection “Channel Role”
- `is_favorite` Boolean “Favorite”
- `seen_message_id` Many2one → `mail.message` “Last Seen”
- `new_message_separator` Integer (required)
- `message_unread_counter` Integer “Unread Messages Counter” (compute=_compute_message_unread)
- `is_unread` Boolean “Has unread messages” (compute=_compute_is_unread)
- `custom_notifications` Selection
- `invitation_sent_dt` Datetime “Invitation Sent On”
- `mute_until_dt` Datetime “Mute notifications until”
- `is_pinned` Boolean “Is pinned on the interface” (compute=_compute_is_pinned)
- `unpin_dt` Datetime “Unpin date” (index)
- `last_interest_dt` Datetime “Last Activity” (index)
- `last_seen_dt` Datetime “Last seen date”
- `rtc_session_ids` One2many → `discuss.channel.rtc.session` “RTC Sessions”
- `rtc_inviting_session_id` Many2one → `discuss.channel.rtc.session` “Ringing session”

Public methods: `create`, `unlink`, `write`

Extension points: `_check_channel_role_supported`, `_get_html_link_title`, `_get_member_html_link`, `_get_member_store_list`, `_get_recording_permissions`, `_get_rtc_invite_members_domain`, `_get_rtc_server_info`

## `discuss.channel.rtc.session` (defines)

Mail RTC session

Inherits: `bus.listener.mixin`

- `channel_member_id` Many2one → `discuss.channel.member` (required)
- `channel_id` Many2one → `discuss.channel` (readonly, store, related=channel_member_id.channel_id)
- `partner_id` Many2one → `res.partner` “Partner” (store, index, related=channel_member_id.partner_id)
- `guest_id` Many2one → `mail.guest` (related=channel_member_id.guest_id)
- `write_date` Datetime “Last Updated On” (index)
- `is_screen_sharing_on` Boolean “Is sharing the screen”
- `is_camera_on` Boolean “Is sending user video”
- `is_muted` Boolean “Is microphone muted”
- `is_deaf` Boolean “Has disabled incoming sound”

Public methods: `action_disconnect`, `create`, `unlink`

## `discuss.gif.favorite` (defines)

Save favorite GIF from Tenor API

- `tenor_gif_id` Char “GIF id from Tenor” (required)

## `discuss.voice.metadata` (defines)

Metadata for voice attachments

- `attachment_id` Many2one → `ir.attachment` (index)

## `ir.attachment` (extends)

- `voice_ids` One2many → `discuss.voice.metadata`

Extension points: `_post_add_create`

## `ir.websocket` (extends)


## `mail.guest` (defines)

Guest

Inherits: `avatar.mixin`, `bus.listener.mixin`

- `name` Char “Name” (required)
- `access_token` Char “Access Token” (required, readonly)
- `country_id` Many2one → `res.country` “Country”
- `email` Char
- `lang` Selection “Language”
- `timezone` Selection “Timezone”
- `channel_ids` Many2many → `discuss.channel` “Channels”
- `presence_ids` One2many → `mail.presence`
- `im_status` Selection (compute=_compute_im_status)
- `offline_since` Datetime “Offline since” (compute=_compute_im_status)

Extension points: `_get_guest_from_context`, `_get_guest_from_token`, `_get_im_status_access_token`, `_get_or_create_guest`, `_get_timezone_from_request`

## `mail.message` (extends)

- `call_history_ids` One2many → `discuss.call.history`
- `channel_id` Many2one → `discuss.channel` (compute=_compute_channel_id)

Extension points: `_get_with_access`

## `res.groups` (extends)


Public methods: `write`

## `res.partner` (extends)

- `channel_ids` Many2many → `discuss.channel` “Channels”
- `channel_member_ids` One2many → `discuss.channel.member`
- `is_in_call` Boolean (compute=_compute_is_in_call)
- `rtc_session_ids` One2many → `discuss.channel.rtc.session`

Public methods: `get_mention_suggestions_from_channel`, `search_for_channel_invite`

Extension points: `_get_channel_invite_domain`

## `res.users` (extends)

- `is_in_call` Boolean “Is in call” (related=partner_id.is_in_call)

Public methods: `create`, `unlink`, `write`

## `res.users.settings` (extends)

Inherits: `bus.sync.mixin`

- `volume_settings_ids` One2many → `res.users.settings.volumes` “Volumes of other partners”
- `channel_notifications` Selection

Public methods: `set_volume_setting`

## `res.users.settings.volumes` (defines)

User Settings Volumes

Inherits: `bus.listener.mixin`, `bus.sync.mixin`

- `user_setting_id` Many2one → `res.users.settings` (required, index)
- `partner_id` Many2one → `res.partner` (index)
- `guest_id` Many2one → `res.partner` (index)
- `volume` Float

## `fetchmail.server` (defines)

Incoming Mail Server

- `name` Char “Name” (required)
- `active` Boolean “Active”
- `state` Selection “Status” (readonly, index)
- `server` Char “Server Name”
- `port` Integer
- `server_type` Selection “Server Type” (required, index)
- `server_type_info` Text “Server Type Info” (compute=_compute_server_type_info)
- `is_ssl` Boolean “SSL/TLS”
- `attach` Boolean “Keep Attachments”
- `original` Boolean “Keep Original”
- `date` Datetime “Last Fetch Date” (readonly)
- `error_date` Datetime “Last Error Date” (readonly)
- `error_message` Text “Last Error Message” (readonly)
- `user` Char “Username”
- `password` Char
- `object_id` Many2one → `ir.model` “Create a New Record”
- `priority` Integer “Server Priority”
- `message_ids` One2many → `mail.mail` “Messages” (readonly)
- `configuration` Text “Configuration” (readonly)
- `script` Char (readonly)

Public methods: `button_confirm_login`, `create`, `fetch_mail`, `onchange_server_type`, `set_draft`, `unlink`, `write`

Extension points: `_get_connection_type`

## `ir.access` (extends)

Inherits: `mail.thread`

- `active` Boolean
- `domain` Char
- `operation` Selection

## `ir.actions.act_window.view` (extends)

- `view_mode` Selection

## `ir.actions.server` (extends)

Server Action

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char
- `model_id` Many2one
- `crud_model_id` Many2one
- `link_field_id` Many2one
- `update_path` Char
- `value` Text
- `evaluation_type` Selection
- `webhook_url` Char
- `state` Selection
- `followers_type` Selection “Followers Type” (store, compute=_compute_followers_type)
- `followers_partner_field_name` Char “Followers Field” (store, compute=_compute_followers_info)
- `partner_ids` Many2many → `res.partner` (store, compute=_compute_followers_info)
- `subtype_ids` Many2many → `mail.message.subtype` “Subscriptions” (store)
- `template_id` Many2one → `mail.template` (store, compute=_compute_template_id)
- `mail_post_autofollow` Boolean “Subscribe Recipients” (store, compute=_compute_mail_post_autofollow)
- `log_note_note` Html “Internal Note” (store, compute=_compute_log_note_note)
- `has_activity_plans` Boolean (compute=_compute_has_activity_plans)
- `activity_plan_id` Many2one → `mail.activity.plan` “Activity Plan” (store, compute=_compute_activity_plan_id)
- `activity_plan_has_user_on_demand` Boolean (related=activity_plan_id.has_user_on_demand)
- `activity_type_id` Many2one → `mail.activity.type` “Activity Type” (store, compute=_compute_activity_type_id)
- `activity_summary` Char “Summary” (store)
- `activity_note` Html “Note” (store)
- `activity_date_deadline_range` Integer “Due In” (store, compute=_compute_activity_date_deadline_range)
- `activity_date_deadline_range_type` Selection “Due type” (store, compute=_compute_activity_date_deadline_range_type)
- `activity_user_type` Selection “User Type” (store, compute=_compute_activity_user_type)
- `activity_user_id` Many2one → `res.users` “Responsible” (store, compute=_compute_activity_user_id)
- `activity_user_field_name` Char “User Field” (store, compute=_compute_activity_user_field_name)
- `activity_role_id` Many2one → `res.role` “Responsible Role” (store, compute=_compute_activity_role_id)

Extension points: `_check_activity_plan_and_type`, `_get_eval_context`, `_get_warning_messages`

## `ir.attachment` (extends)

- `thumbnail` Image
- `has_thumbnail` Boolean (compute=_compute_has_thumbnail)

Public methods: `register_as_main_attachment`

Extension points: `_get_ownership_token`, `_get_thumbnail_token`, `_post_add_create`

## `ir.config_parameter` (extends)


Public methods: `create`, `set_bool`, `set_str`, `write`

## `ir.cron` (extends)

Inherits: `mail.thread`, `mail.activity.mixin`

- `user_id` Many2one
- `interval_number` Integer
- `interval_type` Selection
- `priority` Integer
- `active` Boolean

## `ir.http` (extends)


Public methods: `session_info`

## `ir.mail_server` (extends)

- `mail_template_ids` One2many → `mail.template` “Mail template using this mail server” (readonly)
- `owner_user_id` Many2one → `res.users`
- `owner_limit_time` Datetime “Owner Limit Time”
- `owner_limit_count` Integer “Owner Limit Count”

Extension points: `_check_forced_mail_server`, `_get_default_bounce_address`, `_get_default_from_address`, `_get_personal_mail_servers_limit`, `_get_test_email_from`

## `ir.model` (extends)

- `is_mail_thread` Boolean “Has Mail Thread”
- `is_mail_activity` Boolean “Has Mail Activity”
- `is_mail_blacklist` Boolean “Has Mail Blacklist”

Public methods: `write`

Extension points: `_get_definitions`, `_get_model_definitions`

## `ir.model.fields` (extends)

- `tracking` Integer “Enable Ordered Tracking”

## `ir.qweb` (extends)


Extension points: `_get_template_cache_keys`

## `ir.ui.menu` (extends)


Extension points: `_get_best_backend_root_menu_id_for_model`

## `ir.ui.view` (extends)

- `type` Selection
- `technical_usage` Selection

Extension points: `_get_view_info`

## `ir.websocket` (extends)


## `kpi.provider` (extends)


Public methods: `get_kpi_summary`, `get_mail_activities_kpi_summary`

## `mail.activity` (defines)

Activity

- `res_model_id` Many2one → `ir.model` (index)
- `res_model` Char “Related Document Model” (readonly, store, index, related=res_model_id.model)
- `res_model_name` Char “Model” (related=res_model_id.display_name)
- `res_id` Many2oneReference “Related Document ID” (index)
- `res_name` Char “Document Name” (readonly, store, compute=_compute_res_name)
- `res_access_read` Boolean
- `res_access_write` Boolean
- `res_access_create` Boolean
- `res_access_unlink` Boolean
- `activity_type_id` Many2one → `mail.activity.type` “Activity Type”
- `activity_category` Selection (readonly, related=activity_type_id.category)
- `activity_decoration` Selection (readonly, related=activity_type_id.decoration_type)
- `icon` Char “Icon” (readonly, related=activity_type_id.icon)
- `activity_plan_id` Many2one → `mail.activity.plan` “Plan”
- `activity_template_id` Many2one → `mail.activity.plan.template` “Generated From”
- `phone` Char “Phone” (store, compute=_compute_phone)
- `summary` Char “Summary” (store, compute=_compute_summary)
- `note` Html “Note” (store, compute=_compute_note)
- `date_deadline` Date “Due Date” (required, store, index, compute=_compute_date_deadline)
- `date_done` Date “Done Date” (store, compute=_compute_date_done)
- `feedback` Text “Feedback”
- `automated` Boolean “Automated activity” (readonly)
- `technical_usage` Selection (readonly)
- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `user_id` Many2one → `res.users` (store, index, compute=_compute_user_id)
- `role_id` Many2one → `res.role` (store, compute=_compute_role_id)
- `user_tz` Selection “Timezone” (store, related=user_id.tz)
- `state` Selection (compute=_compute_state)
- `mail_template_ids` Many2many (readonly, related=activity_type_id.mail_template_ids)
- `can_write` Boolean (compute=_compute_can_write)
- `active` Boolean

Public methods: `action_close_dialog`, `action_done`, `action_done_redirect_to_other`, `action_done_schedule_next`, `action_feedback`, `action_feedback_schedule_next`, `action_notify`, `action_open_document`, `action_reschedule_customdate`, `action_reschedule_nextweek`, `action_reschedule_today`, `action_reschedule_tomorrow`, `create`, `default_get`, `get_activity_data`, `unlink`, `write`

Extension points: `_action_done`, `_get_activity_done_message_extra_values`, `_get_phone_number_from_record`, `_get_phone_numbers_by_activity`

## `mail.activity.mixin` (defines)

Activity Mixin

- `activity_ids` One2many → `mail.activity`
- `activity_state` Selection “Activity State” (compute=_compute_activity_state)
- `activity_user_id` Many2one → `res.users` (readonly, compute=_compute_activity_user_id)
- `activity_type_id` Many2one → `mail.activity.type` (related=activity_ids.activity_type_id)
- `activity_type_icon` Char “Activity Type Icon” (related=activity_ids.icon)
- `activity_date_deadline` Date “Next Activity Deadline” (readonly, compute=_compute_activity_date_deadline)
- `my_activity_date_deadline` Date “My Activity Deadline” (readonly, compute=_compute_my_activity_date_deadline)
- `activity_summary` Char “Next Activity Summary” (related=activity_ids.summary)
- `activity_exception_decoration` Selection (compute=_compute_activity_exception_type)
- `activity_exception_icon` Char “Icon” (compute=_compute_activity_exception_type)
- `activity_plans_ids` Many2many → `mail.activity.plan` “Activity Plans” (compute=_compute_activity_plans_ids)

Public methods: `action_reschedule_my_next_customdate`, `action_reschedule_my_next_nextweek`, `action_reschedule_my_next_today`, `action_reschedule_my_next_tomorrow`, `activity_feedback`, `activity_reschedule`, `activity_schedule`, `activity_search`, `activity_send_mail`, `activity_unlink`

## `mail.activity.plan` (defines)

Activity Plan

- `name` Char “Name” (required)
- `company_id` Many2one → `res.company`
- `template_ids` One2many → `mail.activity.plan.template` “Activities”
- `active` Boolean
- `res_model_id` Many2one → `ir.model` “Applies to” (required, store, compute=_compute_res_model_id)
- `res_model` Selection “Model” (required)
- `steps_count` Integer (compute=_compute_steps_count)
- `has_user_on_demand` Boolean “Has on demand responsible” (compute=_compute_has_user_on_demand)

Extension points: `_check_res_model_compatibility_with_templates`, `_get_model_selection`

## `mail.activity.plan.template` (defines)

Activity plan template

- `plan_id` Many2one → `mail.activity.plan` “Plan” (required, index)
- `res_model` Selection (related=plan_id.res_model)
- `company_id` Many2one (related=plan_id.company_id)
- `sequence` Integer
- `activity_type_id` Many2one → `mail.activity.type` (required, index)
- `delay_count` Integer “Interval”
- `delay_unit` Selection “Delay units” (required)
- `delay_from` Selection “Trigger” (required)
- `icon` Char “Icon” (readonly, related=activity_type_id.icon)
- `summary` Char “Summary” (store, compute=_compute_summary)
- `responsible_type` Selection “Assignment” (required, store, compute=_compute_responsible_type)
- `responsible_id` Many2one → `res.users` (store, compute=_compute_responsible_id)
- `role_id` Many2one → `res.role` (store, compute=_compute_role_id)
- `note` Html “Note” (store, compute=_compute_note)
- `suggested_next_type_id` Many2one “Suggested Next Activity” (related=activity_type_id.suggested_next_type_id)

Extension points: `_check_activity_type_res_model`, `_check_responsible`, `_get_date_deadline`

## `mail.activity.type` (defines)

Activity Type

- `name` Char “Name” (required)
- `summary` Char “Default Summary”
- `sequence` Integer “Sequence”
- `active` Boolean
- `create_uid` Many2one → `res.users` (index)
- `delay_count` Integer “Schedule”
- `delay_unit` Selection “Delay units” (required)
- `delay_label` Char (compute=_compute_delay_label)
- `delay_from` Selection “Delay Type” (required)
- `icon` Char “Icon”
- `decoration_type` Selection “Decoration Type”
- `res_model` Selection “Model”
- `suggested_next_type_id` Many2one → `mail.activity.type` “Suggest Next Activity”
- `previous_type_ids` Many2many → `mail.activity.type` “Preceding Activities”
- `category` Selection “Action”
- `mail_template_ids` Many2many → `mail.template` “Email templates”
- `default_user_id` Many2one → `res.users` “Default User”
- `default_role_id` Many2one → `res.role` “Role”
- `default_note` Html “Default Note”
- `kpi_provider_visibility` Selection “KPI Provider Visibility”
- `initial_res_model` Selection “Initial model” (compute=_compute_initial_res_model)
- `res_model_change` Boolean “Model has change”

Public methods: `action_archive`, `unlink`, `write`

Extension points: `_check_activity_type_res_model`, `_get_date_deadline`, `_get_model_info_by_xmlid`, `_get_model_selection`

## `mail.alias` (defines)

Email Alias

- `alias_name` Char “Alias Name”
- `alias_full_name` Char “Alias Email” (store, compute=_compute_alias_full_name)
- `alias_domain_id` Many2one → `mail.alias.domain` “Alias Domain”
- `alias_domain` Char “Alias domain name” (related=alias_domain_id.name)
- `alias_model_id` Many2one → `ir.model` (required)
- `alias_defaults` Text “Default Values” (required)
- `alias_force_thread_id` Integer “Record Thread ID”
- `alias_parent_model_id` Many2one → `ir.model`
- `alias_parent_thread_id` Integer “Parent Record Thread ID”
- `alias_contact` Selection “Alias Contact Security” (required)
- `alias_incoming_local` Boolean “Local-part based incoming detection”
- `alias_bounced_content` Html “Custom Bounced Message”
- `alias_status` Selection (store, compute=_compute_alias_status)

Public methods: `create`, `open_document`, `open_parent_document`, `write`

Extension points: `_check_alias_defaults`, `_check_alias_domain_clash`, `_check_alias_domain_id_mc`, `_check_alias_is_ascii`, `_check_unique`, `_get_alias_bounced_body`, `_get_alias_bounced_body_fallback`, `_get_alias_contact_description`, `_get_alias_invalid_body`

## `mail.alias.domain` (defines)

Email Domain

- `name` Char “Name” (required)
- `company_ids` One2many → `res.company` “Companies”
- `sequence` Integer
- `bounce_alias` Char “Bounce Alias” (required)
- `bounce_email` Char “Bounce Email” (compute=_compute_bounce_email)
- `catchall_alias` Char “Catchall Alias” (required)
- `catchall_email` Char “Catchall Email” (compute=_compute_catchall_email)
- `default_from` Char “Default From Alias”
- `default_from_email` Char “Default From” (compute=_compute_default_from_email)

Public methods: `create`, `write`

Extension points: `_check_bounce_catchall_uniqueness`, `_check_default_from_not_used_by_users`, `_check_name`

## `mail.alias.mixin` (defines)

Email Aliases Mixin

Inherits: `mail.alias.mixin.optional`

- `alias_id` Many2one (required, index)
- `alias_name` Char
- `alias_defaults` Text

## `mail.alias.mixin.optional` (defines)

Email Aliases Mixin (light)

- `alias_id` Many2one → `mail.alias` “Alias”
- `alias_name` Char (related=alias_id.alias_name)
- `alias_domain_id` Many2one → `mail.alias.domain` “Alias Domain” (related=alias_id.alias_domain_id)
- `alias_domain` Char “Alias Domain Name” (related=alias_id.alias_domain)
- `alias_defaults` Text (related=alias_id.alias_defaults)
- `alias_email` Char “Email Alias” (compute=_compute_alias_email)

Public methods: `copy_data`, `create`, `unlink`, `write`

## `mail.blacklist` (defines)

Mail Blacklist

Inherits: `mail.thread`

- `email` Char “Email Address” (required)
- `active` Boolean

Public methods: `action_add`, `create`, `mail_action_blacklist_remove`, `write`

## `mail.call.artifact` (defines)

Call Artifact

- `discuss_call_history_id` Many2one → `discuss.call.history` “Discuss Call History” (index)
- `recording_started_by_id` Many2one → `res.users` “Recording Started By” (readonly)
- `recording_upload_pending` Boolean
- `media_id` Many2one → `ir.attachment` “Media Attachment” (compute=_compute_media_id)
- `start_ms` Integer “Start (ms)” (required)
- `end_ms` Integer “End (ms)” (required)

Extension points: `_check_artifacts_overlap`, `_get_artifacts_grouped_by_call`, `_get_related_call`

## `mail.canned.response` (defines)

Canned Response

- `source` Char “Shortcut” (required)
- `substitution` Text “Substitution” (required)
- `last_used` Datetime “Last Used”
- `group_ids` Many2many → `res.groups` “Authorized Groups”
- `is_shared` Boolean “Determines if the canned_response is currently shared with other users” (store, compute=_compute_is_shared)
- `is_editable` Boolean “Determines if the canned response can be edited by the current user” (compute=_compute_is_editable)

Public methods: `create`, `unlink`, `write`

## `mail.composer.mixin` (defines)

Mail Composer Mixin

Inherits: `mail.render.mixin`

- `subject` Char “Subject” (store, compute=_compute_subject)
- `body` Html “Contents” (store, compute=_compute_body)
- `body_has_template_value` Boolean “Body content is the same as the template” (compute=_compute_body_has_template_value)
- `template_id` Many2one → `mail.template`
- `lang` Char (store, compute=_compute_lang)
- `is_mail_template_editor` Boolean “Is Editor” (compute=_compute_is_mail_template_editor)
- `can_edit_body` Boolean “Can Edit Body” (compute=_compute_can_edit_body)

## `mail.followers` (defines)

Document Follower

- `res_model` Char “Related Document Model Name” (required, index)
- `res_id` Many2oneReference “Related Document ID” (index)
- `partner_id` Many2one → `res.partner` “Related Partner” (required, index)
- `subtype_ids` Many2many → `mail.message.subtype` “Subtype”
- `name` Char “Name” (related=partner_id.name)
- `email` Char “Email” (related=partner_id.email)
- `is_active` Boolean “Is Active” (related=partner_id.active)

Extension points: `_get_mail_doc_to_followers`, `_get_recipient_data`, `_get_subscription_data`

## `mail.gateway.allowed` (defines)

Mail Gateway Allowed

- `email` Char “Email Address” (required)
- `email_normalized` Char “Normalized Email” (store, index, compute=_compute_email_normalized)

Public methods: `get_empty_list_help`

## `mail.ice.server` (defines)

ICE Server

- `server_type` Selection “Type” (required)
- `uri` Char “URI” (required)
- `username` Char
- `credential` Char

Extension points: `_get_ice_servers`, `_get_local_ice_servers`

## `mail.link.preview` (defines)

Store link preview data

Inherits: `bus.listener.mixin`

- `source_url` Char “URL” (required)
- `og_type` Char “Type”
- `og_title` Char “Title”
- `og_site_name` Char “Site name”
- `og_image` Char “Image”
- `og_description` Text “Description”
- `og_mimetype` Char “MIME type”
- `image_mimetype` Char “Image MIME type”
- `create_date` Datetime (index)
- `message_link_preview_ids` One2many → `mail.message.link.preview`

Extension points: `_create_from_message_and_notify`

## `mail.mail` (defines)

Outgoing Mail

- `mail_message_id` Many2one → `mail.message` (required, index)
- `mail_message_id_int` Integer (compute=_compute_mail_message_id_int)
- `message_type` Selection (related=mail_message_id.message_type)
- `body_html` Text “Text Contents”
- `body_content` Html “Rich-text Contents” (compute=_compute_body_content)
- `references` Text “References” (readonly)
- `headers` Text “Headers”
- `restricted_attachment_count` Integer “Restricted attachments” (compute=_compute_restricted_attachments)
- `unrestricted_attachment_ids` Many2many → `ir.attachment` “Unrestricted Attachments” (compute=_compute_restricted_attachments)
- `is_notification` Boolean “Notification Email”
- `email_to` Text “To”
- `email_cc` Char “Cc”
- `recipient_ids` Many2many → `res.partner` “To (Partners)”
- `recipient_cc_ids` Many2many → `res.partner` “Cc (Partners)”
- `state` Selection (readonly)
- `failure_type` Selection “Failure type”
- `failure_reason` Text “Failure Reason” (readonly)
- `auto_delete` Boolean “Auto Delete”
- `scheduled_date` Datetime “Scheduled Send Date”
- `fetchmail_server_id` Many2one → `fetchmail.server` (readonly)

Public methods: `action_open_document`, `action_retry`, `action_send_and_close`, `cancel`, `create`, `default_get`, `mark_outgoing`, `process_email_queue`, `send`, `send_after_commit`, `unlink`, `write`

Extension points: `_check_mail_server_id`, `_get_notification_status`, `_get_notification_values`, `_post_model_setup__`, `_prepare_outgoing_body`, `_prepare_outgoing_list`

## `mail.message` (defines)

Message

Inherits: `bus.listener.mixin`

- `subject` Char “Subject”
- `date` Datetime “Date”
- `body` Html “Contents”
- `preview` Char “Preview” (compute=_compute_preview)
- `linked_message_ids` Many2many → `mail.message` (compute=_compute_linked_message_ids)
- `message_link_preview_ids` One2many → `mail.message.link.preview`
- `reaction_ids` One2many → `mail.message.reaction` “Reactions”
- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `parent_id` Many2one → `mail.message`
- `child_ids` One2many → `mail.message`
- `model` Char “Related Document Model”
- `res_id` Many2oneReference “Related Document ID”
- `res_access_read` Boolean
- `res_access_write` Boolean
- `res_access_create` Boolean
- `res_access_unlink` Boolean
- `record_name` Char “Message Record Name” (compute=_compute_record_name)
- `record_alias_domain_id` Many2one → `mail.alias.domain`
- `record_company_id` Many2one → `res.company`
- `message_type` Selection (required)
- `subtype_id` Many2one → `mail.message.subtype` (index)
- `mail_activity_type_id` Many2one → `mail.activity.type`
- `is_internal` Boolean “Employee Only”
- `email_from` Char “From”
- `author_id` Many2one → `res.partner` (index)
- `author_avatar` Binary “Author's avatar” (related=author_id.avatar_128)
- `author_guest_id` Many2one → `mail.guest` “Guest”
- `is_current_user_or_guest_author` Boolean (compute=_compute_is_current_user_or_guest_author)
- `partner_ids` Many2many → `res.partner` “Recipients (To)”
- `partner_cc_ids` Many2many → `res.partner` “Recipients (Cc)”
- `incoming_email_to` Text “Emails To”
- `incoming_email_cc` Char “Emails Cc”
- `outgoing_email_to` Char “emails To”
- `notified_partner_ids` Many2many → `res.partner` “Partners with Need Action”
- `needaction` Boolean “Need Action” (compute=_compute_needaction)
- `has_error` Boolean “Has error” (compute=_compute_has_error)
- `notification_ids` One2many → `mail.notification`
- `bookmarked_partner_ids` Many2many → `res.partner` “Bookmarked By”
- `pinned_at` Datetime “Pinned”
- `is_bookmarked` Boolean “Bookmarked” (compute=_compute_is_bookmarked)
- `ended_poll_ids` One2many → `mail.poll`
- `started_poll_ids` One2many → `mail.poll`
- `has_poll` Boolean (compute=_compute_has_poll)
- `reply_to_force_new` Boolean “No threading for answers”
- `message_id` Char “Message-Id” (readonly)
- `reply_to` Char “Reply-To”
- `mail_server_id` Many2one → `ir.mail_server`
- `email_layout_xmlid` Char “Layout”
- `email_add_signature` Boolean
- `mail_ids` One2many → `mail.mail` “Mails”

Public methods: `action_open_document`, `create`, `default_get`, `export_data`, `mark_all_as_read`, `mark_as_unread`, `set_message_done`, `unlink`, `write`

Extension points: `_get_empty_domain`, `_get_message_id`, `_get_reply_to`, `_get_search_domain_share`, `_get_tracking_values_domain`, `_get_with_access`

## `mail.message.link.preview` (defines)

Link between link previews and messages

Inherits: `bus.listener.mixin`

- `message_id` Many2one → `mail.message` (required, index)
- `link_preview_id` Many2one → `mail.link.preview` (required, index)
- `sequence` Integer “Sequence”
- `is_hidden` Boolean
- `author_id` Many2one (related=message_id.author_id)

## `mail.message.reaction` (defines)

Message Reaction

- `message_id` Many2one → `mail.message` “Message” (required, readonly, index)
- `content` Char “Content” (required, readonly)
- `partner_id` Many2one → `res.partner` “Reacting Partner” (readonly)
- `guest_id` Many2one → `mail.guest` “Reacting Guest” (readonly)

## `mail.message.schedule` (defines)

Scheduled Message

- `mail_message_id` Many2one → `mail.message` “Message” (required)
- `notification_parameters` Text “Notification Parameter”
- `scheduled_datetime` Datetime “Scheduled Send Date” (required)

Public methods: `create`, `force_send`

## `mail.message.subtype` (defines)

Message Subtype

- `name` Char “Message Type” (required)
- `description` Text “Description”
- `internal` Boolean “Internal Only”
- `parent_id` Many2one → `mail.message.subtype` “Parent”
- `relation_field` Char “Relation field”
- `res_model` Char “Model”
- `default` Boolean “Default”
- `sequence` Integer “Sequence”
- `hidden` Boolean “Hidden”
- `track_recipients` Boolean “Track Recipients”

Public methods: `default_subtypes`, `write`

Extension points: `_get_auto_subscription_subtypes`, `_get_model_info_by_xmlid`

## `mail.message.translation` (defines)

Message Translation

- `message_id` Many2one → `mail.message` (required)
- `source_lang` Char “Source Language” (required)
- `target_lang` Char “Target Language” (required)
- `body` Html “Translation Body” (required)
- `create_date` Datetime (index)

## `mail.notification` (defines)

Message Notification

- `author_id` Many2one → `res.partner`
- `mail_message_id` Many2one → `mail.message` (required, index)
- `mail_mail_id` Many2one → `mail.mail` (index)
- `res_partner_id` Many2one → `res.partner` (index)
- `mail_email_address` Char
- `notification_type` Selection “Notification Type” (required, index)
- `notification_status` Selection “Status” (index)
- `is_read` Boolean “Is Read” (index)
- `read_date` Datetime “Read Date”
- `failure_type` Selection “Failure type”
- `failure_reason` Text “Failure reason”

Public methods: `create`, `format_failure_reason`, `write`

## `mail.poll` (defines)

Poll

- `allow_multiple_options` Boolean
- `end_message_id` Many2one → `mail.message` (index)
- `option_ids` One2many → `mail.poll.option` (required)
- `poll_end_dt` Datetime (index)
- `poll_question` Char (required)
- `start_message_id` Many2one → `mail.message` (required, index)
- `winning_option_id` Many2one → `mail.poll.option` (compute=_compute_winning_option_ids)

## `mail.poll.option` (defines)

Poll option

- `number_of_votes` Integer (compute=_compute_number_of_votes)
- `option_emoji` Char “Emoji”
- `option_label` Char “Label” (required)
- `poll_id` Many2one → `mail.poll` (required, index)
- `selected_by_self` Boolean (compute=_compute_selected_by_self)
- `vote_ids` One2many → `mail.poll.vote`
- `vote_percentage` Integer (compute=_compute_vote_percentage)

Public methods: `write`

## `mail.poll.vote` (defines)

Poll vote

- `guest_id` Many2one → `mail.guest`
- `is_self_vote` Boolean (compute=_compute_is_self_vote)
- `option_id` Many2one → `mail.poll.option` (required, index)
- `user_id` Many2one → `res.users`

Public methods: `create`

Extension points: `_check_allow_multiple_options`

## `mail.presence` (defines)

User/Guest Presence

Inherits: `bus.listener.mixin`

- `user_id` Many2one → `res.users`
- `guest_id` Many2one → `mail.guest`
- `last_poll` Datetime “Last Poll”
- `last_presence` Datetime “Last Presence”
- `status` Selection

Public methods: `create`, `unlink`, `write`

## `mail.push` (defines)

Push Notification

- `mail_push_device_id` Many2one → `mail.push.device` “devices” (required)
- `payload` Text

## `mail.push.device` (defines)

Push Notification Device

- `partner_id` Many2one → `res.partner` “Partner” (required, index)
- `endpoint` Char “Browser endpoint” (required)
- `keys` Char “Browser keys” (required)
- `expiration_time` Datetime “Expiration Token Date”

Public methods: `get_web_push_vapid_public_key`, `register_devices`, `unregister_devices`

## `mail.render.mixin` (defines)

Mail Render Mixin

- `lang` Char “Language”
- `render_model` Char “Rendering Model” (compute=_compute_render_model)

Public methods: `create`, `write`

Extension points: `_check_access_right_dynamic_template`

## `mail.scheduled.message` (defines)

Scheduled Message

- `subject` Char “Subject”
- `body` Html “Contents”
- `scheduled_date` Datetime “Scheduled Date” (required)
- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `composition_comment_option` Selection “Comment Options”
- `model` Char “Related Document Model” (required)
- `res_id` Many2oneReference “Related Document Id” (required)
- `author_id` Many2one → `res.partner` (required)
- `partner_ids` Many2many → `res.partner` “Recipients (To)”
- `partner_cc_ids` Many2many → `res.partner` “Recipients (Cc)”
- `is_note` Boolean “Is a note”
- `notification_parameters` Text “Notification parameters”
- `send_context` Json “Sending Context”
- `res_access` Boolean (compute=_compute_res_access)

Public methods: `create`, `open_edit_form`, `post_message`, `write`

Extension points: `_check_model`, `_check_scheduled_date`, `_post_message`, `_post_message_send`, `_post_messages_cron`

## `mail.template` (defines)

Email Template

Inherits: `mail.render.mixin`, `template.reset.mixin`

- `name` Char “Name”
- `description` Text “Template Description”
- `active` Boolean
- `template_category` Selection (compute=_compute_template_category)
- `model_id` Many2one → `ir.model`
- `model` Char “Related Document Model” (readonly, store, index, related=model_id.model)
- `subject` Char “Subject”
- `email_from` Char “Send From”
- `user_id` Many2one → `res.users` “Owner”
- `use_default_to` Boolean “Default Recipients”
- `email_to` Char “To (Emails)”
- `partner_to` Char “To (Partners)”
- `email_cc` Char “Cc”
- `partner_cc` Char “Cc (Partners)”
- `reply_to` Char “Reply To Address”
- `body_html` Html “Body”
- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `report_template_ids` Many2many → `ir.actions.report` “Dynamic Reports”
- `email_layout_xmlid` Char “Email Notification Layout”
- `email_layout_force_header` Boolean “Force Header”
- `email_layout_force_footer` Boolean “Force Footer”
- `mail_server_id` Many2one → `ir.mail_server`
- `scheduled_date` Char “Scheduled Date”
- `auto_delete` Boolean “Auto Delete”
- `ref_ir_act_window` Many2one → `ir.actions.act_window` (readonly)
- `can_write` Boolean (compute=_compute_can_write)
- `is_template_editor` Boolean (compute=_compute_is_template_editor)
- `has_dynamic_reports` Boolean (compute=_compute_has_dynamic_reports)
- `has_mail_server` Boolean (compute=_compute_has_mail_server)

Public methods: `action_open_mail_preview`, `copy`, `create`, `create_action`, `default_get`, `send_mail`, `send_mail_batch`, `unlink`, `unlink_action`, `write`

Extension points: `_check_abstract_models`, `_check_can_be_rendered`, `_get_dynamic_field_names`, `_get_non_abstract_models_domain`

## `mail.thread` (defines)

Email Thread

Inherits: `bus.listener.mixin`, `mail.track.mixin`

- `message_is_follower` Boolean “Is Follower” (compute=_compute_message_is_follower)
- `message_follower_ids` One2many → `mail.followers` “Followers”
- `message_partner_ids` Many2many → `res.partner` “Followers (Partners)” (compute=_compute_message_partner_ids)
- `message_ids` One2many → `mail.message` “Messages”
- `has_message` Boolean (compute=_compute_has_message)
- `message_needaction` Boolean “Action Needed” (compute=_compute_message_needaction)
- `message_needaction_counter` Integer “Number of Actions” (compute=_compute_message_needaction)
- `message_has_error` Boolean “Message Delivery error” (compute=_compute_message_has_error)
- `message_has_error_counter` Integer “Number of errors” (compute=_compute_message_has_error)
- `message_attachment_count` Integer “Attachment Count” (compute=_compute_message_attachment_count)

Public methods: `create`, `get_empty_list_help`, `get_views`, `message_change_thread`, `message_get_followers`, `message_mail_with_source`, `message_new`, `message_notify`, `message_parse`, `message_post`, `message_post_with_source`, `message_process`, `message_route`, `message_subscribe`, `message_unsubscribe`, `message_update`, `message_update_siblings_subscription`, `notify_cancel_by_type`, `set_message_pin`, `unlink`, `write`

Extension points: `_check_can_update_message_content`, `_create_attachments_for_post`, `_get_action_link_params`, `_get_allowed_access_params`, `_get_allowed_message_params`, `_get_bounced_message_data`, `_get_customer_information`, `_get_customer_portal_message_types`, `_get_log_valid_parameters`, `_get_mail_thread_data_attachments`, `_get_message_create_ignore_field_names`, `_get_message_create_valid_field_names`, `_get_message_parameters_updated_for_rendering`, `_get_model_description`, `_get_notify_valid_parameters`, `_get_parent_message`, `_get_share_message_domain`, `_get_source_from_ref`, `_get_thread_with_access`

## `mail.thread.blacklist` (defines)

Mail Blacklist mixin

Inherits: `mail.thread`

- `email_normalized` Char “Normalized Email” (store, compute=_compute_email_normalized)
- `is_blacklisted` Boolean “Blacklist” (compute=_compute_is_blacklisted)
- `message_bounce` Integer “Bounce”

Public methods: `mail_action_blacklist_remove`

## `mail.thread.main.attachment` (defines)

Mail Main Attachment management

Inherits: `mail.thread`

- `message_main_attachment_id` Many2one → `ir.attachment` “Main Attachment”

## `mail.thread.subject.suggested` (defines)

Thread with suggested subject

Inherits: `mail.thread`


## `mail.track.mixin` (defines)

Mail Track Mixin


Public methods: `fields_get`, `write`

Extension points: `_create_mail_tracking_values`, `_create_mail_tracking_values_property`

## `mail.tracking.duration.mixin` (defines)

Mixin to compute the time a record has spent in each value a many2one field can take

Inherits: `mail.thread`

- `duration_tracking` Json “Status time” (store, compute=_compute_duration_tracking)
- `rotting_days` Integer “Days Rotting” (compute=_compute_rotting)
- `is_rotting` Boolean “Rotting” (compute=_compute_rotting)

Extension points: `_get_rotting_depends_fields`, `_get_rotting_domain`

## `base` (extends)


Public methods: `mail_allowed_qweb_expressions`, `mail_get_partner_fields`, `unlink`, `with_user`

Extension points: `_get_backend_root_menu_ids`, `_get_default_activity_view`, `_get_html_link`

## `res.company` (extends)

- `alias_domain_id` Many2one → `mail.alias.domain` “Email Domain”
- `bounce_email` Char “Bounce Email” (compute=_compute_bounce)
- `bounce_formatted` Char “Bounce” (compute=_compute_bounce)
- `catchall_email` Char “Catchall Email” (compute=_compute_catchall)
- `catchall_formatted` Char “Catchall” (compute=_compute_catchall)
- `default_from_email` Char “Default From” (readonly, related=alias_domain_id.default_from_email)
- `email_formatted` Char “Formatted Email” (compute=_compute_email_formatted)
- `email_primary_color` Char “Email Button Text”
- `email_secondary_color` Char “Email Button Color”

## `res.config.settings` (extends)

- `external_email_server_default` Boolean “Use Custom Email Servers”
- `fail_counter` Integer “Fail Mail” (compute=_compute_fail_counter)
- `alias_domain_id` Many2one → `mail.alias.domain` (related=company_id.alias_domain_id)
- `module_google_gmail` Boolean “Support Gmail Authentication”
- `module_microsoft_outlook` Boolean “Support Outlook Authentication”
- `restrict_template_rendering` Boolean “Restrict Template Rendering”
- `use_call_server` Boolean “Use Call Server”
- `use_twilio_rtc_servers` Boolean “Use Twilio ICE servers”
- `twilio_account_sid` Char “Account SID”
- `twilio_account_token` Char “Account Auth Token”
- `use_sfu_server` Boolean “Use SFU server”
- `sfu_server_url` Char “SFU Server URL”
- `sfu_server_key` Char “SFU Server key”
- `use_custom_sfu_client` Boolean “Use Custom SFU Bundle”
- `sfu_client_source` Text “SFU Client Bundle”
- `email_primary_color` Char (related=company_id.email_primary_color)
- `email_secondary_color` Char (related=company_id.email_secondary_color)
- `use_tenor_api` Boolean “Use Klipy API”
- `tenor_api_key` Char “Klipy API key”
- `use_google_translate_api` Boolean “Use Google Translate API”
- `google_translate_api_key` Char “Message Translation API Key”

Public methods: `action_open_sfu_client_source`, `action_save_sfu_client_asset`, `get_values`, `open_email_layout`, `open_mail_templates`, `set_values`

Extension points: `_get_sfu_client_asset`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.partner` (extends)

Inherits: `mail.thread.blacklist`, `mail.activity.mixin`

- `name` Char
- `email` Char
- `phone` Char
- `parent_id` Many2one
- `user_id` Many2one
- `vat` Char
- `contact_address_inline` Char

Public methods: `create`, `find_or_create`, `get_mention_suggestions`

Extension points: `_get_mention_suggestions_domain`, `_get_mention_token`, `_get_needaction_count`, `_get_view_cache_key`

## `res.role` (defines)

Represents a role in the system used to categorize users. Each role has a unique name and can be associated with multiple users. Roles can be mentioned in messages to notify all associated users.

- `name` Char (required)
- `active` Boolean
- `user_ids` Many2many → `res.users` “Users”
- `user_ids_count` Integer (compute=_compute_user_ids_count)

## `res.users` (extends)

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char
- `email` Char
- `phone` Char
- `login` Char
- `role_ids` Many2many → `res.role` “User Roles”
- `can_edit_role` Boolean (compute=_compute_can_edit_role)
- `notification_type` Selection (required, store, compute=_compute_notification_type)
- `presence_ids` One2many → `mail.presence`
- `out_of_office_from` Datetime
- `out_of_office_to` Datetime
- `out_of_office_message` Html “Vacation Responder”
- `is_out_of_office` Boolean “Out of Office” (compute=_compute_is_out_of_office)
- `im_status` Selection (compute=_compute_im_status)
- `offline_since` Datetime “Offline since” (compute=_compute_im_status)
- `manual_im_status` Selection “IM status manually set by the user”
- `outgoing_mail_server_id` Many2one → `ir.mail_server` (compute=_compute_outgoing_mail_server_id)
- `outgoing_mail_server_type` Selection (required, compute=_compute_outgoing_mail_server_id)
- `has_external_mail_server` Boolean (compute=_compute_has_external_mail_server)

Public methods: `action_archive`, `action_setup_outgoing_mail_server`, `action_test_outgoing_mail_server`, `create`, `write`

Extension points: `_get_activities_to_assign_count`, `_get_activity_groups`, `_get_current_persona`, `_get_im_status_access_token`, `_get_mail_server_setup_end_action`, `_get_mail_server_values`, `_get_portal_access_update_body`

## `template.reset.mixin` (defines)

Template Reset Mixin

- `template_fs` Char “Template Filename”

Public methods: `create`, `reset_template`

## `publisher_warranty.contract` (defines)

Publisher Warranty Contract


Public methods: `update_notification`

Extension points: `_get_message`, `_get_sys_logs`

## `base.module.uninstall` (extends)


Extension points: `_get_models`

## `base.partner.merge.automatic.wizard` (extends)


Extension points: `_action_next_screen`

## `mail.activity.schedule` (defines)

Activity schedule plan Wizard

- `res_model_id` Many2one → `ir.model` “Applies to” (store, compute=_compute_res_model_id)
- `res_model` Char “Model”
- `res_ids` Text “Document IDs” (store, compute=_compute_res_ids)
- `is_batch_mode` Boolean “Use in batch” (compute=_compute_is_batch_mode)
- `company_id` Many2one → `res.company` (compute=_compute_company_id)
- `error` Html (compute=_compute_error)
- `has_error` Boolean (compute=_compute_error)
- `warning` Html (compute=_compute_error)
- `has_warning` Boolean (compute=_compute_error)
- `plan_available_ids` Many2many → `mail.activity.plan` (store, compute=_compute_plan_available_ids)
- `plan_id` Many2one → `mail.activity.plan` (store, compute=_compute_plan_id)
- `plan_has_user_on_demand` Boolean (related=plan_id.has_user_on_demand)
- `plan_schedule_line_ids` One2many → `mail.activity.schedule.line` “Schedule Lines” (compute=_compute_plan_schedule_line_ids)
- `plan_on_demand_user_id` Many2one → `res.users`
- `plan_on_demand_role_id` Many2one → `res.role`
- `plan_date` Date “Plan Date” (store, compute=_compute_plan_date)
- `activity_type_available_ids` Many2many → `mail.activity.type` (compute=_compute_activity_type_available_ids)
- `activity_type_id` Many2one → `mail.activity.type` “Activity Type” (store, compute=_compute_activity_type_id)
- `activity_category` Selection (readonly, related=activity_type_id.category)
- `date_deadline` Date “Due Date” (store, compute=_compute_date_deadline)
- `summary` Char “Summary” (store, compute=_compute_summary)
- `phone` Char “Phone” (store, compute=_compute_phone)
- `note` Html “Note” (store, compute=_compute_note)
- `activity_user_id` Many2one → `res.users` (store, compute=_compute_activity_user_id)
- `activity_role_id` Many2one → `res.role` (store, compute=_compute_activity_role_id)
- `activity_user_id_fname` Char “User Field”

Public methods: `action_schedule_activities`, `action_schedule_activities_done`, `action_schedule_plan`, `default_get`, `get_model_options`

Extension points: `_action_schedule_activities`, `_action_schedule_activities_personal`, `_check_consistency`, `_check_plan_templates_error`, `_check_plan_templates_warning`, `_check_res_ids`, `_get_activity_type_available_base_domain`, `_get_applied_on_records`, `_get_phone_number`, `_get_phone_number_for_activity`, `_get_plan_available_base_domain`

## `mail.activity.schedule.line` (defines)

Mail Activity Schedule Line

- `activity_schedule_id` Many2one → `mail.activity.schedule` “Activity Schedule” (required)
- `line_description` Char “Line Description”
- `line_date_deadline` Date “Date Deadline”
- `responsible_user_id` Many2one → `res.users` “Responsible User”
- `role_id` Many2one → `res.role` “Role”

## `mail.blacklist.remove` (defines)

Remove email from blacklist wizard

- `email` Char (required, readonly)
- `reason` Char

Public methods: `action_unblacklist_apply`

## `mail.compose.message` (defines)

Email composition wizard

Inherits: `mail.composer.mixin`

- `subject` Char “Subject” (store, compute=_compute_subject)
- `subject_placeholder` Char “Subject Placeholder” (compute=_compute_subject_placeholder)
- `body` Html “Contents” (store, compute=_compute_body)
- `parent_id` Many2one → `mail.message`
- `template_id` Many2one → `mail.template`
- `attachment_ids` Many2many → `ir.attachment` “Attachments” (store, compute=_compute_attachment_ids)
- `attachment_links` Html “Attachment links” (compute=_compute_attachment_links)
- `attachment_links_info` Char (compute=_compute_attachment_links)
- `email_layout_xmlid` Char “Email Notification Layout” (store, compute=_compute_email_layout_xmlid)
- `email_notification_allow_header` Boolean
- `email_add_signature` Boolean “Add signature” (store, compute=_compute_email_add_signature)
- `email_from` Char “From” (store, compute=_compute_authorship)
- `author_id` Many2one → `res.partner` “Author” (store, compute=_compute_authorship)
- `composition_mode` Selection “Composition mode”
- `composition_batch` Boolean “Batch composition” (compute=_compute_composition_batch)
- `composition_comment_option` Selection “Comment Options”
- `model` Char “Related Document Model” (store, compute=_compute_model)
- `model_is_thread` Boolean “Thread-Enabled” (compute=_compute_model_is_thread)
- `res_ids` Text “Related Document IDs” (store, compute=_compute_res_ids)
- `res_domain` Text “Active domain”
- `res_domain_user_id` Many2one → `res.users` “Responsible”
- `record_alias_domain_id` Many2one → `mail.alias.domain` (store, compute=_compute_record_environment)
- `record_company_id` Many2one → `res.company` (store, compute=_compute_record_environment)
- `message_type` Selection (required)
- `subtype_id` Many2one → `mail.message.subtype` (store, compute=_compute_subtype_id)
- `subtype_is_log` Boolean “Is a log” (compute=_compute_subtype_is_log)
- `mail_activity_type_id` Many2one → `mail.activity.type`
- `reply_to` Char “Reply To” (store, compute=_compute_reply_to)
- `reply_to_force_new` Boolean “Considers answers as new thread” (store, compute=_compute_reply_to_force_new)
- `reply_to_mode` Selection “Replies” (compute=_compute_reply_to_mode)
- `partner_cc_allowed` Boolean “Cc Usage Allowed” (store, compute=_compute_partner_cc_allowed)
- `partner_ids` Many2many → `res.partner` (store, compute=_compute_recipient_partners)
- `partner_cc_ids` Many2many → `res.partner` (store, compute=_compute_recipient_partners)
- `partner_ids_all_have_email` Boolean (compute=_compute_partner_ids_all_have_email)
- `notified_bcc_contains_share` Boolean “Is an external partner follower of the document?” (compute=_compute_notified_bcc_contains_share)
- `auto_delete` Boolean “Delete Emails” (store, compute=_compute_auto_delete)
- `auto_delete_keep_log` Boolean “Keep Message Copy” (store, compute=_compute_auto_delete_keep_log)
- `force_send` Boolean “Send mailing or notifications directly” (store, compute=_compute_force_send)
- `mail_server_id` Many2one → `ir.mail_server` “Outgoing mail server” (store, compute=_compute_mail_server_id)
- `notify_author` Boolean (store, compute=_compute_notify_author)
- `notify_author_mention` Boolean (store, compute=_compute_notify_author_mention)
- `notify_skip_followers` Boolean (store, compute=_compute_notify_skip_followers)
- `scheduled_date` Char “Scheduled Date” (store, compute=_compute_scheduled_date)
- `use_exclusion_list` Boolean “Use Exclusion List”
- `template_name` Char “Template Name”

Public methods: `action_schedule_message`, `action_send_mail`, `action_update_message`, `cancel_save_template`, `create_mail_template`, `default_get`, `open_template_creation_wizard`

Extension points: `_action_schedule_message`, `_action_send_mail`, `_action_send_mail_comment`, `_action_send_mail_mass_mail`, `_check_res_domain`, `_check_res_ids`, `_get_blacklist_record_ids`, `_get_body_with_full_composer_marker`, `_get_done_emails`, `_get_optout_emails`, `_get_recipients_data`, `_prepare_mail_values`, `_prepare_mail_values_dynamic`, `_prepare_mail_values_rendered`, `_prepare_mail_values_static`, `_prepare_schedule_message_post_values`

## `mail.followers.edit` (defines)

Followers edit wizard

- `res_model` Char “Related Document Model” (required)
- `res_ids` Char “Related Document IDs”
- `operation` Selection “Operation” (required)
- `partner_ids` Many2many → `res.partner` “Followers” (required)
- `message` Html “Message”
- `notify` Boolean “Notify Recipients”

Public methods: `edit_followers`

Extension points: `_prepare_message_values`

## `mail.template.preview` (defines)

Email Template Preview

- `mail_template_id` Many2one → `mail.template` “Related Mail Template” (required)
- `model_id` Many2one → `ir.model` “Targeted model” (related=mail_template_id.model_id)
- `resource_ref` Reference “Record” (store, compute=_compute_resource_ref)
- `lang` Selection “Template Preview Language”
- `no_record` Boolean “No Record” (compute=_compute_no_record)
- `error_msg` Char “Error Message” (compute=_compute_mail_template_fields)
- `subject` Char “Subject” (compute=_compute_mail_template_fields)
- `email_from` Char “From” (compute=_compute_mail_template_fields)
- `email_to` Char “To” (compute=_compute_mail_template_fields)
- `email_cc` Char “Cc” (compute=_compute_mail_template_fields)
- `reply_to` Char “Reply-To” (compute=_compute_mail_template_fields)
- `scheduled_date` Char “Scheduled Date” (compute=_compute_mail_template_fields)
- `body_html` Html “Body” (compute=_compute_mail_template_fields)
- `attachment_ids` Many2many → `ir.attachment` “Attachments” (compute=_compute_mail_template_fields)
- `has_attachments` Boolean (compute=_compute_has_attachments)
- `has_several_languages_installed` Boolean (compute=_compute_has_several_languages_installed)
- `recipient_names` Char “Recipient Names” (compute=_compute_mail_template_fields)
- `recipient_cc_names` Char “Recipient Cc Names” (compute=_compute_mail_template_fields)
- `partner_ids` Many2many → `res.partner` “Recipients To” (compute=_compute_mail_template_fields)
- `partner_cc_ids` Many2many → `res.partner` “Recipients Cc” (compute=_compute_mail_template_fields)

## `mail.template.reset` (defines)

Mail Template Reset

- `template_ids` Many2many → `mail.template`

Public methods: `reset_template`
