# Contributing

Corrections are welcome, above all for versions other than 20.0, where Odoo's own skills
say less.

## The rule: check it in the source

Every version-specific statement must be true in that branch of
[odoo/odoo](https://github.com/odoo/odoo). Before you change one, check it in the source
of that version, and say in the pull request where (file and line, or a link).

## Where to change what

| To change | Edit |
|---|---|
| `odoo/<version>/odoo-guidelines`, `odoo-web-guidelines`, `odoo-security`, `odoo-review`, `odoo-git` | `tools/generate_guidelines.py`, then regenerate |
| `odoo/<version>/odoo-reference` | `tools/reference/`, then regenerate with `tools/build_reference.py` |
| `odoo/common/odoo-upgrade` | the files directly |
| `dooservice/` | the files directly |

Do not edit generated files by hand: the next regeneration overwrites them. The README
explains how to check out Odoo's source and regenerate.

## Pull requests

- One change per pull request, for every version it applies to.
- Commit messages in English, one line, saying what the change fixes:
  `fix(17.0): odoo-guidelines uses _sql_constraints, not models.Constraint`.
- Run the generators and commit their output together with your change.

## Sign your commits

Every commit must carry a `Signed-off-by` line, which says you wrote the change or have
the right to submit it under this project's license, as the
[Developer Certificate of Origin](https://developercertificate.org) describes. Add it with
`git commit -s`.

## License

By contributing, you agree that your contribution is licensed under the
[LGPL-3.0](LICENSE), like the rest of the repository.
