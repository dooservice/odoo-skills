# l10n_dk — Denmark - Accounting

Depends on: account, account_edi_proxy_client, account_edi_ubl_cii.

## `account.account` (extends)


## `account_edi_proxy_client.user` (extends)

- `nemhandel_verification_code` Char “Nemhandel SMS verification code”
- `proxy_type` Selection

Extension points: `_check_user_on_alternative_service`, `_get_nemhandel_company_details`, `_get_nemhandel_user_from_token`, `_get_proxy_identification`, `_get_proxy_urls`

## `account.edi.xml.oioubl_21` (defines)

OIOUBL 2.1

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_address_node`, `_get_currency_decimal_places`, `_get_customization_id`, `_get_document_type_code_node`, `_get_line_discount_allowance_charge_node`, `_get_party_node`, `_get_tax_category_node`, `_get_tax_subtotal_node`

## `account.journal` (extends)

- `l10n_dk_nemhandel_proxy_state` Selection (related=company_id.l10n_dk_nemhandel_proxy_state)
- `is_nemhandel_journal` Boolean “Journal used for Nemhandel”

Public methods: `button_fetch_in_einvoices`, `button_refresh_out_einvoices_status`

Extension points: `_prepare_liquidity_account_vals`

## `account.move` (extends)

- `nemhandel_message_uuid` Char “Nemhandel message ID”
- `nemhandel_move_state` Selection “Nemhandel status” (store, compute=_compute_nemhandel_move_state)
- `nemhandel_response_ids` One2many → `nemhandel.response`
- `nemhandel_can_send_response` Boolean (compute=_compute_nemhandel_can_send_response)

Public methods: `action_cancel_nemhandel_documents`, `action_nemhandel_open_rejection_wizard`, `action_nemhandel_send_approval_response`, `action_open_nemhandel_reponses`, `action_send_and_print`, `button_cancel`

Extension points: `_get_import_file_type`, `_get_ubl_cii_builder_from_xml_tree`

## `account.move.send` (extends)


Extension points: `_get_default_invoice_edi_format`

## `nemhandel.response` (defines)

Business Level Responses for Nemhandel

- `nemhandel_message_uuid` Char “Nemhandel UUID”
- `response_code` Selection (required)
- `nemhandel_state` Selection “Nemhandel status”
- `move_id` Many2one → `account.move`
- `company_id` Many2one (related=move_id.company_id)

## `res.company` (extends)

- `nemhandel_contact_email` Char “Nemhandel Contact email” (store, compute=_compute_nemhandel_contact_email)
- `nemhandel_phone_number` Char “Nemhandel Phone number (for validation)” (store, compute=_compute_nemhandel_phone_number)
- `l10n_dk_nemhandel_proxy_state` Selection “Nemhandel status” (required)
- `nemhandel_identifier_type` Selection (related=partner_id.nemhandel_identifier_type)
- `nemhandel_identifier_value` Char (related=partner_id.nemhandel_identifier_value)
- `nemhandel_purchase_journal_id` Many2one → `account.journal` “Nemhandel Purchase Journal” (store, compute=_compute_nemhandel_purchase_journal_id)
- `nemhandel_edi_user` Many2one → `account_edi_proxy_client.user` (compute=_compute_nemhandel_edi_user)

Extension points: `_check_nemhandel_phone_number`, `_check_nemhandel_purchase_journal_id`, `_check_phonenumbers_import`, `_get_nemhandel_edi_mode`, `_get_nemhandel_webhook_endpoint`

## `res.config.settings` (extends)

- `nemhandel_edi_user` Many2one (related=company_id.nemhandel_edi_user)
- `nemhandel_edi_mode` Selection “Nemhandel EDI operating mode” (related=nemhandel_edi_user.edi_mode)
- `nemhandel_contact_email` Char (related=company_id.nemhandel_contact_email)
- `nemhandel_identifier_type` Selection (related=company_id.nemhandel_identifier_type)
- `nemhandel_identifier_value` Char (related=company_id.nemhandel_identifier_value)
- `nemhandel_edi_identification` Char “Nemhandel identification” (related=nemhandel_edi_user.edi_identification)
- `nemhandel_phone_number` Char (related=company_id.nemhandel_phone_number)
- `l10n_dk_nemhandel_proxy_state` Selection (related=company_id.l10n_dk_nemhandel_proxy_state)
- `nemhandel_purchase_journal_id` Many2one (related=company_id.nemhandel_purchase_journal_id)

Public methods: `action_open_nemhandel_form`, `button_deregister_nemhandel_participant`, `button_update_nemhandel_user_data`

## `res.partner` (extends)

- `invoice_sending_method` Selection
- `invoice_edi_format` Selection
- `nemhandel_verification_state` Selection “Nemhandel endpoint verification” (company_dependent)
- `nemhandel_identifier_type` Selection “Nemhandel Endpoint Type” (store, compute=_compute_nemhandel_identifier_type)
- `nemhandel_identifier_value` Char “Nemhandel Endpoint” (store, compute=_compute_nemhandel_identifier_value)
- `nemhandel_supported_documents` Json “Supported Nemhandel Documents”
- `nemhandel_response_support` Boolean “Nemhandel Response Service” (compute=_compute_nemhandel_response_support)
- `is_using_nemhandel` Boolean (compute=_compute_is_using_nemhandel)

Public methods: `button_nemhandel_check_partner_endpoint`, `create`, `write`

Extension points: `_check_nemhandel_participant_exists`, `_check_nemhandel_send_oioubl`, `_get_edi_builder`, `_get_nemhandel_participant_info`, `_get_nemhandel_verification_state`, `_get_suggested_invoice_edi_format`, `_get_ubl_cii_formats_info`

## `account.chart.template` (extends)


Extension points: `_get_dk_res_company`, `_get_dk_template_data`

## `account.move.send.batch.wizard` (extends)


Public methods: `action_send_and_print`

## `account.move.send.wizard` (extends)


Public methods: `action_send_and_print`

## `nemhandel.registration` (defines)

Nemhandel Registration

- `company_id` Many2one → `res.company` (required)
- `contact_email` Char (required, related=company_id.nemhandel_contact_email)
- `edi_mode` Selection “EDI mode” (compute=_compute_edi_mode)
- `edi_user_id` Many2one → `account_edi_proxy_client.user` “EDI user” (compute=_compute_edi_user_id)
- `phone_number` Char (related=company_id.nemhandel_phone_number)
- `l10n_dk_nemhandel_proxy_state` Selection (related=company_id.l10n_dk_nemhandel_proxy_state)
- `verification_code` Char (related=edi_user_id.nemhandel_verification_code)
- `identifier_type` Selection (required, related=company_id.nemhandel_identifier_type)
- `identifier_value` Char (required, related=company_id.nemhandel_identifier_value)

Public methods: `button_check_nemhandel_verification_code`, `button_deregister_nemhandel_participant`, `button_nemhandel_receiver_registration`, `button_nemhandel_registration_sms`, `button_update_nemhandel_user_data`, `send_nemhandel_verification_code`

Extension points: `_action_open_nemhandel_form`, `_action_send_notification`

## `nemhandel.rejection.wizard` (defines)

Nemhandel Rejection wizard

- `move_ids` Many2many → `account.move` (required)
- `note` Text “Additional note”

Public methods: `button_send`
