# l10n_mx — Mexico - Accounting

Depends on: account.

## `account.account` (extends)


Public methods: `create`

## `account.tax` (extends)

- `l10n_mx_factor_type` Selection “Factor Type”
- `l10n_mx_tax_type` Selection “SAT Tax Type” (store, compute=_compute_l10n_mx_tax_type)

## `res.bank` (extends)

- `l10n_mx_edi_code` Char “ABM Code”

## `res.partner.bank` (extends)

- `l10n_mx_edi_clabe` Char “CLABE”

## `res.config.settings` (extends)

- `module_l10n_mx_edi` Boolean “Mexican Electronic Invoicing”

Public methods: `get_views`

## `account.chart.template` (extends)


Extension points: `_get_accounts_data_values`, `_get_mx_account_journal`, `_get_mx_res_company`, `_get_mx_template_data`
