# mass_mailing — Email Marketing

Depends on: contacts, mail, utm, link_tracker, web_editor, web_kanban_gauge, social_media, web_tour, digest.

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `ir.mail_server` (extends)

- `active_mailing_ids` One2many → `mailing.mailing` “Active mailing using this mail server” (readonly)

## `ir.model` (extends)

- `is_mailing_enabled` Boolean “Mailing Enabled” (compute=_compute_is_mailing_enabled)

## `link.tracker` (extends)

- `mass_mailing_id` Many2one → `mailing.mailing` “Mass Mailing”

## `link.tracker.click` (extends)

- `mailing_trace_id` Many2one → `mailing.trace` “Mail Statistics”
- `mass_mailing_id` Many2one → `mailing.mailing` “Mass Mailing”

Public methods: `add_click`

Extension points: `_prepare_click_values_from_route`

## `mail.mail` (extends)

- `mailing_id` Many2one → `mailing.mailing` “Mass Mailing”
- `mailing_trace_ids` One2many → `mailing.trace` “Statistics”

Extension points: `_get_tracking_url`

## `mail.render.mixin` (extends)


## `mail.thread` (extends)


Public methods: `message_new`, `message_post_with_template`

## `mailing.mailing` (defines)

Mass Mailing

Inherits: `mail.thread`, `mail.activity.mixin`, `mail.render.mixin`, `utm.source.mixin`

- `active` Boolean
- `subject` Char “Subject” (required)
- `preview` Char “Preview”
- `email_from` Char “Send From” (required, store, compute=_compute_email_from)
- `favorite` Boolean “Favorite”
- `favorite_date` Datetime “Favorite Date” (store, compute=_compute_favorite_date)
- `sent_date` Datetime “Sent Date”
- `schedule_type` Selection “Schedule” (required, readonly)
- `schedule_date` Datetime “Scheduled for” (readonly, store, compute=_compute_schedule_date)
- `calendar_date` Datetime “Calendar Date” (store, compute=_compute_calendar_date)
- `body_arch` Html “Body”
- `body_html` Html “Body converted to be sent by mail”
- `is_body_empty` Boolean (compute=_compute_is_body_empty)
- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `keep_archives` Boolean “Keep Archives”
- `campaign_id` Many2one → `utm.campaign` “UTM Campaign” (index)
- `medium_id` Many2one → `utm.medium` “Medium” (store, compute=_compute_medium_id)
- `state` Selection “Status” (required)
- `color` Integer “Color Index”
- `user_id` Many2one → `res.users` “Responsible”
- `mailing_type` Selection “Mailing Type” (required)
- `mailing_type_description` Char “Mailing Type Description” (compute=_compute_mailing_type_description)
- `reply_to_mode` Selection “Reply-To Mode” (store, compute=_compute_reply_to_mode)
- `reply_to` Char “Reply To” (store, compute=_compute_reply_to)
- `mailing_model_real` Char “Recipients Real Model” (compute=_compute_mailing_model_real)
- `mailing_model_id` Many2one → `ir.model` “Recipients Model” (required)
- `mailing_model_name` Char “Recipients Model Name” (readonly, related=mailing_model_id.model)
- `mailing_domain` Char “Domain” (store, compute=_compute_mailing_domain)
- `mail_server_available` Boolean (compute=_compute_mail_server_available)
- `mail_server_id` Many2one → `ir.mail_server` “Mail Server”
- `contact_list_ids` Many2many → `mailing.list` “Mailing Lists”
- `mailing_filter_id` Many2one → `mailing.filter` “Favorite Filter” (store, compute=_compute_mailing_filter_id)
- `mailing_filter_domain` Char “Favorite filter domain” (related=mailing_filter_id.mailing_domain)
- `mailing_filter_count` Integer “# Favorite Filters” (compute=_compute_mailing_filter_count)
- `ab_testing_completed` Boolean (store, related=campaign_id.ab_testing_completed)
- `ab_testing_description` Html “A/B Testing Description” (compute=_compute_ab_testing_description)
- `ab_testing_enabled` Boolean “Allow A/B Testing”
- `ab_testing_mailings_count` Integer (related=campaign_id.ab_testing_mailings_count)
- `ab_testing_pc` Integer “A/B Testing percentage”
- `ab_testing_schedule_datetime` Datetime (related=campaign_id.ab_testing_schedule_datetime)
- `ab_testing_winner_selection` Selection (related=campaign_id.ab_testing_winner_selection)
- `kpi_mail_required` Boolean “KPI mail required”
- `mailing_trace_ids` One2many → `mailing.trace` “Emails Statistics”
- `total` Integer (compute=_compute_total)
- `scheduled` Integer (compute=_compute_statistics)
- `expected` Integer (compute=_compute_statistics)
- `canceled` Integer (compute=_compute_statistics)
- `sent` Integer (compute=_compute_statistics)
- `delivered` Integer (compute=_compute_statistics)
- `opened` Integer (compute=_compute_statistics)
- `clicked` Integer (compute=_compute_statistics)
- `replied` Integer (compute=_compute_statistics)
- `bounced` Integer (compute=_compute_statistics)
- `failed` Integer (compute=_compute_statistics)
- `received_ratio` Integer “Received Ratio” (compute=_compute_statistics)
- `opened_ratio` Integer “Opened Ratio” (compute=_compute_statistics)
- `replied_ratio` Integer “Replied Ratio” (compute=_compute_statistics)
- `bounced_ratio` Integer “Bounced Ratio” (compute=_compute_statistics)
- `clicks_ratio` Integer “Number of Clicks” (compute=_compute_clicks_ratio)
- `next_departure` Datetime “Scheduled date” (compute=_compute_next_departure)
- `warning_message` Char “Warning Message” (compute=_compute_warning_message)

Public methods: `action_cancel`, `action_compare_versions`, `action_duplicate`, `action_fetch_favorites`, `action_launch`, `action_put_in_queue`, `action_remove_favorite`, `action_retry_failed`, `action_schedule`, `action_select_as_winner`, `action_send_mail`, `action_send_winner_mailing`, `action_set_favorite`, `action_test`, `action_view_bounced`, `action_view_clicked`, `action_view_delivered`, `action_view_mailing_contacts`, `action_view_opened`, `action_view_replied`, `action_view_traces_canceled`, `action_view_traces_failed`, `action_view_traces_scheduled`, `action_view_traces_sent`, `convert_links`, `copy`, `create`, `default_get`, `update_opt_out`, `write`

Extension points: `_action_send_statistics`, `_action_view_documents_filtered`, `_action_view_traces_filtered`, `_check_mailing_filter_model`, `_create_ab_testing_utm_campaigns`, `_create_attachments_from_inline_images`, `_get_ab_testing_description_modifying_fields`, `_get_ab_testing_description_values`, `_get_ab_testing_siblings_mailings`, `_get_ab_testing_winner_selection`, `_get_default_ab_testing_campaign_values`, `_get_default_mail_server_id`, `_get_default_mailing_domain`, `_get_image_by_url`, `_get_link_tracker_values`, `_get_mass_mailing_context`, `_get_opt_out_list`, `_get_pretty_mailing_type`, `_get_recipients`, `_get_remaining_recipients`, `_get_seen_list`, `_get_seen_list_extra`, `_get_unsubscribe_oneclick_url`, `_get_unsubscribe_token`, `_get_unsubscribe_url`, `_get_view_url`, `_prepare_statistics_email_values`

## `mailing.contact.subscription` (defines)

Mass Mailing Subscription Information

- `contact_id` Many2one → `mailing.contact` “Contact” (required)
- `list_id` Many2one → `mailing.list` “Mailing List” (required)
- `opt_out` Boolean “Opt Out”
- `unsubscription_date` Datetime “Unsubscription Date”
- `message_bounce` Integer (related=contact_id.message_bounce)
- `is_blacklisted` Boolean (related=contact_id.is_blacklisted)

Public methods: `create`, `write`

## `mailing.contact` (defines)

Mailing Contact

Inherits: `mail.thread.blacklist`

- `name` Char
- `company_name` Char “Company Name”
- `title_id` Many2one → `res.partner.title` “Title”
- `email` Char “Email”
- `list_ids` Many2many → `mailing.list` “Mailing Lists”
- `subscription_list_ids` One2many → `mailing.contact.subscription` “Subscription Information”
- `country_id` Many2one → `res.country` “Country”
- `tag_ids` Many2many → `res.partner.category` “Tags”
- `opt_out` Boolean “Opt Out” (compute=_compute_opt_out)

Public methods: `action_add_to_mailing_list`, `add_to_list`, `copy`, `create`, `default_get`, `get_import_templates`, `get_name_email`, `name_create`

## `mailing.contact.subscription` (defines)

Mass Mailing Subscription Information

- `contact_id` Many2one → `mailing.contact` “Contact” (required)
- `list_id` Many2one → `mailing.list` “Mailing List” (required)
- `opt_out` Boolean “Opt Out”
- `unsubscription_date` Datetime “Unsubscription Date”
- `message_bounce` Integer (related=contact_id.message_bounce)
- `is_blacklisted` Boolean (related=contact_id.is_blacklisted)

Public methods: `create`, `write`

## `mailing.filter` (defines)

Mailing Favorite Filters

- `create_uid` Many2one → `res.users` (readonly, index)
- `name` Char “Filter Name” (required)
- `mailing_domain` Char “Filter Domain” (required)
- `mailing_model_id` Many2one → `ir.model` “Recipients Model” (required)
- `mailing_model_name` Char “Recipients Model Name” (related=mailing_model_id.model)

Extension points: `_check_mailing_domain`

## `mailing.list` (defines)

Mailing List

- `name` Char “Mailing List” (required)
- `active` Boolean
- `contact_count` Integer “Number of Contacts” (compute=_compute_mailing_list_statistics)
- `contact_count_email` Integer “Number of Emails” (compute=_compute_mailing_list_statistics)
- `contact_count_opt_out` Integer “Number of Opted-out” (compute=_compute_mailing_list_statistics)
- `contact_pct_opt_out` Float “Percentage of Opted-out” (compute=_compute_mailing_list_statistics)
- `contact_count_blacklisted` Integer “Number of Blacklisted” (compute=_compute_mailing_list_statistics)
- `contact_pct_blacklisted` Float “Percentage of Blacklisted” (compute=_compute_mailing_list_statistics)
- `contact_pct_bounce` Float “Percentage of Bouncing” (compute=_compute_mailing_list_statistics)
- `contact_ids` Many2many → `mailing.contact` “Mailing Lists”
- `mailing_count` Integer “Number of Mailing” (compute=_compute_mailing_list_count)
- `mailing_ids` Many2many → `mailing.mailing` “Mass Mailings”
- `subscription_ids` One2many → `mailing.contact.subscription` “Subscription Information”
- `is_public` Boolean “Show In Preferences”

Public methods: `action_merge`, `action_open_import`, `action_send_mailing`, `action_view_contacts`, `action_view_contacts_blacklisted`, `action_view_contacts_bouncing`, `action_view_contacts_email`, `action_view_contacts_opt_out`, `action_view_mailings`, `close_dialog`, `copy`, `name_get`, `write`

Extension points: `_get_contact_statistics_fields`, `_get_contact_statistics_joins`

## `mailing.trace` (defines)

Mailing Statistics

- `trace_type` Selection “Type” (required)
- `display_name` Char (compute=_compute_display_name)
- `mail_mail_id` Many2one → `mail.mail` “Mail”
- `mail_mail_id_int` Integer “Mail ID (tech)”
- `email` Char “Email”
- `message_id` Char “Message-ID”
- `medium_id` Many2one (related=mass_mailing_id.medium_id)
- `source_id` Many2one (related=mass_mailing_id.source_id)
- `model` Char “Document model” (required)
- `res_id` Many2oneReference “Document ID”
- `mass_mailing_id` Many2one → `mailing.mailing` “Mailing” (index)
- `campaign_id` Many2one “Campaign” (readonly, store, related=mass_mailing_id.campaign_id)
- `sent_datetime` Datetime “Sent On”
- `open_datetime` Datetime “Opened On”
- `reply_datetime` Datetime “Replied On”
- `trace_status` Selection “Status”
- `failure_type` Selection “Failure type”
- `links_click_ids` One2many → `link.tracker.click` “Links click”
- `links_click_datetime` Datetime “Clicked On”

Public methods: `action_view_contact`, `create`, `set_bounced`, `set_canceled`, `set_clicked`, `set_failed`, `set_opened`, `set_replied`, `set_sent`

## `res.company` (extends)


Extension points: `_get_social_media_links`

## `res.config.settings` (extends)

- `group_mass_mailing_campaign` Boolean “Mailing Campaigns”
- `mass_mailing_outgoing_mail_server` Boolean “Dedicated Server”
- `mass_mailing_mail_server_id` Many2one → `ir.mail_server` “Mail Server”
- `show_blacklist_buttons` Boolean “Blacklist Option when Unsubscribing”
- `mass_mailing_reports` Boolean “24H Stat Mailing Reports”

Public methods: `set_values`

## `res.partner` (extends)


## `res.users` (extends)


Public methods: `systray_get_activities`

## `utm.campaign` (extends)

- `mailing_mail_ids` One2many → `mailing.mailing` “Mass Mailings”
- `mailing_mail_count` Integer “Number of Mass Mailing” (compute=_compute_mailing_mail_count)
- `is_mailing_campaign_activated` Boolean (compute=_compute_is_mailing_campaign_activated)
- `ab_testing_mailings_count` Integer “A/B Test Mailings #” (compute=_compute_mailing_mail_count)
- `ab_testing_completed` Boolean “A/B Testing Campaign Finished”
- `ab_testing_schedule_datetime` Datetime “Send Final On”
- `ab_testing_total_pc` Integer “Total A/B test percentage” (store, compute=_compute_ab_testing_total_pc)
- `ab_testing_winner_selection` Selection “Winner Selection”
- `received_ratio` Integer “Received Ratio” (compute=_compute_statistics)
- `opened_ratio` Integer “Opened Ratio” (compute=_compute_statistics)
- `replied_ratio` Integer “Replied Ratio” (compute=_compute_statistics)
- `bounced_ratio` Integer “Bounced Ratio” (compute=_compute_statistics)

Extension points: `_check_ab_testing_total_pc`, `_get_mailing_recipients`

## `utm.medium` (extends)


## `utm.source` (extends)


## `mailing.trace.report` (defines)

Mass Mailing Statistics

- `name` Char “Mass Mail” (readonly)
- `mailing_type` Selection “Type” (required)
- `campaign` Char “Mailing Campaign” (readonly)
- `scheduled_date` Datetime “Scheduled Date” (readonly)
- `state` Selection “Status” (readonly)
- `email_from` Char “From” (readonly)
- `scheduled` Integer (readonly)
- `sent` Integer (readonly)
- `delivered` Integer (readonly)
- `error` Integer (readonly)
- `opened` Integer (readonly)
- `replied` Integer (readonly)
- `bounced` Integer (readonly)
- `canceled` Integer (readonly)
- `clicked` Integer (readonly)

Public methods: `init`

## `mail.compose.message` (extends)

- `mass_mailing_id` Many2one → `mailing.mailing` “Mass Mailing”
- `campaign_id` Many2one → `utm.campaign` “Mass Mailing Campaign”
- `mass_mailing_name` Char “Mass Mailing Name”
- `mailing_list_ids` Many2many → `mailing.list` “Mailing List”

Public methods: `get_mail_values`

Extension points: `_get_done_emails`, `_get_optout_emails`

## `mailing.contact.import` (defines)

Mailing Contact Import

- `mailing_list_ids` Many2many → `mailing.list` “Lists”
- `contact_list` Text “Contact List”

Public methods: `action_import`, `action_open_base_import`

## `mailing.contact.to.list` (defines)

Add Contacts to Mailing List

- `contact_ids` Many2many → `mailing.contact` “Contacts”
- `mailing_list_id` Many2one → `mailing.list` “Mailing List” (required)

Public methods: `action_add_contacts`, `action_add_contacts_and_send_mailing`

## `mailing.list.merge` (defines)

Merge Mass Mailing List

- `src_list_ids` Many2many → `mailing.list` “Mailing Lists”
- `dest_list_id` Many2one → `mailing.list` “Destination Mailing List”
- `merge_options` Selection (required)
- `new_list_name` Char “New Mailing List Name”
- `archive_src_lists` Boolean “Archive source mailing lists”

Public methods: `action_mailing_lists_merge`, `default_get`

## `mailing.mailing.schedule.date` (defines)

schedule a mailing

- `schedule_date` Datetime “Scheduled for”
- `mass_mailing_id` Many2one → `mailing.mailing` (required)

Public methods: `action_schedule_date`

## `mailing.mailing.test` (defines)

Sample Mail Wizard

- `email_to` Text “Recipients” (required)
- `mass_mailing_id` Many2one → `mailing.mailing` “Mailing” (required)

Public methods: `send_mail_test`
