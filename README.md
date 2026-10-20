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
| **Developers** | `odoo-guidelines`, `odoo-web-guidelines`, `odoo-security`, `odoo-review`, `odoo-git`, `odoo-upgrade` | modules, ORM, views, controllers, JavaScript and Owl, security audits, code review, commits, porting between versions |
| **Functional consultants** | `odoo-functional` | configuring Odoo without code, in 26 recipes that follow Odoo's own flow step by step: from go-live, sales, purchase, inventory, manufacturing, point of sale and eCommerce to taxes, bank reconciliation, closing the period, users, automations and "why does Odoo do X" |
| **Each country** | `odoo-l10n-<country>` | the chart of accounts, taxes, identification, electronic invoicing and legal reports of one country, by people who implement Odoo there |
| **Everyone** | `odoo-reference` | every model, field, Settings switch and XML id of each version, generated from its source |

## How it is checked

- **Every recipe ran on a real database of each version.** Each step of `odoo-functional`
  was executed on Odoo 16.0, 17.0, 18.0, 19.0 and 20.0, and its effect read back; the
  steps follow Odoo's documentation of that version and the menus of that version.
- **The reference matches a running Odoo.** Every model, field, XML id and Settings field
  it lists was compared with Odoo's own registry, in each version: no mismatch.
- **Every version difference is checked in that branch's source**, with the file and line.
- **What it changes is measured.** `evals/` runs the same tasks with and without the
  skills; see [the results](#results).

The developer skills are adapted from Odoo's own skill library (20.0 branch), with every
version-specific statement checked against that branch's source.

## Results

The same tasks, given to Claude Sonnet 5.5 with and without the skills, three runs each.
Each task asks for a file (a view, a model, a controller, an `odoo-bin shell` script) and
checks that it uses what that Odoo version has and nothing it does not:

| Odoo | Tasks | With the skills | Without | Difference |
|---|---|---|---|---|
| 20.0 | 19 | **88.6%** | 69.2% | **+19.4 points** |
| 16.0 | 20 | **97.8%** | 96.3% | +1.5 points |

Models already know an older version like 16.0 well; the skills matter most on the newer
ones, where field names, security files, stock and accounting changed. On 20.0, scrapping
stock, time off types and fiscal positions went from 33% to 100%, and pricelists from 25%
to 83%. The cases, the graders and how to run them are in [`evals/`](evals/README.md);
tasks still below 98% are the next work.

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

## Localizations

The skills above hold for every country. What depends on one (its chart of accounts and
taxes, how contacts are identified, electronic invoicing, legal reports) lives in a skill
of its own, `odoo-l10n-<country code>`, written and maintained by people who implement
Odoo there. `odoo-functional` loads it when the database has that country's `l10n_*`
module installed, and `install.sh` installs it when your modules depend on one.

| Country | Skill | Maintained by |
|---|---|---|
| Peru | [`odoo-l10n-pe`](localization/pe/odoo-l10n-pe/SKILL.md) | Josué Salazar ([@Josuesp1620](https://github.com/Josuesp1620)), [Dooservice](https://dooservice.sh) |
| Yours | | [Add your country](CONTRIBUTING.md#add-your-country) |

Install one: `/plugin install odoo-l10n-<country code> --marketplace dooservice/odoo-skills`,
or `npx skills add dooservice/odoo-skills/localization/<country code>`.

**Add your country.** Copy `localization/template/odoo-l10n-xx/` to
`localization/<country code>/odoo-l10n-<country code>/`, fill in each section, name
yourself in `MAINTAINERS.md`, run `python3 tools/build_catalog.py`, and open a pull
request. [CONTRIBUTING.md](CONTRIBUTING.md#add-your-country) has the rules. You stay listed
here as its maintainer.

## Layout

```
odoo/<version>/      generated: odoo-guidelines, odoo-web-guidelines, odoo-security, odoo-review,
                     odoo-git (from Odoo's 20.0 skills) and odoo-reference (from that version's source)
odoo/common/         version-independent, written by hand: odoo-upgrade, and odoo-functional
                     with its recipes, which name the differences between versions
localization/        one skill per country, written by hand; template/ is the one to copy
.claude-plugin/      the Claude Code marketplace: one plugin per version and per country,
                     written by tools/build_catalog.py from the folders
install.sh           the installer above
tools/               the generators, not part of any skill:
  build_guidelines.py  builds the guideline skills from Odoo's 20.0 skills; guidelines/ is its
                       code, one class per file it writes, and guidelines/templates/ the text
  build_reference.py   builds odoo-reference from .odoo/src/<version>; reference/ is its code
  build_catalog.py     checks every localization and writes the marketplace; catalog/ is its code
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
