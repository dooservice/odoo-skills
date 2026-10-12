# l10n_latam_check — Third Party and Deferred/Electronic Checks Management

Depends on: account_check_printing, base_vat.

## `account.chart.template` (extends)


Extension points: `_get_latam_check_account_journal`, `_get_third_party_checks_country_codes`

## `account.journal` (extends)

- `l10n_latam_manual_checks` Boolean “Use electronic and deferred checks”

Extension points: `_check_l10n_latam_manual_checks`

## `account.payment` (extends)

- `l10n_latam_check_id` Many2one → `account.payment` “Check”
- `l10n_latam_check_operation_ids` One2many → `account.payment` “Check Operations” (readonly)
- `l10n_latam_check_current_journal_id` Many2one → `account.journal` “Check Current Journal” (store, compute=_compute_l10n_latam_check_current_journal)
- `l10n_latam_check_warning_msg` Text (compute=_compute_l10n_latam_check_warning_msg)
- `l10n_latam_check_number` Char (compute=_compute_l10n_latam_check_number)
- `l10n_latam_check_bank_id` Many2one → `res.bank` “Check Bank” (store, compute=_compute_l10n_latam_check_bank_id)
- `l10n_latam_check_issuer_vat` Char “Check Issuer VAT” (store, compute=_compute_l10n_latam_check_issuer_vat)
- `l10n_latam_check_payment_date` Date “Check Cash-In Date”
- `l10n_latam_manual_checks` Boolean (related=journal_id.l10n_latam_manual_checks)

Public methods: `action_draft`, `action_post`, `action_unmark_sent`, `button_open_check_operations`

Extension points: `_check_l10n_latam_check_id`, `_check_l10n_latam_check_issuer_vat`, `_create_paired_internal_transfer_payment`, `_get_blocking_l10n_latam_warning_msg`, `_get_payment_method_codes_to_exclude`, `_get_trigger_fields_to_synchronize`, `_prepare_move_line_default_vals`

## `account.payment.method` (extends)


Extension points: `_get_payment_method_information`

## `account.payment.register` (extends)

- `l10n_latam_check_id` Many2one → `account.payment` “Check”
- `l10n_latam_check_bank_id` Many2one → `res.bank` “Check Bank” (store, compute=_compute_l10n_latam_check_bank_id)
- `l10n_latam_check_issuer_vat` Char “Check Issuer VAT” (store, compute=_compute_l10n_latam_check_issuer_vat)
- `l10n_latam_check_number` Char “Check Number”
- `l10n_latam_manual_checks` Boolean (related=journal_id.l10n_latam_manual_checks)
- `l10n_latam_check_payment_date` Date “Check Cash-In Date”

Extension points: `_create_payment_vals_from_wizard`

## `l10n_latam.payment.mass.transfer` (defines)

Checks Mass Transfers

- `payment_date` Date “Payment Date” (required)
- `destination_journal_id` Many2one → `account.journal` “Destination Journal”
- `communication` Char “Memo”
- `journal_id` Many2one → `account.journal` (compute=_compute_journal_company)
- `company_id` Many2one → `res.company` (compute=_compute_journal_company)
- `check_ids` Many2many → `account.payment`

Public methods: `action_create_payments`, `default_get`

Extension points: `_create_payments`
