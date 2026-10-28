---
name: odoo-review
description: >-
  Review Odoo 19.0 addon code against the house rules, dispatching each changed
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

1. **Scope.** Work in a local checkout of the revision under review: the
   working tree, a local branch tip, or a remote branch or pull request head
   checked out at its current commit. Pin that commit and the base it is
   compared against (`git merge-base HEAD origin/<target branch>`), and take
   the diff between the two from the checkout, never from a saved copy;
   branches move and pull requests get force-pushed. Every file the review
   reads, in the diff or around it, comes from that checkout, and the Odoo
   source it reads is the one the project runs (19.0); a checkout at
   another revision, however close, is not a source. Read each touched
   module's `__manifest__.py` for its purpose and `depends`, the commit
   messages, and the pull request description and comments when there is one.
   Note whether the module is already installed in a database that matters.
   A change inside a submodule is reviewed in that submodule, together with
   the project commit that points at it.
2. **Map.** List every changed file with the guideline sections that apply to
   it, taken from the sibling tables. Every file maps to at least one section:
   Python always gets Imports and Naming, anything under `static/` gets the web
   guidelines, a `tests/` file gets Tests, and a module already installed in a
   database that matters adds Changes to an installed module and Changes in a
   stable version to every file. A file left without a section is a mapping
   mistake to fix, never a file without rules.
3. **Read.** Open every mapped section, and the version table
   (`../odoo-guidelines/guidelines/version.md`), before writing the first
   finding. The files sit in the sibling `guidelines/` folders and are short;
   `cat` them whole.
4. **Rules pass.** Judge the diff against the sections read, then against
   what the diff never shows (below).
5. **Merits pass.** The rules are the floor, not the ceiling. For every changed
   hunk, hunt for the input or state that makes it wrong: edge values,
   rounding, timezones, empty and multi-record calls, multi-company,
   concurrency, the second run. Check that the commit message's claim is what
   the code does, that the tests would fail without the change, and what the
   change costs on real data. Give this pass the same legwork as the rules
   pass.
6. **Prove.** Update the module and run its tests on a database with realistic
   data (`odoo-bin -u <module> --test-enable --stop-after-init`): a review that
   never installed the change has not seen it fail.
7. **Report.** Each finding carries file and line, the defect, the concrete
   failure scenario, a fix, and the guideline section it applies, or
   *judgement* when it came from the merits pass. A finding that rests on
   code outside the diff names the revision it was read at. Close with a
   **Guidelines read:** line listing every section opened. Flag; fix only
   what is unambiguous.

The review is complete when every changed file is mapped, every mapped section
has been read, every hunk has had both passes, and every finding names its
section or its failure scenario.

## Installed modules and new code

In a module version already installed in a database that matters, the existing
file style supersedes the guidelines: keep the diff minimal, match the
surrounding code, and check the change against
[Changes in a stable version](../odoo-guidelines/guidelines/stable.md#changes-in-a-stable-version).
In new code or a new module version, apply the guidelines to new code, and to
existing code only when a file is under major change (do a separate *move*
commit first).

## Version traps

This is Odoo 19.0. Odoo's ORM and view/template syntax change between major
versions (`attrs=`, `<tree>`, `name_get`, `read_group` all changed or went
away in recent versions). Before flagging or writing an API or attribute,
check the version table, and when it is silent confirm the API exists in the
Odoo 19.0 source (`grep -rn` the ORM source or a usage) rather than
trusting memory: code written for another version is the most common defect
AI-written Odoo code has.

## Code the diff never shows

Odoo modules extend each other: standard ones, other repositories in the
addons path, and the project's own. Anything the diff changes may be consumed by
code it never shows: methods are overridden, fields and XML ids referenced,
templates called and inherited, data dictionaries and context keys produced
and read on both the Python and JavaScript sides. For each changed method,
field, template, key, or export, find its consumers across every directory in
the addons path and confirm they still hold.

- Overrides: `grep -rn "def <name>("` and read them. Do they still call
  `super()` with valid arguments, and does the new behaviour hold with their
  additions?
- Renamed or removed names: grep for them in Python, XML, and JavaScript. A
  stale reference in a view, a domain, an xpath, a `patch()`, or an import
  fails only at runtime, or only when that module is installed.
- Shared contracts: a template, a data dictionary, or a context key read in
  one place is produced in others. A new key or a changed requirement must be
  met by every producer, including the JavaScript twin of a Python one, or
  the callers the diff never touched break at render.
- Data already in the database: a renamed field, a changed selection or a
  removed XML id needs a migration (see the `odoo-upgrade` skill).
- In a module version already installed, treat a signature change as a bug on
  its own (see
  [Changes in a stable version](../odoo-guidelines/guidelines/stable.md#changes-in-a-stable-version)).
