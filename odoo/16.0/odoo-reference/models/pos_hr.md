# pos_hr — pos_hr

Depends on: point_of_sale, hr.

## `hr.employee` (extends)


Public methods: `get_barcodes_and_pin_hashed`

## `hr.employee.public` (extends)


Public methods: `read`

## `pos.config` (extends)

- `employee_ids` Many2many → `hr.employee` “Employees with access”

## `pos.order` (extends)

- `employee_id` Many2one → `hr.employee`
- `cashier` Char “Cashier” (store, compute=_compute_cashier)

## `pos.session` (extends)


Extension points: `_get_pos_ui_hr_employee`

## `res.config.settings` (extends)

- `pos_employee_ids` Many2many (related=pos_config_id.employee_ids)

## `report.pos.order` (extends)

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
