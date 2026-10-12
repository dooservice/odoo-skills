# l10n_de — Germany - Accounting

Depends on: base_iban, base_vat, l10n_din5008, account.

## `account.account` (extends)


Public methods: `write`

## `account.journal` (extends)


Extension points: `_prepare_liquidity_account_vals`

## `account.move` (extends)


## `account.chart.template` (extends)


Extension points: `_get_de_res_company`

## `account.tax` (extends)

- `l10n_de_datev_code` Char

## `product.template` (extends)


Extension points: `_get_product_accounts`

## `ir.actions.report` (extends)


Extension points: `_get_rendering_context`

## `ir.attachment` (extends)


Public methods: `unlink`, `write`

## `res.company` (extends)

- `l10n_de_stnr` Char “St.-Nr.”
- `l10n_de_widnr` Char “W-IdNr.”

Public methods: `get_l10n_de_stnr_national`, `write`

## `res.partner` (extends)


Extension points: `_get_company_registry_labels`

## `account.chart.template` (extends)


Extension points: `_get_de_skr03_reconcile_model`, `_get_de_skr03_res_company`, `_get_de_skr03_template_data`

## `account.chart.template` (extends)


Extension points: `_get_de_skr04_reconcile_model`, `_get_de_skr04_res_company`, `_get_de_skr04_template_data`
