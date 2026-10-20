# Automations

Three kinds, from the lightest:

- **Server action** (`ir.actions.server`): something done on records: update a field,
  create a record, send an email, add an activity, run a few lines of Python. Run from
  the Action menu, a button, an automation or a scheduled action.
- **Automation rule** (`base.automation`, module `base_automation`; "Automated Action"
  in 16.0): server actions run when records are created, changed, deleted, or when a
  date is reached.
- **Scheduled action** (`ir.cron`): a server action run every so often.

Prefer the lightest that does the job, a standard feature over all three (a follow-up
activity plan, a reminder in the email template settings), and code in server actions
only when the other types cannot do it. Every automation needs the user's yes: it acts
on many records without anyone watching. Odoo documents automation rules through Studio
(Enterprise); without Studio the same form is in Settings ‣ Technical, in developer mode.

## Before you start

- Apps: `base_automation` for automation rules (install it with the user's yes); server
  and scheduled actions are in `base`.
- Settings: developer mode, for Settings ‣ Technical ‣ Automation and ‣ Actions.
- Read first:

```python
for r in env['base.automation'].with_context(active_test=False).search([]):
    print(r.id, r.name, r.model_id.model, r.trigger, r.active)
for c in env['ir.cron'].with_context(active_test=False).search([]):
    print(c.id, c.cron_name, c.active, c.interval_number, c.interval_type, c.nextcall)
```

## The standard flow

The example: when a quotation is confirmed, tag its customer.

1. **Create the rule on its model.** Settings ‣ Technical ‣ Automation ‣ Automation
   Rules (Automated Actions in 16.0) ‣ New; give it a clear name and pick the Model.

   Nothing is saved until step 4.

2. **Choose the trigger.** 17.0+: the Values Updated triggers say it directly: State is
   set to, Sales Order. 16.0: On Update, with Trigger Fields `state`.

   - Triggers in every version: `on_create`, `on_write`, `on_create_or_write`,
     `on_unlink`, `on_change` (form edits, Python code only), `on_time` (relative to a
     date field). 17.0 adds `on_stage_set`, `on_user_set`, `on_tag_set`,
     `on_state_set`, `on_priority_set`, `on_archive`, `on_unarchive`,
     `on_time_created`, `on_time_updated`, `on_message_received`, `on_message_sent`
     and `on_webhook`, and marks `on_create` and `on_write` as deprecated in favour of
     `on_create_or_write` (19.0 keeps only `on_write` deprecated).
   - The stage, state, priority and tag triggers need the value to watch
     (`trg_selection_field_id` for state and priority, `trg_field_ref` for stage and
     tag); the form fills `trigger_field_ids` and the Apply on domain from it. Through
     the ORM, pass `trigger_field_ids` too: 17.0 does not fill it on `create()`, and the
     rule then never fires.
   - `trigger_field_ids` limits a save trigger to changes of those fields. Without it,
     every save fires the rule; 18.0 fills it from the fields in `filter_domain`.

3. **Add the conditions.** Before Update Domain (`filter_pre_domain`, checked before the
   change, not on creation) and Apply on (`filter_domain`, checked after). In 16.0 both
   are needed here: together they fire once, on the transition. With `filter_domain`
   alone the rule fires again on later saves of a confirmed order that change a trigger
   field.

4. **Add the action and save.** Actions To Do tab ‣ Add an action (16.0: Action To Do on
   the rule itself). 17.0+: Update Record, Customer ‣ Tags, By Adding, the tag. 16.0 has
   no update through a related field: Execute Python Code.

   17.0 to 20.0:

   ```python
   tag = env['res.partner.category'].create({'name': 'Customer'})
   state = env['ir.model.fields']._get('sale.order', 'state')
   rule = env['base.automation'].create({
       'name': 'Tag customer on confirmation',
       'model_id': env['ir.model']._get_id('sale.order'),
       'trigger': 'on_state_set',
       'trigger_field_ids': [(6, 0, state.ids)],
       'trg_selection_field_id': state.selection_ids.filtered(lambda s: s.value == 'sale').id,
       'action_server_ids': [(0, 0, {
           'name': 'Tag customer',
           'model_id': env['ir.model']._get_id('sale.order'),
           'state': 'object_write',
           'update_path': 'partner_id.category_id',
           'update_m2m_operation': 'add',
           'value': str(tag.id),
       })],
   })
   print(rule.trigger_field_ids.mapped('name'), rule.filter_domain)
   env.cr.commit()
   ```

   16.0 (the rule *is* a server action: `state` and `code` on the rule itself, no
   `action_server_ids`):

   ```python
   tag = env['res.partner.category'].create({'name': 'Customer'})
   env['base.automation'].create({
       'name': 'Tag customer on confirmation',
       'model_id': env['ir.model']._get_id('sale.order'),
       'trigger': 'on_write',
       'trigger_field_ids': [(6, 0, [env['ir.model.fields']._get('sale.order', 'state').id])],
       'filter_pre_domain': "[('state', '!=', 'sale')]",
       'filter_domain': "[('state', '=', 'sale')]",
       'state': 'code',
       'code': f"records.partner_id.write({{'category_id': [(4, {tag.id})]}})",
   })
   env.cr.commit()
   ```

   Several actions run in the order listed: an email after an update sees the updated
   values. Leaves the rule active: it runs on the next order confirmed by anyone.

5. **Timed rules: start the clock.** For `on_time` (Based on date field) and, from 17.0,
   `on_time_created` and `on_time_updated`, set the Delay and save, then open the
   scheduled action `base_automation.ir_cron_data_base_automation_check` (Automation
   Rules: check and execute) and Run Manually; Odoo documents this from 19.0. Each run
   acts on records whose date plus delay falls between the rule's last run and now; a
   rule never run starts from 1970, so its first run (manual or not) also acts on every
   old record. To start from today, save the rule first without actions (or with an
   Apply on condition that excludes old records), Run Manually (which also runs the
   other timed rules, as the scheduler would), then add the actions.
   The code behaves the same from 16.0.

   - `trg_date_id` (the date field), `trg_date_range` and `trg_date_range_type`
     (`minutes`, `hour`, `day`, `month`). Up to 18.0 a negative delay means before the
     date; from 19.0 use `trg_date_range_mode` (`after`, `before`).
   - The scheduler is active only while a timed rule exists, and runs every 4 hours,
     or more often when a rule has a short delay: not to the minute.

6. **Try it on one record.** Confirm one test quotation and look at the customer, with
   the user's yes, or roll back in a shell.

   ```python
   order = env['sale.order'].search([('state', 'in', ('draft', 'sent'))], limit=1)
   order.action_confirm()
   print(order.state, tag in order.partner_id.category_id)
   ```

   Leaves the order confirmed and the customer tagged, unless rolled back.

## Variations

- **Any save, with before and after domains (all versions).** Instead of State is set
  to, the trigger `on_create_or_write` with `trigger_field_ids` and both domains, and
  Python code; this is the 16.0 shape and still works from 17.0:

  ```python
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

- **A server action run by hand.** Settings ‣ Technical ‣ Actions ‣ Server Actions ‣
  New, then Create Contextual Action to show it in the model's Action menu. For any
  type but `code`, build it in the form or read an existing one of the same type with
  `read()` before creating one by script.
- **Python code in a server action.** Available names: `env`, `model`, `record` and
  `records` (the records it runs on), `log`, `datetime`, `dateutil`, `time`,
  `UserError`. Keep it short, act on `records`, and do not `commit()`. It runs as the
  user who triggered it, with their rights; a scheduled action runs as its `user_id`.
  Test on one record before turning it on, with the user's yes:
  `action.with_context(active_model='sale.order', active_ids=[42], active_id=42).run()`,
  then roll back if it was a test.
- **A scheduled action.** Settings ‣ Technical ‣ Automation ‣ Scheduled Actions ‣ New.
  Example, cancel expired quotations every night:

  ```python
  cron = env['ir.cron'].create({
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

  - `nextcall` is in UTC. `interval_type`: `minutes`, `hours`, `days`, `weeks`,
    `months`.
  - Up to 17.0, `numbercall` is how many times it runs (1 by default, -1 for ever) and
    `doall` replays missed runs; both are gone from 18.0.
  - From 18.0, a job that fails at least 5 times in a row over 7 days is turned off;
    `failure_count` and `first_failure_date` show it.
  - Run Manually (`cron.method_direct_trigger()`) acts on every record the code finds,
    not on a test record. Up to 18.0 it runs in the current transaction; from 19.0 it
    runs and commits in its own, so it cannot be rolled back.
- **Turning off.** `active = False` on the rule or scheduled action; never delete one in
  use: archiving keeps its history and can be undone.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Rules menu (developer mode) | Settings ‣ Technical ‣ Automation ‣ Automated Actions | Settings ‣ Technical ‣ Automation ‣ Automation Rules | same as 17.0 | same | same |
| Server actions menu | Settings ‣ Technical ‣ Actions ‣ Server Actions | same | same | same | same |
| Scheduled actions menu | Settings ‣ Technical ‣ Automation ‣ Scheduled Actions | same | same | same | same |
| Actions of a rule | on the rule (`state`, `code`) | `action_server_ids` | same | same | same |
| Value triggers (`on_state_set`...) | - | yes | yes | yes | yes |
| `trigger_field_ids` filled from `filter_domain` | - | - | yes | yes | yes |
| Before / after the date | negative delay | negative delay | negative delay | `trg_date_range_mode` | as 19.0 |
| `numbercall`, `doall` on `ir.cron` | yes | yes | - | - | - |
| Cron turned off after repeated failures | - | - | yes | yes | yes |
| Run Manually commits on its own | - | - | - | yes | yes |

Server action types (`state`); Python code (`code`) works in every version:

| Type | 16.0 | 17.0–19.0 | 20.0 |
|---|---|---|---|
| Update record | `object_write` with `fields_lines`, on the record's own fields | `object_write` with `update_path`, `value` | as 17.0 |
| Create record | `object_create` | `object_create` | as 17.0 |
| Duplicate record | - | `object_copy` (19.0) | `object_copy` |
| Email | `mail_post` + `template_id`, `mail_post_method` | same | `mail_post` ("Send Message") or `log_note` |
| Followers | `followers` | `followers`, `remove_followers` | same |
| Activity | `next_activity` | `next_activity` | same |
| Webhook | - | `webhook` | `webhook` |
| Several | `multi` (`child_ids`) | `multi` | `multi` |

## Verify

```python
rule = env['base.automation'].search([('name', '=', 'Tag customer on confirmation')])
print(rule.read(['active', 'trigger', 'filter_pre_domain', 'filter_domain']), rule.trigger_field_ids.mapped('name'))
cron = env['ir.cron'].search([('cron_name', '=', 'Cancel expired quotations')])
print(cron.read(['active', 'nextcall', 'interval_number', 'interval_type', 'user_id']))
```

Then do the business action once (step 6) and read the result.

## Pitfalls

- **A rule that fires on every save**: no `trigger_field_ids` and no Before Update
  Domain. Add them.
- **A timed rule that acts on old records** the first time: its first run starts from
  1970. Run the scheduled action once before the rule has actions (step 5).
- **A neutralized copy** turns off every scheduled action except the autovacuum
  (production keeps its own); automation rules still run there.
- **Run Manually is not a test**: it works on real records and, from 19.0, commits.
- **Code that commits or acts outside `records`** breaks the transaction or touches
  records nobody chose. Keep it to `records`.
- **Deleting** a rule or cron loses its history; archive it.
