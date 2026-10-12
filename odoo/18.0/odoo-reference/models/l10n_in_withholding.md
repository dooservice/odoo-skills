# l10n_in_withholding — Indian - TDS and TCS

Depends on: l10n_in.

## `account.account` (extends)

- `l10n_in_tds_tcs_section_id` Many2one → `l10n_in.section.alert` “TCS/TDS Section”

## `account.chart.template` (extends)


Extension points: `_get_in_base_res_company`, `_get_in_withholding_account_account`, `_get_in_withholding_account_tax`

## `account.move` (extends)

- `l10n_in_is_withholding` Boolean “Is Indian TDS Entry”
- `l10n_in_withholding_ref_move_id` Many2one → `account.move` “Indian TDS Ref Move” (readonly)
- `l10n_in_withhold_move_ids` One2many → `account.move` “Indian TDS Entries”
- `l10n_in_withholding_line_ids` One2many → `account.move.line` “Indian TDS Lines” (compute=_compute_l10n_in_withholding_line_ids)
- `l10n_in_total_withholding_amount` Monetary “Total Indian TDS Amount” (compute=_compute_l10n_in_total_withholding_amount)
- `l10n_in_tcs_tds_warning` Char “TDC/TCS Warning” (compute=_compute_l10n_in_tcs_tds_warning)
- `l10n_in_display_higher_tcs_button` Boolean “Display higher TCS button” (compute=_compute_l10n_in_display_higher_tcs_button)

Public methods: `action_l10n_in_apply_higher_tax`, `action_l10n_in_withholding_entries`

Extension points: `_get_l10n_in_invalid_tax_lines`, `_get_sections_aggregate_sum_by_pan`

## `account.move.line` (extends)

- `l10n_in_withhold_tax_amount` Monetary “TDS Tax Amount” (compute=_compute_withhold_tax_amount)

## `account.payment` (extends)

- `l10n_in_total_withholding_amount` Monetary (related=move_id.l10n_in_total_withholding_amount)
- `l10n_in_withhold_move_ids` One2many (related=move_id.l10n_in_withhold_move_ids)

Public methods: `action_l10n_in_withholding_entries`

## `account.tax` (extends)

- `l10n_in_tds_tax_type` Selection “TDS Tax Type”
- `l10n_in_section_id` Many2one → `l10n_in.section.alert` “Section”

## `l10n_in.section.alert` (defines)

indian section alert

- `name` Char “Section Name”
- `tax_source_type` Selection “Tax Source Type”
- `consider_amount` Selection “Consider” (required)
- `is_per_transaction_limit` Boolean “Per Transaction”
- `per_transaction_limit` Float “Per Transaction limit”
- `is_aggregate_limit` Boolean “Aggregate”
- `aggregate_limit` Float “Aggregate limit”
- `aggregate_period` Selection “Aggregate Period”
- `l10n_in_section_tax_ids` One2many → `account.tax` “Taxes”

Extension points: `_get_warning_message`

## `res.company` (extends)

- `l10n_in_withholding_account_id` Many2one → `account.account` “TDS Account”
- `l10n_in_withholding_journal_id` Many2one → `account.journal` “TDS Journal”

## `res.config.settings` (extends)

- `l10n_in_withholding_account_id` Many2one (related=company_id.l10n_in_withholding_account_id)
- `l10n_in_withholding_journal_id` Many2one (related=company_id.l10n_in_withholding_journal_id)

## `l10n_in.withhold.wizard` (defines)

Withhold Wizard

- `reference` Char “Reference”
- `type_name` Char “Type” (compute=_compute_type_name)
- `related_move_id` Many2one → `account.move` “Invoice/Bill” (readonly)
- `related_payment_id` Many2one → `account.payment` “Payment” (readonly)
- `company_id` Many2one → `res.company` “Company” (compute=_compute_company_id)
- `currency_id` Many2one “Currency” (related=company_id.currency_id)
- `journal_id` Many2one → `account.journal` “Journal” (required, store, compute=_compute_journal)
- `date` Date “Date”
- `l10n_in_tds_tax_type` Char “Indian Tax Type” (compute=_compute_l10n_in_tds_tax_type)
- `withhold_line_ids` One2many → `l10n_in.withhold.wizard.line` “TDS Lines” (store)
- `l10n_in_withholding_warning` Json “Withholding warning” (compute=_compute_l10n_in_withholding_warning)

Public methods: `action_create_and_post_withhold`, `default_get`

Extension points: `_get_withhold_type`, `_prepare_withhold_header`, `_prepare_withhold_move_lines`

## `l10n_in.withhold.wizard.line` (defines)

Withhold Wizard Lines

- `base` Monetary “Base”
- `currency_id` Many2one (related=withhold_id.currency_id)
- `l10n_in_tds_tax_type` Char (related=withhold_id.l10n_in_tds_tax_type)
- `withhold_id` Many2one → `l10n_in.withhold.wizard` (required)
- `tax_id` Many2one → `account.tax` “TDS Tax” (required)
- `amount` Monetary “TDS Amount” (store, compute=_compute_amount)

Extension points: `_check_amounts`
