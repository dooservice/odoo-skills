# Changelog

## [1.0.0] — 2026-10-20

The first tagged release.

### Added
- `odoo-functional`, for every version: configuring Odoo without a module the way a
  functional consultant does (understand, read, find the lever, confirm, change through
  the ORM, verify, leave a change note), how to reach the database (agent tools,
  `odoo-bin shell`, XML-RPC, JSON-2 from 19.0), and 26 recipes. Each one follows Odoo's
  own flow as its documentation describes it for that version, step by step with the
  menu of that version, the ORM equivalent and the state it leaves, in the same parts:
  before you start, the standard flow, variations, versions, verify, pitfalls. They cover
  go-live, sales and CRM, purchase (tenders and blanket orders included), inventory
  (batch transfers and scrap included), manufacturing, point of sale, website and
  eCommerce, projects and timesheets, employees and expenses, companies, users and access,
  currencies, taxes and journals, payment terms and fiscal positions, bank reconciliation,
  closing the period, products, partners and imports, pricelists, sequences, email
  templates, mail servers, reports, languages, automations, and diagnosing "why does
  Odoo do X". Every snippet was run on a real database of 16.0, 17.0, 18.0, 19.0 and 20.0,
  its effect read back; they name no country.
- `odoo-l10n-pe`, the first localization: modules per version, the PCGE chart and the
  taxes it brings, identification, documents and series, detracciones, retenciones and
  percepciones, electronic invoicing with SUNAT and legal reports (PLE, SIRE). Every legal
  rule cites its official source; every Odoo statement was run on a Peruvian database of
  each version.
- `evals/`: tasks on Odoo 16.0 and 20.0 that measure what the skills change, run with and
  without them.
- Localizations: one skill per country, `odoo-l10n-<country code>`, from a template with
  the sections every country fills in, and a guide to add yours. `odoo-functional` loads
  the one of each `l10n_*` the database has installed.
- Install in one step: a Claude Code marketplace with one plugin per version (`odoo-16`
  to `odoo-20`) and per country, `npx skills add`, or `install.sh`, which reads the
  version and the countries from the project's `__manifest__.py` files.
- A check on every push: each skill against the Agent Skills format, each localization
  complete, the marketplace in line with the folders (`claude plugin validate`), and the
  generators through the linter.

### Changed
- The guideline skills are built from Markdown templates, one per file, with a small
  class each for what differs between versions; the output is the same as before.
- The reference no longer shows a target on a field that is not relational. Checked
  against a running Odoo of each version: every model, field, XML id and Settings field
  it lists matches.

### Removed
- `dooservice/`: the dooservice console's own skill moved to the console's image, so this
  repository holds only what works with any Odoo.
