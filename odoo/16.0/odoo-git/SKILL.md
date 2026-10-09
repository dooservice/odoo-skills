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
  performance, `[I18N]` translations, `[MIG]` migration of a module to 16.0.
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

- One branch per change, named after it (`16.0-fix-delivery-date`), from the branch
  it will be merged into; rebase on that branch rather than merging it in.
- A pull request carries only the commits that should land: squash fixups into the
  commit they fix.
- The description says why, which modules it touches, how to test it, and whether it
  needs a module update or a migration. Write it in the reader's language.
- A change in a submodule needs a pull request in that submodule's repository too,
  merged before the project's, or the project points at a commit nobody can fetch.
