# Users, groups and access

A user (`res.users`) logs in and acts with the rights of their groups (`res.groups`).
Groups grant access to models (create, read, write, delete) and carry record rules that
filter which rows of a model the user reaches. Internal users work in the back end;
portal users only see their own documents on the website. Access changes need the
user's yes: they decide what people can see and do.

Read first:

```python
groups_field = 'group_ids' if 'group_ids' in env['res.users'] else 'groups_id'   # 19.0+ / up to 18.0
for u in env['res.users'].search([('share', '=', False)]):
    print(u.login, u.company_id.name, sorted(u[groups_field].mapped('full_name')))
```

## Version differences

| | 16.0–18.0 | 19.0 | 20.0 |
|---|---|---|---|
| User's groups | `groups_id` (implied groups included) | `group_ids` (explicit); `all_group_ids` (with implied) | same as 19.0 |
| Group's users | `users` | `user_ids`; `all_user_ids` | same as 19.0 |
| Group's application | `category_id` | `privilege_id` → `res.groups.privilege` (`category_id`) | same as 19.0 |
| Model access and row filters | `ir.model.access` + `ir.rule` | `ir.model.access` + `ir.rule` | one model, `ir.access` |

`user.has_group('sales_team.group_sale_manager')` works in every version, implied groups
included.

## A new internal user

```python
user = env['res.users'].create({
    'name': 'Ana Ríos',
    'login': 'ana@acme.example',
    'email': 'ana@acme.example',
    'company_id': company.id,
    'company_ids': [(6, 0, [company.id])],
})
user.write({groups_field: [
    (4, env.ref('sales_team.group_sale_salesman').id),
    (4, env.ref('account.group_account_invoice').id),
]})
env.cr.commit()
```

- Creating a user with an email sends the invitation to set a password (module
  `auth_signup`). Never set or send a password. To send it again:
  `user.action_reset_password()`. In a neutralized copy the email does not leave.
- A new user starts with the default groups: those of the template user
  (`base.default_user`) up to 18.0, those of `base.default_user_group` from 19.0. Add
  application groups with `(4, id)`; replacing the list with `(6, 0, ids)` drops them.
- An internal user usually counts as a paid user in an Odoo subscription; ask before
  creating one.
- Application groups imply the lower ones: `sales_team.group_sale_manager` includes
  `sales_team.group_sale_salesman_all_leads`, which includes
  `sales_team.group_sale_salesman`. Give the one level the person needs. Find groups under `## res.groups` in
  `odoo-reference/xmlids/<addon>.md`.
- 20.0: the user form has a `role` (`light_user`, `regular_user`, `group_system`),
  computed from the groups. Light users only hold light groups; giving a regular
  application group makes a regular user.

## Removing access

Archive, never delete: `user.active = False`. The user's documents, messages and history
stay. Remove a group with `(3, id)` on the groups field.

## Portal users

Give a contact access to their documents (quotations, invoices, tickets) on the portal:

```python
partners = env['res.partner'].search([('email', 'in', ['buyer@client.example'])])
wizard = env['portal.wizard'].create({'partner_ids': [(6, 0, partners.ids)]})
for line in wizard.user_ids:
    line.action_grant_access()
env.cr.commit()
```

This creates the user in `base.group_portal` and sends the invitation. A user is either
internal (`base.group_user`), portal (`base.group_portal`) or public, never two.

## A new group with limited access

For a need no standard group covers (for example, read-only access to sales), create a
group and give it model access. Never widen a standard group: every user in it changes.

```python
group = env['res.groups'].create({'name': 'Sales: read only'})
for model in ('sale.order', 'sale.order.line'):
    env['ir.model.access'].create({                       # 16.0–19.0
        'name': f'{model} read only',
        'model_id': env['ir.model']._get_id(model),
        'group_id': group.id,
        'perm_read': True,
    })
env.cr.commit()
```

20.0:

```python
for model in ('sale.order', 'sale.order.line'):
    env['ir.access'].create({
        'name': f'{model} read only',
        'model_id': env['ir.model']._get_id(model),
        'group_id': group.id,
        'operation': 'r',            # any subset of 'crud': 'r', 'ru', 'cru', 'crud'...
    })
```

The user still needs `base.group_user` and the menus to reach the records; a menu shows
when the user has one of its groups (`groups_id` on `ir.ui.menu` up to 18.0,
`group_ids` from 19.0) or it has none.

## Record rules

A rule filters rows with a domain evaluated per user (`user`, `company_ids` are
available). Up to 19.0:

```python
env['ir.rule'].create({
    'name': 'Read-only sales: own team only',
    'model_id': env['ir.model']._get_id('sale.order'),
    'groups': [(6, 0, [group.id])],
    'domain_force': "[('team_id', 'in', user.crm_team_ids.ids)]",
    'perm_read': True, 'perm_write': True, 'perm_create': True, 'perm_unlink': True,
})
env.cr.commit()
```

20.0: the same filter is the `domain` of the group's `ir.access` record.

- Rules of the user's groups are OR-ed: a rule on one group never narrows what another
  group of the same user already grants. Adding a rule to a group that has rules on that
  model widens it.
- Rules without a group (global, or in 20.0 an `ir.access` without group) are AND-ed
  and apply to everyone, administrators included. Avoid them for business needs.
- Standard rules already cover the common cases: `sales_team.group_sale_salesman` sees
  its own orders and unassigned ones; `..._all_leads` sees all.
- Standard rules and accesses can be rewritten by a module update unless `noupdate`:
  change the users' groups, not the standard rules.

## Verify

```python
Orders = env['sale.order'].with_user(user)
print(Orders.search_count([]), env['sale.order'].search_count([]))
print(Orders.check_access_rights('write', raise_exception=False))   # 16.0, 17.0
print(Orders.has_access('write'))                                    # 18.0+
```

Then ask the person to log in and try the action. To explain an access error, see
`diagnosis.md`.
