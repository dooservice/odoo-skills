# Bank and reconciliation

A bank journal (`account.journal`, `type='bank'`) holds the bank's transactions as
statement lines (`account.bank.statement.line`). Each line is a posted entry: the bank
account against the journal's suspense account. Reconciling a line replaces the suspense
line with the real counterpart (a customer's receivable, a vendor's payable, a payment's
outstanding account, an expense) and matches it with the open item. Community has the
journals, the statement lines and the reconciliation models, but not the screen that
reconciles: the bank reconciliation view, the statement file importers (CAMT, OFX, QIF,
CSV) and bank synchronization are Enterprise (Accounting app). In Community the steps
below are done through the ORM, making the same journal-item changes that screen makes.
Every change here is accounting: get the user's yes first.

## Before you start

- Apps: `account` (Invoicing).
- Settings: none. Foreign-currency bank accounts need multi-currency, see `currencies-and-rates.md`.
- Read first:

```python
company = env.company
env['account.journal'].search_read([('company_id', '=', company.id), ('type', 'in', ('bank', 'cash'))], ['name', 'code', 'type', 'default_account_id', 'suspense_account_id', 'bank_account_id', 'currency_id'])
lines = env['account.bank.statement.line'].search([('company_id', '=', company.id), ('is_reconciled', '=', False)])
lines.read(['date', 'payment_ref', 'partner_id', 'amount', 'amount_residual', 'journal_id'])
env['account.reconcile.model'].search_read([('company_id', '=', company.id)], ['name', 'sequence', 'match_journal_ids'])
```

## The standard flow

1. **The bank journal.** Invoicing ‣ Configuration ‣ Accounting ‣ Journals (16.0 to
   20.0). The chart installs one bank journal; create one per bank account as in
   `taxes-and-journals.md`. Each has a bank account (`default_account_id`) and a
   suspense account (`suspense_account_id`, the company's by default).

2. **Register the transactions.** Invoicing ‣ Dashboard, the bank journal's card (it opens
   the journal's statements). Positive `amount` is money in, negative money out;
   `payment_ref` is the bank's label.

   ```python
   journal = env['account.journal'].search([('company_id', '=', company.id), ('type', '=', 'bank'), ('code', '=', '<journal code>')])
   line = env['account.bank.statement.line'].create({
       'journal_id': journal.id, 'date': '2026-10-15', 'amount': 1000.0,
       'payment_ref': '<label from the bank>', 'partner_id': partner.id,
   })
   env.cr.commit()
   ```

   Leaves a posted entry on the suspense account, `is_reconciled` False.

3. **Group them in a statement** (optional, to check balances against the bank's).

   ```python
   statement = env['account.bank.statement'].create({
       'name': '<statement reference>', 'balance_end_real': <closing balance on the statement>,
       'line_ids': [Command.set(lines.ids)],
   })
   env.cr.commit()
   ```

   `balance_start` comes from the previous statement; `is_complete` is True when
   `balance_end` (start plus lines) equals `balance_end_real`. Needs `from odoo import Command`.

4. **Match a line with an invoice or bill.** Point the suspense line to the invoice's
   receivable or payable account and reconcile the two.

   ```python
   invoice = env['account.move'].search([('name', '=', '<invoice number>'), ('company_id', '=', company.id), ('state', '=', 'posted')])
   counterpart = invoice.line_ids.filtered(lambda l: l.account_id.account_type in ('asset_receivable', 'liability_payable') and not l.reconciled)
   line.partner_id = invoice.commercial_partner_id
   _liquidity, suspense, _other = line._seek_for_lines()
   suspense.account_id = counterpart.account_id
   (suspense + counterpart).reconcile()
   env.cr.commit()
   ```

   Leaves the line `is_reconciled` and the invoice `paid` (or `partial` when the line is
   smaller). Community has no `in_payment` step: an invoice is `paid` as soon as a
   payment covers it.

5. **Or match it with a payment** already registered on the invoice, so the money is
   not counted twice: use the payment's outstanding line as the counterpart.

   ```python
   payment = env['account.payment'].search([('name', '=', '<payment number>'), ('company_id', '=', company.id)])
   counterpart = payment.move_id.line_ids.filtered(lambda l: l.account_id == payment.outstanding_account_id and not l.reconciled)
   line.partner_id = payment.partner_id.commercial_partner_id
   _liquidity, suspense, _other = line._seek_for_lines()
   suspense.account_id = counterpart.account_id
   (suspense + counterpart).reconcile()
   env.cr.commit()
   ```

   Leaves the payment `is_matched`. In Community every payment gets a journal entry on
   an outstanding account, so there is always a line to match.

## Variations

- **Write-off** (bank charges, rounding, a small underpayment the user forgives): book the
  difference on an account the user names, in the same entry, then reconcile.

  ```python
  counterpart = invoice.line_ids.filtered(lambda l: l.account_id.account_type in ('asset_receivable', 'liability_payable') and not l.reconciled)
  _liquidity, suspense, _other = line._seek_for_lines()
  difference = counterpart.amount_residual + suspense.balance
  line.move_id.with_context(skip_readonly_check=True).write({'line_ids': [
      Command.update(suspense.id, {'account_id': counterpart.account_id.id, 'balance': -counterpart.amount_residual, 'amount_currency': -counterpart.amount_residual}),
      Command.create({'name': '<write-off label>', 'account_id': writeoff_account.id, 'partner_id': line.partner_id.id, 'balance': difference, 'amount_currency': difference}),
  ]})
  _liquidity, _suspense, other = line._seek_for_lines()
  (other.filtered(lambda l: l.account_id == counterpart.account_id) + counterpart).reconcile()
  env.cr.commit()
  ```

  For a bank and an invoice in the company currency. In another currency, stop and ask.
- **A line that is only an expense** (fees, interest): `suspense.account_id = <account>`
  and nothing to reconcile.
- **Load many lines from a spreadsheet**: `env['account.bank.statement.line'].load(fields, rows)`
  with `journal_id/id` (or the name), `date`, `payment_ref`, `amount`, the generic
  import every list offers. The bank-format importers are Enterprise.
- **Reconciliation models**: rules stored in Community and applied by the Enterprise
  screen (buttons, suggestions, automatic matching). Creating one does nothing in a
  Community database: say so before the user relies on it. Menu: Invoicing ‣
  Configuration ‣ Banks ‣ Reconciliation Models in 16.0 to 18.0, shown only to an
  accounting administrator who also has "Show Full Accounting Features"
  (`account.group_account_user`); no menu in Community from 19.0.

  ```python
  env['account.reconcile.model'].create({
      'name': 'Bank charges', 'rule_type': 'writeoff_suggestion',        # 16.0 to 18.0
      # 'trigger': 'manual',                                             # 19.0 and 20.0, instead of rule_type
      'match_journal_ids': [Command.set(journal.ids)],
      'match_label': 'contains', 'match_label_param': '<text in the bank label>',
      'line_ids': [Command.create({'account_id': writeoff_account.id, 'amount_type': 'percentage', 'amount_string': '100', 'label': 'Bank charges'})],
  })
  env.cr.commit()
  ```

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| model kind | `rule_type`: `writeoff_button`, `writeoff_suggestion`, `invoice_matching` | same | same | `trigger`: `manual`, `auto_reconcile`; no `rule_type` | `trigger`; `rule_type`: `reco_model`, `matching_rule` |
| auto-validate | `auto_reconcile` | same | same | `trigger='auto_reconcile'` | same |
| reconciliation models menu | Configuration ‣ Banks | same | same | none in Community | none in Community |
| editing a posted statement entry's lines | allowed | allowed | needs `skip_readonly_check` | same | same |

## Verify

```python
line.invalidate_recordset()
print(line.is_reconciled, line.amount_residual, [(l.account_id.code, l.balance, l.reconciled) for l in line.move_id.line_ids])
print(invoice.payment_state, invoice.amount_residual)
print(env['account.bank.statement.line'].search_count([('company_id', '=', company.id), ('is_reconciled', '=', False)]))
```

## Pitfalls

- **Unreconciling history.** `line.action_undo_reconciliation()` puts the line back on
  suspense and reopens the invoice; on a period already reported or locked, it changes
  what was declared. Never without the user's explicit yes, and never in bulk.
- **Matching an invoice that has a payment.** The invoice is already `paid`: match the
  payment (step 5), or the money is booked twice and the outstanding account never clears.
- **Wrong sign.** A customer receipt is a positive `amount`; a vendor payment negative.
- **Lock dates** refuse changes in a locked period; see `closing-the-period.md`.
