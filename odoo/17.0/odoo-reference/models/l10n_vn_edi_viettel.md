# l10n_vn_edi_viettel — Vietnam - E-invoicing

Depends on: l10n_vn.

## `account.move` (extends)

- `l10n_vn_edi_invoice_state` Selection “Sinvoice Status” (store, compute=_compute_l10n_vn_edi_invoice_state)
- `l10n_vn_edi_invoice_transaction_id` Char “SInvoice Transaction ID”
- `l10n_vn_edi_invoice_symbol` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “Invoice Symbol” (store, compute=_compute_l10n_vn_edi_invoice_symbol)
- `l10n_vn_edi_invoice_number` Char “SInvoice Number” (readonly)
- `l10n_vn_edi_reservation_code` Char “Secret Code” (readonly)
- `l10n_vn_edi_issue_date` Datetime “Issue Date” (readonly)
- `l10n_vn_edi_sinvoice_file_id` Many2one → `ir.attachment` (readonly)
- `l10n_vn_edi_sinvoice_file` Binary “SInvoice json File” (readonly)
- `l10n_vn_edi_sinvoice_xml_file_id` Many2one → `ir.attachment` (readonly)
- `l10n_vn_edi_sinvoice_xml_file` Binary “SInvoice xml File” (readonly)
- `l10n_vn_edi_sinvoice_pdf_file_id` Many2one → `ir.attachment` (readonly)
- `l10n_vn_edi_sinvoice_pdf_file` Binary “SInvoice pdf File” (readonly)
- `l10n_vn_edi_agreement_document_name` Char “Agreement Name”
- `l10n_vn_edi_agreement_document_date` Datetime “Agreement Date”
- `l10n_vn_edi_adjustment_type` Selection “Adjustment type”
- `l10n_vn_edi_replacement_origin_id` Many2one → `account.move` “Replacement of” (readonly)
- `l10n_vn_edi_reversed_entry_invoice_number` Char “Revered Entry SInvoice Number” (related=reversed_entry_id.l10n_vn_edi_invoice_number)

Public methods: `action_l10n_vn_edi_update_payment_status`, `button_draft`, `button_request_cancel`

Extension points: `_get_mail_thread_data_attachments`

## `res.company` (extends)

- `l10n_vn_edi_username` Char “SInvoice Username”
- `l10n_vn_edi_password` Char “Sinvoice Password”
- `l10n_vn_edi_token` Char “Sinvoice Access Token” (readonly)
- `l10n_vn_edi_token_expiry` Datetime “Sinvoice Access Token Expiration Date” (readonly)

## `res.config.settings` (extends)

- `l10n_vn_edi_username` Char (related=company_id.l10n_vn_edi_username)
- `l10n_vn_edi_password` Char (related=company_id.l10n_vn_edi_password)
- `l10n_vn_edi_default_symbol` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “Default Symbol” (compute=_compute_l10n_vn_edi_default_symbol)

## `res.partner` (extends)

- `l10n_vn_edi_symbol` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “Default Symbol” (company_dependent)

## `l10n_vn_edi_viettel.sinvoice.template` (defines)

SInvoice template

- `name` Char “Template Code” (required)
- `template_invoice_type` Selection (required)
- `invoice_symbols_ids` One2many → `l10n_vn_edi_viettel.sinvoice.symbol`

## `l10n_vn_edi_viettel.sinvoice.symbol` (defines)

SInvoice symbol

- `name` Char “Symbol” (required)
- `invoice_template_id` Many2one → `l10n_vn_edi_viettel.sinvoice.template` (required)

## `account.move.reversal` (extends)

- `l10n_vn_edi_adjustment_type` Selection “Adjustment type” (required)
- `l10n_vn_edi_agreement_document_name` Char “Agreement Name”
- `l10n_vn_edi_agreement_document_date` Datetime “Agreement Date”

Public methods: `reverse_moves`

Extension points: `_prepare_default_reversal`

## `account.move.send` (extends)

- `l10n_vn_edi_enable` Boolean (compute=_compute_l10n_vn_edi_enable)
- `l10n_vn_edi_send_checkbox` Boolean “Send to SInvoice” (store, compute=_compute_l10n_vn_edi_send_checkbox)
- `l10n_vn_edi_generate_file_checkbox` Boolean “Generate SInvoice file” (store, compute=_compute_l10n_vn_edi_generate_file_checkbox)

Extension points: `_get_invoice_extra_attachments`, `_get_placeholder_mail_attachments_data`, `_get_wizard_values`

## `l10n_vn_edi_viettel.cancellation` (defines)

E-invoice cancellation wizard

- `invoice_id` Many2one → `account.move` “Invoice to cancel”
- `reason` Char “Reason” (required)
- `agreement_document_name` Char “Agreement Name”
- `agreement_document_date` Datetime “Agreement Date”

Public methods: `button_request_cancel`
