# l10n_mx — Mexico - Accounting

Depends on: account.

## `account.account` (extends)


Public methods: `create`

## `account.move.line` (extends)


## `account.tax` (extends)

- `l10n_mx_factor_type` Selection “Factor Type”
- `l10n_mx_tax_type` Selection “SAT Tax Type” (store, compute=_compute_l10n_mx_tax_type)

## `res.company` (extends)

- `l10n_mx_income_return_discount_account_id` Many2one → `account.account` “Income account for returns and discounts”
- `l10n_mx_income_re_invoicing_account_id` Many2one → `account.account` “Income account for re-invoicing”

## `res.config.settings` (extends)

- `l10n_mx_account_income_return_discount_id` Many2one → `account.account` “Income Returns and Discounts Account” (related=company_id.l10n_mx_income_return_discount_account_id)

## `account.chart.template` (extends)


Extension points: `_get_account_parent_xmlid`, `_get_accounts_data_values`, `_get_mx_account_account`, `_get_mx_account_journal`, `_get_mx_res_company`, `_get_mx_template_data`
