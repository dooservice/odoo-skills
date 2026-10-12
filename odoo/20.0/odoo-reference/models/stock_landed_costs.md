# stock_landed_costs — WMS Landed Costs

Depends on: stock_account, purchase_stock.

## `account.move` (extends)

- `landed_costs_ids` One2many → `stock.landed.cost` “Landed Costs”
- `landed_costs_visible` Boolean (compute=_compute_landed_costs_visible)

Public methods: `action_view_landed_costs`, `button_create_landed_costs`

## `account.move.line` (extends)

- `product_type` Selection (readonly, related=product_id.type)
- `is_landed_costs_line` Boolean

## `product.template` (extends)

- `landed_cost_ok` Boolean “Is a Landed Cost”
- `split_method_landed_cost` Selection “Default Split Method”
- `landed_cost_on_product_ids` Many2many → `product.product` “Apply Landed Cost On”

Public methods: `write`

## `purchase.order.line` (extends)


Extension points: `_prepare_account_move_line`

## `res.company` (extends)

- `lc_journal_id` Many2one → `account.journal`

## `res.config.settings` (extends)

- `lc_journal_id` Many2one → `account.journal` “Default Journal” (related=company_id.lc_journal_id)

## `stock.landed.cost` (defines)

Stock Landed Cost

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Name” (readonly)
- `date` Date “Date” (required)
- `target_model` Selection “Apply On” (required)
- `picking_ids` Many2many → `stock.picking` “Transfers”
- `pickings_count` Integer (compute=_compute_pickings_count)
- `cost_lines` One2many → `stock.landed.cost.lines`
- `valuation_adjustment_lines` One2many → `stock.valuation.adjustment.lines`
- `description` Text “Item Description”
- `amount_total` Monetary “Total” (store, compute=_compute_total_amount)
- `state` Selection (readonly)
- `account_move_id` Many2one → `account.move` (readonly)
- `account_journal_id` Many2one → `account.journal` (required)
- `company_id` Many2one → `res.company` “Company” (required, index)
- `vendor_bill_id` Many2one → `account.move`
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `allowed_product_ids` Many2many → `product.product` (compute=_compute_allowed_product_ids)

Public methods: `action_view_pickings`, `button_cancel`, `button_validate`, `compute_landed_cost`, `create`, `get_valuation_lines`, `unlink`

Extension points: `_check_can_validate`, `_check_sum`, `_get_targeted_move_ids`

## `stock.landed.cost.lines` (defines)

Stock Landed Cost Line

- `name` Char “Description”
- `cost_id` Many2one → `stock.landed.cost` (required, index)
- `product_id` Many2one → `product.product` (required)
- `price_unit` Monetary “Cost” (required)
- `split_method` Selection “Split Method” (required)
- `account_id` Many2one → `account.account`
- `currency_id` Many2one → `res.currency` (related=cost_id.currency_id)
- `apply_on_product_ids` Many2many → `product.product` “Apply On” (store, compute=_compute_apply_on_product_ids)

Public methods: `onchange_product_id`

## `stock.valuation.adjustment.lines` (defines)

Valuation Adjustment Line

- `name` Char “Description” (store, compute=_compute_name)
- `cost_id` Many2one → `stock.landed.cost` (required, index)
- `cost_line_id` Many2one → `stock.landed.cost.lines` (readonly, index)
- `move_id` Many2one → `stock.move` (readonly)
- `product_id` Many2one → `product.product` (required, index)
- `quantity` Float “Quantity” (required)
- `weight` Float “Weight”
- `volume` Float “Volume”
- `former_cost` Monetary “Original Value”
- `additional_landed_cost` Monetary “Additional Landed Cost”
- `final_cost` Monetary “New Value” (store, compute=_compute_final_cost)
- `currency_id` Many2one → `res.currency` (related=cost_id.company_id.currency_id)

Extension points: `_create_account_move_line`, `_create_accounting_entries`, `_prepare_account_move_line_values`

## `stock.move` (extends)


Extension points: `_get_landed_cost`, `_get_value_from_extra`
