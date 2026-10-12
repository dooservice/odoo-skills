# maintenance — Maintenance

Depends on: mail.

## `maintenance.stage` (defines)

Maintenance Stage

- `name` Char “Name” (required)
- `sequence` Integer “Sequence”
- `fold` Boolean “Folded in Maintenance Pipe”
- `maintenance_team_ids` Many2many → `maintenance.team` “Maintenance Teams”

## `maintenance.equipment.category` (defines)

Maintenance Equipment Category

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
- `fold` Boolean “Folded in Maintenance Pipe” (store, compute=_compute_fold)
- `equipment_properties_definition` PropertiesDefinition “Equipment Properties”

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
- `owner_user_id` Many2one → `res.users` “Owner” (store, compute=_compute_owner)
- `category_id` Many2one → `maintenance.equipment.category` “Equipment Category”
- `partner_id` Many2one → `res.partner` “Vendor”
- `partner_ref` Char “Vendor Reference”
- `model` Char “Model”
- `serial_no` Char “Serial Number”
- `assign_date` Date “Assigned Date” (store, compute=_compute_equipment_assignment_fields)
- `cost` Float “Cost”
- `note` Html “Note”
- `warranty_date` Date “Warranty Expiration Date”
- `color` Integer “Color Index”
- `scrap_date` Date “Scrap Date”
- `maintenance_ids` One2many → `maintenance.request`
- `equipment_properties` Properties “Properties”
- `equipment_assign_to` Selection “Used By”
- `is_assigned` Boolean (compute=_compute_is_assigned)
- `technician_user_id` Many2one
- `equipment_req_properties_definition` PropertiesDefinition “Maintenance Request Properties”

Public methods: `create`, `write`

Extension points: `_get_assign_fields`, `_get_assignment_handlers_by_equipment_assign_to`, `_get_owner_methods_by_equipment_assign_to`

## `maintenance.request` (defines)

Maintenance Request

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Subjects” (required)
- `company_id` Many2one → `res.company` “Company” (required)
- `description` Html “Description”
- `owner_user_id` Many2one → `res.users` “Created by User”
- `category_id` Many2one → `maintenance.equipment.category` “Category” (readonly, store, related=equipment_id.category_id)
- `equipment_id` Many2one → `maintenance.equipment` “Equipment” (index)
- `user_ids` Many2many → `res.users` “Technicians” (store, compute=_compute_user_ids)
- `stage_id` Many2one → `maintenance.stage` “Stage” (store, compute=_compute_stage_id)
- `priority` Selection “Priority”
- `color` Integer “Color Index”
- `close_date` Date “Close Date”
- `state` Selection “State” (required)
- `maintenance_type` Selection “Maintenance Type”
- `schedule_date` Datetime “Scheduled Date”
- `schedule_end` Datetime “Scheduled End” (store, compute=_compute_schedule_end)
- `maintenance_team_id` Many2one → `maintenance.team` “Team” (required, store, index, compute=_compute_maintenance_team_id)
- `duration` Float (store, compute=_compute_duration)
- `instruction_text` Html “Text”
- `recurring_maintenance` Boolean “Recurrent” (store, compute=_compute_recurring_maintenance)
- `repeat_interval` Integer “Repeat Every”
- `repeat_unit` Selection
- `repeat_type` Selection “Until”
- `repeat_until` Date “End Date”
- `equipment_req_properties` Properties “Maintenance Request Properties”

Public methods: `cancel_equipment_request`, `create`, `reset_equipment_request`, `write`

Extension points: `_check_repeat_interval`, `_check_schedule_interval`, `_get_default_team_id`

## `maintenance.team` (defines)

Maintenance Team

Inherits: `mail.alias.mixin`, `mail.thread`

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
- `todo_request_count_changes_requested` Integer “Number of Requests with Changes Requested” (compute=_compute_todo_requests)
- `todo_request_count_unscheduled` Integer “Number of Requests Unscheduled” (compute=_compute_todo_requests)
- `alias_id` Many2one

## `res.config.settings` (extends)

- `module_maintenance_worksheet` Boolean “Custom Maintenance Worksheets”
