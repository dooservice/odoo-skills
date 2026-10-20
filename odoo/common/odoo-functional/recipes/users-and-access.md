# Users, groups and access

A user (`res.users`) logs in and acts with the rights of their groups (`res.groups`).
Groups grant access to models (create, read, write, delete) and carry record rules that
filter which rows of a model the user reaches. Internal users work in the back end;
portal users only see their own documents on the portal. Everything here is in `base`
and `portal`; login with external providers, two-factor policies and LDAP are left out.
Access changes need the user's yes: they decide what people can see and do.

## Before you start

- Apps: `base`; `portal` for portal users; `auth_signup` sends the invitation.
- Settings: none to switch on. Creating groups, access rights and record rules in the
  interface needs developer mode.
- Read first:

```python
groups_field = 'group_ids' if 'group_ids' in env['res.users'] else 'groups_id'   # 19.0+ / up to 18.0
for u in env['res.users'].search([('share', '=', False)]):
    print(u.login, u.company_id.name, sorted(u[groups_field].mapped('full_name')))
```

`user.has_group('sales_team.group_sale_manager')` works in every version, implied groups
included.

## The standard flow

Odoo's order: create the user with their access level per application, adjust specific
permissions when needed, give customers portal access from their contact, and create a
group only for a need no standard group covers. People who leave are archived.

1. **Create the internal user.** Settings ‣ Users section ‣ Manage Users ‣ New, which
   opens Settings ‣ Users & Companies ‣ Users. Name, email, Companies and Default
   Company; in the Access Rights tab, one level per application.

   ```python
   company = env.company
   user = env['res.users'].create({
       'name': '<full name>',
       'login': '<email>',
       'email': '<email>',
       'company_id': company.id,
       'company_ids': [(6, 0, [company.id])],
   })
   user.write({groups_field: [
       (4, env.ref('sales_team.group_sale_salesman').id),
       (4, env.ref('account.group_account_invoice').id),
   ]})
   env.cr.commit()
   ```

   Leaves an active internal user, invited by email to set a password.

   - Creating a user with an email sends the invitation to set a password (module
     `auth_signup`). Never set or send a password. The invitation is sent at once, not
     queued: if the mail server fails, the user is still created, without invitation,
     and nothing shows in the mail queue. To send it again once mail works:
     `user.action_reset_password()`. In a neutralized copy the email does not leave.
   - A new user starts with the default groups: those of the template user
     (`base.default_user`) up to 18.0; Internal User plus the groups implied by
     `base.default_user_group` from 19.0. Up to 18.0 the template often carries
     application administrator groups: read the new user's groups after creating and
     remove what the person should not have. Add application groups with `(4, id)`;
     replacing the list with `(6, 0, ids)` drops the default ones.
   - An internal user usually counts as a paid user in an Odoo subscription; ask before
     creating one.
   - Application groups imply the lower ones: `sales_team.group_sale_manager` includes
     `sales_team.group_sale_salesman_all_leads`, which includes
     `sales_team.group_sale_salesman`. Give the one level the person needs. Find groups
     under `## res.groups` in `odoo-reference/xmlids/<addon>.md`.
   - 20.0: the user form has a `role` (`light_user`, `regular_user`, `group_system`),
     computed from the groups. Light users only hold light groups; giving a regular
     application group makes a regular user.

2. **Adjust specific permissions.** In developer mode, the same user form lists every
   group (the Technical Access Rights tab from 19.0). Add or remove one group on the
   groups field: `(4, id)` adds, `(3, id)` removes.

   Leaves the user with that group and the groups it implies. Up to 18.0 the field also
   holds implied groups, and a group implied by another group the user keeps stays:
   remove the higher group too, then check with `user.has_group(...)`.

3. **Give a customer or vendor portal access.** Contacts ‣ the contact ‣ Actions ‣ Grant
   portal access ‣ Grant Access.

   ```python
   partners = env['res.partner'].search([('email', 'in', ['buyer@client.example'])])
   wizard = env['portal.wizard'].create({'partner_ids': [(6, 0, partners.ids)]})
   for line in wizard.user_ids:
       line.action_grant_access()
   env.cr.commit()
   ```

   Leaves a portal user (`base.group_portal`) for each contact, invited by email, who
   sees their own quotations, orders and invoices. A user is either internal
   (`base.group_user`), portal (`base.group_portal`) or public, never two. Revoke from
   the same wizard (`action_revoke_access`).

4. **Create a group for a need no standard group covers** (for example, read-only
   access to sales). In developer mode, Settings ‣ Users & Companies ‣ Groups ‣ New;
   the Access Rights tab gives the models, the Users tab the people. Never widen a
   standard group: every user in it changes.

   16.0 to 19.0, the Access Rights tab is `model_access`:

   ```python
   group = env['res.groups'].create({
       'name': 'Sales: read only',
       'model_access': [(0, 0, {
           'name': f'{model} read only',
           'model_id': env['ir.model']._get_id(model),
           'perm_read': True,
       }) for model in ('sale.order', 'sale.order.line')],
   })
   env.cr.commit()
   ```

   20.0, it is `access_ids` (model `ir.access`):

   ```python
   group = env['res.groups'].create({
       'name': 'Sales: read only',
       'access_ids': [(0, 0, {
           'name': f'{model} read only',
           'model_id': env['ir.model']._get_id(model),
           'operation': 'r',            # any subset of 'crud': 'r', 'ru', 'cru', 'crud'...
       }) for model in ('sale.order', 'sale.order.line')],
   })
   env.cr.commit()
   ```

   Leaves a group with read access to those models. Add the users with the groups field
   of step 2. The user still needs `base.group_user` and the menus to reach the
   records; a menu shows when the user has one of its groups (`groups_id` on
   `ir.ui.menu` up to 18.0, `group_ids` from 19.0) or it has none.

5. **Filter rows with a record rule**, when the group must see only part of a model. The
   group's Record Rules tab ‣ Add a line. A rule filters rows with a domain evaluated
   per user (`user`, `company_ids` are available). 16.0 to 19.0:

   ```python
   group.write({'rule_groups': [(0, 0, {
       'name': 'Read-only sales: own team only',
       'model_id': env['ir.model']._get_id('sale.order'),
       'domain_force': "[('team_id', 'in', user.crm_team_ids.ids)]",
       'perm_read': True, 'perm_write': True, 'perm_create': True, 'perm_unlink': True,
   })]})
   env.cr.commit()
   ```

   20.0: the same filter is the `domain` of the group's `ir.access` record.

   ```python
   group.access_ids.filtered(lambda a: a.model_id.model == 'sale.order').write({
       'domain': "[('team_id', 'in', user.crm_team_ids.ids)]",
   })
   env.cr.commit()
   ```

   Leaves the group's users reaching only the matching rows.

6. **Remove access when someone leaves.** Settings ‣ Users section ‣ Manage Users,
   select the user, Actions ‣ Archive.

   ```python
   user.active = False
   env.cr.commit()
   ```

   Leaves the user unable to log in; their documents, messages and history stay. Archive,
   never delete. Never archive the administrator.

## Variations

- **Rules on their own.** Settings ‣ Technical ‣ Security ‣ Record Rules (developer
  mode) lists every rule; `env['ir.rule'].create({..., 'groups': [(6, 0, [group.id])]})`
  is the same as the group's tab. Up to 19.0 access rights also have their own menu,
  Settings ‣ Technical ‣ Security ‣ Access Rights (`ir.model.access` with `group_id`);
  in 20.0 that menu lists `ir.access`.
- **Standard rules first.** Standard rules already cover the common cases:
  `sales_team.group_sale_salesman` sees its own orders and unassigned ones;
  `..._all_leads` sees all. Choosing the right standard group beats a new rule.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Users | Settings ‣ Users & Companies ‣ Users | same | same | same | same |
| Groups (developer mode) | Settings ‣ Users & Companies ‣ Groups | same | same | same | same |
| Access rights menu | Settings ‣ Technical ‣ Security ‣ Access Rights (`ir.model.access`) | same | same | same | same menu, `ir.access` |
| Record rules menu | Settings ‣ Technical ‣ Security ‣ Record Rules | same | same | same | none: `domain` on `ir.access` |
| User's groups | `groups_id` (implied included) | same | same | `group_ids` (explicit); `all_group_ids` (with implied) | same as 19.0 |
| Group's users | `users` | same | same | `user_ids`; `all_user_ids` | same as 19.0 |
| Group's application | `category_id` | same | same | `privilege_id` → `res.groups.privilege` (`category_id`) | same as 19.0 |
| Group's access and rules | `model_access`, `rule_groups` | same | same | same | `access_ids` |
| Default groups of a new user | template user `base.default_user` | same | same | `base.default_user_group` | same as 19.0 |
| User role | none | none | none | none | `role` |
| Menu groups | `groups_id` | same | same | `group_ids` | same as 19.0 |

## Verify

```python
Orders = env['sale.order'].with_user(user)
print(Orders.search_count([]), env['sale.order'].search_count([]))
if hasattr(Orders, 'has_access'):                                    # 18.0+
    print(Orders.has_access('write'))
else:                                                                # 16.0, 17.0
    print(Orders.check_access_rights('write', raise_exception=False))
```

Then ask the person to log in and try the action. To explain an access error, see
`diagnosis.md`.

## Pitfalls

- **Rules of the user's groups are OR-ed.** A rule on one group never narrows what
  another group of the same user already grants. Adding a rule to a group that has
  rules on that model widens it.
- **Rules without a group apply to everyone.** Global rules (or in 20.0 an `ir.access`
  without group) are AND-ed and apply to everyone, administrators included. Avoid them
  for business needs.
- **Standard rules and accesses come back.** A module update rewrites them unless
  `noupdate`: change the users' groups, not the standard rules.
- **Too many default groups.** Up to 18.0 a new user can inherit administrator groups
  from the template user: read the groups after creating.
- **No invitation.** The mail server failed when the user was created; resend with
  `user.action_reset_password()` once mail works.
