# mail — XML ids

## discuss.channel

- `mail.channel_all_employees`
- `mail.channel_admin`
- `mail.channel_all_employees`
- `mail.channel_admin`

## discuss.channel.member

- `mail.channel_member_general_channel_for_admin`
- `mail.channel_member_channel_admin_partner_admin`

## ir.actions.act_url

- `mail.action_open_discuss_settings`

## ir.actions.act_window

- `mail.action_email_compose_message_wizard`
- `mail.mail_template_preview_action`
- `mail.mail_template_reset_action`
- `mail.action_email_server_tree`
- `mail.ir_ui_view_action_usage_mail_post`
- `mail.action_view_message_subtype`
- `mail.mail_notification_action`
- `mail.action_view_mail_message`
- `base.action_attachment`
- `mail.mail_message_schedule_action`
- `mail.action_view_mail_mail`
- `mail.act_server_history`
- `mail.action_view_followers`
- `mail.action_ice_servers`
- `mail.discuss_category_settings_action`
- `mail.discuss_channel_member_action`
- `mail.discuss_channel_rtc_session_action`
- `mail.mail_link_preview_action`
- `mail.discuss_gif_favorite_action`
- `mail.discuss_channel_action_view`
- `mail.discuss_channel_action`
- `mail.discuss_my_conversations_action`
- `mail.mail_canned_response_action`
- `mail.res_role_action`
- `mail.mail_activity_type_action`
- `mail.mail_activity_action`
- `mail.mail_activity_without_access_action`
- `mail.mail_activity_action_my`
- `mail.mail_activity_action_to_assign`
- `mail.mail_activity_plan_action`
- `base.ir_cron_act`
- `mail.mail_alias_domain_action`
- `mail.mail_alias_action`
- `mail.mail_gateway_allowed_action`
- `mail.mail_guest_action`
- `mail.mail_message_reaction_action`
- `mail.action_res_users_my_fullpage`
- `mail.res_users_settings_action`
- `mail.action_email_template_tree_all`
- `base.action_partner_form`
- `base.action_partner_customer_form`
- `base.action_partner_supplier_form`
- `mail.action_partner_mass_mail`
- `mail.mail_blacklist_action`
- `mail.discuss_call_history_action`

## ir.actions.act_window.view

- `mail.mail_activity_action_view_tree`
- `mail.mail_activity_action_view_form`
- `mail.mail_activity_action_without_access_view_tree`
- `mail.mail_activity_action_without_access_view_form`
- `mail.mail_activity_action_my_view_tree`
- `mail.mail_activity_action_my_view_kanban`
- `mail.mail_activity_action_my_view_calendar`
- `mail.mail_activity_action_my_view_pivot`
- `mail.mail_activity_action_my_view_graph`
- `mail.mail_activity_action_to_assign_view_list`
- `mail.mail_activity_plan_view_tree_action`
- `mail.mail_activity_plan_view_form_action`
- `mail.action_res_users_my_fullpage_view`

## ir.actions.client

- `mail.action_discuss`
- `mail.discuss_notification_settings_action`
- `mail.discuss_call_settings_action`

## ir.config_parameter

- `mail.gc_delete_overdue_activities_year_threshold`
- `mail.restrict_template_rendering`

## ir.cron

- `mail.ir_cron_mail_scheduler_action`
- `mail.ir_cron_module_update_notification`
- `mail.ir_cron_delete_notification`
- `mail.ir_cron_mail_gateway_action`
- `mail.ir_cron_post_scheduled_message`
- `mail.ir_cron_send_scheduled_message`
- `mail.ir_cron_web_push_notification`
- `mail.ir_cron_mail_end_polls`
- `mail.ir_cron_discuss_channel_member_unmute`
- `mail.ir_cron_discuss_channel_sync_last_interest_dt`

## ir.ui.menu

- `mail.menu_root_discuss` — Discuss
- `mail.main_menu_discuss` — Discuss
- `mail.menu_channel` — Channels
- `mail.menu_configuration` — Configuration
- `mail.menu_settings` — Settings
- `mail.menu_discuss_category` — Categories
- `mail.menu_canned_responses` — Canned Responses
- `mail.menu_roles` — Roles
- `mail.menu_discuss_user_settings` — User Settings
- `mail.menu_notification_settings` — Notifications
- `mail.menu_call_settings` — Voice & Video
- `base.menu_email`
- `mail.menu_mail_mail` — Emails
- `mail.mail_alias_menu`
- `mail.mail_alias_domain_menu`
- `mail.menu_action_fetchmail_server_tree` — Incoming Mail Servers
- `mail.menu_email_templates`
- `mail.ir_ui_view_menu_usage_mail_post` — System Notifications
- `mail.discuss_channel_menu_settings` — Channels
- `mail.discuss_channel_member_menu` — Channels/Members
- `mail.mail_gateway_allowed_menu`
- `mail.mail_menu_technical` — Discuss
- `mail.menu_mail_message` — Messages
- `mail.mail_message_schedule_menu` — Scheduled Messages
- `mail.menu_message_subtype` — Subtypes
- `mail.mail_notification_menu` — Notifications
- `mail.menu_email_followers` — Followers
- `mail.mail_blacklist_menu` — Email Blacklist
- `mail.res_users_settings_menu` — User Settings
- `mail.mail_guest_menu` — Guests
- `mail.discuss_channel_rtc_session_menu` — RTC sessions
- `mail.ice_servers_menu` — ICE Servers
- `mail.mail_message_reaction_menu` — Message Reactions
- `mail.mail_link_preview_menu` — Link Previews
- `mail.discuss_gif_favorite_menu` — GIF favorite
- `mail.menu_mail_activities_section` — Activities
- `mail.menu_mail_activities`
- `mail.menu_mail_activity_type`
- `mail.menu_mail_activity_plan`
- `mail.discuss_channel_integrations_menu`
- `mail.discuss_call_history_menu` — Call History

## ir.ui.view

- `mail.mail_activity_schedule_view_form` — on mail.activity.schedule
- `mail.mail_blacklist_remove_view_form` — on mail.blacklist.remove
- `mail.email_compose_message_wizard_form` — on mail.compose.message
- `mail.mail_compose_message_view_form_template_save` — on mail.compose.message
- `mail.mail_template_preview_view_form` — on mail.template.preview
- `mail.mail_followers_edit_form` — on mail.followers.edit
- `mail.mail_followers_list_edit_form` — on mail.followers.edit inherits mail_followers_edit_form
- `mail.mail_template_reset_view_form` — on mail.template.reset
- `mail.view_email_server_tree` — on fetchmail.server
- `mail.view_email_server_form` — on fetchmail.server
- `mail.view_email_server_search` — on fetchmail.server
- `mail.ir_access_form_view_inherit_mail` — on ir.access inherits base.ir_access_form_view
- `mail.ir_cron_view_form` — on ir.cron inherits base.ir_cron_view_form
- `mail.ir_filters_view_form` — on ir.filters inherits base.ir_filters_view_form
- `mail.ir_filters_view_tree` — on ir.filters inherits base.ir_filters_view_tree
- `mail.ir_mail_server_view_form` — on ir.mail_server inherits base.ir_mail_server_form
- `mail.ir_ui_view_view_search_mail` — on ir.ui.view
- `mail.view_message_subtype_tree` — on mail.message.subtype
- `mail.view_mail_message_subtype_form` — on mail.message.subtype
- `mail.mail_message_subtype_view_search` — on mail.message.subtype
- `mail.mail_notification_view_tree` — on mail.notification
- `mail.mail_notification_view_form` — on mail.notification
- `mail.view_message_tree` — on mail.message
- `mail.mail_message_view_form` — on mail.message
- `mail.view_message_search` — on mail.message
- `mail.view_document_file_kanban` — on ir.attachment
- `mail.ir_attachment_view_list` — on ir.attachment inherits base.view_attachment_tree
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
- `mail.view_ice_server_kanban` — on mail.ice.server
- `mail.view_ice_server_search` — on mail.ice.server
- `mail.discuss_category_view_search` — on discuss.category
- `mail.discuss_category_view_tree` — on discuss.category
- `mail.discuss_category_view_form` — on discuss.category
- `mail.discuss_category_view_kanban` — on discuss.category
- `mail.discuss_channel_member_view_tree` — on discuss.channel.member
- `mail.discuss_channel_member_view_form` — on discuss.channel.member
- `mail.discuss_channel_rtc_session_view_search` — on discuss.channel.rtc.session
- `mail.discuss_channel_rtc_session_view_tree` — on discuss.channel.rtc.session
- `mail.discuss_channel_rtc_session_view_form` — on discuss.channel.rtc.session
- `mail.mail_link_preview_view_form` — on mail.link.preview
- `mail.mail_link_preview_view_tree` — on mail.link.preview
- `mail.message_link_preview_list` — on mail.message.link.preview
- `mail.discuss_gif_favorite_view_form` — on discuss.gif.favorite
- `mail.discuss_gif_favorite_view_tree` — on discuss.gif.favorite
- `mail.discuss_channel_view_kanban` — on discuss.channel
- `mail.discuss_channel_view_list` — on discuss.channel
- `mail.discuss_channel_view_form` — on discuss.channel
- `mail.discuss_channel_view_tree` — on discuss.channel
- `mail.discuss_channel_view_search` — on discuss.channel
- `mail.discuss_my_conversations_view_search` — on discuss.channel
- `mail.mail_canned_response_view_search` — on mail.canned.response
- `mail.mail_canned_response_view_tree` — on mail.canned.response
- `mail.mail_canned_response_view_form` — on mail.canned.response
- `mail.mail_canned_response_view_kanban` — on mail.canned.response
- `mail.res_role_view_search` — on res.role
- `mail.res_role_view_tree` — on res.role
- `mail.res_role_view_form` — on res.role
- `mail.mail_activity_type_view_form` — on mail.activity.type
- `mail.mail_activity_type_view_search` — on mail.activity.type
- `mail.mail_activity_type_view_tree` — on mail.activity.type
- `mail.mail_activity_type_view_kanban` — on mail.activity.type
- `mail.mail_activity_view_form_popup` — on mail.activity
- `mail.mail_activity_view_form` — on mail.activity inherits mail.mail_activity_view_form_popup
- `mail.mail_activity_view_form_without_record_access` — on mail.activity
- `mail.mail_activity_view_search` — on mail.activity
- `mail.mail_activity_view_tree` — on mail.activity
- `mail.mail_activity_view_tree_without_record_access` — on mail.activity inherits mail_activity_view_tree
- `mail.mail_activity_view_tree_open_target` — on mail.activity inherits mail_activity_view_tree
- `mail.mail_activity_view_kanban_open_target` — on mail.activity
- `mail.mail_activity_view_calendar` — on mail.activity
- `mail.mail_activity_view_pivot` — on mail.activity
- `mail.mail_activity_view_graph` — on mail.activity
- `mail.mail_activity_plan_view_search` — on mail.activity.plan
- `mail.mail_activity_plan_view_tree` — on mail.activity.plan
- `mail.mail_activity_plan_view_tree_detailed` — on mail.activity.plan inherits mail.mail_activity_plan_view_tree
- `mail.mail_activity_plan_view_form` — on mail.activity.plan
- `mail.mail_activity_plan_view_kanban` — on mail.activity.plan
- `mail.mail_activity_plan_view_form_fixed_model` — on mail.activity.plan inherits mail.mail_activity_plan_view_form
- `mail.mail_activity_plan_template_view_tree` — on mail.activity.plan.template
- `mail.mail_activity_plan_template_view_form` — on mail.activity.plan.template
- `mail.res_config_settings_view_form_sfu_client_source` — on res.config.settings
- `mail.res_config_settings_view_form` — on res.config.settings inherits base_setup.res_config_settings_view_form
- `mail.message_user_assigned`
- `mail.message_activity_done`
- `mail.message_activity_assigned`
- `mail.message_origin_link`
- `mail.discuss_channel_invitation_template`
- `mail.mail_tracking_template`
- `mail.group_change_template`
- `mail.mail_notification_layout`
- `mail.mail_notification_light`
- `mail.notification_preview`
- `mail.mail_notification_layout_with_responsible_signature` — inherits mail.mail_notification_layout
- `mail.message_notification_limit_email`
- `mail.message_notification_out_of_office`
- `mail.mail_bounce_catchall`
- `mail.mail_bounce_alias_security`
- `mail.mail_attachment_links`
- `mail.account_security_alert`
- `mail.discuss_public_channel_template`
- `mail.mail_alias_domain_view_form` — on mail.alias.domain
- `mail.mail_alias_domain_view_tree` — on mail.alias.domain
- `mail.mail_alias_domain_view_search` — on mail.alias.domain
- `mail.mail_alias_view_form` — on mail.alias
- `mail.mail_alias_view_tree` — on mail.alias
- `mail.mail_alias_view_search` — on mail.alias
- `mail.content_text`
- `mail.content_markdown`
- `mail.mail_gateway_allowed_view_tree` — on mail.gateway.allowed
- `mail.mail_gateway_allowed_view_search` — on mail.gateway.allowed
- `mail.mail_guest_view_tree` — on mail.guest
- `mail.mail_guest_view_form` — on mail.guest
- `mail.mail_message_reaction_view_form` — on mail.message.reaction
- `mail.mail_message_reaction_view_tree` — on mail.message.reaction
- `mail.public_layout`
- `mail.message_document_unfollowed`
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
- `mail.discuss_call_history_view_tree` — on discuss.call.history
- `mail.discuss_call_history_view_search` — on discuss.call.history
- `mail.discuss_call_history_view_form` — on discuss.call.history
- `mail.res_company_view_form` — on res.company inherits base.view_company_form
- `mail.mail_scheduled_message_view_form` — on mail.scheduled.message
- `mail.mail_notification_invite` — inherits mail.mail_notification_layout
- `mail.mail_notification_multi_invite` — inherits mail.mail_notification_invite

## mail.activity.type

- `mail.mail_activity_data_email`
- `mail.mail_activity_data_call`
- `mail.mail_activity_data_meeting`
- `mail.mail_activity_data_todo`
- `mail.mail_activity_data_upload_document`
- `mail.mail_activity_data_warning`

## mail.canned.response

- `mail.mail_canned_response_data_hello`

## mail.message

- `mail.module_install_notification`

## mail.message.subtype

- `mail.mt_comment`
- `mail.mt_note`
- `mail.mt_activities`
- `mail.mt_important_notification`

## res.groups

- `mail.group_mail_canned_response_admin`
- `mail.group_mail_template_editor`
- `base.group_system`
- `mail.group_mail_notification_type_inbox`

## res.groups.privilege

- `mail.res_groups_privilege_canned_response`

## res.partner

- `base.partner_root`

## res.users

- `base.user_root`

## web_tour.tour

- `mail.discuss_channel_tour`
