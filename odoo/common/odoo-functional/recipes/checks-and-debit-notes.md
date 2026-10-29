# Checks and debit notes

Two corrections and means of payment around customer invoices and vendor bills. Check
printing (`account_check_printing`) pays vendors with checks: a bank journal gets the
Checks payment method, payments made with it get a check number and print on the
company's check layout. Debit notes (`account_debit_note`) add an amount to a posted
invoice or bill without cancelling it, linked to the original by `debit_origin_id`;
`account_debit_note_sequence` (17.0 only; part of `account_debit_note` from 18.0) gives
them their own numbering. All in Community. The check layouts themselves (the printed
format of the check paper) come only with a country's localization, which also decides
whether checks and debit notes are used and with which numbering: it is not covered
here, so check it with the user.

## Before you start

- Apps: `account`; `account_check_printing` (installed by the Checks setting);
  `account_debit_note` from Apps (16.0, 17.0 add `account_debit_note_sequence` for the
  dedicated numbering). Installing a module needs the user's yes.
- Settings (Invoicing ‣ Configuration ‣ Settings ‣ Vendor Payments ‣ Checks):

```python
env['res.config.settings'].create({'module_account_check_printing': True}).execute()
env.cr.commit()
```

- After the install, the same block shows the company's check options:
  `account_check_printing_layout` (`disabled`, "None", is the only Community value;
  localizations add the layouts), `account_check_printing_date_label`,
  `account_check_printing_multi_stub`, `account_check_printing_margin_top`,
  `account_check_printing_margin_left`, `account_check_printing_margin_right`.
- Read first:

```python
print(env['ir.module.module'].search_read([('name', 'in', ['account_check_printing', 'account_debit_note', 'account_debit_note_sequence'])], ['name', 'state']))
print(env.company.account_check_printing_layout, env['res.company']._fields['account_check_printing_layout'].selection)
bank = env['account.journal'].search([('type', '=', 'bank'), ('company_id', '=', env.company.id)], limit=1)
print(bank.outbound_payment_method_line_ids.mapped('code'), bank.check_manual_sequencing, bank.check_next_number)
```

## The standard flow

### Pay a vendor by check

1. **Choose the check layout.** Invoicing ‣ Configuration ‣ Settings ‣ Vendor Payments ‣
   Checks ‣ Check Layout, and the margins for the printer.

   ```python
   env['res.config.settings'].create({'account_check_printing_layout': '<layout from the localization>'}).execute()
   env.cr.commit()
   ```

   Leaves the company layout set. Without a layout other than `disabled`, printing
   stops with "You have to choose a check layout": the localization brings them. From
   18.0 a bank journal can override it with `bank_check_printing_layout`.

2. **Set the bank journal's numbering.** Invoicing ‣ Configuration ‣ Accounting ‣
   Journals ‣ the bank journal ‣ Outgoing Payments tab. Installing the module adds the
   Checks method to every bank journal and creates its check sequence.

   ```python
   bank.write({'check_manual_sequencing': True, 'check_next_number': '000101'})
   env.cr.commit()
   ```

   Leaves the journal numbering checks from 101 at posting. `check_manual_sequencing`
   False (the default) means pre-numbered paper: the number is asked when printing.

3. **Register the payment with the Checks method.** The vendor bill ‣ Pay, Journal: the
   bank journal, Payment Method: Checks.

   ```python
   method_line = bank.outbound_payment_method_line_ids.filtered(lambda l: l.code == 'check_printing')
   payments = env['account.payment.register'].with_context(active_model='account.move', active_ids=bill.ids).create({
       'journal_id': bank.id, 'payment_method_line_id': method_line.id,
   })._create_payments()
   env.cr.commit()
   ```

   Leaves the payment posted with `check_number` (manual numbering) and the bill in
   payment. Payments are accounting changes: only with the user's yes.

4. **Print the checks.** Invoicing ‣ Vendors ‣ Payments, filter Checks to Print, select
   ‣ Print Check (the payment form's Print Check button for one).

   ```python
   action = payments.print_checks()
   env.cr.commit()
   ```

   With manual numbering, `action` is the PDF report and the payments are marked sent
   (`is_sent`; `is_move_sent` in 16.0, 17.0). With pre-numbered paper, `action` opens the
   wizard `print.prenumbered.checks`: give the first number on the paper and print.

   ```python
   wizard = env['print.prenumbered.checks'].with_context(payment_ids=payments.ids).create({'next_check_number': '000101'})
   wizard.print_checks()
   env.cr.commit()
   ```

### Add a debit note to an invoice

1. **Create the debit note.** The posted invoice or bill ‣ Debit Note (button in 16.0,
   19.0, 20.0, labeled Add Debit Note in 16.0; Actions ‣ Debit Note in 17.0, 18.0).

   ```python
   wizard = env['account.debit.note'].with_context(active_model='account.move', active_ids=invoice.ids).create({
       'reason': 'Price correction', 'copy_lines': True,
   })
   action = wizard.create_debit()
   debit_note = env['account.move'].browse(action['res_id'])
   env.cr.commit()
   ```

   Leaves a draft invoice (`out_invoice`, or `in_invoice` for a bill) with
   `debit_origin_id` on the original, `ref` "<original>, <reason>" and no payment
   terms. `copy_lines` False leaves it without lines to fill in; `journal_id` picks
   another journal; `date` is the debit note date. Only posted documents can be
   debited, and a debit note cannot be debited again (17.0+).

2. **Adjust and post it.** Set the lines to the amount to add, then Confirm.

   ```python
   debit_note.invoice_line_ids.write({'quantity': 1, 'price_unit': 50})
   debit_note.action_post()
   env.cr.commit()
   ```

   Leaves the debit note posted. With a dedicated sequence (see `## Variations`) its
   number starts with `D` (`DINV/2026/00001`). The original shows a Debit Notes smart
   button; from 20.0 the debit note shows one back to its origin.

## Variations

- **Dedicated debit note numbering**: the sale or purchase journal ‣ Advanced Settings,
  `debit_sequence` ("Dedicated Debit Note Sequence"). In 17.0 it needs
  `account_debit_note_sequence`; from 18.0 it is in `account_debit_note`, on by default
  for new sale and purchase journals. 16.0 has none: debit notes share the invoice
  numbering.
- **Debit a credit note**: from a customer or vendor credit note the debit note is an
  invoice (`out_invoice`, `in_invoice`); its lines are not copied.
- **Void a printed check**: the payment ‣ Void Check (`action_void_check`), which
  resets and cancels the payment; then register a new one. Unmark Sent (`unmark_as_sent`;
  `action_unmark_sent` in 16.0, 17.0) only clears the sent flag to print again.
- **Several checks in one run**: select payments of the same bank journal; checks of
  different journals are refused.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Sent flag on payments | `is_move_sent` | same | `is_sent` | same | same |
| Payment state for Checks to Print and Void | `posted` | same | `in_process` | same | `paid` |
| Layout per bank journal | no | no | `bank_check_printing_layout` | same | same |
| Unmark sent method | `action_unmark_sent` | same | `unmark_as_sent` | same | same |
| Debit note entry point | Add Debit Note button | Actions ‣ Debit Note | Actions ‣ Debit Note | Debit Note button | same |
| Dedicated debit numbering | no | `account_debit_note_sequence` | `account_debit_note` | same | same |
| Refuses debiting a debit note | no | yes | yes | yes | yes |
| Smart button back to origin | no | no | no | no | yes |

The same in every version: Invoicing ‣ Vendors ‣ Payments; Invoicing ‣ Configuration ‣
Settings ‣ Vendor Payments ‣ Checks; Invoicing ‣ Configuration ‣ Accounting ‣ Journals.

## Verify

```python
print(payments.read(['name', 'check_number', 'state', 'is_sent']))
print(debit_note.read(['name', 'state', 'debit_origin_id', 'amount_total']))
print(invoice.debit_note_ids.mapped('name'))
```

On 16.0 and 17.0 read `is_move_sent` instead of `is_sent`. Check numbers follow each
other, payments are sent, and the debit note is posted and linked to its origin.

## Pitfalls

- Printing marks the checks sent before the paper comes out: if the printer jams,
  unmark them and print again instead of voiding.
- Check numbers must be unique per journal; a manual `check_number` that repeats one is
  refused.
- Changing `check_next_number` backwards reuses numbers already printed.
- A debit note copies the original's lines with `copy_lines`: change quantities and
  prices before posting, or the customer is billed twice.
- Turning on `debit_sequence` on a journal with debit notes already numbered starts a
  new `D` sequence: decide it before the first debit note.
