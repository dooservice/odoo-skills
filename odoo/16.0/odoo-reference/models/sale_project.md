# sale_project — Sales - Project

Depends on: sale_management, project.

## `account.move.line` (extends)


## `product.template` (extends)

- `service_tracking` Selection “Create on Order”
- `project_id` Many2one → `project.project` (company_dependent)
- `project_template_id` Many2one → `project.project` (company_dependent)
- `service_policy` Selection “Service Invoicing Policy” (compute=_compute_service_policy)
- `service_type` Selection

Public methods: `write`

Extension points: `_check_project_and_template`, `_get_general_to_service`, `_get_general_to_service_map`, `_get_service_to_general`, `_get_service_to_general_map`

## `product.product` (extends)


Public methods: `write`

## `project.project` (extends)

- `allow_billable` Boolean “Billable”
- `sale_line_id` Many2one → `sale.order.line` (store, compute=_compute_sale_line_id)
- `sale_order_id` Many2one “Sales Order” (related=sale_line_id.order_id)
- `has_any_so_to_invoice` Boolean “Has SO to Invoice” (compute=_compute_has_any_so_to_invoice)
- `sale_order_count` Integer (compute=_compute_sale_order_count)
- `has_any_so_with_nothing_to_invoice` Boolean “Has a SO with an invoice status of No” (compute=_compute_has_any_so_with_nothing_to_invoice)
- `invoice_count` Integer (compute=_compute_invoice_count)
- `vendor_bill_count` Integer (related=analytic_account_id.vendor_bill_count)

Public methods: `action_create_invoice`, `action_get_list_view`, `action_open_project_invoices`, `action_open_project_vendor_bills`, `action_profitability_items`, `action_view_sos`, `get_panel_data`, `get_sale_items_data`

Extension points: `_get_profitability_items`, `_get_profitability_labels`, `_get_profitability_sale_order_items_domain`, `_get_profitability_sequence_per_invoice_type`, `_get_projects_for_invoice_status`, `_get_revenues_items_from_invoices`, `_get_revenues_items_from_invoices_domain`, `_get_revenues_items_from_sol`, `_get_sale_items`, `_get_sale_items_domain`, `_get_sale_order_items`, `_get_sale_order_items_query`, `_get_sale_orders`, `_get_service_policy_to_invoice_type`, `_get_stat_buttons`

## `project.task` (extends)

- `sale_order_id` Many2one → `sale.order` (store, compute=_compute_sale_order_id)
- `sale_line_id` Many2one → `sale.order.line` (store, compute=_compute_sale_line)
- `project_sale_order_id` Many2one → `sale.order` “Project's sale order” (related=project_id.sale_order_id)
- `task_to_invoice` Boolean “To invoice” (compute=_compute_task_to_invoice)
- `display_sale_order_button` Boolean “Display Sales Order” (compute=_compute_display_sale_order_button)

Public methods: `SELF_READABLE_FIELDS`, `action_project_sharing_view_so`, `action_view_so`

Extension points: `_check_sale_line_type`, `_get_action_view_so_ids`

## `project.task.recurrence` (extends)


Extension points: `_get_sale_line_id`

## `project.milestone` (extends)

- `allow_billable` Boolean (related=project_id.allow_billable)
- `project_partner_id` Many2one (related=project_id.partner_id)
- `sale_line_id` Many2one → `sale.order.line`
- `quantity_percentage` Float “Quantity”
- `sale_line_name` Text (related=sale_line_id.name)

Extension points: `_get_fields_to_export`

## `res.config.settings` (extends)


Public methods: `set_values`

## `sale.order` (extends)

- `tasks_ids` Many2many → `project.task` “Tasks associated to this sale” (compute=_compute_tasks_ids)
- `tasks_count` Integer “Tasks” (compute=_compute_tasks_ids)
- `visible_project` Boolean “Display project” (readonly, compute=_compute_visible_project)
- `project_id` Many2one → `project.project` (readonly)
- `project_ids` Many2many → `project.project` “Projects” (compute=_compute_project_ids)
- `project_count` Integer “Number of Projects” (compute=_compute_project_ids)
- `milestone_count` Integer (compute=_compute_milestone_count)
- `is_product_milestone` Boolean (compute=_compute_is_product_milestone)

Public methods: `action_view_milestone`, `action_view_project_ids`, `action_view_task`, `write`

Extension points: `_action_confirm`, `_prepare_analytic_account_data`

## `sale.order.line` (extends)

- `qty_delivered_method` Selection
- `project_id` Many2one → `project.project` (index)
- `task_id` Many2one → `project.task` (index)
- `is_service` Boolean “Is a Service” (store, compute=_compute_is_service)
- `reached_milestones_ids` One2many → `project.milestone` “Reached Milestones”

Public methods: `create`, `name_get`, `write`

Extension points: `_get_action_per_item`, `_prepare_invoice_line`

## `sale.order.template.line` (extends)


Extension points: `_prepare_order_line_values`

## `report.project.task.user` (extends)

- `sale_line_id` Many2one → `sale.order.line` “Sales Order Item” (readonly)
- `sale_order_id` Many2one → `sale.order` “Sales Order” (readonly)
