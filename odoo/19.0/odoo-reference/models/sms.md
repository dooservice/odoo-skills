# sms — SMS gateway

Depends on: base, iap_mail, mail, phone_validation.

## `iap.account` (extends)

- `sender_name` Char (readonly)

Public methods: `action_open_registration_wizard`, `action_open_sender_name_wizard`

Extension points: `_get_account_info`

## `ir.actions.server` (extends)

- `state` Selection
- `sms_template_id` Many2one → `sms.template` (store, compute=_compute_sms_template_id)
- `sms_method` Selection “Send SMS As” (store, compute=_compute_sms_method)

Extension points: `_get_warning_messages`

## `ir.model` (extends)

- `is_mail_thread_sms` Boolean “Mail Thread SMS” (compute=_compute_is_mail_thread_sms)

## `mail.followers` (extends)


Extension points: `_get_recipient_data`

## `mail.message` (extends)

- `message_type` Selection
- `has_sms_error` Boolean “Has SMS error” (compute=_compute_has_sms_error)

## `mail.notification` (extends)

- `notification_type` Selection
- `sms_id_int` Integer “SMS ID”
- `sms_id` Many2one → `sms.sms` “SMS” (compute=_compute_sms_id)
- `sms_tracker_ids` One2many → `sms.tracker` “SMS Trackers”
- `sms_number` Char “SMS Number”
- `failure_type` Selection

## `mail.thread` (extends)

- `message_has_sms_error` Boolean “SMS Delivery error” (compute=_compute_message_has_sms_error)

Public methods: `message_post`, `notify_cancel_by_type`

Extension points: `_get_notify_valid_parameters`

## `base` (extends)


## `res.company` (extends)


Extension points: `_get_sms_api_class`

## `sms.sms` (defines)

Outgoing SMS

- `uuid` Char “UUID” (readonly)
- `number` Char “Number”
- `body` Text
- `partner_id` Many2one → `res.partner`
- `mail_message_id` Many2one → `mail.message` (index)
- `state` Selection (required, readonly)
- `failure_type` Selection
- `sms_tracker_id` Many2one → `sms.tracker` “SMS trackers” (compute=_compute_sms_tracker_id)
- `to_delete` Boolean “Marked for deletion”

Public methods: `action_set_canceled`, `action_set_error`, `action_set_outgoing`, `create`, `resend_failed`, `send`

Extension points: `_get_send_batch_size`, `_get_sms_company`

## `sms.template` (defines)

SMS Templates

Inherits: `mail.render.mixin`, `template.reset.mixin`

- `name` Char “Name”
- `model_id` Many2one → `ir.model` “Applies to” (required)
- `model` Char “Related Document Model” (readonly, store, index, related=model_id.model)
- `body` Char “Body” (required)
- `sidebar_action_id` Many2one → `ir.actions.act_window` (readonly)

Public methods: `action_create_sidebar_action`, `action_unlink_sidebar_action`, `copy_data`, `default_get`, `unlink`

## `sms.tracker` (defines)

Link SMS to mailing/sms tracking models

- `sms_uuid` Char “SMS uuid” (required)
- `mail_notification_id` Many2one → `mail.notification`

Extension points: `_action_update_from_provider_error`, `_action_update_from_sms_state`

## `sms.account.code` (defines)

SMS Account Verification Code Wizard

- `account_id` Many2one → `iap.account` (required)
- `verification_code` Char (required)

Public methods: `action_register`

## `sms.account.phone` (defines)

SMS Account Registration Phone Number Wizard

- `account_id` Many2one → `iap.account` (required)
- `phone_number` Char (required)

Public methods: `action_send_verification_code`

## `sms.account.sender` (defines)

SMS Account Sender Name Wizard

- `account_id` Many2one → `iap.account` (required)
- `sender_name` Char

Public methods: `action_set_sender_name`

Extension points: `_check_sender_name`

## `sms.composer` (defines)

Send SMS Wizard

- `composition_mode` Selection “Composition Mode” (required, store, compute=_compute_composition_mode)
- `res_model` Char “Document Model Name”
- `res_model_description` Char “Document Model Description” (compute=_compute_res_model_description)
- `res_id` Integer “Document ID”
- `res_ids` Char “Document IDs”
- `res_ids_count` Integer “Visible records count” (compute=_compute_res_ids_count)
- `comment_single_recipient` Boolean “Single Mode” (compute=_compute_comment_single_recipient)
- `mass_keep_log` Boolean “Keep a note on document”
- `mass_force_send` Boolean “Send directly”
- `use_exclusion_list` Boolean “Use Exclusion List”
- `recipient_valid_count` Integer “# Valid recipients” (compute=_compute_recipients)
- `recipient_invalid_count` Integer “# Invalid recipients” (compute=_compute_recipients)
- `recipient_single_description` Text “Recipients (Partners)” (compute=_compute_recipient_single_non_stored)
- `recipient_single_number` Char “Stored Recipient Number” (compute=_compute_recipient_single_non_stored)
- `recipient_single_number_itf` Char “Recipient Number” (store, compute=_compute_recipient_single_stored)
- `recipient_single_valid` Boolean “Is valid” (compute=_compute_recipient_single_valid)
- `number_field_name` Char “Number Field”
- `numbers` Char “Recipients (Numbers)”
- `sanitized_numbers` Char “Sanitized Number” (compute=_compute_sanitized_numbers)
- `template_id` Many2one → `sms.template` “Use Template”
- `body` Text “Message” (required, store, compute=_compute_body)

Public methods: `action_send_sms`, `action_send_sms_mass_now`, `default_get`

Extension points: `_action_send_sms`, `_action_send_sms_comment`, `_action_send_sms_comment_single`, `_action_send_sms_mass`, `_action_send_sms_numbers`, `_get_additional_render_context`, `_get_blacklist_record_ids`, `_get_composer_values`, `_get_done_record_ids`, `_get_optout_record_ids`, `_get_records`, `_prepare_body_values`, `_prepare_log_body_values`, `_prepare_mass_log_values`, `_prepare_mass_sms`, `_prepare_mass_sms_values`, `_prepare_recipient_values`

## `sms.template.preview` (defines)

SMS Template Preview

- `sms_template_id` Many2one → `sms.template` (required)
- `lang` Selection “Template Preview Language”
- `model_id` Many2one → `ir.model` (related=sms_template_id.model_id)
- `body` Char “Body” (compute=_compute_sms_template_fields)
- `resource_ref` Reference “Record reference”
- `no_record` Boolean “No Record” (compute=_compute_no_record)

Public methods: `default_get`

## `sms.template.reset` (defines)

SMS Template Reset

- `template_ids` Many2many → `sms.template`

Public methods: `reset_template`
