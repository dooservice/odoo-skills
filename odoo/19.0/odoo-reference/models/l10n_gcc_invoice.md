# l10n_gcc_invoice — Gulf Cooperation Council - Invoice

Depends on: account.

## `account.move` (extends)

- `narration` Html

Public methods: `create`

Extension points: `_get_name_invoice_report`

## `account.move.line` (extends)

- `l10n_gcc_invoice_tax_amount` Float “Tax Amount” (compute=_compute_tax_amount)
- `l10n_gcc_line_name` Char (compute=_compute_l10n_gcc_line_name)

Extension points: `_get_child_lines`

## `product.product` (extends)


## `res.company` (extends)

- `l10n_gcc_dual_language_invoice` Boolean “GCC Formatted Invoices”
- `l10n_gcc_country_is_gcc` Boolean (compute=_compute_l10n_gcc_country_is_gcc)

## `res.config.settings` (extends)

- `l10n_gcc_dual_language_invoice` Boolean (related=company_id.l10n_gcc_dual_language_invoice)
- `l10n_gcc_country_is_gcc` Boolean (related=company_id.l10n_gcc_country_is_gcc)
