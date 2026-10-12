# l10n_jo_edi_extended — Jordan E-Invoicing Extended Features

Depends on: l10n_jo_edi.

## `account.move` (extends)

- `l10n_jo_edi_invoice_type` Selection “Invoice Type” (store, compute=_compute_l10n_jo_edi_invoice_type)
- `l10n_jo_edi_payment_method` Selection “JoFotara Payment Method”
- `l10n_jo_edi_state` Selection

Extension points: `_get_invoice_payment_method_code`, `_get_invoice_scope_code`

## `res.company` (extends)

- `l10n_jo_edi_demo_mode` Boolean “JoFotara Demo Mode”

## `res.config.settings` (extends)

- `l10n_jo_edi_demo_mode` Boolean “JoFotara Demo Mode” (related=company_id.l10n_jo_edi_demo_mode)

## `account.move.send` (extends)

- `l10n_jo_edi_demo_mode` Boolean (related=company_id.l10n_jo_edi_demo_mode)
