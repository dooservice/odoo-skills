# l10n_ar_withholding — Argentina - Payment Withholdings

Depends on: l10n_ar, l10n_latam_check.

## `account.chart.template` (extends)


Extension points: `_post_load_demo_data`

## `account.chart.template` (extends)


Extension points: `_get_ar_base_res_company`, `_get_ar_base_withholding_account_account`, `_get_ar_ex_withholding_account_tax`, `_get_ar_ex_withholding_account_tax_group`, `_get_ar_ri_withholding_account_tax`, `_get_ar_ri_withholding_account_tax_group`

## `account.move` (extends)

- `l10n_ar_withholding_ids` One2many → `account.move.line` “Withholdings” (readonly, compute=_compute_l10n_ar_withholding_ids)

## `account.payment` (extends)


## `account.tax` (extends)

- `l10n_ar_withholding_payment_type` Selection (store, compute=_compute_l10n_ar_withholding_payment_type)
- `l10n_ar_withholding_sequence_id` Many2one → `ir.sequence`

## `res.company` (extends)

- `l10n_ar_tax_base_account_id` Many2one → `account.account` “Tax Base Account”

## `res.config.settings` (extends)

- `l10n_ar_tax_base_account_id` Many2one → `account.account` “Tax Base Account” (related=company_id.l10n_ar_tax_base_account_id)

## `account.payment.register` (extends)

- `l10n_ar_withholding_ids` One2many → `l10n_ar.payment.register.withholding` “Withholdings”
- `l10n_ar_net_amount` Monetary (readonly, compute=_compute_l10n_ar_net_amount)
- `l10n_ar_adjustment_warning` Boolean (compute=_compute_l10n_ar_adjustment_warning)

Extension points: `_create_payment_vals_from_wizard`, `_get_conversion_rate`

## `l10n_ar.payment.register.withholding` (defines)

Payment register withholding lines

- `payment_register_id` Many2one → `account.payment.register` (required)
- `company_id` Many2one (related=payment_register_id.company_id)
- `currency_id` Many2one (related=payment_register_id.currency_id)
- `name` Char “Number”
- `tax_id` Many2one → `account.tax` (required)
- `withholding_sequence_id` Many2one (related=tax_id.l10n_ar_withholding_sequence_id)
- `base_amount` Monetary (required)
- `amount` Monetary (required, store, compute=_compute_amount)
