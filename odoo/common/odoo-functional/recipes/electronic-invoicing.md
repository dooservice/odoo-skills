# Electronic invoicing: UBL and CII files, Peppol

An electronic invoice is a structured file (UBL or CII XML) that the customer's software
reads without retyping. `account_edi_ubl_cii` writes it for customer invoices and reads
it from vendor bills; the format is chosen per customer. Peppol (`account_peppol`) is the
international network that carries those files between registered companies through
Odoo's access point (an IAP service). `account_peppol_response` (17.0 to 19.0, part of
`account_peppol` in 20.0) answers received documents with accept or reject;
`account_peppol_selfbilling` (17.0, 18.0, part of `account_peppol` from 19.0) carries
self-billed invoices. `account_add_gln` (16.0 to 19.0, part of `account` in 20.0) adds the
Global Location Number to delivery addresses, and `account_edi_ubl_cii_tax_extension`
(16.0 to 18.0, part of `account_edi_ubl_cii` from 19.0) the tax category codes. In 16.0
the formats hang on the sales journal through `account_edi`; from 17.0 `account_edi` only
serves country formats. Whether e-invoices are mandatory, which format and which
national platform apply is decided by the country's localization (national formats are
in the `l10n_*` modules): it is not covered here, so check it with the user.

## Before you start

- Apps: `account_edi_ubl_cii` (from Apps; some localizations install it);
  `account_peppol` from the setting below (auto-installed with `account_edi_ubl_cii`
  for companies in Peppol countries from 18.0). Installing needs the user's yes.
- Settings (Invoicing ‣ Configuration ‣ Settings ‣ PEPPOL Electronic Invoicing, 17.0+;
  the block shows only for companies in the countries Odoo's access point serves):

```python
env['res.config.settings'].create({'module_account_peppol': True}).execute()
env.cr.commit()
```

- 17.0 also has `invoice_is_ubl_cii` (Customer Invoices ‣ Peppol format): attach the
  XML by default in the send wizard.
- Read first:

```python
print(env['ir.module.module'].search_read([('name', 'like', 'account_edi%'), ('state', '=', 'installed')], ['name']))
print(env['ir.module.module'].search_read([('name', 'like', 'account_peppol%')], ['name', 'state']))
print(partner.read(['vat', 'country_id', 'invoice_edi_format', 'peppol_eas', 'peppol_endpoint']))
print(env.company.read(['account_peppol_proxy_state']))
```

This is 18.0 and 19.0. In 20.0 the partner's Peppol address is `routing_scheme` and
`routing_endpoint`; in 17.0 the format is `ubl_cii_format`; in 16.0 read the sales
journal's `edi_format_ids` instead. `account_peppol_proxy_state` exists once
`account_peppol` is installed.

## The standard flow

1. **Complete the company and the customer.** The company (Settings ‣ Companies) and
   the customer need a name, full address, country and tax ID (`vat`): the files carry
   them and are refused without.

2. **Choose the customer's format.** Invoicing ‣ Customers ‣ Customers ‣ the customer ‣
   Invoicing tab ‣ eInvoice format (Format in 17.0), and for Peppol the Peppol address.

   ```python
   partner.write({'invoice_edi_format': 'ubl_bis3', 'peppol_eas': '0088', 'peppol_endpoint': '<customer GLN>'})
   env.cr.commit()
   ```

   This is 18.0 and 19.0. In 20.0 write `routing_scheme` and `routing_endpoint` instead
   of `peppol_eas` and `peppol_endpoint`; in 17.0 the format field is `ubl_cii_format`.
   `ubl_bis3` ("EU Standard (Peppol Bis 3.0)") is the general format; `facturx`,
   `zugferd`, `xrechnung`, `nlcius`, `ubl_a_nz`, `ubl_sg` are national variants. The
   EAS (`0088` is GLN, `0208`, `9925` and others are national company or VAT numbers)
   and the endpoint are the customer's Peppol identifier: ask the customer, never guess.
   In 16.0 there is no per-customer format: Invoicing ‣ Configuration ‣ Accounting ‣
   Journals ‣ the sales journal ‣ Advanced Settings ‣ Electronic Data Interchange, tick
   the formats (`edi_format_ids`).

3. **Send the invoice with its XML.** The posted invoice ‣ Send (Send & Print in 16.0,
   17.0), with the e-invoice checkbox ticked (it shows the format's name). The send
   wizard itself is in `invoice-sending.md`.

   ```python
   wizard = env['account.move.send.wizard'].with_context(active_model='account.move', active_ids=invoice.ids).create({
       'sending_methods': ['email'],
   })
   print(wizard.invoice_edi_format)
   wizard.action_send_and_print()
   env.cr.commit()
   ```

   This is 18.0 to 20.0; in 17.0 use `account.move.send` with `checkbox_ubl_cii_xml`
   True. In 16.0 posting the invoice generates the file by itself (the journal's
   formats), with `edi_state` `sent`. Leaves the XML attached to the invoice
   (`ubl_cii_xml_id`, 17.0+) and to the email, and the PDF with the XML embedded.

4. **Register on Peppol** (17.0+, and 16.0 when `account_peppol` is installed). The
   user does it in Invoicing ‣ Configuration ‣ Settings ‣ PEPPOL Electronic Invoicing:
   the company's Peppol address, contact email and phone, then the registration (a
   verification code by SMS up to 18.0). It is an agreement with an external service:
   the user registers, never a script. Leaves `account_peppol_proxy_state`:

   | Version | Values |
   |---|---|
   | 16.0 | `not_registered`, `pending`, `active`, `rejected`, `canceled` |
   | 17.0 | adds `not_verified`, `sent_verification`, `sender` |
   | 18.0 | `not_registered`, `in_verification`, `sender`, `smp_registration`, `receiver`, `rejected` |
   | 19.0, 20.0 | `not_registered`, `sender`, `smp_registration`, `receiver`, `rejected` |

   `sender` can send only; `receiver` (`active` up to 17.0) also receives, into the
   purchase journal `peppol_purchase_journal_id`.

5. **Send by Peppol.** The invoice ‣ Send ‣ by Peppol (18.0+; "Send via PEPPOL" in
   17.0), or the customer's `invoice_sending_method` set to `peppol`.

   ```python
   wizard = env['account.move.send.wizard'].with_context(active_model='account.move', active_ids=invoice.ids).create({
       'sending_methods': ['peppol'],
   })
   wizard.action_send_and_print()
   env.cr.commit()
   ```

   This is 18.0 to 20.0; in 17.0 `checkbox_send_peppol` True on `account.move.send`.
   Leaves `peppol_move_state` `processing` ("Pending Reception"), then `done` when the
   access point confirms, or `error` with the reason in the chatter. The customer must
   be registered on Peppol: the partner shows whether its address is valid.

6. **Receive vendor bills.** Bills sent to the company on Peppol arrive in the Peppol
   purchase journal by a scheduled action; the journal's dashboard card has a button to
   fetch now. Files received by email or on paper are uploaded: Invoicing ‣ Vendors ‣
   Bills ‣ Upload.

   ```python
   attachment = env['ir.attachment'].create({'name': 'bill.xml', 'raw': xml_bytes})
   purchase_journal = env['account.journal'].search([('type', '=', 'purchase'), ('company_id', '=', env.company.id)], limit=1)
   action = purchase_journal.with_context(default_move_type='in_invoice').create_document_from_attachment(attachment.ids)
   env.cr.commit()
   ```

   Leaves a draft bill filled from the file: vendor (by VAT or Peppol address), lines,
   taxes and totals. Check it before posting: unknown products and taxes are left for
   the user.

## Variations

- **Answer a received bill** (17.0+ with `account_peppol_response`, in `account_peppol`
  in 20.0): the bill's Peppol buttons approve or reject it; a rejection asks reasons
  (the rejection wizard). The sender sees `AP` (approved) or `RE` (rejected) in 20.0,
  or the responses list (`account.peppol.response`) on the invoice up to 19.0.
- **Self-billing** (17.0, 18.0 with `account_peppol_selfbilling`; in `account_peppol`
  from 19.0): when the customer writes the supplier's invoice, a purchase journal marked
  `is_self_billing` (up to 18.0) sends the self-billed invoice on Peppol; from 19.0 the
  company's `peppol_activate_self_billing_sending` and
  `peppol_self_billing_reception_journal_id` do it.
- **Delivery address GLN**: the delivery address ‣ GLN (`global_location_number`,
  shown on addresses of type delivery). It goes into the files as the delivery place.
- **Tax category codes**: the tax form ‣ Tax Category Code
  (`ubl_cii_tax_category_code`: `S` standard, `Z` zero rated, `E` exempt, `AE` reverse
  charge, `O` outside scope, `K` intra-community, `G` export...) and, for `AE`, `E`, `G`,
  `O`, `K`, the exemption reason (`ubl_cii_tax_exemption_reason_code`). Without them
  Odoo infers the category from the tax amount, which fails for exempt and reverse charge
  lines.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Where the format is chosen | sales journal `edi_format_ids` | partner `ubl_cii_format` | partner `invoice_edi_format` | same | same |
| Partner Peppol address | `peppol_eas`, `peppol_endpoint` | same | same | same | `routing_scheme`, `routing_endpoint` |
| Generated when | at posting | in the send wizard | same | same | same |
| Peppol setting | none (install from Apps) | `module_account_peppol` | same | same | same |
| Peppol responses | no | `account_peppol_response` | same | same | in `account_peppol` |
| Self-billing | no | `account_peppol_selfbilling` | same | in `account_peppol` | same |
| GLN | `account_add_gln` | same | same | same | in `account` |
| Tax category codes | `account_edi_ubl_cii_tax_extension` | same | same | in `account_edi_ubl_cii` | same |
| Fetch Peppol now | `peppol_get_new_documents` | same | same | same | `button_fetch_in_einvoices` |

The same in every version: Invoicing ‣ Vendors ‣ Bills ‣ Upload; Invoicing ‣
Configuration ‣ Settings.

## Verify

```python
print(invoice.ubl_cii_xml_id.name, invoice.peppol_move_state)
print(env['ir.attachment'].search_read([('res_model', '=', 'account.move'), ('res_id', '=', invoice.id)], ['name', 'mimetype']))
```

In 16.0 read `invoice.edi_state` and `invoice.edi_document_ids` instead. The XML is
attached, and a Peppol invoice reaches `done`. Ask the user to open the received bill
and compare it with the vendor's PDF.

## Pitfalls

- A missing VAT, address or Peppol address makes the wizard warn and skip the file:
  fix the partner, not the XML.
- A neutralized copy puts its Peppol connection in demo mode (`edi_mode` `demo`):
  nothing really leaves there. Never switch a copy back to production with the
  production identifier: documents would go out twice.
- Uploading the same file twice creates two bills: search by the vendor reference first.
- A national format chosen for a customer abroad is rejected by their software: use
  `ubl_bis3` unless the customer asks otherwise.
