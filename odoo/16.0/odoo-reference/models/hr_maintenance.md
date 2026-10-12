# hr_maintenance — Maintenance - HR

Depends on: hr, maintenance.

## `maintenance.equipment` (extends)

- `employee_id` Many2one → `hr.employee` “Assigned Employee” (store, compute=_compute_equipment_assign)
- `department_id` Many2one → `hr.department` “Assigned Department” (store, compute=_compute_equipment_assign)
- `equipment_assign_to` Selection “Used By” (required)
- `owner_user_id` Many2one (store, compute=_compute_owner)
- `assign_date` Date (store, compute=_compute_equipment_assign)

Public methods: `create`, `write`

## `maintenance.request` (extends)

- `employee_id` Many2one → `hr.employee` “Employee”
- `owner_user_id` Many2one (store, compute=_compute_owner)
- `equipment_id` Many2one

Public methods: `create`, `message_new`, `write`

## `res.users` (extends)

- `equipment_ids` One2many → `maintenance.equipment` “Managed Equipments”
- `equipment_count` Integer “Assigned Equipments” (related=employee_id.equipment_count)

Public methods: `SELF_READABLE_FIELDS`

## `hr.employee` (extends)

- `equipment_ids` One2many → `maintenance.equipment`
- `equipment_count` Integer “Equipments” (compute=_compute_equipment_count)
