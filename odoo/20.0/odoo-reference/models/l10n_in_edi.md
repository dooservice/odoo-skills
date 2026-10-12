# l10n_in_edi — Indian - E-invoicing

Depends on: l10n_in.

## `account.journal` (extends)


Public methods: `action_l10n_in_einvoice_open_pending`

Extension points: `_get_journal_dashboard_data_batched`

## `account.move` (extends)

- `l10n_in_edi_status` Selection “India E-Invoice Status” (readonly)
- `l10n_in_edi_attachment_id` Many2one → `ir.attachment` “E-Invoice(IN) Attachment”
- `l10n_in_edi_attachment_file` Binary “E-Invoice(IN) File”
- `l10n_in_edi_cancel_reason` Selection “E-Invoice(IN) Cancel Reason”
- `l10n_in_edi_cancel_remarks` Char “E-Invoice(IN) Cancel Remarks”
- `l10n_in_edi_content` Binary “E-Invoice(IN) Content” (compute=_compute_l10n_in_edi_content)
- `l10n_in_edi_error` Html (readonly)

Public methods: `action_export_l10n_in_edi_content_json`, `action_l10n_in_edi_force_cancel`, `button_draft`, `button_request_cancel`

Extension points: `_get_l10n_in_edi_line_details`, `_get_l10n_in_edi_partner_details`, `_get_l10n_in_edi_response_json`

## `account.move.line` (extends)


## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`, `_get_invoice_extra_attachments`

## `ir.attachment` (extends)


## `res.company` (extends)

- `l10n_in_edi_feature` Boolean “Indian E-Invoicing”
- `l10n_in_edi_username` Char “E-invoice (IN) Username”
- `l10n_in_edi_password` Char “E-invoice (IN) Password”
- `l10n_in_edi_token` Char “E-invoice (IN) Token”
- `l10n_in_edi_token_validity` Datetime “E-invoice (IN) Valid Until”

## `res.config.settings` (extends)

- `l10n_in_edi_feature` Boolean (related=company_id.l10n_in_edi_feature)
- `l10n_in_edi_username` Char “Indian EDI username” (related=company_id.l10n_in_edi_username)
- `l10n_in_edi_password` Char “Indian EDI password” (related=company_id.l10n_in_edi_password)

Public methods: `l10n_in_edi_test`

## `res.partner` (extends)


## `l10n_in_edi.cancel` (defines)

Cancel E-Invoice

- `move_id` Many2one → `account.move` “Invoice” (required)
- `cancel_reason` Selection “Cancel Reason” (required)
- `cancel_remarks` Char “Cancel Remarks” (required)

Public methods: `cancel_l10n_in_edi_move`
