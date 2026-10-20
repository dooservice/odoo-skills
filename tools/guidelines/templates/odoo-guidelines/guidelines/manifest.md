# Manifest

- `name` is required. `version` is `$version.x.y.z` (the Odoo series, then the
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
