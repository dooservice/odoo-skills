# Facturas, boletas, notes and their series

How a Peruvian company issues facturas (01), boletas de venta (03), credit notes (07) and
debit notes (08) in its own series, and records suppliers' comprobantes with their
number. It needs Invoicing (`account`) with `l10n_pe`. Which document goes to which
customer is SUNAT's rule (see Electronic invoicing in `SKILL.md`). Sending the documents
to SUNAT is `l10n_pe_edi` (Enterprise) and is left out; the setup here is what that module
works on. Every step is an accounting change and needs the user's yes.

## Before you start

- Apps: `account` with `l10n_pe` and `l10n_latam_invoice_document`; credit and debit notes
  need `account_debit_note`, installed with `l10n_pe`.
- Settings: none. Each sale or purchase journal has "Use Documents?"
  (`l10n_latam_use_documents`), which cannot change once the journal has posted entries.
- The series plan comes from the accountant: which series for facturas, boletas, and for
  the notes on each (they start with F for facturas and B for boletas; whether notes get
  their own series is for the accountant to decide).
- Read first:

```python
company = env.company
for journal in env['account.journal'].search([('company_id', '=', company.id), ('type', 'in', ('sale', 'purchase'))]):
    last = env['account.move'].search([('journal_id', '=', journal.id), ('state', '=', 'posted')], order='id desc', limit=3)
    print(journal.code, journal.name, journal.type, journal.l10n_latam_use_documents, last.mapped('name'))
document_types = env['l10n_latam.document.type'].search([('country_id.code', '=', 'PE'), ('code', 'in', ('01', '03', '07', '08'))])
xml_ids = document_types.get_external_id()
for document_type in document_types:
    print(xml_ids[document_type.id], document_type.code, document_type.name, document_type.doc_code_prefix, document_type.internal_type)
```

| XML id | Code | Document | Prefix |
|---|---|---|---|
| `l10n_pe.document_type01` | 01 | Factura | F |
| `l10n_pe.document_type02` | 03 | Boleta | B |
| `l10n_pe.document_type07` | 07 | Nota de Crédito (on a factura) | F |
| `l10n_pe.document_type07b` | 07 | Nota de Crédito Boleta | B |
| `l10n_pe.document_type08` | 08 | Nota de Débito (on a factura) | F |
| `l10n_pe.document_type08b` | 08 | Nota de Débito Boleta | B |

`document_type02` is the boleta and `document_type03` the Recibo por Honorarios (code 02):
read `code`, not the XML id.

## The standard flow

Odoo numbers every document posted in a journal from one sequence, whatever its document
type. One sale journal per series keeps each correlative continuous. The snippets use the
partners `partner` (RUC) and `person` (DNI) from Contacts in `SKILL.md`, and a `product`.

1. **Create one journal per series.** Invoicing ‣ Configuration ‣ Accounting ‣ Journals,
   New, type Sales; "Use Documents?" is ticked by the form. The journal code is the
   series.

   ```python
   Journal = env['account.journal']
   series = {
       'F001': 'Facturas F001',
       'B001': 'Boletas B001',
       'FC01': 'Notas de crédito FC01',
       'BC01': 'Notas de crédito BC01',
       'FD01': 'Notas de débito FD01',
   }
   journals = {
       code: Journal.create({'name': name, 'code': code, 'type': 'sale', 'company_id': company.id, 'l10n_latam_use_documents': True})
       for code, name in series.items()
   }
   env.cr.commit()
   ```

   Leaves the journals empty. A script must pass `l10n_latam_use_documents`: only the form
   sets it.

2. **Issue the first factura and give it its number.** Invoicing ‣ Customers ‣ Invoices,
   New, journal F001, Document Type Factura. On the first document of a journal, write the
   number in the form's name field before confirming; Odoo continues from it.

   ```python
   factura = env['account.move'].create({
       'move_type': 'out_invoice', 'partner_id': partner.id, 'journal_id': journals['F001'].id,
       'l10n_latam_document_type_id': env.ref('l10n_pe.document_type01').id,
       'invoice_line_ids': [(0, 0, {'product_id': product.id, 'quantity': 1, 'price_unit': 100})],
   })
   factura.name = 'F F001-00000001'
   factura.action_post()
   env.cr.commit()
   ```

   Leaves the invoice `posted` as `F F001-00000001`, document number `F001-00000001`. The
   next ones in F001 need no name: they get `F F001-00000002` and on.

3. **Issue the first boleta** the same way in B001, Document Type Boleta, for a customer
   identified by DNI (or with no RUC).

   ```python
   boleta = env['account.move'].create({
       'move_type': 'out_invoice', 'partner_id': person.id, 'journal_id': journals['B001'].id,
       'l10n_latam_document_type_id': env.ref('l10n_pe.document_type02').id,
       'invoice_line_ids': [(0, 0, {'product_id': product.id, 'quantity': 1, 'price_unit': 100})],
   })
   boleta.name = 'B B001-00000001'
   boleta.action_post()
   env.cr.commit()
   ```

   Leaves it `posted` as `B B001-00000001`.

4. **Credit note.** On the posted invoice, Credit Note: give a reason, choose the note's
   journal and the Document Type (Nota de Crédito for a factura, Nota de Crédito Boleta for
   a boleta), Reverse; then confirm the draft note. Name the first note of each journal as
   in step 2.

   ```python
   wizard = env['account.move.reversal'].with_context(active_model='account.move', active_ids=factura.ids).create({
       'reason': 'Descuento posterior', 'journal_id': journals['FC01'].id,
   })
   wizard.l10n_latam_document_type_id = env.ref('l10n_pe.document_type07')
   action = wizard.reverse_moves()
   credit_note = env['account.move'].browse(action['res_id'])
   credit_note.name = 'F FC01-00000001'
   credit_note.action_post()
   env.cr.commit()
   ```

   For the boleta, the same with `boleta`, `journals['BC01']`, `l10n_pe.document_type07b`
   and `'B BC01-00000001'`. Leaves the note `posted`, linked to the invoice by
   `reversed_entry_id`.

5. **Debit note.** On the posted invoice, Debit Note: reason, journal, Copy Lines if the
   lines repeat, Create Debit Note; then confirm it.

   ```python
   wizard = env['account.debit.note'].with_context(active_model='account.move', active_ids=factura.ids).create({
       'reason': 'Intereses por mora', 'copy_lines': True, 'journal_id': journals['FD01'].id,
   })
   action = wizard.create_debit()
   debit_note = env['account.move'].browse(action['res_id'])
   debit_note.name = 'F FD01-00000001'
   debit_note.action_post()
   env.cr.commit()
   ```

   Leaves an `out_invoice` with document type 08, linked by `debit_origin_id`. From 17.0 a
   debit note on a boleta gets Nota de Débito Boleta by itself.

6. **Vendor bills.** Invoicing ‣ Vendors ‣ Bills, New: Document Type and Document Number
   as printed by the supplier (`F001-123`). Purchase journals number nothing: the number is
   required to confirm.

   ```python
   bill = env['account.move'].create({
       'move_type': 'in_invoice', 'partner_id': vendor.id, 'invoice_date': '2026-10-01',
       'journal_id': env['account.journal'].search([('type', '=', 'purchase'), ('company_id', '=', company.id)], limit=1).id,
       'l10n_latam_document_type_id': env.ref('l10n_pe.document_type01').id,
       'l10n_latam_document_number': 'F001-123',
       'invoice_line_ids': [(0, 0, {'product_id': product.id, 'quantity': 1, 'price_unit': 50})],
   })
   bill.action_post()
   env.cr.commit()
   ```

   Leaves the bill `posted` as `F F001-00000123`: for types 01, 03, 07 and 08 Odoo pads
   the correlative to 8 digits.

## Variations

- **One journal for everything.** Fine while all documents are of one type (only
  facturas). Mixing types in it gives a boleta the next factura number.
- **Several points of issue.** One journal per series and point (F002, B002 for a
  second branch), and the users of each point pick their journal.
- **Exports.** A factura to a customer abroad: from 17.0 the form offers only boletas for
  a customer without RUC, so choose Factura (in a script, give
  `l10n_latam_document_type_id` in `create()`); the export fiscal position puts `0% Exp`.
- **Supplier documents other than facturas**: Recibo por Honorarios (02), Liquidación de
  compra (04), Comprobante de No Domiciliado (91) and the rest are offered on vendor bills;
  the purchase journal offers 54 types.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Types offered to a customer without RUC | all | Boleta, ND Boleta, NC Boleta | same | same | same |
| Note offered on a boleta | Nota de Crédito (choose Boleta) | same | same | same | only Nota de Crédito Boleta |
| Debit note on a boleta | Nota de Débito (choose Boleta) | Nota de Débito Boleta | same | same | same |
| New journal by script, `refund_sequence` | True: credit notes left in the invoice journal get their own `F 00000001` | True | False: they continue the invoice sequence | False | False |
| Vendor number padded when given in `create()` | yes | no (only through the form) | yes | yes | yes |
| Menus | Invoicing ‣ Customers ‣ Invoices, Invoicing ‣ Configuration ‣ Accounting ‣ Journals | same | same | same | same |

## Verify

```python
for move in env['account.move'].search([('company_id', '=', company.id), ('move_type', '!=', 'entry'), ('state', '=', 'posted')], order='id desc', limit=10):
    print(move.journal_id.code, move.move_type, move.l10n_latam_document_type_id.code, move.name, move.l10n_latam_document_number, move.partner_id.name, move.amount_total)
```

Each journal shows one document type and a continuous correlative.

## Pitfalls

- **A boleta in the factura journal** gets the factura sequence (`F F001-00000003`). Posted,
  it is history: issue a credit note and the right document again.
- **The first number.** A journal without documents starts at `<prefix> 00000001`, without
  series. Name its first document `F F001-00000001` before posting; the prefix and a space
  come first.
- **Credit notes default to "Nota de Crédito"** (F) up to 19.0, even on a boleta. Choose
  Nota de Crédito Boleta.
- **"Use Documents?" off** on a journal created by script, or changed after posting
  (refused). Set it at creation.
- **17.0 vendor bills by script** keep the supplier's number as given (`F001-123`); write
  it padded (`F001-00000123`).
- **The same supplier number twice** is a duplicate. Search by name before importing
  bills (`l10n_latam_document_number` is not searchable in 20.0), with the number padded:
  `env['account.move'].search_count([('partner_id', '=', vendor.id), ('name', '=like', '% ' + 'F001-00000123'), ('move_type', '=', 'in_invoice')])`.
