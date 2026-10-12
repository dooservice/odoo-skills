# crm_sale_project — CRM - Project

Depends on: sale_project, crm.

## `crm.lead` (extends)

- `project_ids` One2many → `project.project`
- `project_count` Integer (compute=_compute_project_count)
- `task_count` Integer (compute=_compute_task_count)

Public methods: `action_create_project`, `action_view_project_ids`

Extension points: `_get_project_create_from_lead_context`, `_prepare_opportunity_quotation_context`

## `project.project` (extends)

- `lead_id` Many2one → `crm.lead` (index)

Public methods: `action_view_lead`, `default_get`

Extension points: `_get_template_default_context_whitelist`

## `sale.order` (extends)


Public methods: `create`

## `project.template.create.wizard` (extends)

- `customer_action` Selection “Project Customer”
- `is_customer_action_visible` Boolean (compute=_compute_customer_action_visibility)

Public methods: `action_create_project_from_lead`, `action_open_template_view`
