# Automations

Three kinds, from the lightest:

- **Server action** (`ir.actions.server`): something done on records, run from a button
  or from an automation.
- **Automated action** (`base.automation`, module `base_automation`): a server action run
  when records change or a date passes. Install the module first.
- **Scheduled action** (`ir.cron`): a server action run every so often. In a neutralized
  clone every scheduled action is off; they come back in production.

## When a quotation is confirmed, tag the customer

```python
tag = env['res.partner.category'].create({'name': 'Customer'})
action = env['ir.actions.server'].create({
    'name': 'Tag customer on confirmation',
    'model_id': env.ref('sale.model_sale_order').id,
    'state': 'code',
    'code': f"records.partner_id.write({{'category_id': [(4, {tag.id})]}})",
})
env['base.automation'].create({
    'name': 'Tag customer on confirmation',
    'model_id': env.ref('sale.model_sale_order').id,
    'trigger': 'on_create_or_write',
    'filter_domain': "[('state', '=', 'sale')]",
    'action_server_ids': [(6, 0, [action.id])],
})
env.cr.commit()
```

- 17.0 and later link actions with `action_server_ids`; in 16.0 the automation *is* a
  server action: put `state` and `code` on the `base.automation` itself.
- Triggers differ by version (`on_stage_set`, `on_state_set`, `on_time`…): read the
  selection in this version's source before choosing one.
- Code in a server action runs as the user who changes the record: keep it small, and
  test it on one record before turning it on.
