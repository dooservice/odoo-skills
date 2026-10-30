# Lead generation

Leads (`crm.lead`) reach CRM from several sources: the website contact form
(`website_crm`), live chat (`crm_livechat`), company data that Odoo fills from the
lead's email domain (`crm_iap_enrich`), lead mining by country, industry and size
(`crm_iap_mine`), companies identified from website visits (`website_crm_iap_reveal`),
and SMS follow-up from the pipeline (`crm_sms`). Leads a reseller should handle are
assigned by geolocation and forwarded to them (`website_crm_partner_assign`). Enrichment,
mining, visit identification, SMS and company autocomplete are In-App Purchase (IAP)
services: they run on Odoo S.A.'s servers and spend prepaid credits of the database's
IAP accounts (`iap`). All of this is in Community; the credits are bought from Odoo S.A.
Qualifying and converting leads is in `sales-and-crm.md`.

**At a glance**

- Apps: `crm`; `website_crm`, `crm_livechat`, `crm_sms`, `crm_iap_enrich`, `crm_iap_mine`,
  `website_crm_iap_reveal`; `website_crm_partner_assign` for resellers.
- Names that change by version: enrichment cron hourly up to 18.0, daily 19.0+; lead
  mining of companies only in 20.0; chatbot step `create_lead_and_forward` 19.0 only; live
  chat channel `mail.channel` in 16.0, `discuss.channel` 17.0+; reseller levels
  (`res.partner.grade`) in `website_crm_partner_assign` up to 18.0, `partnership` 19.0+,
  with menus under CRM ‣ Configuration ‣ Resellers up to 18.0 and CRM ‣ Configuration ‣
  Members 19.0+; SMS states add `process`, `pending` 17.0+.
- Sections: Before you start; The standard flow (1 check the IAP credits, 2 send contact
  form submissions to a team, 3 create leads from live chat, 4 enrich the leads, 5 mine
  new leads, 6 turn website visits into leads, 7 follow up by SMS, 8 grade the resellers,
  9 assign and forward the lead); Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: `crm`. `website_crm` installs itself with `crm` and `website`; `crm_livechat` with
  `crm` and `im_livechat`; `crm_sms` with `crm` and `sms`; `crm_iap_enrich` and
  `crm_iap_mine` with `crm`. `website_crm_iap_reveal` is installed from the CRM setting
  below.
  `website_crm_partner_assign` (Resellers) is installed from Apps; from 19.0 it needs
  `partnership`, from 20.0 `website_partnership`.
- Settings (CRM ‣ Configuration ‣ Settings, all versions unless noted):

| Setting | Field | Notes |
|---|---|---|
| Leads | `group_use_lead` | without it every new lead is an opportunity |
| Lead Enrichment | `module_crm_iap_enrich`, `lead_enrich_auto` (`auto`, `manual`) | `lead_enrich_auto` activates or archives the cron `crm_iap_enrich.ir_cron_lead_enrichment` |
| Lead Mining | `module_crm_iap_mine`, `lead_mining_in_pipeline` | the second adds a Generate Leads button to the pipeline |
| Visits to Leads | `module_website_crm_iap_reveal` | needs `website` |
| Partner Autocomplete | `module_partner_autocomplete` | General Settings; `base_setup` |
| Membership / Partnership | `module_partnership` | 19.0+ |

- IAP credits: each service has an `iap.account` per database (or per company, with
  `company_ids`). Enrichment, mining and visits spend the `reveal` service, SMS the `sms`
  service, autocomplete the `partner_autocomplete` service. The account is created on
  first use; buying credits happens on Odoo S.A.'s site, from the account's Buy Credits
  button or the URL below.
- Read first:

```python
s = env['res.config.settings'].create({})
print(s.group_use_lead, s.module_crm_iap_enrich, s.lead_enrich_auto, s.module_crm_iap_mine,
      s.lead_mining_in_pipeline, s.module_website_crm_iap_reveal)
print(env['ir.module.module'].search_read([('name', 'in', ['website_crm', 'crm_livechat', 'crm_sms',
      'crm_iap_enrich', 'crm_iap_mine', 'website_crm_iap_reveal', 'website_crm_partner_assign',
      'partner_autocomplete'])], ['name', 'state']))
for a in env['iap.account'].sudo().search([]):
    print(a.id, a.service_name, a.company_ids.mapped('name'), (a.account_token or '')[-9:])
```

A token that ends in `+disabled` belongs to a neutralized copy: its IAP calls fail and
spend nothing.

## The standard flow

Odoo's documentation sets up each source of leads, then sends the leads a reseller should
handle to that reseller. Every step that calls an IAP service says so: run it only with
the user's yes, because it spends real credits.

1. **Check the IAP credits.** Settings ‣ Technical ‣ IAP ‣ IAP Accounts (In-App Purchase
   Accounts in 20.0), in developer mode; or the Buy credits link under each setting.

   ```python
   acc = env['iap.account']
   print(acc.get_credits('reveal'), acc.get_credits('sms'))   # asks Odoo's IAP server; spends nothing, -1 on error
   print(acc.get_credits_url('reveal'))                        # creates the account if missing; no call
   ```

   Leaves the balance known. The user buys credits at the URL; nothing changes in the
   database except the account.

2. **Send contact form submissions to a team.** Website ‣ Go to Website, open the Contact
   Us page, Edit, select the form: Action `Create an Opportunity`, and its Sales Team and
   Salesperson options. Without them, the website's defaults apply.

   ```python
   website = env['website'].search([], limit=1)
   website.write({'crm_default_team_id': team.id, 'crm_default_user_id': seller.id})
   env.cr.commit()
   ```

   Leaves every form submission creating a `crm.lead` with medium `Website`
   (`utm.utm_medium_website`), the form's team and salesperson (or the website's), and
   type `lead` when that team has `use_leads`, else `opportunity`. The lead is linked to
   the website visitor (`visitor_ids`), whose pages appear under its Page Views button.

3. **Create leads from live chat.** Live Chat ‣ Configuration ‣ Chatbots, open the
   chatbot, add a step of type Create Lead after the steps that ask the email and phone.

   ```python
   bot = env['chatbot.script'].search([('title', '=', 'Example Bot')], limit=1)
   env['chatbot.script.step'].create({
       'chatbot_script_id': bot.id, 'step_type': 'create_lead', 'crm_team_id': team.id,
       'message': 'Thank you. A salesperson will contact you.',
   })
   env.cr.commit()
   ```

   Leaves the chatbot creating a lead named `<chatbot title>'s New Lead` with the
   conversation as description, in that team (type `lead` when the team uses leads).
   An operator in a conversation types `/lead <title>` to do the same by hand (19.0+:
   the lead keeps the conversation in `origin_channel_id`).

4. **Enrich the leads.** Automatic with `lead_enrich_auto='auto'`; by hand, the lead's
   Enrich button (shown while `show_enrich_button` is true). Uses `reveal` credits.

   ```python
   lead.iap_enrich()   # IAP call: spends credits; commits each batch of 50 by itself
   print(lead.iap_enrich_done, lead.partner_name, lead.street, lead.city, lead.country_id.name)
   ```

   Leaves `iap_enrich_done` true, the company name, address, phone, country and state
   filled where empty, and a note with the company data in the chatter. Generic email domains
   (Gmail and the like) are marked done without a call; leads without email, won leads
   and leads already revealed are skipped. The cron only takes leads created in the last
   hour (16.0 to 18.0) or the last 24 hours (19.0+).

5. **Mine new leads.** CRM ‣ Configuration ‣ Lead Generation ‣ Lead Mining Requests ‣ New
   (or the pipeline's Generate Leads button with `lead_mining_in_pipeline`): number of
   leads, countries, industries, size, team, salesperson, tags; Generate Leads. Uses
   `reveal` credits.

   ```python
   req = env['crm.iap.lead.mining.request'].create({
       'lead_number': 3, 'lead_type': 'opportunity', 'team_id': team.id, 'user_id': seller.id,
       'country_ids': [(6, 0, [country.id])], 'industry_ids': [(6, 0, industries.ids)],
       'filter_on_size': True, 'company_size_min': 10, 'company_size_max': 50,
       'tag_ids': [(6, 0, [tag.id])],
   })
   env.cr.commit()
   req.action_submit()   # IAP call: spends credits
   env.cr.commit()
   ```

   Leaves the request in `done` with its leads in `lead_ids` (`lead_mining_request_id` on
   each lead), or in `error` with `error_type='credits'`; with no match it stays in
   `draft` with `error_type='no_result'`.
   16.0 to 19.0 can also target contacts: `search_type='people'` with
   `contact_number`, `contact_filter_type` (`role`, `seniority`), `preferred_role_id`,
   `role_ids`, `seniority_id`. 20.0 mines companies only.

6. **Turn website visits into leads.** CRM ‣ Configuration ‣ Lead Generation ‣ Visits to
   Leads Rules ‣ New: pages (`regex_url`), countries and states, website, company
   filters, type, team, salesperson, tags, suffix.

   ```python
   rule = env['crm.reveal.rule'].create({
       'name': 'Pricing page', 'regex_url': '/pricing', 'country_ids': [(6, 0, [country.id])],
       'lead_for': 'companies', 'lead_type': 'lead', 'team_id': team.id, 'suffix': 'Web visit',
   })
   env.cr.commit()
   ```

   Leaves the rule active. Each page view by a public visitor that matches it stores the
   visitor's IP (`crm.reveal.view`, `reveal_state='to_process'`); the daily cron
   `website_crm_iap_reveal.ir_cron_crm_reveal_lead` sends them to IAP (spends `reveal`
   credits) and creates a lead per company identified, with `reveal_rule_id` set.
   Visitors who already have a lead are skipped.

7. **Follow up by SMS.** CRM ‣ Sales ‣ My Pipeline, list view, select the opportunities,
   SMS (or the SMS button on one lead). Uses `sms` credits.

   ```python
   composer = env['sms.composer'].create({
       'composition_mode': 'mass', 'res_model': 'crm.lead', 'res_ids': repr(leads.ids),
       'body': 'Example Shop: your quotation is ready.', 'mass_keep_log': True,
   })
   composer.action_send_sms()
   env.cr.commit()
   ```

   Leaves one `sms.sms` per lead in `outgoing` and a note on each lead. The cron SMS: SMS
   Queue Manager sends them through IAP, which spends the credits. On a copy of
   production, say that they will not leave.

8. **Grade the resellers.** CRM ‣ Configuration ‣ Resellers ‣ Partner Levels (16.0 to
   18.0); CRM ‣ Configuration ‣ Members ‣ Levels (19.0+, the menu takes the company's
   `partnership_label`, `Members` by default). Then on each reseller's contact, tab
   Partner Assignment: Partner Level, and Geolocation's compute button.

   ```python
   grade = env['res.partner.grade'].create({'name': 'Gold', 'partner_weight': 10})
   reseller.write({'grade_id': grade.id})
   reseller.geo_localize()   # calls the geolocation provider (OpenStreetMap by default), not IAP
   print(reseller.partner_weight, reseller.partner_latitude, reseller.partner_longitude)
   env.cr.commit()
   ```

   Leaves the reseller with `partner_weight` taken from its level (0 means never
   assigned) and coordinates. Its contacts need portal access to see their leads.

9. **Assign and forward the lead.** The lead's Assigned Partner tab: Automatic Assignment,
   then Send Email.

   ```python
   lead.action_assign_partner()
   print(lead.partner_assigned_id.name, lead.user_id.name, lead.date_partner_assign)
   wizard = env['crm.lead.forward.to.partner'].with_context(
       active_ids=lead.ids, default_composition_mode='forward').create({
       'forward_type': 'single', 'partner_id': lead.partner_assigned_id.id,
   })
   wizard.action_forward()
   env.cr.commit()
   ```

   Leaves the lead geolocated, `partner_assigned_id` set (chosen at random among the
   nearest graded resellers in the lead's country, weighted by `partner_weight`), the
   reseller's salesperson as `user_id`, and an email with the portal link in the mail
   queue. The reseller opens it in the portal (`/my/leads`, `/my/opportunities`) and
   accepts it, which converts it to an opportunity, or declines it, which clears the
   assignment and adds the reseller to `partner_declined_ids`.

## Variations

- **Enrich on demand only.** `lead_enrich_auto='manual'`: the cron is archived and only
  the Enrich button (step 4) spends credits. Choose it when credits are scarce.
- **Forward many leads at once.** CRM ‣ Leads, list, select, Action ‣ Forward to partner:
  the wizard opens with `forward_type='assigned'` lines that use the automatic
  assignment; each reseller gets one email with all its leads.

  ```python
  wizard = env['crm.lead.forward.to.partner'].with_context(
      active_ids=leads.ids, default_composition_mode='mass_mail').create({'forward_type': 'assigned'})
  wizard.action_forward()
  env.cr.commit()
  ```

- **Chatbot that creates the lead and hands over.** 19.0 only: step type
  `create_lead_and_forward` creates the lead and forwards the visitor to an operator.
- **Company autocomplete on contacts.** With `partner_autocomplete`, typing a company
  name on a contact or company form suggests companies and fills address, VAT, logo and
  industry; each fill spends `partner_autocomplete` credits. 20.0 adds Action ‣ Enrich
  (`action_enrich_partner`) on existing contacts.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Enrichment cron | hourly, leads of the last hour | same | same | daily, leads of the last 24 hours | same as 19.0 |
| Lead mining targets | companies or companies and contacts | same | same | same | companies only; `company_size_max` defaults to 100 |
| Chatbot steps | `create_lead` | same | same | `create_lead`, `create_lead_and_forward` | `create_lead` |
| Live chat channel model | `mail.channel` | `discuss.channel` | same | same, lead keeps `origin_channel_id` | same as 19.0 |
| Reseller levels (`res.partner.grade`) | `website_crm_partner_assign` | same | same | `partnership`, extended with `partner_weight` | same as 19.0 |
| Menu: levels | CRM ‣ Configuration ‣ Resellers ‣ Partner Levels | same | same | CRM ‣ Configuration ‣ Members ‣ Levels | same as 19.0 |
| Menu: activations | CRM ‣ Configuration ‣ Resellers ‣ Partner Activations | same | same | CRM ‣ Configuration ‣ Members ‣ Partner Activations | same as 19.0 |
| Menu: IAP accounts | Settings ‣ Technical ‣ IAP ‣ IAP Accounts | same | same | same | Settings ‣ Technical ‣ IAP ‣ In-App Purchase Accounts |
| SMS states | `outgoing`, `sent`, `error`, `canceled` | adds `process`, `pending` | same | same | same |

The same in every version: CRM ‣ Configuration ‣ Lead Generation ‣ Lead Mining Requests,
CRM ‣ Configuration ‣ Lead Generation ‣ Visits to Leads Rules, Live Chat ‣ Configuration
‣ Chatbots, the `/lead` command, the lead's Enrich button and Assigned Partner tab.

## Verify

```python
Lead = env['crm.lead'].with_context(active_test=False)
print(Lead.search_count([('medium_id', '=', env.ref('utm.utm_medium_website').id)]),
      Lead.search_count([('iap_enrich_done', '=', True)]),
      Lead.search_count([('lead_mining_request_id', '!=', False)]),
      Lead.search_count([('reveal_rule_id', '!=', False)]),
      Lead.search_count([('partner_assigned_id', '!=', False)]))
print(env['crm.iap.lead.mining.request'].search_read([], ['name', 'state', 'error_type', 'lead_count']))
print(env['crm.reveal.view'].sudo().read_group([], ['reveal_state'], ['reveal_state']))
print(env['sms.sms'].sudo().read_group([('model', '=', 'crm.lead')], ['state'], ['state']))
```

Each source shows the leads it created; mining requests are `done`; visits leave the
`to_process` state after the daily cron; SMS leave `outgoing`.

## Pitfalls

- On a neutralized copy IAP tokens end in `+disabled`: enrichment, mining, visits and SMS
  fail there. Never buy credits from a copy, and never copy a production token into it.
- Credits run out silently in the crons: enrichment and visit identification stop and
  log it. Read the balance (step 1) before blaming the configuration.
- Visits to Leads needs a GeoIP database on the server and the real client IP: behind a
  reverse proxy, Odoo runs with `--proxy-mode`; without both, no visit is recorded.
- Leads created before the enrichment cron's window (one hour, or 24 hours from 19.0)
  are never enriched automatically: use the Enrich button.
- Automatic Assignment skips leads without a country and tags leads with no reseller in
  range `No more partner available`. A reseller whose level weighs 0 is never chosen.
- Forwarding fails when the reseller has no email; the reseller sees nothing in the
  portal until one of its contacts has portal access.
- A chatbot Create Lead step placed before the email question creates leads without
  email, which enrichment cannot use.
