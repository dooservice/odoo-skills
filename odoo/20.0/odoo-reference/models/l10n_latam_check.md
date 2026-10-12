# l10n_latam_check — Third Party and Deferred/Electronic Checks Management

Depends on: account.

## `account.chart.template` (extends)


Extension points: `_get_latam_check_account_journal`, `_get_latam_check_outstanding_account_account`, `_get_third_party_checks_country_codes`

## `account.journal` (extends)


Public methods: `create`

Extension points: `_get_reusable_payment_methods`

## `account.move` (extends)


Public methods: `button_draft`

## `account.move.line` (extends)

- `l10n_latam_check_ids` One2many → `l10n_latam.check` “Checks”

## `account.payment` (extends)

- `l10n_latam_new_check_ids` One2many → `l10n_latam.check` “Checks”
- `l10n_latam_move_check_ids` Many2many → `l10n_latam.check` “Checks Operations” (required)
- `l10n_latam_checks_amount` Monetary “Checks Amount” (compute=_compute_l10n_latam_checks_amount)
- `l10n_latam_check_warning_msg` Text (compute=_compute_l10n_latam_check_warning_msg)
- `amount` Monetary (store, compute=_compute_amount)

Public methods: `action_cancel`, `action_draft`, `action_post`

Extension points: `_check_move_id`, `_check_no_later_operation`, `_get_blocking_l10n_latam_warning_msg`, `_get_latam_checks`, `_get_reconciled_checks_error`, `_get_trigger_fields_to_synchronize`, `_prepare_move_liquidity_lines`

## `account.payment.method` (extends)


Extension points: `_get_payment_method_information`

## `l10n_latam.check` (defines)

Account payment check

Inherits: `mail.thread`, `mail.activity.mixin`

- `payment_id` Many2one → `account.payment` (required)
- `operation_ids` Many2many → `account.payment` (readonly)
- `on_hand` Boolean (compute=_compute_on_hand)
- `current_journal_id` Many2one → `account.journal` (store, compute=_compute_current_journal)
- `name` Char “Number”
- `issuer_vat` Char (store, compute=_compute_issuer_vat)
- `payment_date` Date (required)
- `amount` Monetary
- `outstanding_line_id` Many2one → `account.move.line` (readonly)
- `issue_state` Selection (store, compute=_compute_issue_state)
- `payment_method_code` Char (related=payment_id.payment_method_code)
- `partner_id` Many2one (related=payment_id.partner_id)
- `original_journal_id` Many2one (related=payment_id.journal_id)
- `company_id` Many2one → `res.company` (store, compute=_compute_company_id)
- `currency_id` Many2one (related=payment_id.currency_id)
- `first_payment_date` Date “First Payment Date” (related=payment_id.date)
- `memo` Char (related=payment_id.memo)
- `payment_method_line_id` Many2one (store, related=payment_id.payment_method_line_id)
- `bank_account_id` Many2one → `res.partner.bank` (store, compute=_compute_bank_account_id)

Public methods: `action_show_journal_entry`, `action_show_reconciled_move`, `action_void`, `button_open_check_operations`, `button_open_payment`

Extension points: `_check_issuer_vat`, `_get_last_operation`, `_get_operations`, `_get_reconciled_move`, `_prepare_void_move_vals`

## `account.payment.register` (extends)

- `l10n_latam_new_check_ids` One2many → `l10n_latam.payment.register.check` “New Checks”
- `l10n_latam_move_check_ids` Many2many → `l10n_latam.check` “Checks”
- `l10n_latam_checks_amount` Monetary “Checks Amount” (compute=_compute_l10n_latam_checks_amount)

Public methods: `action_create_payments`

Extension points: `_create_payment_vals_from_wizard`

## `l10n_latam.payment.mass.transfer` (defines)

Checks Mass Transfers

- `company_ids` Many2many → `res.company`
- `from_journal_id` Many2one → `account.journal`
- `from_journal_currency_id` Many2one (related=from_journal_id.currency_id)
- `to_journal_id` Many2one → `account.journal` “Destination Journal” (required)
- `check_ids` Many2many → `l10n_latam.check`
- `payment_date` Date “Payment Date” (required)
- `communication` Char “Memo”

Public methods: `action_create_payments`, `default_get`

Extension points: `_check_source_journal`, `_create_payments`, `_get_source_journal`

## `l10n_latam.payment.register.check` (defines)

Payment register check

- `payment_register_id` Many2one → `account.payment.register` (required)
- `company_id` Many2one (related=payment_register_id.company_id)
- `currency_id` Many2one (related=payment_register_id.currency_id)
- `name` Char “Number”
- `issuer_vat` Char (store, compute=_compute_issuer_vat)
- `payment_date` Date (required)
- `amount` Monetary
- `bank_account_id` Many2one → `res.partner.bank` (store, compute=_compute_bank_account_id)
