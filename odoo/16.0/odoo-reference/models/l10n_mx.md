# l10n_mx — Mexico - Accounting

Depends on: account.

## `account.account` (extends)


Public methods: `create`

## `account.tax.template` (extends)

- `l10n_mx_tax_type` Selection “Factor Type”

Extension points: `_get_tax_vals`

## `account.tax` (extends)

- `l10n_mx_tax_type` Selection “Factor Type”

## `account.chart.template` (extends)


Public methods: `generate_journals`

Extension points: `_prepare_all_journals`

## `res.bank` (extends)

- `l10n_mx_edi_code` Char “ABM Code”

## `res.partner.bank` (extends)

- `l10n_mx_edi_clabe` Char “CLABE”

## `res.config.settings` (extends)

- `module_l10n_mx_edi` Boolean “Mexican Electronic Invoicing”
