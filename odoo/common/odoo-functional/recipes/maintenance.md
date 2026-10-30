# Maintenance: equipment, requests and preventive maintenance

The Maintenance app (`maintenance`) keeps the company's equipment (`maintenance.equipment`)
and the work done on it as maintenance requests (`maintenance.request`), handled by
maintenance teams (`maintenance.team`) through stages (`maintenance.stage`). A request is
corrective (something broke) or preventive (planned). Bridges installed by themselves
add who or what uses the equipment: `hr_maintenance` (an employee or a department),
`fleet_maintenance` (a vehicle, 20.0 only) and `stock_maintenance` (a stock location and
the serial number's lot, 19.0+). Equipment on work centers, maintenance from
manufacturing orders and the OEE reports come from `mrp_maintenance`, and custom
worksheets from `maintenance_worksheet` (setting `module_maintenance_worksheet`); both
are Enterprise and left out. Community has no link between Maintenance and Manufacturing.

**At a glance**

- Apps: `maintenance`. `hr_maintenance` installs itself with `hr`, `fleet_maintenance`
  (20.0) with `fleet`, `stock_maintenance` (19.0+) with `stock`.
- Names that change by version: preventive by equipment `period` in 16.0, recurring
  request 17.0+; in 20.0 `state` replaces the done stage and `kanban_state`,
  `cancel_equipment_request` replaces `archive_equipment_request`, `user_ids` replaces
  `user_id`, no `request_date`; `schedule_end` and email alias on the team 19.0+;
  `location_id` 19.0+; menu Maintenance ‣ Equipments in 16.0, Maintenance ‣ Equipment
  17.0+.
- Sections: Before you start; The standard flow (1 create the maintenance team, 2 create
  the equipment categories, 3 register the equipment, 4 create a corrective request, 5
  work the request through the stages, 6 close it); Variations; Versions; Verify;
  Pitfalls.

## Before you start

- Settings: none in Community. Who configures (teams, categories, stages) is the group
  `maintenance.group_equipment_manager` (Equipment Manager); any internal user creates
  requests. Giving the group is an access change: see `users-and-access.md`, ask first.
- Read first:

```python
company = env.company
env['maintenance.team'].search_read([], ['name', 'company_id', 'member_ids'])
env['maintenance.stage'].search_read([], ['name', 'sequence', 'fold'])
env['maintenance.equipment.category'].search_read([], ['name', 'technician_user_id', 'company_id'])
env['maintenance.equipment'].search_read([('company_id', 'in', [company.id, False])], ['name', 'serial_no', 'category_id', 'maintenance_team_id', 'technician_user_id', 'owner_user_id'])
env['maintenance.request'].search_read([('equipment_id', '=', equipment.id)], ['name', 'maintenance_type', 'stage_id', 'schedule_date'])
```

Up to 19.0 also read the stages' `done`, which tells which stages close a request.

The standard data gives the stages `New Request` (`maintenance.stage_0`), `In
Progress` (`stage_1`), `Repaired` (`stage_3`) and `Scrap` (`stage_4`), and the teams
`Internal Maintenance` (`maintenance.equipment_team_maintenance`), `Metrology` and
`Subcontractor`. Up to 19.0 `Repaired` and `Scrap` have `done` set, which closes a
request; 20.0 has no `done` on stages: a request is closed by its `state`.

## The standard flow

Odoo's Maintenance documentation: teams and categories, equipment, then requests through
the stages, and preventive maintenance.

1. **Create the maintenance team.** Maintenance ‣ Configuration ‣ Maintenance Teams ‣
   New.

   ```python
   team = env['maintenance.team'].create({
       'name': 'Workshop', 'company_id': company.id,
       'member_ids': [(6, 0, technicians.ids)],
   })
   env.cr.commit()
   ```

   Leaves a team that requests and equipment can point to. Members must belong to the
   team's company. A request without a team takes the company's first team.

2. **Create the equipment categories.** Maintenance ‣ Configuration ‣ Equipment
   Categories ‣ New.

   ```python
   category = env['maintenance.equipment.category'].create({
       'name': 'Machine tools', 'technician_user_id': technician.id, 'company_id': company.id,
   })
   env.cr.commit()
   ```

   Leaves a category whose `technician_user_id` (Responsible) is proposed as technician
   for its equipment and requests.

   An email alias creates requests from incoming mail (`mail-servers.md`): on the
   category up to 18.0 (requests land in that category), on the team from 19.0
   (requests land in that team). The field shows in debug mode.

3. **Register the equipment.** Maintenance ‣ Equipments (16.0) or Maintenance ‣
   Equipment (17.0+) ‣ New.

   ```python
   equipment = env['maintenance.equipment'].create({
       'name': 'Lathe 01', 'category_id': category.id, 'company_id': company.id,
       'maintenance_team_id': team.id, 'technician_user_id': technician.id,
       'serial_no': 'LT-0001', 'model': 'Model X', 'partner_id': vendor.id,
       'effective_date': '2026-01-15', 'warranty_date': '2028-01-15', 'cost': 12000,
   })
   env.cr.commit()
   ```

   Leaves an active equipment record with no open request.

   - `serial_no` is unique across the database.
   - `effective_date` (required, today by default) is where the failure statistics
     start counting.
   - Where it is used: the free text `location` up to 18.0; from 19.0 `location_id`, an
     internal `stock.location`, with `stock_maintenance` (no location without it).
   - Who uses it, with `hr_maintenance`: `equipment_assign_to` (`employee`,
     `department`, `other`; default `employee`) with `employee_id` or `department_id`.
     The owner (`owner_user_id`) follows: the employee's user, or the department
     manager's user. 20.0 with `fleet_maintenance` adds `vehicle` and `vehicle_id`; the
     owner is the vehicle's fleet manager. Pass `equipment_assign_to` explicitly in 20.0,
     since each bridge sets its own default.

4. **Create a corrective request.** Maintenance ‣ Maintenance ‣ Maintenance Requests ‣
   New; also the Maintenance smart button on the equipment.

   ```python
   request = env['maintenance.request'].create({
       'name': 'Spindle noise', 'equipment_id': equipment.id,
       'maintenance_type': 'corrective', 'priority': '2',
       'schedule_date': '2026-03-02 08:00:00',
   })
   env.cr.commit()
   ```

   Leaves the request in the first stage (`New Request`), with the equipment's team and
   technician, and a "Maintenance Request" activity on the scheduled day for the
   technician (up to 19.0).

   - Technician: `user_id` up to 19.0; `user_ids` (several) in 20.0.
   - Dates: `request_date` (when it was asked; up to 19.0) and `schedule_date` (when the
     team plans it). From 19.0 `schedule_end` follows `schedule_date` plus one hour and
     `duration` is computed from both: set `schedule_end`, not `duration`. 20.0 has no
     `request_date`, defaults `schedule_date` to now and needs both dates or neither.
   - With `hr_maintenance`, `employee_id` (Created By) is the current user's employee.

5. **Work the request through the stages.** The request's kanban, drag the card; or the
   stage bar on the form.

   ```python
   request.write({'stage_id': env.ref('maintenance.stage_1').id})
   env.cr.commit()
   ```

   Leaves the request `In Progress`. Up to 19.0 the card also has `kanban_state`
   (`normal`, `blocked`, `done`: Ready for next stage), reset to `normal` on each stage
   change. 20.0 replaces it with `state`: `normal` (In Progress), `changes_requested`,
   `approved`, `done`, `cancelled`.

6. **Close it.** Up to 19.0, move it to `Repaired`. In 20.0, mark it Done (the state
   widget on the card or form) and move it to `Repaired`.

   20.0:

   ```python
   request.write({'state': 'done', 'stage_id': env.ref('maintenance.stage_3').id})
   env.cr.commit()
   ```

   16.0 to 19.0:

   ```python
   request.write({'stage_id': env.ref('maintenance.stage_3').id})
   env.cr.commit()
   ```

   Leaves the request closed with `close_date` today, out of the equipment's open
   count. Up to 19.0 any stage with `done` closes it; leaving such a stage clears
   `close_date`. In 20.0 only `state='done'` closes it, whatever the stage.

## Variations

- **Preventive maintenance, 17.0+: a recurring request.** On a request with
  `maintenance_type='preventive'`, tick Recurrent and say how often:

  ```python
  env['maintenance.request'].create({
      'name': 'Lathe 01 lubrication', 'equipment_id': equipment.id,
      'maintenance_type': 'preventive', 'schedule_date': '2026-04-01 08:00:00',
      'recurring_maintenance': True, 'repeat_interval': 1, 'repeat_unit': 'month',
      'repeat_type': 'until', 'repeat_until': '2026-12-31',
  })
  env.cr.commit()
  ```

  Closing it (step 6) creates the next one in the first stage, `schedule_date` moved
  by the interval, while it stays before `repeat_until` (`repeat_type='forever'` has no
  end). `repeat_unit`: `day`, `week`, `month`, `year`; `repeat_interval` at least 1.
  Corrective requests cannot recur. Cancelling the request stops the recurrence.

- **Preventive maintenance, 16.0: a period on the equipment.** The equipment's
  Maintenance tab: `period` (days between maintenances) and `maintenance_duration`
  (hours). The daily scheduled action `maintenance.maintenance_requests_cron` creates a
  preventive request on `next_action_date` (computed from `effective_date` and the last
  closed preventive request). To run it now:

  ```python
  equipment.write({'period': 90, 'maintenance_duration': 2.0})
  env['maintenance.equipment']._cron_generate_requests()
  env.cr.commit()
  ```

- **Plan in the calendar.** Maintenance ‣ Maintenance ‣ Maintenance Calendar (16.0 to
  19.0) or the calendar view of Maintenance ‣ Maintenance ‣ Maintenance Requests (20.0).
  Moving an event writes `schedule_date` (and `schedule_end` from 19.0); up to 19.0 it
  also reschedules the technician's activity. Maintenance ‣ Dashboard shows each team's open, scheduled,
  high-priority and blocked (20.0: changes requested) requests.

- **Cancel a request.** The form's Cancel button: up to 19.0 `archive_equipment_request()`
  (sets `archive`, hidden from the pipe); 20.0 `cancel_equipment_request()` (state
  `cancelled`). Reopen Request (`reset_equipment_request()`) puts it back in the first
  stage.

- **Scrap equipment.** Close its last request in the `Scrap` stage (step 6 with
  `maintenance.stage_4`), then, with the user's yes, record the date and archive it:

  ```python
  equipment.write({'scrap_date': '2026-06-30', 'active': False})
  env.cr.commit()
  ```

  Nothing in Maintenance does this by itself, and no stock or accounting follows
  (`scrap_date` is visible in debug mode). Archiving keeps its history.

- **Equipment per employee.** With `hr_maintenance`, the employee form's Equipment smart
  button lists what is assigned to them; requests can be grouped by Employee or
  Department. In 20.0 registering an employee's departure unassigns their equipment.

- **Equipment and stock, 19.0+.** With `stock_maintenance`, the location form has an
  Equipments smart button, and when `serial_no` matches a lot (`stock.lot`) and lots
  are on (`group_stock_production_lot`) the equipment form shows a Serial Number smart
  button to that lot. In 18.0 the same button comes from `maintenance` itself, without
  the location.

- **Reliability figures, 17.0+.** The equipment form computes MTBF, MTTR, latest
  failure and estimated next failure from closed corrective requests; set
  `expected_mtbf` to compare. In 16.0 they are Enterprise (`mrp_maintenance`).

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Preventive | equipment `period`, daily cron | recurring request | same | same | same |
| Request closed by | stage with `done` | same | same | same | `state='done'` |
| Card status | `kanban_state` | same | same | same | `state` |
| Cancel | `archive_equipment_request` (`archive`) | same | same | same | `cancel_equipment_request` (`cancelled`) |
| Technician on request | `user_id` | same | same | same | `user_ids` |
| `request_date` | yes | yes | yes | yes | no |
| `schedule_end`, computed `duration` | no | no | no | yes | yes |
| Email alias | category | same | same | team | team |
| Equipment location | `location` text | same | same | `location_id` (`stock_maintenance`) | same |
| Lot smart button | no | no | `maintenance` | `stock_maintenance` | same |
| MTBF, MTTR | Enterprise | `maintenance` | same | same | same |
| Assigned to a vehicle | no | no | no | no | `fleet_maintenance` |
| Stages restricted to teams | no | no | no | no | `maintenance_team_ids` |
| Menu: equipment | Maintenance ‣ Equipments | Maintenance ‣ Equipment | same | same | same |
| Menu: calendar | Maintenance ‣ Maintenance ‣ Maintenance Calendar | same | same | same | none (calendar view of the requests) |
| Menu: reporting | Maintenance ‣ Reporting ‣ Maintenance Requests | same | same | Maintenance ‣ Reporting ‣ Maintenance Requests Analysis | same |
| Menu: settings | none | Maintenance ‣ Configuration ‣ Settings | same | same | same |

The same in every version: Maintenance ‣ Dashboard, Maintenance ‣ Maintenance ‣
Maintenance Requests, Maintenance ‣ Configuration ‣ Maintenance Teams, Equipment
Categories and Maintenance Stages.

## Verify

```python
print(equipment.read(['maintenance_count', 'maintenance_open_count', 'maintenance_team_id', 'technician_user_id', 'active']))
print(env['maintenance.request'].search_read([('equipment_id', '=', equipment.id)], ['name', 'maintenance_type', 'state', 'stage_id', 'schedule_date', 'close_date']))
```

Up to 19.0 requests have no `state`: leave it out of the list.

Closed requests have `close_date`; a recurring preventive request has a successor in the
first stage at the next date; the open count matches the requests still to do.

## Pitfalls

- 20.0: moving a request to `Repaired` does not close it and does not create the next
  recurring one; set `state='done'`.
- Up to 19.0, a custom stage without `done` never closes requests, so recurrence and
  MTBF ignore them; tick Request Done on the closing stages.
- A second `serial_no` already used by another equipment is refused; the check covers
  every company.
- 16.0: without the scheduled action running, preventive requests never appear; check
  that `maintenance.maintenance_requests_cron` is active.
- From 19.0, writing `duration` on a request is ignored: it comes from `schedule_date`
  and `schedule_end`.
- A team or technician of another company is cleared from the equipment or request:
  check `company_id` before assigning.
- Linking equipment to manufacturing work centers needs Enterprise (`mrp_maintenance`);
  do not look for it in Community.
