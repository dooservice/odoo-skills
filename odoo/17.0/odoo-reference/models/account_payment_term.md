# account_payment_term — Payment Term - Days end of month on the

Depends on: account.

## `account.payment.term.line` (extends)

- `delay_type` Selection
- `display_days_next_month` Boolean (compute=_compute_display_days_next_month)
- `days_next_month` Char “Days on the next month” (store)

Extension points: `_check_valid_char_value`, `_get_due_date`
