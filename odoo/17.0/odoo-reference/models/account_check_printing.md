# account_check_printing — Check Printing Base

Depends on: account.

## `account.journal` (extends)

- `check_manual_sequencing` Boolean “Manual Numbering”
- `check_sequence_id` Many2one → `ir.sequence` “Check Sequence” (readonly)
- `check_next_number` Char “Next Check Number” (compute=_compute_check_next_number)

Public methods: `action_checks_to_print`, `create`

Extension points: `_create_check_sequence`, `_get_journal_dashboard_data_batched`

## `account.move` (extends)

- `preferred_payment_method_id` Many2one → `account.payment.method` “Preferred Payment Method” (store, compute=_compute_preferred_payment_method_idd)

## `account.payment.register` (extends)


## `account.payment` (extends)

- `check_amount_in_words` Char “Amount in Words” (store, compute=_compute_check_amount_in_words)
- `check_manual_sequencing` Boolean (related=journal_id.check_manual_sequencing)
- `check_number` Char “Check Number” (readonly, store, compute=_compute_check_number)
- `payment_method_line_id` Many2one (index)
- `show_check_number` Boolean (compute=_compute_show_check_number)

Public methods: `action_post`, `action_unmark_sent`, `action_void_check`, `do_print_checks`, `print_checks`

Extension points: `_check_build_page_info`, `_check_fill_line`, `_check_get_pages`, `_check_make_stub_pages`, `_get_aml_default_display_name_list`

## `account.payment.method` (extends)


Extension points: `_get_payment_method_information`

## `res.company` (extends)

- `account_check_printing_layout` Selection “Check Layout”
- `account_check_printing_date_label` Boolean “Print Date Label”
- `account_check_printing_multi_stub` Boolean “Multi-Pages Check Stub”
- `account_check_printing_margin_top` Float “Check Top Margin”
- `account_check_printing_margin_left` Float “Check Left Margin”
- `account_check_printing_margin_right` Float “Right Margin”

## `res.config.settings` (extends)

- `account_check_printing_layout` Selection “Check Layout” (related=company_id.account_check_printing_layout)
- `account_check_printing_date_label` Boolean “Print Date Label” (related=company_id.account_check_printing_date_label)
- `account_check_printing_multi_stub` Boolean “Multi-Pages Check Stub” (related=company_id.account_check_printing_multi_stub)
- `account_check_printing_margin_top` Float “Check Top Margin” (related=company_id.account_check_printing_margin_top)
- `account_check_printing_margin_left` Float “Check Left Margin” (related=company_id.account_check_printing_margin_left)
- `account_check_printing_margin_right` Float “Check Right Margin” (related=company_id.account_check_printing_margin_right)

## `res.partner` (extends)

- `property_payment_method_id` Many2one → `account.payment.method` “Payment Method” (company_dependent)

## `print.prenumbered.checks` (defines)

Print Pre-numbered Checks

- `next_check_number` Char “Next Check Number” (required)

Public methods: `print_checks`

Extension points: `_check_next_check_number`
