# l10n_my_edi — Malaysia - E-invoicing

Depends on: l10n_my, l10n_my_ubl_pint, account_edi_proxy_client.

## `account_edi_proxy_client.user` (extends)

- `proxy_type` Selection

Extension points: `_get_proxy_identification`, `_get_proxy_urls`

## `account.edi.xml.ubl_myinvois_my` (defines)

Malaysian implementation of ubl for the MyInvois portal

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_myinvois_document_address_node`, `_get_myinvois_document_line_node`, `_get_myinvois_document_node`, `_get_myinvois_document_party_identification_node`, `_get_myinvois_document_party_node`, `_get_tax_category_node`

## `account.journal` (extends)


Public methods: `open_myinvois_document`

## `account.move` (extends)

- `l10n_my_edi_document_ids` Many2many → `myinvois.document`
- `l10n_my_edi_display_tax_exemption_reason` Boolean “Display Tax Exemption Reason” (compute=_compute_l10n_my_edi_display_tax_exemption_reason)
- `l10n_my_edi_is_applicable` Boolean (compute=_compute_l10n_my_edi_is_applicable)
- `l10n_my_edi_state` Selection “MyInvois State” (store, compute=_compute_l10n_my_edi_state)
- `l10n_my_edi_exemption_reason` Char “Tax Exemption Reason”
- `l10n_my_edi_custom_form_reference` Char “Customs Form Reference Number”

Public methods: `action_invoice_sent`, `action_l10n_my_edi_send_invoice`, `action_l10n_my_edi_update_status`, `action_show_myinvois_documents`, `button_draft`, `button_request_cancel`

Extension points: `_create_myinvois_document`, `_get_active_myinvois_document`, `_get_fields_to_detach`, `_get_name_invoice_report`

## `account.move.line` (extends)

- `l10n_my_edi_classification_code` Selection “Malaysian classification code” (store, compute=_compute_l10n_my_edi_classification_code)

## `account.move.send` (extends)


Extension points: `_get_invoice_extra_attachments`

## `account.tax` (extends)

- `l10n_my_tax_type` Selection “Malaysian Tax Type” (store, compute=_compute_l10n_my_tax_type)
- `l10n_my_tax_exemption_reason` Char “Malaysian Tax Exemption Reason”

## `l10n_my_edi.industry_classification` (defines)

Malaysian Industry Classification

- `name` Char (required)
- `code` Char (required)

## `myinvois.document` (defines)

MyInvois Document

Inherits: `mail.thread`, `mail.activity.mixin`, `sequence.mixin`

- `name` Char (store, compute=_compute_name)
- `active` Boolean “Active”
- `company_id` Many2one → `res.company` (required, readonly)
- `currency_id` Many2one → `res.currency` (required)
- `company_currency_id` Many2one “Company Currency” (related=company_id.currency_id)
- `myinvois_issuance_date` Date “Issuance Date” (readonly)
- `myinvois_file_id` Many2one → `ir.attachment`
- `myinvois_file` Binary “MyInvois XML File” (readonly)
- `myinvois_state` Selection “MyInvois State” (readonly)
- `is_superseded` Boolean (readonly)
- `myinvois_error_document_hash` Char “Document Hash” (readonly)
- `myinvois_retry_at` Char “Document Retry At” (readonly)
- `myinvois_exemption_reason` Char “Tax Exemption Reason”
- `myinvois_custom_form_reference` Char “Customs Form Reference Number”
- `myinvois_submission_uid` Char “Submission UID” (readonly)
- `myinvois_external_uuid` Char “MyInvois ID” (readonly, index)
- `myinvois_validation_time` Datetime “Validation Time” (readonly)
- `myinvois_document_long_id` Char “MyInvois Long ID” (readonly)
- `invoice_ids` Many2many → `account.move`
- `linked_invoice_count` Integer (compute=_compute_linked_invoice_count)
- `is_consolidated_invoice` Boolean
- `move_type` Selection “Type” (required, readonly, index)
- `journal_id` Many2one → `account.journal` “Journal” (required, readonly, index)
- `is_debit_note` Boolean (readonly)

Public methods: `action_cancel_submission`, `action_generate_xml_file`, `action_open_consolidate_invoice_wizard`, `action_show_myinvois_documents`, `action_submit_to_myinvois`, `action_update_submission_status`, `action_view_linked_invoices`, `init`

Extension points: `_action_myinvois_update_document`, `_check_move_type`, `_get_active_myinvois_document`, `_get_last_sequence_domain`, `_get_mail_thread_data_attachments`, `_get_record_rounded_base_lines`, `_get_rounded_base_lines`, `_get_sequence_date_range`, `_get_starting_sequence`

## `product.template` (extends)

- `l10n_my_edi_classification_code` Selection “Malaysian classification code”

## `res.company` (extends)

- `l10n_my_edi_is_branch` Boolean (compute=_compute_l10n_my_edi_is_branch)
- `l10n_my_edi_proxy_user_id` Many2one → `account_edi_proxy_client.user` (compute=_compute_l10n_my_edi_proxy_user_id)
- `l10n_my_identification_type` Selection (related=partner_id.l10n_my_identification_type)
- `l10n_my_identification_number` Char (related=partner_id.l10n_my_identification_number)
- `l10n_my_identification_number_placeholder` Char (compute=_compute_l10n_my_identification_number_placeholder)
- `l10n_my_edi_industrial_classification` Many2one (related=partner_id.l10n_my_edi_industrial_classification)
- `l10n_my_edi_is_sole_proprietor` Boolean
- `l10n_my_edi_mode` Selection
- `l10n_my_edi_default_import_journal_id` Many2one → `account.journal` “Default import journal”

## `res.config.settings` (extends)

- `l10n_my_edi_mode` Selection (related=company_id.l10n_my_edi_mode)
- `l10n_my_edi_default_import_journal_id` Many2one (related=company_id.l10n_my_edi_default_import_journal_id)
- `l10n_my_edi_proxy_user_id` Many2one (related=company_id.l10n_my_edi_proxy_user_id)
- `l10n_my_edi_company_vat` Char (related=company_id.vat)
- `l10n_my_edi_is_branch` Boolean (related=company_id.l10n_my_edi_is_branch)
- `l10n_my_edi_parent_mode` Selection “Parent MyInvois mode” (related=company_id.parent_id.l10n_my_edi_mode)
- `l10n_my_edi_is_sole_proprietor` Boolean (related=company_id.l10n_my_edi_is_sole_proprietor)
- `l10n_my_edi_show_sole_proprietor` Boolean (compute=_compute_l10n_my_edi_show_sole_proprietor)
- `l10n_my_edi_identification_number` Char (related=company_id.l10n_my_identification_number)
- `l10n_my_accept_processing` Boolean

Public methods: `action_l10n_my_edi_allow_processing`, `action_l10n_my_edi_unregister`, `action_open_company_form`

## `res.partner` (extends)

- `l10n_my_tin_validation_state` Selection “Tin Validation State” (store, compute=_compute_l10n_my_tin_validation_state)
- `l10n_my_edi_display_tin_warning` Boolean (compute=_compute_l10n_my_edi_display_tin_warning)
- `l10n_my_identification_type` Selection “ID Type”
- `l10n_my_identification_number` Char “ID Number”
- `l10n_my_identification_number_placeholder` Char (compute=_compute_l10n_my_identification_number_placeholder)
- `l10n_my_edi_industrial_classification` Many2one → `l10n_my_edi.industry_classification` “Ind. Classification” (store, compute=_compute_l10n_my_edi_industrial_classification)
- `l10n_my_edi_malaysian_tin` Char “Malaysian TIN”

Public methods: `action_validate_tin`

Extension points: `_get_frontend_writable_fields`

## `myinvois.consolidate.invoice.wizard` (defines)

Consolidate Invoice Wizard

- `date_from` Date “Date From” (required)
- `date_to` Date “Date To” (required)
- `consolidation_type` Selection (required)

Public methods: `button_consolidate`

Extension points: `_get_myinvois_consolidated_invoice_vals`, `_get_myinvois_document_vals`

## `myinvois.document.status.update.wizard` (defines)

Document Status Update Wizard

- `document_id` Many2one → `myinvois.document` “Document To Update” (required, readonly)
- `reason` Char (required)
- `new_status` Char (required, readonly)

Public methods: `button_request_update`
