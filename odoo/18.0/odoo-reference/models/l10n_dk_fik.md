# l10n_dk_fik — Denmark - FIK Number

Depends on: l10n_dk.

## `account.journal` (extends)

- `invoice_reference_model` Selection
- `l10n_dk_fik_creditor_number` Char “FIK Creditor Number” (store, compute=_compute_l10n_dk_fik_creditor_number)

Extension points: `_check_fik_creditor_number`

## `account.move` (extends)


Extension points: `_get_invoice_reference_dk_fik`, `_get_invoice_reference_dk_fik_71_invoice`, `_get_invoice_reference_dk_fik_75_invoice`
