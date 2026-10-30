# Odoo skills for every version, 16.0 to 20.0

[Agent skills](https://agentskills.io) that make AI agents (Claude Code, OpenCode, Codex,
Cursor, Copilot...) work on Odoo the way an experienced developer and functional
consultant would, **for the Odoo version you actually run**.

An agent that knows Odoo 20.0 writes `<list>`, `models.Constraint` or `is_storable` in a
16.0 project, where they do not exist, and configures a database with fields that
version does not have. These skills tell it what each version has, and how Odoo itself
does each task.

## What is inside

| For | Skills | What they cover |
|---|---|---|
| **Developers** | `odoo-guidelines`, `odoo-web-guidelines`, `odoo-security`, `odoo-review`, `odoo-git`, `odoo-upgrade` | every framework feature of each version: models and inheritance, every field type, `api` decorator and public ORM method, every view and action type, menus and scheduled actions, routes and the external API, mail, multi-company, access rights, reports, data files, migrations, translations, tests and `odoo-bin`; in the web client Owl, every registry, services, field widgets and views, website and portal, the Point of Sale and JavaScript tests; plus security audits, code review, commits and porting between versions |
| **Functional consultants** | `odoo-functional` | configuring Odoo without code, in 70 recipes that follow Odoo's own flow step by step and together cover every Community app and module of each version: accounting, sales and CRM, purchase, inventory, manufacturing, repairs and maintenance, Point of Sale, website and eCommerce, marketing and events, projects, HR, fleet, settings and security, and "why does Odoo do X" |
| **Everyone** | `odoo-reference` | every model, field, Settings switch and XML id of each version, generated from its source |

Only Odoo's standard flows, the same in every country. Localizations (`l10n_*`: a
country's chart of accounts, taxes, electronic invoicing, legal reports) are not covered:
each needs accountants of that country to keep it right as its law changes.

## How it is checked

- **Every recipe follows Odoo's own flow and its code.** The steps follow Odoo's
  documentation and menus of each version, and every model, field, value, method, setting
  and menu they name is checked in that version's source. The first 26 recipes were also
  run on a real database of each version.
- **Nothing is left out by accident.** `tools/build_coverage.py` reads every Community
  module and every framework feature (field types, `api` decorators, view and action
  types, route types and `auth` values, public ORM methods, web client registries, test
  tools) from the source of each version, and checks that a recipe or a guideline covers
  it; [`COVERAGE.md`](COVERAGE.md) is its report. Today nothing is missing in any version.
- **The reference matches a running Odoo.** Every model, field, XML id and Settings field
  it lists was compared with Odoo's own registry, in each version: no mismatch.
- **Every version difference is checked in that branch's source**, with the file and line.
- **What it changes is measured.** `evals/` runs the same tasks with and without the
  skills; see [the results](#results).

The developer skills are adapted from Odoo's own skill library (20.0 branch), with every
version-specific statement checked against that branch's source.

## Results

The same tasks, run three times each with and without the skills. Each task asks for a
file (a view, a model, a controller, an `odoo-bin shell` script) and checks that it uses
what that Odoo version has and nothing it does not. Measured on the 1.1.1 skills, on
2026-10-30.

**Claude Haiku 5.5**, a small and cheap model

| Odoo | Tasks | With the skills | Without | Difference | Code / functional with the skills | Cost |
|---|---|---|---|---|---|---|
| 20.0 | 19 | **100%** | 59.1% | **+40.9 points** | 100% / 100% | 0.36 USD |
| 19.0 | 22 | **100%** | 77.8% | **+22.2 points** | 100% / 100% | 0.40 USD |
| 18.0 | 20 | **100%** | 86.3% | **+13.7 points** | 100% / 100% | 0.31 USD |
| 17.0 | 21 | **98.3%** | 85.8% | **+12.5 points** | 100% / 96.4% | 0.31 USD |
| 16.0 | 20 | **97.2%** | 88.9% | **+8.3 points** | 96.7% / 97.8% | 0.30 USD |

**Claude Sonnet 5.5**

| Odoo | Tasks | With the skills | Without | Difference | Cost |
|---|---|---|---|---|---|
| 20.0 | 19 | **99.4%** | 68.6% | **+30.8 points** | 4.52 USD |
| 19.0 | 22 | **100%** | 94.4% | +5.6 points | 4.74 USD |
| 18.0 | 20 | **100%** | 96.1% | +3.9 points | 4.11 USD |
| 17.0 | 21 | **100%** | 94.0% | +6.0 points | 4.45 USD |
| 16.0 | 20 | **98.3%** | 95.0% | +3.3 points | 4.23 USD |

Sonnet on 17.0 to 19.0 was measured on 1.1.0, already at 100%; 1.1.1 changes only the
skills' descriptions. The cost is what each suite cost through the API, both sides
included.

The skills matter most where a model knows least: the newest version, and the smaller
model. With 1.1.0, Haiku gained only 13.6 points on 20.0, because on code tasks it did not
load the skills and wrote from memory. 1.1.1 puts the names that change most in each
version into the skills' descriptions, the one part an agent always sees: Haiku now
reaches 97% to 100% on every version. The full history, with every run, its cost and its
tokens, is in [`evals/RESULTS.md`](evals/RESULTS.md); the cases, the graders and how to
run them are in [`evals/`](evals/README.md).

How these results were reached: [case study](docs/case-study/README.md).

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

Install the skills of the Odoo version you run. They reference each other, so install
the whole set: the version's own skills and the common ones.

**Claude Code**: one plugin per version, `odoo-16` to `odoo-20`:

```
/plugin install odoo-18 --marketplace dooservice/odoo-skills
```

Or from your shell: `claude plugin marketplace add dooservice/odoo-skills`, then
`claude plugin install odoo-18@odoo-skills`. `/plugin` updates it.

**Any agent** (Claude Code, OpenCode, Codex, Cursor, Copilot and more), with
[`npx skills`](https://github.com/vercel-labs/skills); from the root of your Odoo project:

```bash
curl -fsSL https://raw.githubusercontent.com/dooservice/odoo-skills/main/install.sh | bash
```

It reads the version from the first `__manifest__.py` it finds (`18.0.1.0.0` is Odoo
18.0), or takes it as an argument (`| bash -s 17.0`), and installs for the agents it finds
on your machine. Other options pass through to `npx skills add`: `-g` for every project of your user,
`-a codex` for one agent. The same without the script:

```bash
npx skills add dooservice/odoo-skills/odoo/18.0
npx skills add dooservice/odoo-skills/odoo/common
```

**By hand**: copy the folders where your agent reads skills (`.claude/skills/` or
`.agents/skills/` in the project, `~/.claude/skills/` for your user):

```bash
git clone --depth 1 https://github.com/dooservice/odoo-skills.git
cp -r odoo-skills/odoo/18.0/* odoo-skills/odoo/common/* ~/.claude/skills/
```

Restart the agent; it picks the skill that matches the task by itself.

## Layout

```
odoo/<version>/      generated: odoo-guidelines, odoo-web-guidelines, odoo-security, odoo-review,
                     odoo-git (from Odoo's 20.0 skills) and odoo-reference (from that version's source)
odoo/common/         version-independent, written by hand: odoo-upgrade, and odoo-functional
                     with its recipes, which name the differences between versions
.claude-plugin/      the Claude Code marketplace: one plugin per version,
                     written by tools/build_catalog.py from the folders
install.sh           the installer above
tools/               the generators, not part of any skill:
  build_guidelines.py  builds the guideline skills from Odoo's 20.0 skills; guidelines/ is its
                       code, one class per file it writes, and guidelines/templates/ the text
  build_reference.py   builds odoo-reference from .odoo/src/<version>; reference/ is its code
  build_catalog.py     writes the marketplace; catalog/ is its code
  build_coverage.py    measures what the skills cover against each version's source, into
                       COVERAGE.md; coverage/ is its code, recipes.toml and technical.toml its data
  upstream.py          lists Odoo's commits to its own skills since the one ours follow
```

The `odoo/<version>/` skills are generated; change `tools/`, not the files. The text of
each guideline file is a Markdown template in `tools/guidelines/templates/`, where `$name`
marks what differs between versions; the class of the same name in
`tools/guidelines/documents/` says what it is in each version. To regenerate after Odoo
updates its skills:

```bash
git clone --depth 1 -b 20.0 --filter=blob:none --sparse https://github.com/odoo/odoo.git .odoo/src/20.0
git -C .odoo/src/20.0 sparse-checkout set skills
python3 tools/build_guidelines.py .odoo/src/20.0/skills .
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
python3 tools/build_reference.py
```

`tools/reference/check.py` checks the reference against a running Odoo of each version:
it installs a broad set of apps in a throwaway database, scans the same source, and
compares every model, field (type and target), XML id and Settings field with Odoo's own
registry and data. Run it inside `odoo-bin shell` with `tools` on the path:

```python
from pathlib import Path
from reference.check import ReferenceCheck
print(ReferenceCheck(env, Path("/usr/lib/python3/dist-packages")).run())
```

Check every version-specific change in that branch's source before making it:
`.odoo/` is ignored by git and is the place for those checkouts.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md). If a skill tells an agent to do something unsafe,
report it privately as [SECURITY.md](SECURITY.md) explains.

## Credits and license

Derived from Odoo's skill library (odoo/odoo, branch 20.0, `skills/`), by Odoo S.A.,
licensed LGPL-3; this work is LGPL-3 as well: [LICENSE](LICENSE), with the GNU GPL v3 it
incorporates in [licenses/GPL-3.0.txt](licenses/GPL-3.0.txt). Not affiliated
with or endorsed by Odoo S.A.

Maintained by [dooservice](https://dooservice.sh), which uses them in the AI console of
its Odoo hosting platform.
