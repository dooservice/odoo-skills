# Plain ASCII punctuation in comments and messages

Write code comments, docstrings, user-facing strings and commit messages with
ASCII punctuation only. The character that keeps showing up is the em dash
(`—`): replace it with a comma, a colon, a semicolon, parentheses, or two
sentences, whichever the sentence actually needs. Same for the en dash (`–`),
curly quotes (`“ ” ‘ ’`) and the ellipsis character (`…`): write `-`, `"`, `'`
and `...`.

```python
# bad
# recompute the totals — the taxes may have changed
raise UserError(_("Book %s is already borrowed — return it first", book.name))

# good
# recompute the totals: the taxes may have changed
raise UserError(_("Book %s is already borrowed, return it first", book.name))
```

## Why

- The em dash is not on the keyboard layouts code is written with, so in practice it
  arrives by copy-paste or from a generation tool. A diff full of them reads as text
  nobody typed.
- ASCII punctuation is greppable and diffable. A comment or a commit message is
  searched for with what a reviewer can type.
- A translatable literal is keyed on its exact source string, so two variants of the
  same sentence that differ only in the dash are two terms to translate (see
  [Translate only static literals](python.md#translate-only-static-literals)).

## Exceptions

- Data, not prose: a test fixture, a localization file, or a string whose content is
  the character itself.
- Existing translatable text in an installed module: rewording a term breaks its
  translations (see [Changes to an installed module](installed.md#changes-to-an-installed-module)).
