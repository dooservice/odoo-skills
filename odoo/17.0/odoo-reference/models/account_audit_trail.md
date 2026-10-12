# account_audit_trail — Account Audit Trail

Depends on: account.

## `account.bank.statement.line` (extends)


Public methods: `unlink`

## `account.move` (extends)


Public methods: `unlink`

## `mail.message` (extends)

- `account_audit_log_preview` Html “Description” (compute=_compute_account_audit_log_preview)
- `account_audit_log_move_id` Many2one → `account.move` “Journal Entry” (compute=_compute_account_audit_log_move_id)
- `account_audit_log_partner_id` Many2one → `res.partner` “Partner” (compute=_compute_account_audit_log_partner_id)
- `account_audit_log_account_id` Many2one → `account.account` “Account” (compute=_compute_account_audit_log_account_id)
- `account_audit_log_tax_id` Many2one → `account.tax` “Tax” (compute=_compute_account_audit_log_tax_id)
- `account_audit_log_company_id` Many2one → `res.company` “Company ” (compute=_compute_account_audit_log_company_id)
- `account_audit_log_display_name` Char (compute=_compute_account_audit_log_display_name)
- `show_audit_log` Boolean (compute=_compute_show_audit_log)

Public methods: `write`

## `mail.tracking.value` (extends)


Public methods: `write`

## `base.partner.merge.automatic.wizard` (extends)


## `res.company` (extends)

- `check_account_audit_trail` Boolean “Audit Trail”

## `res.config.settings` (extends)

- `check_account_audit_trail` Boolean “Audit Trail” (related=company_id.check_account_audit_trail)

Extension points: `_check_audit_trail_records`
