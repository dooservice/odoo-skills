# Email templates

A `mail.template` is the email Odoo prepares for a document: the quotation, the order
confirmation, the invoice, the delivery. It belongs to one model (`model`), and its
fields are rendered on the record being sent (`object`). Find the standard one by XML id
(`grep "mail.template" odoo-reference/xmlids/<addon>.md`), not by name: names are
translated and users rename them.

## Read first

```python
env['mail.template'].search_read([('model', '=', 'account.move')], ['name', 'subject', 'lang'])
template = env.ref('account.email_template_edi_invoice')
template.read(['subject', 'email_from', 'partner_to', 'email_to', 'email_cc', 'reply_to', 'lang', 'body_html'])
record = env['account.move'].search([('move_type', '=', 'out_invoice'), ('state', '=', 'posted')], limit=1)
template._render_field('subject', record.ids)
template._render_field('body_html', record.ids, compute_lang=True)
```

`_render_field` returns `{record_id: text}` as the customer would receive it;
`compute_lang=True` renders in the language the template's `lang` picks for that record.
Render before and after every change.

Common XML ids: `sale.email_template_edi_sale` (quotation), `sale.mail_template_sale_confirmation`
(order confirmed), `account.email_template_edi_invoice` (invoice),
`purchase.email_template_edi_purchase` (RFQ), `stock.mail_template_data_delivery_confirmation`.

## Change the words

```python
template.write({'subject': '{{ object.company_id.name }}: invoice {{ object.name or "draft" }}'})
env.cr.commit()
```

- `subject`, `email_from`, `email_to`, `partner_to`, `email_cc`, `reply_to`, `lang` take
  `{{ expression }}`; `body_html` is QWeb (`<t t-out="object.name"/>`, `t-if`).
- Change words, keep expressions. For `body_html`, read the current body, edit that
  text, and write it back; never rebuild it from nothing.
- `partner_to` is a comma-separated list of partner ids (`{{ object.partner_id.id }}`);
  `email_to` is free addresses. Some standard templates set `use_default_to` instead,
  which sends to the document's default recipients.
- `lang` (usually `{{ object.partner_id.lang }}`) picks which translation is sent.

## Translations

`subject` and `body_html` keep one text per language. Write each language that customers
receive:

```python
template.with_context(lang='es_MX').write({'subject': 'Factura {{ object.name }} de {{ object.company_id.name }}'})
template.with_context(lang='fr_BE').write({'subject': 'Facture {{ object.name }} de {{ object.company_id.name }}'})
env.cr.commit()
```

The language must be active (`env['res.lang'].search([('code', '=', 'fr_BE')])`).

## Attachments and layout

- The PDF attached: `report_template` (one report) in 16.0; `report_template_ids`
  (several) from 17.0 on. `attachment_ids` adds fixed files such as terms and conditions.
- `email_layout_xmlid` (17.0 on) chooses the wrapper around the body. 20.0 adds
  `partner_cc`, `email_layout_force_header` and `email_layout_force_footer`.
- `mail_server_id` forces one outgoing server; leave it empty unless the user asks.

## Standard template or a copy

The standard templates are loaded `noupdate`: an edit survives module updates. The user
can bring back the original with "Reset Template" (`template.reset_template()`), which
discards the edit, so ask first. For a different email for some documents, copy it:

```python
copy = template.copy({'name': 'Invoice (wholesale customers)'})
env.cr.commit()
```

A copy is not used by anything until something points to it: the Send wizard's choice,
an automation rule, or a setting such as `invoice_mail_template_id` (Sales, template of
invoices sent after online payment).

## Test

Send to yourself, not to the customer: open the Send wizard on a test record, or render
as above. In a neutralized copy of production outgoing mail is off, so a "sent" email
there only reaches the outgoing queue (`mail.mail`).
