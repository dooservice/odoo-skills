# Changelog

## [1.1.1] - 2026-10-30

Small models now get the version right: Claude Haiku 5.5 goes from 71% to 100% on Odoo
20.0, and reaches 97% to 100% on every version.

### Changed
- The descriptions of `odoo-guidelines` and `odoo-web-guidelines` tell the agent to read
  the skill before writing any file, and carry the names that change most in that
  version (`ir.access`, `group_ids`, `models.Constraint`, `Domain`, `<list>`, Owl 3...).
  A diagnosis showed that on code tasks agents did not load the skills and wrote from
  memory; the description is the one part they always see.
- The description of `odoo-reference` carries the business names that change most in its
  version (tax fields on sale lines, fiscal position mapping, time off types, pricelist
  rules, expense reports, bank journals, scrap...).

### Fixed
- `evals/`: the JavaScript test tasks of 16.0 to 18.0 describe the widget under test, so a
  model writes the test instead of searching an empty project for it until its turns run
  out. The graders are unchanged.

## [1.1.0] - 2026-10-29

Complete for Odoo's standard flows: every Community module and every framework feature of
16.0 to 20.0 is covered, and a tool checks it against each version's source.

### Added
- Developer guidelines for every framework feature of each version, each statement
  checked in that version's source: models and inheritance (`models.md`), every field
  type and its attributes (`fields.md`), every `api` decorator (`api.md`), every public
  ORM method (`orm.md`), every view type (`views.md`), every action type, menus and
  scheduled actions (`actions.md`), route types and `auth` values, the external API
  (XML-RPC, JSON-RPC, JSON-2) and API keys, mail and the chatter, multi-company, access
  rights and record rules, QWeb PDF reports, data files, migrations and hooks,
  translations, tests and `odoo-bin`. About 30,000 words per version, against about
  4,800 in Odoo's own 20.0 skills.
- Web client guidelines for each version: Owl (Owl 3 in 20.0), every web client registry,
  services, field widgets and `js_class` views, website and portal code (`publicWidget`
  and Interactions), the Point of Sale, assets bundles and JavaScript tests and tours.
- From Odoo's own skills: `stable.md` (changes to a module version already installed) and
  both `AUTHORING.md`; `odoo-git` and `odoo-review` brought up to date with Odoo's latest
  rules.
- 44 functional recipes, so that every Community app and module of each version has its
  flow: analytic accounting, checks and debit notes, invoice sending, electronic
  invoicing, payment providers, inventory valuation, accounting controls, lead generation,
  loyalty and promotions, margins and product grids, quotation builder, make to order,
  memberships, dropship and subcontracting, lots and expiry, shipping, pickup in store,
  repairs, maintenance, purchases from other flows, Point of Sale restaurant, self
  ordering, shop options and hardware, attendance, recruitment, skills, contracts and
  work entries, badges, project costs, customers and team, fleet, lunch, events, email
  and SMS marketing, surveys and eLearning, live chat, website content, shop extras,
  calendar, authentication and security, dashboards and data cleaning, contacts and
  addresses. Every name they use is checked in each version's source.
- `tools/build_coverage.py` and `COVERAGE.md`: every Community module and framework
  feature of each version, read from its source, and the recipe or guideline that covers
  it. Nothing is missing in any version.
- `tools/upstream.py`: lists Odoo's commits to its own skills since the one ours follow.
- `evals/`: suites for 17.0, 18.0 and 19.0, so all five versions are measured.

### Changed
- Every code block in a recipe is for one range of versions, newest first, with no other
  version's names in comments: models copied the old line.
- Skill descriptions name the business objects and code they cover, so agents load them;
  `odoo-reference` sends business flows to `odoo-functional`.
- `odoo-reference` regenerated from the latest 19.0 and 20.0 source.

### Fixed
- 20.0: `type='json'` routes are a deprecated alias, not gone; `--unsafe-policy` exists;
  Owl 3 has no `useState`; `ir.config_parameter` has `get_int` and `get_str`, not
  `get_param`. 16.0: `patch` uses `this._super`. 16.0 and 17.0: imported test classes
  are collected.

### Removed
- Localizations: `odoo-l10n-pe`, the country template and the `l10n_*` modules of the
  reference. Each country needs accountants of that country to keep it right as its law
  changes; the skills cover Odoo's standard flows only.

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
