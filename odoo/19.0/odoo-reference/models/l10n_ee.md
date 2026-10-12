# l10n_ee — Estonia - Accounting

Depends on: account, account_edi_ubl_cii.

## `account.tax` (extends)

- `l10n_ee_kmd_inf_code` Selection “KMD INF Code”

## `res.company` (extends)

- `l10n_ee_rounding_difference_loss_account_id` Many2one → `account.account`
- `l10n_ee_rounding_difference_profit_account_id` Many2one → `account.account`

## `account.chart.template` (extends)


Extension points: `_get_ee_account_account`, `_get_ee_res_company`, `_get_ee_template_data`
