# l10n_in_boe — Indian - Bill Of Entry

Depends on: l10n_in, stock_landed_costs.

## `account.move` (extends)


Public methods: `action_l10n_in_open_boe_wizard`

## `l10n_in.boe.wizard` (defines)

Bill Of Entry Wizard

- `move_ids` Many2many → `account.move` “Original Entry” (required)
- `company_currency_id` Many2one → `res.currency` “Company Currency” (compute=_compute_move_defaults)
- `currency_id` Many2one → `res.currency` “Document Currency” (compute=_compute_move_defaults)
- `source_partner_id` Many2one → `res.partner` (compute=_compute_move_defaults)
- `invoice_currency_rate` Float “Currency Rate” (store, compute=_compute_invoice_currency_rate)
- `picking_ids` Many2many → `stock.picking` “Transfers” (store, compute=_compute_picking_ids)
- `line_ids` One2many → `l10n_in.boe.wizard.line` “Lines” (store, compute=_compute_line_ids)
- `l10n_in_shipping_bill_number` Char “Shipping Bill Number”
- `l10n_in_shipping_bill_date` Date “Shipping Bill Date”
- `l10n_in_shipping_port_code_id` Many2one → `l10n_in.port.code`
- `total_custom_duty` Monetary (compute=_compute_amount)
- `total_tax` Monetary (compute=_compute_amount)
- `total_amount` Monetary (compute=_compute_amount)

Public methods: `action_on_submit_boe`, `default_get`

Extension points: `_check_move_ids`, `_check_valid_boe_moves`, `_get_l10n_in_find_or_create_custom_duty_product`

## `l10n_in.boe.wizard.line` (defines)

Bill of Entry Line Wizard

- `wizard_id` Many2one → `l10n_in.boe.wizard`
- `product_id` Many2one → `product.product`
- `stock_move_id` Many2one → `stock.move` “Stock Move”
- `quantity` Float “Quantity” (related=stock_move_id.quantity)
- `assessable_value` Monetary
- `custom_duty` Monetary
- `tax_ids` Many2many → `account.tax`
- `taxable_amount` Monetary (compute=_compute_amounts)
- `tax_amount` Monetary (compute=_compute_amounts)
- `currency_id` Many2one (related=wizard_id.company_currency_id)
