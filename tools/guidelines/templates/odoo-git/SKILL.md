---
name: odoo-git
description: >-
  Commit and pull request conventions for an Odoo project repository: the
  [TAG] module: header, a why-first body and where each part of it comes
  from, reference trailers, one logical change per commit, submodules,
  branches and pull requests. Use when committing, writing or amending a
  commit message or a pull request description, or publishing work.
---

# Commits and pull requests

For a project's Odoo repository: its own modules, and the repositories it brings in
as submodules. Commits follow Odoo's own message convention. If the environment you
work in has its own way to publish (a platform skill says so), use it instead of
`git push`.

## Commit message

A commit message is a header `[TAG] module: summary`, a blank line, a body that
says **why** the change is made, and reference trailers last, one per line.

```
[FIX] bookshop: keep open orders visible after a book is archived

Steps to reproduce:
- Archive a book that still has open orders
- Open the customer's portal page

The open orders of that book are gone from the page, so the customer
loses track of what they are still waiting for. They should stay listed
until they are delivered.

The order list was searched through the book with the default active
filter, so archiving the book filtered its orders out.

After this commit, the order list searches orders directly, with
active_test disabled on the book relation, so an archived book still shows
its open orders until they are delivered.

Fixes #123
```

```
[IMP] bookshop, *: bugfix and improvements

Fixed the order list and improved the portal page. Also updated the tests.
```

The second message mixes fixes with improvements, uses a vague noun phrase
for the summary, and says what changed without explaining why.

### Header

- Write `[TAG]`, a space, the scope, a colon, a space, then the summary. The scope
  is the module's technical name. Several modules: `[FIX] bookshop, bookshop_portal:`.
  Many modules: the main one then `*` (`[REF] bookshop, *:`), or `*` alone for a
  transversal change; the body then lists the modules the `*` stands for.
- Make the summary complete the sentence "if applied, this commit will ...": an
  imperative verb, no trailing period, about 50 characters.
- Keep the whole header to about 70 characters (closer to 80 when the module name
  is long).
- Never use "bugfix", "improvements" or "changes" as a summary.
- Tags:

  | Tag | Use |
  | --- | --- |
  | `[FIX]` | bug fix |
  | `[IMP]` | incremental improvement |
  | `[REF]` | refactoring, a feature heavily rewritten |
  | `[ADD]` | new module |
  | `[REM]` | removed resources: dead code, views, modules |
  | `[MOV]` | files or code moved without content change, so history follows |
  | `[REV]` | revert of an earlier commit |
  | `[PERF]` | performance: speed, memory, query or RPC count |
  | `[CLN]` | cleanup |
  | `[LINT]` | lint pass |
  | `[I18N]` | translation files |
  | `[MIG]` | migration of a module to $version |
  | `[REL]` | release |
  | `[MERGE]` | merge commit |

### Body

The diff gives the what. The rest of the message comes from outside it: the
why and who it affects from the task, ticket, or reporter; the reported
scenario from the ticket; benchmark figures from a measurement; the reason
for a revert from the regression it answers. Reading the code tells you what
it can do wrong, never what was reported.

- Ask the author for what the message needs and the conversation does not hold:
  for a fix, the ticket or issue and the reported scenario; for a feature, the
  task and who asked for it.
- When the answer is not at hand, write from what the code and the tests show,
  then tell the author which parts are derived and which are missing, and offer
  to amend.
- Never present a scenario inferred from the code as the reported bug: a
  plausible guess presented as the report is worse than a question.
- Write the why first: the purpose of the change, what was wrong for whom.
  Describe the what only for a technical choice, and then say why that choice.
  "The customer asked for it" is not a why.
- For a feature or an improvement, describe what it does and for whom.
- For a bug fix, give the steps that reproduce the bug: what to do, what happens,
  what should happen. Lead with the reported case; the test shows which cases the
  fix covers, and the other ones can follow. A fix message without the reported
  steps is not finished.
- Use "Before this commit, ... After this commit, ..." for the why and the outcome
  when it fits.
- For a `[PERF]` commit, add a Benchmark section: the workload and the relevant
  record counts, before/after measurements, and the speedup or reduction for the
  metric improved, with several dataset sizes when they show scaling. Take the
  figures from a run, yours or the author's; ask for them when you have none.
- Wrap at about 72 characters. Be complete rather than short: the message is the
  whole change for most readers, and a linked ticket is not readable by all of
  them. Several paragraphs is normal.
- Use ASCII punctuation only, header included: no em dash, curly quotes or
  ellipsis character; see [Plain ASCII punctuation in comments and messages](../odoo-guidelines/guidelines/comments.md#plain-ascii-punctuation-in-comments-and-messages).
- Write the message in English unless the repository's history is in another
  language.

### Trailers

- Put each reference on its own line after the body, in the form the repository's
  history uses: the task or ticket, `Fixes #123` for an issue this commit closes,
  `Co-authored-by: Name <email>`.
- Ask the author for the task, ticket, or issue; link what exists and leave the
  trailer out otherwise. Never invent a reference.
- Keep the metadata that tooling adds (merge and release messages, generated
  trailers) as it is.

## Commits

- Make one logical change per commit, and one module per commit unless the change
  is inseparable.
- Commit a move on its own as `[MOV]`, before the `[REF]` that edits the moved code.
- Commit a change inside a submodule **in the submodule first**, then in the
  project (`git add <submodule path>`), so the project points at it.
- Never change the configured git identity (`user.name`/`user.email`).
- Never commit generated files, secrets, dumps or `__pycache__`.

## Branches and pull requests

- Create one branch per change, from the branch it will be merged into, named
  `<target>-<topic>` (`$version-order-archive-fix`).
- Update the target locally with `git fetch origin <target>:<target>`, rebase the
  branch on it, and push with `--force-with-lease`; when the push is rejected
  because the remote branch moved, `git pull --rebase` the branch first. Never
  merge the target into the branch.
- Rebase on the target before submitting and whenever it conflicts; squash fixups
  into the commit they fix. A pull request carries only the commits that should
  land, never "address review" commits or merge commits.
- Follow [Changes in a stable version](../odoo-guidelines/guidelines/stable.md#changes-in-a-stable-version)
  for a fix to a module version already installed in a database that matters.
- Write the description as the commit message: why, which modules it touches, how
  to test it, whether it needs a module update or a migration, and the task,
  ticket, or issue when one exists. Write it in the reader's language.
- Add a test that reproduces the bug to a fix, when one is possible.
- Open a pull request in the submodule's repository for a change inside a
  submodule, and merge it before the project's, or the project points at a commit
  nobody can fetch.
