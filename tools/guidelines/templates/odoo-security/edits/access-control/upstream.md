## Access control

Mechanics of `ir.access` rows and field `groups` are in the `odoo-guidelines`
skill ([Access rights](../odoo-guidelines/guidelines/security.md#access-rights),
[Fields](../odoo-guidelines/guidelines/fields.md#fields)); audit `security/` with
the attacker's reading:

- Flag any `c`/`u`/`d` operation granted to `base.group_everyone`,
  `base.group_portal`, or `base.group_public`; scrutinize even `r` on models
  holding personal or business-sensitive data.
- A permission row's `operation` set is what it grants; a *restriction*
  (group-less) row covering only some operations leaves the others governed by
  the permission rows alone: if any permission grants `write`, an attacker
  can alter records the read restriction hides (`write` checks write access
  only, never read). Cover **all** CRUD operations that need restricting.
- Multi-company models need a company restriction row; sensitive models need
  domain restrictions, not just group permissions.
