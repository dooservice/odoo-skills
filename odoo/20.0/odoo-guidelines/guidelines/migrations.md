Key names in 20.0: `'version': '20.0.1.0.0'`; a script folder is the full version (`20.0.1.1.0`) or the module part (`1.1.0`), its scripts define `migrate(cr, version)`; `util.rename_field` and the rest of upgrade-util for renames; hooks take `env`.

Sections of this file:

- [Version the module as series.x.y.z](#version-the-module-as-seriesxyz)
- [Write a migration script for every data change between two versions](#write-a-migration-script-for-every-data-change-between-two-versions)
- [Use upgrade-util for renames and removals](#use-upgrade-util-for-renames-and-removals)
- [Use init hooks only for install-time work](#use-init-hooks-only-for-install-time-work)

# Version the module as series.x.y.z

The manifest `version` is the Odoo series followed by the module's own three numbers:
`'version': '20.0.1.0.0'`. Migration scripts run by comparing it with the version
the database has installed, so it is what decides whether a script runs.

- Bump `x` for a change that breaks other modules or data (a removed field, a renamed
  model), `y` for a feature, `z` for a fix. Any change that ships a migration script
  bumps the version to the version of that script.
- A version without the series (`1.0.0`) is prefixed with it. A version that is not two to five
  numbers stops the module from loading with `ValueError` (`invalid manifest`); the
  version of another series makes the module uninstallable, with a log warning only.
- Never lower the version of an installed module: the scripts between the two versions
  would never run.

# Write a migration script for every data change between two versions

`odoo-bin -u library` updates the schema and reloads the data files, but it never
moves data: a renamed field ends empty, a split field stays unfilled. Each such change
gets a script in the module:

```text
library/
  migrations/
    20.0.1.1.0/
      pre-rename_author.py
      post-fill_isbn.py
      end-recompute_stats.py
```

```python
def migrate(cr, version):
    cr.execute("UPDATE library_book SET isbn = barcode WHERE isbn IS NULL")
```

- The folder is the module version that needs the script. Name it with the full version
  (`20.0.1.1.0`) or the module part alone (`1.1.0`), compared without the
  series.
- A script runs when the installed version is lower than its folder and the new version
  is equal or higher. On install, no script runs.
- `version` is the installed version, the one being migrated from. A script without
  `migrate(cr, version)` stops the update (the parameters may also be named `_cr`
  and `_version`).
- `pre-` scripts run before the module's Python models are loaded: the tables still
  have the old schema and the ORM does not know the new fields, so they use SQL. Rename
  a column there: once the models load, the ORM creates the new column empty, and the
  end of the update drops the old one with its data.
- `post-` scripts run after the module's models and data files are loaded: use the ORM
  through `env = api.Environment(cr, api.SUPERUSER_ID, {})`.
- `end-` scripts run once every module of the update is loaded: use them for data that
  other modules' fields or overrides compute.
- Files run in name order within a stage. A folder named `0.0.0` holds scripts run on
  every version change: first among `pre-` scripts, last among `post-` and `end-`.
- Scripts may also live in an `upgrades/` folder of the module, or in a
  `<module>/<version>/` folder of a path given by `--upgrade-path`; they follow the same
  rules.
- Test the update on a copy of production with
  `odoo-bin -d library_copy -u library --stop-after-init`, never only a fresh install.

# Use upgrade-util for renames and removals

Renaming or removing a field, a model or an XML id by hand in SQL leaves references
behind (`ir_model_data`, `ir_model_fields`, views, filters, server actions). The
upgrade-util library (`odoo/upgrade-util` on GitHub) updates all of them.

- It is not part of Odoo: install it, or pass its `src` folder to `--upgrade-path`. It
  is then imported as `from odoo.upgrade import util`.
- In a `pre-` script: `util.rename_field(cr, 'library.book', 'author', 'author_name')`,
  `util.rename_model(cr, 'library.loan', 'library.lending')`,
  `util.remove_field(cr, 'library.book', 'old_code')`,
  `util.rename_xmlid(cr, 'library.old_menu', 'library.menu_books')`.
- Without upgrade-util, rename the column in a `pre-` script and update the matching
  `ir_model_data` rows yourself; never let the ORM drop a column that holds data.

# Use init hooks only for install-time work

`pre_init_hook`, `post_init_hook` and `uninstall_hook` name functions of the module's
`__init__.py` in the manifest (`'post_init_hook': 'post_init_hook'`):

```python
def pre_init_hook(env):
    ...


def post_init_hook(env):
    env['library.book'].search([])._compute_isbn()


def uninstall_hook(env):
    ...
```

Each hook receives an `env` as superuser; a hook written with the `(cr)` or
`(cr, registry)` signature of earlier versions fails.

- `pre_init_hook` runs on install, before the module's tables exist; `post_init_hook`
  runs on install, after its data files are loaded; `uninstall_hook` runs on uninstall,
  before the module's data and tables are removed.
- No hook runs on `-u`. Anything that an installed database also needs goes in a
  migration script; a hook alone leaves existing databases without it.
- Prefer a data file to a `post_init_hook` whenever the records can be written in
  XML or CSV: data files are updated and cleaned up with the module, hook data is not.
- `post_load` names a function called without arguments right after the module's Python
  package is imported; it is only for patches of Odoo's own code.
