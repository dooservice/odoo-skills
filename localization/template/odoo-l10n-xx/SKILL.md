---
name: odoo-l10n-xx
description: >-
  Odoo in <Country>, 16.0 to 20.0: which l10n_xx modules to install, the chart
  of accounts and taxes they bring, how contacts are identified, electronic
  invoicing with <authority>, legal reports, and the mistakes that reach
  production. Use when the database has l10n_xx installed or a company is in
  <Country>, together with odoo-functional.
---

# Odoo in <Country>

<!-- Copy this folder to localization/<country code>/odoo-l10n-<country code>/, rename
     every xx and <Country>, and replace each instruction below with what is true in
     your country. Delete these comments. Every statement about Odoo is checked in the
     source of the version it names; every legal rule cites its official source in
     Sources. -->

What a functional consultant in <Country> needs on top of `odoo-functional`, whose
method and recipes still apply. `versions.md` has what changes between Odoo versions.

## Modules

<!-- Which l10n_xx* modules to install in each version, Community and Enterprise, what each
     adds, and the order. How to check what is installed:
     env['ir.module.module'].search([('name', 'like', 'l10n_xx'), ('state', '=', 'installed')]) -->

## Chart of accounts and taxes

<!-- The chart template code (17.0+) or XML id (16.0), the taxes it brings, the ones that
     are usually missing or need a change, withholdings, and the fiscal positions a
     company here normally uses. -->

## Contacts

<!-- Identification document types and their validation, mandatory fields for customers
     and vendors, address data the authority requires. -->

## Electronic invoicing

<!-- The authority or provider, certificates and credentials, test against production
     mode, the document types, the states a document goes through, and the errors people
     hit with their fix. Say which parts are Enterprise only. -->

## Legal reports

<!-- Books and returns: what Odoo produces, in which module, and what has to be done
     outside Odoo. -->

## Pitfalls

<!-- What breaks in production, each with its symptom, its cause and its fix. -->

## Sources

<!-- The official rules (law, resolution, authority documentation) behind each legal
     statement, and the Odoo source (file:line, version) behind each statement about
     Odoo. -->
