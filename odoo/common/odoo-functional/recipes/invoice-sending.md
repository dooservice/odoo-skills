# Sending invoices: email, post and product emails

A posted customer invoice reaches the customer through the send wizard (Send & Print): by
email, as a downloaded PDF, by post (`snailmail_account`) or, from 18.0, by Peppol
(`electronic-invoicing.md`). From 18.0 each customer has a preferred sending method that
the wizard proposes. A product can also carry its own email template
(`product_email_template`), sent when an invoice with that product is posted. Post
letters go through Odoo's IAP snailmail service, paid with IAP credits. All in Community.
The wording and attachments of the invoice email are a mail template
(`email-templates.md`); the PDF layout is in `reports-and-layout.md`.

**At a glance**

- Apps: `account`; `snailmail_account` (installs `snailmail`); `product_email_template`.
- Names that change by version: wizard `account.invoice.send` (16.0), `account.move.send`
  (17.0), `account.move.send.wizard` and `account.move.send.batch.wizard` (18.0+);
  methods `is_email`, `is_print`, `snailmail_is_letter` (16.0), `checkbox_send_mail`,
  `checkbox_download`, `checkbox_send_by_post` (17.0), `sending_methods` (18.0+);
  `invoice_sending_method` (18.0+); `manual` label Download (18.0), Manual (19.0+);
  invoice button Send & Print (16.0, 17.0), Send (18.0+).
- Sections: Before you start; The standard flow (1 set the customer's sending method,
  2 check the address or email, 3 send the invoice, 4 follow the letters); Variations;
  Versions; Verify; Pitfalls.

## Before you start

- Apps: `account`; `snailmail_account` (installed by the Snailmail setting; it
  installs `snailmail`); `product_email_template` from Apps. Installing needs the user's
  yes.
- Settings (Invoicing ‣ Configuration ‣ Settings ‣ Customer Invoices):

```python
env['res.config.settings'].create({
    'module_snailmail_account': True,
}).execute()
env.cr.commit()
```

- After the install, the Snailmail block shows `snailmail_color`, `snailmail_cover`
  (cover page with the address), `snailmail_duplex` (both sides).
- 16.0 and 17.0 also have the wizard's default checkboxes per company: 16.0
  `invoice_is_email`, `invoice_is_print`, `invoice_is_snailmail`; 17.0
  `invoice_is_email`, `invoice_is_download`, `invoice_is_snailmail`.
- Read first:

```python
print(env['ir.module.module'].search_read([('name', 'in', ['snailmail_account', 'product_email_template'])], ['name', 'state']))
print(env.company.read(['snailmail_color', 'snailmail_cover', 'snailmail_duplex']))
print(partner.read(['email', 'street', 'city', 'zip', 'country_id', 'invoice_sending_method']))
print(env['product.template'].search_read([('email_template_id', '!=', False)], ['name', 'email_template_id']))
```

`invoice_sending_method` exists from 18.0; on 16.0 and 17.0 leave it out.

## The standard flow

1. **Set the customer's sending method** (18.0+). Invoicing ‣ Customers ‣ Customers ‣ the
   customer ‣ Invoicing tab ‣ Invoice sending.

   ```python
   partner.invoice_sending_method = 'snailmail'
   env.cr.commit()
   ```

   Leaves the wizard proposing post for this customer, per company. Values: `email`
   ("by Email"), `manual` ("Download" in 18.0, "Manual" from 19.0), `snailmail` ("by
   Post", with `snailmail_account`), `peppol` ("by Peppol", with `account_peppol`).
   Up to 17.0 the wizard starts from the company's checkboxes instead.

2. **Check the address or email.** Post needs `street`, `city`, `zip` and `country_id`
   on the invoice's partner; email needs `email`. Missing data shows a warning in the
   wizard and that invoice is skipped for that method.

3. **Send the invoice.** The posted invoice ‣ Send (Send & Print in 16.0, 17.0); for
   several, select them in Invoicing ‣ Customers ‣ Invoices ‣ Send (Actions ‣ Send &
   Print in 16.0, 17.0).

   ```python
   wizard = env['account.move.send.wizard'].with_context(active_model='account.move', active_ids=invoice.ids).create({
       'sending_methods': ['email', 'snailmail'],
   })
   wizard.action_send_and_print()
   env.cr.commit()
   ```

   This is 18.0 to 20.0; several invoices use `account.move.send.batch.wizard` with the
   same call and each customer's own method. On 17.0:

   ```python
   wizard = env['account.move.send'].with_context(active_model='account.move', active_ids=invoice.ids).create({
       'checkbox_send_mail': True, 'checkbox_download': False, 'checkbox_send_by_post': True,
   })
   wizard.action_send_and_print()
   env.cr.commit()
   ```

   On 16.0:

   ```python
   ctx = invoice.action_invoice_sent()['context']
   wizard = env['account.invoice.send'].with_context(ctx, active_model='account.move', active_ids=invoice.ids).create({
       'is_email': True, 'is_print': False, 'snailmail_is_letter': True,
   })
   wizard.onchange_template_id()
   wizard.send_and_print_action()
   env.cr.commit()
   ```

   `onchange_template_id()` loads the template's subject and body into the email, as the
   form does. Leaves the invoice marked sent (`is_move_sent`), the email in its chatter and, for
   post, a letter (`snailmail.letter`) in `pending`. The letter is sent by the scheduled
   action "Snailmail: process letters queue" and moves to `sent` or `error`. Sending
   emails and paid letters to customers needs the user's yes.

4. **Follow the letters.** Settings ‣ Technical ‣ Email ‣ Snailmail Letters (developer
   mode), or the invoice's chatter, where a failed letter shows a red envelope with
   Resend and Cancel.

## Variations

- **An email per product.** The product ‣ Accounting tab ‣ Email Template
  (`email_template_id`, a template on `account.move`). Posting a customer invoice with
  that product posts the template in the invoice's chatter and subscribes the customer.

  ```python
  template = env['mail.template'].create({
      'name': 'Product A instructions', 'model_id': env['ir.model']._get_id('account.move'),
      'subject': 'How to use Product A', 'body_html': '<p>Instructions...</p>',
  })
  product.product_tmpl_id.email_template_id = template
  env.cr.commit()
  ```

  Only customer invoices (`out_invoice`) send it, once per line with the product.
- **Download only**: `manual` method (18.0+), `checkbox_download` (17.0), `is_print`
  (16.0); nothing is sent, the PDF is generated and attached.
- **Letters in color, with cover, both sides**: the Snailmail settings above; they
  change the price of each letter.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Wizard model | `account.invoice.send` | `account.move.send` | `account.move.send.wizard`, `account.move.send.batch.wizard` | same | same |
| Choose methods | `is_email`, `is_print`, `snailmail_is_letter` | `checkbox_send_mail`, `checkbox_download`, `checkbox_send_by_post` | `sending_methods` list | same | same |
| Customer's preferred method | no | no | `invoice_sending_method` | same | same |
| `manual` label | none | none | Download | Manual | Manual |
| Letter states | `pending`, `sent`, `error`, `canceled` | same | same | same | adds `process` |
| Button on the invoice | Send & Print | same | Send | same | same |

The same in every version: Invoicing ‣ Configuration ‣ Settings ‣ Customer Invoices ‣
Snailmail; Settings ‣ Technical ‣ Email ‣ Snailmail Letters; the product's Accounting
tab.

## Verify

```python
print(invoice.read(['is_move_sent']))
print(env['snailmail.letter'].search_read([('model', '=', 'account.move'), ('res_id', '=', invoice.id)], ['state', 'error_code', 'info_msg']))
print(invoice.message_ids[:3].mapped('subject'))
```

The invoice is sent, its letter is `pending` or `sent`, and the email is in the chatter.

## Pitfalls

- A letter in `error` with `CREDIT_ERROR` or `TRIAL_ERROR` needs IAP credits: the user
  buys them in Settings ‣ Odoo IAP; then Resend.
- `MISSING_REQUIRED_FIELDS`: complete the customer's address, then Resend.
- Letters are printed and posted by a third party: cancel within the queue time, after
  `sent` they cannot be recalled.
- An email template on many products sends one email per line: a long invoice floods
  the customer.
- On a neutralized copy outgoing mail servers are disabled: emails sent there stay in
  the queue.
