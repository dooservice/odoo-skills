# Email templates

A `mail.template` is the email Odoo prepares for a document: the quotation, the order
confirmation, the invoice, the delivery. It belongs to one model (`model`), and its
fields are rendered on the record being sent (`object`). Each app brings the templates of
its documents; this recipe changes their words, sender, recipients, attachments and
translations. Templates are edited from Settings ‣ Technical, which needs developer mode.
Email Marketing, Marketing Automation and Studio are left out.

## Before you start

- Apps: `mail`, installed by every app that sends documents. The templates come with
  their app (`sale`, `account`, `purchase`, `stock`).
- Settings: developer mode (Settings ‣ Developer Tools ‣ Activate the developer mode, or
  `?debug=1` in the URL), to see Settings ‣ Technical. Translations need two or more
  active languages (`languages-and-translations.md`).
- Find the standard template by XML id (`grep "mail.template" odoo-reference/xmlids/<addon>.md`),
  not by name: names are translated and users rename them. Common ones:
  `sale.email_template_edi_sale` (quotation), `sale.mail_template_sale_confirmation`
  (order confirmed), `account.email_template_edi_invoice` (invoice),
  `purchase.email_template_edi_purchase` (RFQ), `stock.mail_template_data_delivery_confirmation`.
- Read first:

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

## The standard flow

1. **Open the template.** Settings ‣ Technical ‣ Email ‣ Email Templates (developer
   mode), and open the one sent for that document.

   ```python
   template = env.ref('account.email_template_edi_invoice')
   ```

   Changes nothing.

2. **Change the subject and the body.** The subject is at the top of the form; the body
   is on the Content tab (16.0 to 18.0) or the Body tab (19.0 and 20.0), edited in place,
   with `/` for the powerbox and its Dynamic Placeholder, or as HTML with the `</>`
   button (developer mode).

   ```python
   template.write({'subject': '{{ object.company_id.name }}: invoice {{ object.name or "draft" }}'})
   env.cr.commit()
   ```

   - `subject`, `email_from`, `email_to`, `partner_to`, `email_cc`, `reply_to`, `lang`
     take `{{ expression }}`; `body_html` is QWeb (`<t t-out="object.name"/>`, `t-if`).
   - Change words, keep expressions. For `body_html`, read the current body, edit that
     text, and write it back; never rebuild it from nothing.

   Leaves the template changed for every document sent with it from now on, in the
   language of the write (see step 5).

3. **Set the sender and the recipients.** Email Configuration tab (16.0 to 18.0) or
   Settings tab (19.0 and 20.0): From, To (Emails), To (Partners), Cc, Reply To.

   ```python
   template.write({'reply_to': '{{ object.company_id.email }}'})
   env.cr.commit()
   ```

   - `partner_to` is a comma-separated list of partner ids (`{{ object.partner_id.id }}`);
     `email_to` is free addresses. Some standard templates set `use_default_to` instead,
     which sends to the document's default recipients.
   - Odoo documents Reply To for emails sent to many records at once (from a list view);
     a single document's replies follow its thread.

   Leaves the template with the new addresses.

4. **Attachments, language and server.** Settings tab in 16.0 to 18.0 (fixed
   attachments on the Content tab); in 19.0 and 20.0 language and server are on the
   Settings tab, reports and attachments on the Options tab.

   ```python
   template.read(['report_template_ids', 'attachment_ids', 'lang', 'mail_server_id', 'auto_delete'])   # 17.0+
   template.read(['report_template', 'attachment_ids', 'lang', 'mail_server_id', 'auto_delete'])       # 16.0
   ```

   - The PDF attached: `report_template` (one report) in 16.0; `report_template_ids`
     (several) from 17.0. `attachment_ids` adds fixed files such as terms and conditions.
   - `lang` (usually `{{ object.partner_id.lang }}`) picks which translation is sent.
     From 19.0 many standard templates leave it empty: the recipient's language is used.
   - `mail_server_id` forces one outgoing server; leave it empty unless the user asks.
   - `email_layout_xmlid` (17.0 on) chooses the wrapper around the body. 20.0 adds
     `partner_cc`, `email_layout_force_header` and `email_layout_force_footer`.

   Leaves the template sending those attachments, in that language.

5. **Translate.** On a translatable field (subject, body), the language button (`EN`)
   opens one value per active language; it appears with two or more active languages.

   ```python
   for lang, subject in {
       '<lang code>': '<subject in that language> {{ object.name }}',
       '<other lang code>': '<subject in the other language> {{ object.name }}',
   }.items():
       template.with_context(lang=lang).write({'subject': subject})
   env.cr.commit()
   ```

   `subject` and `body_html` keep one text per language: write each language that
   customers receive; the active ones are `env['res.lang'].search([]).mapped('code')`.
   Only active languages: with an inactive one, 16.0 and 17.0 overwrite the English text,
   18.0 and later refuse ("Invalid language code").

   Leaves one text per language; a language not written shows the `en_US` one.

6. **Preview, then send to yourself.** The Preview button renders the template on a
   chosen record and language. Then send it from a test document (its Send button) to
   your own address, not the customer's.

   ```python
   template._render_field('subject', record.ids)
   template._render_field('body_html', record.ids, compute_lang=True)
   ```

   Changes nothing. In a neutralized copy of production outgoing mail is off, so a
   "sent" email there only reaches the outgoing queue (`mail.mail`).

## Variations

- **A different email for some documents: a copy.** Duplicate the template (the form's
  action menu ‣ Duplicate) and change the copy. Choose it when the standard one must stay
  as it is for the other documents.

  ```python
  copy = template.copy()
  copy.name = 'Invoice (wholesale customers)'     # 16.0 ignores a name passed to copy()
  env.cr.commit()
  ```

  A copy is not used by anything until something points to it: the Send wizard's
  choice, an automation rule (`automations.md`), or a setting such as
  `invoice_mail_template_id` (Sales, template of invoices sent after online payment).
- **Back to the original: Reset Template.** The button on the form
  (`template.reset_template()`) reloads the module's version and discards the edit; ask
  first.
- **The wrapper around every email.** From 19.0, Settings ‣ Companies ‣ Update Mail
  Layout edits it; before 19.0 it is a QWeb view, which is code.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Menu (developer mode) | Settings ‣ Technical ‣ Email ‣ Email Templates | same | same | same | same |
| Body tab | Content | Content | Content | Body | Body |
| Sender and recipients tab | Email Configuration | Email Configuration | Email Configuration | Settings | Settings |
| Report attached, tab | Settings | Settings | Settings | Options | Options |
| Report attached, field | `report_template` (one) | `report_template_ids` | `report_template_ids` | `report_template_ids` | `report_template_ids` |
| `email_layout_xmlid` | - | yes | yes | yes | yes |
| `partner_cc`, `email_layout_force_header/footer` | - | - | - | - | yes |
| `lang` on standard templates | set | set | set | often empty | often empty |
| Write in an inactive language | overwrites English | overwrites English | refused | refused | refused |
| Name passed to `copy()` | ignored | used | used | used | used |
| Settings ‣ Companies ‣ Update Mail Layout | - | - | - | yes | yes |

## Verify

```python
template = env.ref('account.email_template_edi_invoice')
record = env['account.move'].search([('move_type', '=', 'out_invoice'), ('state', '=', 'posted')], limit=1)
print(template._render_field('subject', record.ids))
print(template.with_context(lang='<lang code>')._render_field('subject', record.ids))
print(template.read(['email_from', 'partner_to', 'reply_to', 'lang']))
```

The rendered subject shows the new words with the document's values; each language
shows its own text.

## Pitfalls

- **Standard templates are `noupdate`.** An edit survives module updates, but "Reset
  Template" (or a user who presses it) discards it. Record every edit in the change note.
- **A body rebuilt from nothing** loses the standard expressions, buttons and
  conditions. Always edit the current `body_html`.
- **Searching by name** finds the translated or renamed template, or none. Use the XML id.
- **A copy nobody points to** is never sent. Link it from the Send wizard, an automation
  or a setting.
- **Writing without `lang`** in the context goes to the environment's language (often
  `en_US` in a shell), not the customer's. Say which language you write.
- **`mail_server_id` set by hand** forces that server for every email of the template;
  leave it empty unless the user asks (`mail-servers.md`).
- **Testing in a neutralized copy**: mail never leaves; check `mail.mail` instead of the
  inbox.
