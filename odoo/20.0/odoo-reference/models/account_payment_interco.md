# account_payment_interco — Intercompany Payment - Account

Depends on: account_payment.

## `account.move` (extends)


Extension points: `_check_interco_clearing`

## `res.company` (extends)

- `account_interco_clearing_journal_id` Many2one → `account.journal` “Intercompany Clearing Journal”
- `account_interco_payable_id` Many2one → `account.account` “Intercompany Clearing Payable Account”
- `account_interco_receivable_id` Many2one → `account.account` “Intercompany Clearing Receivable Account”

## `res.config.settings` (extends)

- `account_interco_clearing_journal_id` Many2one → `account.journal` (related=company_id.account_interco_clearing_journal_id)
- `account_interco_payable_id` Many2one → `account.account` (related=company_id.account_interco_payable_id)
- `account_interco_receivable_id` Many2one → `account.account` (related=company_id.account_interco_receivable_id)
