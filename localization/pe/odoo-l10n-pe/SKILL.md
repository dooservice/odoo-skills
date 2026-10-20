---
name: odoo-l10n-pe
description: >-
  Odoo in Peru, 16.0 to 20.0: which l10n_pe modules to install, the PCGE chart
  of accounts and the IGV, exonerated, unaffected, export, ISC and free-transfer
  taxes they bring, how contacts are identified (RUC, DNI and the rest of
  SUNAT's types), facturas, boletas and notes with their series, detracciones,
  retenciones and percepciones, electronic invoicing with SUNAT through an OSE,
  the PLE and SIRE registers, and the mistakes that reach production. Use when
  the database has l10n_pe installed or a company is in Peru, together with
  odoo-functional.
---

# Odoo in Peru

What a functional consultant in Peru needs on top of `odoo-functional`, whose method and
recipes still apply. `versions.md` has what changes between Odoo versions. Everything
about Odoo here was read in the Community source of each version and run on a Peruvian
test database of that version. Rates and rules are SUNAT's as of the date given; check
them again when the date is old, and send anything marked "check with your accountant"
to the accountant before configuring it.

| Recipe | Covers |
|---|---|
| `recipes/documents-and-series.md` | facturas, boletas, credit and debit notes, one journal per series, vendor bills with the supplier's number |
| `recipes/withholding-perception-detraction.md` | detracciones (SPOT), IGV withholding (retenciones) and perception (percepciones): what Community does and how to record them |

## Modules

| Module | Edition | What it adds | Versions |
|---|---|---|---|
| `l10n_pe` | Community | PCGE chart, taxes, fiscal positions, SUNAT document types, identification types (up to 19.0), provinces (`res.city`) and districts (`l10n_pe.res.city.district`) | 16.0 to 20.0 |
| `l10n_latam_base` | Community | identification types (`l10n_latam.identification.type`) | 16.0 to 19.0; gone in 20.0 |
| `l10n_latam_invoice_document` | Community | document types on invoices, "Use Documents?" on journals | 16.0 to 20.0 |
| `l10n_pe_pos` | Community | district, city and identification in the point of sale, the "Consumidor Final" customer | 17.0 to 20.0, installs itself with `point_of_sale` |
| `l10n_pe_website_sale` | Community | identification type, city and district in the eCommerce checkout | 17.0 and 18.0 only; from 19.0 `l10n_pe` does it |
| `l10n_pe_edi` | Enterprise | electronic invoicing with SUNAT (UBL 2.1) | |
| `l10n_pe_reports` | Enterprise | RVIE 14.4, RCE 8.4 and 8.5, PLE 5.1, 5.3, 6.1, 1.1, 1.2 | |
| `l10n_pe_edi_stock`, `l10n_pe_edi_stock_20` | Enterprise | electronic delivery guide (guía de remisión) | |
| `l10n_pe_reports_stock` | Enterprise | PLE 12.1 and 13.1 permanent inventory | |

The Enterprise modules are described only from Odoo's documentation; their code was not
available to check. A company created in Peru gets `l10n_pe` with its chart; the other
Community modules follow when their app is installed. Install `l10n_pe_edi` and the
reports only on a database with an Enterprise subscription.

```python
company = env.company
print(env['ir.module.module'].search([('name', '=like', 'l10n\\_pe%'), ('state', '=', 'installed')]).mapped('name'))
print(company.country_id.code, company.currency_id.name, company.vat, company.account_sale_tax_id.name, company.account_purchase_tax_id.name)
print(env['account.journal'].search_read([('company_id', '=', company.id), ('type', 'in', ('sale', 'purchase'))], ['code', 'name', 'type', 'l10n_latam_use_documents']))
```

The company's own RUC goes in `vat` with country Peru; in 16.0 to 19.0 its partner also
needs the RUC identification type (see Contacts).

## Chart of accounts and taxes

The chart is the PCGE: template `l10n_pe.pe_chart_template` in 16.0, template code `pe`
(`company.chart_template`) from 17.0, with 7-digit account codes (`4011100`). Receivable
`1213`, payable `4212`, IGV `40111`, IGV withholding `40114`, ISC `4012`, other taxes
`40189`.

The taxes it creates, with the SUNAT tax code (`l10n_pe_edi_tax_code`, catalogue 05) and
the UN/ECE category (`l10n_pe_edi_unece_category`) the electronic invoice uses. XML ids
are `account.<company id>_<id>` from 17.0 and `l10n_pe.<company id>_<id>` in 16.0, where the
two purchase IGV G NG and NG taxes are `..._sale_tax_igv_18g_ng` and `..._sale_tax_igv_18_ng`.

| id | Name (18.0 on) | Use | Rate | Code |
|---|---|---|---|---|
| `sale_tax_igv_18`, `purchase_tax_igv_18` | VAT 18% | IGV, the company default | 18% | 1000 |
| `purchase_tax_igv_18g_ng`, `purchase_tax_igv_18_ng` | VAT 18% G NG, VAT 18% NG | purchases for taxed and untaxed sales, for untaxed sales (accounts 40117, 40116) | 18% | 1000 |
| `sale_tax_exo`, `purchase_tax_exo` | 0% Exo | exonerated | 0% | 9997 |
| `sale_tax_ina`, `purchase_tax_ina` | 0% Ina | unaffected (inafecto) | 0% | 9998 |
| `sale_tax_exp`, `purchase_tax_exp_0` | 0% Exp | exports; the purchase one books on 40115 (IGV imports) | 0% | 9995 |
| `sale_tax_gra`, `purchase_tax_gra` | 0% Gra | free (gratuito) | 0% | 9996 |
| `sale_tax_ics_0` | 0% ISC | ISC placeholder, account 4012 | 0% | 2000 |
| `tax_free_group` | 18% Free Group | free transfer of a taxed good: the line totals 0, IGV 18% goes to 40111 and its cost to 6411 | group | 9996 |
| `sale_tax_withholding_3` | 3% IGV Withholding | IGV withheld by the customer, account 40114 (19.0 on) | -3% | |

16.0 and 17.0 also have `sale_tax_igv_18_included` and `purchase_tax_igv_18_included`
(price included); 18.0 drops them for `price_include_override`. 16.0 has no
`tax_free_group`. In 17.0 the purchase `18% Levied and Not Taxed`, `18% Not Levied` and
`0% EXP` are price-included: check them before using them. `versions.md` has the rest.

```python
taxes = env['account.tax'].with_context(active_test=False).search([('company_id', '=', company.id)])
xml_ids = taxes.get_external_id()
for tax in taxes:
    print(xml_ids[tax.id], tax.name, tax.type_tax_use, tax.amount_type, tax.amount, tax.l10n_pe_edi_tax_code, tax.l10n_pe_edi_unece_category, tax.active)
```

The law behind them, as of the dates in Sources:

- **IGV.** The general rate is 18%: the IGV proper plus the Impuesto de Promoción Municipal
  (IPM). Ley 32387 moves 0.5 points a year from IGV to IPM from 2026: 15.5% + 2.5% in
  2026, 15% + 3% in 2027, 14.5% + 3.5% in 2028, 14% + 4% in 2029, always 18% in total.
  Odoo's single 18% tax stays correct; what changes is how the 18% is split in the
  return, which is the accountant's.
- **Restaurants and hotels (MYPE).** Ley 31556, as amended by Ley 32219, sets a special
  IGV rate of 8% for 2026 and 12% for 2027, plus IPM. Odoo has no tax for it: create one
  (copy `sale_tax_igv_18`) only with the total rate the accountant confirms.
- **Exports** of goods and services are not subject to IGV (TUO de la Ley del IGV,
  art. 33) and are invoiced with a factura (Reglamento de Comprobantes de Pago, art. 4).
  The export fiscal position replaces IGV with `0% Exp` (see below).
- **ISC** is computed by one of three systems: al valor, específico, or al valor según
  precio de venta al público (TUO, art. 55). The localization brings only a 0% ISC tax and
  the field `l10n_pe_edi_isc_type` (01, 02, 03) to say which system: create the real ISC
  tax per product family with the accountant.
- **ICBPER**, the plastic bag tax, is S/ 0.50 per bag from 2023 (Ley 30884, art. 12).
  There is a tax group and a code (7152) for it, but no tax. Create it:

```python
igv = company.account_sale_tax_id
group = env['account.tax.group'].search([('name', '=', 'ICBPER')], limit=1)                                   # 16.0
group = env['account.tax.group'].search([('name', '=', 'ICBPER'), ('company_id', '=', company.id)], limit=1)  # 17.0 on
account = env['account.account'].search([('code', '=like', '40189%'), ('company_id', '=', company.id)], limit=1)   # 16.0, 17.0
account = env['account.account'].search([('code', '=like', '40189%'), ('company_ids', 'in', company.id)], limit=1)  # 18.0 on
icbper = igv.copy({
    'name': 'ICBPER', 'description': 'ICBPER', 'amount_type': 'fixed', 'amount': 0.50,
    'tax_group_id': group.id, 'include_base_amount': False, 'sequence': 20,
    'l10n_pe_edi_tax_code': '7152', 'l10n_pe_edi_unece_category': 'S',
})
lines = icbper.invoice_repartition_line_ids | icbper.refund_repartition_line_ids
lines.filtered(lambda l: l.repartition_type == 'tax').write({'account_id': account.id})
env.cr.commit()
```

  Put it on the bag product together with IGV: three bags at S/ 0.20 give IGV 0.11 and
  ICBPER 1.50. Account 40189 ("other taxes") is a choice: check with your accountant.
- **Free transfers.** The comprobante must say "TRANSFERENCIA GRATUITA" (or "SERVICIO
  PRESTADO GRATUITAMENTE") and show the value the sale would have had (Reglamento de
  Comprobantes de Pago, art. 8). Who bears the IGV and how it is booked: check with your
  accountant; `tax_free_group` books it as an expense (6411).
- Any tax you create needs `l10n_pe_edi_tax_code` and `l10n_pe_edi_unece_category` (and
  `l10n_pe_edi_isc_type` for ISC): Odoo's documentation says the electronic invoice needs
  them.

**Fiscal positions.** `local_peru` (LOCAL PERU, country Peru) and `exportation` (FOREIGN -
EXPORT, any country), both automatic. A customer abroad gets `0% Exp` instead of IGV; a
customer with no country gets no position and keeps IGV. Up to 18.0 the mapping is a
line of the position; from 19.0 every Peruvian tax is limited to LOCAL PERU and `0% Exp`
replaces `VAT 18%` through `original_tax_ids`, so a tax you create in 19.0 or 20.0 should
get `fiscal_position_ids` too (`odoo-functional`, payment-terms-and-fiscal-positions).

## Contacts

SUNAT's identity document types (catalogue 06) are, among others: 0 non-domiciled tax
document without RUC, 1 DNI, 4 carné de extranjería, 6 RUC, 7 passport, A diplomatic
identity card, B identity document of the country of residence, C TIN, D IN. Odoo knows
them as follows.

**16.0 to 19.0**: `l10n_latam_identification_type_id` says what `vat` holds; the SUNAT code
is `l10n_pe_vat_code` on the type.

| XML id | Name | SUNAT code |
|---|---|---|
| `l10n_pe.it_RUC` | RUC | 6 |
| `l10n_pe.it_DNI` | DNI | 1 |
| `l10n_latam_base.it_fid` | Foreign ID | 4 |
| `l10n_latam_base.it_pass` | Passport | 7 |
| `l10n_latam_base.it_vat` | VAT | 0 |
| `l10n_pe.it_NDTD` | Non-Domiciled Tax Document | 0 |
| `l10n_pe.it_DIC`, `it_IDCR`, `it_TIN`, `it_IN`, `it_TAM`, `it_PTP`, `it_SP`, `it_CPP` | the other SUNAT types | A, B, C, D, E, F, G, H |

```python
partner = env['res.partner'].create({
    'name': 'Cliente SAC', 'is_company': True, 'country_id': env.ref('base.pe').id,
    'l10n_latam_identification_type_id': env.ref('l10n_pe.it_RUC').id, 'vat': '20555555556',
})
person = env['res.partner'].create({
    'name': 'Juan Pérez', 'country_id': env.ref('base.pe').id,
    'l10n_latam_identification_type_id': env.ref('l10n_pe.it_DNI').id, 'vat': '12345678',
})
env.cr.commit()
```

- The RUC is checked (11 digits, check digit) only when the type is RUC or VAT; a wrong
  one raises a `ValidationError`. A DNI or any other type is not checked at all.
- A partner created without a type gets `l10n_latam_base.it_vat` (VAT, SUNAT code 0), not
  RUC: the form sets RUC from the country, a script or an import does not. Such a
  customer can only receive boletas from 17.0 (see Electronic invoicing). Find and fix
  them, with the user's yes:

```python
wrong = env['res.partner'].search([
    ('country_id.code', '=', 'PE'), ('vat', '!=', False),
    ('l10n_latam_identification_type_id', '=', env.ref('l10n_latam_base.it_vat').id),
])
print(len(wrong), wrong.mapped('vat')[:20])
wrong.filtered(lambda p: len(p.vat) == 11).write({'l10n_latam_identification_type_id': env.ref('l10n_pe.it_RUC').id})
env.cr.commit()
```

**20.0**: identification types are gone. The RUC goes in `vat` (checked as above); other
documents go in `additional_identifiers` with keys `PE_DNI` (checked), `PASSPORT`,
`PE_NDTD`, `PE_DIC`, `PE_IDCR`, `PE_TIN`, `PE_IN`, `PE_TAM`, `PE_PTP`, `PE_SP`, `PE_CPP`.
Odoo computes `l10n_pe_sunat_id_code` and `l10n_pe_sunat_id_value`: 6 for a Peruvian
RUC, 1 for a DNI, 7 for a passport, 0 for a foreign tax ID or for nothing at all.

```python
partner = env['res.partner'].create({
    'name': 'Cliente SAC', 'is_company': True, 'country_id': env.ref('base.pe').id, 'vat': '20555555556',
})
person = env['res.partner'].create({
    'name': 'Juan Pérez', 'country_id': env.ref('base.pe').id, 'additional_identifiers': {'PE_DNI': '12345678'},
})
env.cr.commit()
print(partner.l10n_pe_sunat_id_code, person.l10n_pe_sunat_id_code, person.l10n_pe_sunat_id_value)
```

**Address.** Peru enforces cities: the state is the department, `city_id` the province
(196 in `res.city`, with `l10n_pe_code`), `l10n_pe_district` the district (1874, with a
6-digit `code`). Choosing the district fills the province. From 17.0 (with
`l10n_pe_website_sale`) and in `l10n_pe` from 19.0 the portal and checkout ask for the
district of Peruvian addresses. Odoo's documentation asks for the identification of
every partner on electronic documents, and the district of those on delivery guides.

## Electronic invoicing

**Which document.** A factura (01) is issued when the buyer is an IGV taxpayer entitled to
tax credit, when the buyer asks for one to support cost or expense, and for exports; a boleta de venta (03) to final consumers, and it gives no
tax credit. A boleta above S/ 700 must show the buyer's name and identity document type
and number. Credit notes (07) and debit notes (08) are issued only to the same buyer, to
modify a comprobante issued before (Reglamento de Comprobantes de Pago, arts. 4, 8 and
10). Electronic series are 4 characters, starting with F for facturas and B for boletas
(F001, B001), followed by the correlative (F001-00000001).

**What Odoo Community does** (verified): sale journals use documents
(`l10n_latam_use_documents`); a sale invoice offers 01 Factura, 03 Boleta, 08 Nota de
Débito and their boleta variants; a refund offers 07 Nota de Crédito and 07 Nota de
Crédito Boleta (`l10n_pe.document_type07b`). From 17.0 a customer whose identification is
not RUC is offered only Boleta, ND Boleta and NC Boleta; that includes foreign customers,
so an export factura has to be chosen in the invoice form's document type or set by
script (the domain is not enforced on write). In 20.0 a note offers only the subtype of
the document it modifies. The posted name is `<prefix> <number>`, `F F001-00000001`.

Watch the XML ids: `l10n_pe.document_type02` is the Boleta (code 03) and
`l10n_pe.document_type03` the Recibo por Honorarios (code 02). Always read `code`.

Odoo numbers all documents of one journal in one sequence, whatever their type: a boleta
posted in the factura journal becomes `F F001-00000003`. Use one sale journal per series,
and name its first document. `recipes/documents-and-series.md` has the setup.

**Electronic issuance (Enterprise, `l10n_pe_edi`).** From Odoo's documentation, not checked
in code:

- Signature provider: IAP (Odoo signs and sends to the OSE Digiflow; certificate
  included; 1000 free credits, then paid; one credit per sending, retries included),
  Digiflow (own certificate and contract), or SUNAT directly (own certificate, SUNAT's
  approval, and the SOL user written as company RUC + user, `20121888549JOHNSMITH`).
- Without IAP a `.pfx` certificate and its password are loaded in Settings.
- Databases start in production mode; a test mode exists and, with IAP, costs no
  credits.
- The company needs its "Address Type Code" (SUNAT establishment code, `0000` when
  unknown), sale journals the EDI format "Peru UBL 2.1" (untick Factur-X), products their
  UNSPSC code, invoices an operation type and each line an EDI affectation reason.
- States: To be sent (an hourly scheduled action sends, or "Send now"), Sent (accepted;
  the CDR zip is in the chatter). A rejected document stays To be sent with the error on
  top: fix the partner, product or tax and Retry, or reset to draft for invoice data.
- Cancellation: "Request Cancellation" with a reason, then To Cancel and Cancelled.

The rules behind it, from SUNAT's norms (dates in Sources):

- An OSE checks each electronic document for the issuer and returns the CDR (constancia
  de recepción); the issuer chooses SEE-OSE in SUNAT Operaciones en Línea and registers
  at least one valid digital certificate there, unless it authorises a PSE to act on its
  behalf (R.S. 117-2017/SUNAT, art. 9).
- Facturas and their notes are sent on the issue date or within 3 calendar days from the
  next day (R.S. 000003-2023/SUNAT). Boletas can go in a daily summary (resumen diario)
  the day they are issued or up to the 7th calendar day after.
- A factura is voided (comunicación de baja) within 7 calendar days from the day after
  its CDR. From 1 January 2027 the 7 days count from the day after the document was
  generated (R.S. 000048-2026/SUNAT, in force by R.S. 000143-2026/SUNAT).
- Operation type 1001 marks an operation subject to detracción, 0200 an export of goods,
  0101 an internal sale (catalogue 51).

SUNAT's list of rejection codes is on cpe.sunat.gob.pe; it could not be read for this
skill, so no code is quoted here. Read the error on the invoice and fix the data it
names.

## Legal reports

Community produces none of them. Book from posted entries; export the data with the
accountant's tool or use Enterprise.

- **PLE** (Programa de Libros Electrónicos, R.S. 286-2009/SUNAT): taxpayers with income
  of 75 UIT or more must keep the sales and purchase registers electronically
  (R.S. 361-2015/SUNAT); principal taxpayers keep more books (journal, ledger...) in PLE.
  Formats 14.1 (sales) and 8.1, 8.2 (purchases) were the PLE registers before SIRE.
- **SIRE** (R.S. 112-2021/SUNAT for sales, R.S. 040-2022/SUNAT for purchases): those
  obliged to keep the sales and purchase registers electronically keep them in SIRE.
  SUNAT proposes the sales register (RVIE) and the purchase register (RCE) from the
  electronic comprobantes it received, from the second day of each month; the taxpayer
  accepts, complements or replaces the proposal. SUNAT brought taxpayers in by groups; the
  last, principal taxpayers with 2024 income above 2 300 UIT, was postponed to the period
  October 2026 (R.S. 000392-2025/SUNAT, R.S. 000125-2026/SUNAT), so from that period the
  PLE sales and purchase registers no longer apply to the groups designated. Earlier
  periods stay in whatever system applied then: check with your accountant.
- `l10n_pe_reports` (Enterprise) produces RVIE 14.4, RCE 8.4 and 8.5, and PLE 5.1 journal,
  5.3 chart of accounts, 6.1 general ledger, 1.1 cash and 1.2 bank books; it needs the
  "PLE Type of CoA" set in Accounting settings. `l10n_pe_reports_stock` produces PLE 12.1
  and 13.1 (permanent inventory, units and valued) from stock moves: products need their
  type of existence and automatic valuation with a costing method other than standard,
  warehouses their annex establishment code, transfers their operation type. All from
  Odoo's documentation, not checked in code.
- What Community gives that these reports use: the document type and number of each
  invoice and bill (`l10n_latam_document_type_id`, `l10n_latam_document_number`), the
  partner's SUNAT identification, the tax codes above. Keep them right from day one: a
  register built later from wrong data has to be corrected document by document.
- Electronic delivery guides (guías de remisión) have been mandatory for senders and
  carriers since 1 January 2024 (R.S. 000123-2022/SUNAT). Community has none;
  `l10n_pe_edi_stock_20` (Enterprise) issues the sender's guide.

## Pitfalls

- **Customers created by script or import are "VAT", not RUC** (16.0 to 19.0). Symptom:
  from 17.0 the invoice offers only Boleta; the RUC is still validated. Cause: the default
  type is `l10n_latam_base.it_vat`. Fix: set the type on create; correct existing ones
  with the snippet in Contacts.
- **Boletas numbered as facturas.** Symptom: a boleta named `F F001-...`. Cause: one
  journal, one sequence. Fix: one journal per series (`recipes/documents-and-series.md`);
  a posted wrong number is not renamed, it is reversed and issued again.
- **Journals created by script do not use documents.** `l10n_latam_use_documents` is set
  by the form's onchange, not by `create()`: pass it. It cannot change once the journal
  has posted entries.
- **Credit notes on a boleta default to "Nota de Crédito"** (code 07, F prefix) up to
  19.0. Choose `Nota de Crédito Boleta` (`l10n_pe.document_type07b`) in the reversal
  wizard.
- **Export invoices become boletas** from 17.0: a foreign customer is not RUC, so only
  boletas are offered. Choose Factura on the invoice (or set
  `l10n_latam_document_type_id` in `create()`), and use the export fiscal position.
  Setting the type after creation by script in 17.0 kept the boleta's `B` prefix in the
  name: give it in `create()`.
- **Notes and exchange rates.** In 17.0 a credit or debit note in foreign currency takes
  the rate of the invoice it modifies; in 16.0 and 18.0 on it takes the rate of its own
  date. Which rate SUNAT expects: check with your accountant, and set the rate on the
  note if needed.
- **A customer without a country** gets no fiscal position. Always set the country.
- **The 3% IGV withholding tax** (19.0 on) is on the invoice and reduces the receivable;
  using it or a payment write-off is the accountant's choice
  (`recipes/withholding-perception-detraction.md`).
- **17.0 purchase taxes** `18% Levied and Not Taxed`, `18% Not Levied` and `0% EXP` are
  price-included: a bill entered with prices before tax comes out wrong.
- **New taxes without SUNAT codes** are rejected by the electronic invoice; in 19.0 and
  20.0 they also skip the fiscal position logic unless linked to it.
- **IPM change in 2026.** Do not create a 15.5% IGV tax: the rate charged is still 18%.

## Sources

Legal, as of the date given (opened 2026-10-20):

- IGV rate and IPM schedule: TUO de la Ley del IGV (D.S. 055-99-EF), art. 17 as amended
  by Ley 32387 (El Peruano 16.6.2025), SUNAT consolidated text dated 08.09.2025:
  https://www.sunat.gob.pe/legislacion/igv/ley/capitul5.pdf; SUNAT orientation, 18%
  rate and 2026 split: https://orientacion.sunat.gob.pe/node/1737
- Restaurants and hotels: Ley 32219 (El Peruano 29.12.2024), amending Ley 31556:
  https://busquedas.elperuano.pe/dispositivo/NL/2357993-3
- ISC systems: TUO, art. 55: https://www.sunat.gob.pe/legislacion/igv/ley/titulo2/cap3.pdf
- Exports not subject to IGV: TUO, art. 33:
  https://www.sunat.gob.pe/legislacion/igv/ley/capitul9.pdf
- ICBPER S/ 0.50 from 2023: Ley 30884, art. 12, SUNAT press note 001-2022 (1.1.2022):
  https://www.sunat.gob.pe/salaprensa/2022/enero/NotaPrensaN0012022.doc
- Factura, boleta and exports: Reglamento de Comprobantes de Pago (R.S. 007-99/SUNAT),
  art. 4, text dated 13.05.2026:
  https://www.sunat.gob.pe/legislacion/comprob/regla/capituloI.pdf
- Boleta above S/ 700, free transfers, notes to the same buyer: same Reglamento, arts. 8
  and 10, text dated 03.10.2025:
  https://www.sunat.gob.pe/legislacion/comprob/regla/capituloIII.pdf
- F and B series: SUNAT orientation on electronic comprobantes:
  https://orientacion.sunat.gob.pe/node/732; number format F###-NNNNNNNN:
  https://www.sunat.gob.pe/legislacion/superin/2017/anexoVIII-117-2017.pdf
- Sending facturas within 3 days: R.S. 000003-2023/SUNAT (El Peruano 05.01.2023):
  https://busquedas.elperuano.pe/dispositivo/NL/2140551-1
- Daily summary of boletas: https://orientacion.sunat.gob.pe/04-resumen-diario-boleta-de-venta-electronica
- Comunicación de baja from 2027: R.S. 000048-2026/SUNAT:
  https://www.sunat.gob.pe/legislacion/superin/2026/000048-2026.pdf, in force 1.1.2027 by
  R.S. 000143-2026/SUNAT: https://busquedas.elperuano.pe/dispositivo/NL/2538547-1;
  current rule (7 days from the CDR): https://orientacion.sunat.gob.pe/node/732
- OSE, CDR, PSE, digital certificate: R.S. 117-2017/SUNAT, arts. 1, 4 and 9:
  https://www.sunat.gob.pe/legislacion/superin/2017/117-2017.pdf
- Catalogues 01, 06, 07: https://www.sunat.gob.pe/legislacion/superin/2017/anexoVII-117-2017.pdf;
  catalogue 05: https://www.sunat.gob.pe/legislacion/superin/2019/anexos-150-2019.pdf;
  catalogue 51: https://www.sunat.gob.pe/legislacion/superin/2023/anexo-000005-2023.pdf
- PLE obligation at 75 UIT: R.S. 361-2015/SUNAT:
  https://www.sunat.gob.pe/legislacion/superin/2015/361-2015.pdf; formats 14.1, 8.1, 8.2:
  https://orientacion.sunat.gob.pe/preguntas-frecuentes-libros-y-registros
- SIRE: R.S. 112-2021/SUNAT: https://www.sunat.gob.pe/legislacion/superin/2021/112-2021.pdf;
  R.S. 040-2022/SUNAT: https://www.sunat.gob.pe/legislacion/superin/2022/040-2022.pdf;
  R.S. 000392-2025/SUNAT: https://www.sunat.gob.pe/legislacion/superin/2025/000392-2025.pdf;
  R.S. 000125-2026/SUNAT (30.06.2026): https://www.sunat.gob.pe/legislacion/superin/2026/000125-2026.pdf
- Electronic delivery guide mandatory from 2024: R.S. 000123-2022/SUNAT, art. 7 and annex X:
  https://www.sunat.gob.pe/legislacion/superin/2022/123-2022.pdf
- Odoo's documentation for the Enterprise modules (16.0 to 19.0):
  https://www.odoo.com/documentation/19.0/applications/finance/fiscal_localizations/peru.html

Odoo, Community source (`.odoo/src/<version>/addons`) and runs on pe16 to pe20:

- Modules and dependencies: `l10n_pe/__manifest__.py` of each version; `l10n_pe_pos` in
  17.0 to 20.0, `l10n_pe_website_sale` in 17.0 and 18.0 only, `l10n_latam_base` absent in
  20.0 (directory listing).
- Chart: `16.0/l10n_pe/data/l10n_pe_chart_data.xml:3,8`; `20.0/l10n_pe/models/template_pe.py:9-43`.
- Taxes, codes, accounts and fiscal position links: `l10n_pe/data/template/account.tax-pe.csv`
  (17.0 to 20.0), `16.0/l10n_pe/data/account_tax_data.xml`; fields in
  `20.0/l10n_pe/models/account_tax.py:8-41`; listed on each database.
- Fiscal positions: `l10n_pe/data/template/account.fiscal.position-pe.csv`,
  `16.0/l10n_pe/data/fiscal_position_data.xml`; run with Peruvian, foreign and countryless
  customers.
- Free group and withholding amounts: run (S/ 100 free line totals 0; 1000 with IGV and
  3% withholding totals 1144.60 in 19.0 and 20.0, computed on 1180).
- Identification types: `l10n_pe/data/l10n_latam_identification_type_data.xml` (16.0 to
  19.0); `20.0/l10n_pe/tools/partner_identifiers.py:8-89`,
  `20.0/l10n_pe/models/res_partner.py:22-56`; RUC check `check_vat_pe` in
  `16.0/base_vat/models/res_partner.py:527` and `20.0/odoo/addons/base/models/res_partner.py:2130`;
  default type `19.0/l10n_latam_base/models/res_partner.py:9-12`; run (valid and invalid
  RUC, DNI of 3 digits accepted in 16.0 to 19.0 and refused in 20.0).
- Document type domain: `16.0/l10n_pe/models/account_move.py:17-24`,
  `17.0/l10n_pe/models/account_move.py` (`_get_l10n_latam_documents_domain`),
  `20.0/l10n_pe/models/account_move.py:6-36`; run (DNI customer offered 03 and 08 from
  17.0; NC Boleta only in 20.0).
- One sequence per journal: `l10n_latam_invoice_document/models/account_move.py`
  (`_get_starting_sequence`, `_get_last_sequence_domain`); run (boleta named
  `F 00000002` in the default journal in every version).
- `l10n_latam_use_documents` set by onchange only:
  `l10n_latam_invoice_document/models/account_journal.py` (`_onchange_company`); run.
- Credit note rate date: `17.0/l10n_pe/models/account_move.py:58-73`, absent in other
  versions.
- Vendor bill number padding: `20.0/l10n_pe/models/account_move.py:38-67`; run
  (`F001-123` becomes `F F001-00000123`).
- Address: `l10n_pe/data/res_country_data.xml`, `l10n_pe/data/res.city.csv`,
  `l10n_pe/data/l10n_pe.res.city.district.csv`, `19.0/l10n_pe/controllers/portal.py`,
  `17.0/l10n_pe_website_sale/controllers/main.py`.
- Point of sale: `l10n_pe_pos/data/res_partner_data.xml` (17.0, 20.0).
