# Projects, tasks and timesheets

A project (`project.project`) holds tasks (`project.task`) that move through stages
(`project.task.type`); its visibility decides who reaches it. With `hr_timesheet`,
employees log time on tasks as analytic lines (`account.analytic.line`); with
`sale_timesheet`, a service product creates the task or project when its order is
confirmed, and the hours logged are invoiced from that order. Timesheet validation, the
grid view, planning and field service are Enterprise and left out.

## Before you start

- Apps: `project`; `hr_timesheet` for timesheets; `sale_timesheet` (with `sale_project`)
  to sell time.
- Settings: `module_hr_timesheet` (Project ‣ Configuration ‣ Settings ‣ Timesheets: it
  installs a module, so ask first); `group_analytic_accounting` (Accounting settings,
  Analytic Accounting) shows the analytic distribution on invoices, as Odoo's
  documentation sets it; `group_project_stages` adds stages to projects themselves.
- Read first:

```python
print(env['project.project'].search_read([], ['name', 'privacy_visibility', 'user_id', 'allow_timesheets', 'company_id']))
print(env['project.task.type'].search_read([('project_ids', '!=', False)], ['name', 'sequence', 'fold', 'project_ids']))
print(env['hr.employee'].search_read([('user_id', '!=', False)], ['name', 'user_id', 'company_id']))
print(env['product.template'].search_read([('service_tracking', '!=', 'no')], ['name', 'service_tracking', 'service_policy', 'project_id', 'project_template_id']))
```

## The standard flow

1. **Create the project and its stages.** Project ‣ Projects ‣ New, then add stages in
   the kanban (Project ‣ Configuration ‣ Task Stages lists them in developer mode).

   ```python
   stages = env['project.task.type'].create([
       {'name': name, 'sequence': seq, 'fold': fold}
       for seq, (name, fold) in enumerate([('To do', False), ('In progress', False), ('Done', True)])
   ])
   project = env['project.project'].create({
       'name': '<project name>', 'user_id': manager.id, 'company_id': company.id,
       'privacy_visibility': 'employees', 'allow_timesheets': True,
       'type_ids': [(6, 0, stages.ids)],
   })
   env.cr.commit()
   ```

   Leaves an active project with those stages. To reuse existing stages, add the project
   to their `project_ids` instead of creating copies.

2. **Set who sees it.** The project's Settings tab, Visibility (`privacy_visibility`, see
   Versions). For a private project, add the people (16.0–19.0 as followers, 20.0 as team
   members):

   ```python
   if 'allowed_internal_user_ids' in project:                     # 20.0
       project.allowed_internal_user_ids = [(4, user.id)]
   else:                                                          # 16.0-19.0
       project.message_subscribe(partner_ids=user.partner_id.ids)
   env.cr.commit()
   ```

3. **Create tasks.** Open the project, New in a stage column.

   ```python
   hours_field = 'allocated_hours' if 'allocated_hours' in env['project.task'] else 'planned_hours'  # 17.0+ / 16.0
   task = env['project.task'].create({
       'name': '<task>', 'project_id': project.id, 'user_ids': [(6, 0, [user.id])], hours_field: 8,
   })
   env.cr.commit()
   ```

   Leaves the task in the first stage; from 17.0 its `state` is `01_in_progress`.

4. **Log time.** The task's Timesheets tab, Add a line (or Timesheets ‣ Timesheets ‣ My
   Timesheets). The user needs an employee in the project's company.

   ```python
   employee = env['hr.employee'].search([('user_id', '=', user.id), ('company_id', '=', company.id)], limit=1)
   env['account.analytic.line'].create({
       'name': '<what was done>', 'project_id': project.id, 'task_id': task.id,
       'employee_id': employee.id, 'unit_amount': 2.5, 'date': '<YYYY-MM-DD>',
   })
   env.cr.commit()
   ```

   `task.effective_hours` sums it; the line's `amount` is minus hours times the
   employee's `hourly_cost`.

5. **A service product that creates the work.** Sales ‣ Products ‣ Products: Product Type
   Service, Invoicing Policy "Based on Timesheets" (`service_policy`), Create on Order
   (`service_tracking`): Task in an existing project, or Project & Task.

   ```python
   hour = env.ref('uom.product_uom_hour')
   vals = {'name': '<service>', 'type': 'service', 'list_price': 100, 'uom_id': hour.id,
           'service_tracking': 'task_global_project', 'project_id': project.id,
           'service_policy': 'delivered_timesheet'}
   if 'detailed_type' in env['product.template']:                 # 16.0, 17.0
       vals['detailed_type'] = 'service'
   if 'uom_po_id' in env['product.template']:                     # 16.0-18.0
       vals['uom_po_id'] = hour.id
   product = env['product.product'].create(vals)
   project.allow_billable = True
   env.cr.commit()
   ```

   Writing `service_policy` sets `invoice_policy` (`delivery`) and `service_type`
   (`timesheet`). Sell it in Hours so logged time converts.

6. **Sell it.** Sales ‣ Orders ‣ Quotations ‣ New, add the product, Confirm: the task
   (`order_line.task_id`) or project (`order_line.project_id`) is created. Time logged on
   that task is linked to the line (`so_line`) and fills its `qty_delivered`.

7. **Invoice the hours.** On the order, Create Invoice, Regular invoice, Create Draft
   Invoice; the accountant confirms it.

   ```python
   wizard = env['sale.advance.payment.inv'].with_context(active_model='sale.order', active_ids=order.ids).create({
       'advance_payment_method': 'delivered',
   })
   wizard.create_invoices()
   print(order.invoice_ids.mapped(lambda m: (m.name, m.state, m.invoice_line_ids.mapped('quantity'))))
   env.cr.commit()
   ```

   Leaves a draft invoice with the hours not yet invoiced. Posting it (`action_post()`,
   only with the user's yes) marks those timesheets invoiced; they can no longer be edited.

## Variations

- **Project & Task** (`task_in_project`): a new project per order, copied from
  `project_template_id` when set, named after the order. **Project** (`project_only`): the
  project without task.
- **Prepaid or fixed quantity**: `service_policy` `ordered_prepaid` (invoice what was
  ordered) or `delivered_manual` (quantity typed on the line); `delivered_milestones` with
  milestones on.
- **Close a task**: 16.0 move it to a folded stage; from 17.0 set `state` to `1_done` or
  `1_canceled`, whatever the stage.
- **Portal customers**: Share on a project with visibility `portal` (19.0+ also
  `invited_users`); do it from the interface, it sends invitations.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Task hours field | `planned_hours` | `allocated_hours` | same | same | same |
| Task closed by | folded stage (`is_closed`) | `state` | same | same | same |
| Visibility values | `followers`, `employees`, `portal` | same | same | adds `invited_users` | same; `followers` is "Team members only" |
| Private project access | followers | followers | followers | followers | `allowed_internal_user_ids` |
| Encoding unit setting | `timesheet_encode_uom_id` | `timesheet_encode_method` | same | same | same |
| Milestones, dependencies, recurrence | settings `group_project_milestone`, ... | same | same | project fields `allow_milestones`, ... | same |
| Invoiced timesheet | `timesheet_invoice_id` | same | same | same | `reinvoice_move_id` |
| Billing category | `timesheet_invoice_type` | same | same | same | `billable_type` (`04_billable_time`, ...) |
| New project without `type_ids` | no stages | no stages | no stages | no stages | four default stages |

## Verify

```python
print(bool(env['project.project'].with_user(user).search([('id', '=', project.id)])))
print(task.effective_hours, task.remaining_hours)
print(order.order_line.mapped(lambda l: (l.task_id.name, l.project_id.name, l.qty_delivered, l.qty_to_invoice)))
```

Then ask a team member to log time on the task and check the line's delivered quantity.

## Pitfalls

- A user without an employee in the project's company cannot log time: create or link
  the employee (see `employees-and-expenses.md`).
- Being assigned a task does not open a private project: add the person as follower (team
  member in 20.0). Making a project more private hides it from people using it today.
- Changing `service_tracking` or `service_policy` on a product already on confirmed
  orders does not change those orders: list them first and ask.
