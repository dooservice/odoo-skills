# Sequences

Most documents number themselves from an `ir.sequence`: quotations and sales orders
(code `sale.order`), purchase orders (`purchase.order`), transfers (the sequence of each
picking type). Invoices, bills, payments and journal entries do not: their numbers come
from the journal, see `taxes-and-journals.md`. A number already given is part of the
history users and customers have seen: change only the numbers still to come.

## Read first

```python
company = env.company
sequences = env['ir.sequence'].search([('code', 'in', ['sale.order', 'purchase.order']), ('company_id', 'in', [company.id, False])])
sequences.read(['name', 'code', 'company_id', 'prefix', 'suffix', 'padding', 'number_next_actual', 'use_date_range', 'implementation'])
env['sale.order'].search([('company_id', '=', company.id)], order='id desc', limit=3).mapped('name')
```

## Change the format

```python
sequence = env['ir.sequence'].search([('code', '=', 'sale.order'), ('company_id', 'in', [company.id, False])], limit=1)
sequence.write({'prefix': 'QT/%(year)s/', 'padding': 5})
env.cr.commit()
```

- Placeholders in `prefix` and `suffix`: `%(year)s`, `%(y)s` (two digits), `%(month)s`,
  `%(day)s`, `%(doy)s`, `%(woy)s`, `%(weekday)s`, `%(h24)s`, `%(h12)s`, `%(min)s`,
  `%(sec)s`. Each has a `%(range_...)s` twin that uses the date range instead of today.
- `padding` is the number of digits; `number_increment` the step.
- Sale and purchase sequences ship with `company_id` empty, shared by all companies.
  For a different format per company (Spain and Mexico companies in one database),
  copy it with `sequence.copy({'company_id': company.id, 'prefix': ...})`: the sequence
  of the document's company wins over the shared one.

## Restart each year

```python
sequence.write({'use_date_range': True})
env.cr.commit()
```

With `use_date_range`, each period (`ir.sequence.date_range`, created on first use for
the calendar year) has its own `number_next_actual`, so numbering restarts at 1.

## The next number

`number_next_actual` is the next number to give. Raising it skips numbers (fine, say so).
Lowering it reuses numbers already given and can fail on unique names: never without
the user's explicit yes, after checking no document has that number.

```python
sequence.write({'number_next_actual': 1500})
env.cr.commit()
```

- `implementation`: `standard` is fast but a cancelled transaction loses its number;
  `no_gap` never skips but locks the row. Keep the default unless gaps are a legal
  problem for that document.

## Transfers

Each `stock.picking.type` has its own `sequence_id`; receipts and deliveries of each
warehouse number apart (`WH/IN/00001`, `WH/OUT/00001`).

```python
picking_type = env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1).out_type_id
picking_type.sequence_id.write({'prefix': 'MAD/OUT/', 'padding': 6})
env.cr.commit()
```

- `sequence_code` on the picking type is a separate required field up to 19.0 (used to
  build the prefix when the type is created); in 20.0 it is the sequence prefix itself.

## Versions

The `ir.sequence` fields and placeholders above are the same from 16.0 to 20.0.
