# mail — Discuss

Depends on: base, base_setup, bus, web_tour, html_editor.

## `bus.listener.mixin` (extends)


## `bus.presence` (extends)

- `guest_id` Many2one → `mail.guest`

Public methods: `init`

Extension points: `_get_bus_target`, `_get_identity_data`, `_get_identity_field_name`

## `bus.listener.mixin` (extends)


## `discuss.channel` (defines)

Discussion Channel

Inherits: `mail.thread`, `bus.listener.mixin`

- `name` Char “Name” (required)
- `active` Boolean
- `channel_type` Selection “Channel Type” (required, readonly)
- `is_editable` Boolean “Is Editable” (compute=_compute_is_editable)
- `default_display_mode` Selection “Default Display Mode”
- `description` Text “Description”
- `image_128` Image “Image”
- `avatar_128` Image “Avatar” (compute=_compute_avatar_128)
- `avatar_cache_key` Char (compute=_compute_avatar_cache_key)
- `channel_partner_ids` Many2many → `res.partner` “Partners” (compute=_compute_channel_partner_ids)
- `channel_member_ids` One2many → `discuss.channel.member` “Members”
- `parent_channel_id` Many2one → `discuss.channel` (readonly, index)
- `sub_channel_ids` One2many → `discuss.channel` “Sub Channels” (readonly)
- `from_message_id` Many2one → `mail.message` (readonly)
- `pinned_message_ids` One2many → `mail.message` “Pinned Messages”
- `sfu_channel_uuid` Char
- `sfu_server_url` Char
- `rtc_session_ids` One2many → `discuss.channel.rtc.session`
- `is_member` Boolean “Is Member” (compute=_compute_is_member)
- `member_count` Integer “Member Count” (compute=_compute_member_count)
- `last_interest_dt` Datetime “Last Interest” (index)
- `group_ids` Many2many → `res.groups` “Auto Subscription”
- `uuid` Char “UUID”
- `group_public_id` Many2one → `res.groups` “Authorized Group” (store, compute=_compute_group_public_id)
- `invitation_url` Char “Invitation URL” (compute=_compute_invitation_url)
- `allow_public_upload` Boolean

Public methods: `action_unfollow`, `add_members`, `channel_change_description`, `channel_create`, `channel_fetched`, `channel_get`, `channel_join`, `channel_pin`, `channel_rename`, `channel_set_custom_name`, `create`, `create_group`, `execute_command_help`, `execute_command_leave`, `execute_command_who`, `get_mention_suggestions`, `init`, `message_post`, `set_message_pin`, `write`

Extension points: `_action_unfollow`, `_check_can_update_message_content`, `_create_attachments_for_post`, `_create_sub_channel`, `_get_access_action`, `_get_allowed_message_post_params`, `_get_channels_as_member`, `_get_last_messages`, `_get_notify_valid_parameters`

## `discuss.channel.member` (defines)

Channel Member

Inherits: `bus.listener.mixin`

- `partner_id` Many2one → `res.partner` (index)
- `guest_id` Many2one → `mail.guest` (index)
- `is_self` Boolean (compute=_compute_is_self)
- `channel_id` Many2one → `discuss.channel` (required)
- `custom_channel_name` Char “Custom channel name”
- `fetched_message_id` Many2one → `mail.message` “Last Fetched”
- `seen_message_id` Many2one → `mail.message` “Last Seen”
- `new_message_separator` Integer (required)
- `message_unread_counter` Integer “Unread Messages Counter” (compute=_compute_message_unread)
- `fold_state` Selection “Conversation Fold State”
- `custom_notifications` Selection
- `mute_until_dt` Datetime “Mute notifications until”
- `is_pinned` Boolean “Is pinned on the interface” (compute=_compute_is_pinned)
- `unpin_dt` Datetime “Unpin date” (index)
- `last_interest_dt` Datetime “Last Interest” (index)
- `last_seen_dt` Datetime “Last seen date”
- `rtc_session_ids` One2many → `discuss.channel.rtc.session` “RTC Sessions”
- `rtc_inviting_session_id` Many2one → `discuss.channel.rtc.session` “Ringing session”

Public methods: `create`, `init`, `set_custom_notifications`, `unlink`, `write`

Extension points: `_get_html_link`, `_get_rtc_invite_members_domain`, `_get_rtc_server_info`, `_get_store_partner_fields`

## `discuss.channel.rtc.session` (defines)

Mail RTC session

Inherits: `bus.listener.mixin`

- `channel_member_id` Many2one → `discuss.channel.member` (required)
- `channel_id` Many2one → `discuss.channel` (readonly, store, related=channel_member_id.channel_id)
- `partner_id` Many2one → `res.partner` “Partner” (related=channel_member_id.partner_id)
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


Extension points: `_get_missed_presences_bus_target`, `_get_missed_presences_identity_domains`

## `mail.guest` (defines)

Guest

Inherits: `avatar.mixin`, `bus.listener.mixin`

- `name` Char “Name” (required)
- `access_token` Char “Access Token” (required, readonly)
- `country_id` Many2one → `res.country` “Country”
- `lang` Selection “Language”
- `timezone` Selection “Timezone”
- `channel_ids` Many2many → `discuss.channel` “Channels”
- `im_status` Char “IM Status” (compute=_compute_im_status)

Extension points: `_get_guest_from_context`, `_get_guest_from_token`, `_get_timezone_from_request`

## `mail.message` (extends)


## `res.groups` (extends)


Public methods: `write`

## `res.partner` (extends)

- `channel_ids` Many2many → `discuss.channel` “Channels”

Public methods: `get_mention_suggestions_from_channel`, `search_for_channel_invite`

## `res.users` (extends)


Public methods: `create`, `unlink`, `write`

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
- `user` Char “Username”
- `password` Char
- `object_id` Many2one → `ir.model` “Create a New Record”
- `priority` Integer “Server Priority”
- `message_ids` One2many → `mail.mail` “Messages” (readonly)
- `configuration` Text “Configuration” (readonly)
- `script` Char (readonly)

Public methods: `button_confirm_login`, `connect`, `create`, `fetch_mail`, `onchange_server_type`, `set_draft`, `unlink`, `write`

Extension points: `_get_connection_type`

## `ir.actions.act_window.view` (extends)

- `view_mode` Selection

## `ir.actions.server` (extends)

Server Action

- `state` Selection
- `partner_ids` Many2many → `res.partner` (store, compute=_compute_partner_ids)
- `template_id` Many2one → `mail.template` (store, compute=_compute_template_id)
- `mail_post_autofollow` Boolean “Subscribe Recipients” (store, compute=_compute_mail_post_autofollow)
- `mail_post_method` Selection “Send Email As” (store, compute=_compute_mail_post_method)
- `activity_type_id` Many2one → `mail.activity.type` “Activity Type” (store, compute=_compute_activity_type_id)
- `activity_summary` Char “Title” (store, compute=_compute_activity_info)
- `activity_note` Html “Note” (store, compute=_compute_activity_info)
- `activity_date_deadline_range` Integer “Due Date In” (store, compute=_compute_activity_info)
- `activity_date_deadline_range_type` Selection “Due type” (store, compute=_compute_activity_info)
- `activity_user_type` Selection “User Type” (store, compute=_compute_activity_info)
- `activity_user_id` Many2one → `res.users` “Responsible” (store, compute=_compute_activity_info)
- `activity_user_field_name` Char “User Field” (store, compute=_compute_activity_info)

Extension points: `_check_activity_date_deadline_range`, `_check_mail_model_coherency`, `_check_mail_template_model`, `_get_eval_context`

## `ir.attachment` (extends)


Public methods: `register_as_main_attachment`

Extension points: `_check_attachments_access`, `_post_add_create`

## `ir.config_parameter` (extends)


Public methods: `create`, `set_param`, `write`

## `ir.cron` (extends)


## `ir.http` (extends)


Public methods: `session_info`

## `ir.mail_server` (extends)

- `mail_template_ids` One2many → `mail.template` “Mail template using this mail server” (readonly)

Extension points: `_get_default_bounce_address`, `_get_default_from_address`, `_get_test_email_from`

## `ir.model` (extends)

- `is_mail_thread` Boolean “Has Mail Thread”
- `is_mail_activity` Boolean “Has Mail Activity”
- `is_mail_blacklist` Boolean “Has Mail Blacklist”

Public methods: `unlink`, `write`

Extension points: `_get_definitions`, `_get_model_definitions`

## `ir.model.fields` (extends)

- `tracking` Integer “Enable Ordered Tracking”

Public methods: `unlink`

## `ir.qweb` (extends)


Extension points: `_get_template_cache_keys`

## `ir.ui.menu` (extends)


Extension points: `_get_best_backend_root_menu_id_for_model`

## `ir.ui.view` (extends)

- `type` Selection

Extension points: `_get_view_info`

## `mail.activity` (defines)

Activity

- `res_model_id` Many2one → `ir.model` (required, index)
- `res_model` Char “Related Document Model” (readonly, store, index, related=res_model_id.model)
- `res_id` Many2oneReference “Related Document ID” (index)
- `res_name` Char “Document Name” (readonly, store, compute=_compute_res_name)
- `activity_type_id` Many2one → `mail.activity.type` “Activity Type”
- `activity_category` Selection (readonly, related=activity_type_id.category)
- `activity_decoration` Selection (readonly, related=activity_type_id.decoration_type)
- `icon` Char “Icon” (readonly, related=activity_type_id.icon)
- `summary` Char “Summary”
- `note` Html “Note”
- `date_deadline` Date “Due Date” (required, index)
- `date_done` Date “Done Date” (store, compute=_compute_date_done)
- `automated` Boolean “Automated activity” (readonly)
- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `user_id` Many2one → `res.users` (required, index)
- `user_tz` Selection “Timezone” (store, related=user_id.tz)
- `request_partner_id` Many2one → `res.partner` “Requesting Partner”
- `state` Selection (compute=_compute_state)
- `recommended_activity_type_id` Many2one → `mail.activity.type` “Recommended Activity Type”
- `previous_activity_type_id` Many2one → `mail.activity.type` “Previous Activity Type” (readonly)
- `has_recommended_activities` Boolean “Next activities available” (compute=_compute_has_recommended_activities)
- `mail_template_ids` Many2many (readonly, related=activity_type_id.mail_template_ids)
- `chaining_type` Selection (readonly, related=activity_type_id.chaining_type)
- `can_write` Boolean (compute=_compute_can_write)
- `active` Boolean

Public methods: `action_cancel`, `action_close_dialog`, `action_done`, `action_done_redirect_to_other`, `action_done_schedule_next`, `action_feedback`, `action_feedback_schedule_next`, `action_notify`, `action_open_document`, `action_snooze`, `activity_format`, `create`, `default_get`, `get_activity_data`, `unlink`, `write`

Extension points: `_action_done`, `_check_access`, `_prepare_next_activity_values`

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

Public methods: `activity_feedback`, `activity_reschedule`, `activity_schedule`, `activity_search`, `activity_send_mail`, `activity_unlink`, `toggle_active`, `unlink`, `write`

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

Public methods: `copy_data`

Extension points: `_check_res_model_compatibility_with_templates`, `_get_model_selection`

## `mail.activity.plan.template` (defines)

Activity plan template

- `plan_id` Many2one → `mail.activity.plan` “Plan” (required)
- `res_model` Selection (related=plan_id.res_model)
- `company_id` Many2one (related=plan_id.company_id)
- `sequence` Integer
- `activity_type_id` Many2one → `mail.activity.type` (required)
- `delay_count` Integer “Interval”
- `delay_unit` Selection “Delay units” (required)
- `delay_from` Selection “Trigger” (required)
- `icon` Char “Icon” (readonly, related=activity_type_id.icon)
- `summary` Char “Summary” (store, compute=_compute_summary)
- `responsible_type` Selection “Assignment” (required, store, compute=_compute_responsible_type)
- `responsible_id` Many2one → `res.users` (store, compute=_compute_responsible_id)
- `note` Html “Note” (store, compute=_compute_note)

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
- `triggered_next_type_id` Many2one → `mail.activity.type` “Trigger” (store, compute=_compute_triggered_next_type_id)
- `chaining_type` Selection “Chaining Type” (required)
- `suggested_next_type_ids` Many2many → `mail.activity.type` “Suggest” (store, compute=_compute_suggested_next_type_ids)
- `previous_type_ids` Many2many → `mail.activity.type` “Preceding Activities”
- `category` Selection “Action”
- `mail_template_ids` Many2many → `mail.template` “Email templates”
- `default_user_id` Many2one → `res.users` “Default User”
- `default_note` Html “Default Note”
- `keep_done` Boolean “Keep Done”
- `initial_res_model` Selection “Initial model” (compute=_compute_initial_res_model)
- `res_model_change` Boolean “Model has change”

Public methods: `action_archive`, `write`

Extension points: `_check_activity_type_res_model`, `_get_date_deadline`, `_get_model_info_by_xmlid`, `_get_model_selection`

## `mail.alias` (defines)

Email Aliases

- `alias_name` Char “Alias Name”
- `alias_full_name` Char “Alias Email” (store, compute=_compute_alias_full_name)
- `display_name` Char “Display Name” (compute=_compute_display_name)
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

Public methods: `create`, `init`, `open_document`, `open_parent_document`, `write`

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

Extension points: `_check_bounce_catchall_uniqueness`, `_check_name`

## `mail.alias.mixin` (defines)

Email Aliases Mixin

Inherits: `mail.alias.mixin.optional`

- `alias_id` Many2one (required)
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

## `mail.canned.response` (defines)

Canned Response

- `source` Char “Shortcut” (required)
- `substitution` Text “Substitution” (required)
- `description` Char “Description”
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

Document Followers

- `res_model` Char “Related Document Model Name” (required, index)
- `res_id` Many2oneReference “Related Document ID” (index)
- `partner_id` Many2one → `res.partner` “Related Partner” (required, index)
- `subtype_ids` Many2many → `mail.message.subtype` “Subtype”
- `name` Char “Name” (related=partner_id.name)
- `email` Char “Email” (related=partner_id.email)
- `is_active` Boolean “Is Active” (related=partner_id.active)

Public methods: `create`, `unlink`, `write`

Extension points: `_get_mail_recipients_follower_status`, `_get_recipient_data`, `_get_subscription_data`

## `mail.gateway.allowed` (defines)

Mail Gateway Allowed

- `email` Char “Email Address” (required)
- `email_normalized` Char “Normalized Email” (store, index, compute=_compute_email_normalized)

Public methods: `get_empty_list_help`

## `mail.ice.server` (defines)

ICE server

- `server_type` Selection “Type” (required)
- `uri` Char “URI” (required)
- `username` Char
- `credential` Char

Extension points: `_get_ice_servers`, `_get_local_ice_servers`

## `mail.link.preview` (defines)

Store link preview data

Inherits: `bus.listener.mixin`

- `message_id` Many2one → `mail.message` “Message” (index)
- `is_hidden` Boolean
- `source_url` Char “URL” (required)
- `og_type` Char “Type”
- `og_title` Char “Title”
- `og_site_name` Char “Site name”
- `og_image` Char “Image”
- `og_description` Text “Description”
- `og_mimetype` Char “MIME type”
- `image_mimetype` Char “Image MIME type”
- `create_date` Datetime (index)

Extension points: `_create_from_message_and_notify`

## `mail.mail` (defines)

Outgoing Mails

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
- `state` Selection (readonly)
- `failure_type` Selection “Failure type”
- `failure_reason` Text “Failure Reason” (readonly)
- `auto_delete` Boolean “Auto Delete”
- `scheduled_date` Datetime “Scheduled Send Date”
- `fetchmail_server_id` Many2one → `fetchmail.server` (readonly)

Public methods: `action_open_document`, `action_retry`, `cancel`, `create`, `default_get`, `fields_get`, `mark_outgoing`, `process_email_queue`, `send`, `send_after_commit`, `unlink`, `write`

Extension points: `_prepare_outgoing_body`, `_prepare_outgoing_list`

## `mail.message` (defines)

Message

Inherits: `bus.listener.mixin`

- `subject` Char “Subject”
- `date` Datetime “Date”
- `body` Html “Contents”
- `preview` Char “Preview” (compute=_compute_preview)
- `link_preview_ids` One2many → `mail.link.preview` “Link Previews”
- `reaction_ids` One2many → `mail.message.reaction` “Reactions”
- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `parent_id` Many2one → `mail.message`
- `child_ids` One2many → `mail.message`
- `model` Char “Related Document Model”
- `res_id` Many2oneReference “Related Document ID”
- `record_name` Char “Message Record Name”
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
- `partner_ids` Many2many → `res.partner` “Recipients”
- `notified_partner_ids` Many2many → `res.partner` “Partners with Need Action”
- `needaction` Boolean “Need Action” (compute=_compute_needaction)
- `has_error` Boolean “Has error” (compute=_compute_has_error)
- `notification_ids` One2many → `mail.notification`
- `starred_partner_ids` Many2many → `res.partner` “Favorited By”
- `pinned_at` Datetime “Pinned”
- `starred` Boolean “Starred” (compute=_compute_starred)
- `tracking_value_ids` One2many → `mail.tracking.value` “Tracking values”
- `reply_to_force_new` Boolean “No threading for answers”
- `message_id` Char “Message-Id” (readonly)
- `reply_to` Char “Reply-To”
- `mail_server_id` Many2one → `ir.mail_server`
- `email_layout_xmlid` Char “Layout”
- `email_add_signature` Boolean
- `mail_ids` One2many → `mail.mail` “Mails”

Public methods: `action_open_document`, `copy_data`, `create`, `default_get`, `export_data`, `fetch`, `init`, `is_thread_message`, `mark_all_as_read`, `read`, `set_message_done`, `toggle_message_starred`, `unlink`, `unstar_all`, `write`

Extension points: `_check_access`, `_get_forbidden_access`, `_get_message_id`, `_get_record_name`, `_get_reply_to`, `_get_search_domain_share`, `_get_with_access`

## `mail.message.reaction` (defines)

Message Reaction

- `message_id` Many2one → `mail.message` “Message” (required, readonly)
- `content` Char “Content” (required, readonly)
- `partner_id` Many2one → `res.partner` “Reacting Partner” (readonly)
- `guest_id` Many2one → `mail.guest` “Reacting Guest” (readonly)

Public methods: `init`

## `mail.message.schedule` (defines)

Scheduled Messages

- `mail_message_id` Many2one → `mail.message` “Message” (required)
- `notification_parameters` Text “Notification Parameter”
- `scheduled_datetime` Datetime “Scheduled Send Date” (required)

Public methods: `create`, `force_send`

## `mail.message.subtype` (defines)

Message subtypes

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

Public methods: `create`, `default_subtypes`, `unlink`, `write`

Extension points: `_get_auto_subscription_subtypes`

## `mail.message.translation` (defines)

Message Translation

- `message_id` Many2one → `mail.message` (required)
- `source_lang` Char “Source Language” (required)
- `target_lang` Char “Target Language” (required)
- `body` Html “Translation Body” (required)
- `create_date` Datetime (index)

Public methods: `init`

## `mail.notification` (defines)

Message Notifications

- `author_id` Many2one → `res.partner`
- `mail_message_id` Many2one → `mail.message` (required, index)
- `mail_mail_id` Many2one → `mail.mail` (index)
- `res_partner_id` Many2one → `res.partner` (index)
- `notification_type` Selection “Notification Type” (required, index)
- `notification_status` Selection “Status” (index)
- `is_read` Boolean “Is Read” (index)
- `read_date` Datetime “Read Date”
- `failure_type` Selection “Failure type”
- `failure_reason` Text “Failure reason”

Public methods: `create`, `format_failure_reason`, `init`, `write`

## `mail.push` (defines)

Push Notifications

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
- `model` Char “Related Document Model” (required)
- `res_id` Many2oneReference “Related Document Id” (required)
- `author_id` Many2one → `res.partner` (required)
- `partner_ids` Many2many → `res.partner` “Recipients”
- `is_note` Boolean “Is a note”
- `notification_parameters` Text “Notification parameters”

Public methods: `create`, `open_edit_form`, `post_message`, `unlink`, `write`

Extension points: `_check_model`, `_check_scheduled_date`, `_post_message`, `_post_messages_cron`

## `mail.template` (defines)

Email Templates

Inherits: `mail.render.mixin`, `template.reset.mixin`

- `name` Char “Name”
- `description` Text “Template Description”
- `active` Boolean
- `template_category` Selection (compute=_compute_template_category)
- `model_id` Many2one → `ir.model`
- `model` Char “Related Document Model” (readonly, store, index, related=model_id.model)
- `subject` Char “Subject”
- `email_from` Char “From”
- `user_id` Many2one → `res.users` “User”
- `use_default_to` Boolean “Default recipients”
- `email_to` Char “To (Emails)”
- `partner_to` Char “To (Partners)”
- `email_cc` Char “Cc”
- `reply_to` Char “Reply To”
- `body_html` Html “Body”
- `attachment_ids` Many2many → `ir.attachment`
- `report_template_ids` Many2many → `ir.actions.report` “Dynamic Reports”
- `email_layout_xmlid` Char “Email Notification Layout”
- `mail_server_id` Many2one → `ir.mail_server`
- `scheduled_date` Char “Scheduled Date”
- `auto_delete` Boolean “Auto Delete”
- `ref_ir_act_window` Many2one → `ir.actions.act_window` (readonly)
- `can_write` Boolean (compute=_compute_can_write)
- `is_template_editor` Boolean (compute=_compute_is_template_editor)

Public methods: `cancel_unlink`, `copy`, `copy_data`, `create`, `create_action`, `default_get`, `open_delete_confirmation_modal`, `send_mail`, `send_mail_batch`, `unlink`, `unlink_action`, `write`

Extension points: `_check_abstract_models`

## `mail.thread` (defines)

Email Thread

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

Public methods: `copy_data`, `create`, `get_empty_list_help`, `get_views`, `message_change_thread`, `message_get_followers`, `message_mail_with_source`, `message_new`, `message_notify`, `message_parse`, `message_post`, `message_post_with_source`, `message_process`, `message_route`, `message_subscribe`, `message_unsubscribe`, `message_update`, `notify_cancel_by_type`, `unlink`, `write`

Extension points: `_check_can_update_message_content`, `_create_attachments_for_post`, `_get_action_link_params`, `_get_allowed_message_post_params`, `_get_allowed_message_update_params`, `_get_bounced_message_data`, `_get_customer_information`, `_get_mail_message_access`, `_get_mail_thread_data_attachments`, `_get_message_create_ignore_field_names`, `_get_message_create_valid_field_names`, `_get_model_description`, `_get_notify_valid_parameters`, `_get_parent_message`, `_get_source_from_ref`, `_get_thread_with_access`

## `mail.thread.blacklist` (defines)

Mail Blacklist mixin

Inherits: `mail.thread`

- `email_normalized` Char “Normalized Email” (store, compute=_compute_email_normalized)
- `is_blacklisted` Boolean “Blacklist” (compute=_compute_is_blacklisted)
- `message_bounce` Integer “Bounce”

Public methods: `mail_action_blacklist_remove`

## `mail.thread.cc` (defines)

Email CC management

Inherits: `mail.thread`

- `email_cc` Char “Email cc”

Public methods: `message_new`, `message_update`

## `mail.thread.main.attachment` (defines)

Mail Main Attachment management

Inherits: `mail.thread`

- `message_main_attachment_id` Many2one → `ir.attachment` “Main Attachment”

## `mail.tracking.duration.mixin` (defines)

Mixin to compute the time a record has spent in each value a many2one field can take

- `duration_tracking` Json “Status time” (compute=_compute_duration_tracking)

Extension points: `_get_duration_from_tracking`

## `mail.tracking.value` (defines)

Mail Tracking Value

- `field_id` Many2one → `ir.model.fields` (readonly, index)
- `field_info` Json “Removed field information”
- `old_value_integer` Integer “Old Value Integer” (readonly)
- `old_value_float` Float “Old Value Float” (readonly)
- `old_value_char` Char “Old Value Char” (readonly)
- `old_value_text` Text “Old Value Text” (readonly)
- `old_value_datetime` Datetime “Old Value DateTime” (readonly)
- `new_value_integer` Integer “New Value Integer” (readonly)
- `new_value_float` Float “New Value Float” (readonly)
- `new_value_char` Char “New Value Char” (readonly)
- `new_value_text` Text “New Value Text” (readonly)
- `new_value_datetime` Datetime “New Value Datetime” (readonly)
- `currency_id` Many2one → `res.currency` (readonly)
- `mail_message_id` Many2one → `mail.message` (required, index)

Extension points: `_create_tracking_values`

## `base` (extends)


Public methods: `mail_allowed_qweb_expressions`

Extension points: `_get_backend_root_menu_ids`, `_get_default_activity_view`, `_get_html_link`

## `res.company` (extends)

- `alias_domain_id` Many2one → `mail.alias.domain` “Email Domain”
- `alias_domain_name` Char “Alias Domain Name” (readonly, store, related=alias_domain_id.name)
- `bounce_email` Char “Bounce Email” (compute=_compute_bounce)
- `bounce_formatted` Char “Bounce” (compute=_compute_bounce)
- `catchall_email` Char “Catchall Email” (compute=_compute_catchall)
- `catchall_formatted` Char “Catchall” (compute=_compute_catchall)
- `default_from_email` Char “Default From” (readonly, related=alias_domain_id.default_from_email)
- `email_formatted` Char “Formatted Email” (compute=_compute_email_formatted)
- `email_primary_color` Char “Email Header Color” (store, compute=_compute_email_primary_color)
- `email_secondary_color` Char “Email Button Color” (store, compute=_compute_email_secondary_color)

## `res.config.settings` (extends)

- `external_email_server_default` Boolean “Use Custom Email Servers”
- `fail_counter` Integer “Fail Mail” (compute=_compute_fail_counter)
- `alias_domain_id` Many2one → `mail.alias.domain` (related=company_id.alias_domain_id)
- `module_google_gmail` Boolean “Support Gmail Authentication”
- `module_microsoft_outlook` Boolean “Support Outlook Authentication”
- `restrict_template_rendering` Boolean “Restrict Template Rendering”
- `use_twilio_rtc_servers` Boolean “Use Twilio ICE servers”
- `twilio_account_sid` Char “Twilio Account SID”
- `twilio_account_token` Char “Twilio Account Auth Token”
- `sfu_server_url` Char “SFU Server URL”
- `sfu_server_key` Char “SFU Server key”
- `email_primary_color` Char (related=company_id.email_primary_color)
- `email_secondary_color` Char (related=company_id.email_secondary_color)
- `tenor_api_key` Char “Klipy API key”
- `tenor_content_filter` Selection “Klipy content filter”
- `tenor_gif_limit` Integer “Klipy GIF limits”
- `google_translate_api_key` Char “Message Translation API Key”

Public methods: `open_email_layout`, `open_mail_templates`

## `res.partner` (extends)

Inherits: `mail.activity.mixin`, `mail.thread.blacklist`

- `name` Char
- `email` Char
- `phone` Char
- `parent_id` Many2one
- `user_id` Many2one
- `vat` Char
- `contact_address_inline` Char “Inlined Complete Address” (compute=_compute_contact_address_inline)
- `starred_message_ids` Many2many → `mail.message`

Public methods: `find_or_create`, `get_mention_suggestions`, `im_search`

Extension points: `_get_current_persona`, `_get_mention_suggestions_domain`, `_get_needaction_count`, `_get_view_cache_key`

## `res.users` (extends)

- `notification_type` Selection (required, store, compute=_compute_notification_type)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`, `action_archive`, `create`, `write`

Extension points: `_get_activity_groups`, `_get_portal_access_update_body`

## `res.users.settings` (extends)

- `is_discuss_sidebar_category_channel_open` Boolean “Is discuss sidebar category channel open?”
- `is_discuss_sidebar_category_chat_open` Boolean “Is discuss sidebar category chat open?”
- `push_to_talk_key` Char “Push-To-Talk shortcut”
- `use_push_to_talk` Boolean “Use the push to talk feature”
- `voice_active_duration` Integer “Duration of voice activity in ms”
- `volume_settings_ids` One2many → `res.users.settings.volumes` “Volumes of other partners”
- `channel_notifications` Selection
- `mute_until_dt` Datetime “Mute notifications until” (index)

Public methods: `set_custom_notifications`, `set_res_users_settings`, `set_volume_setting`

## `res.users.settings.volumes` (defines)

User Settings Volumes

- `user_setting_id` Many2one → `res.users.settings` (required, index)
- `partner_id` Many2one → `res.partner` (index)
- `guest_id` Many2one → `res.partner` (index)
- `volume` Float

Public methods: `init`

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


## `mail.activity.schedule` (defines)

Activity schedule plan Wizard

- `res_model_id` Many2one → `ir.model` “Applies to” (required, store, compute=_compute_res_model_id)
- `res_model` Char “Model” (required, readonly)
- `res_ids` Text “Document IDs” (readonly, store, compute=_compute_res_ids)
- `is_batch_mode` Boolean “Use in batch” (compute=_compute_is_batch_mode)
- `company_id` Many2one → `res.company` (required, compute=_compute_company_id)
- `error` Html (compute=_compute_error)
- `has_error` Boolean (compute=_compute_error)
- `plan_available_ids` Many2many → `mail.activity.plan` (store, compute=_compute_plan_available_ids)
- `plan_id` Many2one → `mail.activity.plan` (store, compute=_compute_plan_id)
- `plan_has_user_on_demand` Boolean (related=plan_id.has_user_on_demand)
- `plan_summary` Html (compute=_compute_plan_summary)
- `plan_on_demand_user_id` Many2one → `res.users`
- `plan_date` Date “Plan Date” (store, compute=_compute_plan_date)
- `activity_type_id` Many2one → `mail.activity.type` “Activity Type” (store, compute=_compute_activity_type_id)
- `activity_category` Selection (readonly, related=activity_type_id.category)
- `date_deadline` Date “Due Date” (store, compute=_compute_date_deadline)
- `summary` Char “Summary” (store, compute=_compute_summary)
- `note` Html “Note” (store, compute=_compute_note)
- `activity_user_id` Many2one → `res.users` (store, compute=_compute_activity_user_id)
- `chaining_type` Selection (readonly, related=activity_type_id.chaining_type)

Public methods: `action_schedule_activities`, `action_schedule_activities_done`, `action_schedule_activities_done_and_schedule`, `action_schedule_plan`, `default_get`

Extension points: `_action_schedule_activities`, `_check_consistency`, `_check_plan_templates_error`, `_check_res_ids`, `_get_applied_on_records`, `_get_plan_available_base_domain`, `_get_summary_lines`

## `mail.blacklist.remove` (defines)

Remove email from blacklist wizard

- `email` Char (required, readonly)
- `reason` Char

Public methods: `action_unblacklist_apply`

## `mail.compose.message` (defines)

Email composition wizard

Inherits: `mail.composer.mixin`

- `subject` Char “Subject” (store, compute=_compute_subject)
- `body` Html “Contents” (store, compute=_compute_body)
- `parent_id` Many2one → `mail.message`
- `template_id` Many2one → `mail.template`
- `attachment_ids` Many2many → `ir.attachment` “Attachments” (store, compute=_compute_attachment_ids)
- `email_layout_xmlid` Char “Email Notification Layout” (store, compute=_compute_email_layout_xmlid)
- `email_add_signature` Boolean “Add signature” (store, compute=_compute_email_add_signature)
- `email_from` Char “From” (store, compute=_compute_authorship)
- `author_id` Many2one → `res.partner` “Author” (store, compute=_compute_authorship)
- `composition_mode` Selection “Composition mode”
- `composition_batch` Boolean “Batch composition” (compute=_compute_composition_batch)
- `model` Char “Related Document Model” (store, compute=_compute_model)
- `model_is_thread` Boolean “Thread-Enabled” (compute=_compute_model_is_thread)
- `res_ids` Text “Related Document IDs” (store, compute=_compute_res_ids)
- `res_domain` Text “Active domain”
- `res_domain_user_id` Many2one → `res.users` “Responsible”
- `record_alias_domain_id` Many2one → `mail.alias.domain` (store, compute=_compute_record_environment)
- `record_company_id` Many2one → `res.company` (store, compute=_compute_record_environment)
- `record_name` Char “Record Name” (store, compute=_compute_record_name)
- `message_type` Selection (required)
- `subtype_id` Many2one → `mail.message.subtype` (store, compute=_compute_subtype_id)
- `subtype_is_log` Boolean “Is a log” (compute=_compute_subtype_is_log)
- `mail_activity_type_id` Many2one → `mail.activity.type`
- `reply_to` Char “Reply To” (store, compute=_compute_reply_to)
- `reply_to_force_new` Boolean “Considers answers as new thread” (store, compute=_compute_reply_to_force_new)
- `reply_to_mode` Selection “Replies” (compute=_compute_reply_to_mode)
- `partner_ids` Many2many → `res.partner` (store, compute=_compute_partner_ids)
- `auto_delete` Boolean “Delete Emails” (store, compute=_compute_auto_delete)
- `auto_delete_keep_log` Boolean “Keep Message Copy” (store, compute=_compute_auto_delete_keep_log)
- `force_send` Boolean “Send mailing or notifications directly” (store, compute=_compute_force_send)
- `mail_server_id` Many2one → `ir.mail_server` “Outgoing mail server” (store, compute=_compute_mail_server_id)
- `scheduled_date` Char “Scheduled Date” (store, compute=_compute_scheduled_date)
- `use_exclusion_list` Boolean “Check Exclusion List”
- `template_name` Char “Template Name”

Public methods: `action_schedule_message`, `action_send_mail`, `cancel_save_template`, `create_mail_template`, `default_get`, `open_template_creation_wizard`

Extension points: `_action_send_mail`, `_action_send_mail_comment`, `_action_send_mail_mass_mail`, `_check_res_domain`, `_check_res_ids`, `_get_blacklist_record_ids`, `_get_done_emails`, `_get_optout_emails`, `_get_recipients_data`, `_prepare_mail_values`, `_prepare_mail_values_dynamic`, `_prepare_mail_values_rendered`, `_prepare_mail_values_static`

## `mail.resend.message` (defines)

Email resend wizard

- `mail_message_id` Many2one → `mail.message` (readonly)
- `partner_ids` One2many → `mail.resend.partner` “Recipients”
- `notification_ids` Many2many → `mail.notification` “Notifications” (readonly)
- `can_cancel` Boolean (compute=_compute_can_cancel)
- `can_resend` Boolean (compute=_compute_can_resend)
- `partner_readonly` Boolean (compute=_compute_partner_readonly)

Public methods: `cancel_mail_action`, `default_get`, `resend_mail_action`

## `mail.resend.partner` (defines)

Partner with additional information for mail resend

- `notification_id` Many2one → `mail.notification` “Notification” (required)
- `partner_id` Many2one → `res.partner` “Partner” (related=notification_id.res_partner_id)
- `name` Char “Recipient Name” (related=partner_id.name)
- `email` Char “Email Address” (related=partner_id.email)
- `failure_reason` Text “Failure Reason” (related=notification_id.failure_reason)
- `resend` Boolean “Try Again”
- `resend_wizard_id` Many2one → `mail.resend.message` “Resend wizard”
- `message` Char “Error message”
- `partner_readonly` Boolean “Partner Readonly” (related=resend_wizard_id.partner_readonly)

Public methods: `action_open_record`, `action_open_resend_partner`, `action_resend`

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
- `attachment_ids` Many2many → `ir.attachment` (compute=_compute_mail_template_fields)
- `partner_ids` Many2many → `res.partner` “Recipients” (compute=_compute_mail_template_fields)

## `mail.template.reset` (defines)

Mail Template Reset

- `template_ids` Many2many → `mail.template`

Public methods: `reset_template`

## `mail.wizard.invite` (defines)

Invite wizard

- `res_model` Char “Related Document Model” (required)
- `res_id` Integer “Related Document ID”
- `partner_ids` Many2many → `res.partner` “Recipients”
- `message` Html “Message”
- `notify` Boolean “Notify Recipients”

Public methods: `add_followers`

Extension points: `_prepare_message_values`
