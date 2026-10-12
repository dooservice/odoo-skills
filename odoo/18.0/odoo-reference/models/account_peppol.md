# account_peppol — Peppol

Depends on: account_edi_proxy_client, account_edi_ubl_cii.

## `account_edi_proxy_client.user` (extends)

- `peppol_verification_code` Char “SMS verification code”
- `proxy_type` Selection

Extension points: `_check_company_on_peppol`, `_get_can_send_domain`, `_get_company_details`, `_get_peppol_proxy_endpoint`, `_get_peppol_proxy_types`, `_get_proxy_identification`, `_get_proxy_urls`, `_get_type_code`

## `account.edi.xml.ubl_bis3` (extends)


## `account.journal` (extends)

- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `is_peppol_journal` Boolean “Account used for Peppol”

Public methods: `action_peppol_ready_moves`, `peppol_get_message_status`, `peppol_get_new_documents`

Extension points: `_check_type_for_peppol_journal`

## `account.move` (extends)

- `peppol_message_uuid` Char “PEPPOL message ID”
- `peppol_move_state` Selection “PEPPOL status” (store, compute=_compute_peppol_move_state)
- `peppol_is_sent` Boolean (compute=_compute_peppol_is_sent)

Public methods: `action_cancel_peppol_documents`

## `account.move.send` (extends)


Public methods: `action_what_is_peppol_activate`

Extension points: `_get_alerts`, `_get_default_invoice_edi_format`, `_get_default_sending_method`, `_get_mail_layout`, `_get_peppol_attachments_linked_message`, `_get_peppol_document_params`, `_get_peppol_partner_want_peppol_message`, `_get_peppol_what_is_pdp_message`, `_get_peppol_what_is_peppol_alert`, `_get_peppol_what_is_peppol_message`

## `res.company` (extends)

- `account_peppol_contact_email` Char “Primary contact email” (store, compute=_compute_account_peppol_contact_email)
- `account_peppol_migration_key` Char “Migration Key”
- `account_peppol_phone_number` Char “Mobile number” (store, compute=_compute_account_peppol_phone_number)
- `account_peppol_proxy_state` Selection “PEPPOL status” (required)
- `account_peppol_edi_user` Many2one → `account_edi_proxy_client.user` (compute=_compute_account_peppol_edi_user)
- `peppol_eas` Selection (related=partner_id.peppol_eas)
- `peppol_endpoint` Char (related=partner_id.peppol_endpoint)
- `peppol_purchase_journal_id` Many2one → `account.journal` “PEPPOL Purchase Journal” (store, compute=_compute_peppol_purchase_journal_id)
- `peppol_can_send` Boolean (compute=_compute_peppol_can_send)
- `peppol_parent_company_id` Many2one → `res.company` (compute=_compute_peppol_parent_company_id)

Public methods: `create`, `write`

Extension points: `_check_account_peppol_phone_number`, `_check_peppol_endpoint`, `_check_peppol_endpoint_number`, `_check_peppol_purchase_journal_id`, `_check_phonenumbers_import`, `_get_einvoicing_identifier_name`, `_get_einvoicing_network_name`, `_get_peppol_edi_mode`, `_get_peppol_proxy_type`

## `res.config.settings` (extends)

- `account_peppol_edi_user` Many2one (related=company_id.account_peppol_edi_user)
- `account_peppol_edi_mode` Selection (related=account_peppol_edi_user.edi_mode)
- `account_peppol_contact_email` Char (related=company_id.account_peppol_contact_email)
- `account_peppol_eas` Selection (related=company_id.peppol_eas)
- `account_peppol_edi_identification` Char (related=account_peppol_edi_user.edi_identification)
- `account_peppol_endpoint` Char (related=company_id.peppol_endpoint)
- `account_peppol_migration_key` Char (related=company_id.account_peppol_migration_key)
- `account_peppol_phone_number` Char (related=company_id.account_peppol_phone_number)
- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `account_peppol_purchase_journal_id` Many2one (related=company_id.peppol_purchase_journal_id)
- `peppol_purchase_journal_required` Boolean (compute=_compute_peppol_purchase_journal_required)
- `peppol_use_parent_company` Boolean (compute=_compute_peppol_use_parent_company)
- `peppol_parent_company_name` Char (compute=_compute_peppol_use_parent_company)

Public methods: `action_open_peppol_form`, `button_account_peppol_configure_services`, `button_deregister_peppol_participant`, `button_migrate_peppol_registration`, `button_peppol_disconnect_branch_from_parent`, `button_peppol_reregister`, `button_peppol_reset_to_sender`, `button_peppol_smp_registration`, `button_update_peppol_user_data`

Extension points: `_get_pdp_module_info`, `_get_peppol_proxy_type`

## `res.partner` (extends)

- `invoice_sending_method` Selection
- `peppol_eas` Selection
- `available_peppol_sending_methods` Json (compute=_compute_available_peppol_sending_methods)
- `available_peppol_edi_formats` Json (compute=_compute_available_peppol_edi_formats)
- `peppol_verification_state` Selection “Peppol status” (company_dependent)

Public methods: `button_account_peppol_check_partner_endpoint`, `create`, `write`

Extension points: `_check_document_type_support`, `_check_peppol_participant_exists`, `_get_participant_info`, `_get_partners_to_skip_peppol_computation`, `_get_peppol_proxy_identification_info`, `_get_peppol_verification_state`

## `account.move.send.batch.wizard` (extends)


Public methods: `action_send_and_print`

## `account.move.send.wizard` (extends)


Public methods: `action_send_and_print`

Extension points: `_get_peppol_checkbox_addendum_disable_reason`, `_get_peppol_checkbox_label`

## `peppol.registration` (defines)

Peppol Registration

- `company_id` Many2one → `res.company` (required)
- `parent_company_id` Many2one → `res.company` (compute=_compute_parent_company_id)
- `parent_company_name` Char (related=parent_company_id.name)
- `selected_company_id` Many2one → `res.company` (compute=_compute_selected_company_id)
- `use_parent_connection_selection` Selection (compute=_compute_use_parent_connection_selection)
- `use_parent_connection` Boolean (compute=_compute_use_parent_connection)
- `contact_email` Char (required, related=selected_company_id.account_peppol_contact_email)
- `edi_mode` Selection “EDI mode” (compute=_compute_edi_mode)
- `edi_user_id` Many2one → `account_edi_proxy_client.user` “EDI user” (compute=_compute_edi_user_id)
- `account_peppol_migration_key` Char (related=selected_company_id.account_peppol_migration_key)
- `edi_mode_constraint` Selection (compute=_compute_edi_mode_constraint)
- `phone_number` Char (related=selected_company_id.account_peppol_phone_number)
- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `verification_code` Char (related=edi_user_id.peppol_verification_code)
- `peppol_eas` Selection (required, compute=_compute_peppol_eas)
- `peppol_endpoint` Char (required, related=company_id.peppol_endpoint)
- `peppol_warnings` Json “Peppol warnings” (compute=_compute_peppol_warnings)
- `smp_registration` Boolean “Register as a receiver” (store, compute=_compute_smp_registration)

Public methods: `button_check_peppol_verification_code`, `button_deregister_peppol_participant`, `button_peppol_sender_registration`, `button_peppol_smp_registration`, `button_register_peppol_participant`, `button_register_with_kyc`, `button_send_peppol_verification_code`, `button_update_peppol_user_data`

Extension points: `_action_open_peppol_form`, `_action_send_notification`, `_get_peppol_eas_selection`

## `account_peppol.service` (defines)

Peppol Service

- `wizard_id` Many2one → `account_peppol.service.wizard`
- `document_identifier` Char
- `document_name` Char
- `enabled` Boolean

## `account_peppol.service.wizard` (defines)

Peppol Services Wizard

- `edi_user_id` Many2one → `account_edi_proxy_client.user` “EDI user”
- `service_json` Json
- `service_info` Html (compute=_compute_service_info)
- `service_ids` One2many → `account_peppol.service`

Public methods: `confirm`, `create`
