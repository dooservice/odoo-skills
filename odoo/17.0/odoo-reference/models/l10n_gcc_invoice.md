# l10n_gcc_invoice — G.C.C. - Arabic/English Invoice

Depends on: account.

## `account.move` (extends)

- `narration` Html

Extension points: `_get_name_invoice_report`

## `account.move.line` (extends)

- `l10n_gcc_invoice_tax_amount` Float “Tax Amount” (compute=_compute_tax_amount)

## `product.product` (extends)
