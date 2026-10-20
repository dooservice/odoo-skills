# Closing the period

Closing a month, quarter or year means checking that everything in it is posted and
reconciled, allocating the year's result, then setting lock dates on the company
(`res.company`) so nobody changes it. Odoo posts no closing entry by itself. Which periods must be closed, when the tax return is due and how the result is
allocated depend on the country and the company's statutes: the country's localization
decides this; see its localization skill if installed. The Accounting app
(`account_accountant`), its Lock Dates form, fiscal years and financial reports (balance
sheet, profit and loss, tax report, aged balances) are Enterprise; this recipe uses what
Community has. Every step is an accounting change and needs the user's yes.

## Before you start

- Apps: `account` (the Invoicing menu). Journal Entries and Journal Items appear only
  for users in `account.group_account_readonly` or above.
- Settings: none. The fiscal year end is `fiscalyear_last_month` and `fiscalyear_last_day`
  on the company (the Settings field for it is Enterprise).
- Read first:

```python
company = env.company
lock_fields = [f for f in ('period_lock_date', 'fiscalyear_lock_date', 'tax_lock_date',
                           'sale_lock_date', 'purchase_lock_date', 'hard_lock_date') if f in company._fields]
print(company.read(lock_fields + ['fiscalyear_last_day', 'fiscalyear_last_month']))
print(company.get_unaffected_earnings_account().read(['code', 'name', 'account_type']))
print(company.read(['currency_exchange_journal_id', 'income_currency_exchange_account_id', 'expense_currency_exchange_account_id']))
```

## The standard flow

The order of Odoo's year-end documentation; a month or quarter stops after step 3.

1. **Check the period is complete.** Invoicing ‣ Accounting ‣ Journals ‣ Journal Entries
   (16.0, 17.0), Invoicing ‣ Accounting ‣ Journal Entries (18.0), Invoicing ‣ Accounting ‣
   Transactions ‣ Journal Entries (19.0, 20.0), filtered on drafts. Drafts are posted or
   deleted, bank lines reconciled (`bank-and-reconciliation.md`), expenses and payments
   entered. Ask about bills not yet entered, accruals and depreciation: the accountant
   decides those entries. Changes nothing.

   ```python
   import datetime
   period_end = datetime.date(2026, 3, 31)
   Move = env['account.move']
   print('draft entries', Move.search_count([('company_id', '=', company.id), ('state', '=', 'draft'), ('date', '<=', period_end)]))
   print('unreconciled bank lines', env['account.bank.statement.line'].search_count([('company_id', '=', company.id), ('is_reconciled', '=', False), ('date', '<=', period_end)]))
   print('open invoices and bills', Move.search_count([('company_id', '=', company.id), ('state', '=', 'posted'), ('date', '<=', period_end),
       ('move_type', 'in', ('out_invoice', 'out_refund', 'in_invoice', 'in_refund')), ('payment_state', 'in', ('not_paid', 'partial'))]))
   ```

2. **Check the balances.** The tax report and the balance sheet are Enterprise. In
   Community, read the journal items (Invoicing ‣ Accounting ‣ Journals ‣ Journal Items in
   16.0, 17.0; Invoicing ‣ Accounting ‣ Journal Items in 18.0; Invoicing ‣ Review ‣ Control ‣
   Journal Items in 19.0, 20.0) or sum them, and compare with the bank statements and the
   accountant's figures. The year's result:

   ```python
   start, end = datetime.date(2025, 1, 1), datetime.date(2025, 12, 31)
   lines = env['account.move.line'].search([('company_id', '=', company.id), ('parent_state', '=', 'posted'), ('date', '>=', start),
       ('date', '<=', end), ('account_id.internal_group', 'in', ('income', 'expense'))])
   print('result (profit > 0)', -sum(lines.mapped('balance')))
   ```

3. **Lock the period for the review.** Accounting ‣ Accounting ‣ Lock Dates is Enterprise;
   in Community write the company. 16.0, 17.0: the Journal Entries lock
   (`period_lock_date`), which Advisers (`account.group_account_manager`) can still pass.
   18.0 on: Lock Everything (`fiscalyear_lock_date`), for everyone: at year end, post the
   allocation of step 4 first, or open an exception (Variations). Monthly and quarterly
   closes also set the tax lock. Leaves entries on or before the date unchangeable.

   ```python
   field = 'period_lock_date' if 'period_lock_date' in company._fields else 'fiscalyear_lock_date'
   company.write({field: period_end, 'tax_lock_date': period_end})
   env.cr.commit()
   ```

4. **Allocate the year's result** (year end only). Journal Entries ‣ New, dated the last
   day of the fiscal year, from the "Current Year Earnings" account (`equity_unaffected`,
   the one `get_unaffected_earnings_account()` returns) to the accounts the accountant
   gives: retained earnings, reserves, dividends. Prepare it as a draft; the user posts it.

   ```python
   journal = env['account.journal'].search([('company_id', '=', company.id), ('type', '=', 'general')], limit=1)
   domain = [('company_ids', 'in', company.id)] if 'company_ids' in env['account.account']._fields else [('company_id', '=', company.id)]
   retained = env['account.account'].search(domain + [('code', '=', '<account code>')])
   amount = 1000.0   # a profit; for a loss swap debit and credit
   move = env['account.move'].create({'journal_id': journal.id, 'date': end, 'ref': 'Allocation of the 2025 result', 'line_ids': [
       (0, 0, {'account_id': company.get_unaffected_earnings_account().id, 'name': 'Result 2025', 'debit': amount}),
       (0, 0, {'account_id': retained.id, 'name': 'Result 2025', 'credit': amount}),
   ]})
   env.cr.commit()
   ```

   Leaves the entry in `draft`. Posted after a lock that covers its date, it is moved
   into the next period.

5. **Lock the year.** 16.0, 17.0: the All Users lock (`fiscalyear_lock_date`) on the last
   day of the fiscal year. 18.0 on: Lock Everything on that day, and, once the user
   confirms the year is final, the Hard Lock (`hard_lock_date`), which can never be
   lowered or removed. Same write as step 3 with these fields.

## Variations

- **Sales or purchase only** (18.0 on): `sale_lock_date` or `purchase_lock_date` lock those
  journals while the rest stays open.
- **A late correction after the lock** (18.0 on): instead of moving the lock back, an
  Adviser opens a temporary exception for one user, or everyone without `user_id`:

  ```python
  env['account.lock_exception'].create({   # 18.0 on
      'company_id': company.id, 'user_id': user.id, 'lock_date_field': 'fiscalyear_lock_date', 'lock_date': datetime.date(2026, 1, 31),
      'reason': '<why>', 'end_datetime': datetime.datetime.now() + datetime.timedelta(hours=2),
  })
  env.cr.commit()
  ```

- **Irreversible lock in 16.0, 17.0:** the Community module `account_lock`; installing it
  is the user's decision.
- **Exchange differences:** realized ones are posted automatically when a foreign-currency
  invoice is reconciled with its payment, in `currency_exchange_journal_id` on the income
  or expense exchange account (check all three are set). Revaluing open balances at the
  closing rate is an Enterprise report; in Community it is a miscellaneous entry with the
  accountant's amounts. Rates: `currencies-and-rates.md`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| lock fields | `period_lock_date`, `fiscalyear_lock_date`, `tax_lock_date` | same | `fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date`, `hard_lock_date` | same | same |
| a lock is refused by | drafts or unreconciled bank lines (year lock) | same | unreconciled bank lines; drafts only for the hard lock | same | same |
| lock exceptions | no | no | `account.lock_exception` | same | same |
| Current Year Earnings accounts | one per company, carried forward | same | same | several allowed, not carried forward | same |
| Community reports | Invoice Analysis | same | + Audit Trail | + Analytic Report | same |

## Verify

```python
print(company.read(lock_fields))
print(move.state, move.date, sum(move.line_ids.mapped('debit')) == sum(move.line_ids.mapped('credit')))
print(Move.search_count([('company_id', '=', company.id), ('state', '=', 'draft'), ('date', '<=', period_end)]))
```

## Pitfalls

- A new entry posted with a locked date is not refused: Odoo moves its accounting date
  after the lock and numbers it there. Check the date of anything posted late.
- 19.0 on, the generic chart has two Current Year Earnings accounts: ask which one the
  result goes through before step 4.
- The hard lock is irreversible: only with the user's explicit yes for that date.
- Resetting a posted entry in a locked period to draft is refused: reverse it in an open
  period.
