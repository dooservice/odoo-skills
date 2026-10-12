# l10n_vn_edi_viettel — Vietnam - E-invoicing

Depends on: l10n_vn.

## `account.journal` (extends)

- `l10n_vn_edi_default_symbol_id` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “Default E-invoice Symbol”

## `account.move` (extends)

- `l10n_vn_edi_invoice_state` Selection “SInvoice Status” (readonly, store, compute=_compute_l10n_vn_edi_invoice_state)
- `l10n_vn_edi_invoice_transaction_id` Char “SInvoice Transaction ID”
- `l10n_vn_edi_invoice_symbol` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “SInvoice Symbol” (store, compute=_compute_l10n_vn_edi_invoice_symbol)
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

Public methods: `action_l10n_vn_edi_update_payment_status`, `l10n_vn_edi_fetch_files_with_tax_code`

Extension points: `_get_fields_to_detach`, `_get_mail_thread_data_attachments`

## `account.move.send` (extends)


Extension points: `_get_all_extra_edis`, `_get_invoice_extra_attachments`, `_get_placeholder_mail_attachments_data`

## `res.company` (extends)

- `l10n_vn_edi_username` Char “SInvoice Username”
- `l10n_vn_edi_password` Char “SInvoice Password”
- `l10n_vn_edi_token` Char “SInvoice Access Token” (readonly)
- `l10n_vn_edi_token_expiry` Datetime “SInvoice Access Token Expiration Date” (readonly)
- `l10n_vn_edi_symbol_id` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “Default Symbol”

## `res.config.settings` (extends)

- `l10n_vn_edi_username` Char (related=company_id.l10n_vn_edi_username)
- `l10n_vn_edi_password` Char (related=company_id.l10n_vn_edi_password)
- `l10n_vn_edi_default_symbol_id` Many2one “Default Symbol” (related=company_id.l10n_vn_edi_symbol_id)

Public methods: `action_fetch_symbols`

## `res.partner` (extends)

- `invoice_edi_format` Selection

## `l10n_vn_edi_viettel.sinvoice.symbol` (defines)

SInvoice symbol

- `name` Char “Symbol” (required, readonly)
- `invoice_template_code` Char “Template Code” (required, readonly)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `active` Boolean

Public methods: `action_fetch_symbols`

## `account.move.reversal` (extends)

- `l10n_vn_edi_adjustment_type` Selection “Adjustment type” (required)
- `l10n_vn_edi_agreement_document_name` Char “Agreement Name”
- `l10n_vn_edi_agreement_document_date` Datetime “Agreement Date”

Public methods: `reverse_moves`

Extension points: `_prepare_default_reversal`
