# l10n_it_edi_ndd — Italy - E-invoicing - Additional module to support the debit notes (nota di debito - NDD)

Depends on: l10n_it_edi.

## `account.move` (extends)

- `l10n_it_payment_method` Selection (store, compute=_compute_l10n_it_payment_method)
- `l10n_it_document_type` Many2one → `l10n_it.document.type` (store, compute=_compute_l10n_it_document_type)

## `account.payment.method.line` (extends)

- `l10n_it_payment_method` Selection “Italian Payment Method”

Extension points: `_get_l10n_it_payment_method_selection_code`

## `l10n_it.document.type` (defines)

Italian Document Type

- `name` Char (required)
- `code` Char (required)
- `type` Selection

Extension points: `_check_code_unique`
