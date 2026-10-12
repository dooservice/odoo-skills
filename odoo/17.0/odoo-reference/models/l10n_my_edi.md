# l10n_my_edi — Malaysia - E-invoicing

Depends on: l10n_my, l10n_my_ubl_pint, account_edi_proxy_client.

## `account_edi_proxy_client.user` (extends)

- `proxy_type` Selection

Extension points: `_get_proxy_identification`, `_get_proxy_urls`

## `account.edi.xml.ubl_myinvois_my` (defines)

Malaysian implementation of ubl for the MyInvois portal

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_country_vals`, `_get_delivery_vals_list`, `_get_invoice_line_item_vals`, `_get_invoice_line_vals`, `_get_partner_address_vals`, `_get_partner_contact_vals`, `_get_partner_party_identification_vals_list`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_tax_category_list`, `_get_tax_unece_codes`

## `account.move` (extends)

- `l10n_my_edi_file_id` Many2one → `ir.attachment` (readonly)
- `l10n_my_edi_file` Binary “MyInvois XML File” (readonly)
- `l10n_my_edi_display_tax_exemption_reason` Boolean “Display Tax Exemption Reason” (compute=_compute_l10n_my_edi_display_tax_exemption_reason)
- `l10n_my_edi_exemption_reason` Char “Tax Exemption Reason”
- `l10n_my_edi_custom_form_reference` Char “Customs Form Reference Number”
- `l10n_my_edi_state` Selection “MyInvois State” (readonly)
- `l10n_my_edi_validation_time` Datetime “Validation Time” (readonly)
- `l10n_my_edi_submission_uid` Char “Submission UID” (readonly)
- `l10n_my_edi_external_uuid` Char “MyInvois ID” (readonly, index)
- `l10n_my_error_document_hash` Char “Document Hash” (readonly)
- `l10n_my_edi_retry_at` Char “Document Retry At” (readonly)

Public methods: `action_l10n_my_edi_reject_bill`, `action_l10n_my_edi_update_status`, `action_validate_tin`, `button_draft`, `button_request_cancel`

## `account.tax` (extends)

- `l10n_my_tax_type` Selection “Malaysian Tax Type” (store, compute=_compute_l10n_my_tax_type)

## `l10n_my_edi.industry_classification` (defines)

Malaysian Industry Classification

- `name` Char (required)
- `code` Char (required)

## `product.template` (extends)

- `l10n_my_edi_classification_code` Selection “Malaysian classification code”

## `res.company` (extends)

- `l10n_my_edi_proxy_user_id` Many2one → `account_edi_proxy_client.user` (compute=_compute_l10n_my_edi_proxy_user_id)
- `l10n_my_identification_type` Selection (related=partner_id.l10n_my_identification_type)
- `l10n_my_identification_number` Char (related=partner_id.l10n_my_identification_number)
- `l10n_my_edi_industrial_classification` Many2one → `l10n_my_edi.industry_classification` “Ind. Classification”
- `l10n_my_edi_mode` Selection
- `l10n_my_edi_default_import_journal_id` Many2one → `account.journal` “Default import journal”

## `res.config.settings` (extends)

- `l10n_my_edi_mode` Selection (related=company_id.l10n_my_edi_mode)
- `l10n_my_edi_default_import_journal_id` Many2one (related=company_id.l10n_my_edi_default_import_journal_id)
- `l10n_my_edi_proxy_user_id` Many2one (related=company_id.l10n_my_edi_proxy_user_id)
- `l10n_my_edi_company_vat` Char (related=company_id.vat)
- `l10n_my_accept_processing` Boolean

Public methods: `action_l10n_my_edi_allow_processing`, `action_l10n_my_edi_unregister`, `action_open_company_form`

## `res.partner` (extends)

- `l10n_my_tin_validation_state` Selection “Tin Validation State” (store, compute=_compute_l10n_my_tin_validation_state)
- `l10n_my_edi_display_tin_warning` Boolean (compute=_compute_l10n_my_edi_display_tin_warning)
- `l10n_my_identification_type` Selection “ID Type”
- `l10n_my_identification_number` Char “ID Number”

Public methods: `action_validate_tin`

## `account.move.send` (extends)

- `l10n_my_edi_enable` Boolean (compute=_compute_l10n_my_edi_enable)
- `l10n_my_edi_send_checkbox` Boolean “Send to MyInvois” (store, compute=_compute_l10n_my_edi_send_checkbox)

Extension points: `_get_invoice_extra_attachments`, `_get_wizard_values`

## `l10n_my_edi.document.status.update` (defines)

Document Status Update Wizard

- `invoice_id` Many2one → `account.move` “Document To Update” (required, readonly)
- `reason` Char (required)
- `new_status` Char (required, readonly)

Public methods: `button_request_update`
