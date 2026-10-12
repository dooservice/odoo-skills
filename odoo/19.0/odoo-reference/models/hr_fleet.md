# hr_fleet — Fleet History

Depends on: hr, fleet.

## `hr.employee` (extends)

- `employee_cars_count` Integer “Cars” (compute=_compute_employee_cars_count)
- `car_ids` One2many → `fleet.vehicle` “Vehicles (private)”
- `license_plate` Char (compute=_compute_license_plate)
- `mobility_card` Char

Public methods: `action_open_employee_cars`, `write`

Extension points: `_check_work_contact_id`

## `hr.employee.public` (extends)

- `mobility_card` Char (readonly)

## `fleet.vehicle` (extends)

- `mobility_card` Char (store, compute=_compute_mobility_card)
- `driver_employee_id` Many2one → `hr.employee` (store, compute=_compute_driver_employee_id)
- `driver_employee_name` Char (related=driver_employee_id.name)
- `future_driver_employee_id` Many2one → `hr.employee` (store, compute=_compute_future_driver_employee_id)

Public methods: `action_open_employee`, `create`, `open_assignation_logs`, `write`

## `fleet.vehicle.assignation.log` (extends)

- `driver_employee_id` Many2one → `hr.employee` “Driver (Employee)” (store, compute=_compute_driver_employee_id)
- `attachment_number` Integer “Number of Attachments” (compute=_compute_attachment_number)

Public methods: `action_get_attachment_view`

## `fleet.vehicle.log.contract` (extends)

- `purchaser_employee_id` Many2one “Driver (Employee)” (related=vehicle_id.driver_employee_id)

Public methods: `action_open_employee`

## `fleet.vehicle.log.services` (extends)

- `purchaser_employee_id` Many2one → `hr.employee` “Driver (Employee)” (store, compute=_compute_purchaser_employee_id)

## `fleet.vehicle.odometer` (extends)

- `driver_employee_id` Many2one “Driver (Employee)” (readonly, related=vehicle_id.driver_employee_id)

## `ir.attachment` (extends)


Public methods: `action_preview_attachment`

## `mail.activity.plan.template` (extends)

- `responsible_type` Selection

Extension points: `_check_responsible_hr_fleet`

## `hr.departure.wizard` (extends)

- `release_campany_car` Boolean “Release Company Car”

Public methods: `action_register_departure`
