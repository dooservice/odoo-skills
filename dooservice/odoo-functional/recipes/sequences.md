# Sequences

Most documents number themselves from an `ir.sequence` found by its code: quotations
(`sale.order`), purchase orders (`purchase.order`), transfers (each picking type has
its own). Invoices and journal entries do not: their numbers come from the journal, see
`taxes-and-journals.md`.

```python
sequence = env['ir.sequence'].search([('code', '=', 'sale.order'), ('company_id', 'in', [company.id, False])])
sequence.write({'prefix': 'QT/%(year)s/', 'padding': 5})
env.cr.commit()
```

- `number_next_actual` is the next number; lowering it reuses numbers already given:
  never do it without the user saying so.
- `%(year)s`, `%(month)s`, `%(day)s` in `prefix` or `suffix`; `use_date_range` restarts
  the count each period.
- One sequence per company when there are several: check `company_id` before writing.
