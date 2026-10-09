---
name: odoo-review
description: >-
  Review Odoo 18.0 addon code against the house rules, dispatching each changed
  file to the matching odoo-guidelines, odoo-web-guidelines, and
  odoo-security material. Use when reviewing a diff, commit, PR, or module.
---

# Reviewing Odoo code

A review has two passes. The house rules, which live in three sibling skills
next to this skill's base directory and are read fresh for every review, are
the floor. The change is then judged on its merits, as its author's most
sceptical colleague would; that pass finds most of the blocking defects.

| Sibling skill | Covers |
| --- | --- |
| `../odoo-guidelines/SKILL.md` | every file outside `static/`; its table maps file types to sections in `guidelines/` |
| `../odoo-web-guidelines/SKILL.md` | every file under `static/`: JavaScript, Owl templates, SCSS, hoot tests |
| `../odoo-security/SKILL.md` | controllers, `ir.model.access` rows, `ir.rule`, `sudo()`, raw SQL, `eval`, public or RPC-callable methods |

## Process

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

This is Odoo 18.0. Before flagging or writing an API or attribute,
check the version table, and when it is silent confirm the API exists in the
Odoo 18.0 source (`grep -rn`) rather than trusting memory:
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
