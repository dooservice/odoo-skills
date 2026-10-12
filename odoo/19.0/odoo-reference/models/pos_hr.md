# pos_hr — POS - HR

Depends on: point_of_sale, hr.

## `account.bank.statement.line` (extends)

- `employee_id` Many2one → `hr.employee` “Employee”

## `hr.employee` (extends)

Inherits: `pos.load.mixin`


Public methods: `get_barcodes_and_pin_hashed`

## `pos.config` (extends)

Inherits: `hr.mixin`

- `minimal_employee_ids` Many2many → `hr.employee` “Employees with minimal access”
- `basic_employee_ids` Many2many → `hr.employee` “Employees with basic access”
- `advanced_employee_ids` Many2many → `hr.employee` “Employees with manager access”

Public methods: `write`

## `pos.order` (extends)

- `employee_id` Many2one → `hr.employee` “Cashier”
- `cashier` Char “Cashier name” (store, compute=_compute_cashier)

Extension points: `_prepare_pos_log`

## `pos.payment` (extends)

- `employee_id` Many2one → `hr.employee` “Cashier” (store, index, related=pos_order_id.employee_id)

## `pos.session` (extends)

- `employee_id` Many2one → `hr.employee` “Cashier”

Public methods: `get_closing_control_data`, `post_close_register_message`

Extension points: `_get_cash_move_cashier_name`, `_get_message_author`, `_prepare_account_bank_statement_line_vals`

## `product.product` (extends)


## `res.config.settings` (extends)

- `pos_basic_employee_ids` Many2many (related=pos_config_id.basic_employee_ids)
- `pos_advanced_employee_ids` Many2many (related=pos_config_id.advanced_employee_ids)
- `pos_minimal_employee_ids` Many2many (related=pos_config_id.minimal_employee_ids)

Public methods: `create`

## `res.partner` (extends)


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

Extension points: `_get_report_data`
