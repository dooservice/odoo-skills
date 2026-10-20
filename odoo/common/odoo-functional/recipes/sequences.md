# Sequences

Most documents number themselves from an `ir.sequence`: quotations and sales orders
(code `sale.order`), purchase orders (`purchase.order`), transfers (the sequence of each
operation type). Invoices, bills, payments and journal entries do not: their numbers come
from the journal, see `taxes-and-journals.md`. The exception: from 18.0 a payment without
a journal entry takes its number from the `account.payment` sequence. Sequences are in
`base`; the documents that use them come with `sale`, `purchase` and `stock`. A number
already given is part of the history users and customers have seen: change only the
numbers still to come.

## Before you start

- Apps: `base`; `sale`, `purchase`, `stock` for their documents.
- Settings: none. The Sequences menu is under Settings ‣ Technical, which needs
  developer mode; transfers are numbered from the operation type, without it.
- Read first:

```python
company = env.company
sequences = env['ir.sequence'].search([('code', 'in', ['sale.order', 'purchase.order']), ('company_id', 'in', [company.id, False])])
sequences.read(['name', 'code', 'company_id', 'prefix', 'suffix', 'padding', 'number_next_actual', 'use_date_range', 'implementation'])
env['sale.order'].search([('company_id', '=', company.id)], order='id desc', limit=3).mapped('name')
```

## The standard flow

Odoo has no functional page for `ir.sequence`: its interface is the Sequences menu in
developer mode, with the format, the yearly restart and the next number on one form.
Transfers are the exception, numbered from the Sequence Prefix of their operation type
(Odoo's Inventory documentation).

1. **Change the format.** Settings ‣ Technical ‣ Sequences & Identifiers ‣ Sequences ‣
   the sequence (search by its code): Prefix, Suffix, Sequence Size.

   ```python
   sequence = env['ir.sequence'].search([('code', '=', 'sale.order'), ('company_id', 'in', [company.id, False])], limit=1)
   sequence.write({'prefix': 'QT/%(year)s/', 'padding': 5})
   env.cr.commit()
   ```

   Leaves the next documents numbered `QT/2026/00042`; those already numbered keep
   theirs.

   - Placeholders in `prefix` and `suffix`: `%(year)s`, `%(y)s` (two digits),
     `%(month)s`, `%(day)s`, `%(doy)s`, `%(woy)s`, `%(weekday)s`, `%(h24)s`, `%(h12)s`,
     `%(min)s`, `%(sec)s`. Each has a `%(range_...)s` twin that uses the date range
     instead of today.
   - `padding` is the number of digits; `number_increment` the step.
   - Sale and purchase sequences ship with `company_id` empty, shared by all companies.
     For a different format per company (two companies in one database), copy it with
     `sequence.copy({'company_id': company.id, 'prefix': ...})`: the sequence of the
     document's company wins over the shared one.

2. **Restart each year.** The same form ‣ Use subsequences per date_range.

   ```python
   sequence.write({'use_date_range': True})
   env.cr.commit()
   ```

   Leaves numbering per period: each period (`ir.sequence.date_range`, created on
   first use for the calendar year) has its own `number_next_actual`, so numbering
   restarts at 1. Turned on in the middle of a year, the current year also restarts at
   1 and repeats numbers already given (sale and purchase names are not unique, so
   nothing stops it). Unless the prefix changes too, create this year's period with the
   current number first:

   ```python
   import datetime
   year = datetime.date.today().year
   env['ir.sequence.date_range'].create({
       'sequence_id': sequence.id,
       'date_from': f'{year}-01-01', 'date_to': f'{year}-12-31',
       'number_next_actual': sequence.number_next_actual,
   })
   sequence.write({'use_date_range': True})
   env.cr.commit()
   ```

3. **Set the next number.** The same form ‣ Next Number (`number_next_actual`, Actual Next Number). `number_next_actual` is the
   next number to give. Raising it skips numbers (fine, say so). Lowering it reuses
   numbers already given: most document names are not unique, so Odoo gives the same
   number twice without complaint. Never without the user's explicit yes, after
   checking no document has that number.

   ```python
   sequence.write({'number_next_actual': 1500})
   env.cr.commit()
   ```

   Leaves the next document numbered 1500. With `use_date_range` this does nothing to
   the numbers given: write the period instead (with `import datetime`),
   `sequence.date_range_ids.filtered(lambda r: r.date_from <= datetime.date.today() <= r.date_to).write({'number_next_actual': 1500})`.

4. **Number transfers by operation type.** Inventory ‣ Configuration ‣ Warehouse
   Management ‣ Operations Types ‣ the type ‣ Sequence Prefix. Each `stock.picking.type`
   has its own `sequence_id`; receipts and deliveries of each warehouse number apart
   (`WH/IN/00001`, `WH/OUT/00001`).

   16.0 to 19.0, Sequence Prefix (`sequence_code`) is the middle part; Odoo rebuilds
   the sequence prefix as `<warehouse code>/<sequence_code>/`:

   ```python
   picking_type = env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1).out_type_id
   picking_type.write({'sequence_code': 'OUT2'})
   env.cr.commit()
   ```

   20.0, Sequence Prefix is the sequence prefix itself:

   ```python
   picking_type.write({'sequence_code': 'WH2/OUT/'})
   env.cr.commit()
   ```

   Leaves the next transfers of that type numbered with the new prefix, and the
   sequence's padding reset to 5.

## Variations

- **Another padding or prefix for transfers.** Write the operation type's sequence
  itself, from the Sequences menu or:

  ```python
  picking_type.sequence_id.write({'prefix': 'WH2/OUT/', 'padding': 6})
  env.cr.commit()
  ```

  A later edit of Sequence Prefix on the operation type rewrites this prefix and resets
  the padding to 5.
- **No gaps.** `implementation`: `standard` is fast but a cancelled transaction loses its
  number; `no_gap` never skips but locks the row. Keep the default unless gaps are a
  legal problem for that document.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Sequences (developer mode) | Settings ‣ Technical ‣ Sequences & Identifiers ‣ Sequences | same | same | same | Settings ‣ Technical ‣ User Interface ‣ Sequences & Identifiers ‣ Sequences |
| Operations Types | Inventory ‣ Configuration ‣ Warehouse Management ‣ Operations Types | same | same | same | same |
| `sequence_code` on the operation type | required; builds `<warehouse>/<code>/` | same | same | same | related to the sequence prefix |
| Payments without entry | journal | journal | `account.payment` sequence | same as 18.0 | same as 18.0 |

The `ir.sequence` fields and placeholders above are the same from 16.0 to 20.0.

## Verify

```python
sequence.invalidate_recordset()
print(sequence.read(['prefix', 'padding', 'number_next_actual', 'use_date_range']))
print(sequence.date_range_ids.read(['date_from', 'date_to', 'number_next_actual']))
print(picking_type.sequence_id.read(['prefix', 'padding', 'number_next_actual']))
```

Then create one draft quotation (or transfer) and read its name; `next_by_id()` from a
script consumes a number.

## Pitfalls

- **Lowering the next number.** Gives numbers twice: names of sales and purchases are
  not unique. Only with the user's yes, after checking.
- **Yearly restart in the middle of a year.** Repeats this year's numbers unless the
  period is created with the current number first (step 2).
- **The next number on a sequence with periods.** Writing `number_next_actual` on the
  sequence changes nothing: write the current period.
- **A custom transfer prefix lost.** Editing Sequence Prefix later rewrites the prefix
  and the padding.
- **One shared sequence for two companies.** Copy it per company for different formats.
