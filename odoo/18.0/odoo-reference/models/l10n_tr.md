# l10n_tr — Türkiye - Accounting

Depends on: account.

## `account.journal` (extends)

- `l10n_tr_default_sales_return_account_id` Many2one → `account.account` (store, compute=_compute_l10n_tr_default_sales_return_account_id)

## `account.move.line` (extends)


Public methods: `copy_data`

## `product.template` (extends)

- `l10n_tr_default_sales_return_account_id` Many2one → `account.account` (company_dependent)

Public methods: `create`

## `account.chart.template` (extends)


Extension points: `_get_tr_res_company`, `_get_tr_template_data`
