# Fleet: vehicles, drivers, contracts and services

A vehicle (`fleet.vehicle`) is built on a model (`fleet.vehicle.model`) of a manufacturer
(`fleet.vehicle.model.brand`) and moves through statuses (`fleet.vehicle.state`). Its
driver is a contact; with `hr_fleet`, an employee. What the vehicle costs is recorded in
contracts (`fleet.vehicle.log.contract`: leasing, insurance) and services
(`fleet.vehicle.log.services`: repairs, fuel); its mileage in odometer readings
(`fleet.vehicle.odometer`). With `account_fleet`, a vendor bill line can name the vehicle
and, once posted, creates the service on it. This recipe covers `fleet`, `hr_fleet` and
`account_fleet`, all in Community.

**At a glance**

- Apps: `fleet`; `hr_fleet` (with `hr`); `account_fleet` (with `account`).
- Names that change by version: default vehicle status Registered (16.0), New Request
  (17.0+); service date `date` (16.0-19.0), `date_from`, `date_to` (20.0); first contract
  date `first_contract_date` (16.0-18.0), `contract_date_start` (19.0+); contract states
  futur, open, expired, closed (16.0-19.0), adds `done` (20.0); employee's driver contact
  `address_home_id` (16.0), `work_contact_id` (17.0+); `model_id` required (16.0-19.0),
  optional (20.0).
- Sections: Before you start; The standard flow (1 manufacturer, 2 model, 3 vehicle,
  4 driver, 5 contract, 6 service, 7 odometer reading, 8 costs); Variations; Versions;
  Verify; Pitfalls.

## Before you start

- Apps: `fleet`; `hr_fleet` (installed automatically with `hr`) to pick employees as
  drivers; `account_fleet` (installed automatically with `account`) to book vendor bills
  on vehicles.
- Access: Fleet: Officer (`fleet.fleet_group_user`) manages vehicles; Fleet:
  Administrator (`fleet.fleet_group_manager`) also sees configuration and costs.
- Settings (Fleet ‣ Configuration ‣ Settings): `delay_alert_contract`, the days before a
  contract's expiration date at which its responsible gets a renewal activity (default
  30).

```python
env['res.config.settings'].create({'delay_alert_contract': 30}).execute()
env.cr.commit()
```

- Read first:

```python
print(env['fleet.vehicle.state'].search_read([], ['name', 'sequence']))
print(env['fleet.vehicle.model.brand'].search_read([], ['name']))
print(env['fleet.vehicle.model'].search_read([], ['name', 'brand_id', 'vehicle_type', 'default_fuel_type']))
print(env['fleet.service.type'].search_read([], ['name', 'category']))
print(env['fleet.vehicle'].search_read([], ['name', 'license_plate', 'driver_id', 'state_id', 'odometer', 'contract_state']))
```

## The standard flow

The order of Odoo's Fleet documentation: manufacturers and models, the vehicle, its
driver, then contracts, services and odometer readings as they happen.

1. **Manufacturer.** Fleet ‣ Configuration ‣ Models ‣ Manufacturers ‣ New.

   ```python
   brand = env['fleet.vehicle.model.brand'].create({'name': 'Brand A'})
   ```

2. **Model.** Fleet ‣ Configuration ‣ Models ‣ Models ‣ New. The model holds what every
   vehicle of it shares: type, fuel, seats, doors, power; a new vehicle copies them.

   ```python
   model = env['fleet.vehicle.model'].create({
       'name': 'Model A', 'brand_id': brand.id, 'vehicle_type': 'car',
       'default_fuel_type': 'gasoline', 'seats': 5, 'doors': 5,
   })
   ```

   `vehicle_type` is `car`, `bike` or, in 20.0 only, `other`. `default_fuel_type` is one of `diesel`, `gasoline`, `full_hybrid`,
   `plug_in_hybrid_diesel`, `plug_in_hybrid_gasoline`, `cng`, `lpg`, `hydrogen`,
   `electric` (the default).

3. **Vehicle.** Fleet ‣ Fleet ‣ Fleet ‣ New.

   ```python
   vehicle = env['fleet.vehicle'].create({
       'model_id': model.id, 'license_plate': 'ABC-123', 'vin_sn': '<chassis number>',
       'acquisition_date': '<YYYY-MM-DD>', 'manager_id': fleet_user.id,
       'company_id': env.company.id,
   })
   env.cr.commit()
   ```

   Leaves the vehicle in status `New Request` (16.0: `Registered`), named
   `<brand>/<model>/<plate>`. `model_id` is required up to 19.0. Move it through the
   statuses (New Request, To Order, Registered, Downgraded) by writing `state_id`, as the
   kanban drag does.

4. **Driver.** On the vehicle, Driver (a contact) or, with `hr_fleet`, Driver (Employee).

   ```python
   vehicle.write({'driver_employee_id': employee.id})   # hr_fleet: sets driver_id to the employee's contact
   vehicle.write({'driver_id': partner.id})             # without hr_fleet
   env.cr.commit()
   ```

   Each change of driver writes a line in the drivers history
   (`fleet.vehicle.assignation.log`, Drivers History smart button). The employee's
   contact is `work_contact_id` (16.0: the private address `address_home_id`).

5. **Contract.** Fleet ‣ Fleet ‣ Contracts ‣ New (or the Contracts smart button).

   ```python
   contract_type = env['fleet.service.type'].search([('category', '=', 'contract')], limit=1)
   contract = env['fleet.vehicle.log.contract'].create({
       'vehicle_id': vehicle.id, 'cost_subtype_id': contract_type.id, 'insurer_id': vendor.id,
       'start_date': '<YYYY-MM-DD>', 'expiration_date': '<YYYY-MM-DD>',
       'amount': 0.0,                                        # activation cost
       'cost_generated': 350.0, 'cost_frequency': 'monthly', # recurring cost
       'user_id': fleet_user.id,
   })
   env.cr.commit()
   print(contract.state)
   ```

   Up to 19.0 a new contract is `open` (In Progress, 18.0: Running) whatever its dates;
   the daily scheduled action then moves it to `futur` (Incoming / New) before its start
   date and `expired` after its expiration date. In 20.0 it gets the state of its dates
   at once. The expiration date defaults to one year after today.

6. **Service.** Fleet ‣ Fleet ‣ Services ‣ New.

   ```python
   service_type = env['fleet.service.type'].search([('category', '=', 'service')], limit=1)
   service = env['fleet.vehicle.log.services'].create({
       'vehicle_id': vehicle.id, 'service_type_id': service_type.id, 'vendor_id': vendor.id,
       'description': '<what was done>', 'amount': 120.0, 'odometer': 15200,
       'date_from': '<YYYY-MM-DD>', 'date_to': '<YYYY-MM-DD>',
   })
   service.write({'state': 'running'})
   env.cr.commit()
   ```

   That is 20.0. In 16.0 to 19.0 the service has one date, `date`, in place of
   `date_from` and `date_to`. Write `state` `done` when the work is finished.

   Created `new`; the kanban stages are `new`, `running`, `done`, `cancelled`. A non-zero
   `odometer` creates an odometer reading on the service date.

7. **Odometer reading.** Fleet ‣ Fleet ‣ Odometers ‣ New, or Last Odometer on the vehicle.

   ```python
   env['fleet.vehicle.odometer'].create({'vehicle_id': vehicle.id, 'value': 15800, 'date': '<YYYY-MM-DD>'})
   vehicle.odometer = 16000      # same thing: a reading dated today
   env.cr.commit()
   ```

   The vehicle's `odometer` is its highest reading. From 18.0, writing a lower Last
   Odometer on the vehicle is refused.

8. **Costs.** Fleet ‣ Reporting ‣ Costs (`fleet.vehicle.cost.report`): contracts and
   services by vehicle and month. From 19.0, Fleet ‣ Reporting ‣ Odometers analyses the
   readings.

## Variations

- **Vendor bill on a vehicle** (`account_fleet`): on a vendor bill line, show the
  optional Vehicle column and pick the vehicle. Posting the bill creates a service of
  type `Vendor Bill` on it with the line's amount, vendor and label.

  ```python
  bill = env['account.move'].create({
      'move_type': 'in_invoice', 'partner_id': vendor.id, 'invoice_date': '<YYYY-MM-DD>',
      'invoice_line_ids': [(0, 0, {'name': '<label>', 'quantity': 1, 'price_unit': 200.0, 'vehicle_id': vehicle.id})],
  })
  bill.action_post()
  env.cr.commit()
  print(env['fleet.vehicle.log.services'].search_read([('vehicle_id', '=', vehicle.id)], ['service_type_id', 'amount', 'description']))
  ```

  The Bills smart button on the vehicle lists them. From 18.0 the service stays linked
  to the bill line (`account_move_line_id`): its cost follows the line and cannot be
  edited, and removing the vehicle from the line deletes the service. 20.0 adds Requires
  vehicle (`is_vehicle_account`) on expense and fixed asset accounts, which makes the
  Vehicle column required on their bill lines, and a Create Bill button on a service
  (`action_create_account_move`) that drafts the bill from it.
- **Planned driver change**: set Future Driver (`future_driver_id`, with `hr_fleet`
  `future_driver_employee_id`), then Apply Change on the vehicle
  (`vehicle.action_accept_driver_change()`): the future driver becomes the driver and
  leaves any other vehicle of the same type they were driving.
- **Employee leaves** (`hr_fleet`): registering the departure ends the employee's
  driver history at the departure date and frees their vehicles: up to 19.0 when the
  wizard's Release Company Car is ticked, in 20.0 always (also as future driver).
- **Vehicles of an employee** (`hr_fleet`): the Cars smart button on the employee
  (`employee.action_open_employee_cars()`); up to 19.0 the employee also carries a
  mobility card number (`mobility_card`) shown on the vehicle.
- **Contract handled** (20.0): Done on an expired contract (`contract.action_done()`)
  stops its renewal reminders; Reactivate (`action_reactivate()`) puts it back by its
  dates. Up to 19.0 close it (`action_close()`).

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Default vehicle status | Registered | New Request | same | same | same |
| `model_id` on vehicle | required | required | required | required | optional |
| Vehicle types | car, bike | same | same | same | car, bike, other |
| Model year | integer | same | same | selection | selection |
| First contract date field | `first_contract_date` | same | same | `contract_date_start` | same |
| Plan to change car/bike | on the driver contact | same | same | on the vehicle | `plan_to_change_vehicle` |
| Contract states | futur, open, expired, closed | same | same, labels New, Running, Cancelled | same | adds `done`; state set from dates at create |
| Contract types menu | Services ‣ Types (category) | same | same | same | Configuration ‣ Contracts ‣ Contract Types |
| Service date | `date` | same | same | same | `date_from`, `date_to` |
| Lower odometer on vehicle | allowed | allowed | refused | refused | refused |
| Reporting ‣ Odometers | no | no | no | yes | yes |
| Employee's driver contact | `address_home_id` | `work_contact_id` | same | same | same |
| Mobility card on employee | yes | yes | yes | yes | no |
| Bill line to service | first post only, amount copied | same | linked to the line | same | same, plus Requires vehicle and Create Bill |

## Verify

```python
vehicle.invalidate_recordset()
print(vehicle.name, vehicle.state_id.name, vehicle.driver_id.name, vehicle.odometer, vehicle.contract_state)
if 'driver_employee_id' in vehicle._fields:
    print(vehicle.driver_employee_id.name)
print(vehicle.log_drivers.read(['driver_id', 'date_start', 'date_end']))
print(vehicle.log_contracts.read(['name', 'state', 'start_date', 'expiration_date', 'cost_generated', 'cost_frequency']))
print(vehicle.log_services.read(['service_type_id', 'state', 'amount', 'vendor_id']))
print(env['fleet.vehicle.odometer'].search_read([('vehicle_id', '=', vehicle.id)], ['date', 'value'], order='value desc'))
```

## Pitfalls

- A new contract shows as running up to 19.0 even when it starts next month: the daily
  scheduled action (Fleet: Generate contracts costs based on costs frequency) fixes it.
  Run `env['fleet.vehicle.log.contract'].scheduler_manage_contract_expiration()` to
  apply it now.
- Renewal activities go only to contracts with a Responsible (`user_id`) that are
  `open`; set it on every contract.
- The driver is a contact. With `hr_fleet`, choosing an employee without a work contact
  (16.0: without private address) leaves the driver empty; 16.0 also refuses to clear
  the private address of an employee who drives a vehicle.
- A vehicle on a bill line creates a service only for vendor bills (`in_invoice`), not
  refunds or receipts, and only at posting. Up to 17.0, resetting a posted bill to draft
  and posting it again creates no new service.
- Archiving a vehicle archives its contracts and services.
- 18.0 and later: a service created from a bill cannot be deleted while the bill line
  exists; remove the vehicle from the line instead.
