# fleet_maintenance — Maintenance - Fleet

Depends on: fleet, maintenance.

## `fleet.vehicle` (extends)

- `equipment_ids` One2many → `maintenance.equipment`
- `equipment_count` Integer “Equipment Count” (compute=_compute_equipment_count)

## `maintenance.equipment` (extends)

- `equipment_assign_to` Selection (required)
- `vehicle_id` Many2one → `fleet.vehicle` “Vehicle” (store, compute=_compute_equipment_assignment_fields)

Extension points: `_get_assign_fields`, `_get_assignment_handlers_by_equipment_assign_to`, `_get_owner_methods_by_equipment_assign_to`
