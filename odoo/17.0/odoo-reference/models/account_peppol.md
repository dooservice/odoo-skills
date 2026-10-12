# account_peppol — Peppol

Depends on: account_edi_proxy_client, account_edi_ubl_cii.

## `account_edi_proxy_client.user` (extends)

- `peppol_verification_code` Char “SMS verification code”
- `proxy_type` Selection

Extension points: `_get_company_details`, `_get_peppol_proxy_endpoint`, `_get_peppol_proxy_types`, `_get_proxy_identification`, `_get_proxy_urls`, `_get_type_code`

## `account.journal` (extends)

- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `is_peppol_journal` Boolean “Account used for Peppol”

Public methods: `action_peppol_ready_moves`, `peppol_get_message_status`, `peppol_get_new_documents`

Extension points: `_check_type_for_peppol_journal`

## `account.move` (extends)

- `peppol_message_uuid` Char “PEPPOL message ID”
- `peppol_move_state` Selection “PEPPOL status” (store, compute=_compute_peppol_move_state)
- `peppol_is_demo_uuid` Boolean (compute=_compute_peppol_is_demo_uuid)
- `peppol_is_sent` Boolean (compute=_compute_peppol_is_sent)

Public methods: `action_cancel_peppol_documents`, `fields_get`

## `res.company` (extends)

- `account_peppol_contact_email` Char “Primary contact email” (store, compute=_compute_account_peppol_contact_email)
- `account_peppol_migration_key` Char “Migration Key”
- `account_peppol_phone_number` Char “Mobile number (for validation)” (store, compute=_compute_account_peppol_phone_number)
- `account_peppol_proxy_state` Selection “PEPPOL status” (required)
- `is_account_peppol_participant` Boolean “PEPPOL Participant”
- `peppol_eas` Selection (related=partner_id.peppol_eas)
- `peppol_endpoint` Char (related=partner_id.peppol_endpoint)
- `peppol_purchase_journal_id` Many2one → `account.journal` “PEPPOL Purchase Journal” (store, compute=_compute_peppol_purchase_journal_id)
- `account_peppol_edi_user` Many2one → `account_edi_proxy_client.user` (compute=_compute_account_peppol_edi_user)

Public methods: `create`, `write`

Extension points: `_check_account_peppol_phone_number`, `_check_peppol_endpoint`, `_check_peppol_endpoint_number`, `_check_peppol_purchase_journal_id`, `_get_peppol_edi_mode`, `_get_peppol_proxy_type`

## `res.config.settings` (extends)

- `account_peppol_edi_user` Many2one → `account_edi_proxy_client.user` “EDI user” (compute=_compute_account_peppol_edi_user)
- `account_peppol_contact_email` Char (related=company_id.account_peppol_contact_email)
- `account_peppol_eas` Selection (related=company_id.peppol_eas)
- `account_peppol_edi_identification` Char (related=account_peppol_edi_user.edi_identification)
- `account_peppol_endpoint` Char (related=company_id.peppol_endpoint)
- `account_peppol_endpoint_warning` Char “Warning” (compute=_compute_account_peppol_endpoint_warning)
- `account_peppol_migration_key` Char (related=company_id.account_peppol_migration_key)
- `account_peppol_phone_number` Char (related=company_id.account_peppol_phone_number)
- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `account_peppol_purchase_journal_id` Many2one (related=company_id.peppol_purchase_journal_id)
- `account_peppol_verification_code` Char (related=account_peppol_edi_user.peppol_verification_code)
- `is_account_peppol_participant` Boolean “Use PEPPOL” (related=company_id.is_account_peppol_participant)
- `account_peppol_edi_mode` Selection (compute=_compute_account_peppol_edi_mode)
- `account_peppol_mode_constraint` Selection (compute=_compute_account_peppol_mode_constraint)
- `peppol_use_parent_company` Boolean (compute=_compute_peppol_use_parent_company)

Public methods: `action_open_peppol_form`, `button_cancel_peppol_registration`, `button_check_peppol_verification_code`, `button_create_peppol_proxy_user`, `button_create_peppol_proxy_user_sender_only`, `button_deregister_peppol_participant`, `button_migrate_peppol_registration`, `button_peppol_register_sender_as_receiver`, `button_peppol_reregister`, `button_peppol_reset_to_sender`, `button_register_with_kyc`, `button_send_peppol_verification_code`, `button_update_peppol_user_data`, `fields_get`

Extension points: `_check_mandatory_peppol_user_data`, `_get_peppol_proxy_type`

## `res.partner` (extends)

- `account_peppol_is_endpoint_valid` Boolean “PEPPOL endpoint validity” (store, compute=_compute_account_peppol_is_endpoint_valid)
- `account_peppol_validity_last_check` Date “Checked on” (store, compute=_compute_account_peppol_is_endpoint_valid)
- `account_peppol_verification_label` Selection “Peppol status” (compute=_compute_account_peppol_verification_label)
- `is_peppol_edi_format` Boolean (compute=_compute_is_peppol_edi_format)

Public methods: `button_account_peppol_check_partner_endpoint`, `fields_get`

Extension points: `_check_document_type_support`, `_check_peppol_participant_exists`, `_get_participant_info`, `_get_partners_to_skip_peppol_computation`, `_get_peppol_proxy_identification_info`

## `account.move.send` (extends)

- `checkbox_send_peppol` Boolean “Send via PEPPOL” (store, compute=_compute_checkbox_send_peppol)
- `enable_peppol` Boolean (compute=_compute_enable_peppol)
- `peppol_warning` Char “Warning” (compute=_compute_peppol_warning)
- `account_peppol_edi_mode_info` Char (compute=_compute_account_peppol_edi_mode_info)

Public methods: `action_send_and_print`

Extension points: `_get_invalid_peppol_partners`, `_get_mail_layout`, `_get_peppol_attachments_linked_message`, `_get_peppol_document_params`, `_get_wizard_vals_restrict_to`, `_get_wizard_values`
