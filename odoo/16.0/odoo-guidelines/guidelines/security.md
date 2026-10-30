Key names in 16.0: access rows in `ir.model.access.csv` (`perm_read`...), record rules `ir.rule` with `domain_force`; groups with `category_id` and users `groups_id`; `has_group`; `records.check_access_rights('write')`; fields `groups=`; `sudo()` after a check.

Sections of this file:

- [Access rights](#access-rights)
- [Grant every model access explicitly](#grant-every-model-access-explicitly)
- [Restrict records with domains](#restrict-records-with-domains)
- [Declare groups per application](#declare-groups-per-application)
- [Check group membership in code](#check-group-membership-in-code)
- [Restrict fields with `groups=`](#restrict-fields-with-groups)
- [Use `sudo()` only after an explicit check](#use-sudo-only-after-an-explicit-check)

# Access rights

Odoo 16.0 has two layers: **access rows** (`ir.model.access`) say which groups may
read, write, create or unlink a model at all; **record rules** (`ir.rule`) restrict
which records. Both are needed for anything sensitive.

- Security files live in `security/` and load in this order in the manifest's
  `data`: the groups (`<module>_groups.xml`), then
  `ir.model.access.csv`, then the XML records that use the groups.
- Every new model, `TransientModel` wizards included, gets its access rows in
  the same commit.
- Grant the least each group needs, and give the application's manager group
  everything its user group has, through `implied_ids`.
- Hiding a menu, a button or a view element with `groups=` is presentation,
  not security: the model stays reachable by RPC with the same rights.

For auditing beyond the data files (`sudo()`, SQL, public methods, ...), use the
`odoo-security` skill.

# Grant every model access explicitly

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
  `base.group_portal` / `base.group_public`.

# Restrict records with domains

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
  is evaluated with `user`, `time`, `company_ids` and `company_id`.
- Rules never apply to the superuser or in `sudo()`.

# Declare groups per application

A module's groups belong to an application through `category_id` (an
`ir.module.category`), and each level implies the one below.

```xml
<record id="group_library_user" model="res.groups">
    <field name="name">User</field>
    <field name="category_id" ref="base.module_category_services"/>
    <field name="implied_ids" eval="[Command.link(ref('base.group_user'))]"/>
</record>
<record id="group_library_manager" model="res.groups">
    <field name="name">Administrator</field>
    <field name="category_id" ref="base.module_category_services"/>
    <field name="implied_ids" eval="[Command.link(ref('group_library_user'))]"/>
    <field name="users" eval="[Command.link(ref('base.user_admin'))]"/>
</record>
```

- Groups of one category that form an `implied_ids` chain show as one selection
  on the user form (generated fields `sel_groups_<ids>`); other groups show as
  check boxes (`in_group_<id>`). Never reference those generated fields: write
  `groups_id` on `res.users`, which also holds the implied groups.
- `users` on the group lists its members; `comment` explains what it grants.

# Check group membership in code

Test a group through the user and its full external id; never compare group
names or database ids, which differ between databases.

- `self.env.user.has_group('library.group_library_manager')` tests one group.
- `self.user_has_groups('library.group_library_manager,!base.group_portal')`
  tests a comma-separated list where `!` negates a group.
- `has_group('base.group_no_one')` is true for every internal user, debug mode
  or not; only `user_has_groups` applies the debug-mode rule of that group.

# Restrict fields with `groups=`

A field that only some users may see or change declares `groups=` on the field,
not only on the views that show it.

- `fields.Monetary(groups='library.group_library_manager')`: for users outside
  the group the field is left out of `fields_get` and removed from every view
  arch, and reading or writing it raises `AccessError`. Several groups are
  comma-separated; `!` excludes one.
- A compute, constraint or `create` override that reads a restricted field runs
  as the current user: read it on `self.sudo()` there, or every user outside the
  group gets an access error on an unrelated screen.
- `groups=` on a view element, a menu or a button only hides it; use it for
  clutter, and use field `groups` for data.
- To test field access in code, call
  `check_field_access_rights('read', ['field_name'])`: it raises
  `AccessError` on a refused field, and without names returns the readable ones.

# Use `sudo()` only after an explicit check

`sudo()` bypasses access rows, record rules and field `groups`; call it on the
narrowest expression, after checking what the current user may do.

- Check first: `records.check_access_rights('write')` then
  `records.check_access_rule('write')`, or a group with
  `self.env.user.has_group(...)`, or an access token for public pages.
- Records reached from a sudoed recordset are sudoed too
  (`book_sudo.author_id.partner_ids` bypasses rules all the way): name sudoed
  variables with a `_sudo` suffix and never return them to the client unread.
- `sudo()` keeps `self.env.user`; `create_uid`, `write_uid` and chatter
  authors stay the real user. To act as another user, use
  `with_user(user)`, which applies that user's rights.
- Never pass a domain, a model name or ids taken from the request to a sudoed
  `search` or `browse`: that turns the endpoint into a read-anything API.
- `sudo(False)` returns to the user's rights; `self.env.su` tells whether the
  current environment is sudoed.
