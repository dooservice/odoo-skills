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
- `equipment_ids` One2many → `maintenance.equipment` “Equipment”
- `equipment_count` Integer “Equipment Count” (compute=_compute_equipment_count)
- `maintenance_ids` One2many → `maintenance.request`
- `maintenance_count` Integer “Maintenance Count” (compute=_compute_maintenance_count)
- `maintenance_open_count` Integer “Current Maintenance” (compute=_compute_maintenance_count)
- `alias_id` Many2one
- `fold` Boolean “Folded in Maintenance Pipe” (store, compute=_compute_fold)

## `maintenance.mixin` (defines)

Maintenance Maintained Item

- `company_id` Many2one → `res.company` “Company”
- `effective_date` Date “Effective Date” (required)
- `maintenance_team_id` Many2one → `maintenance.team` “Maintenance Team” (store, compute=_compute_maintenance_team_id)
- `technician_user_id` Many2one → `res.users` “Technician”
- `maintenance_ids` One2many → `maintenance.request`
- `maintenance_count` Integer “Maintenance Count” (store, compute=_compute_maintenance_count)
- `maintenance_open_count` Integer “Current Maintenance” (store, compute=_compute_maintenance_count)
- `expected_mtbf` Integer “Expected MTBF”
- `mtbf` Integer “MTBF” (compute=_compute_maintenance_request)
- `mttr` Integer “MTTR” (compute=_compute_maintenance_request)
- `estimated_next_failure` Date “Estimated time before next failure (in days)” (compute=_compute_maintenance_request)
- `latest_failure_date` Date “Latest Failure Date” (compute=_compute_maintenance_request)

## `maintenance.equipment` (defines)

Maintenance Equipment

Inherits: `mail.thread`, `mail.activity.mixin`, `maintenance.mixin`

- `name` Char “Equipment Name” (required)
- `active` Boolean
- `owner_user_id` Many2one → `res.users` “Owner”
- `category_id` Many2one → `maintenance.equipment.category` “Equipment Category”
- `partner_id` Many2one → `res.partner` “Vendor”
- `partner_ref` Char “Vendor Reference”
- `location` Char “Location”
- `model` Char “Model”
- `serial_no` Char “Serial Number”
- `assign_date` Date “Assigned Date”
- `cost` Float “Cost”
- `note` Html “Note”
- `warranty_date` Date “Warranty Expiration Date”
- `color` Integer “Color Index”
- `scrap_date` Date “Scrap Date”
- `maintenance_ids` One2many → `maintenance.request`

Public methods: `create`, `write`

## `maintenance.request` (defines)

Maintenance Request

Inherits: `mail.thread.cc`, `mail.activity.mixin`

- `name` Char “Subjects” (required)
- `company_id` Many2one → `res.company` “Company” (required)
- `description` Html “Description”
- `request_date` Date “Request Date”
- `owner_user_id` Many2one → `res.users` “Created by User”
- `category_id` Many2one → `maintenance.equipment.category` “Category” (readonly, store, related=equipment_id.category_id)
- `equipment_id` Many2one → `maintenance.equipment` “Equipment” (index)
- `user_id` Many2one → `res.users` “Technician” (store, compute=_compute_user_id)
- `stage_id` Many2one → `maintenance.stage` “Stage”
- `priority` Selection “Priority”
- `color` Integer “Color Index”
- `close_date` Date “Close Date”
- `kanban_state` Selection “Kanban State” (required)
- `archive` Boolean
- `maintenance_type` Selection “Maintenance Type”
- `schedule_date` Datetime “Scheduled Date”
- `maintenance_team_id` Many2one → `maintenance.team` “Team” (required, store, compute=_compute_maintenance_team_id)
- `duration` Float
- `done` Boolean (related=stage_id.done)
- `instruction_type` Selection “Instruction”
- `instruction_pdf` Binary “PDF”
- `instruction_google_slide` Char “Google Slide”
- `instruction_text` Html “Text”
- `recurring_maintenance` Boolean “Recurrent” (store, compute=_compute_recurring_maintenance)
- `repeat_interval` Integer “Repeat Every”
- `repeat_unit` Selection
- `repeat_type` Selection “Until”
- `repeat_until` Date “End Date”

Public methods: `activity_update`, `archive_equipment_request`, `create`, `reset_equipment_request`, `write`

Extension points: `_check_repeat_interval`, `_get_activity_note`, `_get_default_team_id`

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

## `res.config.settings` (extends)

- `module_maintenance_worksheet` Boolean “Custom Maintenance Worksheets”
