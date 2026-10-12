"""Builds odoo/<version>/ from Odoo's 20.0 skills, adapted per version.

Usage: python3 generate.py <odoo 20.0 skills directory> <this repository>

Every version-specific statement below was checked against the source of that branch.
"""

import pathlib
import shutil
import sys

UPSTREAM = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
VERSIONS = (16, 17, 18, 19, 20)


def pick(v, **by):
    """The value for version `v`: keys are `v16` (one), `v17_18` (a range) or `v19_` (from)."""
    for key, value in by.items():
        spec = key[1:]
        if spec.endswith("_"):
            if v >= int(spec[:-1]):
                return value
        elif "_" in spec:
            lo, hi = spec.split("_")
            if int(lo) <= v <= int(hi):
                return value
        elif v == int(spec):
            return value
    raise KeyError((v, by))


def tr(v):
    """The translation call in model code."""
    return "self.env._" if v >= 18 else "_"


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = text.strip("\n") + "\n"
    for bad in ("—", "–", "“", "”", "‘", "’", "…"):
        if bad in text and path.name != "comments.md":
            raise SystemExit(f"non-ASCII punctuation {bad!r} in {path}")
    path.write_text(text)


def version_md(v):
    rows = [
        ("Python", pick(v, v16="3.7 or newer", v17_19="3.10 or newer", v20="3.12 or newer")),
        ("View modifiers", pick(
            v,
            v16="`attrs=\"{'invisible': [('state', '!=', 'draft')]}\"` and `states=\"draft,sent\"`",
            v17_="Python expressions on the attribute itself: `invisible=\"state != 'draft'\"`, "
                 "`readonly=`, `required=`, `column_invisible=`. `attrs` and `states` are refused "
                 "with a ValidationError",
        )),
        ("List view", pick(
            v,
            v16_17="`<tree>`, view_mode `tree`, xml id `<model>_view_tree`",
            v18_="`<list>`, view_mode `list`, xml id `<model>_view_list`. `<tree>` and `tree` are gone",
        )),
        ("Chatter", pick(
            v,
            v16_17="`<div class=\"oe_chatter\">` with `message_follower_ids`, `activity_ids`, `message_ids`",
            v18_="`<chatter/>` at the end of the form",
        )),
        ("Record display name", pick(
            v,
            v16="override `name_get()` (returns `[(id, name)]`)",
            v17="override `_compute_display_name` (with `@api.depends`); `name_get` is deprecated and no longer builds it",
            v18_="override `_compute_display_name`; `name_get` does not exist",
        )),
        ("Grouped reads", pick(
            v,
            v16="`read_group(domain, fields, groupby, lazy=...)`, returns dicts",
            v17_18="`_read_group(domain, groupby, aggregates)`, returns tuples; "
                   "`read_group` stays for the web client",
            v19="`_read_group(domain, groupby, aggregates)`, returns tuples; `read_group` is deprecated",
            v20="`read_group(domain, groupby, aggregates)` and `_read_group`, both return tuples",
        )),
        ("Field aggregation", pick(
            v,
            v16_17="`group_operator='sum'`",
            v18_19="`aggregator='sum'` (`group_operator` is a deprecated alias)",
            v20="`aggregator='sum'`",
        )),
        ("SQL constraints and indexes", pick(
            v,
            v16_18="`_sql_constraints = [(name, definition, message)]`; indexes with `index=True` "
                   "or `index='btree_not_null'`/`'trigram'`",
            v19_="model attributes `_x_check = models.Constraint(\"CHECK (...)\", \"msg\")`, "
                 "`models.Index(...)`, `models.UniqueIndex(...)`; `_sql_constraints` is ignored "
                 "with a warning",
        )),
        ("Domains", pick(
            v,
            v16_18="lists; combine with `odoo.osv.expression.AND([...])` / `OR([...])`",
            v19_="`from odoo.fields import Domain`; `Domain(...) & Domain(...)`, `Domain.AND/OR`",
        )),
        ("Translations in Python", pick(
            v,
            v16_17="`from odoo import _, _lt`; `_(\"...\")`, `_lt` for module-level constants",
            v18_="`self.env._(\"...\")`; `_lt = LazyTranslate(__name__)` for module-level constants; "
                 "bare `_` still works",
        )),
        ("Group categories", pick(
            v,
            v16_18="`category_id` on `res.groups` (an `ir.module.category`)",
            v19_="`privilege_id` on `res.groups` (a `res.groups.privilege`)",
        )),
        ("Access rights", pick(
            v,
            v16_19="`security/ir.model.access.csv` plus `ir.rule` records",
            v20="`security/ir.access.csv` (`ir.access`, one model for ACLs and record rules)",
        )),
        ("Route types", pick(
            v,
            v16_18="`type='http'` or `type='json'`",
            v19="`'http'`, `'jsonrpc'` (`'json'` is a deprecated alias), `'json2'`",
            v20="`'http'`, `'jsonrpc'`, `'json2'`",
        )),
        ("Route auth", pick(v, v16_17="`user`, `public`, `none`", v18_="`user`, `public`, `none`, `bearer`")),
        ("Default test tags", pick(
            v,
            v16_19="`at_install`: write `@tagged('post_install', '-at_install')` on business tests",
            v20="`post_install`",
        )),
        ("QWeb output", pick(
            v,
            v16_19="`t-out`; `t-esc` still works, `t-raw` logs a deprecation warning",
            v20="`t-out` only; `t-esc` and `t-raw` are gone from server QWeb",
        )),
        ("Owl", pick(v, v16_19="Owl 2", v20="Owl 3 (`signal`, `computed`)")),
        ("JS module header", pick(
            v,
            v16_17="every file under `static/src` starts with `/** @odoo-module **/`",
            v18_="none needed",
        )),
        ("JS patch", pick(
            v,
            v16="`patch(Target.prototype, \"module.name\", { ... })`",
            v17_="`patch(Target.prototype, { ... })`",
        )),
        ("JS field registry", pick(
            v,
            v16="`registry.category(\"fields\").add(\"x\", MyField)`, the component itself",
            v17_="`registry.category(\"fields\").add(\"x\", { component: MyField, ... })`",
        )),
        ("JS RPC", pick(
            v,
            v16_17="`this.rpc = useService(\"rpc\")`; `this.orm = useService(\"orm\")`",
            v18_="`import { rpc } from \"@web/core/network/rpc\"`; `useService(\"orm\")`",
        )),
        ("JS tests", pick(
            v,
            v16_17="QUnit, under `static/tests/`, in the `web.qunit_suite_tests` bundle",
            v18="hoot (`@odoo/hoot`), `*.test.js` in `web.assets_unit_tests`; QUnit only for legacy suites",
            v19_="hoot (`@odoo/hoot`), `*.test.js` in `web.assets_unit_tests`",
        )),
    ]
    table = "\n".join(f"| {name} | {value} |" for name, value in rows)
    return f"""
# What Odoo {v}.0 has

These skills are for Odoo {v}.0 and only {v}.0. Write for it: an API from another version
fails at install or, worse, silently does nothing. Each row was checked against the
{v}.0 source.

| Topic | In {v}.0 |
| --- | --- |
{table}

## When unsure

Confirm against the installed source rather than memory:
`grep -rn "<name>" "$(python3 -c 'import odoo, os; print(os.path.dirname(odoo.__file__))')"`
(the framework and the standard modules are there). A usage in a standard module of the same version is the
best example to follow.
"""


def guidelines_skill(v):
    rows = [
        ("What Odoo {v}.0 has", "guidelines/version.md#what-odoo-{v}0-has", "before writing any API, view attribute or JS import you are not sure exists in this version"),
        ("Module structure and file naming", "guidelines/module_structure.md#module-structure-and-file-naming", "creating or moving files in an addon, or adding a module"),
        ("Manifest", "guidelines/manifest.md#manifest", "touching `__manifest__.py`"),
        ("Imports", "guidelines/python.md#imports", "writing Python anywhere in an addon"),
        ("Naming and model layout", "guidelines/python.md#naming-and-model-layout", "naming a model, field, method or variable; laying out a model class"),
        ("Translate only static literals", "guidelines/python.md#translate-only-static-literals", "user-facing strings in Python"),
        ("Recordsets, domains and context", "guidelines/orm.md#recordsets-domains-and-context", "reading records, building domains, passing context"),
        ("Computes, onchange and constraints", "guidelines/orm.md#computes-onchange-and-constraints", "computes, onchange, constraints, indexes, `create` overrides"),
        ("Methods and extension points", "guidelines/orm.md#methods-and-extension-points", "adding a model method, or one another module will override"),
        ("Transactions and exceptions", "guidelines/orm.md#transactions-and-exceptions", "cursors, commits, savepoints, `try`/`except`"),
        ("Fields", "guidelines/fields.md#fields", "declaring or modifying field definitions"),
        ("Controllers", "guidelines/controllers.md#controllers", "touching `controllers/` or `@route`"),
        ("Views, actions and data records", "guidelines/xml.md#views-actions-and-data-records", "touching `views/`, `data/`, or any XML records"),
        ("Anchor view inheritance on names, never on position", "guidelines/xml.md#anchor-view-inheritance-on-names-never-on-position", "extending or overriding an existing view"),
        ("QWeb PDF reports", "guidelines/reports.md#qweb-pdf-reports", "report templates or `_get_report_values`"),
        ("Access rights", "guidelines/security.md#access-rights", "touching `security/` (access rows, record rules, groups)"),
        ("Batch ORM calls", "guidelines/performance.md#batch-orm-calls", "ORM calls (`create`/`search*`/aggregates) inside a loop"),
        ("Performance conventions", "guidelines/performance.md#performance-conventions", "code that loops over records or filters query results"),
        ("Tests", "guidelines/tests.md#tests", "touching `tests/`"),
        ("Plain ASCII punctuation in comments and messages", "guidelines/comments.md#plain-ascii-punctuation-in-comments-and-messages", "writing a comment, a docstring, a user-facing string, or a commit message"),
        ("Changes to an installed module", "guidelines/installed.md#changes-to-an-installed-module", "changing a module that is already installed in a database that matters"),
    ]
    table = "\n".join(f"| [{t.format(v=v)}]({link.format(v=v)}) | {when} |" for t, link, when in rows)
    return f"""
---
name: odoo-guidelines
description: >-
  House rules for Odoo {v}.0 addon code: module structure, manifest, Python/ORM,
  fields, controllers, XML views and data, QWeb reports, access rights and
  record rules, performance, tests, and what exists in {v}.0. Use when writing or
  reviewing any file in an Odoo addon outside static/ (for the JavaScript, Owl
  templates and SCSS under static/, see odoo-web-guidelines).
---

# Odoo {v}.0 addon guidelines

House rules for code in Odoo {v}.0 addons. Everything an addon ships under `static/`
has its own skill: `odoo-web-guidelines`.

Guidelines are grouped by domain, one file per domain in `guidelines/`, one section per
guideline. No rule outranks another. Read the sections that match the files you are
touching instead of loading whole files. The version table comes first whenever an API
is in doubt: these rules are written for {v}.0 and the table says what {v}.0 has.

| Guideline | Read it when |
| --- | --- |
{table}

Adapted from Odoo's own skill library (odoo/odoo, branch 20.0, `skills/`, LGPL-3) and
checked against the {v}.0 source.
"""


def comments_md(v):
    call = tr(v)
    return f"""
# Plain ASCII punctuation in comments and messages

Write code comments, docstrings, user-facing strings and commit messages with
ASCII punctuation only. The character that keeps showing up is the em dash
(`—`): replace it with a comma, a colon, a semicolon, parentheses, or two
sentences, whichever the sentence actually needs. Same for the en dash (`–`),
curly quotes (`“ ” ‘ ’`) and the ellipsis character (`…`): write `-`, `"`, `'`
and `...`.

```python
# bad
# recompute the totals — the taxes may have changed
raise UserError({call}("Book %s is already borrowed — return it first", book.name))

# good
# recompute the totals: the taxes may have changed
raise UserError({call}("Book %s is already borrowed, return it first", book.name))
```

## Why

- The em dash is not on the keyboard layouts code is written with, so in practice it
  arrives by copy-paste or from a generation tool. A diff full of them reads as text
  nobody typed.
- ASCII punctuation is greppable and diffable. A comment or a commit message is
  searched for with what a reviewer can type.
- A translatable literal is keyed on its exact source string, so two variants of the
  same sentence that differ only in the dash are two terms to translate (see
  [Translate only static literals](python.md#translate-only-static-literals)).

## Exceptions

- Data, not prose: a test fixture, a localization file, or a string whose content is
  the character itself.
- Existing translatable text in an installed module: rewording a term breaks its
  translations (see [Changes to an installed module](installed.md#changes-to-an-installed-module)).
"""


def controllers_md(v):
    auth = pick(v, v16_17="`user`, `public`, or `none`", v18_="`user`, `bearer`, `public`, or `none`")
    types = pick(
        v,
        v16_18="Route `type` is `'http'` or `'json'` (JSON-RPC).",
        v19="Route `type` is `'http'`, `'jsonrpc'`, or `'json2'`; `type='json'` is a deprecated alias of `'jsonrpc'`.",
        v20="Route `type` is `'http'`, `'jsonrpc'`, or `'json2'`; `type='json'` is gone.",
    )
    bearer = "" if v < 18 else " `auth='bearer'` authenticates with an API key in the `Authorization` header."
    return f"""
# Controllers

- Routes are methods decorated with `@route` on a `http.Controller` subclass.
  Always re-decorate an **override** with `@route` (an undecorated override is
  not exposed reliably). An empty `@route()` keeps the parent's arguments and
  any argument overrides the parent's, except `type`, which an override can
  never change.
- Set the right `auth` on each route ({auth}): a `public` route must not expose
  internal data or perform privileged writes (see the `odoo-security` skill).{bearer}
- {types}
- Keep controllers thin: parse and check the request, then call a model method
  that does the work. Models never read `odoo.http.request`.
"""


def fields_md(v):
    agg = pick(v, v16_17="`group_operator=`", v18_="`aggregator=`")
    idx = pick(
        v,
        v16_18="multi-column or custom indexes are created in `init()` with "
               "`tools.create_index(self.env.cr, ...)`",
        v19_="multi-column or custom indexes are model attributes (`_x_idx = models.Index(\"(a, b)\")`, "
             "`models.UniqueIndex`; the attribute name must start with `_`)",
    )
    return f"""
# Fields

- Relational suffixes: `Many2one` -> `_id`, `One2many`/`Many2many` -> `_ids`.
- `index=True` on fields that are both searched and selective (many distinct
  values). An index on a low-cardinality field (a boolean, a state) is wasted
  space and slows every write. `index` also accepts a type (`'btree_not_null'`,
  `'trigram'` for `like` searches); {idx}.
- How a numeric field sums in grouped views is {agg} (`'sum'`, `'avg'`, `'max'`,
  `'min'`, `False` to show nothing).
- Restrict sensitive fields with the `groups` attribute (comma-separated external
  ids); restricted fields are dropped from views and `fields_get`, and raise on
  direct read/write.
- Check relational definitions: correct `comodel_name`, sensible `ondelete`,
  `required`, and a currency companion for monetary fields.
- Use **reserved** fields for their built-in behavior rather than reinventing
  them: `active` for archiving (via `action_archive`, not a custom boolean),
  `state` for lifecycle, `parent_id` + `parent_path` (`index=True`, with
  `_parent_store`) for trees, `company_id` for multi-company (consistency via
  `_check_company_auto = True` and `check_company=True` on the relations).
- A field and a method can't share a name (same namespace); flag collisions.
- `related` fields can't chain `One2many`/`Many2many` in the dependency path:
  the ORM does not reject it, it *silently truncates each x2many hop to its
  first record* and returns wrong data; reach the target through a `Many2one`
  (ending the chain on an x2many is fine). Reusing one compute for several
  fields is fine; reusing one **inverse** is discouraged: while the inverse
  runs, every field sharing it reads as `False` when not cached.
- A new stored field on a model with many records: give it a `compute` or a
  `default` that the database can fill in one statement, or the module update
  computes it row by row.
"""


def manifest_md(v):
    return f"""
# Manifest

- `name` is required. `version` is `{v}.0.x.y.z` (the Odoo series, then the
  module's own major.minor.patch): migration scripts run by comparing it, so bump
  it whenever a change needs one (see the `odoo-upgrade` skill).
- `depends` lists every module whose features or resources are used, direct
  dependencies only. Don't list `base` when another dependency already brings it.
- `data` files are always installed/updated; `demo` files load only in demo
  mode. Keep load order correct (a record's dependencies first: groups, then
  access rows, then views, then menus).
- `license` defaults to `LGPL-3`; set it deliberately (`OPL-1` for proprietary
  modules sold on the Odoo apps store, `LGPL-3` or `AGPL-3` otherwise).
- `auto_install` is only for "link" modules (installed automatically when their
  dependencies are); it can also be a *subset* of `depends` that triggers the
  auto-install.
- `application` is `True` only for full apps, not technical modules.
- Declare non-Odoo requirements in `external_dependencies` (`python`/`bin`), and
  add the Python ones to the repository's `requirements.txt`, which deployments
  install.
- `assets` declares how static files load into bundles (don't register assets
  ad-hoc elsewhere).
"""


def module_structure_md(v):
    access = pick(
        v,
        v16_19="Security files: access rows in `security/ir.model.access.csv`; groups and record\n  rules in `security/<module>_security.xml`.",
        v20="Security files: access rows in `security/ir.access.csv`; groups and other\n  security records in `security/<module>_security.xml`.",
    )
    return f"""
# Module structure and file naming

- Standard directories: `models/`, `views/`, `controllers/`, `data/`,
  `security/`, `static/`, and optional `wizard/`, `report/`, `tests/`,
  `migrations/`.
- One model class per file, named after the model with dots as underscores
  (`res_partner.py`), whether the class defines a new model or extends an
  existing one with `_inherit`.
- Suffix conventions: backend views `*_views.xml`, portal/QWeb pages
  `*_templates.xml`, menus optional `*_menus.xml`, data `*_data.xml`, demo
  `*_demo.xml`, wizards `<transient>.py` + `<transient>_views.xml`.
- {access}
- Controllers: feature-named files, or `<inherited_module>.py` when extending
  another module's controller (e.g. `portal.py`).
- Reports: a statistics (SQL-view) report is `<model>_report.py` +
  `<model>_report_views.xml`; a printable report splits `<model>_reports.xml`
  (report actions, paperformat) from `<model>_templates.xml` (QWeb templates).
- File and directory names are Python identifiers: lowercase, `[a-z0-9_]`. The
  module's directory name is its technical name; prefix custom modules with the
  customer or company code so they never collide with a standard one.
"""


def orm_md(v):
    domains = pick(
        v,
        v16_18="- Combine domains with `odoo.osv.expression.AND([...])` / `OR([...])`; never\n"
               "  hand-build `'&'`/`'|'` prefix-notation lists.",
        v19_="- Combine domains with `odoo.fields.Domain`: the `&`, `|`, `~` operators for\n"
             "  domains written inline, `Domain.AND`/`Domain.OR` for a list of domains you\n"
             "  already hold. Never hand-build `'&'`/`'|'` prefix-notation lists.",
    )
    grouped = "`filtered`, `grouped`, `mapped`, `sorted`" if v >= 17 else "`filtered`, `mapped`, `sorted`"
    constraints = pick(
        v,
        v16_18="enforce invariants with `@api.constrains` or `_sql_constraints = [(name,\n"
               "  definition, message)]`.",
        v19_="enforce invariants with `@api.constrains` or SQL constraints declared as model\n"
             "  attributes (`_x_check = models.Constraint(\"CHECK (...)\", \"msg\")`; the\n"
             "  attribute name must start with `_`). Indexes are declared the same way\n"
             "  (`_x_index = models.Index(...)`, `models.UniqueIndex(...)`). `_sql_constraints`\n"
             "  is **ignored** with a log warning in this version: the constraint is never created.",
    )
    display = pick(
        v,
        v16="- The display name comes from `name_get()`; override it returning `[(id, name)]`.",
        v17_="- The display name comes from `_compute_display_name`; override it with\n"
             "  `@api.depends` on what it reads, never `name_get`.",
    )
    return f"""
# Recordsets, domains and context

- Use recordset methods ({grouped}) where they read better than a loop.
- Recordsets/collections are booleans: write `if records:` / `if some_list:`,
  not `if len(...)`.
- Don't read a non-relational field on a multi-record set (it raises); iterate
  or `mapped`. Conversely, guard single-record assumptions with `ensure_one()`.
{domains}
- Propagate context with `with_context(...)` (it's a frozendict, immutable);
  name custom context keys carefully and prefix module-specific ones (a stray
  `default_<field>` in context leaks into unrelated `create` calls).
- Delegation inheritance (`_inherits`) inherits fields but **not** methods; avoid
  it where you can.

# Computes, onchange and constraints

- `create` must accept a list of vals (`@api.model_create_multi`); don't call
  `create` per record in a loop (see [Batch ORM calls](performance.md#batch-orm-calls)).
- `@api.depends` must list **every** field the compute reads; stored computes
  need correct dependencies and no side effects.
- `@api.onchange` is UI-only: never rely on it for data integrity; {constraints}
{display}

# Methods and extension points

- Methods are private (`_` prefix) by default. A public name is an RPC entry
  point: make one only when it must be callable from outside, and decorate
  with `@api.private` a public name that must not be exposed.
- Logic that another module actually overrides goes in its own small method
  (`self._get_partner_domain()`); other modules extend methods, not lines.
  Don't pre-split for extension points that don't exist yet.
- An override calls `super()` and passes its arguments through unchanged;
  never copy the parent's body.
- Don't use `odoo.http.request` in models: it is absent in crons, RPC, tests
  and the shell. Pass what the model needs in from the controller.

# Transactions and exceptions

- **Never** call `cr.commit()` / `cr.rollback()` unless you opened your own
  cursor; the framework owns the transaction. Any unavoidable commit needs an
  explicit comment justifying it.
- Catch **specific** exceptions over the smallest possible block; let unexpected
  ones propagate to the framework. To recover from framework exceptions, wrap the
  work in `with self.env.cr.savepoint():` (more than 64 savepoints in one
  transaction degrades PostgreSQL, so bound batch sizes).
- Errors for the user are `UserError` / `ValidationError` / `AccessError` with a
  translated message; never a bare `Exception`.
"""


def performance_md(v):
    if v == 16:
        group = """```python
# bad: one aggregate query per author
for author in authors:
    author.book_count = Book.search_count([('author_id', '=', author.id)])

# good: one grouped query, then a dict lookup
groups = Book.read_group([('author_id', 'in', authors.ids)], ['author_id'], ['author_id'])
counts = {group['author_id'][0]: group['author_id_count'] for group in groups}
for author in authors:
    author.book_count = counts.get(author.id, 0)
```"""
        calls = "`search`, `search_count`, `read_group` and `create`"
    else:
        group = """```python
# bad: one aggregate query per author
for author in authors:
    author.book_count = Book.search_count([('author_id', '=', author.id)])

# good: one grouped query, then a dict lookup
counts = {
    author.id: count
    for author, count in Book._read_group(
        [('author_id', 'in', authors.ids)], ['author_id'], ['__count'],
    )
}
for author in authors:
    author.book_count = counts.get(author.id, 0)
```"""
        calls = "`search`, `search_count`, `_read_group` and `create`"
    return f"""
# Batch ORM calls

Make **one** ORM call for the whole collection; an ORM call inside a
`for` loop over records or vals is a query per iteration. This covers
{calls} alike.

```python
# bad: one INSERT round-trip per record
for vals in vals_list:
    self.env['library.book'].create(vals)

# good: one batched create (and decorate overrides with @api.model_create_multi)
self.env['library.book'].create(vals_list)
```

{group}

## Why

- Each call is a full round-trip (Python -> SQL -> Python); a loop turns O(1)
  queries into O(n) and dominates response time on real data volumes.
- Reading fields batches too: iterate a recordset (or `browse` all ids
  first) and the ORM prefetches each field for the whole set in one query;
  a record-by-record `browse(id)` loop defeats the prefetch.

## Exceptions

- A loop that only computes in memory on already-read fields is fine; the
  rule is about calls that hit the database.
- When a per-record call is truly unavoidable (e.g. an external API per
  record), bound the batch size.

# Performance conventions

- Put conditions in the search domain, not in `filtered()` on the result:
  `filtered` runs in Python on records already fetched. Reserve it for
  predicates a domain cannot express.
- **Reduce complexity.** Pre-map results into a dict (`{{r.id: r}}`) instead of
  nested loops; cast membership-test collections to `set` (or use recordset
  arithmetic like `self - invalid`) to avoid O(n^2).
- Index searched fields (`index=True`), selectively, per
  [Fields](fields.md#fields).
"""


def python_md(v):
    ruff = "the `ruff.toml` of the Odoo source is the reference for what core enforces" if v >= 17 else "Odoo's pylint rules are the reference"
    if v >= 18:
        imports3 = "`odoo` submodules (`from odoo import Command, api, fields, models`)"
        api = "in model code the current API is `self.env._(...)`"
        call = "self.env._"
        notes = """- Bare `_` (imported from `odoo`) still works: it locates the environment by
  inspecting the caller's frame; in plain functions and comprehensions it can
  silently return the untranslated string. Prefer `self.env._`.
- Never call `_()` at module or class level: it runs at import time with no
  user language. If a module-level constant is unavoidable, make it lazy
  (`_lt = LazyTranslate(__name__)`; `LABEL = _lt("...")`) and resolve it where
  the language is known, with `self.env._(LABEL)`."""
    else:
        imports3 = "`odoo` submodules (`from odoo import _, api, fields, models, Command`)"
        api = "in model code it is `_(...)`, imported from `odoo`"
        call = "_"
        notes = """- `_` locates the environment by inspecting the caller's frame: call it inside
  model methods, where `self.env` exists; in plain helper functions pass the
  translated string in from the caller.
- Never call `_()` at module or class level: it runs at import time with no
  user language. Use `_lt` (lazy, from `odoo`) for such constants."""
    order_constraints = "`_sql_constraints`" if v < 19 else "`models.Constraint`/`models.Index` attributes"
    return f"""
# Imports

PEP 8 applies; {ruff}.

- Four groups, each alphabetically sorted:
  1. stdlib
  2. third-party libs
  3. {imports3}
  4. `odoo.addons.*` (only when another module's code is needed)

# Naming and model layout

- Model `_name`: dotted, prefixed by module, **singular** (`sale.order`, not
  `sale.orders`). Transient/wizard: `<base_model>.<action>`. SQL-view report
  model: `<base_model>.report.<action>`.
- A variable holding a model class is PascalCase (`Partner =
  self.env['res.partner']`). Suffix a var holding a record id / list of ids
  with `_id` / `_ids` (don't name a `res.partner` record `partner_id`).
- Method-name patterns: compute `_compute_<field>`, search `_search_<field>`,
  default `_default_<field>`, selection `_selection_<field>`, onchange
  `_onchange_<field>`, constraint `_check_<name>`, object action `action_*`
  (acts on one record, so start it with `self.ensure_one()`).
- Model body order: private attrs (`_name`, `_description`, `_inherit`) -> default
  methods -> field declarations -> {order_constraints} -> compute/inverse/search
  (field order) -> selection methods -> `@api.constrains`/`@api.onchange` -> CRUD
  overrides -> action methods -> other business methods.

# Translate only static literals

Translate only **static literals**, passing interpolation values as
arguments; {api}.

```python
# good
raise UserError({call}("Record %s cannot be modified", record.display_name))

# good (several variables): name them so translators keep them straight
msg = {call}("%(count)s records imported by %(user)s", count=len(records), user=user.name)

# bad (formats before the lookup): the dynamic string matches no exported term
raise UserError({call}("Record %s cannot be modified" % record.display_name))

# bad (formats after the lookup): bypasses placeholder validation and reordering
raise UserError({call}("Record %s cannot be modified") % record.display_name)
```

## Why

- Translations are keyed on the exact source literal, at export (building the
  `.pot`) and at runtime lookup. Concatenation, f-strings, or `%`-formatting
  inside `_()` produce strings that exist in neither.
- Named placeholders let translators reorder words per language; passing them
  as arguments lets the framework validate them per translation and apply
  Markup-aware escaping.

## Exceptions and notes

{notes}
- Field *values* are translated via the field's `translate` flag, never `_()`.
- Prefer `%`-style placeholders over `.format()`.
"""


def reports_md(v):
    return (UPSTREAM / "odoo-guidelines/guidelines/reports.md").read_text()


def security_md(v):
    if v == 20:
        return (UPSTREAM / "odoo-guidelines/guidelines/security.md").read_text().replace(
            "Master unifies", "Odoo 20.0 unifies"
        )
    category = "`category_id` (an `ir.module.category`)" if v < 19 else "`privilege_id` (a `res.groups.privilege`)"
    return f"""
# Access rights

Odoo {v}.0 has two layers: **access rows** (`ir.model.access`) say which groups may
read, write, create or unlink a model at all; **record rules** (`ir.rule`) restrict
which records. Both are needed for anything sensitive.

- `security/ir.model.access.csv` columns:
  `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`.
  The id is `access_<model>_<group>`; `model_id:id` is `model_<model_with_underscores>`.
- Default deny: a model with no access row is inaccessible to everyone but the
  superuser, and the module logs a warning at install. Every new model gets at
  least one row.
- An access row with an empty group applies to **everyone**, portal and public
  included; flag any write/create/unlink granted that way, or to
  `base.group_portal` / `base.group_public`.
- Record rules (`ir.rule`, in `security/<module>_security.xml`): rules **with**
  groups are OR-ed together for the user's groups; **global** rules (no group)
  are AND-ed onto every user and can lock everyone out. Set `perm_read`,
  `perm_write`, `perm_create`, `perm_unlink` deliberately.
- Multi-company models need a global rule with a company domain:
  `[('company_id', 'in', company_ids)]` (append `+ [False]` when the company is
  optional).
- Groups (`res.groups`) belong to an application through {category}; a group
  that implies another uses `implied_ids`.

For auditing beyond the data files (`sudo()`, SQL, public methods, ...), use the
`odoo-security` skill.
"""


def installed_md(v):
    return f"""
# Changes to an installed module

A module that is installed in a database that matters (production, or a clone of it)
already has its tables, its XML records and its users' data. A change has to work on
that database after `odoo-bin -u <module>`, not only on a fresh install.

- Bump `version` in the manifest whenever the change needs a migration script or a
  data fix, and write the script (see the `odoo-upgrade` skill). A renamed field
  without a script loses its data: the ORM drops the old column and creates an
  empty one.
- Never rename or remove a stored field, a model or an XML id that data may
  reference without a migration. Prefer adding a new field and computing it from
  the old one.
- Records inside `noupdate="1"` are created once and never updated again: changing
  them in the XML has no effect on an installed database. Fix them in a migration
  script, or tell the user what to change by hand.
- Changing a `required=True` or a `selection` on a field with data: check the
  existing rows first (`odoo-bin shell`, a `search_count`), or the update fails
  or leaves invalid records.
- Public model methods (no `_` prefix) may be called by other modules or
  integrations: don't change their signature without checking every caller.
- Don't modify existing translatable source terms for a typo: that breaks their
  translations. Add the new term and leave the old one when wording matters.
- Test the update on a copy of real data, such as a neutralized clone of production,
  before it reaches production.
"""


def tests_md(v):
    tags = pick(
        v,
        v16_19="""- Tests are tagged `standard` and **`at_install`** by default in {v}.0: they run
  before the other modules are installed. Business tests should run on a fully
  loaded registry: decorate them `@tagged('post_install', '-at_install')`. An
  `HttpCase` (tours) must be `post_install`.""",
        v20="""- Tests are tagged `standard` and `post_install` by default (fully-loaded
  registry); set exactly one of `at_install`/`post_install`. Opt into
  `@tagged('at_install', '-post_install')` only when the test must run before
  other modules load, with a comment justifying it; an `HttpCase` must stay
  `post_install`.""",
    ).format(v=v)
    inherited = (
        "\n  sets `allow_inherited_tests_method = True`."
        if v >= 18
        else "\n  defines its own."
    )
    tour = (
        "- Tours: a step that triggers a page unload must set `expectUnloadPage: true`,\n"
        "  and the last step must leave the client in a stable state (no pending edits\n"
        "  or in-flight requests)."
        if v >= 18
        else "- Tours: the last step must leave the client in a stable state (no pending\n"
        "  edits or in-flight requests), or the teardown races the browser."
    )
    return f"""
# Tests

- Use `TransactionCase` (or `HttpCase` for web); start new business tests from
  `odoo.addons.base.tests.common.BaseCommon` (independent non-admin user and
  company, mail side effects disabled), or
  `TransactionCaseWithUserDemo`/`HttpCaseWithUserDemo` when demo data is
  needed (it is not guaranteed present). Assert behavior, not implementation.
{tags}
- Silent skips: a test file must be named `test_*.py` **and** imported from
  `tests/__init__.py`; the test class must be *defined* in that file (a class
  merely imported into it is skipped); and inherited `test_*` methods are not
  collected: a subclass runs nothing of its parent's unless it{inherited}
- `assertQueryCount` only in dedicated performance tests, never inside a
  business test: it breaks on any unrelated ORM change.
- Wrap expected-error and warning logs in `mute_logger(...)` so the expected
  ERROR or WARNING never reaches the log.
{tour}
- Run them with `odoo-bin -u <module> --test-enable --stop-after-init`; one class
  or method with
  `odoo-bin --test-tags /<module>:<Class>.<method> --stop-after-init`.
"""


def xml_md(v):
    list_tag = "list" if v >= 18 else "tree"
    modifiers = pick(
        v,
        v16="- Dynamic visibility and editability: `attrs=\"{'invisible': [('state', '!=', 'draft')]}\"`\n"
            "  and `states=\"draft\"` on buttons. Keep the domain short; a field used in\n"
            "  `attrs` must be in the view (add it `invisible=\"1\"` when needed).",
        v17_="- Dynamic visibility and editability are Python expressions on the attribute:\n"
             "  `invisible=\"state != 'draft'\"`, `readonly=\"is_locked\"`,\n"
             "  `required=\"partner_id\"`, `column_invisible=\"parent.state == 'done'\"`.\n"
             "  `attrs` and `states` are refused at install in this version.",
    )
    chatter = pick(
        v,
        v16_17="- The chatter of a form inheriting `mail.thread` goes last:\n"
               "  `<div class=\"oe_chatter\"><field name=\"message_follower_ids\"/>\n"
               "  <field name=\"activity_ids\"/><field name=\"message_ids\"/></div>`.",
        v18_="- The chatter of a form inheriting `mail.thread` is `<chatter/>`, last in the form.",
    )
    upstream = (UPSTREAM / "odoo-guidelines/guidelines/xml.md").read_text()
    anchor = upstream[upstream.index("# Anchor view inheritance"):]
    return f"""
# Views, actions and data records

- Record format: put `id` before `model`; inside a `field`, `name` first, then
  the value (tag body or `eval`), then other attributes by importance. Group
  records by model.
- Prefer the syntactic-sugar tags `<menuitem>` and `<template>` over raw
  `<record>`. Trap: an `active` attribute on `<template>` is applied at record
  creation and module *install* only; a module **update** never changes `active`.
- `<data noupdate="1">` only for non-updatable data; if the whole file is
  noupdate, set `noupdate="1"` on `<odoo>` and drop `<data>`.
- The list view is `<{list_tag}>` and its view_mode is `{list_tag}`.
{modifiers}
{chatter}
- XML id patterns: view `<model>_view_<type>` (`form`/`{list_tag}`/`kanban`/`search`),
  action `<model>_action[_<detail>]`, menu `<model>_menu[_<do_stuff>]`, group
  `<module>_group_<name>`, rule `<model>_rule_<group>`. The record `name` mirrors
  the id with dots instead of underscores; actions get a real display name.
- CSS classes in views and templates: prefix with `o_<module>` (`o_` alone is
  reserved for the web client), never style through ids.
- Inheriting a view: see
  [Anchor view inheritance on names, never on position](#anchor-view-inheritance-on-names-never-on-position).

{anchor}
"""


def web_skill(v):
    return f"""
---
name: odoo-web-guidelines
description: >-
  House rules for the web framework code of Odoo {v}.0 addons: the JavaScript,
  Owl templates and SCSS in static/src/ and static/tests/. Use when writing,
  reviewing, or moving files under static/ in an Odoo addon.
---

# Odoo {v}.0 web guidelines

These rules apply to the web framework code an addon ships in `static/src/` and
`static/tests/`: JavaScript, Owl templates (XML) and SCSS. They do not apply to
`static/lib/`, which holds vendored code, nor to `static/description/`.

Guidelines are grouped by domain, one file per domain in `guidelines/`, one section per
guideline. Read the sections that match the code you are touching.

| Guideline | Read it when |
| --- | --- |
| [The web framework in {v}.0](guidelines/javascript.md#the-web-framework-in-{v}0) | writing any JavaScript: modules, services, registries, patches, tests |
| [Organize files by feature](guidelines/javascript.md#organize-files-by-feature-not-by-type) | creating a file, or deciding where new code lives |
| [Avoid getters](guidelines/javascript.md#avoid-getters) | adding a computed value to a class or a component |
| [Patch sparingly](guidelines/javascript.md#patch-sparingly) | extending or overriding behaviour that already exists |
| [SCSS and CSS](guidelines/scss.md#scss-and-css) | touching `*.scss` |
| [Assets](guidelines/assets.md#assets) | adding an image, font, or library |

Adapted from Odoo's own skill library (odoo/odoo, branch 20.0, `skills/`, LGPL-3) and
checked against the {v}.0 source.
"""


def javascript_md(v):
    header = pick(
        v,
        v16_17="- Every JavaScript file under `static/src` starts with `/** @odoo-module **/`;\n"
               "  without it the file is not transpiled and its `import`s fail.",
        v18_="- Files under `static/src` are ES modules; no `@odoo-module` header is needed.",
    )
    patch = pick(
        v,
        v16="`patch(Target.prototype, \"my_module.Target\", { setup() { super.setup(); ... } })`",
        v17_="`patch(Target.prototype, { setup() { super.setup(...arguments); ... } })`",
    )
    field = pick(
        v,
        v16="`registry.category(\"fields\").add(\"my_widget\", MyField)` registers the component",
        v17_="`registry.category(\"fields\").add(\"my_widget\", { component: MyField, supportedTypes: [...] })` registers a descriptor",
    )
    rpc = pick(
        v,
        v16_17="`useService(\"rpc\")` for a route, `useService(\"orm\")` for model methods",
        v18_="`import { rpc } from \"@web/core/network/rpc\"` for a route, `useService(\"orm\")` for model methods",
    )
    owl = pick(
        v,
        v16_19="Owl 2: state with `useState`, lifecycle with `onWillStart`/`onMounted`/`onWillUnmount`",
        v20="Owl 3: reactive `signal` and `computed` next to `useState`; lifecycle with `onWillStart`/`onMounted`/`onWillUnmount`",
    )
    tests = pick(
        v,
        v16_17="QUnit, under `static/tests/`, added to `web.qunit_suite_tests`; run in the browser at `/web/tests`",
        v18="hoot (`@odoo/hoot`): `*.test.js` under `static/tests/`, added to `web.assets_unit_tests`; QUnit is only for legacy suites",
        v19_="hoot (`@odoo/hoot`): `*.test.js` under `static/tests/`, added to `web.assets_unit_tests`",
    )
    html = pick(
        v,
        v16_17="escape with `escape` from `@web/core/utils/strings` or render through `t-out`",
        v18="escape with `htmlEscape` and set content with `setElementContent` (`@web/core/utils/html`), or render through `t-out`",
        v19_="escape with `htmlEscape`, build with `htmlJoin`/`htmlSprintf`, and set content with `setElementContent` (`@web/core/utils/html`), or render through `t-out`",
    )
    return f"""
# The web framework in {v}.0

{header}
- Components are Owl classes with a static `template` (an XML file next to them,
  `t-name="<module>.<Component>"`) and static `props`. {owl}.
- Extend a field widget: {field}.
- Server calls: {rpc}.
- Override existing behaviour: {patch}.
- Raw HTML: never assign `innerHTML` from data; {html}.
- Tests: {tests}.
- Assets are declared in the manifest `assets` (`web.assets_backend`,
  `web.assets_frontend`, ...), never by an XML template in this version.

# Organize files by feature, not by type

Code is organized by feature, not by type. Instead of folders like `components/`,
`services/` or `hooks/`, each feature gets one folder holding all of its files:
`notification/` contains the notification component, its template and its styles.

# Avoid getters

A getter hides the fact that a computation happens, and only saves a pair of
parentheses. Write a plain function instead: the call site then shows that code runs,
and it can take an argument the day the computation needs one.

# Patch sparingly

Outside Odoo's own code a `patch` is the normal way to change standard behaviour, but
it is the hardest code to maintain: reading the patched class no longer tells you what
runs, and the patch drifts from the code it targets at every upgrade. Patch the
smallest method that does the job, always call `super`, and prefer a registry entry,
a new component or a prop when the framework offers one.
"""


def scss_md(v):
    return (UPSTREAM / "odoo-web-guidelines/guidelines/scss.md").read_text()


def assets_md(v):
    return (UPSTREAM / "odoo-web-guidelines/guidelines/assets.md").read_text()


def review_skill(v):
    up = (UPSTREAM / "odoo-review/SKILL.md").read_text()
    head, rest = up.split("## Process", 1)
    head = head.replace(
        "  Review Odoo addon code against the house rules,",
        f"  Review Odoo {v}.0 addon code against the house rules,",
    )
    if v < 20:
        head = head.replace("`ir.access` rows", "`ir.model.access` rows, `ir.rule`")
    return head + f"""## Process

1. **Scope.** Review the working tree (or the commits named): pin the commit and
   its base (`git merge-base HEAD origin/<target branch>`), and
   take the diff from the checkout. Read each touched module's `__manifest__.py`
   for its purpose and `depends`, and the commit messages. A change inside a
   submodule is reviewed in that submodule, and the project commit that points
   at it with it.
2. **Map.** List every changed file with the guideline sections that apply to
   it, taken from the sibling tables. Every file maps to at least one section:
   Python always gets Imports and Naming, anything under `static/` gets the web
   guidelines, a `tests/` file gets Tests, and a module already installed in
   production adds Changes to an installed module.
3. **Read.** Open every mapped section before writing the first finding, and the
   version table (`../odoo-guidelines/guidelines/version.md`).
4. **Rules pass.** Judge the diff against the sections read, then against
   what the diff never shows (below).
5. **Merits pass.** The rules are the floor, not the ceiling. For every changed
   hunk, hunt for the input or state that makes it wrong: edge values,
   rounding, timezones, empty and multi-record calls, multi-company, the
   second run. Check that the commit message's claim is what the code does,
   that the tests would fail without the change, and what the change costs on
   real data.
6. **Prove.** Update the module and run its tests on a database with realistic
   data (`odoo-bin -u <module> --test-enable --stop-after-init`): a review that
   never installed the change has not seen it fail.
7. **Report.** Each finding carries file and line, the defect, the concrete
   failure scenario, a fix, and the guideline section it applies, or
   *judgement* when it came from the merits pass. Close with a
   **Guidelines read:** line listing every section opened. Flag; fix only
   what is unambiguous.

## Version traps

This is Odoo {v}.0. Before flagging or writing an API or attribute,
check the version table, and when it is silent confirm the API exists in the
Odoo {v}.0 source (`grep -rn`) rather than trusting memory:
code written for another version is the most common defect AI-written Odoo code has.

## Code the diff never shows

Odoo modules extend each other: standard ones, other repositories in the
addons path, and the project's own. Anything the diff changes may be consumed by
code it never shows: methods are overridden, fields and XML ids referenced,
templates called and inherited, context keys produced and read on both the
Python and JavaScript sides. For each changed method, field, template, key, or
export, find its consumers across every directory in the addons path and
confirm they still hold.

- Overrides: `grep -rn "def <name>("` and read them. Do they still call
  `super()` with valid arguments?
- Renamed or removed names: grep for them in Python, XML, and JavaScript. A
  stale reference in a view, a domain, an xpath, a `patch()`, or an import
  fails only at runtime, or only when that module is installed.
- Data already in the database: a renamed field, a changed selection or a
  removed XML id needs a migration (see the `odoo-upgrade` skill).
"""


def security_skill(v):
    up = (UPSTREAM / "odoo-security/SKILL.md").read_text()
    up = up.replace("description: >-\n  Security audit of Odoo addon code:", f"description: >-\n  Security audit of Odoo {v}.0 addon code:")
    if v < 20:
        up = up.replace("(ir.access, field groups,", "(ir.model.access, ir.rule, field groups,")
        up = up.replace(
            """## Access control

Mechanics of `ir.access` rows and field `groups` are in the `odoo-guidelines`
skill ([Access rights](../odoo-guidelines/guidelines/security.md#access-rights),
[Fields](../odoo-guidelines/guidelines/fields.md#fields)); audit `security/` with
the attacker's reading:

- Flag any `c`/`u`/`d` operation granted to `base.group_everyone`,
  `base.group_portal`, or `base.group_public`; scrutinize even `r` on models
  holding personal or business-sensitive data.
- A permission row's `operation` set is what it grants; a *restriction*
  (group-less) row covering only some operations leaves the others governed by
  the permission rows alone: if any permission grants `write`, an attacker
  can alter records the read restriction hides (`write` checks write access
  only, never read). Cover **all** CRUD operations that need restricting.
- Multi-company models need a company restriction row; sensitive models need
  domain restrictions, not just group permissions.""",
            """## Access control

Mechanics of `ir.model.access` rows, `ir.rule` record rules and field `groups` are
in the `odoo-guidelines` skill
([Access rights](../odoo-guidelines/guidelines/security.md#access-rights),
[Fields](../odoo-guidelines/guidelines/fields.md#fields)); audit `security/` with
the attacker's reading:

- Flag any write/create/unlink granted to an access row with no group, or to
  `base.group_portal` / `base.group_public`; scrutinize even read on models
  holding personal or business-sensitive data.
- A record rule restricting only `perm_read` leaves write governed by the access
  rows alone: an attacker can alter records the read rule hides (write checks
  write rules only). Cover **all** operations that need restricting.
- Multi-company models need a global company rule; sensitive models need record
  rules, not just access rows.""",
        )
    if v < 19:
        up = up.replace(
            """- Build/extend domains with `fields.Domain` (`domain &= Domain(...)`), never
  by concatenating a user-provided list onto a security domain (a user could
  inject `['|', ...]` to widen access).""",
            """- Extend domains with `expression.AND([security_domain, user_domain])`, never
  by concatenating a user-provided list onto a security domain (a user could
  inject `['|', ...]` to widen access).""",
        )
    if v < 20:
        up = up.replace(
            "| `innerHTML`, `insertAdjacentHTML`, `markup(` (JS), `Markup(` (Python), `t-raw` (dead code) |",
            "| `innerHTML`, `insertAdjacentHTML`, `markup(` (JS), `Markup(` (Python), `t-raw` |",
        )
        up = up.replace(
            """- Server/QWeb: render with `t-out` (escapes by default). `t-raw` no longer
  exists in either server QWeb or OWL: flag any occurrence as broken legacy
  code; the raw-HTML vector today is a `Markup`/`markup()` value reaching
  `t-out`.""",
            """- Server/QWeb: render with `t-out` (escapes by default). `t-raw` still renders
  raw HTML in this version (with a deprecation warning): flag every occurrence
  fed by data. The other raw-HTML vector is a `Markup`/`markup()` value reaching
  `t-out`.""",
        )
        up = up.replace(
            """literal. (`t-esc`: deprecated-but-escaping alias in OWL; server QWeb
  ignores it and renders nothing, a bug to flag, though not an XSS.)""",
            """literal. (`t-esc` still escapes in this version; prefer `t-out`.)""",
        )
    html = pick(
        v,
        v16_17="  Escape with `escape` (`@web/core/utils/strings`) or use the tagged-template form\n  ``markup`<td>${name}</td>` `` (placeholders auto-escape; plain\n  `markup(str)` marks raw HTML), or render through OWL `t-out`.",
        v18="  Escape with `htmlEscape` (`@web/core/utils/html`) or use the tagged-template form\n  ``markup`<td>${name}</td>` `` (placeholders auto-escape; plain\n  `markup(str)` marks raw HTML), set content with `setElementContent`, or render\n  through OWL `t-out`.",
        v19_="  Escape with `htmlEscape` (`@odoo/owl`) or use the tagged-template form\n  ``markup`<td>${name}</td>` `` (placeholders auto-escape; plain\n  `markup(str)` marks raw HTML), use the `@web/core/utils/html` helpers\n  (`setElementContent`, `htmlJoin`), or render through OWL `t-out`.",
    )
    up = up.replace(
        """  Escape with `htmlEscape` (`@odoo/owl`) or use the tagged-template form
  ``markup`<td>${name}</td>` `` (placeholders auto-escape; plain
  `markup(str)` marks raw HTML), use the `@web/core/utils/html` helpers
  (`setInnerHtml`, `htmlJoin`), or render through OWL `t-out`.""",
        html,
    )
    routes = pick(
        v,
        v16_18="  keep CSRF on (never `csrf=False`, except dedicated webhooks);\n  `json` routes have no token check by design, their protection is\n  the JSON content type.",
        v19_="  keep CSRF on (never `csrf=False`, except dedicated webhooks);\n  `jsonrpc`/`json2` routes have no token check by design, their protection is\n  the JSON content type.",
    )
    up = up.replace(
        "  keep CSRF on (never `csrf=False`, except dedicated webhooks);\n  `jsonrpc`/`json2` routes have no token check by design, their protection is\n  the JSON content type.",
        routes,
    )
    up = up.replace(
        "  gives broad capabilities, and plain `eval` allows\n  `__import__('os').popen(...)` RCE; master's extra `--unsafe-policy`\n  whitelist sandbox is observe-only by default).",
        "  gives broad capabilities, and plain `eval` allows\n  `__import__('os').popen(...)` RCE).",
    )
    up = up.replace(
        "  Prefer `search`/`_read_group` and direct field access (not `read()`). For\n  custom SQL over ORM-filtered rows, build the query with `_search(...)` and\n  `Query.select(SQL(...))`: access rules and `active` handling stay in force.",
        "  Prefer `search`/`" + ("read_group" if v == 16 else "_read_group") + "` and direct field access (not `read()`). For\n  custom SQL over ORM-filtered rows, build the query with `_search(...)`" + (" and\n  `Query.select(SQL(...))`" if v >= 17 else "") + ": access rules and `active` handling stay in force.",
    )
    if v == 16:
        up = up.replace(
            "  values as **parameters** (psycopg2 formats them, including a tuple for\n  `IN %s`), or use the `odoo.tools.SQL` wrapper. For dynamic **identifiers**\n  (table/column names, which can't be parameters) use `SQL.identifier(name)`,\n  which validates the name (via `assert`, so a `-O` deployment skips the\n  check; still never feed it raw user input).",
            "  values as **parameters** (psycopg2 formats them, including a tuple for\n  `IN %s`). For dynamic **identifiers** (table/column names, which can't be\n  parameters) use `psycopg2.sql.Identifier`, and never feed them raw user input.",
        )
    return up


def git_skill(v):
    return f"""
---
name: odoo-git
description: >-
  Commit and pull request conventions for an Odoo project repository: the
  [TAG] module: header, a why-first body, one logical change per commit,
  submodules, branches and pull requests. Use when committing, writing a commit
  message or a pull request description, or publishing work.
---

# Commits and pull requests

For a project's Odoo repository: its own modules, and the repositories it brings in
as submodules. Commits follow Odoo's own message convention. If the environment you
work in has its own way to publish (a platform skill says so), use it instead of
`git push`.

## Commit message

A header `[TAG] module: summary`, a blank line, a body that says **why**, and
references last.

```
[FIX] acme_sale: keep the delivery date when the order is duplicated

Duplicating a confirmed order cleared the promised delivery date, so the
copy went out with today's date and the customer was promised the wrong
day.

The field was declared copy=False to avoid copying it into quotations
created from templates; templates now clear it in their own copy() instead.
```

- `[TAG]`, a space, the module's technical name (or several: `acme_sale, acme_stock:`),
  a colon, the summary. The summary completes "if applied, this commit will ...":
  imperative, no trailing period, about 50 characters; the header under ~72.
- Tags: `[FIX]` bug fix, `[IMP]` improvement, `[ADD]` new module, `[REF]` refactor,
  `[REM]` removal, `[MOV]` move without content change, `[REV]` revert, `[PERF]`
  performance, `[I18N]` translations, `[MIG]` migration of a module to {v}.0.
- Body: why first, what was wrong for whom; for a fix, the steps that reproduce it.
  The diff gives the what. Wrap at ~72 characters, ASCII punctuation only.
- Never invent a ticket or task reference; ask the user for it, or leave it out.
- Write the message in English unless the repository's history is in another language.

## Commits

- One logical change per commit, one module per commit unless inseparable.
- A change inside a submodule is committed **in the submodule first**, then in the
  project (`git add <submodule path>`), so the project points at it.
- Never change the configured git identity (`user.name`/`user.email`).
- Never commit generated files, secrets, dumps or `__pycache__`.

## Branches and pull requests

- One branch per change, named after it (`{v}.0-fix-delivery-date`), from the branch
  it will be merged into; rebase on that branch rather than merging it in.
- A pull request carries only the commits that should land: squash fixups into the
  commit they fix.
- The description says why, which modules it touches, how to test it, and whether it
  needs a module update or a migration. Write it in the reader's language.
- A change in a submodule needs a pull request in that submodule's repository too,
  merged before the project's, or the project points at a commit nobody can fetch.
"""


def build(v):
    root = OUT / "odoo" / f"{v}.0"
    for skill in ("odoo-guidelines", "odoo-web-guidelines", "odoo-review", "odoo-security", "odoo-git"):
        if (root / skill).exists():
            shutil.rmtree(root / skill)
    g = root / "odoo-guidelines"
    write(g / "SKILL.md", guidelines_skill(v))
    write(g / "guidelines/version.md", version_md(v))
    write(g / "guidelines/comments.md", comments_md(v))
    write(g / "guidelines/controllers.md", controllers_md(v))
    write(g / "guidelines/fields.md", fields_md(v))
    write(g / "guidelines/manifest.md", manifest_md(v))
    write(g / "guidelines/module_structure.md", module_structure_md(v))
    write(g / "guidelines/orm.md", orm_md(v))
    write(g / "guidelines/performance.md", performance_md(v))
    write(g / "guidelines/python.md", python_md(v))
    write(g / "guidelines/reports.md", reports_md(v))
    write(g / "guidelines/security.md", security_md(v))
    write(g / "guidelines/installed.md", installed_md(v))
    write(g / "guidelines/tests.md", tests_md(v))
    write(g / "guidelines/xml.md", xml_md(v))
    w = root / "odoo-web-guidelines"
    write(w / "SKILL.md", web_skill(v))
    write(w / "guidelines/javascript.md", javascript_md(v))
    write(w / "guidelines/scss.md", scss_md(v))
    write(w / "guidelines/assets.md", assets_md(v))
    write(root / "odoo-review/SKILL.md", review_skill(v))
    write(root / "odoo-security/SKILL.md", security_skill(v))
    write(root / "odoo-git/SKILL.md", git_skill(v))


for version in VERSIONS:
    build(version)
print("ok")
