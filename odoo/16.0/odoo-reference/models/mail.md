# mail — Discuss

Depends on: base, base_setup, bus, web_tour.

## `bus.presence` (extends)

- `guest_id` Many2one → `mail.guest`

Public methods: `init`

## `fetchmail.server` (defines)

Incoming Mail Server

- `name` Char “Name” (required)
- `active` Boolean “Active”
- `state` Selection “Status” (readonly, index)
- `server` Char “Server Name” (readonly)
- `port` Integer (readonly)
- `server_type` Selection “Server Type” (required, index)
- `server_type_info` Text “Server Type Info” (compute=_compute_server_type_info)
- `is_ssl` Boolean “SSL/TLS”
- `attach` Boolean “Keep Attachments”
- `original` Boolean “Keep Original”
- `date` Datetime “Last Fetch Date” (readonly)
- `user` Char “Username” (readonly)
- `password` Char (readonly)
- `object_id` Many2one → `ir.model` “Create a New Record”
- `priority` Integer “Server Priority” (readonly)
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
- `partner_ids` Many2many → `res.partner` “Add Followers” (store, compute=_compute_partner_ids)
- `template_id` Many2one → `mail.template` (store, compute=_compute_template_id)
- `mail_post_autofollow` Boolean “Subscribe Recipients” (store, compute=_compute_mail_post_autofollow)
- `mail_post_method` Selection “Send as” (store, compute=_compute_mail_post_method)
- `activity_type_id` Many2one → `mail.activity.type` “Activity” (store, compute=_compute_activity_type_id)
- `activity_summary` Char “Summary” (store, compute=_compute_activity_info)
- `activity_note` Html “Note” (store, compute=_compute_activity_info)
- `activity_date_deadline_range` Integer “Due Date In” (store, compute=_compute_activity_info)
- `activity_date_deadline_range_type` Selection “Due type” (store, compute=_compute_activity_info)
- `activity_user_type` Selection (store, compute=_compute_activity_info)
- `activity_user_id` Many2one → `res.users` “Responsible” (store, compute=_compute_activity_info)
- `activity_user_field_name` Char “User field name” (store, compute=_compute_activity_info)

Extension points: `_check_activity_date_deadline_range`, `_check_model_coherency`, `_get_eval_context`

## `ir.attachment` (extends)


Public methods: `register_as_main_attachment`

Extension points: `_check_attachments_access`, `_post_add_create`

## `ir.config_parameter` (extends)


Public methods: `create`, `set_param`, `write`

## `ir.http` (extends)


Public methods: `session_info`

## `ir.mail_server` (extends)

- `mail_template_ids` One2many → `mail.template` “Mail template using this mail server” (readonly)

## `ir.model` (extends)

- `is_mail_thread` Boolean “Has Mail Thread”
- `is_mail_activity` Boolean “Has Mail Activity”
- `is_mail_blacklist` Boolean “Has Mail Blacklist”

Public methods: `unlink`, `write`

Extension points: `_get_model_definitions`

## `ir.model.fields` (extends)

- `tracking` Integer “Enable Ordered Tracking”

## `ir.qweb` (extends)


Extension points: `_get_template_cache_keys`

## `ir.ui.view` (extends)

- `type` Selection

## `ir.websocket` (extends)


Extension points: `_get_im_status`

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
- `automated` Boolean “Automated activity” (readonly)
- `user_id` Many2one → `res.users` (required, index)
- `request_partner_id` Many2one → `res.partner` “Requesting Partner”
- `state` Selection (compute=_compute_state)
- `recommended_activity_type_id` Many2one → `mail.activity.type` “Recommended Activity Type”
- `previous_activity_type_id` Many2one → `mail.activity.type` “Previous Activity Type” (readonly)
- `has_recommended_activities` Boolean “Next activities available” (compute=_compute_has_recommended_activities)
- `mail_template_ids` Many2many (readonly, related=activity_type_id.mail_template_ids)
- `chaining_type` Selection (readonly, related=activity_type_id.chaining_type)
- `can_write` Boolean (compute=_compute_can_write)

Public methods: `action_close_dialog`, `action_done`, `action_done_schedule_next`, `action_feedback`, `action_feedback_schedule_next`, `action_notify`, `action_open_document`, `activity_format`, `create`, `default_get`, `get_activity_data`, `name_get`, `read`, `unlink`, `write`

Extension points: `_action_done`, `_check_access_assignation`, `_prepare_next_activity_values`

## `mail.activity.mixin` (defines)

Activity Mixin

- `activity_ids` One2many → `mail.activity`
- `activity_state` Selection “Activity State” (compute=_compute_activity_state)
- `activity_user_id` Many2one → `res.users` (related=activity_ids.user_id)
- `activity_type_id` Many2one → `mail.activity.type` (related=activity_ids.activity_type_id)
- `activity_type_icon` Char “Activity Type Icon” (related=activity_ids.icon)
- `activity_date_deadline` Date “Next Activity Deadline” (readonly, compute=_compute_activity_date_deadline)
- `my_activity_date_deadline` Date “My Activity Deadline” (readonly, compute=_compute_my_activity_date_deadline)
- `activity_summary` Char “Next Activity Summary” (related=activity_ids.summary)
- `activity_exception_decoration` Selection (compute=_compute_activity_exception_type)
- `activity_exception_icon` Char “Icon” (compute=_compute_activity_exception_type)

Public methods: `activity_feedback`, `activity_reschedule`, `activity_schedule`, `activity_search`, `activity_send_mail`, `activity_unlink`, `toggle_active`, `unlink`, `write`

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
- `initial_res_model` Selection “Initial model” (compute=_compute_initial_res_model)
- `res_model_change` Boolean “Model has change”

Extension points: `_get_model_selection`

## `mail.alias` (defines)

Email Aliases

- `alias_name` Char “Alias Name”
- `alias_model_id` Many2one → `ir.model` (required)
- `alias_user_id` Many2one → `res.users`
- `alias_defaults` Text “Default Values” (required)
- `alias_force_thread_id` Integer “Record Thread ID”
- `alias_domain` Char “Alias domain” (compute=_compute_alias_domain)
- `alias_parent_model_id` Many2one → `ir.model`
- `alias_parent_thread_id` Integer “Parent Record Thread ID”
- `alias_contact` Selection “Alias Contact Security” (required)
- `alias_bounced_content` Html “Custom Bounced Message”

Public methods: `create`, `name_get`, `open_document`, `open_parent_document`, `write`

Extension points: `_check_alias_defaults`, `_get_alias_bounced_body`, `_get_alias_bounced_body_fallback`, `_get_alias_contact_description`

## `mail.alias.mixin` (defines)

Email Aliases Mixin

- `alias_id` Many2one → `mail.alias` “Alias” (required)

Public methods: `copy_data`, `create`, `unlink`, `write`

## `mail.blacklist` (defines)

Mail Blacklist

Inherits: `mail.thread`

- `email` Char “Email Address” (required)
- `active` Boolean

Public methods: `action_add`, `action_remove_with_reason`, `create`, `mail_action_blacklist_remove`, `write`

## `mail.channel` (defines)

Discussion Channel

Inherits: `mail.thread`

- `name` Char “Name” (required)
- `active` Boolean
- `channel_type` Selection “Channel Type” (required, readonly)
- `is_chat` Boolean “Is a chat” (compute=_compute_is_chat)
- `default_display_mode` Selection “Default Display Mode”
- `description` Text “Description”
- `image_128` Image “Image”
- `avatar_128` Image “Avatar” (compute=_compute_avatar_128)
- `channel_partner_ids` Many2many → `res.partner` “Partners” (compute=_compute_channel_partner_ids)
- `channel_member_ids` One2many → `mail.channel.member` “Members”
- `rtc_session_ids` One2many → `mail.channel.rtc.session`
- `is_member` Boolean “Is Member” (compute=_compute_is_member)
- `member_count` Integer “Member Count” (compute=_compute_member_count)
- `group_ids` Many2many → `res.groups` “Auto Subscription”
- `uuid` Char “UUID”
- `group_public_id` Many2one → `res.groups` “Authorized Group” (store, compute=_compute_group_public_id)
- `invitation_url` Char “Invitation URL” (compute=_compute_invitation_url)

Public methods: `action_unfollow`, `add_members`, `channel_change_description`, `channel_create`, `channel_fetch_preview`, `channel_fetched`, `channel_fold`, `channel_get`, `channel_info`, `channel_join`, `channel_pin`, `channel_rename`, `channel_set_custom_name`, `create`, `create_group`, `execute_command_help`, `execute_command_leave`, `execute_command_who`, `get_mention_suggestions`, `init`, `load_more_members`, `message_post`, `write`

Extension points: `_action_unfollow`, `_check_can_update_message_content`, `_get_avatar_cache_key`

## `mail.channel.member` (defines)

Listeners of a Channel

- `partner_id` Many2one → `res.partner` “Recipient” (index)
- `guest_id` Many2one → `mail.guest` “Guest” (readonly, index)
- `partner_email` Char “Email” (related=partner_id.email)
- `channel_id` Many2one → `mail.channel` “Channel” (required, readonly)
- `custom_channel_name` Char “Custom channel name”
- `fetched_message_id` Many2one → `mail.message` “Last Fetched”
- `seen_message_id` Many2one → `mail.message` “Last Seen”
- `message_unread_counter` Integer “Unread Messages Counter” (compute=_compute_message_unread)
- `fold_state` Selection “Conversation Fold State”
- `is_minimized` Boolean “Conversation is minimized”
- `is_pinned` Boolean “Is pinned on the interface”
- `last_interest_dt` Datetime “Last Interest”
- `last_seen_dt` Datetime “Last seen date”
- `rtc_session_ids` One2many → `mail.channel.rtc.session` “RTC Sessions”
- `rtc_inviting_session_id` Many2one → `mail.channel.rtc.session` “Ringing session”

Public methods: `create`, `init`, `name_get`, `unlink`, `write`

Extension points: `_get_as_sudo_from_request`, `_get_as_sudo_from_request_or_raise`, `_get_partner_data`

## `mail.channel.rtc.session` (defines)

Mail RTC session

- `channel_member_id` Many2one → `mail.channel.member` (required)
- `channel_id` Many2one → `mail.channel` (readonly, store, related=channel_member_id.channel_id)
- `partner_id` Many2one → `res.partner` “Partner” (related=channel_member_id.partner_id)
- `guest_id` Many2one → `mail.guest` (related=channel_member_id.guest_id)
- `write_date` Datetime “Last Updated On” (index)
- `is_screen_sharing_on` Boolean “Is sharing the screen”
- `is_camera_on` Boolean “Is sending user video”
- `is_muted` Boolean “Is microphone muted”
- `is_deaf` Boolean “Has disabled incoming sound”

Public methods: `action_disconnect`, `create`, `unlink`

## `mail.composer.mixin` (defines)

Mail Composer Mixin

Inherits: `mail.render.mixin`

- `subject` Char “Subject” (store, compute=_compute_subject)
- `body` Html “Contents” (store, compute=_compute_body)
- `template_id` Many2one → `mail.template`
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

Extension points: `_get_recipient_data`, `_get_subscription_data`

## `mail.gateway.allowed` (defines)

Mail Gateway Allowed

- `email` Char “Email Address”
- `email_normalized` Char “Normalized Email” (store, index, compute=_compute_email_normalized)

Public methods: `get_empty_list_help`

## `mail.guest` (defines)

Guest

Inherits: `avatar.mixin`

- `name` Char “Name” (required)
- `access_token` Char “Access Token” (required, readonly)
- `country_id` Many2one → `res.country` “Country”
- `lang` Selection “Language”
- `timezone` Selection “Timezone”
- `channel_ids` Many2many → `mail.channel` “Channels”
- `im_status` Char “IM Status” (compute=_compute_im_status)

Extension points: `_get_guest_from_context`, `_get_guest_from_request`, `_get_timezone_from_request`

## `mail.ice.server` (defines)

ICE server

- `server_type` Selection “Type” (required)
- `uri` Char “URI” (required)
- `username` Char
- `credential` Char

Extension points: `_get_ice_servers`, `_get_local_ice_servers`

## `mail.link.preview` (defines)

Store link preview data

- `message_id` Many2one → `mail.message` “Message” (required, index)
- `source_url` Char “URL” (required)
- `og_type` Char “Type”
- `og_title` Char “Title”
- `og_image` Char “Image”
- `og_description` Text “Description”
- `og_mimetype` Char “MIME type”
- `image_mimetype` Char “Image MIME type”
- `create_date` Datetime (index)

Extension points: `_create_link_preview`, `_create_link_previews`, `_get_link_preview_from_html`, `_get_link_preview_from_url`

## `mail.mail` (defines)

Outgoing Mails

- `mail_message_id` Many2one → `mail.message` (required, index)
- `mail_message_id_int` Integer (compute=_compute_mail_message_id_int)
- `body_html` Text “Text Contents”
- `body_content` Html “Rich-text Contents” (compute=_compute_body_content)
- `references` Text “References”
- `headers` Text “Headers”
- `restricted_attachment_count` Integer “Restricted attachments” (compute=_compute_restricted_attachments)
- `unrestricted_attachment_ids` Many2many → `ir.attachment` “Unrestricted Attachments” (compute=_compute_restricted_attachments)
- `is_notification` Boolean “Notification Email”
- `email_to` Text “To”
- `email_cc` Char “Cc”
- `recipient_ids` Many2many → `res.partner` “To (Partners)”
- `state` Selection (readonly)
- `failure_type` Selection “Failure type”
- `failure_reason` Text “Failure Reason”
- `auto_delete` Boolean “Auto Delete”
- `to_delete` Boolean “To Delete”
- `scheduled_date` Datetime “Scheduled Send Date”
- `fetchmail_server_id` Many2one → `fetchmail.server` (readonly)

Public methods: `action_open_document`, `action_retry`, `cancel`, `create`, `default_get`, `fields_get`, `mark_outgoing`, `process_email_queue`, `send`, `unlink`, `write`

## `mail.message` (defines)

Message

- `subject` Char “Subject”
- `date` Datetime “Date”
- `body` Html “Contents”
- `description` Char “Short description” (compute=_compute_description)
- `preview` Char “Preview” (compute=_compute_preview)
- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `parent_id` Many2one → `mail.message`
- `child_ids` One2many → `mail.message`
- `model` Char “Related Document Model”
- `res_id` Many2oneReference “Related Document ID”
- `record_name` Char “Message Record Name”
- `link_preview_ids` One2many → `mail.link.preview` “Link Previews”
- `message_type` Selection (required)
- `subtype_id` Many2one → `mail.message.subtype` (index)
- `mail_activity_type_id` Many2one → `mail.activity.type` (index)
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
- `starred` Boolean “Starred” (compute=_compute_starred)
- `tracking_value_ids` One2many → `mail.tracking.value` “Tracking values”
- `reply_to_force_new` Boolean “No threading for answers”
- `message_id` Char “Message-Id”
- `reply_to` Char “Reply-To”
- `mail_server_id` Many2one → `ir.mail_server`
- `email_layout_xmlid` Char “Layout”
- `email_add_signature` Boolean
- `mail_ids` One2many → `mail.mail` “Mails”
- `canned_response_ids` One2many → `mail.shortcode` “Canned Responses”
- `reaction_ids` One2many → `mail.message.reaction` “Reactions”

Public methods: `action_open_document`, `check_access_rule`, `create`, `default_get`, `export_data`, `init`, `is_thread_message`, `mark_all_as_read`, `message_format`, `read`, `set_message_done`, `toggle_message_starred`, `unlink`, `unstar_all`, `write`

Extension points: `_get_message_format_fields`, `_get_message_id`, `_get_message_preview`, `_get_record_name`, `_get_reply_to`, `_get_search_domain_share`

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

## `mail.render.mixin` (defines)

Mail Render Mixin

- `lang` Char “Language”
- `render_model` Char “Rendering Model” (compute=_compute_render_model)

Public methods: `create`, `write`

Extension points: `_check_access_right_dynamic_template`

## `mail.shortcode` (defines)

Canned Response / Shortcode

- `source` Char “Shortcut” (required)
- `substitution` Text “Substitution” (required)
- `description` Char “Description”
- `message_ids` Many2one → `mail.message` “Messages”

## `mail.template` (defines)

Email Templates

Inherits: `mail.render.mixin`, `template.reset.mixin`

- `name` Char “Name”
- `description` Text “Template description”
- `active` Boolean
- `template_category` Selection (compute=_compute_template_category)
- `model_id` Many2one → `ir.model`
- `model` Char “Related Document Model” (readonly, store, index, related=model_id.model)
- `subject` Char “Subject”
- `email_from` Char “From”
- `use_default_to` Boolean “Default recipients”
- `email_to` Char “To (Emails)”
- `partner_to` Char “To (Partners)”
- `email_cc` Char “Cc”
- `reply_to` Char “Reply To”
- `body_html` Html “Body”
- `attachment_ids` Many2many → `ir.attachment`
- `report_name` Char “Report Filename”
- `report_template` Many2one → `ir.actions.report`
- `mail_server_id` Many2one → `ir.mail_server`
- `scheduled_date` Char “Scheduled Date”
- `auto_delete` Boolean “Auto Delete”
- `ref_ir_act_window` Many2one → `ir.actions.act_window` (readonly)
- `can_write` Boolean (compute=_compute_can_write)

Public methods: `copy`, `create`, `create_action`, `default_get`, `generate_email`, `generate_recipients`, `send_mail`, `unlink`, `unlink_action`, `write`

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
- `message_main_attachment_id` Many2one → `ir.attachment` “Main Attachment”

Public methods: `copy_data`, `create`, `get_empty_list_help`, `message_change_thread`, `message_new`, `message_notify`, `message_parse`, `message_post`, `message_post_with_template`, `message_post_with_view`, `message_process`, `message_route`, `message_subscribe`, `message_unsubscribe`, `message_update`, `notify_cancel_by_type`, `unlink`, `write`

Extension points: `_check_can_update_message_content`, `_get_mail_message_access`, `_get_mail_thread_data`, `_get_mail_thread_data_attachments`

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

## `mail.tracking.value` (defines)

Mail Tracking Value

- `field` Many2one → `ir.model.fields` (required, index)
- `field_desc` Char “Field Description” (required)
- `field_type` Char “Field Type”
- `field_groups` Char (compute=_compute_field_groups)
- `old_value_integer` Integer “Old Value Integer”
- `old_value_float` Float “Old Value Float”
- `old_value_monetary` Float “Old Value Monetary”
- `old_value_char` Char “Old Value Char”
- `old_value_text` Text “Old Value Text”
- `old_value_datetime` Datetime “Old Value DateTime”
- `new_value_integer` Integer “New Value Integer”
- `new_value_float` Float “New Value Float”
- `new_value_monetary` Float “New Value Monetary”
- `new_value_char` Char “New Value Char”
- `new_value_text` Text “New Value Text”
- `new_value_datetime` Datetime “New Value Datetime”
- `currency_id` Many2one → `res.currency` (readonly)
- `mail_message_id` Many2one → `mail.message` (required, index)
- `tracking_sequence` Integer “Tracking field sequence”

Public methods: `create_tracking_values`

Extension points: `_get_display_value`, `_get_new_display_value`, `_get_old_display_value`

## `base` (extends)


Extension points: `_get_default_activity_view`, `_get_html_link`, `_get_mail_redirect_suggested_company`

## `res.company` (extends)

- `catchall_email` Char “Catchall Email” (compute=_compute_catchall)
- `catchall_formatted` Char “Catchall” (compute=_compute_catchall)
- `email_formatted` Char “Formatted Email” (compute=_compute_email_formatted)

## `res.config.settings` (extends)

- `fail_counter` Integer “Fail Mail” (compute=_compute_fail_counter)
- `alias_domain` Char “Alias Domain”
- `module_google_gmail` Boolean “Support Gmail Authentication”
- `module_microsoft_outlook` Boolean “Support Outlook Authentication”
- `restrict_template_rendering` Boolean “Restrict Template Rendering”
- `use_twilio_rtc_servers` Boolean “Use Twilio ICE servers”
- `twilio_account_sid` Char “Twilio Account SID”
- `twilio_account_token` Char “Twilio Account Auth Token”
- `primary_color` Char “Header Color” (related=company_id.primary_color)
- `secondary_color` Char “Button Color” (related=company_id.secondary_color)

Public methods: `open_email_layout`, `open_mail_templates`

## `res.groups` (extends)

Access Groups


Public methods: `write`

## `res.partner` (extends)

Inherits: `mail.activity.mixin`, `mail.thread.blacklist`

- `email` Char
- `phone` Char
- `parent_id` Many2one
- `user_id` Many2one
- `vat` Char
- `channel_ids` Many2many → `mail.channel` “Channels”

Public methods: `find_or_create`, `get_mention_suggestions`, `im_search`, `mail_partner_format`, `search_for_channel_invite`

Extension points: `_get_channels_as_member`, `_get_needaction_count`, `_get_view_cache_key`

## `res.users` (extends)

- `notification_type` Selection (required, store, compute=_compute_notification_type)
- `res_users_settings_ids` One2many → `res.users.settings`
- `res_users_settings_id` Many2one → `res.users.settings` “Settings” (compute=_compute_res_users_settings_id)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`, `create`, `systray_get_activities`, `unlink`, `write`

Extension points: `_get_portal_access_update_body`

## `res.users.settings` (defines)

User Settings

- `user_id` Many2one → `res.users` “User” (required)
- `is_discuss_sidebar_category_channel_open` Boolean “Is discuss sidebar category channel open?”
- `is_discuss_sidebar_category_chat_open` Boolean “Is discuss sidebar category chat open?”
- `push_to_talk_key` Char “Push-To-Talk shortcut”
- `use_push_to_talk` Boolean “Use the push to talk feature”
- `voice_active_duration` Integer “Duration of voice activity in ms”
- `volume_settings_ids` One2many → `res.users.settings.volumes` “Volumes of other partners”

Public methods: `set_res_users_settings`, `set_volume_setting`

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


## `mail.blacklist.remove` (defines)

Remove email from blacklist wizard

- `email` Char (required, readonly)
- `reason` Char

Public methods: `action_unblacklist_apply`

## `mail.compose.message` (defines)

Email composition wizard

Inherits: `mail.composer.mixin`

- `subject` Char “Subject”
- `body` Html “Contents”
- `parent_id` Many2one → `mail.message`
- `template_id` Many2one → `mail.template`
- `attachment_ids` Many2many → `ir.attachment`
- `email_layout_xmlid` Char “Email Notification Layout”
- `email_add_signature` Boolean
- `email_from` Char “From”
- `author_id` Many2one → `res.partner`
- `composition_mode` Selection “Composition mode”
- `model` Char “Related Document Model”
- `res_id` Integer “Related Document ID”
- `record_name` Char “Message Record Name”
- `use_active_domain` Boolean “Use active domain”
- `active_domain` Text “Active domain” (readonly)
- `message_type` Selection (required)
- `is_log` Boolean “Log as Internal Note”
- `subtype_id` Many2one → `mail.message.subtype`
- `notify` Boolean “Notify followers”
- `mail_activity_type_id` Many2one → `mail.activity.type`
- `reply_to` Char “Reply To”
- `reply_to_force_new` Boolean “Considers answers as new thread”
- `reply_to_mode` Selection “Replies” (compute=_compute_reply_to_mode)
- `partner_ids` Many2many → `res.partner`
- `auto_delete` Boolean “Delete Emails”
- `auto_delete_message` Boolean “Delete Message Copy”
- `mail_server_id` Many2one → `ir.mail_server`

Public methods: `action_save_as_template`, `action_send_mail`, `default_get`, `generate_email_for_composer`, `get_mail_values`, `get_record_data`, `render_message`

Extension points: `_action_send_mail`, `_get_blacklist_record_ids`, `_get_done_emails`, `_get_optout_emails`

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

- `partner_id` Many2one → `res.partner` “Partner” (required)
- `name` Char “Recipient Name” (related=partner_id.name)
- `email` Char “Email Address” (related=partner_id.email)
- `resend` Boolean “Try Again”
- `resend_wizard_id` Many2one → `mail.resend.message` “Resend wizard”
- `message` Char “Error message”

## `mail.template.preview` (defines)

Email Template Preview

- `mail_template_id` Many2one → `mail.template` “Related Mail Template” (required)
- `model_id` Many2one → `ir.model` “Targeted model” (related=mail_template_id.model_id)
- `resource_ref` Reference “Record”
- `lang` Selection “Template Preview Language”
- `no_record` Boolean “No Record” (compute=_compute_no_record)
- `error_msg` Char “Error Message” (readonly)
- `subject` Char “Subject” (compute=_compute_mail_template_fields)
- `email_from` Char “From” (compute=_compute_mail_template_fields)
- `email_to` Char “To” (compute=_compute_mail_template_fields)
- `email_cc` Char “Cc” (compute=_compute_mail_template_fields)
- `reply_to` Char “Reply-To” (compute=_compute_mail_template_fields)
- `scheduled_date` Char “Scheduled Date” (compute=_compute_mail_template_fields)
- `body_html` Html “Body” (compute=_compute_mail_template_fields)
- `attachment_ids` Many2many → `ir.attachment` (compute=_compute_mail_template_fields)
- `partner_ids` Many2many → `res.partner` “Recipients” (compute=_compute_mail_template_fields)

Public methods: `default_get`

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
- `send_mail` Boolean “Send Email”

Public methods: `add_followers`, `default_get`

Extension points: `_prepare_message_values`
