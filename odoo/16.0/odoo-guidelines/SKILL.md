---
name: odoo-guidelines
description: >-
  Read before writing or reviewing any Python, XML or CSV for Odoo 16.0,
  even if you know Odoo: names change between versions. In 16.0: views use `<tree>` and `attrs`/`states`; `name_get`; `_sql_constraints`; domains with `expression.AND/OR`; `group_operator`; chatter `<div class="oe_chatter">`; `_()`; `ir.model.access.csv` and `ir.rule`; users `groups_id`; `get_param`; routes `type='json'`; test tag `at_install`.
  Covers modules, models, fields, the ORM, api decorators, views, actions,
  menus, scheduled actions, security, controllers, the external API, mail,
  multi-company, reports, data, migrations, translations, tests and odoo-bin;
  JavaScript, Owl and SCSS are in odoo-web-guidelines.
---

# Odoo 16.0 addon guidelines

House rules for Python, XML and CSV in Odoo 16.0 addons; what an addon ships under
`static/` is in `odoo-web-guidelines`. These rules are written for 16.0: when an API,
view attribute, security record or record field is in doubt, check
[What Odoo 16.0 has](guidelines/version.md#what-odoo-160-has) first.

Open only the files of your task. Each file starts with the names that matter most in
16.0 and the list of its sections: read that top, then only the sections you need.
No rule outranks another.

| Task | Open |
| --- | --- |
| Start a module: layout, manifest, imports, naming | [module_structure.md](guidelines/module_structure.md), [manifest.md](guidelines/manifest.md), [python.md](guidelines/python.md) |
| A model: attributes, inheritance, overrides, SQL constraints | [models.md](guidelines/models.md) |
| Fields: types, attributes, relations, dates, floats, indexes | [fields.md](guidelines/fields.md) |
| Computes, onchange, constraints, `create`/`unlink` overrides | [computed_fields.md](guidelines/computed_fields.md), [api.md](guidelines/api.md) |
| Search, read and write records; context; batching | [orm.md](guidelines/orm.md), [performance.md](guidelines/performance.md) |
| Access checks in code, raw SQL, caches, field translations, locks, transactions | [orm_advanced.md](guidelines/orm_advanced.md) |
| Views and view inheritance | [views.md](guidelines/views.md), [xml.md](guidelines/xml.md) |
| Actions, menus, scheduled actions, data records | [actions.md](guidelines/actions.md), [xml.md](guidelines/xml.md) |
| Access rights, record rules, groups, `sudo()` | [security.md](guidelines/security.md) |
| Controllers, portal, the external API | [controllers.md](guidelines/controllers.md), [external_api.md](guidelines/external_api.md) |
| Mail, chatter, tracking, email templates | [mail.md](guidelines/mail.md) |
| Multi-company | [multi_company.md](guidelines/multi_company.md) |
| QWeb PDF reports | [reports.md](guidelines/reports.md) |
| Data files, migrations, translations | [installed.md](guidelines/installed.md), [migrations.md](guidelines/migrations.md), [translations.md](guidelines/translations.md) |
| Tests | [tests.md](guidelines/tests.md) |
| `odoo-bin`: run, shell, subcommands | [command_line.md](guidelines/command_line.md) |
| An installed module, or a fix in a stable version | [installed.md](guidelines/installed.md), [stable.md](guidelines/stable.md), [migrations.md](guidelines/migrations.md) |
| Comments, docstrings, messages | [comments.md](guidelines/comments.md) |

To add or restructure a guideline, follow [AUTHORING.md](AUTHORING.md).

Adapted from Odoo's own skill library (odoo/odoo, branch 20.0, `skills/`, LGPL-3) and
checked against the 16.0 source.
