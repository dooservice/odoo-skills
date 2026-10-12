# mass_mailing — Email Marketing

Depends on: contacts, mail, html_builder, utm, link_tracker, social_media, web_tour, digest.

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `ir.mail_server` (extends)

- `active_mailing_ids` One2many → `mailing.mailing` “Active mailing using this mail server” (readonly)

Extension points: `_check_owner_user_id_not_mass_mailing`

## `ir.model` (extends)

- `is_mailing_enabled` Boolean “Mailing Enabled” (compute=_compute_is_mailing_enabled)

## `ir.ui.view` (extends)

- `technical_usage` Selection

## `link.tracker` (extends)

- `mass_mailing_id` Many2one → `mailing.mailing` “Mass Mailing”

## `link.tracker.click` (extends)

- `mailing_trace_id` Many2one → `mailing.trace` “Mail Statistics”
- `mass_mailing_id` Many2one → `mailing.mailing` “Mass Mailing”
- `email` Char “Email” (related=mailing_trace_id.email)
- `url` Char “URL” (related=link_id.url)

Public methods: `add_click`

Extension points: `_action_view_mailing_statistics`, `_prepare_click_values_from_route`

## `mail.blacklist` (extends)

- `opt_out_reason_id` Many2one → `mailing.subscription.optout` “Opt-out Reason”

## `mail.mail` (extends)

- `mailing_id` Many2one → `mailing.mailing` “Mass Mailing”
- `mailing_trace_ids` One2many → `mailing.trace` “Statistics”

Extension points: `_get_tracking_url`, `_prepare_outgoing_body`, `_prepare_outgoing_list`

## `mail.render.mixin` (extends)


## `mail.thread` (extends)


Public methods: `message_mail_with_source`, `message_new`, `message_post_with_source`

## `mailing.mailing` (defines)

Mass Mailing

Inherits: `mail.thread`, `mail.activity.mixin`, `mail.render.mixin`

- `active` Boolean
- `subject` Char “Subject” (required)
- `preview` Char “Preview”
- `email_from` Char “Send From” (store, compute=_compute_email_from)
- `is_template` Boolean “Is Template”
- `sent_date` Datetime “Sent Date”
- `schedule_type` Selection “Schedule” (required)
- `schedule_date` Datetime “Scheduled for” (store, compute=_compute_schedule_date)
- `calendar_date` Datetime “Calendar Date” (store, compute=_compute_calendar_date)
- `body_arch` Html “Body”
- `body_html` Html “Body converted to be sent by mail”
- `is_body_empty` Boolean (compute=_compute_is_body_empty)
- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `keep_archives` Boolean “Keep Archives”
- `campaign_id` Many2one → `utm.campaign` “UTM Campaign” (index)
- `medium_id` Many2one → `utm.medium` “Medium” (store, compute=_compute_medium_id)
- `source_id` Many2one → `utm.source` “Source” (store, compute=_compute_source_id)
- `state` Selection “Status” (required)
- `color` Integer “Color Index”
- `user_id` Many2one → `res.users` “Responsible”
- `mailing_type` Selection “Mailing Type” (required)
- `mailing_type_description` Char “Mailing Type Description” (compute=_compute_mailing_type_description)
- `reply_to_mode` Selection “Reply-To Mode” (store, compute=_compute_reply_to_mode)
- `reply_to` Char “Reply To” (store, compute=_compute_reply_to)
- `mailing_model_real` Char “Recipients Real Model” (compute=_compute_mailing_model_real)
- `mailing_model_id` Many2one → `ir.model` “Recipients Model” (required, store, compute=_compute_mailing_model_id)
- `mailing_model_name` Char “Recipients Model Name” (readonly, related=mailing_model_id.model)
- `mailing_on_mailing_list` Boolean “Based on Mailing Lists” (compute=_compute_mailing_on_mailing_list)
- `mailing_domain` Char “Domain” (store, compute=_compute_mailing_domain)
- `mail_server_available` Boolean (compute=_compute_mail_server_available)
- `mail_server_id` Many2one → `ir.mail_server` “Mail Server”
- `contact_list_ids` Many2many → `mailing.list` “Mailing Lists”
- `use_exclusion_list` Boolean “Use Exclusion List” (store, compute=_compute_use_exclusion_list)
- `recipients_count` Integer “# Of Recipients” (compute=_compute_recipients_count)
- `mailing_filter_ids` Many2many → `mailing.filter` “Dynamic Lists” (store, compute=_compute_mailing_filter_ids)
- `ab_testing_completed` Boolean (related=campaign_id.ab_testing_completed)
- `ab_testing_description` Html “A/B Testing Description” (compute=_compute_ab_testing_description)
- `ab_testing_enabled` Boolean “Allow A/B Testing”
- `ab_testing_is_winner_mailing` Boolean “Is the Winner of its Campaign” (compute=_compute_ab_testing_is_winner_mailing)
- `ab_testing_mailings_count` Integer (related=campaign_id.ab_testing_mailings_count)
- `ab_testing_pc` Integer “A/B Testing percentage”
- `ab_testing_schedule_datetime` Datetime (related=campaign_id.ab_testing_schedule_datetime)
- `ab_testing_version_name` Char “A/B Testing Version”
- `ab_testing_winner_selection` Selection (related=campaign_id.ab_testing_winner_selection)
- `is_ab_test_sent` Boolean (compute=_compute_is_ab_test_sent)
- `kpi_mail_required` Boolean “KPI mail required”
- `mailing_trace_ids` One2many → `mailing.trace` “Emails Statistics”
- `total` Integer (compute=_compute_total)
- `scheduled` Integer (compute=_compute_statistics)
- `expected` Integer (compute=_compute_statistics)
- `canceled` Integer (compute=_compute_statistics)
- `sent` Integer (compute=_compute_statistics)
- `process` Integer (compute=_compute_statistics)
- `pending` Integer (compute=_compute_statistics)
- `delivered` Integer (compute=_compute_statistics)
- `opened` Integer (compute=_compute_statistics)
- `clicked` Integer (compute=_compute_statistics)
- `replied` Integer (compute=_compute_statistics)
- `bounced` Integer (compute=_compute_statistics)
- `failed` Integer (compute=_compute_statistics)
- `received_ratio` Float “Received Ratio” (compute=_compute_statistics)
- `canceled_ratio` Float “Cancelled Ratio” (compute=_compute_statistics)
- `opened_ratio` Float “Opened Ratio” (compute=_compute_statistics)
- `replied_ratio` Float “Replied Ratio” (compute=_compute_statistics)
- `bounced_ratio` Float “Bounced Ratio” (compute=_compute_statistics)
- `clicks_ratio` Float “Number of Clicks” (compute=_compute_clicks_ratio)
- `link_trackers_count` Integer “Link Trackers Count” (compute=_compute_link_trackers_count)
- `next_departure` Datetime “Scheduled date” (compute=_compute_next_departure)
- `next_departure_is_past` Boolean (compute=_compute_next_departure)
- `warning_message` Char “Warning Message” (compute=_compute_warning_message)

Public methods: `action_cancel`, `action_compare_versions`, `action_duplicate`, `action_fetch_templates`, `action_import_mailing_contacts`, `action_launch`, `action_new_mailing_from_template`, `action_preview`, `action_put_in_queue`, `action_reload`, `action_retry_failed`, `action_save_as_template`, `action_schedule`, `action_select_as_winner`, `action_send_mail`, `action_send_winner_mailing`, `action_test`, `action_view_bounced`, `action_view_clicked`, `action_view_delivered`, `action_view_link_trackers`, `action_view_opened`, `action_view_replied`, `action_view_traces`, `action_view_traces_canceled`, `action_view_traces_failed`, `action_view_traces_process`, `action_view_traces_scheduled`, `action_view_traces_sent`, `convert_links`, `copy_data`, `create`, `default_get`, `write`

Extension points: `_action_send_mail`, `_action_send_statistics`, `_action_view_traces`, `_action_view_traces_filtered`, `_check_is_template_mailing_type`, `_check_mailing_filter_model`, `_create_ab_testing_utm_campaigns`, `_create_attachments_from_inline_images`, `_get_ab_testing_description_modifying_fields`, `_get_ab_testing_description_values`, `_get_ab_testing_siblings_mailings`, `_get_ab_testing_winner_selection`, `_get_default_ab_testing_campaign_values`, `_get_default_mail_server_id`, `_get_default_mailing_domain`, `_get_image_by_url`, `_get_link_tracker_values`, `_get_mass_mailing_context`, `_get_opt_out_list`, `_get_pretty_mailing_type`, `_get_recipient_base_url`, `_get_recipients`, `_get_recipients_domain`, `_get_remaining_recipients`, `_get_seen_list`, `_get_seen_list_extra`, `_get_unsubscribe_oneclick_url`, `_get_unsubscribe_url`, `_get_view_url`, `_prepare_statistics_email_values`

## `mailing.contact` (defines)

Mailing Contact

Inherits: `mail.thread.blacklist`, `properties.base.definition.mixin`

- `name` Char “Name” (store, compute=_compute_name)
- `first_name` Char “First Name”
- `last_name` Char “Last Name”
- `company_name` Char “Company Name”
- `email` Char “Email”
- `list_ids` Many2many → `mailing.list` “Mailing Lists”
- `subscription_ids` One2many → `mailing.subscription` “Subscription Information”
- `country_id` Many2one → `res.country` “Country”
- `tag_ids` Many2many → `res.partner.category` “Tags”
- `opt_out` Boolean “Opt Out” (compute=_compute_opt_out)
- `mailing_count` Integer “Number of Mailing” (compute=_compute_statistics)
- `received_ratio` Float “Received Ratio” (compute=_compute_statistics)
- `opened_ratio` Float “Opened Ratio” (compute=_compute_statistics)
- `replied_ratio` Float “Replied Ratio” (compute=_compute_statistics)
- `clicks_ratio` Float “Clicks Ratio” (compute=_compute_clicks_ratio)
- `last_opened_datetime` Datetime “Last Opened On”
- `last_clicked_datetime` Datetime “Last Clicked On”
- `last_replied_datetime` Datetime “Last Replied On”
- `partner_id` Many2one → `res.partner` “Contact”

Public methods: `action_add_to_mailing_list`, `action_import`, `action_open_base_import`, `action_view_clicked`, `action_view_mailings`, `action_view_opened`, `action_view_received`, `action_view_replied`, `add_to_list`, `copy`, `create`, `default_get`, `fields_get`, `get_import_templates`, `name_create`

Extension points: `_get_context_active_list_id`, `_get_sort_key`

## `mailing.filter` (defines)

Mailing Dynamic List

- `create_uid` Many2one → `res.users` (readonly, index)
- `name` Char “List Name” (required)
- `active` Boolean
- `color` Integer “Color”
- `mailing_domain` Char “Filter Domain” (required)
- `mailing_model_id` Many2one → `ir.model` “Recipients Model” (required)
- `mailing_model_name` Char “Recipients Model Name” (related=mailing_model_id.model)
- `mailing_count` Integer “Number of Mailing” (compute=_compute_mailing_count)

Public methods: `action_send_mailing`, `action_view_mailings`, `action_view_recipients`

Extension points: `_check_mailing_domain`

## `mailing.list` (defines)

Mailing List

- `name` Char “Mailing List” (required)
- `active` Boolean
- `color` Integer “Color”
- `contact_count` Integer “Number of Contacts” (compute=_compute_mailing_list_statistics)
- `contact_count_email` Integer “Number of Emails” (compute=_compute_mailing_list_statistics)
- `contact_count_opt_out` Integer “Number of Opted-out” (compute=_compute_mailing_list_statistics)
- `contact_pct_opt_out` Float “Percentage of Opted-out” (compute=_compute_mailing_list_statistics)
- `contact_count_blacklisted` Integer “Number of Blacklisted” (compute=_compute_mailing_list_statistics)
- `contact_pct_blacklisted` Float “Percentage of Blacklisted” (compute=_compute_mailing_list_statistics)
- `contact_pct_bounce` Float “Percentage of Bouncing” (compute=_compute_mailing_list_statistics)
- `contact_ids` Many2many → `mailing.contact` “Mailing Lists”
- `mailing_count` Integer “Number of Mailing” (compute=_compute_mailing_count)
- `mailing_ids` Many2many → `mailing.mailing` “Mass Mailings”
- `subscription_ids` One2many → `mailing.subscription` “Subscription Information”
- `is_public` Boolean “Show In Preferences”

Public methods: `action_mailing_lists_merge`, `action_merge`, `action_open_import`, `action_send_mailing`, `action_view_contacts`, `action_view_contacts_blacklisted`, `action_view_contacts_bouncing`, `action_view_contacts_email`, `action_view_contacts_opt_out`, `action_view_mailings`, `write`

Extension points: `_get_contact_statistics_fields`, `_get_contact_statistics_joins`, `_post_subscribe_hook`

## `mailing.subscription` (defines)

Mailing List Subscription

- `contact_id` Many2one → `mailing.contact` “Contact” (required)
- `list_id` Many2one → `mailing.list` “Mailing List” (required, index)
- `opt_out` Boolean “Opt Out”
- `opt_out_reason_id` Many2one → `mailing.subscription.optout` “Reason”
- `opt_out_datetime` Datetime “Unsubscription Date” (store, compute=_compute_opt_out_datetime)
- `message_bounce` Integer (related=contact_id.message_bounce)
- `is_blacklisted` Boolean (related=contact_id.is_blacklisted)

Public methods: `create`, `open_mailing_contact`, `write`

## `mailing.subscription.optout` (defines)

Mailing Subscription Reason

- `name` Char “Reason”
- `sequence` Integer “Sequence”
- `is_feedback` Boolean “Ask For Feedback”

## `mailing.trace` (defines)

Mailing Statistics

- `trace_type` Selection “Type” (required)
- `is_test_trace` Boolean “Generated for testing”
- `mail_mail_id` Many2one → `mail.mail` “Mail”
- `mail_mail_id_int` Integer “Mail ID (tech)”
- `email` Char “Email”
- `message_id` Char “Message-ID”
- `medium_id` Many2one (related=mass_mailing_id.medium_id)
- `source_id` Many2one (related=mass_mailing_id.source_id)
- `model` Char “Document model” (required, index)
- `res_id` Many2oneReference “Document ID” (index)
- `mass_mailing_id` Many2one → `mailing.mailing` “Mailing” (index)
- `campaign_id` Many2one “Campaign” (readonly, store, related=mass_mailing_id.campaign_id)
- `sent_datetime` Datetime “Sent On”
- `open_datetime` Datetime “Opened On”
- `reply_datetime` Datetime “Replied On”
- `trace_status` Selection “Status”
- `failure_type` Selection “Failure type”
- `failure_reason` Text “Failure reason” (readonly)
- `links_click_ids` One2many → `link.tracker.click` “Links click”
- `links_click_datetime` Datetime “Clicked On”

Public methods: `action_retry_failed`, `action_view_contact`, `create`, `set_bounced`, `set_canceled`, `set_clicked`, `set_failed`, `set_opened`, `set_replied`, `set_sent`

Extension points: `_action_view_mailing_statistics_filtered`

## `res.company` (extends)


Public methods: `get_mailing_snippet_info`, `update_social_links`

Extension points: `_get_social_media_links`

## `res.config.settings` (extends)

- `group_mass_mailing_campaign` Boolean “Mailing Campaigns”
- `mass_mailing_outgoing_mail_server` Boolean “Dedicated Server”
- `mass_mailing_mail_server_id` Many2one → `ir.mail_server` “Mail Server”
- `show_blacklist_buttons` Boolean “Blacklist Option when Unsubscribing”
- `mass_mailing_reports` Boolean “24H Stat Mailing Reports”
- `mass_mailing_split_contact_name` Boolean “Split First and Last Name”

Public methods: `get_values`, `set_values`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.partner` (extends)

- `mailing_contact_id` Many2one → `mailing.contact` “Contact” (compute=_compute_mailing_contact_id)
- `mailing_contact_ids` One2many → `mailing.contact` “Contacts”

Public methods: `action_open_mailing_contacts`

## `res.users` (extends)


Extension points: `_get_activity_groups`

## `utm.campaign` (extends)

- `mailing_mail_ids` One2many → `mailing.mailing` “Mass Mailings”
- `mailing_mail_count` Integer “Number of Mass Mailing” (compute=_compute_mailing_mail_count)
- `is_mailing_campaign_activated` Boolean (compute=_compute_is_mailing_campaign_activated)
- `ab_testing_mailings_count` Integer “A/B Test Mailings #” (compute=_compute_mailing_mail_count)
- `ab_testing_completed` Boolean “A/B Testing Campaign Finished” (readonly, store, compute=_compute_ab_testing_completed)
- `ab_testing_winner_mailing_id` Many2one → `mailing.mailing`
- `ab_testing_schedule_datetime` Datetime “Send Final On”
- `ab_testing_winner_selection` Selection “Winner Selection”
- `received_ratio` Float “Received Ratio” (compute=_compute_statistics)
- `opened_ratio` Float “Opened Ratio” (compute=_compute_statistics)
- `replied_ratio` Float “Replied Ratio” (compute=_compute_statistics)
- `bounced_ratio` Float “Bounced Ratio” (compute=_compute_statistics)

Extension points: `_get_mailing_recipients`

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
- `processing` Integer (readonly)
- `pending` Integer (readonly)
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
- `mass_mailing_create` Boolean “Create Mass Mailing”
- `mailing_list_ids` Many2many → `mailing.list` “Mailing List”

Extension points: `_action_send_mail`, `_get_done_emails`, `_get_optout_emails`, `_prepare_mail_values`, `_prepare_mail_values_mailing_traces`, `_prepare_mailing_values`

## `mailing.contact.import` (defines)

Mailing Contact Import

- `mailing_list_ids` Many2many → `mailing.list` “Lists”
- `contact_list` Text “Contact List”

Public methods: `action_import`, `action_open_base_import`

## `mailing.contact.to.list` (defines)

Add (Mailing) Contacts to Mailing List

- `contact_ids` Many2many → `mailing.contact` “Mailing Contacts”
- `partner_ids` Many2many → `res.partner` “Contacts”
- `mailing_list_ids` Many2many → `mailing.list` “Mailing Lists” (required)

Public methods: `action_add_contacts`

Extension points: `_action_add_mailing_contacts`, `_action_add_res_partners`, `_get_no_contact_details_message`

## `mailing.mailing.schedule.date` (defines)

schedule a mailing

- `schedule_date` Datetime “Scheduled for”
- `mass_mailing_id` Many2one → `mailing.mailing` (required)

Public methods: `action_schedule_date`

## `mailing.mailing.test` (defines)

Sample Mail Wizard

- `email_to` Text “Recipients” (required)
- `mass_mailing_id` Many2one → `mailing.mailing` “Mailing” (required)
- `email_from` Char “From” (compute=_compute_mailing_preview)
- `subject` Char “Subject” (compute=_compute_mailing_preview)
- `preview_text` Char “Preview Text” (compute=_compute_mailing_preview)
- `reply_to` Char “Reply To” (compute=_compute_mailing_preview)
- `body_html` Html “Preview Body” (compute=_compute_mailing_preview)
- `preview_record_ref` Reference “Preview for” (store, compute=_compute_preview_record_ref)

Public methods: `send_mail_test`

Extension points: `_get_model_selection`
