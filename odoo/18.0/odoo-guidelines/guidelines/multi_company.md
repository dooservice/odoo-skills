# Make a model multi-company

A model whose records belong to a company declares `company_id`, checks that
the records it links belong to the same company, and hides other companies'
records with a company record rule.

```python
class LibraryBook(models.Model):
    _name = 'library.book'
    _check_company_auto = True

    company_id = fields.Many2one(
        'res.company', required=True, index=True,
        default=lambda self: self.env.company,
    )
    shelf_id = fields.Many2one('library.shelf', check_company=True)
```

- `company_id` defaults to `self.env.company`. Make it `required=True` when a
  record always belongs to one company; leave it optional when an empty
  company means "shared by all companies".
- A record shared by some companies only has a `company_ids` many2many instead,
  and its rule tests `company_ids`.
- `_check_company_auto = True` makes `create` and `write` call
  `_check_company()`, which raises when a `check_company=True` field points to
  a record of another company. Without it, call `self._check_company()` in
  the methods that link records.
- `check_company=True` also adds the company condition to the field's own
  `domain` in forms, built from the comodel's `_check_company_domain`.
- A comodel shared between a company and its branches sets
  `_check_company_domain = models.check_company_domain_parent_of`; a comodel
  with `company_ids` instead of `company_id` is handled as well.
- A model without `company_id` whose records depend on one (a line of a book)
  takes it as `related='book_id.company_id', store=True` so rules and
  `check_company` can use it.

# Restrict records to the allowed companies

Every model with `company_id` gets a company record rule that every
user receives, so a user sees only the companies selected in the company
switcher.

```xml
<record id="library_book_rule_company" model="ir.rule">
    <field name="name">Library books: multi-company</field>
    <field name="model_id" ref="model_library_book"/>
    <field name="domain_force">[('company_id', 'in', company_ids)]</field>
</record>
```

The rule has no `groups`, so it is global: it applies to every user, AND-ed
with every other rule.

- `company_ids` is the list of companies the user has selected (the
  `allowed_company_ids` context key), and `company_id` the current one; never
  write the rule on `user.company_id`, the user's default company.
- Append `+ [False]` only when an empty `company_id` means "shared"; on a
  required `company_id` it is noise.
- Branches (`res.company.parent_id`) are separate companies: `company_ids`
  holds a branch only when it is selected. To show a parent's records in its
  branches, write the domain with `('company_id', 'parent_of', company_ids)`.

# Work in the right company in code

- `self.env.company` is the current company and `self.env.companies` the
  selected ones. `self.env.user.company_id` is only the user's default company:
  never use it as the current one.
- `records.with_company(company)` puts `company` first in `allowed_company_ids`:
  use it before creating records for another company, reading
  `company_dependent` fields or computing taxes and accounts for that company.
- A scheduled action runs with the user's default company only: loop over the
  companies it must handle and call `with_company(company)` for each.
- `company_dependent=True` fields hold one value per company, read and written
  for `self.env.company`. They are stored as a JSON column keyed by
  company, with the `ir.default` value as fallback; a required or translated
  company-dependent field is not supported.
- Pass `allowed_company_ids` in the context of RPC calls that create or read
  company records; without it the integration user's default company applies.
