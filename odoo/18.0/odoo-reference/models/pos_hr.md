# pos_hr — POS - HR

Depends on: point_of_sale, hr.

## `account.bank.statement.line` (extends)

- `employee_id` Many2one → `hr.employee` “Employee”

## `hr.employee` (extends)


Public methods: `get_barcodes_and_pin_hashed`

## `report.pos_hr.multi_employee_sales_report` (defines)

A collection of single session reports. One for each employee


Extension points: `_get_report_values`

## `pos.config` (extends)

- `basic_employee_ids` Many2many → `hr.employee` “Employees with basic access”
- `advanced_employee_ids` Many2many → `hr.employee` “Employees with manager access”

Public methods: `write`

## `pos.order` (extends)

- `employee_id` Many2one → `hr.employee` “Cashier”
- `cashier` Char “Cashier name” (store, compute=_compute_cashier)

Extension points: `_post_chatter_message`

## `pos.payment` (extends)

- `employee_id` Many2one → `hr.employee` “Cashier” (store, index, related=pos_order_id.employee_id)

## `pos.session` (extends)

- `employee_id` Many2one → `hr.employee` “Cashier”

Public methods: `get_closing_control_data`, `post_close_register_message`

Extension points: `_get_message_author`, `_prepare_account_bank_statement_line_vals`

## `product.product` (extends)


## `res.config.settings` (extends)

- `pos_basic_employee_ids` Many2many (related=pos_config_id.basic_employee_ids)
- `pos_advanced_employee_ids` Many2many (related=pos_config_id.advanced_employee_ids)

Public methods: `create`

## `report.pos_hr.single_employee_sales_report` (defines)

Session sales details for a single employee

Inherits: `report.point_of_sale.report_saledetails`


Public methods: `get_sale_details`

Extension points: `_get_domain`, `_prepare_get_sale_details_args_kwargs`

## `report.pos.order` (extends)

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)

## `pos.daily.sales.reports.wizard` (extends)

- `add_report_per_employee` Boolean “Add a report per each employee”
- `employee_ids` Many2many → `hr.employee` (compute=_compute_employee_ids)

Public methods: `get_multi_report_print_action`, `get_single_report_print_action`

Extension points: `_get_report_data`
