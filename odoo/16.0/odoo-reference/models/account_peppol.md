# account_peppol — Peppol

Depends on: account_edi_proxy_client, account_edi_ubl_cii.

## `account.edi.format` (extends)


Extension points: `_get_move_applicability`, `_get_peppol_builder`, `_get_proxy_identification`

## `account_edi_proxy_client.user` (extends)


Extension points: `_get_create_user_edi_params`, `_get_route`, `_get_server_url_new`

## `account.journal` (extends)

- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `is_peppol_journal` Boolean “Is journal used for Peppol invoices reception”

Public methods: `action_peppol_ready_moves`, `peppol_get_message_status`, `peppol_get_new_documents`

Extension points: `_check_type_for_peppol_journal`

## `account.move` (extends)

- `peppol_message_uuid` Char “PEPPOL message ID”
- `peppol_move_state` Selection “PEPPOL status” (store, compute=_compute_peppol_move_state)
- `peppol_is_demo_uuid` Boolean (compute=_compute_peppol_is_demo_uuid)

Extension points: `_get_peppol_document`

## `ir.actions.report` (extends)


Extension points: `_get_edi_document_format_codes_for_pdf_embedding`

## `res.company` (extends)

- `account_peppol_contact_email` Char “Primary contact email” (store, compute=_compute_account_peppol_contact_email)
- `account_peppol_phone_number` Char “Mobile number (for validation)” (store, compute=_compute_account_peppol_phone_number)
- `account_peppol_proxy_state` Selection “PEPPOL status” (required)
- `is_account_peppol_participant` Boolean “PEPPOL Participant”
- `peppol_eas` Selection (related=partner_id.peppol_eas)
- `peppol_endpoint` Char (related=partner_id.peppol_endpoint)
- `peppol_purchase_journal_id` Many2one → `account.journal` “PEPPOL Purchase Journal” (store, compute=_compute_peppol_purchase_journal_id)

Public methods: `create`, `write`

Extension points: `_check_account_peppol_phone_number`, `_check_peppol_endpoint`, `_check_peppol_endpoint_number`, `_check_peppol_purchase_journal_id`, `_get_peppol_edi_mode`

## `res.config.settings` (extends)

- `account_peppol_edi_user` Many2one → `account_edi_proxy_client.user` “EDI user” (compute=_compute_account_peppol_edi_user)
- `account_peppol_contact_email` Char (related=company_id.account_peppol_contact_email)
- `account_peppol_eas` Selection (related=company_id.peppol_eas)
- `account_peppol_edi_identification` Char (related=account_peppol_edi_user.edi_identification)
- `account_peppol_endpoint` Char (related=company_id.peppol_endpoint)
- `account_peppol_endpoint_warning` Char “Warning” (compute=_compute_account_peppol_endpoint_warning)
- `account_peppol_phone_number` Char (related=company_id.account_peppol_phone_number)
- `account_peppol_proxy_state` Selection (related=company_id.account_peppol_proxy_state)
- `account_peppol_purchase_journal_id` Many2one (related=company_id.peppol_purchase_journal_id)
- `is_account_peppol_participant` Boolean “Use PEPPOL” (related=company_id.is_account_peppol_participant)
- `account_peppol_edi_mode` Selection (compute=_compute_account_peppol_edi_mode)

Public methods: `button_cancel_peppol_registration`, `button_create_peppol_proxy_user`, `button_deregister_peppol_participant`, `button_register_with_kyc`, `button_update_peppol_user_data`

## `res.partner` (extends)

- `account_peppol_is_endpoint_valid` Boolean “PEPPOL endpoint validity” (store, compute=_compute_account_peppol_is_endpoint_valid)
- `account_peppol_validity_last_check` Date “Checked on” (store, compute=_compute_account_peppol_is_endpoint_valid)
- `account_peppol_verification_label` Selection “Peppol status” (compute=_compute_account_peppol_verification_label)
- `ubl_cii_format` Selection “Format” (store, compute=_compute_ubl_cii_format)
- `peppol_endpoint` Char “Peppol Endpoint” (store, compute=_compute_peppol_endpoint)
- `peppol_eas` Selection “Peppol e-address (EAS)” (store, compute=_compute_peppol_eas)

Public methods: `button_account_peppol_check_partner_endpoint`

Extension points: `_check_document_type_support`, `_check_peppol_eas`, `_check_peppol_fields`, `_check_peppol_participant_exists`, `_get_customization_ids`, `_get_partners_to_skip_peppol_computation`, `_get_peppol_edi_format`, `_get_peppol_endpoint_value`, `_get_ubl_cii_formats`

## `account.invoice.send` (extends)

- `peppol_invoice_ids` Many2many → `account.move` (store, compute=_compute_peppol_invoice_ids)
- `company_id` Many2one → `res.company` (store, compute=_compute_company_id)
- `account_peppol_edi_mode_info` Char (compute=_compute_account_peppol_edi_mode_info)
- `checkbox_send_peppol` Boolean “Send via PEPPOL” (store, compute=_compute_checkbox_send_peppol)
- `checkbox_send_peppol_readonly` Boolean (compute=_compute_checkbox_send_peppol_readonly)
- `enable_peppol` Boolean (compute=_compute_enable_peppol)
- `peppol_warning` Char “Warning” (compute=_compute_peppol_warning)

Public methods: `send_and_print_action`

Extension points: `_get_peppol_available_attachments`
