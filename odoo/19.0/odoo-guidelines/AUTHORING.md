# Adding a guideline

## Files

- Guidelines live in `guidelines/`, one file per domain: `orm.md`, `xml.md`, `tests.md`,
  and a new file the day a domain has guidelines of its own.
- Inside a file, one guideline per `#` section. The title states the rule: "Batch ORM
  calls", not "Loops".
- Order inside a file means nothing. No rule outranks another.

## Two kinds of guideline: conventions and rules

- A **convention** is a choice that fits in one line and can be followed as stated.
  - Examples: `_id` suffix on a `Many2one`, one model class per file.
  - Needs no explanation.
  - Written as a bullet.
  - Conventions are grouped by topic, one section per topic.
- A **rule** needs an explanation to be applied correctly.
  - Written as its own section: the rule, then why it exists, then the cases where it
    does not apply.
  - A few sentences is the normal size. Sub-headings and code blocks are allowed, not
    required.
- Promote a convention to a rule when it keeps being violated even though the
  convention was loaded. That shows it needs the explanation.

## Writing the rule itself

- State the rule as something a reviewer can check against code with a yes or no.
  - Good: "no `create` call inside a loop".
  - Bad: "write efficient code".
- The why and the exceptions come after the rule. They do not replace a clear rule.
- Name the alternative. A rule that forbids something says what to write instead.

## Examples

- An example is optional. Add one when the rule is hard to state without it, and keep
  it schematic: the smallest tree or snippet that carries the concept.
- Show the same code both ways when seeing it break the rule is what makes the rule
  clear.
- Do not copy real code. Use schematic model names such as `library.book`, never a
  real one: a real name makes the guideline show up in every grep for that model.
- Do not point at real files or directories. Nothing checks them, and a stale
  reference is worse than none.

## Registering the guideline

- Add a row to the table in `SKILL.md`, through its template
  (`tools/guidelines/templates/odoo-guidelines/SKILL.md`).
- The "Read it when" cell names the files or the activity that should trigger reading
  the guideline. Not every edit of every file.
- The link points at the section title. Renaming a title changes the anchor, so update
  the row with it.

## Generating the guideline for every version

- Never edit a skill under `odoo/<version>/` by hand: the build overwrites it. A
  guideline file is a `Document` subclass in `tools/guidelines/documents/`, listed in
  `DOCUMENTS` of `tools/guidelines/build.py`; it either takes Odoo's file as it is or
  fills a template under `tools/guidelines/templates/odoo-guidelines/`.
- Write each guideline for every version the repository covers, 16.0 to 20.0. Put
  what differs in a template value picked per range of versions
  (`version.pick(v16_17=..., v18_=...)`), never in a sentence that lists versions.
- Check every version-specific statement (a name, an argument, a default, a tag) in
  the source of each version it is written for. A statement checked in one version
  is not checked in the others.
- Write ASCII punctuation only: the build refuses typographic characters.
- Regenerate every version with `python3 build_guidelines.py <odoo 20.0 skills> ..`
  from `tools/`, and read the diff of each version before committing.
