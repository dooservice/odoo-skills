# maintenance — Maintenance

Depends on: mail.

## `maintenance.stage` (defines)

Maintenance Stage

- `name` Char “Name” (required)
- `sequence` Integer “Sequence”
- `fold` Boolean “Folded in Maintenance Pipe”
- `done` Boolean “Request Done”

## `maintenance.equipment.category` (defines)

Maintenance Equipment Category

Inherits: `mail.alias.mixin`, `mail.thread`

- `name` Char “Category Name” (required)
- `company_id` Many2one → `res.company` “Company”
- `technician_user_id` Many2one → `res.users`
- `color` Integer “Color Index”
- `note` Html “Comments”
- `equipment_ids` One2many → `maintenance.equipment` “Equipments”
- `equipment_count` Integer “Equipment” (compute=_compute_equipment_count)
- `maintenance_ids` One2many → `maintenance.request`
- `maintenance_count` Integer “Maintenance Count” (compute=_compute_maintenance_count)
- `alias_id` Many2one → `mail.alias` (required)
- `fold` Boolean “Folded in Maintenance Pipe” (store, compute=_compute_fold)

## `maintenance.equipment` (defines)

Maintenance Equipment

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Equipment Name” (required)
- `company_id` Many2one → `res.company` “Company”
- `active` Boolean
- `technician_user_id` Many2one → `res.users` “Technician”
- `owner_user_id` Many2one → `res.users` “Owner”
- `category_id` Many2one → `maintenance.equipment.category` “Equipment Category”
- `partner_id` Many2one → `res.partner` “Vendor”
- `partner_ref` Char “Vendor Reference”
- `location` Char “Location”
- `model` Char “Model”
- `serial_no` Char “Serial Number”
- `assign_date` Date “Assigned Date”
- `effective_date` Date “Effective Date” (required)
- `cost` Float “Cost”
- `note` Html “Note”
- `warranty_date` Date “Warranty Expiration Date”
- `color` Integer “Color Index”
- `scrap_date` Date “Scrap Date”
- `maintenance_ids` One2many → `maintenance.request`
- `maintenance_count` Integer “Maintenance Count” (store, compute=_compute_maintenance_count)
- `maintenance_open_count` Integer “Current Maintenance” (store, compute=_compute_maintenance_count)
- `period` Integer “Days between each preventive maintenance”
- `next_action_date` Date “Date of the next preventive maintenance” (store, compute=_compute_next_maintenance)
- `maintenance_team_id` Many2one → `maintenance.team` “Maintenance Team”
- `maintenance_duration` Float

Public methods: `create`, `name_get`, `write`

Extension points: `_create_new_request`, `_prepare_maintenance_request_vals`

## `maintenance.request` (defines)

Maintenance Request

Inherits: `mail.thread.cc`, `mail.activity.mixin`

- `name` Char “Subjects” (required)
- `company_id` Many2one → `res.company` “Company”
- `description` Html “Description”
- `request_date` Date “Request Date”
- `owner_user_id` Many2one → `res.users` “Created by User”
- `category_id` Many2one → `maintenance.equipment.category` “Category” (readonly, store, related=equipment_id.category_id)
- `equipment_id` Many2one → `maintenance.equipment` “Equipment” (index)
- `user_id` Many2one → `res.users` “Technician”
- `stage_id` Many2one → `maintenance.stage` “Stage”
- `priority` Selection “Priority”
- `color` Integer “Color Index”
- `close_date` Date “Close Date”
- `kanban_state` Selection “Kanban State” (required)
- `archive` Boolean
- `maintenance_type` Selection “Maintenance Type”
- `schedule_date` Datetime “Scheduled Date”
- `maintenance_team_id` Many2one → `maintenance.team` “Team” (required)
- `duration` Float
- `done` Boolean (related=stage_id.done)

Public methods: `activity_update`, `archive_equipment_request`, `create`, `onchange_category_id`, `onchange_equipment_id`, `reset_equipment_request`, `write`

Extension points: `_get_default_team_id`

## `maintenance.team` (defines)

Maintenance Teams

- `name` Char “Team Name” (required)
- `active` Boolean
- `company_id` Many2one → `res.company` “Company”
- `member_ids` Many2many → `res.users` “Team Members”
- `color` Integer “Color Index”
- `request_ids` One2many → `maintenance.request`
- `equipment_ids` One2many → `maintenance.equipment`
- `todo_request_ids` One2many → `maintenance.request` “Requests” (compute=_compute_todo_requests)
- `todo_request_count` Integer “Number of Requests” (compute=_compute_todo_requests)
- `todo_request_count_date` Integer “Number of Requests Scheduled” (compute=_compute_todo_requests)
- `todo_request_count_high_priority` Integer “Number of Requests in High Priority” (compute=_compute_todo_requests)
- `todo_request_count_block` Integer “Number of Requests Blocked” (compute=_compute_todo_requests)
- `todo_request_count_unscheduled` Integer “Number of Requests Unscheduled” (compute=_compute_todo_requests)
