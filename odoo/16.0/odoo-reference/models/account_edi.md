# account_edi — Import/Export Invoices From XML/PDF

Depends on: account.

## `account.edi.document` (defines)

Electronic Document for an account.move

- `move_id` Many2one → `account.move` (required, index)
- `edi_format_id` Many2one → `account.edi.format` (required)
- `attachment_id` Many2one → `ir.attachment`
- `state` Selection
- `error` Html
- `blocking_level` Selection
- `name` Char (related=attachment_id.name)
- `edi_format_name` Char “Format Name” (related=edi_format_id.name)
- `edi_content` Binary (compute=_compute_edi_content)

Public methods: `action_export_xml`

Extension points: `_prepare_jobs`

## `account.edi.format` (defines)

EDI format

- `name` Char
- `code` Char (required)

Public methods: `create`

Extension points: `_check_move_configuration`, `_create_document_from_attachment`, `_create_invoice_from_binary`, `_create_invoice_from_pdf_reader`, `_create_invoice_from_xml_tree`, `_get_move_applicability`, `_prepare_invoice_report`

## `account.journal` (extends)

- `edi_format_ids` Many2many → `account.edi.format` “Electronic invoicing” (store, compute=_compute_edi_format_ids)
- `compatible_edi_ids` Many2many → `account.edi.format` (compute=_compute_compatible_edi_ids)

Public methods: `write`

## `account.move` (extends)

- `edi_document_ids` One2many → `account.edi.document`
- `edi_state` Selection “Electronic invoicing” (store, compute=_compute_edi_state)
- `edi_error_count` Integer (compute=_compute_edi_error_count)
- `edi_blocking_level` Selection (compute=_compute_edi_error_message)
- `edi_error_message` Html (compute=_compute_edi_error_message)
- `edi_web_services_to_process` Text (compute=_compute_edi_web_services_to_process)
- `edi_show_cancel_button` Boolean (compute=_compute_edi_show_cancel_button)
- `edi_show_abandon_cancel_button` Boolean (compute=_compute_edi_show_abandon_cancel_button)

Public methods: `action_process_edi_web_services`, `action_retry_edi_documents_error`, `button_abandon_cancel_posted_posted_moves`, `button_cancel`, `button_cancel_posted_moves`, `button_draft`, `button_process_edi_web_services`

Extension points: `_check_edi_documents_for_reset_to_draft`, `_get_create_document_from_attachment_decoders`, `_get_edi_attachment`, `_get_edi_document`, `_get_update_invoice_from_attachment_decoders`, `_prepare_edi_tax_details`, `_prepare_edi_vals_to_export`

## `account.move.line` (extends)


Public methods: `reconcile`

Extension points: `_prepare_edi_vals_to_export`

## `account.payment` (extends)


Public methods: `action_process_edi_web_services`, `action_retry_edi_documents_error`

## `ir.actions.report` (extends)


## `ir.attachment` (extends)


## `mail.template` (extends)


Public methods: `generate_email`

Extension points: `_get_edi_attachments`

## `uom.uom` (extends)


Extension points: `_get_unece_code`

## `account.resequence.wizard` (extends)


Public methods: `resequence`
