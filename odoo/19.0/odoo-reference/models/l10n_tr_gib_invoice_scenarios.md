# l10n_tr_gib_invoice_scenarios — Türkiye - Nilvera E-Invoice Commercial and Return

Depends on: l10n_tr_nilvera_einvoice_extended.

## `account.edi.xml.ubl.tr` (extends)


Extension points: `_get_document_nsmap`, `_get_document_template`, `_get_tags_for_document_type`

## `account.move` (extends)

- `l10n_tr_nilvera_send_status` Selection
- `l10n_tr_gib_invoice_scenario` Selection
- `l10n_tr_gib_invoice_type` Selection
- `l10n_tr_original_invoice_date` Date “Original Invoice Date”
- `l10n_tr_ticarifatura_last_checked_at` Datetime “Commercial Status Check Date”

Public methods: `l10n_tr_action_approve_ticarifatura`, `l10n_tr_action_fetch_ticarifatura_response`, `l10n_tr_action_reject_ticarifatura`, `l10n_tr_nilvera_get_pdf`

Extension points: `_get_starting_sequence`

## `account.move.line` (extends)

- `l10n_tr_original_line_id` Many2one → `account.move.line` (readonly)
- `l10n_tr_original_quantity` Float “Original Quantity”
- `l10n_tr_original_tax_without_withholding` Monetary “Original Tax After Withholding”

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_invoice_extra_attachments`

## `l10n_tr.ticarifatura.response.wizard` (defines)

Response Wizard for Bills of type Ticarifatura E-Invoice

- `move_id` Many2one → `account.move` (required)
- `response_code` Selection “Response Code” (required)
- `response_note` Text “Response Note”

Public methods: `action_proceed`
