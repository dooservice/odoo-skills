# l10n_no — Norway - Accounting

Depends on: account, base_iban, base_vat.

## `account.journal` (extends)

- `invoice_reference_model` Selection

## `account.move` (extends)


Extension points: `_get_invoice_reference_no_invoice`, `_get_invoice_reference_no_partner`, `_get_kid_number`

## `res.company` (extends)

- `l10n_no_bronnoysund_number` Char (related=partner_id.l10n_no_bronnoysund_number)

## `res.partner` (extends)

- `l10n_no_bronnoysund_number` Char “Register of Legal Entities (Brønnøysund Register Center)”
