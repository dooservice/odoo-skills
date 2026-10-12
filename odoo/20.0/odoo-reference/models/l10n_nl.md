# l10n_nl — Netherlands - Accounting

Depends on: account, account_edi_ubl_cii.

## `account.chart.template` (extends)


Extension points: `_post_load_data`

## `account.journal` (extends)


Extension points: `_prepare_liquidity_account_vals`

## `res.company` (extends)

- `l10n_nl_rounding_difference_loss_account_id` Many2one → `account.account`
- `l10n_nl_rounding_difference_profit_account_id` Many2one → `account.account`
- `l10n_nl_sbr_ob_nummer` Char (related=partner_id.l10n_nl_sbr_ob_nummer)

## `res.partner` (extends)

- `l10n_nl_sbr_ob_nummer` Char (compute=_compute_l10n_nl_sbr_ob_nummer)

## `account.chart.template` (extends)


Extension points: `_get_nl_account_account`, `_get_nl_res_company`, `_get_nl_template_data`
