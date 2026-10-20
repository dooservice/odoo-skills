# Changelog

## [1.0.0] — 2026-10-20

The first tagged release.

### Added
- `odoo-functional`, for every version: configuring Odoo without a module the way a
  functional consultant does (understand, read, find the lever, confirm, change through
  the ORM, verify, leave a change note), how to reach the database (agent tools,
  `odoo-bin shell`, XML-RPC, JSON-2 from 19.0), and 18 recipes, from diagnosing "why does
  Odoo do X" to taxes, fiscal positions, products, imports, mail servers and reports.
  Every difference between versions they name is checked against each branch's source.
- Install in one step: a Claude Code marketplace with one plugin per version (`odoo-16`
  to `odoo-20`), `npx skills add`, or `install.sh`, which reads the version from the
  project's `__manifest__.py`.
- A check on every push: each skill against the Agent Skills format, and the marketplace
  with `claude plugin validate`.

### Removed
- `dooservice/`: the dooservice console's own skill moved to the console's image, so this
  repository holds only what works with any Odoo.
