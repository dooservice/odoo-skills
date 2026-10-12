# pos_hr — POS - HR

Depends on: point_of_sale, hr.

## `hr.employee` (extends)


Public methods: `get_barcodes_and_pin_hashed`

## `pos.config` (extends)

- `basic_employee_ids` Many2many → `hr.employee` “Employees with basic access”
- `advanced_employee_ids` Many2many → `hr.employee` “Employees with manager access”

## `pos.order` (extends)

- `employee_id` Many2one → `hr.employee`
- `cashier` Char “Cashier” (store, compute=_compute_cashier)

## `pos.session` (extends)


Extension points: `_get_pos_ui_hr_employee`

## `res.config.settings` (extends)

- `pos_basic_employee_ids` Many2many (related=pos_config_id.basic_employee_ids)
- `pos_advanced_employee_ids` Many2many (related=pos_config_id.advanced_employee_ids)

## `report.pos.order` (extends)

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
