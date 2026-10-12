# Users, groups and access

Read first: who exists and what they have, `env['res.users'].search_read([('share', '=', False)], ['login'])`.

The groups field of a user is `groups_id` up to 18.0 and `group_ids` from 19.0 on; check
`odoo-reference/models/base.md` for this version.

## A user

```python
groups = 'group_ids'  # 'groups_id' up to 18.0
user = env['res.users'].create({
    'name': 'Ana Ríos',
    'login': 'ana@acme.example',
    'email': 'ana@acme.example',
    groups: [(6, 0, [env.ref('base.group_user').id, env.ref('sales_team.group_sale_salesman').id])],
})
user.action_reset_password()
env.cr.commit()
```

- Never set a password: `action_reset_password()` mails the user an invitation.
- `base.group_user` is an internal user (a paid seat); `base.group_portal` a customer
  portal user. Do not mix them in one user.
- Give the application group the person needs (`sales_team.group_sale_salesman`,
  `account.group_account_invoice`, `stock.group_stock_user`…); find them with
  `grep "res.groups" odoo-reference/xmlids/<addon>.md`.

## Rules

A record rule narrows what a group sees: confirm with the user first, and test it by
reading as that user (`env['sale.order'].with_user(user).search_count([])`).

```python
env['ir.rule'].create({
    'name': 'Salespeople see their own quotations',
    'model_id': env.ref('sale.model_sale_order').id,
    'domain_force': "[('user_id', '=', user.id)]",
    'groups': [(6, 0, [env.ref('sales_team.group_sale_salesman').id])],
})
```

Changing access rights of standard groups affects every user in them: prefer a new group.
