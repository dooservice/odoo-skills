"""`ir.model.access` rows and `ir.rule` records of `security.md`, up to 19.0."""

from __future__ import annotations


class LegacyAccess:
    """Two models: access rows grant per model, record rules filter records."""

    layers = """\
Odoo {version} has two layers: **access rows** (`ir.model.access`) say which groups may
read, write, create or unlink a model at all; **record rules** (`ir.rule`) restrict
which records. Both are needed for anything sensitive."""

    rows = """\
Give every model at least one row in `security/ir.model.access.csv`; a model
without rows is inaccessible to everyone but the superuser, and the install
logs a warning ("have no access rules").

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_library_book_user,library.book user,model_library_book,base.group_user,1,0,0,0
access_library_book_manager,library.book manager,model_library_book,library.group_library_manager,1,1,1,1
```

- The id is `access_<model>_<group>`; `model_id:id` is
  `model_<model_with_underscores>`.
- Rows add up: a user gets an operation when any row of any of its groups
  grants it. A row cannot take away what another row gives.
- A row with an empty group applies to **everyone**, portal and public
  included; flag any write/create/unlink granted that way, or to
  `base.group_portal` / `base.group_public`."""

    rules = """\
Restrict which records a group sees with `ir.rule` records in
`security/<module>_security.xml`.

```xml
<record id="library_book_rule_own" model="ir.rule">
    <field name="name">Library books: own loans only</field>
    <field name="model_id" ref="model_library_book"/>
    <field name="domain_force">[('user_id', '=', user.id)]</field>
    <field name="groups" eval="[Command.link(ref('library.group_library_user'))]"/>
</record>
```

- Rules **with** groups are OR-ed together for the user's groups; **global**
  rules (no group) are AND-ed onto every user and can lock everyone out. A
  user in none of a rule's groups is not restricted by it.
- A group rule restricts its own group only: when the user group gets an
  "own records" rule, the manager group needs its own rule with
  `[(1, '=', 1)]`, or managers inherit the restriction through `implied_ids`.
- `perm_read`, `perm_write`, `perm_create` and `perm_unlink` all default to
  true: uncheck the operations a rule must not cover.
- `domain_force` is a domain on the rule's model, may traverse relations, and
  is evaluated with {rule_context}.
- Rules never apply to the superuser or in `sudo()`."""
