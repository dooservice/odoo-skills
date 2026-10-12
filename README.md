# Odoo skills for every version, 16.0 to 20.0

[Agent skills](https://agentskills.io) that help AI coding agents (Claude Code, opencode,
Codex, Copilot CLI...) write, review and audit Odoo addons **for the Odoo version you
actually run**.

Odoo ships its own skills in the `skills/` directory of the 20.0 branch. They are
excellent, and they are written for 20.0: an agent following them on a 16.0 or 18.0
codebase writes `models.Constraint`, `<list>`, `ir.access.csv` or `self.env._` where
they do not exist. This repository adapts them to each supported version, with every
version-specific statement checked against that branch's source.

| Skill | What it covers |
|---|---|
| `odoo-guidelines` | module structure, manifest, Python/ORM, fields, controllers, XML views and data, reports, access rights, performance, tests, changes to installed modules, and `guidelines/version.md`: what exists in that version |
| `odoo-web-guidelines` | JavaScript, Owl templates and SCSS under `static/`: module headers, patches, registries, RPC, tests |
| `odoo-security` | access control, `sudo()`, SQL and domain injection, XSS, routes and CSRF, `eval`, files, timing attacks |
| `odoo-review` | a two-pass review of a diff: house rules, then the merits, then proving it installs |
| `odoo-git` | commit messages (`[TAG] module: summary`, why first), branches, submodules, pull requests |
| `odoo-upgrade` | porting a module to a newer version, and migration scripts with odoo-upgrade-util |
| `odoo-reference` | generated from each version's source: every addon's models (fields, public methods, extension points), every Settings switch and where it keeps its value, and every XML id an addon declares |

## What changes between versions

A few of the rows in each `odoo/<version>/odoo-guidelines/guidelines/version.md`:

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| View modifiers | `attrs`, `states` | expressions | expressions | expressions | expressions |
| List view | `<tree>` | `<tree>` | `<list>` | `<list>` | `<list>` |
| Display name | `name_get` | `_compute_display_name` | `_compute_display_name` | `_compute_display_name` | `_compute_display_name` |
| SQL constraints | `_sql_constraints` | `_sql_constraints` | `_sql_constraints` | `models.Constraint` | `models.Constraint` |
| Domains | `expression.AND/OR` | `expression.AND/OR` | `expression.AND/OR` | `Domain` | `Domain` |
| Translations | `_()` | `_()` | `self.env._()` | `self.env._()` | `self.env._()` |
| Access rights | `ir.model.access.csv` | `ir.model.access.csv` | `ir.model.access.csv` | `ir.model.access.csv` | `ir.access.csv` |
| Default test tag | `at_install` | `at_install` | `at_install` | `at_install` | `post_install` |
| JS tests | QUnit | QUnit | hoot | hoot | hoot |
| Owl | 2 | 2 | 2 | 2 | 3 |

## Install

Copy the skills of your version, together with `odoo/common/`, where your agent reads
skills. The skills reference each other, so install them all:

```bash
git clone https://github.com/dooservice/odoo-skills.git
mkdir -p ~/.claude/skills
cp -r odoo-skills/odoo/18.0/* odoo-skills/odoo/common/* ~/.claude/skills/
```

For a single project, use `.claude/skills/` (or `.agents/skills/`) at its root instead.
opencode reads `~/.config/opencode/skills/`. Restart the agent; it picks the skill that
matches the task by itself.

## Layout

```
odoo/<version>/      generated: odoo-guidelines, odoo-web-guidelines, odoo-security, odoo-review,
                     odoo-git (from Odoo's 20.0 skills) and odoo-reference (from that version's source)
odoo/common/         version-independent: odoo-upgrade
dooservice/          the dooservice platform's own: its console commands, and configuring Odoo without code
generate.py          builds the guideline skills of odoo/<version>/ from Odoo's 20.0 skills
build_reference.py   builds odoo/<version>/odoo-reference from .odoo/src/<version>
```

The `odoo/<version>/` skills are generated; change `generate.py`, not the files. To
regenerate after Odoo updates its skills:

```bash
git clone --depth 1 -b 20.0 --filter=blob:none --sparse https://github.com/odoo/odoo.git .odoo/src/20.0
git -C .odoo/src/20.0 sparse-checkout set skills
python3 generate.py .odoo/src/20.0/skills .
```

To regenerate the references, check out each version without its static files and
translations, then build:

```bash
for v in 16.0 17.0 18.0 19.0 20.0; do
  git clone --depth 1 -b $v --filter=blob:none --no-checkout https://github.com/odoo/odoo.git .odoo/src/$v
  git -C .odoo/src/$v sparse-checkout set --no-cone '/*' '!/addons/*/static/' '!/addons/*/i18n/' \
    '!/odoo/addons/*/static/' '!/odoo/addons/*/i18n/' '/addons/web/static/src/' '/skills/'
  git -C .odoo/src/$v checkout $v
done
python3 build_reference.py
```

Check every version-specific change in that branch's source before making it:
`.odoo/` is ignored by git and is the place for those checkouts.

## Credits and license

Derived from Odoo's skill library (odoo/odoo, branch 20.0, `skills/`), by Odoo S.A.,
licensed LGPL-3; this work is LGPL-3 as well (see [LICENSE](LICENSE)). Not affiliated
with or endorsed by Odoo S.A.

Maintained by [dooservice](https://dooservice.sh), which uses them in the AI console of
its Odoo hosting platform.
