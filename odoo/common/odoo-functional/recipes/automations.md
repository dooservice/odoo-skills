# Automations

Three kinds, from the lightest:

- **Server action** (`ir.actions.server`): something done on records: update a field,
  create a record, send an email, add an activity, run a few lines of Python. Run from
  the Action menu, a button, an automation or a scheduled action.
- **Automation rule** (`base.automation`, module `base_automation`; "Automated Action"
  in 16.0): server actions run when records are created, changed, deleted, or when a
  date is reached. Install the module first.
- **Scheduled action** (`ir.cron`): a server action run every so often.

Prefer the lightest that does the job, a standard feature over all three (a follow-up
activity plan, a reminder in the email template settings), and code in server actions
only when the other types cannot do it. Every automation needs the user's yes: it acts
on many records without anyone watching.

Read first:

```python
for r in env['base.automation'].with_context(active_test=False).search([]):
    print(r.id, r.name, r.model_id.model, r.trigger, r.active)
for c in env['ir.cron'].with_context(active_test=False).search([]):
    print(c.id, c.cron_name, c.active, c.interval_number, c.interval_type, c.nextcall)
```

## Automation rule: when a quotation is confirmed, tag the customer

17.0 and later (the rule holds its actions in `action_server_ids`):

```python
tag = env['res.partner.category'].create({'name': 'Customer'})
env['base.automation'].create({
    'name': 'Tag customer on confirmation',
    'model_id': env['ir.model']._get_id('sale.order'),
    'trigger': 'on_create_or_write',
    'trigger_field_ids': [(6, 0, [env['ir.model.fields']._get('sale.order', 'state').id])],
    'filter_pre_domain': "[('state', '!=', 'sale')]",
    'filter_domain': "[('state', '=', 'sale')]",
    'action_server_ids': [(0, 0, {
        'name': 'Tag customer',
        'model_id': env['ir.model']._get_id('sale.order'),
        'state': 'code',
        'code': f"records.partner_id.write({{'category_id': [(4, {tag.id})]}})",
    })],
})
env.cr.commit()
```

16.0: the rule *is* a server action. Put `state` and `code` on the rule itself, without
`action_server_ids`.

- `filter_pre_domain` is checked before the change, `filter_domain` after: together
  they fire once, on the transition. With `filter_domain` alone the rule fires on every
  later save of a confirmed order.
- `trigger_field_ids` limits `on_create_or_write` to changes of those fields.
- Triggers in every version: `on_create`, `on_write`, `on_create_or_write`,
  `on_unlink`, `on_change` (form edits, Python code only), `on_time` (relative to a date
  field). 17.0 adds `on_stage_set`, `on_user_set`, `on_tag_set`, `on_state_set`,
  `on_priority_set`, `on_archive`, `on_unarchive`, `on_time_created`,
  `on_time_updated`, `on_message_received`, `on_message_sent` and `on_webhook`, and
  marks `on_create` and `on_write` as deprecated in favour of `on_create_or_write`
  (19.0 keeps only `on_write` deprecated). The stage, state, priority and tag triggers
  also need the value to watch (`trg_field_ref` or `trg_selection_field_id`): set those
  up from the form, or read an existing rule first.
- Timed rules (`on_time`...): `trg_date_id` (the date field), `trg_date_range` and
  `trg_date_range_type` (`minutes`, `hour`, `day`, `month`). Up to 18.0 a negative
  delay means before the date; from 19.0 use `trg_date_range_mode` (`after`,
  `before`). They run from the scheduled action
  `base_automation.ir_cron_data_base_automation_check`, so not to the minute.

## Server action types

`state` says what the action does. Python code (`code`) works in every version; the
others differ:

| Type | 16.0 | 17.0–19.0 | 20.0 |
|---|---|---|---|
| Update record | `object_write` with `fields_lines` | `object_write` with `update_path`, `value` | as 17.0 |
| Create record | `object_create` | `object_create` | as 17.0 |
| Duplicate record | - | `object_copy` (19.0) | `object_copy` |
| Email | `mail_post` + `template_id`, `mail_post_method` | same | `mail_post` ("Send Message") or `log_note` |
| Followers | `followers` | `followers`, `remove_followers` | same |
| Activity | `next_activity` | `next_activity` | same |
| Webhook | - | `webhook` | `webhook` |
| Several | `multi` (`child_ids`) | `multi` | `multi` |

For anything but `code`, build the action in the form (Settings, debug mode, Technical,
Server Actions) or read an existing one of the same type with `read()` before creating
one by script.

## Python code in a server action

Available names: `env`, `model`, `record` and `records` (the records it runs on), `log`,
`datetime`, `dateutil`, `time`, `UserError`. Keep it short, act on `records`, and do not
`commit()`.

- It runs as the user who triggered it, with their rights. A scheduled action runs as
  its `user_id`.
- Test on one record before turning it on, with the user's yes:
  `action.with_context(active_model='sale.order', active_ids=[42], active_id=42).run()`,
  then roll back if it was a test.

## Scheduled action: cancel expired quotations every night

```python
env['ir.cron'].create({
    'name': 'Cancel expired quotations',
    'model_id': env['ir.model']._get_id('sale.order'),
    'state': 'code',
    'code': "model.search([('state', 'in', ('draft', 'sent')), "
            "('validity_date', '<', datetime.date.today())])._action_cancel()",
    'interval_number': 1,
    'interval_type': 'days',
    'nextcall': '2026-10-21 03:00:00',
    # 16.0 and 17.0 only: 'numbercall': -1,
})
env.cr.commit()
```

- `nextcall` is in UTC. `interval_type`: `minutes`, `hours`, `days`, `weeks`, `months`.
- Up to 17.0, `numbercall` is how many times it runs (1 by default, -1 for ever) and
  `doall` replays missed runs; both are gone from 18.0.
- From 18.0, a job that fails at least 5 times in a row over 7 days is turned off;
  `failure_count` and `first_failure_date` show it.
- Run it now to check: `cron.method_direct_trigger()` (it commits).
- In a neutralized copy every scheduled action is off except the autovacuum; they stay
  as they were in production.

## Turning off

`active = False` on the rule or scheduled action, never delete one in use: archiving
keeps its history and can be undone.
