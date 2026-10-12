# hr_maintenance — Maintenance - HR

Depends on: hr, maintenance.

## `maintenance.equipment` (extends)

- `employee_id` Many2one → `hr.employee` “Assigned Employee” (store, compute=_compute_equipment_assignment_fields)
- `department_id` Many2one → `hr.department` “Assigned Department” (store, compute=_compute_equipment_assignment_fields)
- `equipment_assign_to` Selection (required)

Public methods: `create`, `write`

Extension points: `_get_assign_fields`, `_get_assignment_handlers_by_equipment_assign_to`, `_get_owner_methods_by_equipment_assign_to`

## `maintenance.request` (extends)

- `employee_id` Many2one → `hr.employee` “Employee”
- `owner_user_id` Many2one (store, compute=_compute_owner)
- `equipment_id` Many2one

Public methods: `create`, `message_new`, `write`

## `hr.employee` (extends)

- `equipment_ids` One2many → `maintenance.equipment`
- `equipment_count` Integer “Equipment Count” (compute=_compute_equipment_count)

## `hr.employee.departure` (extends)


Public methods: `action_register`

## `hr.employee.public` (extends)

- `equipment_count` Integer (related=employee_id.equipment_count)
