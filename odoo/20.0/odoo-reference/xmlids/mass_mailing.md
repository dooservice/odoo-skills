# mass_mailing — XML ids

## ir.actions.act_window

- `mass_mailing.mailing_contact_import_action`
- `mass_mailing.mailing_contact_to_list_action`
- `mass_mailing.res_partner_to_list_action`
- `mass_mailing.action_mail_mass_mailing_test`
- `mass_mailing.mailing_mailing_schedule_date_action`
- `mass_mailing.mailing_trace_report_action_mail`
- `mass_mailing.mailing_filter_action`
- `mass_mailing.action_mailing_filter_quick_create`
- `mass_mailing.mailing_trace_action`
- `mass_mailing.action_view_mail_mail_statistics_mailing`
- `mass_mailing.action_view_mass_mailing_contacts`
- `mass_mailing.action_mailing_list_quick_create`
- `mass_mailing.action_view_mass_mailing_lists`
- `mass_mailing.mailing_mailing_action_mail`
- `mass_mailing.action_view_mass_mailings_from_campaign`
- `mass_mailing.action_create_mass_mailings_from_campaign`
- `mass_mailing.action_ab_testing_open_winner_mailing`
- `mass_mailing.mailing_mailing_action_templates`
- `mass_mailing.mailing_subscription_optout_action`
- `mass_mailing.mailing_subscription_action_report_optout`
- `mass_mailing.action_mass_mailing_configuration`
- `mass_mailing.action_view_utm_campaigns`

## ir.actions.act_window.view

- `mass_mailing.mailing_mailing_action_mail_fullwidth_tree`
- `mass_mailing.mailing_mailing_action_mail_fullwidth_kanban`
- `mass_mailing.mailing_mailing_action_mail_fullwidth_calendar`

## ir.actions.client

- `mass_mailing.res_partner_to_list_results_action`

## ir.actions.server

- `mass_mailing.mailing_list_merge_action`

## ir.attachment

- `mass_mailing.s_cover_default_image`
- `mass_mailing.s_media_list_default_image_1`
- `mass_mailing.s_media_list_default_image_2`
- `mass_mailing.s_media_list_default_image_3`
- `mass_mailing.s_company_team_default_image_1`
- `mass_mailing.s_company_team_default_image_2`
- `mass_mailing.s_company_team_default_image_3`
- `mass_mailing.s_company_team_default_image_4`
- `mass_mailing.s_company_team_default_image_5`
- `mass_mailing.s_company_team_default_image_6`
- `mass_mailing.s_reference_default_image_1`
- `mass_mailing.s_reference_default_image_2`
- `mass_mailing.s_reference_default_image_3`
- `mass_mailing.s_reference_default_image_4`
- `mass_mailing.s_product_list_default_image_1`
- `mass_mailing.s_product_list_default_image_2`
- `mass_mailing.s_product_list_default_image_3`
- `mass_mailing.s_blockquote_default_image`
- `mass_mailing.s_image_text_default_image`
- `mass_mailing.s_event_default_image_1`
- `mass_mailing.s_event_default_image_2`
- `mass_mailing.s_masonry_block_default_image_1`
- `mass_mailing.s_masonry_block_default_image_2`
- `mass_mailing.s_picture_default_image`
- `mass_mailing.s_text_image_default_image`
- `mass_mailing.s_three_columns_default_image_1`
- `mass_mailing.s_three_columns_default_image_2`
- `mass_mailing.s_three_columns_default_image_3`
- `mass_mailing.s_shape_image_default_image`
- `mass_mailing.set_catalog_square_md_1`
- `mass_mailing.set_catalog_square_md_2`
- `mass_mailing.set_catalog_square_md_3`
- `mass_mailing.set_catalog_square_md_4`

## ir.cron

- `mass_mailing.ir_cron_mass_mailing_queue`
- `mass_mailing.ir_cron_mass_mailing_ab_testing`

## ir.ui.menu

- `mass_mailing.mass_mailing_menu_root` — Email Marketing
- `mass_mailing.mass_mailing_menu` — Mailings
- `mass_mailing.mass_mailing_mailing_list_menu` — Recipients
- `mass_mailing.menu_email_mass_mailing_lists` — Mailing Lists
- `mass_mailing.menu_email_mass_mailing_contacts` — Mailing Contacts
- `mass_mailing.menu_email_mass_mailing_dynamic_lists` — Dynamic Lists
- `mass_mailing.mass_mailing_template_menu` — Templates
- `mass_mailing.menu_email_campaigns` — Campaigns
- `mass_mailing.menu_mass_mailing_report` — Reporting
- `mass_mailing.mailing_menu_report_mailing` — Mailing Analysis
- `mass_mailing.mailing_menu_report_subscribe_reason` — Opt-Out Report
- `mass_mailing.mass_mailing_configuration` — Configuration
- `mass_mailing.menu_mass_mailing_global_settings` — Settings
- `mass_mailing.menu_view_mass_mailing_stages` — Campaign Stages
- `mass_mailing.mass_mailing_tag_menu`
- `mass_mailing.link_tracker_menu_mass_mailing` — Link Tracker
- `mass_mailing.mail_blacklist_mm_menu` — Blacklisted Email Addresses
- `mass_mailing.mailing_subscription_optout_menu` — Optout Reasons
- `mass_mailing.mailing_mailing_menu_technical` — Mass Mailing
- `mass_mailing.menu_email_statistics` — Mailing Traces

## ir.ui.view

- `mass_mailing.digest_mail_main` — inherits digest.digest_mail_main
- `mass_mailing.mass_mailing_mail_layout`
- `mass_mailing.ab_testing_description`
- `mass_mailing.mass_mailing_kpi_link_trackers`
- `mass_mailing.email_compose_form_mass_mailing` — on mail.compose.message inherits mail.email_compose_message_wizard_form
- `mass_mailing.mailing_contact_import_view_form` — on mailing.contact.import
- `mass_mailing.mailing_contact_to_list_view_form` — on mailing.contact.to.list
- `mass_mailing.view_mail_mass_mailing_test_form` — on mailing.mailing.test
- `mass_mailing.view_mail_mass_mailing_test_send_test_form` — on mailing.mailing.test
- `mass_mailing.mailing_mailing_schedule_date_view_form` — on mailing.mailing.schedule.date
- `mass_mailing.mailing_trace_report_view_tree` — on mailing.trace.report
- `mass_mailing.mailing_trace_report_view_pivot` — on mailing.trace.report
- `mass_mailing.mailing_trace_report_view_graph` — on mailing.trace.report
- `mass_mailing.mailing_trace_report_view_search` — on mailing.trace.report
- `mass_mailing.mail_blacklist_view_tree` — on mail.blacklist inherits mail.mail_blacklist_view_tree
- `mass_mailing.mail_blacklist_view_form` — on mail.blacklist inherits mail.mail_blacklist_view_form
- `mass_mailing.mail_blacklist_view_search` — on mail.blacklist inherits mail.mail_blacklist_view_search
- `mass_mailing.mailing_filter_view_search` — on mailing.filter
- `mass_mailing.mailing_filter_view_tree` — on mailing.filter
- `mass_mailing.mailing_filter_view_kanban` — on mailing.filter
- `mass_mailing.mailing_filter_view_form` — on mailing.filter
- `mass_mailing.mailing_filter_view_form_simplified` — on mailing.filter inherits mailing_filter_view_form
- `mass_mailing.preview_content_mobile`
- `mass_mailing.mailing_trace_view_search` — on mailing.trace
- `mass_mailing.mailing_trace_view_tree` — on mailing.trace
- `mass_mailing.mailing_trace_view_tree_mail` — on mailing.trace
- `mass_mailing.mailing_trace_view_form` — on mailing.trace
- `mass_mailing.view_mail_mail_statistics_graph` — on mailing.trace
- `mass_mailing.link_tracker_view_search` — on link.tracker inherits link_tracker.link_tracker_view_search
- `mass_mailing.link_tracker_view_form` — on link.tracker inherits link_tracker.link_tracker_view_form
- `mass_mailing.link_tracker_view_tree` — on link.tracker inherits link_tracker.link_tracker_view_tree
- `mass_mailing.link_tracker_click_view_search` — on link.tracker.click inherits link_tracker.link_tracker_click_view_search
- `mass_mailing.link_tracker_click_view_form` — on link.tracker.click inherits link_tracker.link_tracker_click_view_form
- `mass_mailing.link_tracker_click_view_tree` — on link.tracker.click inherits link_tracker.link_tracker_click_view_tree
- `mass_mailing.link_tracker_click_view_list_simplified` — on link.tracker.click
- `mass_mailing.link_tracker_click_view_graph` — on link.tracker.click inherits link_tracker.link_tracker_click_view_graph
- `mass_mailing.mailing_contact_view_search` — on mailing.contact
- `mass_mailing.mailing_contact_view_tree` — on mailing.contact
- `mass_mailing.mailing_contact_view_list_from_filter` — on mailing.contact inherits mailing_contact_view_tree
- `mass_mailing.mailing_contact_view_kanban` — on mailing.contact
- `mass_mailing.mailing_contact_view_form` — on mailing.contact
- `mass_mailing.mailing_contact_view_pivot` — on mailing.contact
- `mass_mailing.mailing_contact_view_graph` — on mailing.contact
- `mass_mailing.mailing_contact_view_tree_split_name` — on mailing.contact inherits mass_mailing.mailing_contact_view_tree
- `mass_mailing.mailing_contact_view_form_split_name` — on mailing.contact inherits mass_mailing.mailing_contact_view_form
- `mass_mailing.mailing_list_view_search` — on mailing.list
- `mass_mailing.mailing_list_view_tree` — on mailing.list
- `mass_mailing.mailing_list_view_form` — on mailing.list
- `mass_mailing.mailing_list_view_form_simplified` — on mailing.list
- `mass_mailing.mailing_list_view_kanban` — on mailing.list
- `mass_mailing.view_mail_mass_mailing_search` — on mailing.mailing
- `mass_mailing.view_mail_mass_mailing_tree` — on mailing.mailing
- `mass_mailing.mailing_mailing_view_list_template` — on mailing.mailing
- `mass_mailing.view_mail_mass_mailing_form` — on mailing.mailing
- `mass_mailing.view_mail_mass_mailing_kanban` — on mailing.mailing
- `mass_mailing.mailing_mailing_view_calendar` — on mailing.mailing
- `mass_mailing.mailing_mailing_view_search_templates` — on mailing.mailing
- `mass_mailing.mailing_mailing_view_kanban_templates` — on mailing.mailing
- `mass_mailing.mailing_subscription_optout_view_form` — on mailing.subscription.optout
- `mass_mailing.mailing_subscription_optout_view_tree` — on mailing.subscription.optout
- `mass_mailing.mailing_subscription_optout_view_search` — on mailing.subscription.optout
- `mass_mailing.mailing_subscription_view_form` — on mailing.subscription
- `mass_mailing.mailing_subscription_view_graph` — on mailing.subscription
- `mass_mailing.mailing_subscription_view_pivot` — on mailing.subscription
- `mass_mailing.mailing_subscription_view_tree` — on mailing.subscription
- `mass_mailing.mailing_subscription_view_search` — on mailing.subscription
- `mass_mailing.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form
- `mass_mailing.res_partner_view_list` — on res.partner inherits base.view_partner_tree
- `mass_mailing.res_partner_view_form` — on res.partner inherits base.view_partner_form
- `mass_mailing.utm_campaign_view_form` — on utm.campaign inherits utm.utm_campaign_view_form
- `mass_mailing.utm_campaign_view_kanban` — on utm.campaign inherits utm.utm_campaign_view_kanban
- `mass_mailing.layout`
- `mass_mailing.mailing_report_deactivated`
- `mass_mailing.mailing_view_generic`
- `mass_mailing.mailing_view`
- `mass_mailing.page_mailing_confirm_unsubscribe`
- `mass_mailing.page_mailing_has_unsubscribed`
- `mass_mailing.page_mailing_unsubscribe`
- `mass_mailing.unsubscribe_form`
- `mass_mailing.theme_basic_template`
- `mass_mailing.theme_empty_template`
- `mass_mailing.theme_default_template`
- `mass_mailing.s_social_media_template`
- `mass_mailing.s_social_media`
- `mass_mailing.social_links`
- `mass_mailing.s_mail_block_header_logo_and_stacked_menu`
- `mass_mailing.s_mail_company_logo`
- `mass_mailing.s_mail_block_footer_social`
- `mass_mailing.email_designer_themes`
- `mass_mailing.email_designer_snippets`

## mailing.contact

- `mass_mailing.mass_mail_contact_0`

## mailing.list

- `mass_mailing.mailing_list_data`

## mailing.subscription

- `mass_mailing.mailing_list_data_sub_contact_0`

## mailing.subscription.optout

- `mass_mailing.mailing_subscription_optout_data_0`
- `mass_mailing.mailing_subscription_optout_data_1`
- `mass_mailing.mailing_subscription_optout_data_2`
- `mass_mailing.mailing_subscription_optout_data_3`
- `mass_mailing.mailing_subscription_optout_data_4`

## portal.entry

- `mass_mailing.portal_entry_newsletters`

## res.groups

- `mass_mailing.group_mass_mailing_user`
- `mass_mailing.group_mass_mailing_campaign`

## res.groups.privilege

- `mass_mailing.res_groups_privilege_email_marketing`

## web_tour.tour

- `mass_mailing.mass_mailing_tour`
