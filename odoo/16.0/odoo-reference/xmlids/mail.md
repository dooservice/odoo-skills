# mail — XML ids

## ir.actions.act_window

- `mail.action_email_compose_message_wizard`
- `mail.mail_resend_message_action`
- `mail.mail_template_preview_action`
- `mail.mail_template_reset_action`
- `mail.action_email_server_tree`
- `mail.action_view_message_subtype`
- `mail.action_view_mail_tracking_value`
- `mail.mail_notification_action`
- `mail.action_view_mail_message`
- `base.action_attachment`
- `mail.mail_message_schedule_action`
- `mail.action_view_mail_mail`
- `mail.act_server_history`
- `mail.action_view_followers`
- `mail.action_ice_servers`
- `mail.mail_channel_member_action`
- `mail.mail_channel_rtc_session_action`
- `mail.mail_link_preview_action`
- `mail.mail_channel_action_view`
- `mail.mail_shortcode_action`
- `mail.mail_activity_type_action`
- `mail.mail_activity_action`
- `base.ir_cron_act`
- `mail.action_view_mail_alias`
- `mail.mail_gateway_allowed_action`
- `mail.mail_guest_action`
- `mail.mail_message_reaction_action`
- `mail.res_users_settings_action`
- `mail.action_email_template_tree_all`
- `base.action_partner_form`
- `base.action_partner_customer_form`
- `base.action_partner_supplier_form`
- `mail.action_partner_mass_mail`
- `mail.mail_blacklist_action`

## ir.actions.act_window.view

- `mail.mail_activity_action_view_tree`
- `mail.mail_activity_action_view_form`

## ir.actions.client

- `mail.action_discuss`

## ir.cron

- `mail.ir_cron_mail_scheduler_action`
- `mail.ir_cron_module_update_notification`
- `mail.ir_cron_delete_notification`
- `mail.ir_cron_mail_gateway_action`
- `mail.ir_cron_send_scheduled_message`

## ir.rule

- `mail.mail_channel_rule`
- `mail.mail_channel_admin`
- `mail.ir_rule_mail_channel_member_group_user`
- `mail.ir_rule_mail_channel_member_group_system`
- `mail.ir_rule_mail_notifications_group_user`
- `mail.ir_rule_mail_notifications_group_portal`
- `mail.mail_message_subtype_rule_public`
- `mail.mail_activity_rule_user`
- `mail.mail_compose_message_rule`
- `mail.mail_template_employee_rule`
- `mail.mail_template_editor_rule`
- `mail.res_users_settings_rule_admin`
- `mail.res_users_settings_rule_user`
- `mail.res_users_settings_volumes_rule_user`
- `mail.res_users_settings_volumes_rule_admin`

## ir.ui.menu

- `mail.menu_root_discuss` — Discuss
- `base.menu_email`
- `mail.menu_mail_mail` — Emails
- `mail.menu_action_fetchmail_server_tree` — Incoming Mail Servers
- `mail.menu_email_templates`
- `mail.mail_alias_menu`
- `mail.mail_channel_menu_settings` — Channels
- `mail.mail_channel_member_menu` — Channels/Partner
- `mail.mail_gateway_allowed_menu`
- `mail.mail_menu_technical` — Discuss
- `mail.menu_mail_message` — Messages
- `mail.mail_message_schedule_menu` — Scheduled Messages
- `mail.menu_message_subtype` — Subtypes
- `mail.menu_mail_tracking_value` — Tracking Values
- `mail.menu_mail_activity_type`
- `mail.menu_mail_activities`
- `mail.mail_notification_menu` — Notifications
- `mail.menu_email_followers` — Followers
- `mail.mail_blacklist_menu` — Email Blacklist
- `mail.res_users_settings_menu` — User Settings
- `mail.mail_guest_menu` — Guests
- `mail.mail_channel_rtc_session_menu` — RTC sessions
- `mail.mail_channel_ice_servers_menu` — ICE servers
- `mail.mail_message_reaction_menu` — Message Reactions
- `mail.mail_link_preview_menu` — Link Previews
- `mail.mail_channel_integrations_menu`

## ir.ui.view

- `mail.mail_blacklist_remove_view_form` — on mail.blacklist.remove
- `mail.email_compose_message_wizard_form` — on mail.compose.message
- `mail.mail_resend_message_view_form` — on mail.resend.message
- `mail.mail_template_preview_view_form` — on mail.template.preview
- `mail.mail_wizard_invite_form` — on mail.wizard.invite
- `mail.mail_template_reset_view_form` — on mail.template.reset
- `mail.view_email_server_tree` — on fetchmail.server
- `mail.view_email_server_form` — on fetchmail.server
- `mail.view_email_server_search` — on fetchmail.server
- `mail.view_message_subtype_tree` — on mail.message.subtype
- `mail.view_mail_message_subtype_form` — on mail.message.subtype
- `mail.view_mail_tracking_value_tree` — on mail.tracking.value
- `mail.view_mail_tracking_value_form` — on mail.tracking.value
- `mail.mail_notification_view_tree` — on mail.notification
- `mail.mail_notification_view_form` — on mail.notification
- `mail.view_message_tree` — on mail.message
- `mail.mail_message_view_form` — on mail.message
- `mail.view_message_search` — on mail.message
- `mail.view_document_file_kanban` — on ir.attachment
- `mail.mail_message_schedule_view_form` — on mail.message.schedule
- `mail.mail_message_schedule_view_tree` — on mail.message.schedule
- `mail.mail_message_schedule_view_search` — on mail.message.schedule
- `mail.view_mail_form` — on mail.mail
- `mail.view_mail_tree` — on mail.mail
- `mail.view_mail_search` — on mail.mail
- `mail.view_followers_tree` — on mail.followers
- `mail.view_mail_subscription_form` — on mail.followers
- `mail.view_ice_server_tree` — on mail.ice.server
- `mail.view_ice_server_form` — on mail.ice.server
- `mail.mail_channel_member_view_tree` — on mail.channel.member
- `mail.mail_channel_member_view_form` — on mail.channel.member
- `mail.mail_channel_rtc_session_view_search` — on mail.channel.rtc.session
- `mail.mail_channel_rtc_session_view_tree` — on mail.channel.rtc.session
- `mail.mail_channel_rtc_session_view_form` — on mail.channel.rtc.session
- `mail.mail_link_preview_view_tree` — on mail.link.preview
- `mail.mail_channel_view_kanban` — on mail.channel
- `mail.mail_channel_view_form` — on mail.channel
- `mail.mail_channel_view_tree` — on mail.channel
- `mail.mail_channel_view_search` — on mail.channel
- `mail.mail_shortcode_view_tree` — on mail.shortcode
- `mail.mail_shortcode_view_form` — on mail.shortcode
- `mail.mail_activity_type_view_form` — on mail.activity.type
- `mail.mail_activity_type_view_search` — on mail.activity.type
- `mail.mail_activity_type_view_tree` — on mail.activity.type
- `mail.mail_activity_view_form_popup` — on mail.activity
- `mail.mail_activity_view_form` — on mail.activity inherits mail.mail_activity_view_form_popup
- `mail.mail_activity_view_search` — on mail.activity
- `mail.mail_activity_view_tree` — on mail.activity
- `mail.mail_activity_view_calendar` — on mail.activity
- `mail.res_config_settings_view_form` — on res.config.settings inherits base_setup.res_config_settings_view_form
- `mail.message_user_assigned`
- `mail.message_activity_done`
- `mail.message_activity_assigned`
- `mail.message_origin_link`
- `mail.mail_notification_layout`
- `mail.mail_notification_light`
- `mail.notification_preview`
- `mail.mail_notification_layout_with_responsible_signature` — inherits mail.mail_notification_layout
- `mail.message_notification_limit_email`
- `mail.mail_bounce_catchall`
- `mail.mail_bounce_alias_security`
- `mail.discuss_public_layout`
- `mail.discuss_public_channel_template`
- `mail.view_mail_alias_form` — on mail.alias
- `mail.view_mail_alias_tree` — on mail.alias
- `mail.view_mail_alias_search` — on mail.alias
- `mail.mail_gateway_allowed_view_tree` — on mail.gateway.allowed
- `mail.mail_gateway_allowed_view_search` — on mail.gateway.allowed
- `mail.mail_guest_view_tree` — on mail.guest
- `mail.mail_message_reaction_view_tree` — on mail.message.reaction
- `mail.view_users_form_simple_modif_mail` — on res.users inherits base.view_users_form_simple_modif
- `mail.view_users_form_mail` — on res.users inherits base.view_users_form
- `mail.res_users_settings_view_tree` — on res.users.settings
- `mail.res_users_settings_view_form` — on res.users.settings
- `mail.email_template_form` — on mail.template
- `mail.email_template_tree` — on mail.template
- `mail.view_email_template_search` — on mail.template
- `mail.view_server_action_form_template` — on ir.actions.server inherits base.view_server_action_form
- `mail.model_form_view` — on ir.model inherits base.view_model_form
- `mail.model_search_view` — on ir.model inherits base.view_model_search
- `mail.field_form_view` — on ir.model.fields inherits base.view_model_fields_form
- `mail.res_partner_view_form_inherit_mail` — on res.partner inherits base.view_partner_form
- `mail.res_partner_view_kanban_inherit_mail` — on res.partner inherits base.res_partner_kanban_view
- `mail.res_partner_view_search_inherit_mail` — on res.partner inherits base.view_res_partner_filter
- `mail.res_partner_view_tree_inherit_mail` — on res.partner inherits base.view_partner_tree
- `mail.res_partner_view_activity` — on res.partner
- `mail.mail_blacklist_view_tree` — on mail.blacklist
- `mail.mail_blacklist_view_form` — on mail.blacklist
- `mail.mail_blacklist_view_search` — on mail.blacklist

## mail.activity.type

- `mail.mail_activity_data_email`
- `mail.mail_activity_data_call`
- `mail.mail_activity_data_meeting`
- `mail.mail_activity_data_todo`
- `mail.mail_activity_data_upload_document`
- `mail.mail_activity_data_warning`

## mail.channel

- `mail.channel_all_employees`
- `mail.channel_all_employees`

## mail.channel.member

- `mail.channel_member_general_channel_for_admin`

## mail.message

- `mail.module_install_notification`

## mail.message.subtype

- `mail.mt_comment`
- `mail.mt_note`
- `mail.mt_activities`

## res.groups

- `mail.group_mail_template_editor`
- `base.group_system`
- `base.group_user`

## res.partner

- `base.partner_root`

## res.users

- `base.user_root`
