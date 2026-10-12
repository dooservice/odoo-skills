# l10n_vn_edi_viettel_stock — Vietnam - Delivery E-invoicing

Depends on: l10n_vn_edi_viettel, stock.

## `res.company` (extends)

- `l10n_vn_edi_send_transfer_note` Boolean “Send Transfer Note to SInvoice”
- `l10n_vn_edi_stock_default_sinvoice_symbol_id` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “Default Delivery Symbol”

## `res.config.settings` (extends)

- `l10n_vn_edi_send_transfer_note` Boolean (related=company_id.l10n_vn_edi_send_transfer_note)
- `l10n_vn_edi_stock_default_sinvoice_symbol_id` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` (related=company_id.l10n_vn_edi_stock_default_sinvoice_symbol_id)

## `stock.move` (extends)

- `l10n_vn_edi_unit_price` Float “Vietnam EDI Unit Price” (store, compute=_compute_l10n_vn_edi_unit_price)
- `l10n_vn_edi_total_price` Float “Total Price” (compute=_compute_l10n_vn_edi_total_price)

## `stock.picking` (extends)

- `l10n_vn_edi_is_sent` Boolean “Sent to SInvoice” (readonly)
- `l10n_vn_edi_transaction_id` Char “SInvoice Transaction ID”
- `l10n_vn_edi_symbol_id` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “SInvoice Symbol” (store, compute=_compute_l10n_vn_edi_symbol_id)
- `l10n_vn_edi_invoice_number` Char “SInvoice Number” (readonly)
- `l10n_vn_edi_reservation_code` Char “Secret Code” (readonly)
- `l10n_vn_edi_issue_date` Datetime “Issue Date” (readonly)
- `l10n_vn_edi_sinvoice_file_id` Many2one → `ir.attachment` (readonly)
- `l10n_vn_edi_sinvoice_xml_file_id` Many2one → `ir.attachment` (readonly)
- `l10n_vn_edi_sinvoice_pdf_file_id` Many2one → `ir.attachment` (readonly)
- `l10n_vn_edi_show_send_button` Boolean (compute=_compute_l10n_vn_edi_show_send_button)

Public methods: `action_l10n_vn_send_to_sinvoice`, `l10n_vn_edi_fetch_files`

## `stock.warehouse` (extends)

- `l10n_vn_edi_sinvoice_symbol_id` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “Default Warehouse Symbol”
- `l10n_vn_edi_country_code` Char “Country” (related=company_id.country_code)

## `l10n_vn_edi_viettel_stock.send_wizard` (defines)

Send Transfer Note to SInvoice

- `picking_id` Many2one → `stock.picking` “Transfer” (required)
- `template_field_ids` One2many → `l10n_vn_edi_viettel_stock.template_field_line` “Template Fields”

Public methods: `action_send`

## `l10n_vn_edi_viettel_stock.template_field_line` (defines)

Template Field Line for SInvoice Transfer Note

- `wizard_id` Many2one → `l10n_vn_edi_viettel_stock.send_wizard` (required)
- `key_tag` Char “Key Tag” (required)
- `key_label` Char “Field” (required)
- `value` Char “Value”
- `value_type` Char “Value Type”
- `is_required` Boolean “Required”
- `is_seller` Boolean “Is Seller”
