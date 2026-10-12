# mass_mailing_sms — SMS Marketing

Depends on: portal, mass_mailing, sms.

## `mailing.contact` (extends)

Inherits: `mail.thread.phone`

- `mobile` Char “Mobile”

## `mailing.list` (extends)

- `contact_count_sms` Integer “SMS Contacts” (compute=_compute_mailing_list_statistics)

Public methods: `action_send_mailing_sms`, `action_view_contacts_sms`, `action_view_mailings`

Extension points: `_get_contact_statistics_fields`, `_get_contact_statistics_joins`

## `mailing.mailing` (extends)

- `mailing_type` Selection
- `sms_subject` Char “Title” (related=subject)
- `body_plaintext` Text “SMS Body” (store, compute=_compute_body_plaintext)
- `sms_template_id` Many2one → `sms.template` “SMS Template”
- `sms_has_insufficient_credit` Boolean “Insufficient IAP credits” (compute=_compute_sms_has_iap_failure)
- `sms_has_unregistered_account` Boolean “Unregistered IAP account” (compute=_compute_sms_has_iap_failure)
- `sms_force_send` Boolean “Send Directly”
- `sms_allow_unsubscribe` Boolean “Include opt-out link”
- `ab_testing_sms_winner_selection` Selection (related=campaign_id.ab_testing_sms_winner_selection)
- `ab_testing_mailings_sms_count` Integer (related=campaign_id.ab_testing_mailings_sms_count)

Public methods: `action_buy_sms_credits`, `action_retry_failed`, `action_retry_failed_sms`, `action_send_sms`, `action_test`, `convert_links`, `create`, `default_get`, `get_sms_link_replacements_placeholders`

Extension points: `_action_send_mail`, `_action_view_traces_filtered`, `_get_ab_testing_description_modifying_fields`, `_get_ab_testing_description_values`, `_get_ab_testing_siblings_mailings`, `_get_ab_testing_winner_selection`, `_get_default_ab_testing_campaign_values`, `_get_opt_out_list_sms`, `_get_pretty_mailing_type`, `_get_seen_list_sms`, `_prepare_statistics_email_values`

## `mailing.trace` (extends)

- `trace_type` Selection
- `sms_id` Many2one → `sms.sms` “SMS” (compute=_compute_sms_id)
- `sms_id_int` Integer “SMS ID”
- `sms_tracker_ids` One2many → `sms.tracker` “SMS Trackers”
- `sms_number` Char “Number”
- `sms_code` Char “Code”
- `failure_type` Selection

Public methods: `create`, `fields_get`

Extension points: `_get_random_code`

## `res.users` (extends)


Extension points: `_get_activity_groups`

## `sms.sms` (extends)

- `mailing_id` Many2one → `mailing.mailing` “Mass Mailing”
- `mailing_trace_ids` One2many → `mailing.trace` “Statistics”

## `sms.tracker` (extends)

- `mailing_trace_id` Many2one → `mailing.trace`

Extension points: `_action_update_from_provider_error`, `_action_update_from_sms_state`

## `utm.campaign` (extends)

- `mailing_sms_ids` One2many → `mailing.mailing` “Mass SMS”
- `mailing_sms_count` Integer “Number of Mass SMS” (compute=_compute_mailing_sms_count)
- `ab_testing_mailings_sms_count` Integer “A/B Test Mailings SMS #” (compute=_compute_mailing_sms_count)
- `ab_testing_sms_winner_selection` Selection “SMS Winner Selection”

Public methods: `action_create_mass_sms`, `action_redirect_to_mailing_sms`

## `utm.medium` (extends)


Public methods: `SELF_REQUIRED_UTM_MEDIUMS_REF`

## `mailing.sms.test` (defines)

Test SMS Mailing

- `numbers` Text “Number(s)” (required)
- `mailing_id` Many2one → `mailing.mailing` “Mailing” (required)

Public methods: `action_send_sms`

Extension points: `_prepare_test_trace_values`

## `sms.composer` (extends)

- `mass_sms_allow_unsubscribe` Boolean “Include opt-out link”
- `mailing_id` Many2one → `mailing.mailing` “Mailing”
- `utm_campaign_id` Many2one → `utm.campaign` “Campaign”

Extension points: `_get_done_record_ids`, `_get_optout_record_ids`, `_get_unsubscribe_info`, `_get_unsubscribe_url`, `_prepare_body_values`, `_prepare_mass_sms`, `_prepare_mass_sms_trace_values`, `_prepare_mass_sms_values`
