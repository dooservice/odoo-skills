# The method in full

The detail behind the short method in `SKILL.md`: each step, the ways into the
database, the rules that save databases, the country, the parts of a recipe and what
each one covers, the change note, and when a request needs code.

Most requests are configuration: a setting, a record, a rule, a template. They are data
in the database, changed through the ORM so Odoo's own checks, computes and access rules
run. No module is written. Code is the last resort (see the end).

## The method

1. **Understand the request in business terms.** Which company, which documents, which
   people, what should happen that does not today. Ask when it is ambiguous; one question
   saves a wrong configuration.
2. **Read the current state.** The records involved, their values, and what uses them.
   Never change what you have not read.
3. **Find the right lever.** The setting, field or XML id, in `odoo-reference` for this
   version (`settings.md`, `models/<addon>.md`, `xmlids/<addon>.md`), not from memory:
   names change between versions.
4. **Propose, then wait.** What will change, on which records, how many, and how to undo
   it. Changes to many records, access rights, record rules, accounting or users need
   the user's yes. Prefer archiving (`active=False`) to deleting.
5. **Change through the ORM**, in the smallest step that works.
6. **Verify.** Read the records again, and try it as the user would: create the document,
   open it as the affected user, run the action on one record.
7. **Leave a change note** (below), so the change can be repeated elsewhere.

## Reaching the database

Use what the environment gives, in this order. `connect.md` has the details.

- **Tools that read and write records through the ORM**, when your environment provides
  them (an MCP server, a platform's own tools). They usually add confirmation and limits.
- **`odoo-bin shell`** on the server, with a script on stdin ending in `env.cr.commit()`.
- **The external API** with an API key, when there is no shell: Odoo.sh, Odoo Online, a
  server you only reach over HTTP. XML-RPC up to 18.0; JSON-2 from 19.0, where XML-RPC
  and JSON-RPC are deprecated.
- **SQL only to look**, never to change: it skips computes, constraints, access rules and
  the cache.

## Rules that save databases

- **Write for one version.** Read it first (`odoo.release.series` in a shell, the
  `server_version` of the external API) and use only that version's models, fields and
  values. Recipes give one block per version range, newest first: copy the block of
  this version. Never write fallbacks that test for a field or model
  (`'a' if 'a' in env['x'] else 'b'`) and never leave another version's names in
  comments: a name from another version fails, or is silently ignored.
- **Records are shared.** A tax, journal, pricelist or template changed here changes every
  document that uses it. Count the users before changing one in use.
- **Posted accounting is history.** Never change a tax, account or journal that has posted
  entries: create a new one and archive the old.
- **Settings go through Settings.** Write a `res.config.settings` and `execute()` it, so
  groups, modules and parameters follow; never write the parameter or group by hand.
- **XML ids over names.** `env.ref('sale.email_template_edi_sale')` survives renames and
  translations; a search by name does not.
- **Multi-company.** Most configuration is per company. Read `company_id` before writing,
  and use `with_company()` when creating for another company.
- **Translations.** Translatable fields keep one value per language: write with
  `with_context(lang=...)` for each language that matters.
- **Standard records may come back.** A module update can rewrite standard data unless it
  is `noupdate`. Prefer a copy for large changes to standard templates, views or rules.
- **A copy of production is not production.** In a neutralized or test copy, outgoing
  mail, scheduled actions and payment providers are off; say so when the user tests there.

## The country

This skill covers Odoo's standard flows, the same in every country. What depends on one
country (its chart of accounts, taxes, identification of contacts, electronic invoicing,
legal reports) comes from its `l10n_*` modules and is not covered here. Read which ones the
database has:

```python
env['ir.module.module'].search([('name', '=like', 'l10n\\_%'), ('state', '=', 'installed')]).mapped('name')
```

For anything country-specific, say that it is not covered, read what the installed `l10n_*`
module defines, and check it with the user before acting.

## Recipe index

Read the matching one before starting. Each has the same parts: *Before you start* (apps,
settings, what to read first), *The standard flow* (Odoo's own steps, in the order a user
takes them, each with its menu, its ORM equivalent and the state it leaves),
*Variations*, *Versions*, *Verify* and *Pitfalls*.

| Recipe | Covers |
|---|---|
| `recipes/go-live.md` | starting a new company: the order to load its data, opening balances, open invoices, initial stock |
| `recipes/diagnosis.md` | "why does Odoo do X": access errors, missing taxes, wrong prices, hidden records, silent automations |
| `recipes/companies.md` | companies, multi-company, the chart of accounts |
| `recipes/users-and-access.md` | users, groups, record rules, portal users |
| `recipes/authentication-and-security.md` | password rules, two-factor and its enforcement, passkeys, timeouts, OAuth and LDAP login, module import, certificates, cloud storage |
| `recipes/currencies-and-rates.md` | currencies, rates, multi-currency |
| `recipes/taxes-and-journals.md` | taxes, journals, invoice numbering |
| `recipes/payment-terms-and-fiscal-positions.md` | payment terms, fiscal positions, tax mapping |
| `recipes/bank-and-reconciliation.md` | bank journals, statement lines, matching with invoices and payments, write-offs |
| `recipes/closing-the-period.md` | checks before closing, the year's result, lock dates |
| `recipes/accounting-controls.md` | audit trail, accounting consistency tests, updating tax grids on posted entries |
| `recipes/analytic-accounting.md` | analytic plans, accounts, distribution models and mandatory rules; analytic items and report |
| `recipes/checks-and-debit-notes.md` | paying vendors by printed check (numbering, printing, voiding) and adding debit notes to posted invoices |
| `recipes/invoice-sending.md` | sending invoices by email, download or post, each customer's sending method, product-specific emails |
| `recipes/electronic-invoicing.md` | UBL/CII e-invoice formats per customer, Peppol registration, sending and receiving, uploading e-bills, GLN and tax category codes |
| `recipes/payment-providers.md` | online payment providers (credentials, methods, journal, test to live), paying invoices online, payment links, refunds, manual capture |
| `recipes/products-and-categories.md` | product types, variants, units of measure, categories and their accounts |
| `recipes/inventory-valuation.md` | costing methods, periodic or perpetual valuation, stock accounts, stock closing, landed costs, manufacturing costs and WIP |
| `recipes/partners-and-imports.md` | contacts, companies and people, bulk loads that do not duplicate |
| `recipes/contacts-and-addresses.md` | working schedules and public holidays, extended addresses, geolocation, phone formatting, privacy lookup |
| `recipes/pricelists.md` | pricelists and their rules |
| `recipes/sales-and-crm.md` | from opportunity to quotation, order, delivery and invoice; teams, stages, down payments |
| `recipes/lead-generation.md` | where leads come from: website form, live chat, enrichment, lead mining, website visits, SMS, IAP credits, forwarding to resellers |
| `recipes/loyalty-and-promotions.md` | promotions, discount codes, coupons, buy X get Y, loyalty cards, gift cards and eWallet, on quotations and in the online shop |
| `recipes/sales-margins-and-matrix.md` | variants through the configurator, optional products and the order grid; cost and margin on quotations; product margins |
| `recipes/quotation-builder.md` | richer quotations: PDF quotes with header and footer pages, product sheets, filled form fields |
| `recipes/sales-with-manufacturing-and-purchase.md` | sales that trigger the work behind them: buy or manufacture on order, kits, subcontracted services, projects from opportunities |
| `recipes/memberships.md` | selling memberships and following members, member levels with their pricelist, the public members page |
| `recipes/purchase.md` | from request for quotation to receipt and vendor bill; approval, vendor prices, tenders, blanket orders |
| `recipes/purchase-from-other-flows.md` | buying for manufacturing orders, buying kits and their cost split, agreements used by replenishment |
| `recipes/inventory.md` | warehouses, locations, routes, initial quantities, reordering, batch transfers, scrap |
| `recipes/dropship-and-subcontracting.md` | vendors shipping straight to customers, subcontracted manufacturing, components sent to the subcontractor, its portal |
| `recipes/lots-serials-and-expiry.md` | lots and serial numbers, traceability and recalls, expiration dates, FEFO and expiry alerts, barcode and GS1 nomenclatures |
| `recipes/shipping-and-carriers.md` | delivery methods, weights and packages, tracking references, shipping invoiced with the order, batches by carrier, vehicles and docks |
| `recipes/pickup-in-store.md` | customers who order online and collect (and pay) in a store |
| `recipes/manufacturing.md` | bills of materials, kits, work centers, manufacturing orders, unbuild |
| `recipes/repairs.md` | repair orders: parts added, removed or recycled, quotation and invoice, warranty, repairs from returns and from sales orders |
| `recipes/maintenance.md` | equipment and who uses it, maintenance teams, corrective and preventive requests, calendar, scrapping equipment |
| `recipes/point-of-sale.md` | shops, payment methods, sessions and closing the cash register |
| `recipes/pos-restaurant.md` | restaurant and bar shops: floors and tables, kitchen and bar printers, printing and splitting the bill, tips, courses |
| `recipes/pos-self-order.md` | customers ordering from a QR code or a kiosk, and online payment of POS orders |
| `recipes/pos-features.md` | shop options: global discount, employee login and rights, sale orders and down payments in the POS, stock, event tickets, SMS receipts, session report, loyalty |
| `recipes/pos-hardware.md` | card terminals, QR payment providers, cash machines, receipt and kitchen printers |
| `recipes/website-and-ecommerce.md` | the online shop: publishing products, prices with or without tax, delivery, payment providers, sign-up |
| `recipes/ecommerce-extras.md` | stock shown in the shop, out-of-stock rules, wishlist, product comparison, digital products |
| `recipes/website-content.md` | pages, menus, redirects, blog, forum, profiles, customer references, discussion groups, captcha, address autocomplete |
| `recipes/live-chat.md` | the website chat button, operators, rules, chatbots, canned responses, leads from chats |
| `recipes/events.md` | events, tickets sold on orders or online, attendees, mail schedules, booths, talks, sponsors, quizzes, leads from attendees |
| `recipes/email-and-sms-marketing.md` | mailing lists, email and SMS campaigns, A/B tests, newsletter, tracked links and UTMs, KPI digests, marketing cards |
| `recipes/surveys-and-elearning.md` | surveys, scored quizzes, certifications, live sessions, online courses sold or free |
| `recipes/projects-and-timesheets.md` | projects, tasks, timesheets, services sold by the hour |
| `recipes/project-costs.md` | project costs and profitability: hourly cost, purchases, stock and manufacturing charged to a project |
| `recipes/project-customers.md` | website request form that creates tasks, SMS on stage changes, ratings, customer conversations on the portal |
| `recipes/project-team.md` | personal to-dos, finding tasks by skills, time off and public holidays in timesheets |
| `recipes/employees-and-expenses.md` | employees, time off, expense reports and their accounting |
| `recipes/attendance.md` | check-in and check-out, kiosk, extra hours and their approval, comparison with timesheets |
| `recipes/attendance-variations.md` | time off from extra hours, accrual on worked hours, adjusting the balance by hand, presence and remote work |
| `recipes/recruitment.md` | job positions, applications through the stages, interviews, refusing, hiring, online job pages, skills matching |
| `recipes/skills-and-certifications.md` | employee skills and levels, resumes, courses and certifications from eLearning, Surveys and Events |
| `recipes/contracts-and-work-entries.md` | employment contracts and their versions, contract end and renewal, work entries, org chart |
| `recipes/challenges-and-badges.md` | badges between colleagues, challenges with goals and rewards |
| `recipes/fleet.md` | company vehicles: models, drivers, leasing and insurance contracts, services, odometers, costs and vendor bills |
| `recipes/lunch.md` | employee lunch ordering: vendors, products, reminders, lunch accounts, ordering and receiving |
| `recipes/sequences.md` | document numbering |
| `recipes/email-templates.md` | the emails Odoo sends |
| `recipes/mail-servers.md` | outgoing and incoming mail, aliases |
| `recipes/reports-and-layout.md` | document layout, logo, paper formats |
| `recipes/languages-and-translations.md` | languages, translated terms, date and number formats |
| `recipes/automations.md` | server actions, automation rules, scheduled actions |
| `recipes/calendar-and-sync.md` | meetings, reminders by email or SMS, recurrence, Google and Outlook calendar sync |
| `recipes/dashboards-and-data-cleaning.md` | dashboards and who sees them, rules that archive or delete old records, notes |

## The change note

End with a note the user can keep and repeat in another database (configuration does
not travel on its own):

```markdown
## Change: <what, in business terms>
- Database / company: <db>, <company>
- Changed: <model> <record (XML id or name)>: <field> <old> → <new>
- Created: <model> <name> (<key values>)
- Archived: <model> <name>
- Undo: <how>
- Checked: <what you tried and what happened>
```

## When it needs code

A new model or stored field, a report layout beyond the document layout, an override of
behaviour, an integration, a scheduled job with logic. First offer the closest
configuration (a server action, an automation rule, a filter, a template, a report
parameter). If it still needs code, say what module would do it and why configuration
cannot, and hand over to `odoo-guidelines`.
