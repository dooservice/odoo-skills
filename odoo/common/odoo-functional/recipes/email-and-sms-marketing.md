# Email and SMS marketing

A mailing (`mailing.mailing`) sends one designed email, or one SMS, to many recipients:
the contacts of mailing lists (`mailing.list`, `mailing.contact`) or the records of
another model filtered by a domain (customers, leads, attendees). Each recipient gets a
trace (`mailing.trace`) that records sent, opened, clicked, replied and bounced. Links
are rewritten through the link tracker with UTM campaign, medium and source, so leads,
orders and revenue come back to the campaign. This recipe also covers SMS, the website
newsletter forms, link tracking, KPI digests, marketing cards and the company's social
links. Marketing Automation and Social Marketing are Enterprise and left out. The mail
server and bounces are in `mail-servers.md`; transactional templates in
`email-templates.md`.

**At a glance**

- Apps: `mass_mailing`, `mass_mailing_sms`; bridges such as `mass_mailing_themes`,
  `mass_mailing_crm`, `mass_mailing_sale`, `website_mass_mailing`,
  `website_sale_mass_mailing` (18.0+); `sms_twilio` (17.0+); `marketing_card` (18.0+).
- Names that change by version: `mailing.contact.subscription` (16.0),
  `mailing.subscription` (17.0+); `is_public` default True (16.0), False (17.0+);
  `trace_status` adds `process`, `pending` and `sent` means delivered (17.0+); lists menu
  Mailing Lists (16.0-19.0), Recipients (20.0); saved templates as favorites
  (16.0-19.0), Templates menu (20.0).
- Sections: Before you start; The standard flow (1 mailing list and contacts, 2 create the
  mailing, 3 test, 4 send or schedule, 5 read the results); Variations; Versions; Verify;
  Pitfalls.

## Before you start

- Apps: `mass_mailing` (Email Marketing); `mass_mailing_sms` (SMS Marketing). Bridges
  install themselves: `mass_mailing_themes`, `mass_mailing_crm`, `mass_mailing_sale`,
  `mass_mailing_event`, `mass_mailing_event_track`, `mass_mailing_slides`,
  `website_mass_mailing`, `website_mass_mailing_sms`, `website_sale_mass_mailing` (18.0+).
- Settings (Email Marketing ‣ Configuration ‣ Settings): `group_mass_mailing_campaign`
  (Mailing Campaigns: the Campaigns menu and A/B tests across mailings),
  `mass_mailing_outgoing_mail_server` with `mass_mailing_mail_server_id` (a dedicated
  server), `show_blacklist_buttons`, `mass_mailing_reports` (report to the sender);
  18.0+ `mass_mailing_split_contact_name` (first and last name on contacts).
- SMS go through Odoo's IAP service (prepaid credits). 17.0+ `sms_twilio` adds
  `sms_provider` (`iap` or `twilio`) in Settings ‣ General Settings, SMS section, with
  the Twilio account SID, token and numbers. Credentials come from the user.
- Read first:

```python
print(env['ir.mail_server'].search_read([], ['name', 'smtp_host', 'active']))
print(env['mailing.list'].search_read([], ['name', 'contact_count', 'is_public']))
print(env['mailing.mailing'].search_read([], ['subject', 'mailing_type', 'state', 'sent_date'], limit=10, order='id desc'))
print(env['ir.config_parameter'].sudo().get_param('mass_mailing.outgoing_mail_server'))
```

## The standard flow

1. **Mailing list and contacts.** Email Marketing ‣ Mailing Lists ‣ Mailing Lists ‣ New
   (20.0: ‣ Recipients ‣ Mailing Lists); contacts in ‣ Mailing List Contacts (20.0:
   Recipients ‣ Mailing Contacts), or imported (`partners-and-imports.md` for the import
   rules).

   ```python
   mlist = env['mailing.list'].create({'name': 'Newsletter', 'is_public': True})
   env['mailing.contact'].create([
       {'name': 'Customer A', 'email': 'customer.a@example.com', 'list_ids': [(4, mlist.id)]},
       {'name': 'Customer B', 'email': 'customer.b@example.com', 'list_ids': [(4, mlist.id)]},
   ])
   env.cr.commit()
   ```

   Leaves the contacts subscribed. A subscription is `mailing.contact.subscription`
   (16.0) or `mailing.subscription` (17.0+), with `opt_out`. `is_public` shows the list
   on the recipients' subscription page (default True in 16.0, False from 17.0).

2. **Create the mailing.** Email Marketing ‣ Mailings ‣ New: subject, recipients (a
   mailing list, or a model with a filter), then the body in the editor (a theme from
   `mass_mailing_themes`, or a saved template in 20.0).

   ```python
   mailing = env['mailing.mailing'].create({
       'subject': 'November news',
       'mailing_model_id': env['ir.model']._get_id('mailing.list'),
       'contact_list_ids': [(6, 0, [mlist.id])],
       'body_html': '<p>Hello,</p><p><a href="https://shop.example.com/sale">See the offers</a></p>',
   })
   env.cr.commit()
   ```

   Leaves it in `draft`. For records of another model: `mailing_model_id` of that model
   (only models with `is_mailing_enabled`) and `mailing_domain`, for example
   `"[('customer_rank', '>', 0)]"` on `res.partner`.

3. **Test.** The mailing's Test button, one address per line.

   ```python
   env['mailing.mailing.test'].create({'mass_mailing_id': mailing.id,
                                       'email_to': 'me@example.com'}).send_mail_test()
   env.cr.commit()
   ```

   Sends one copy; the mailing stays `draft`.

4. **Send or schedule.** Send (now) or Schedule (a date).

   ```python
   mailing.action_launch()
   env.cr.commit()
   ```

   To schedule instead: write `schedule_type='scheduled'` and `schedule_date`, then
   `mailing.action_schedule()`.

   Leaves it `in_queue`. The scheduled action `mass_mailing.ir_cron_mass_mailing_queue`
   sends it in batches (`sending`, then `done`). Blacklisted, opted-out and duplicate
   addresses are skipped and traced as `cancel`.

5. **Read the results.** The mailing's smart buttons (Sent, Opened, Clicked, Replied,
   Bounced), Email Marketing ‣ Reporting, and on the campaign the leads, quotations and
   revenue (with `mass_mailing_crm`, `mass_mailing_sale`).

   ```python
   mailing.invalidate_recordset()
   print(mailing.state, mailing.sent, mailing.opened_ratio, mailing.clicks_ratio, mailing.bounced_ratio)
   print(env['mailing.trace'].read_group([('mass_mailing_id', '=', mailing.id)], ['trace_status'], ['trace_status']))
   ```

   `trace_status` 16.0: `outgoing`, `sent`, `open`, `reply`, `bounce`, `error`,
   `cancel`; 17.0+ adds `process` and `pending` (Sent) and `sent` means Delivered.

## Variations

- **Campaigns.** With `group_mass_mailing_campaign`, Email Marketing ‣ Campaigns groups
  mailings and SMS of one `utm.campaign` (stages in Configuration ‣ Campaign Stages).
- **A/B test.** On the mailing, A/B Tests tab: `ab_testing_enabled`, `ab_testing_pc`
  (percentage of recipients per version), `ab_testing_winner_selection` (`manual`,
  `opened_ratio`, `clicks_ratio`, `replied_ratio`; `crm_lead_count` with
  `mass_mailing_crm`; `sale_quotation_count`, `sale_invoiced_amount` with
  `mass_mailing_sale`) and `ab_testing_schedule_datetime`. Duplicate the mailing for
  each version: same campaign, same settings. At that date the winner goes to the rest
  (`action_send_winner_mailing`, or Send this version for `manual`).
- **SMS mailing.** SMS Marketing ‣ SMS Marketing ‣ New: `mailing_type='sms'`,
  `body_plaintext`; recipients need a valid mobile. `sms_allow_unsubscribe` adds a stop
  link. Without credits the mailing shows `sms_has_insufficient_credit`.
- **Mail the attendees or members of another app.** Event: Contact Attendees and Invite
  (`mass_mailing_event`); tracks: Contact Track Speakers (`mass_mailing_event_track`);
  courses: Contact Attendees (`mass_mailing_slides`). Each opens a mailing on that model.
- **Dynamic lists.** A saved filter (`mailing.filter`): the Favorite Filters menu up to
  19.0, Recipients ‣ Dynamic Lists in 20.0.
- **Newsletter on the website** (`website_mass_mailing`). The Newsletter building blocks
  (form, popup) subscribe visitors to a list; with `website_mass_mailing_sms` they can
  give a phone number. reCAPTCHA or Turnstile protect them (`website-content.md`).
  18.0+ `website_sale_mass_mailing`: Website ‣ Configuration ‣ Settings,
  `is_newsletter_enabled` and `newsletter_id` add a newsletter checkbox at checkout.
- **Opt-out and blacklist.** Every mailing has an unsubscribe link. Email Marketing ‣
  Configuration ‣ Blacklisted Email Addresses (`mail.blacklist`); SMS Marketing ‣
  Configuration ‣ Blacklisted Phone Numbers (`phone.blacklist`). 17.0+ Optout Reasons
  and an Opt-Out report.
- **Tracked links and UTMs** (`link_tracker`, `utm`, `website_links`). Every link in a
  mailing becomes a `link.tracker` with the mailing's campaign, medium and source. Short
  links by hand: Email Marketing ‣ Configuration ‣ Link Tracker, or on the website the
  Link Tracker page (`/r`, from Website ‣ Site ‣ This page ‣ Link Tracker). UTM records:
  developer mode, Link Tracker ‣ UTMs.

  ```python
  link = env['link.tracker'].create({'url': 'https://shop.example.com/sale', 'title': 'Sale',
                                     'campaign_id': mailing.campaign_id.id, 'medium_id': env.ref('utm.utm_medium_email').id})
  print(link.short_url, link.count)
  ```

- **KPI digest** (`digest`). Settings ‣ General Settings, Digest Email (`digest_emails`,
  `digest_id`): a periodic email of key figures to internal users. The digest records
  (`digest.digest`: `periodicity` `daily`, `weekly`, `monthly`, `quarterly`; the KPI
  checkboxes; `user_ids`) are in developer mode, Settings ‣ Technical ‣ Email ‣ Digest
  Emails.
- **Marketing cards** (18.0+, `marketing_card`). Marketing Card ‣ Campaigns ‣ New: a
  card design (`card_template_id`), the record type it is built for (`res_model`:
  contacts, and from `marketing_card_event` attendees, booths, tracks), header and
  texts, and `target_url`. Send creates a mailing; each recipient gets a personal image
  to share, and clicks and shares are counted.
- **Social links** (`social_media`). Settings ‣ Users & Companies ‣ Companies ‣ the
  company, Social Media group: `social_twitter`, `social_facebook`, `social_github`,
  `social_linkedin`, `social_youtube`, `social_instagram`; 17.0+ `social_tiktok`; 19.0+
  `social_discord`. Mailing themes and the website footer use them.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Lists menu | Mailing Lists | same | same | same | Recipients |
| Subscription model | `mailing.contact.subscription` | `mailing.subscription` | same | same | same |
| `is_public` default | True | False | False | False | False |
| Trace statuses | 7, `sent` = sent | adds `process`, `pending`; `sent` = delivered | same | same | same |
| Twilio provider | no | `sms_twilio` | yes | yes | yes |
| Split contact name | no | no | yes | yes | yes |
| Newsletter at checkout | no | no | `website_sale_mass_mailing` | yes | yes |
| Marketing cards | no | no | yes | yes | yes, plus `marketing_card_event` |
| Saved mailing templates | favorites | favorites | favorites | favorites | Templates menu |
| `social_tiktok` / `social_discord` | no / no | yes / no | yes / no | yes / yes | yes / yes |

## Verify

```python
mailing.invalidate_recordset()
print(mailing.state, mailing.sent_date, mailing.expected, mailing.sent, mailing.canceled, mailing.failed)
print(mailing.campaign_id.name, mailing.medium_id.name, mailing.source_id.name)
```

`expected` is the number of recipients; `canceled` and `failed` explain the gap.

## Pitfalls

- Sending is irreversible. Test first, read the recipient count, and ask the user before
  `action_launch`.
- Mailings from a domain without SPF and DKIM for the sending server land in spam;
  check the domain with the user (`mail-servers.md`). A neutralized copy sends nothing.
- A mailing on `res.partner` with an empty domain reaches every contact with an email,
  vendors included: always set `mailing_domain`.
- Importing contacts without their consent breaks privacy law in many countries; ask
  where the addresses come from.
- SMS cost credits per message part; long texts and special characters double the
  parts.
