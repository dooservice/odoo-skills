# l10n_dk_nemhandel — Denmark EDI - Nemhandel

Depends on: account_edi_proxy_client, account_edi_ubl_cii, l10n_dk.

## `account_edi_proxy_client.user` (extends)

- `nemhandel_verification_code` Char “Nemhandel SMS verification code”
- `proxy_type` Selection

Extension points: `_check_user_on_alternative_service`, `_get_nemhandel_company_details`, `_get_nemhandel_user_from_token`, `_get_proxy_identification`, `_get_proxy_urls`

## `account.edi.xml.oioubl_21` (defines)

OIOUBL 2.1

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_address_node`, `_get_currency_decimal_places`, `_get_document_type_code_vals`, `_get_line_discount_allowance_charge_node`, `_get_party_node`, `_get_tax_category_node`, `_get_tax_subtotal_node`

## `account.journal` (extends)

- `l10n_dk_nemhandel_proxy_state` Selection (related=company_id.l10n_dk_nemhandel_proxy_state)
- `is_nemhandel_journal` Boolean “Journal used for Nemhandel”

Public methods: `nemhandel_get_message_status`, `nemhandel_get_new_documents`

## `account.move` (extends)

- `nemhandel_message_uuid` Char “Nemhandel message ID”
- `nemhandel_move_state` Selection “Nemhandel status” (store, compute=_compute_nemhandel_move_state)

Public methods: `action_cancel_nemhandel_documents`

Extension points: `_get_ubl_cii_builder_from_xml_tree`

## `account.move.send` (extends)


Extension points: `_get_default_invoice_edi_format`

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
- `is_using_nemhandel` Boolean (compute=_compute_is_using_nemhandel)

Public methods: `button_nemhandel_check_partner_endpoint`, `create`, `write`

Extension points: `_check_nemhandel_participant_exists`, `_check_nemhandel_send_oioubl`, `_get_edi_builder`, `_get_nemhandel_participant_info`, `_get_nemhandel_verification_state`, `_get_suggested_invoice_edi_format`, `_get_ubl_cii_formats_info`

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
