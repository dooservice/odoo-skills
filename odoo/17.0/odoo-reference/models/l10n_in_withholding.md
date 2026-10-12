# l10n_in_withholding — Indian - TDS

Depends on: l10n_in.

## `account.chart.template` (extends)


Extension points: `_get_in_base_res_company`, `_get_in_withholding_account_account`, `_get_in_withholding_account_tax`

## `account.move` (extends)

- `l10n_in_is_withholding` Boolean “Is Indian TDS Entry”
- `l10n_in_withholding_ref_move_id` Many2one → `account.move` “Indian TDS Ref Move” (readonly)
- `l10n_in_withhold_move_ids` One2many → `account.move` “Indian TDS Entries”
- `l10n_in_withholding_line_ids` One2many → `account.move.line` “Indian TDS Lines” (compute=_compute_l10n_in_withholding_line_ids)
- `l10n_in_total_withholding_amount` Monetary “Total Indian TDS Amount” (compute=_compute_l10n_in_total_withholding_amount)

Public methods: `action_l10n_in_withholding_entries`

## `account.move.line` (extends)

- `l10n_in_withhold_tax_amount` Monetary “TDS Tax Amount” (compute=_compute_withhold_tax_amount)

## `account.payment` (extends)


Public methods: `action_l10n_in_withholding_entries`

## `account.tax` (extends)

- `l10n_in_tds_tax_type` Selection “TDS Tax Type”

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
- `warning_message` Char (compute=_compute_warning_message)

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
