# l10n_fr_pdp — France - E-Invoicing (Approved Platform)

Depends on: l10n_fr_account, account_peppol, iap.

## `account.edi.cii` (extends)


## `account.edi.common` (extends)


Extension points: `_get_default_notes`

## `account_edi_proxy_client.user` (extends)

- `proxy_type` Selection

Extension points: `_get_peppol_proxy_types`, `_get_proxy_identification`, `_get_proxy_urls`, `_get_type_code`

## `account.edi.ubl` (extends)


## `account.edi.xml.cii` (extends)


Extension points: `_get_exchanged_document_vals`

## `account.edi.xml.ubl_21_fr` (defines)

France UBL 2.1 E-Invoicing Format

Inherits: `account.edi.xml.ubl_bis3`


## `account.journal` (extends)


Public methods: `button_fetch_in_einvoices`

Extension points: `_get_onboarding_action_data`

## `account.move` (extends)

- `peppol_move_state` Selection “E-Invoicing Status”
- `pdp_ppf_move_state` Selection “PPF Invoice Status” (store, compute=_compute_pdp_ppf_state)
- `pdp_lifecycle_residual` Monetary “Lifecycle Residual” (store, compute=_compute_pdp_lifecycle_residual)
- `pdp_ppf_lifecycle_state` Selection “PPF Lifeycle Status” (store, compute=_compute_pdp_ppf_state)
- `pdp_can_send_response` Boolean (compute=_compute_pdp_can_send_response)
- `pdp_is_sent` Boolean (compute=_compute_pdp_is_sent)
- `pdp_uses_pdp` Boolean (compute=_compute_pdp_uses_pdp)
- `l10n_fr_pdp_sent_in_flow_ids` Many2many → `l10n.fr.pdp.reports.flow` “Sent in French E-Reporting Flows”
- `l10n_fr_pdp_last_flow_id` Many2one → `l10n.fr.pdp.reports.flow` “Last French E-Reporting Flow” (store, compute=_compute_l10n_fr_pdp_last_flow_id)
- `l10n_fr_pdp_status` Selection “E-Reporting Status” (store, compute=_compute_l10n_fr_pdp_status)
- `l10n_fr_pdp_display_info` Boolean (related=company_id.l10n_fr_f10_enable_reporting)
- `l10n_fr_pdp_flow_10_report_type` Selection (store, compute=_compute_l10n_fr_pdp_flow_10_report_type)
- `l10n_fr_pdp_flow_10_operation_type` Selection (store, compute=_compute_l10n_fr_pdp_flow_10_operation_type)
- `l10n_fr_pdp_error_message` Text “Flow 10 blocking errors” (compute=_compute_l10n_fr_pdp_error_message)
- `l10n_fr_pdp_has_error` Boolean (readonly, store, compute=_compute_l10n_fr_pdp_has_error)

Public methods: `action_pdp_open_response_wizard`, `button_cancel`, `button_draft`, `fields_get`

Extension points: `_get_l10n_fr_pdp_errors`, `_get_ubl_cii_builder_from_xml_tree`

## `account.move.send` (extends)


Public methods: `action_what_is_peppol_activate`

Extension points: `_get_default_invoice_edi_format`, `_get_default_sending_methods`, `_get_peppol_attachments_linked_message`, `_get_peppol_document_params`, `_get_peppol_partner_want_peppol_message`, `_get_peppol_what_is_pdp_message`, `_get_peppol_what_is_peppol_alert`, `_get_peppol_what_is_peppol_message`

## `account.peppol.response` (extends)

- `response_code` Selection
- `pdp_ref_response_code` Selection “Original Response Code”
- `pdp_flow_number` Selection “Flow Number”
- `pdp_issue_date` Datetime “Issue Date”
- `pdp_status_info` Text “Status Info”
- `pdp_payment_info` Json “Payment Info”
- `pdp_ref_uuid` Char “Referenced UUID”
- `pdp_ppf_state` Selection “PPF Status” (store, compute=_compute_pdp_ppf_state)

Public methods: `fields_get`

## `account.tax` (extends)


## `ir.attachment` (extends)


## `l10n.fr.pdp.reports.flow` (defines)

French E-Reporting Flow

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char
- `state` Selection “Status” (required)
- `payload_id` Many2one → `ir.attachment` “XML Payload” (compute=_compute_payload_attachment)
- `transport_status` Char
- `transport_message` Text
- `report_type` Selection (required)
- `operation_type` Selection (required)
- `transmission_type` Selection (compute=_compute_transmission_type)
- `initial_flow_id` Many2one → `l10n.fr.pdp.reports.flow`
- `rectificative_flow_ids` One2many → `l10n.fr.pdp.reports.flow`
- `pdp_flow_id` Char (readonly)
- `period_start` Date (required)
- `period_end` Date (required)
- `due_period_start` Date (required)
- `due_period_end` Date (required)
- `periodicity_code` Char
- `company_id` Many2one → `res.company` “Company” (required)
- `move_ids` Many2many → `account.move` (compute=_compute_move_ids)
- `sent_move_ids` Many2many → `account.move`
- `error_moves_count` Integer (compute=_compute_move_ids)
- `error_move_message` Text “Invalid Invoice Details”
- `period_status` Selection “Period Status” (compute=_compute_period_status)

Public methods: `action_build_payload_manual`, `action_open_send_wizard`, `action_send`, `action_send_from_ui`, `action_view_error_moves`, `action_view_initial`, `action_view_moves`

Extension points: `_get_moves`, `_get_open_flow_and_create_if_needed`, `_get_pdp_proxy_user`, `_get_period_flow_properties`, `_get_scope_params_for_move`, `_get_tracking_id`, `_post_sent_message_on_moves`

## `pdp.flow.10.xml.builder` (defines)

Flow 10 XML Builder

Inherits: `account.edi.common`


Extension points: `_get_b2bi_transaction_nodes`, `_get_b2c_transaction_nodes`, `_get_line_category_code`, `_get_line_taxes_result`, `_get_move_business_process_id`, `_get_move_tax_data`, `_get_move_typecode`, `_get_payments`, `_get_payments_summary`, `_get_report_period`, `_get_tax_codes_and_exemption`, `_get_tax_summary`

## `res.company` (extends)

- `l10n_fr_pdp_send_to_ppf` Boolean “Send to PPF”
- `l10n_fr_pdp_pilot_phase` Boolean “E-Invoicing Pilot Phase”
- `l10n_fr_pdp_annuaire_start_date` Date “Annuaire Start Date”
- `l10n_fr_pdp_registered` Boolean “Approved Platform Registered” (compute=_compute_l10n_fr_pdp_registered)
- `pdp_identifier` Char (compute=_compute_pdp_identifier)
- `l10n_fr_pdp_periodicity` Selection “Flow 10 Report Periodicity” (required)
- `l10n_fr_f10_enable_reporting` Boolean “Enable Flux 10 Reporting” (readonly, store, compute=_compute_l10n_fr_f10_enable_reporting)
- `l10n_fr_pdp_flow_10_start_date` Date (compute=_compute_l10n_fr_pdp_flow_10_start_date)
- `pdp_kyc_status` Selection
- `pdp_authentication_uuid` Char “Authentication IAP UUID”

Extension points: `_action_open_pdp_form`, `_check_pdp_identifier`, `_get_einvoicing_identifier_name`, `_get_einvoicing_network_name`

## `res.config.settings` (extends)

- `l10n_fr_pdp_pilot_phase` Boolean “Pilot Phase” (compute=_compute_l10n_fr_pdp_pilot_phase)
- `l10n_fr_pdp_send_to_ppf` Boolean “Send to PPF” (related=company_id.l10n_fr_pdp_send_to_ppf)
- `l10n_fr_pdp_annuaire_start_date` Date “Annuaire Start Date” (related=company_id.l10n_fr_pdp_annuaire_start_date)
- `l10n_fr_pdp_registered` Boolean “Approved Platform Registered” (related=company_id.l10n_fr_pdp_registered)
- `l10n_fr_pdp_periodicity` Selection “Flow 10 Report Periodicity” (required, related=company_id.l10n_fr_pdp_periodicity)

Public methods: `action_open_peppol_form`

## `res.partner` (extends)

- `invoice_edi_format` Selection
- `l10n_fr_is_pdp` Boolean (compute=_compute_l10n_fr_is_pdp)
- `pdp_verification_display_state` Selection “E-Invoicing State” (compute=_compute_pdp_verification_display_state)

Public methods: `action_pdp_annuaire_lookup`, `fields_get`

Extension points: `_check_pdp_send_ubl_21_fr`, `_get_edi_builder`, `_get_pdp_annuaire_verification_state`, `_get_pdp_display_verification_state`, `_get_peppol_verification_state`, `_get_preferred_routing_identifier_vals`, `_get_suggested_invoice_edi_format`, `_get_suggested_peppol_edi_format`, `_get_ubl_cii_formats_info`

## `account.move.send.wizard` (extends)


Extension points: `_get_peppol_checkbox_addendum_disable_reason`, `_get_peppol_checkbox_label`

## `l10n_fr_pdp.partner.lookup` (defines)

Partner Lookup

- `available_annuaire_line_ids` Many2many → `l10n_fr_pdp.annuaire.line` “Available Annuaire Lines”
- `selected_line_id` Many2one → `l10n_fr_pdp.annuaire.line` “Selected Line” (store, compute=_compute_selected_line_id)
- `partner_id` Many2one → `res.partner` (required)

Public methods: `action_change_pdp_endpoint`

## `l10n_fr_pdp.annuaire.line` (defines)

Annuaire Line

- `identifier` Char
- `platform_id` Char
- `nature` Char

## `pdp.registration` (defines)

Approved Platform Registration

- `company_id` Many2one → `res.company` (required)
- `contact_email` Char (required, related=company_id.account_peppol_contact_email)
- `pdp_identifier` Char (store, compute=_compute_pdp_identifier)
- `pdp_pilot_phase` Boolean “ Pilot Phase” (related=company_id.l10n_fr_pdp_pilot_phase)
- `edi_mode` Selection “EDI mode” (compute=_compute_edi_mode)
- `edi_user_id` Many2one → `account_edi_proxy_client.user` “EDI user” (compute=_compute_edi_user_id)
- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `warnings` Json “Warnings” (compute=_compute_warnings)
- `siren_number` Char (store, compute=_compute_siren_number)
- `pdp_authentication_uuid` Char “Authentication IAP UUID” (store, related=company_id.pdp_authentication_uuid)
- `pdp_kyc_status` Selection “Authentication status” (related=company_id.pdp_kyc_status)
- `auth_url_hash` Char “Company Authentication IAP UUID” (related=company_id.pdp_authentication_uuid)

Public methods: `button_cancel_authentication`, `button_deregister_pdp_participant`, `button_open_authentication_link`, `button_refresh_authentication`, `button_register_pdp_participant`, `button_trigger_authentication`, `display_status_notification_from_uuid`

Extension points: `_action_open_pdp_form`, `_action_send_notification`, `_get_company_details`, `_get_kyc_siren`, `_get_status_notification_data`

## `pdp.response.wizard` (defines)

French E-Invoicing Response Wizard

- `move_ids` Many2many → `account.move` (required)
- `status` Selection
- `available_statuses` Char (compute=_compute_available_statuses)
- `reason_code` Selection
- `show_reason_code` Boolean (compute=_compute_show_reason_code)
- `note` Text “Additional note”
- `move_count` Integer (store, compute=_compute_move_count)
- `fully_paid` Boolean “Fully paid” (store, compute=_compute_paid_amount)
- `paid_amount` Monetary “Payment Amount” (store, compute=_compute_paid_amount)
- `currency_id` Many2one → `res.currency` “Currency” (store, compute=_compute_currency_id)

Public methods: `button_send`, `fields_get`

Extension points: `_get_base_lines`, `_get_early_payment_discount_tax_details`, `_get_payments_data`, `_get_payments_data_fully_paid`, `_get_tax_details`

## `l10n.fr.pdp.reports.send.wizard` (defines)

Send French E-Reporting Flow Wizard

- `flow_id` Many2one → `l10n.fr.pdp.reports.flow` (required)
- `warning` Text (readonly)

Public methods: `action_send_anyway`, `action_view_errors`
