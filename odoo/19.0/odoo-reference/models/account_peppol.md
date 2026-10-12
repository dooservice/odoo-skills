# account_peppol — Peppol

Depends on: account_edi_proxy_client, account_edi_ubl_cii.

## `account.edi.common` (extends)


## `account_edi_proxy_client.user` (extends)

- `proxy_type` Selection

Extension points: `_get_can_send_domain`, `_get_company_details`, `_get_peppol_error_message`, `_get_peppol_proxy_endpoint`, `_get_peppol_proxy_types`, `_get_proxy_identification`, `_get_proxy_urls`, `_get_type_code`, `_get_user_from_token`

## `account.edi.ubl` (extends)


## `account.edi.xml.ubl_bis3` (extends)


## `account.journal` (extends)

- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `is_peppol_journal` Boolean “Account used for Peppol”

Public methods: `button_fetch_in_einvoices`, `button_refresh_out_einvoices_status`

Extension points: `_check_type_for_peppol_journal`

## `account.move` (extends)

- `peppol_message_uuid` Char “PEPPOL message ID”
- `peppol_move_state` Selection “PEPPOL status” (store, compute=_compute_peppol_move_state)
- `peppol_is_sent` Boolean (compute=_compute_peppol_is_sent)

Public methods: `action_cancel_peppol_documents`, `action_peppol_cancel_and_remove_sequence`, `action_peppol_reset_documents`, `action_send_and_print`

## `account.move.send` (extends)


Public methods: `action_what_is_peppol_activate`

Extension points: `_get_alerts`, `_get_default_invoice_edi_format`, `_get_default_sending_methods`, `_get_mail_layout`, `_get_peppol_attachments_linked_message`, `_get_peppol_document_params`, `_get_peppol_partner_want_peppol_message`, `_get_peppol_what_is_pdp_message`, `_get_peppol_what_is_peppol_alert`, `_get_peppol_what_is_peppol_message`

## `res.company` (extends)

- `account_peppol_contact_email` Char “Primary contact email” (store, compute=_compute_account_peppol_contact_email)
- `account_peppol_migration_key` Char “Migration Key”
- `account_peppol_phone_number` Char “Mobile number” (store, compute=_compute_account_peppol_phone_number)
- `account_peppol_proxy_state` Selection “PEPPOL status” (required)
- `account_peppol_edi_user` Many2one → `account_edi_proxy_client.user` (compute=_compute_account_peppol_edi_user)
- `peppol_eas` Selection (related=partner_id.peppol_eas)
- `peppol_endpoint` Char (related=partner_id.peppol_endpoint)
- `peppol_purchase_journal_id` Many2one → `account.journal` “Peppol Purchase Journal” (store, compute=_compute_peppol_purchase_journal_id)
- `peppol_external_provider` Char
- `peppol_can_send` Boolean (compute=_compute_peppol_can_send)
- `peppol_parent_company_id` Many2one → `res.company` (compute=_compute_peppol_parent_company_id)
- `peppol_metadata` Json “Peppol Metadata”
- `peppol_metadata_updated_at` Datetime “Peppol meta updated at”
- `peppol_activate_self_billing_sending` Boolean “Activate self-billing sending”
- `peppol_self_billing_reception_journal_id` Many2one → `account.journal` “Self-Billing reception journal” (store, compute=_compute_peppol_self_billing_reception_journal_id)

Public methods: `create`, `write`

Extension points: `_check_account_peppol_phone_number`, `_check_peppol_endpoint`, `_check_peppol_endpoint_number`, `_check_peppol_purchase_journal_id`, `_check_phonenumbers_import`, `_get_active_peppol_parent_company`, `_get_company_info_on_peppol`, `_get_einvoicing_identifier_name`, `_get_einvoicing_network_name`, `_get_peppol_edi_mode`, `_get_peppol_proxy_type`, `_get_peppol_webhook_endpoint`

## `res.config.settings` (extends)

- `account_peppol_edi_user` Many2one (related=company_id.account_peppol_edi_user)
- `account_peppol_edi_mode` Selection (related=account_peppol_edi_user.edi_mode)
- `account_peppol_contact_email` Char (compute=_compute_account_peppol_contact_email)
- `account_peppol_eas` Selection (related=company_id.peppol_eas)
- `account_peppol_edi_identification` Char (related=account_peppol_edi_user.edi_identification)
- `account_peppol_endpoint` Char (related=company_id.peppol_endpoint)
- `account_peppol_migration_key` Char (related=company_id.account_peppol_migration_key)
- `account_peppol_phone_number` Char (related=company_id.account_peppol_phone_number)
- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `account_peppol_purchase_journal_id` Many2one (related=company_id.peppol_purchase_journal_id)
- `peppol_external_provider` Char (related=company_id.peppol_external_provider)
- `peppol_purchase_journal_required` Boolean (compute=_compute_peppol_purchase_journal_required)
- `peppol_use_parent_company` Boolean (compute=_compute_peppol_use_parent_company)
- `peppol_parent_company_name` Char (compute=_compute_peppol_use_parent_company)
- `account_is_token_out_of_sync` Boolean (related=account_peppol_edi_user.is_token_out_of_sync)
- `peppol_participation_role` Selection (compute=_compute_peppol_participation_role)

Public methods: `action_open_peppol_form`, `button_disconnect_this_database`, `button_open_peppol_config_wizard`, `button_peppol_deregister`, `button_peppol_disconnect_branch_from_parent`, `button_peppol_register_sender_as_receiver`, `button_peppol_reregister`, `button_reconnect_this_database`

Extension points: `_get_pdp_module_info`, `_get_peppol_proxy_type`

## `res.partner` (extends)

- `invoice_sending_method` Selection
- `peppol_eas` Selection
- `available_peppol_sending_methods` Json (compute=_compute_available_peppol_sending_methods)
- `available_peppol_edi_formats` Json (compute=_compute_available_peppol_edi_formats)
- `peppol_verification_state` Selection “Peppol status” (company_dependent)

Public methods: `button_account_peppol_check_partner_endpoint`, `create`

Extension points: `_check_document_type_support`, `_check_peppol_participant_exists`, `_get_frontend_writable_fields`, `_get_participant_info`, `_get_partners_to_skip_peppol_computation`, `_get_peppol_proxy_identification_info`, `_get_peppol_verification_state`

## `account.move.send.batch.wizard` (extends)


Public methods: `action_send_and_print`

## `account.move.send.wizard` (extends)


Public methods: `action_send_and_print`

Extension points: `_get_peppol_checkbox_addendum_disable_reason`, `_get_peppol_checkbox_label`

## `account_peppol.service` (defines)

Peppol Service

- `wizard_id` Many2one → `peppol.config.wizard`
- `document_identifier` Char
- `document_name` Char
- `enabled` Boolean

## `peppol.config.wizard` (defines)

Peppol Configuration Wizard

- `company_id` Many2one → `res.company` (required)
- `account_peppol_edi_user` Many2one (related=company_id.account_peppol_edi_user)
- `account_peppol_edi_identification` Char (related=account_peppol_edi_user.edi_identification)
- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `account_peppol_contact_email` Char (required)
- `account_peppol_migration_key` Char (related=company_id.account_peppol_migration_key)
- `peppol_activate_self_billing` Boolean “Activate self-billing” (compute=_compute_peppol_activate_self_billing)
- `peppol_self_billing_reception_journal_id` Many2one (related=company_id.peppol_self_billing_reception_journal_id)
- `service_json` Json (store, compute=_compute_service_json)
- `service_info` Html (compute=_compute_service_info)
- `service_ids` One2many → `account_peppol.service` (store, compute=_compute_service_ids)

Public methods: `button_peppol_register_sender_as_receiver`, `button_peppol_reset_to_sender`, `button_peppol_unregister`, `button_sync_form_with_peppol_proxy`

## `peppol.registration` (defines)

Peppol Registration

- `company_id` Many2one → `res.company` (required)
- `parent_company_id` Many2one → `res.company` (compute=_compute_parent_company_id)
- `parent_company_name` Char (related=parent_company_id.name)
- `selected_company_id` Many2one → `res.company` (compute=_compute_selected_company_id)
- `display_use_parent_connection_selection` Boolean (compute=_compute_display_use_parent_connection_selection)
- `use_parent_connection_selection` Selection (store, compute=_compute_use_parent_connection_selection)
- `use_parent_connection` Boolean (compute=_compute_use_parent_connection)
- `is_branch_company` Boolean
- `active_parent_company` Many2one “Active Parent Company” (related=parent_company_id)
- `active_parent_company_name` Char “Active Parent Company Name” (related=parent_company_name)
- `can_use_parent_connection` Boolean “Can Use Parent Connection” (related=display_use_parent_connection_selection)
- `edi_mode` Selection “EDI mode” (compute=_compute_edi_mode)
- `edi_user_id` Many2one → `account_edi_proxy_client.user` “EDI user” (compute=_compute_edi_user_id)
- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `peppol_eas` Selection (required, compute=_compute_peppol_eas)
- `peppol_warnings` Json “Peppol warnings” (compute=_compute_peppol_warnings)
- `contact_email` Char (required, related=selected_company_id.account_peppol_contact_email)
- `phone_number` Char (related=selected_company_id.account_peppol_phone_number)
- `peppol_endpoint` Char (required, related=selected_company_id.peppol_endpoint)
- `smp_registration` Boolean “Register as a receiver” (compute=_compute_smp_registration_external_provider)
- `peppol_external_provider` Char (compute=_compute_smp_registration_external_provider)
- `peppol_can_connect_data` Json (compute=_compute_peppol_can_connect_data)
- `display_itsme_login` Boolean (compute=_compute_peppol_can_connect_data)
- `display_no_auth_buttons` Boolean (compute=_compute_peppol_can_connect_data)

Public methods: `button_register_peppol_participant`, `button_register_with_itsme`

Extension points: `_action_open_peppol_form`, `_action_send_notification`, `_create_connection`, `_get_company_details`, `_get_peppol_eas_selection`
