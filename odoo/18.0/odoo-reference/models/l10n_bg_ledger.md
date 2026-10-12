# l10n_bg_ledger — Bulgaria - Report ledger

Depends on: l10n_bg.

## `account.journal` (extends)

- `l10n_bg_customer_invoice` Selection “Customer Invoices”
- `l10n_bg_credit_notes` Selection “Credit Notes”
- `l10n_bg_debit_notes` Selection “Debit Notes”

## `account.move` (extends)

- `l10n_bg_document_type` Selection “Document Type (BG)” (store, compute=_compute_l10n_bg_document_type)
- `l10n_bg_document_number` Char “Document Number (BG)” (compute=_compute_l10n_bg_document_number)
- `l10n_bg_exemption_reason` Selection “Exemption reason (BG)”
