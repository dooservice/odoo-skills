# l10n_ar_withholding — Argentina - Payment Withholdings

Depends on: l10n_ar, l10n_latam_check, l10n_account_withholding_tax.

## `account.chart.template` (extends)


Extension points: `_get_ar_base_withholding_demo_account_tax`, `_get_ar_withholding_ir_sequence_demo`, `_get_ar_withholding_partner_tax_demo`, `_get_ar_witholding_account_tax_demo`

## `account.chart.template` (extends)


Extension points: `_get_ar_base_withholding_account_account`, `_get_ar_base_withholding_res_company`, `_get_ar_ex_withholding_account_tax`, `_get_ar_ex_withholding_account_tax_group`, `_get_ar_ri_withholding_account_tax`, `_get_ar_ri_withholding_account_tax_group`

## `account.payment` (extends)


Extension points: `_check_withholding_line_sequence_number`

## `account.payment.withholding.line` (extends)


## `account.tax` (extends)

- `l10n_ar_withholding_tax_type` Selection “Argentine Withhold type”
- `l10n_ar_code` Char “ARCA Code”
- `l10n_ar_non_taxable_amount` Float “Non Taxable Amount”
- `l10n_ar_minimum_threshold` Float “Minimum Threshold”
- `l10n_ar_state_id` Many2one → `res.country.state` “Jurisdiction”
- `l10n_ar_scale_id` Many2one → `l10n_ar.earnings.scale` “Scale”

Public methods: `create`, `write`

Extension points: `_check_l10n_ar_withholding_tax_type_alignment`, `_prepare_base_line_tax_repartition_grouping_key`

## `account.withholding.line` (extends)


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
- `fixed_amount` Monetary “$” (compute=_compute_fixed_amount)
- `percentage` Float “Add %”

## `l10n_ar.partner.tax` (defines)

Argentinean Partner Taxes

- `partner_id` Many2one → `res.partner` (required)
- `tax_id` Many2one → `account.tax` (required)
- `company_id` Many2one (store, related=tax_id.company_id)
- `from_date` Date “From Date”
- `to_date` Date “To Date”
- `ref` Char “ref”

Extension points: `_check_partner_tax_dates`

## `res.partner` (extends)

- `l10n_ar_partner_tax_ids` One2many → `l10n_ar.partner.tax`

## `account.payment.register` (extends)


Extension points: `_get_default_withhold`

## `account.payment.register.withholding.line` (extends)
