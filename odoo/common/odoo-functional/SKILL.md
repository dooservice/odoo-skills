---
name: odoo-functional
description: >-
  Configuring and fixing an Odoo database without writing a module, the way a
  functional consultant does, in the interface or with an `odoo-bin shell`
  script: companies and the chart of accounts, users and user groups, access
  and record rules, contacts (customer companies and their contact persons),
  products and units of measure, pricelists and discounts, taxes, bank and
  other journals, payment terms, fiscal positions and tax mapping, bank
  reconciliation and reconciliation models, sales, purchase, inventory and
  scrap, manufacturing, point of sale, employees, time off types and
  allocations, expenses and expense reports, sequences, email templates and
  mail servers, reports, automation rules, server and scheduled actions,
  imports, and diagnosing "why does Odoo do X". Use for any task that
  creates, reads or changes records or settings of an Odoo database (shell
  script, external API or an agent's tools) and for any functional question,
  before deciding that something needs code.
---

# Configuring Odoo without code

Most requests are configuration: data changed through the ORM, no module. This
page is enough to work; open `method.md` only when a step is unclear.

## The method

1. Understand the request in business terms; ask if ambiguous.
2. Read the current state; never change what you did not read.
3. Find the lever in `odoo-reference` for this version, not from memory.
4. Read the matching recipe; copy the code block of this version.
5. Propose the change, its records and its undo; wait for the yes.
6. Change through the ORM, smallest step; archive, never delete.
7. Verify: read again, try it as the user.
8. End with a change note: what changed, how to undo, what you checked.
9. Country rules (`l10n_*`) are not covered: say so, ask the user.
10. Needs code: offer the closest configuration, then `odoo-guidelines`.

Reach the database with the environment's ORM tools, else `odoo-bin shell -d <db>
< script.py` (`env` ready, end with `env.cr.commit()`), else the external API; SQL
only to read. `connect.md`: the API, dry runs, acting as a user.

## Rules that save databases

- One version (`odoo.release.series`): no fallbacks, no other version's names.
- Records are shared: count the users first.
- Posted accounting: create new, archive old.
- Settings: `res.config.settings` then `execute()`.
- `env.ref()` over names; read `company_id`, use `with_company()`;
  `with_context(lang=...)` per language.
- Module updates may restore standard data; test copies send nothing.

## Recipes

In `recipes/`, `.md` left out:

Accounting
- `taxes-and-journals`, invoice numbering
- `payment-terms-and-fiscal-positions`
- `currencies-and-rates`
- `bank-and-reconciliation`
- `closing-the-period`, lock dates
- `accounting-controls`: audit trail
- `analytic-accounting`
- `checks-and-debit-notes`
- `invoice-sending`
- `electronic-invoicing`: Peppol
- `payment-providers`, payment links

Sales and CRM
- `sales-and-crm`
- `pricelists`
- `lead-generation`
- `loyalty-and-promotions`: coupons, gift cards
- `sales-margins-and-matrix`
- `quotation-builder`
- `sales-with-manufacturing-and-purchase`
- `memberships`

Purchase
- `purchase`: tenders, blanket orders
- `purchase-from-other-flows`

Inventory and manufacturing
- `products-and-categories`, units of measure
- `inventory`: routes, reordering, scrap
- `inventory-valuation`, landed costs
- `lots-serials-and-expiry`
- `shipping-and-carriers`
- `dropship-and-subcontracting`
- `manufacturing`
- `repairs`
- `maintenance`

Point of Sale
- `point-of-sale`
- `pos-features`
- `pos-hardware`
- `pos-restaurant`
- `pos-self-order`
- `pickup-in-store`

Website and marketing
- `website-and-ecommerce`
- `ecommerce-extras`
- `website-content`: blog, forum
- `live-chat`
- `events`
- `email-and-sms-marketing`
- `surveys-and-elearning`

Projects and HR
- `projects-and-timesheets`
- `project-costs`
- `project-customers`
- `project-team`
- `employees-and-expenses`, time off
- `attendance`: extra hours
- `attendance-variations`: presence, remote work
- `recruitment`
- `skills-and-certifications`
- `contracts-and-work-entries`
- `challenges-and-badges`
- `fleet`
- `lunch`

Settings and security
- `go-live`: a new company
- `companies`, chart of accounts
- `users-and-access`, record rules
- `authentication-and-security`
- `partners-and-imports`
- `contacts-and-addresses`
- `sequences`
- `email-templates`
- `mail-servers`
- `reports-and-layout`
- `languages-and-translations`
- `automations`
- `calendar-and-sync`
- `dashboards-and-data-cleaning`

Diagnosis
- `diagnosis`: why Odoo does X
