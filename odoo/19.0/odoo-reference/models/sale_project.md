# sale_project — Sales - Project

Depends on: sale_management, sale_service, project_account.

## `account.move` (extends)


Extension points: `_get_action_per_item`

## `account.move.line` (extends)


Extension points: `_get_so_mapping_domain`, `_get_so_mapping_from_project`

## `product.product` (extends)


Public methods: `write`

## `product.template` (extends)

- `service_tracking` Selection
- `project_id` Many2one → `project.project` (company_dependent)
- `project_template_id` Many2one → `project.project` (company_dependent)
- `task_template_id` Many2one → `project.task` (store, company_dependent, compute=_compute_task_template)
- `service_policy` Selection “Service Invoicing Policy” (compute=_compute_service_policy)
- `service_type` Selection

Public methods: `write`

Extension points: `_check_project_and_template`, `_get_general_to_service`, `_get_general_to_service_map`, `_get_saleable_tracking_types`, `_get_service_to_general`, `_get_service_to_general_map`, `_prepare_invoicing_tooltip`, `_prepare_service_tracking_tooltip`

## `project.milestone` (extends)

- `allow_billable` Boolean (related=project_id.allow_billable)
- `project_partner_id` Many2one (related=project_id.partner_id)
- `sale_line_id` Many2one → `sale.order.line`
- `quantity_percentage` Float “Quantity (%)” (store, compute=_compute_quantity_percentage)
- `sale_line_display_name` Char “Sale Line Display Name” (related=sale_line_id.display_name)
- `product_uom_id` Many2one (related=sale_line_id.product_uom_id)
- `product_uom_qty` Float “Quantity” (compute=_compute_product_uom_qty)

Public methods: `action_view_sale_order`

Extension points: `_get_fields_to_export`

## `project.project` (extends)

- `allow_billable` Boolean “Billable”
- `sale_line_id` Many2one → `sale.order.line` (store, compute=_compute_sale_line_id)
- `sale_order_id` Many2one (related=sale_line_id.order_id)
- `has_any_so_to_invoice` Boolean “Has SO to Invoice” (compute=_compute_has_any_so_to_invoice)
- `sale_order_line_count` Integer (compute=_compute_sale_order_count)
- `sale_order_count` Integer (compute=_compute_sale_order_count)
- `has_any_so_with_nothing_to_invoice` Boolean “Has a SO with an invoice status of No” (compute=_compute_has_any_so_with_nothing_to_invoice)
- `invoice_count` Integer (compute=_compute_invoice_count)
- `vendor_bill_count` Integer (related=account_id.vendor_bill_count)
- `partner_id` Many2one (store, compute=_compute_partner_id)
- `display_sales_stat_buttons` Boolean (compute=_compute_display_sales_stat_buttons)
- `sale_order_state` Selection (related=sale_order_id.state)
- `reinvoiced_sale_order_id` Many2one → `sale.order` “Sales Order”

Public methods: `action_create_invoice`, `action_customer_preview`, `action_get_list_view`, `action_open_project_invoices`, `action_open_project_vendor_bills`, `action_profitability_items`, `action_view_sols`, `action_view_sos`, `action_view_tasks`, `create`, `default_get`, `get_panel_data`, `get_sale_items_data`, `template_to_project_confirmation_callback`, `write`

Extension points: `_get_domain_from_section_id`, `_get_foldable_section`, `_get_hide_partner`, `_get_items_from_invoices`, `_get_items_from_invoices_domain`, `_get_profitability_items`, `_get_profitability_labels`, `_get_profitability_sale_order_items_domain`, `_get_profitability_sequence_per_invoice_type`, `_get_profitability_values`, `_get_projects_for_invoice_status`, `_get_projects_to_make_billable_domain`, `_get_revenues_items_from_sol`, `_get_sale_items_domain`, `_get_sale_order_items`, `_get_sale_order_items_query`, `_get_sale_orders`, `_get_sale_orders_domain`, `_get_service_policy_to_invoice_type`, `_get_stat_buttons`, `_get_template_default_context_whitelist`, `_get_template_to_project_confirmation_callbacks`, `_get_template_to_project_warnings`, `_get_view_action`

## `project.task` (extends)

- `sale_order_id` Many2one → `sale.order` (store, compute=_compute_sale_order_id)
- `sale_line_id` Many2one → `sale.order.line` (store, compute=_compute_sale_line)
- `project_sale_order_id` Many2one → `sale.order` “Project's sale order” (related=project_id.sale_order_id)
- `sale_order_state` Selection (related=sale_order_id.state)
- `task_to_invoice` Boolean “To invoice” (compute=_compute_task_to_invoice)
- `allow_billable` Boolean (related=project_id.allow_billable)
- `partner_id` Many2one
- `display_sale_order_button` Boolean “Display Sales Order” (compute=_compute_display_sale_order_button)

Public methods: `TASK_PORTAL_READABLE_FIELDS`, `action_project_sharing_view_so`, `action_view_so`, `create`, `default_get`, `write`

Extension points: `_check_sale_line_type`, `_get_action_view_so_ids`, `_get_projects_to_make_billable_domain`, `_get_template_default_context_whitelist`

## `project.task.recurrence` (extends)


Extension points: `_get_recurring_fields_to_copy`

## `project.task.type` (extends)

- `show_rating_active` Boolean (compute=_compute_show_rating_active)

## `project.update` (extends)


Extension points: `_get_template_values`

## `sale.order` (extends)

- `tasks_ids` Many2many → `project.task` “Tasks associated with this sale” (compute=_compute_tasks_ids)
- `tasks_count` Integer “Tasks” (compute=_compute_tasks_ids)
- `visible_project` Boolean “Display project” (readonly, compute=_compute_visible_project)
- `project_ids` Many2many → `project.project` “Projects” (compute=_compute_project_ids)
- `project_count` Integer “Number of Projects” (compute=_compute_project_ids)
- `milestone_count` Integer (compute=_compute_milestone_count)
- `is_product_milestone` Boolean (compute=_compute_is_product_milestone)
- `show_create_project_button` Boolean (compute=_compute_show_project_and_task_button)
- `show_project_button` Boolean (compute=_compute_show_project_and_task_button)
- `closed_task_count` Integer (compute=_compute_tasks_ids)
- `completed_task_percentage` Float (compute=_compute_completed_task_percentage)
- `project_id` Many2one → `project.project`
- `project_account_id` Many2one → `account.analytic.account` (related=project_id.account_id)

Public methods: `action_confirm`, `action_create_project`, `action_view_milestone`, `action_view_project_ids`, `create`, `default_get`, `get_first_service_line`, `write`

Extension points: `_action_confirm`

## `sale.order.line` (extends)

- `qty_delivered_method` Selection
- `project_id` Many2one → `project.project` (index)
- `task_id` Many2one → `project.task` (index)
- `reached_milestones_ids` One2many → `project.milestone` “Reached Milestones”

Public methods: `copy_data`, `create`, `default_get`, `write`

Extension points: `_get_action_per_item`, `_get_product_from_sol_name_domain`, `_get_product_service_policy`, `_get_sale_order_partner_id`, `_get_so_lines_new_project`, `_get_so_lines_task_global_project`, `_prepare_invoice_line`, `_prepare_procurement_values`, `_prepare_qty_delivered`, `_prepare_task_template_vals`

## `sale.order.template.line` (extends)


Extension points: `_prepare_order_line_values`

## `report.project.task.user` (extends)

- `sale_line_id` Many2one → `sale.order.line` “Sales Order Item” (readonly)
- `sale_order_id` Many2one → `sale.order` “Sales Order” (readonly)

## `sale.report` (extends)

- `project_id` Many2one → `project.project` (readonly)

## `project.template.create.wizard` (extends)

- `partner_id` Many2one → `res.partner`
- `allow_billable` Boolean (related=template_id.allow_billable)
- `role_to_users_ids` One2many (store, compute=_compute_role_to_users_ids)

Public methods: `action_create_project_from_so`, `action_open_template_view`

Extension points: `_get_template_whitelist_fields`
