# l10n_my_edi_pos — Malaysia - E-invoicing (POS)

Depends on: l10n_my_edi_extended, point_of_sale.

## `account.edi.xml.ubl_myinvois_my` (extends)


Extension points: `_get_address_node`, `_get_consolidated_invoice_node`, `_get_consolidated_invoice_party_node`, `_get_invoice_line_item_vals`

## `account.tax` (extends)

- `l10n_my_tax_exemption_reason` Char “Malaysian Tax Exemption Reason”

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
- `myinvois_error_document_hash` Char “Document Hash” (readonly)
- `myinvois_retry_at` Char “Document Retry At” (readonly)
- `myinvois_exemption_reason` Char “Tax Exemption Reason”
- `myinvois_custom_form_reference` Char “Customs Form Reference Number”
- `myinvois_submission_uid` Char “Submission UID” (readonly)
- `myinvois_external_uuid` Char “MyInvois ID” (readonly, index)
- `myinvois_validation_time` Datetime “Validation Time” (readonly)
- `myinvois_document_long_id` Char “MyInvois Long ID” (readonly)
- `invoice_ids` Many2many → `account.move`

Public methods: `action_cancel_submission`, `action_generate_xml_file`, `action_submit_to_myinvois`, `action_update_submission_status`

Extension points: `_action_myinvois_update_document`, `_get_active_document`, `_get_last_sequence_domain`, `_get_mail_thread_data_attachments`, `_get_sequence_date_range`, `_get_starting_sequence`

## `myinvois.document` (extends)

- `pos_order_ids` Many2many → `pos.order`
- `pos_config_id` Many2one → `pos.config` “PoS Config” (readonly)
- `linked_order_count` Integer (compute=_compute_linked_order_count)
- `pos_order_date_range` Char “Date Range” (store, compute=_compute_pos_order_date_range)

Public methods: `action_open_consolidate_invoice_wizard`, `action_view_linked_orders`

Extension points: `_get_starting_sequence`

## `pos.order` (extends)

- `consolidated_invoice_ids` Many2many → `myinvois.document`

Public methods: `action_show_consolidated_invoice`

Extension points: `_get_active_consolidated_invoice`

## `myinvois.consolidate.invoice.wizard` (defines)

Consolidate Invoice Wizard

- `date_from` Date “Date From” (required)
- `date_to` Date “Date To” (required)

Public methods: `button_consolidate_orders`

## `myinvois.document.status.update.wizard` (defines)

Document Status Update Wizard

- `document_id` Many2one → `myinvois.document` “Document To Update” (required, readonly)
- `reason` Char (required)
- `new_status` Char (required, readonly)

Public methods: `button_request_update`
