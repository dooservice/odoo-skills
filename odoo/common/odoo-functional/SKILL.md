---
name: odoo-functional
description: >-
  Configuring and fixing an Odoo database without writing a module, the way a
  functional consultant does: settings, companies, users and access, products,
  partners, taxes, journals, fiscal positions, pricelists, sequences, email
  templates, reports, automations, imports, and diagnosing "why does Odoo do
  X". Use for any configuration, data fix or functional question, before
  deciding that something needs code.
---

# Configuring Odoo without code

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

## Recipes

Read the matching one before starting. Each names what differs between versions.

| Recipe | Covers |
|---|---|
| `recipes/diagnosis.md` | "why does Odoo do X": access errors, missing taxes, wrong prices, hidden records, silent automations |
| `recipes/companies.md` | companies, multi-company, the chart of accounts |
| `recipes/users-and-access.md` | users, groups, record rules, portal users |
| `recipes/currencies-and-rates.md` | currencies, rates, multi-currency |
| `recipes/taxes-and-journals.md` | taxes, journals, invoice numbering |
| `recipes/payment-terms-and-fiscal-positions.md` | payment terms, fiscal positions, tax mapping |
| `recipes/products-and-categories.md` | product types, variants, units of measure, categories and their accounts |
| `recipes/partners-and-imports.md` | contacts, companies and people, bulk loads that do not duplicate |
| `recipes/pricelists.md` | pricelists and their rules |
| `recipes/sales-and-crm.md` | sales teams, CRM stages, quotation settings |
| `recipes/purchase.md` | purchase approval, receipts, vendor bills, vendor prices |
| `recipes/inventory.md` | warehouses, locations, routes, initial quantities, reordering |
| `recipes/sequences.md` | document numbering |
| `recipes/email-templates.md` | the emails Odoo sends |
| `recipes/mail-servers.md` | outgoing and incoming mail, aliases |
| `recipes/reports-and-layout.md` | document layout, logo, paper formats |
| `recipes/languages-and-translations.md` | languages, translated terms, date and number formats |
| `recipes/automations.md` | server actions, automation rules, scheduled actions |

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
