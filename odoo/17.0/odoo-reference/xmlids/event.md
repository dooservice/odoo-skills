# event — XML ids

## event.stage

- `event.event_stage_new`
- `event.event_stage_booked`
- `event.event_stage_announced`
- `event.event_stage_done`
- `event.event_stage_cancelled`

## ir.actions.act_window

- `event.action_event_mail`
- `event.act_event_registration_from_event`
- `event.event_registration_action_kanban`
- `event.event_registration_action`
- `event.event_registration_action_tree`
- `event.action_registration`
- `event.event_registration_action_stats_from_event`
- `event.action_event_type`
- `event.action_event_view`
- `event.event_stage_action`
- `event.action_event_configuration`
- `event.event_tag_category_action_tree`

## ir.actions.client

- `event.event_barcode_action_main_view`

## ir.actions.report

- `event.action_report_event_registration_full_page_ticket`
- `event.action_report_event_event_full_page_ticket`
- `event.action_report_event_registration_badge`
- `event.action_report_event_event_badge`
- `event.action_report_event_registration_responsive_html_ticket`
- `event.action_report_event_event_attendee_list`
- `event.action_report_event_registration_attendee_list`

## ir.cron

- `event.event_mail_scheduler`

## ir.module.category

- `base.module_category_marketing_events`

## ir.rule

- `event.event_event_company_rule`
- `event.event_registration_company_rule`
- `event.ir_rule_event_event_ticket_company`

## ir.ui.menu

- `event.event_main_menu` — Events
- `event.menu_event_event` — Events
- `event.menu_reporting_events` — Reporting
- `event.menu_event_configuration` — Configuration
- `event.menu_event_type` — Event Templates
- `event.event_stage_menu` — Event Stages
- `event.menu_event_mail_schedulers` — Mail Schedulers
- `event.menu_event_category` — Event Tags Categories
- `event.menu_event_mail_schedulers`
- `event.menu_action_registration` — Attendees
- `event.menu_event_type`
- `event.menu_event_event`
- `event.menu_event_registration_desk` — Registration Desk
- `event.event_stage_menu`
- `event.menu_event_global_settings` — Settings
- `event.menu_event_category`

## ir.ui.view

- `event.event_type_ticket_view_tree_from_type` — on event.type.ticket
- `event.event_type_ticket_view_form_from_type` — on event.type.ticket
- `event.event_type_ticket_view_tree` — on event.type.ticket inherits event_type_ticket_view_tree_from_type
- `event.event_type_ticket_view_form` — on event.type.ticket inherits event_type_ticket_view_form_from_type
- `event.event_event_ticket_view_tree_from_event` — on event.event.ticket
- `event.event_event_ticket_view_form_from_event` — on event.event.ticket
- `event.event_event_ticket_view_kanban_from_event` — on event.event.ticket
- `event.event_event_ticket_view_tree` — on event.event.ticket inherits event_event_ticket_view_tree_from_event
- `event.event_event_ticket_form_view` — on event.event.ticket
- `event.view_event_mail_form` — on event.mail
- `event.view_event_mail_tree` — on event.mail
- `event.view_event_registration_tree` — on event.registration
- `event.view_event_registration_form` — on event.registration
- `event.event_registration_view_kanban` — on event.registration
- `event.view_event_registration_calendar` — on event.registration
- `event.view_event_registration_pivot` — on event.registration
- `event.view_event_registration_graph` — on event.registration
- `event.view_registration_search` — on event.registration
- `event.event_registration_view_search_event_specific` — on event.registration inherits view_registration_search
- `event.view_event_type_form` — on event.type
- `event.view_event_type_tree` — on event.type
- `event.event_type_view_search` — on event.type
- `event.view_event_form` — on event.event
- `event.view_event_tree` — on event.event
- `event.event_event_view_activity` — on event.event
- `event.event_event_view_form_quick_create` — on event.event
- `event.view_event_kanban` — on event.event
- `event.view_event_calendar` — on event.event
- `event.view_event_search` — on event.event
- `event.event_stage_view_form` — on event.stage
- `event.event_stage_view_tree` — on event.stage
- `event.event_report_template_foldable_badge`
- `event.event_report_template_a6_badge`
- `event.event_report_template_four_per_sheet_badge`
- `event.event_registration_report_template_badge`
- `event.event_event_report_template_badge`
- `event.event_report_template_full_page_ticket`
- `event.event_report_full_page_ticket_layout`
- `event.event_registration_report_template_full_page_ticket`
- `event.event_event_report_template_full_page_ticket`
- `event.event_registration_report_template_responsive_html_ticket`
- `event.event_report_template_badge_card`
- `event.event_report_template_formatted_event_address`
- `event.attendee_list`
- `event.event_registration_attendee_list`
- `event.event_event_attendee_list`
- `event.res_config_settings_view_form` — on res.config.settings inherits mail.res_config_settings_view_form
- `event.event_default_descripton`
- `event.res_partner_view_tree` — on res.partner inherits base.view_partner_form
- `event.event_tag_category_view_tree` — on event.tag.category
- `event.event_tag_category_view_form` — on event.tag.category
- `event.event_tag_view_tree` — on event.tag
- `event.event_tag_view_form` — on event.tag

## mail.template

- `event.event_registration_mail_template_badge`
- `event.event_subscription`
- `event.event_reminder`

## report.paperformat

- `event.paperformat_event_badge`
- `event.paperformat_event_full_page_ticket`

## res.groups

- `event.group_event_registration_desk`
- `event.group_event_user`
- `event.group_event_manager`

## res.users

- `base.default_user`
