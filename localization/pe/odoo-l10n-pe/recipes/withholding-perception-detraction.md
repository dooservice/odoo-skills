# Detracciones, retenciones and percepciones

Peru's three IGV collection systems and how to record them in Odoo Community: the
detracción (SPOT), where the customer deposits part of the price in the seller's account
at the Banco de la Nación; the IGV withholding (retención), where a customer designated by
SUNAT keeps 3% of the price; and the perception (percepción), where a designated seller
charges an extra percentage. It needs Invoicing (`account`) with `l10n_pe`. Community has
no detracción or perception logic, no comprobante de retención (20) or de percepción (40)
issuing, and no deposit constancias: what follows records the money correctly with
standard Odoo. In `l10n_pe_edi` (Enterprise), Odoo's documentation says invoices subject
to detracción need fields on the products and operation type 1001; that was not checked
in code. Every step is an accounting change and needs the user's yes, and every rate
below goes through the accountant before it is configured.

## Before you start

- Apps: `account` with `l10n_pe`.
- Settings: none.
- The rules, as of the dates in Sources:
  - **Detracción.** The customer deposits the percentage in the seller's detracciones
    account at the Banco de la Nación; the funds only pay the seller's taxes. For services
    it applies above S/ 700. Common rates: 12% for "demás servicios gravados con el IGV",
    labour intermediation, repair of movable goods and other business services; 10% for
    leasing, cargo handling, commission, manufacturing to order and passenger transport;
    4% for construction contracts and for road freight above S/ 400. The customer deposits
    by the date it pays or by the 5th business day of the month after it records the
    comprobante, whichever comes first. The factura must say "Operación sujeta al Sistema
    de Pago de Obligaciones Tributarias con el Gobierno Central." and cannot include other
    operations.
  - **Retención.** 3% of the total price including IGV, applied by customers SUNAT
    designated as agentes de retención, when the operation is above S/ 700; not applied
    when the supplier is a buen contribuyente or itself an agente de retención, or the
    operation is subject to detracción.
    The comprobante de retención is electronic since 1 January 2018.
  - **Percepción.** 2% in general on domestic sales of the goods listed by law, 1% on
    fuels, 0.5% when the buyer is itself an agente de percepción and receives a
    comprobante that gives tax credit; not applied to operations subject to detracción.
- Read first:

```python
company = env.company
groups = env['account.tax.group'].search([('name', 'in', ('DET', 'RET', 'IGV Withholding', 'ICBPER'))])
print(groups.mapped('name'))
print(env['account.tax'].search([('company_id', '=', company.id), ('tax_group_id', 'in', groups.ids)]).mapped('name'))
print(env['l10n_latam.document.type'].search([('country_id.code', '=', 'PE'), ('code', 'in', ('20', '40'))]).read(['code', 'name', 'internal_type']))
print(env['account.journal'].search_read([('company_id', '=', company.id), ('type', '=', 'bank')], ['code', 'name']))
```

The chart has tax groups DET and RET with no tax in them, account 40113 (IGV, perception
regime) and 40114 (IGV, withholding regime). Document types 20 and 40 exist with no
`internal_type`, so no invoice offers them. From 19.0 there is one tax:
`sale_tax_withholding_3` (3% IGV Withholding).

## The standard flow

A sale of S/ 1 000 + IGV = S/ 1 180 to a customer with RUC (`partner`, from Contacts in
`SKILL.md`) of a service (`product`).

1. **Invoice with the detracción legend.** Invoicing ‣ Customers ‣ Invoices, New; write the
   legend in the terms and conditions (`narration`) and confirm.

   ```python
   invoice = env['account.move'].create({
       'move_type': 'out_invoice', 'partner_id': partner.id,
       'narration': 'Operación sujeta al Sistema de Pago de Obligaciones Tributarias con el Gobierno Central.',
       'invoice_line_ids': [(0, 0, {'product_id': product.id, 'quantity': 1, 'price_unit': 1000})],
   })
   invoice.action_post()
   env.cr.commit()
   ```

   Leaves the invoice `posted` for 1 180, the full amount receivable: the detracción does
   not reduce what the customer owes, it changes where it pays.

2. **A bank journal for the detracciones account.** Invoicing ‣ Configuration ‣
   Accounting ‣ Journals, New, type Bank, with the Banco de la Nación account number.

   ```python
   detraction_journal = env['account.journal'].create({
       'name': 'Detracciones Banco de la Nación', 'code': 'DETR', 'type': 'bank', 'company_id': company.id,
   })
   env.cr.commit()
   ```

   Its balance is the money that can only pay taxes.

3. **Register the two payments.** On the invoice, Register Payment twice: the part paid to
   the company's bank, then the deposit (12% here, 141.60) in the detracciones journal.

   ```python
   bank = env['account.journal'].search([('company_id', '=', company.id), ('type', '=', 'bank'), ('id', '!=', detraction_journal.id)], limit=1)
   for journal, amount in ((bank, 1038.40), (detraction_journal, 141.60)):
       env['account.payment.register'].with_context(active_model='account.move', active_ids=invoice.ids).create({
           'journal_id': journal.id, 'amount': amount, 'payment_date': '2026-10-15',
       })._create_payments()
   env.cr.commit()
   ```

   Leaves the invoice with nothing left to pay (`amount_residual` 0). The deposit may be
   made without decimals, rounded on the first decimal (R.S. 183-2004/SUNAT, fifth final
   provision): 141.60 becomes 142 and the bank part 1 038. Register what the customer
   actually deposited and paid. A purchase subject to detracción is the mirror: two vendor
   payments, one to the supplier's bank and one deposit to its Banco de la Nación account.

4. **Retención by the customer.** The customer pays 97% (1 144.60) and sends a comprobante
   de retención for 35.40. Register Payment for the amount received, "Mark as fully paid"
   with the difference on account 40114.

   ```python
   invoice2 = env['account.move'].create({'move_type': 'out_invoice', 'partner_id': partner.id, 'invoice_line_ids': [(0, 0, {'product_id': product.id, 'quantity': 1, 'price_unit': 1000})]})
   invoice2.action_post()
   withholding_account = env['account.account'].search([('code', '=like', '40114%'), ('company_id', '=', company.id)], limit=1)   # 16.0, 17.0
   withholding_account = env['account.account'].search([('code', '=like', '40114%'), ('company_ids', 'in', company.id)], limit=1)  # 18.0 on
   env['account.payment.register'].with_context(active_model='account.move', active_ids=invoice2.ids).create({
       'journal_id': bank.id, 'amount': 1144.60, 'payment_date': '2026-10-15',
       'payment_difference_handling': 'reconcile', 'writeoff_account_id': withholding_account.id,
       'writeoff_label': 'Retención IGV 3%',
   })._create_payments()
   env.cr.commit()
   ```

   Leaves the invoice paid, with 35.40 debited to 40114, where it offsets the IGV to pay.
   Keep the customer's comprobante de retención number in the payment's memo.

## Variations

- **The 3% withholding tax on the invoice (19.0 on).** Put `VAT 18%` and `3% IGV
  Withholding` on the lines of an invoice to an agente de retención: Odoo computes 3% on
  price plus IGV (1 000 gives IGV 180, withholding -35.40, total 1 144.60), booked on
  40114, and the customer owes only 1 144.60. The receivable then differs from the
  comprobante's total; whether to use it or the write-off of step 4 is the accountant's
  choice.

  ```python
  igv = env.ref(f'account.{company.id}_sale_tax_igv_18')
  withholding = env.ref(f'account.{company.id}_sale_tax_withholding_3')
  invoice3 = env['account.move'].create({
      'move_type': 'out_invoice', 'partner_id': partner.id,
      'invoice_line_ids': [(0, 0, {'product_id': product.id, 'quantity': 1, 'price_unit': 1000, 'tax_ids': [(6, 0, (igv | withholding).ids)]})],
  })
  print(invoice3.amount_untaxed, invoice3.amount_tax, invoice3.amount_total)
  ```

- **The company is an agente de retención.** It pays its suppliers 97% and must issue
  comprobantes de retención, which Community does not do: register the vendor payment
  with the difference to the account the accountant gives, and issue the comprobante in
  SUNAT's system or with Enterprise.
- **Percepción charged by a supplier.** The supplier's comprobante shows the perception
  apart from the price. Add it as a bill line on 40113 (no tax) after the accountant
  confirms the account.
- **The company is an agente de percepción.** Community has no perception tax or
  comprobante 40; a tax for it is a configuration decision for the accountant.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| `sale_tax_withholding_3` | no | no | no | yes | yes |
| Account search | `company_id` | `company_id` | `company_ids` | `company_ids` | `company_ids` |
| Tax groups DET, RET (empty) | yes | yes | yes | yes | yes |
| Menus | Invoicing ‣ Customers ‣ Invoices, Invoicing ‣ Configuration ‣ Accounting ‣ Journals | same | same | same | same |

## Verify

```python
print(invoice.name, invoice.amount_total, invoice.amount_residual, invoice.payment_state)
print(invoice2.name, invoice2.amount_total, invoice2.amount_residual, invoice2.payment_state)
print(env['account.move.line'].search([('account_id', '=', withholding_account.id), ('parent_state', '=', 'posted')]).mapped(lambda l: (l.name, l.debit, l.credit)))
```

## Pitfalls

- **Lowering the invoice by the detracción.** The comprobante is for the full price; the
  detracción is a payment. Never put it as a negative line or tax.
- **Detracción and retención together.** The law excludes the retención when the
  detracción applies; do not apply both to one invoice.
- **The threshold.** Below the amounts in Before you start neither applies; Odoo does not
  check them, so the user decides per invoice.
- **The detracciones journal used to pay suppliers.** Its money can only pay taxes;
  keep it apart from the operating bank in reports and cash planning.
- **Rates change.** SUNAT changed detracción annexes in 2025 for gold, other metal ores
  and their processing (R.S. 000086-2025/SUNAT); confirm the rate of each product or
  service before the first invoice.

## Sources

- Detracción: R.S. 183-2004/SUNAT, recitals, arts. 13, 16, 17, 19 and first and fifth
  final provisions: https://www.sunat.gob.pe/legislacion/superin/2004/183.htm; rates (annex 3,
  12% since R.S. 071-2018/SUNAT): https://orientacion.sunat.gob.pe/apendices-del-sistema-de-detracciones;
  2025 change, in force 1.4.2025: https://www.sunat.gob.pe/legislacion/superin/2025/000086-2025.pdf;
  road freight 4% above S/ 400 (R.S. 073-2006/SUNAT):
  https://orientacion.sunat.gob.pe/detracciones-en-el-transporte-de-bienes-por-via-terrestre;
  operation type 1001: https://www.sunat.gob.pe/legislacion/superin/2023/anexo-000005-2023.pdf
- Retención 3% since 1.3.2014 (R.S. 033-2014/SUNAT, amending R.S. 037-2002/SUNAT):
  https://orientacion.sunat.gob.pe/73-importe-de-la-operacion-y-tasa-de-retencion;
  threshold and exclusions: https://orientacion.sunat.gob.pe/06-preguntas-frecuentes-regimen-de-retenciones;
  electronic comprobante since 2018: https://orientacion.sunat.gob.pe/75-comprobante-de-retencion;
  codes 20 and 40: https://www.sunat.gob.pe/legislacion/superin/2017/anexosV-318-2017.pdf
- Percepción rates (Ley 29173): http://contenido.app.sunat.gob.pe/insc/Percepciones+IGV/Porcentaje+de+percepcion.pdf;
  exclusion of SPOT operations: https://orientacion.sunat.gob.pe/02-regimen-de-percepciones-venta-interna
- Odoo: tax groups and accounts in `l10n_pe/data/template/account.tax.group-pe.csv`,
  `account.tax-pe.csv` and `account.account-pe.csv` (17.0 to 20.0),
  `16.0/l10n_pe/data/account_tax_group_data.xml`; document types 20 and 40 in
  `l10n_pe/data/l10n_latam_document_type_data.xml`; payments run on pe16 to pe20.
