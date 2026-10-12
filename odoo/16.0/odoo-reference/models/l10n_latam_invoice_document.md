# l10n_latam_invoice_document — LATAM Document

Depends on: account, account_debit_note.

## `account.chart.template` (extends)


Extension points: `_prepare_all_journals`

## `account.journal` (extends)

- `l10n_latam_use_documents` Boolean “Use Documents?”
- `l10n_latam_company_use_documents` Boolean (compute=_compute_l10n_latam_company_use_documents)

Public methods: `check_use_document`

## `account.move` (extends)

- `l10n_latam_available_document_type_ids` Many2many → `l10n_latam.document.type` (compute=_compute_l10n_latam_available_document_types)
- `l10n_latam_document_type_id` Many2one → `l10n_latam.document.type` “Document Type” (store, compute=_compute_l10n_latam_document_type)
- `l10n_latam_document_number` Char “Document Number” (readonly, compute=_compute_l10n_latam_document_number)
- `l10n_latam_use_documents` Boolean (related=journal_id.l10n_latam_use_documents)
- `l10n_latam_manual_document_number` Boolean “Manual Number” (compute=_compute_l10n_latam_manual_document_number)
- `l10n_latam_document_type_id_code` Char “Doc Type” (related=l10n_latam_document_type_id.code)

Extension points: `_check_invoice_type_document_type`, `_check_l10n_latam_documents`, `_check_unique_sequence_number`, `_check_unique_vendor_number`, `_get_l10n_latam_documents_domain`, `_get_starting_sequence`

## `account.move.line` (extends)

- `l10n_latam_document_type_id` Many2one (store, related=move_id.l10n_latam_document_type_id)

## `l10n_latam.document.type` (defines)

Latam Document Type

- `active` Boolean
- `sequence` Integer (required)
- `country_id` Many2one → `res.country` (required, index)
- `name` Char (required)
- `doc_code_prefix` Char “Document Code Prefix”
- `code` Char
- `report_name` Char “Name on Reports”
- `internal_type` Selection

Public methods: `name_get`

## `res.company` (extends)


## `account.invoice.report` (extends)

- `l10n_latam_document_type_id` Many2one → `l10n_latam.document.type` (index)

## `account.debit.note` (extends)


Public methods: `create_debit`

## `account.move.reversal` (extends)

- `l10n_latam_use_documents` Boolean (compute=_compute_documents_info)
- `l10n_latam_document_type_id` Many2one → `l10n_latam.document.type` (store, compute=_compute_document_type)
- `l10n_latam_available_document_type_ids` Many2many → `l10n_latam.document.type` (compute=_compute_documents_info)
- `l10n_latam_document_number` Char “Document Number”
- `l10n_latam_manual_document_number` Boolean “Manual Number” (compute=_compute_l10n_latam_manual_document_number)

Extension points: `_prepare_default_reversal`
