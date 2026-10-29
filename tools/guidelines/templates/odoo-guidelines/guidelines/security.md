# Access rights

$layers

- Security files live in `security/` and load in this order in the manifest's
  `data`: the groups (`<module>_groups.xml`), then
  $access_file, then the XML records that use the groups.
- Every new model, `TransientModel` wizards included, gets its access rows in
  the same commit.
- Grant the least each group needs, and give the application's manager group
  everything its user group has, through `implied_ids`.
- Hiding a menu, a button or a view element with `groups=` is presentation,
  not security: the model stays reachable by RPC with the same rights.

For auditing beyond the data files (`sudo()`, SQL, public methods, ...), use the
`odoo-security` skill.

# Grant every model access explicitly

$access_rows

# Restrict records with domains

$record_rules

# Declare groups per application

$groups

# Check group membership in code

Test a group through the user and its full external id; never compare group
names or database ids, which differ between databases.

$group_checks

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
- $field_check

# Use `sudo()` only after an explicit check

`sudo()` bypasses access rows, record rules and field `groups`; call it on the
narrowest expression, after checking what the current user may do.

- Check first: $check_access, or a group with
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
