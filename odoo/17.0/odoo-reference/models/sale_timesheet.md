# sale_timesheet — Sales Timesheet

Depends on: sale_project, hr_timesheet.

## `account.analytic.line` (extends)

- `timesheet_invoice_type` Selection “Billable Type” (readonly, store, compute=_compute_timesheet_invoice_type)
- `commercial_partner_id` Many2one → `res.partner` (compute=_compute_commercial_partner)
- `timesheet_invoice_id` Many2one → `account.move` “Invoice” (readonly)
- `so_line` Many2one (store, compute=_compute_so_line)
- `order_id` Many2one (readonly, store, index, related=so_line.order_id)
- `is_so_line_edited` Boolean “Is Sales Order Item Manually Edited”
- `allow_billable` Boolean (related=project_id.allow_billable)

Public methods: `action_invoice_from_timesheet`, `action_sale_order_from_timesheet`

Extension points: `_check_can_write`, `_check_timesheet_can_be_billed`, `_get_employee_mapping_entry`, `_get_timesheets_to_merge`

## `account.move` (extends)

- `timesheet_ids` One2many → `account.analytic.line` “Timesheets” (readonly)
- `timesheet_count` Integer “Number of timesheets” (compute=_compute_timesheet_count)
- `timesheet_encode_uom_id` Many2one → `uom.uom` (related=company_id.timesheet_encode_uom_id)
- `timesheet_total_duration` Integer “Timesheet Total Duration” (compute=_compute_timesheet_total_duration)

Public methods: `action_post`, `action_view_timesheet`

## `account.move.line` (extends)


Public methods: `unlink`

## `account.move.reversal` (extends)


Public methods: `reverse_moves`

## `hr.employee` (extends)


Public methods: `default_get`

## `product.template` (extends)

- `service_type` Selection
- `project_id` Many2one
- `project_template_id` Many2one
- `service_upsell_threshold` Float “Threshold”
- `service_upsell_threshold_ratio` Char (compute=_compute_service_upsell_threshold_ratio)

Public methods: `write`

Extension points: `_get_onchange_service_policy_updates`, `_get_service_to_general_map`

## `product.product` (extends)


Public methods: `write`

Extension points: `_get_default_uom_id`

## `project.project` (extends)

- `pricing_type` Selection “Pricing” (compute=_compute_pricing_type)
- `sale_line_employee_ids` One2many → `project.sale.line.employee.map`
- `billable_percentage` Integer (compute=_compute_billable_percentage)
- `timesheet_product_id` Many2one → `product.product` “Timesheet Product” (store, compute=_compute_timesheet_product_id)
- `warning_employee_rate` Boolean (compute=_compute_warning_employee_rate)
- `partner_id` Many2one (store, compute=_compute_partner_id)
- `allocated_hours` Float
- `billing_type` Selection (required, store, compute=_compute_billing_type)

Public methods: `action_billable_time_button`, `action_make_billable`, `action_profitability_items`, `action_view_timesheet`, `default_get`, `get_panel_data`, `write`

Extension points: `_check_sale_line_type`, `_get_domain_aal_with_no_move_line`, `_get_profitability_aal_domain`, `_get_profitability_items`, `_get_profitability_items_from_aal`, `_get_profitability_labels`, `_get_profitability_sequence_per_invoice_type`, `_get_sale_order_items_query`, `_get_service_policy_to_invoice_type`, `_get_view`

## `project.task` (extends)

- `sale_order_id` Many2one
- `so_analytic_account_id` Many2one “Sale Order Analytic Account” (related=sale_order_id.analytic_account_id)
- `pricing_type` Selection (related=project_id.pricing_type)
- `is_project_map_empty` Boolean “Is Project map empty” (compute=_compute_is_project_map_empty)
- `has_multi_sol` Boolean (compute=_compute_has_multi_sol)
- `timesheet_product_id` Many2one (related=project_id.timesheet_product_id)
- `remaining_hours_so` Float “Remaining Hours on SO” (compute=_compute_remaining_hours_so)
- `remaining_hours_available` Boolean (related=sale_line_id.remaining_hours_available)

Public methods: `SELF_READABLE_FIELDS`

Extension points: `_get_action_view_so_ids`, `_get_default_partner_id`, `_get_last_sol_of_customer`, `_get_timesheet`

## `project.task.recurrence` (extends)


Extension points: `_get_recurring_fields_to_copy`

## `project.sale.line.employee.map` (defines)

Project Sales line, employee mapping

- `project_id` Many2one → `project.project` (required)
- `employee_id` Many2one → `hr.employee` (required)
- `existing_employee_ids` Many2many → `hr.employee` (compute=_compute_existing_employee_ids)
- `sale_line_id` Many2one → `sale.order.line` (store, compute=_compute_sale_line_id)
- `sale_order_id` Many2one (related=project_id.sale_order_id)
- `company_id` Many2one → `res.company` “Company” (related=project_id.company_id)
- `partner_id` Many2one (related=project_id.partner_id)
- `price_unit` Float “Unit Price” (readonly, store, compute=_compute_price_unit)
- `currency_id` Many2one → `res.currency` “Currency” (store, compute=_compute_currency_id)
- `cost` Monetary (store, compute=_compute_cost)
- `display_cost` Monetary “Hourly Cost” (compute=_compute_display_cost)
- `cost_currency_id` Many2one → `res.currency` “Cost Currency” (readonly, related=employee_id.currency_id)
- `is_cost_changed` Boolean “Is Cost Manually Changed” (store, compute=_compute_is_cost_changed)

Public methods: `create`, `write`

Extension points: `_get_working_hours_per_calendar`

## `project.update` (extends)


Extension points: `_get_profitability_values`, `_get_services_values`, `_get_template_values`

## `res.config.settings` (extends)

- `invoice_policy` Boolean “Invoice Policy”

## `sale.order` (extends)

- `timesheet_count` Float “Timesheet activities” (compute=_compute_timesheet_count)
- `project_id` Many2one
- `timesheet_encode_uom_id` Many2one → `uom.uom` (related=company_id.timesheet_encode_uom_id)
- `timesheet_total_duration` Integer “Timesheet Total Duration” (compute=_compute_timesheet_total_duration)
- `show_hours_recorded_button` Boolean (compute=_compute_show_hours_recorded_button)

Public methods: `action_view_timesheet`

Extension points: `_create_invoices`, `_get_order_with_valid_service_product`, `_get_prepaid_service_lines_to_upsell`

## `sale.order.line` (extends)

- `qty_delivered_method` Selection
- `analytic_line_ids` One2many
- `remaining_hours_available` Boolean (compute=_compute_remaining_hours_available)
- `remaining_hours` Float “Remaining Hours on SO” (store, compute=_compute_remaining_hours)
- `has_displayed_warning_upsell` Boolean “Has Displayed Warning Upsell”
- `timesheet_ids` One2many → `account.analytic.line` “Timesheets”

Extension points: `_get_action_per_item`

## `report.project.task.user` (extends)

- `remaining_hours_so` Float “Remaining Hours on SO” (readonly)

## `timesheets.analysis.report` (extends)

- `order_id` Many2one → `sale.order` “Sales Order” (readonly)
- `so_line` Many2one → `sale.order.line` “Sales Order Item” (readonly)
- `timesheet_invoice_type` Selection “Billable Type” (readonly)
- `timesheet_invoice_id` Many2one → `account.move` “Invoice” (readonly)
- `timesheet_revenues` Float “Timesheet Revenues” (readonly)
- `margin` Float “Margin” (readonly)
- `billable_time` Float “Billable Hours” (readonly)
- `non_billable_time` Float “Non-billable Hours” (readonly)

## `project.create.invoice` (defines)

Create Invoice from project

- `project_id` Many2one → `project.project` (required)
- `_candidate_orders` Many2many → `sale.order` (compute=_compute_candidate_orders)
- `sale_order_id` Many2one → `sale.order` “Choose the Sales Order to invoice” (required)
- `amount_to_invoice` Monetary “Amount to invoice” (compute=_compute_amount_to_invoice)
- `currency_id` Many2one (readonly, related=sale_order_id.currency_id)

Public methods: `action_create_invoice`, `default_get`

## `project.create.sale.order` (defines)

Create SO from project

- `project_id` Many2one → `project.project` (required)
- `company_id` Many2one (related=project_id.company_id)
- `partner_id` Many2one → `res.partner` “Customer” (required)
- `commercial_partner_id` Many2one (related=partner_id.commercial_partner_id)
- `sale_order_id` Many2one → `sale.order` “Sales Order”
- `line_ids` One2many → `project.create.sale.order.line` “Lines”
- `info_invoice` Char (compute=_compute_info_invoice)

Public methods: `action_create_sale_order`, `default_get`

Extension points: `_create_sale_order`

## `project.create.sale.order.line` (defines)

Create SO Line from project

- `wizard_id` Many2one → `project.create.sale.order` (required)
- `product_id` Many2one → `product.product` “Service”
- `price_unit` Float “Unit Price”
- `currency_id` Many2one → `res.currency` “Currency”
- `employee_id` Many2one → `hr.employee` “Employee”

## `sale.advance.payment.inv` (extends)

- `date_start_invoice_timesheet` Date “Start Date”
- `date_end_invoice_timesheet` Date “End Date”
- `invoicing_timesheet_enabled` Boolean (store, compute=_compute_invoicing_timesheet_enabled)

Extension points: `_create_invoices`
