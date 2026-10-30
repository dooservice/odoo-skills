Key names in 20.0: one `ir.access` model in `ir.access.csv` (`operation` `crud`, a `domain`) replaces `ir.model.access` and `ir.rule`; groups with `privilege_id`, users `group_ids`; `base.group_everyone`; `records.check_access('write')`; fields `groups=`; `sudo()` after a check.

Sections of this file:

- [Access rights](#access-rights)
- [Grant every model access explicitly](#grant-every-model-access-explicitly)
- [Restrict records with domains](#restrict-records-with-domains)
- [Declare groups per application](#declare-groups-per-application)
- [Check group membership in code](#check-group-membership-in-code)
- [Restrict fields with `groups=`](#restrict-fields-with-groups)
- [Use `sudo()` only after an explicit check](#use-sudo-only-after-an-explicit-check)

# Access rights

Odoo 20.0 unifies the old `ir.model.access` ACLs and `ir.rule` record rules into
a single `ir.access` model, declared in `security/ir.access.csv` with columns
`id,name,model_id,group_id/id,operation,domain`. `ir.model.access` and
`ir.rule` no longer exist.

- Security files live in `security/` and load in this order in the manifest's
  `data`: the groups (`<module>_groups.xml`), then
  `ir.access.csv`, then the XML records that use the groups.
- Every new model, `TransientModel` wizards included, gets its access rows in
  the same commit.
- Grant the least each group needs, and give the application's manager group
  everything its user group has, through `implied_ids`.
- Hiding a menu, a button or a view element with `groups=` is presentation,
  not security: the model stays reachable by RPC with the same rights.

For auditing beyond the data files (`sudo()`, SQL, public methods, ...), use the
`odoo-security` skill.

# Grant every model access explicitly

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
- Rows can also be XML records (`model="ir.access"`) when the domain is long.

# Restrict records with domains

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
- Rows never apply to the superuser or in `sudo()`.

# Declare groups per application

A module's groups belong to an application through `privilege_id` (a
`res.groups.privilege`, itself in an `ir.module.category`), ordered by
`sequence`, and each level implies the one below.

```xml
<record id="res_groups_privilege_library" model="res.groups.privilege">
    <field name="name">Library</field>
    <field name="category_id" ref="base.module_category_services"/>
</record>
<record id="group_library_user" model="res.groups">
    <field name="name">User</field>
    <field name="sequence">10</field>
    <field name="privilege_id" ref="res_groups_privilege_library"/>
    <field name="implied_ids" eval="[Command.link(ref('base.group_user'))]"/>
</record>
<record id="group_library_manager" model="res.groups">
    <field name="name">Administrator</field>
    <field name="sequence">20</field>
    <field name="privilege_id" ref="res_groups_privilege_library"/>
    <field name="implied_ids" eval="[Command.link(ref('group_library_user'))]"/>
    <field name="user_ids" eval="[Command.link(ref('base.user_admin'))]"/>
</record>
```

- `res.users.group_ids` holds only the groups given explicitly, and
  `res.groups.user_ids` only the users given explicitly; search and compare on
  `all_group_ids` / `all_user_ids`, which add the implied ones.
- The user form shows one choice per privilege; there are no generated
  `sel_groups_`/`in_group_` fields any more.
- `base.group_everyone` is implied by the user, portal and public groups:
  it is how a row grants something to every user.

# Check group membership in code

Test a group through the user and its full external id; never compare group
names or database ids, which differ between databases.

- `self.env.user.has_group('library.group_library_manager')` tests one group.
- `self.env.user.has_groups('library.group_library_manager,!base.group_portal')`
  tests a comma-separated list where `!` negates a group. `user_has_groups` no
  longer exists.
- Both apply the debug-mode rule of `base.group_no_one` (technical features).

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
  `has_field_access(record._fields['field_name'], 'read')` or
  `check_field_access(...)`, which take the field object, not its name.

# Use `sudo()` only after an explicit check

`sudo()` bypasses access rows, record rules and field `groups`; call it on the
narrowest expression, after checking what the current user may do.

- Check first: `records.check_access('write')` (or `has_access` for a
  boolean, `_filtered_access` to keep the allowed records), or a group with
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
