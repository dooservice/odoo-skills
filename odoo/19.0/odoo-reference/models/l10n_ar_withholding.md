# l10n_ar_withholding — Argentina - Payment Withholdings

Depends on: l10n_ar, l10n_latam_check.

## `account.chart.template` (extends)


Extension points: `_post_load_demo_data`

## `account.chart.template` (extends)


Extension points: `_get_ar_base_res_company`, `_get_ar_base_withholding_account_account`, `_get_ar_ex_withholding_account_tax`, `_get_ar_ex_withholding_account_tax_group`, `_get_ar_ri_withholding_account_tax`, `_get_ar_ri_withholding_account_tax_group`

## `account.move` (extends)

- `l10n_ar_withholding_ids` One2many → `account.move.line` “Withholdings” (readonly, compute=_compute_l10n_ar_withholding_ids)

## `account.payment` (extends)

- `l10n_ar_withholding_ids` One2many (related=move_id.l10n_ar_withholding_ids)

## `account.tax` (extends)

- `l10n_ar_type_tax_use` Selection “Argentina Tax Type” (compute=_compute_l10n_ar_type_tax_use)
- `l10n_ar_withholding_payment_type` Selection “Argentina Withholding Payment Type”
- `l10n_ar_tax_type` Selection “WTH Tax”
- `l10n_ar_withholding_sequence_id` Many2one → `ir.sequence` “WTH Sequence”
- `l10n_ar_code` Char “ARCA Code”
- `l10n_ar_non_taxable_amount` Float “Non Taxable Amount”
- `l10n_ar_minimum_threshold` Float “Minimum Treshold”
- `l10n_ar_state_id` Many2one → `res.country.state` “Jurisdiction”
- `l10n_ar_scale_id` Many2one → `l10n_ar.earnings.scale` “Scale”

Extension points: `_prepare_base_line_tax_repartition_grouping_key`

## `l10n_ar.earnings.scale` (defines)

l10n_ar.earnings.scale

- `name` Char (required)
- `line_ids` One2many → `l10n_ar.earnings.scale.line`

## `l10n_ar.earnings.scale.line` (defines)

l10n_ar.earnings.scale.line

- `scale_id` Many2one → `l10n_ar.earnings.scale` (required)
- `currency_id` Many2one → `res.currency`
- `from_amount` Monetary “From $” (compute=_compute_from_amount)
- `to_amount` Monetary “To $”
- `fixed_amount` Monetary “$”
- `percentage` Monetary “Add %”
- `excess_amount` Monetary “S/ Exceeding $”

## `l10n_ar.partner.tax` (defines)

Argentinean Partner Taxes

- `partner_id` Many2one → `res.partner` (required)
- `tax_id` Many2one → `account.tax` (required)
- `company_id` Many2one (store, related=tax_id.company_id)
- `from_date` Date “From Date”
- `to_date` Date “To Date”
- `ref` Char “ref”

Public methods: `check_partner_tax_dates`

## `res.company` (extends)

- `l10n_ar_tax_base_account_id` Many2one → `account.account` “Tax Base Account”

## `res.config.settings` (extends)

- `l10n_ar_tax_base_account_id` Many2one → `account.account` “Tax Base Account” (related=company_id.l10n_ar_tax_base_account_id)

## `res.partner` (extends)

- `l10n_ar_partner_tax_ids` One2many → `l10n_ar.partner.tax`

## `account.payment.register` (extends)

- `l10n_ar_withholding_ids` One2many → `l10n_ar.payment.register.withholding` “Withholdings” (store, compute=_compute_l10n_ar_withholding_ids)
- `l10n_ar_net_amount` Monetary (readonly, compute=_compute_l10n_ar_net_amount)
- `l10n_ar_adjustment_warning` Boolean (compute=_compute_l10n_ar_adjustment_warning)

Public methods: `action_create_payments`

Extension points: `_create_payment_vals_from_wizard`, `_get_conversion_rate`

## `l10n_ar.payment.register.withholding` (defines)

Payment register withholding lines

- `payment_register_id` Many2one → `account.payment.register` (required)
- `company_id` Many2one (related=payment_register_id.company_id)
- `currency_id` Many2one (related=payment_register_id.currency_id)
- `name` Char “Number”
- `tax_id` Many2one → `account.tax` (required)
- `withholding_sequence_id` Many2one (related=tax_id.l10n_ar_withholding_sequence_id)
- `base_amount` Monetary (required, store, compute=_compute_base_amount)
- `amount` Monetary (required, store, compute=_compute_amount)
