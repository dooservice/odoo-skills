---
name: odoo-upgrade
description: >-
  Migrating custom Odoo modules: porting a module from an older Odoo version to
  the version the project runs, and writing migration scripts (pre/post/end,
  odoo-upgrade-util) when a module's own data model changes. Use when asked to
  upgrade or port a module, when a renamed or removed field or model needs its
  data kept, or when bumping a module's version.
---

# Upgrading and migrating Odoo modules

Two different jobs share the word:

- **Porting** a module written for an older Odoo to the version the project runs.
- **Migrating data** when a module's own models change between two of its versions on
  the same Odoo.

## Porting a module

1. **Ask the source version** if it has not been given. Read the module's manifest,
   models and views before proposing anything.
2. **Check what is standard now.** Before adapting custom code, look for each custom
   feature in the target version: your knowledge first, then the official
   documentation and release notes (https://www.odoo.com/page/release-notes) for every
   version in between, and only then the source in
   Odoo source of the target version. Present the findings and agree with the user
   on what to keep, drop or rewrite before touching code.
3. **Port.** Read the version table in `odoo-guidelines` (`guidelines/version.md`) and
   rewrite what changed: view modifiers, list tags, display names, grouped reads,
   constraints, domains, translations, access files, JS modules and tests. Set the
   manifest `version` to `<target>.1.0.0`. Commit as `[MIG] <module>: port to <target>`.
4. **Prove.** `odoo-bin -i <module> --stop-after-init` on a database without it, then
   `odoo-bin -u <module> --test-enable --stop-after-init`. Keep existing tests: adapt their syntax, never the
   business flow they check.
5. A database that ran the old version needs Odoo's own upgrade service for the
   standard modules; custom modules come along through their migration scripts. Say
   so when the user expects the data to follow.

## Migration scripts

Odoo runs them during `odoo-bin -u <module>` when the manifest `version` grows:

```
<module>/migrations/<new version>/pre-migrate.py   before the module's models load
<module>/migrations/<new version>/post-migrate.py  after its models and data load
<module>/migrations/<new version>/end-migrate.py   after every module is updated
```

Any `pre-*.py`, `post-*.py` or `end-*.py` file runs, in name order. Each file defines `def migrate(cr, version):`, where `version` is the version that was
installed (`None` on a fresh install: return early then).

- **pre**: rename columns/fields/models before the ORM sees the new definitions, or
  the ORM drops the old column and creates an empty one.
- **post**: recompute, fill, convert data with the new models in place.
- **end**: what depends on other modules being updated too.

### odoo-upgrade-util

Prefer its helpers to raw SQL: they handle the columns, XML ids, translations, views,
filters and server actions that reference what changes.

```python
from odoo.upgrade import util

def migrate(cr, version):
    util.rename_field(cr, "library.book", "writer_id", "author_id")
    util.remove_field(cr, "library.book", "legacy_code")
    util.rename_xmlid(cr, "library.old_view", "library.book_view_form")
```

Others worth knowing: `util.rename_model`, `util.merge_model`, `util.remove_model`,
`util.create_column`, `util.recompute_fields`, `util.update_record_from_xml`,
`util.env(cr)` for ORM access in a post script.

It is not installed by default. For the session:

```bash
python3 -m pip install --break-system-packages git+https://github.com/odoo/upgrade-util@master
```

For the deployment, add `odoo_upgrade @ git+https://github.com/odoo/upgrade-util@master`
to the repository's `requirements.txt` and commit it.

### Checking a migration

Bump the version, `odoo-bin -u <module> --stop-after-init`, read the log for the migration lines
(`module <module>: Running upgrade ...`), and check the data in `odoo-bin shell`. Try
every migration on a copy of production data (a neutralized clone) before it is
merged.
