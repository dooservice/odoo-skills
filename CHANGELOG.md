# Changelog

## [1.0.0] — 2026-10-20

The first tagged release.

### Added
- `odoo-functional`, for every version: configuring Odoo without a module the way a
  functional consultant does (understand, read, find the lever, confirm, change through
  the ORM, verify, leave a change note), how to reach the database (agent tools,
  `odoo-bin shell`, XML-RPC, JSON-2 from 19.0), and 18 recipes, from diagnosing "why does
  Odoo do X" to taxes, fiscal positions, products, imports, mail servers and reports.
  Every snippet was run on a real database of 16.0, 17.0, 18.0, 19.0 and 20.0, and every
  difference between versions they name is checked against each branch's source. They
  name no country.
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
