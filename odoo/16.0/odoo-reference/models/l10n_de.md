# l10n_de — Germany - Accounting

Depends on: account, base_iban, base_vat, l10n_din5008.

## `account.journal` (extends)


Extension points: `_prepare_liquidity_account_vals`

## `account.chart.template` (extends)


Extension points: `_create_liquidity_journal_suspense_account`, `_prepare_transfer_account_template`

## `account.tax.template` (extends)

- `l10n_de_datev_code` Char

Extension points: `_get_tax_vals`

## `account.tax` (extends)

- `l10n_de_datev_code` Char

## `product.template` (extends)


Extension points: `_get_product_accounts`

## `ir.actions.report` (extends)


Extension points: `_get_rendering_context`

## `res.company` (extends)

- `l10n_de_stnr` Char “St.-Nr.”
- `l10n_de_widnr` Char “W-IdNr.”

Public methods: `get_l10n_de_stnr_national`
