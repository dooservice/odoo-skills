# Access rights

Odoo 19.0 has two layers: **access rows** (`ir.model.access`) say which groups may
read, write, create or unlink a model at all; **record rules** (`ir.rule`) restrict
which records. Both are needed for anything sensitive.

- `security/ir.model.access.csv` columns:
  `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`.
  The id is `access_<model>_<group>`; `model_id:id` is `model_<model_with_underscores>`.
- Default deny: a model with no access row is inaccessible to everyone but the
  superuser, and the module logs a warning at install. Every new model gets at
  least one row.
- An access row with an empty group applies to **everyone**, portal and public
  included; flag any write/create/unlink granted that way, or to
  `base.group_portal` / `base.group_public`.
- Record rules (`ir.rule`, in `security/<module>_security.xml`): rules **with**
  groups are OR-ed together for the user's groups; **global** rules (no group)
  are AND-ed onto every user and can lock everyone out. Set `perm_read`,
  `perm_write`, `perm_create`, `perm_unlink` deliberately.
- Multi-company models need a global rule with a company domain:
  `[('company_id', 'in', company_ids)]` (append `+ [False]` when the company is
  optional).
- Groups (`res.groups`) belong to an application through `privilege_id` (a `res.groups.privilege`); a group
  that implies another uses `implied_ids`.

For auditing beyond the data files (`sudo()`, SQL, public methods, ...), use the
`odoo-security` skill.
