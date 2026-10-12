# l10n_hu_edi — Hungary - E-invoicing

Depends on: account_debit_note, base_iban, l10n_hu.

## `account.move` (extends)

- `l10n_hu_payment_mode` Selection “Payment mode”
- `l10n_hu_edi_state` Selection “NAV 3.0 status”
- `l10n_hu_edi_batch_upload_index` Integer “Index of invoice within a batch upload”
- `l10n_hu_edi_attachment` Binary “Invoice XML file”
- `l10n_hu_edi_send_time` Datetime “Invoice upload time”
- `l10n_hu_edi_transaction_code` Char “Transaction Code”
- `l10n_hu_edi_messages` Json “Transaction messages (JSON)”
- `l10n_hu_invoice_chain_index` Integer “Invoice Chain Index”
- `l10n_hu_edi_attachment_filename` Char “Invoice XML filename” (compute=_compute_l10n_hu_edi_attachment_filename)
- `l10n_hu_edi_message_html` Html “Transaction messages” (compute=_compute_message_html)

Public methods: `button_request_cancel`, `l10n_hu_edi_button_hide_banner`, `l10n_hu_edi_button_update_status`

Extension points: `_check_posted_if_active`, `_get_name_invoice_report`

## `account.move.line` (extends)


## `account.tax` (extends)

- `l10n_hu_tax_type` Selection “NAV VAT Tax Type”
- `l10n_hu_tax_reason` Char “NAV VAT Tax Exemption Reason” (compute=_compute_l10n_hu_tax_reason)

## `product.template` (extends)

- `l10n_hu_product_code_type` Selection “Product Code Type”
- `l10n_hu_product_code` Char “Product Code Value”

## `res.company` (extends)

- `l10n_hu_group_vat` Char (related=partner_id.l10n_hu_group_vat)
- `l10n_hu_tax_regime` Selection “NAV Tax Regime”
- `l10n_hu_edi_server_mode` Selection “Server Mode”
- `l10n_hu_edi_username` Char “NAV Username”
- `l10n_hu_edi_password` Char “NAV Password”
- `l10n_hu_edi_signature_key` Char “NAV Signature Key”
- `l10n_hu_edi_replacement_key` Char “NAV Replacement Key”
- `l10n_hu_edi_last_transaction_recovery` Datetime “Last transaction recovery (in production mode)”

## `res.config.settings` (extends)

- `l10n_hu_tax_regime` Selection (related=company_id.l10n_hu_tax_regime)
- `l10n_hu_edi_server_mode` Selection (related=company_id.l10n_hu_edi_server_mode)
- `l10n_hu_edi_username` Char (related=company_id.l10n_hu_edi_username)
- `l10n_hu_edi_password` Char (related=company_id.l10n_hu_edi_password)
- `l10n_hu_edi_signature_key` Char (related=company_id.l10n_hu_edi_signature_key)
- `l10n_hu_edi_replacement_key` Char (related=company_id.l10n_hu_edi_replacement_key)
- `l10n_hu_edi_is_active` Boolean (compute=_compute_l10n_hu_edi_is_active)

Public methods: `create`

## `res.partner` (extends)

- `l10n_hu_group_vat` Char “Group Tax ID” (index)

## `account.chart.template` (extends)


Extension points: `_get_hu_account_tax`

## `uom.uom` (extends)

- `l10n_hu_edi_code` Selection “NAV UoM code”

## `account.debit.note` (extends)


Extension points: `_prepare_default_values`

## `account.move.reversal` (extends)


Public methods: `reverse_moves`

Extension points: `_prepare_default_reversal`

## `account.move.send` (extends)

- `l10n_hu_edi_actionable_errors` Json (compute=_compute_l10n_hu_edi_actionable_errors)
- `l10n_hu_edi_enable_nav_30` Boolean (compute=_compute_l10n_hu_edi_enable_nav_30)
- `l10n_hu_edi_checkbox_nav_30` Boolean “NAV 3.0” (store, compute=_compute_l10n_hu_edi_checkbox_nav_30)

Extension points: `_get_wizard_values`, `_prepare_invoice_pdf_report`

## `l10n_hu_edi.cancellation` (defines)

Technical Annulment Wizard

- `invoice_id` Many2one → `account.move` “Invoice to cancel”
- `code` Selection “Annulment Code” (required)
- `reason` Char “Annulment Reason” (required)

Public methods: `button_request_cancel`

## `l10n_hu_edi.tax_audit_export` (defines)

Tax audit export - Adóhatósági Ellenőrzési Adatszolgáltatás

- `selection_mode` Selection “Selection mode”
- `date_from` Date “Date From”
- `date_to` Date “Date To”
- `name_from` Char “Name From”
- `name_to` Char “Name To”
- `filename` Char “File name” (compute=_compute_filename)
- `export_file` Binary “Generated File” (readonly)

Public methods: `action_export`
