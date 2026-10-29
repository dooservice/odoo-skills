"""`ir.access` rows of `security.md`, the single access model of 20.0."""

from __future__ import annotations


class UnifiedAccess:
    """One model: rows with a group grant, rows without one restrict."""

    layers = """\
Odoo 20.0 unifies the old `ir.model.access` ACLs and `ir.rule` record rules into
a single `ir.access` model, declared in `security/ir.access.csv` with columns
`id,name,model_id,group_id/id,operation,domain`. `ir.model.access` and
`ir.rule` no longer exist."""

    rows = """\
Give every model at least one permission row; a model without one is
inaccessible to everyone but the superuser, and nothing warns at install: test
the module as a non-admin user.

```
id,name,model_id,group_id/id,operation,domain
access_library_book_user,library.book user,library.book,base.group_user,r,
access_library_book_manager,library.book manager,library.book,library.group_library_manager,crud,
library_book_company,library.book multi-company,library.book,,crud,"[('company_id', 'in', company_ids + [False])]"
```

- `model_id` is the model name itself, not an `ir.model` external id; the group
  column is `group_id/id`.
- `operation` is required: a subset of `crud` letters (`r`, `cru`, `crud`, ...);
  a row applies to exactly the operations it lists.
- Default deny: granting to everyone (portal and public included) is done via
  `base.group_everyone`; flag any `c`/`u`/`d` granted to `base.group_everyone`,
  `base.group_portal`, or `base.group_public`.
- Rows can also be XML records (`model="ir.access"`) when the domain is long."""

    rules = """\
Restrict which records a group sees with the `domain` of its `ir.access` rows;
a record rule is an `ir.access` record, never `model="ir.rule"`.

```xml
<record id="library_book_rule_reader_company" model="ir.access">
    <field name="name">library.book: reader, own companies</field>
    <field name="model_id" ref="model_library_book"/>
    <field name="group_id" ref="library.group_reader"/>
    <field name="operation">r</field>
    <field name="domain">[('company_id', 'in', company_ids)]</field>
</record>
```

- The optional `domain` restricts the row to matching records (what record rules
  used to do).
- Rows **with** a group are *permissions*: OR-ed together (union over the
  user's groups); a row's domain limits only what that row grants. Rows
  **without** a group are *restrictions*: AND-ed onto **every** user; they
  never grant anything, and non-overlapping restrictions can lock everyone out.
- "Own records only" is a permission row with a domain for the user group;
  the manager group gets a row without domain, which grants everything.
- `domain` is evaluated with `user`, `time`, `company_ids` and `company_id`.
  The `access` operator delegates to a related record:
  `('shelf_id', 'access', 'read')` keeps the books whose shelf the user can read.
- Rows never apply to the superuser or in `sudo()`."""
