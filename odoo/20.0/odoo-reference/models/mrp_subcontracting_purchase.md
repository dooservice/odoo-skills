# mrp_subcontracting_purchase — Purchase and Subcontracting Management

Depends on: mrp_subcontracting_account, purchase_mrp.

## `account.move` (extends)


Extension points: `_get_price_difference_lines_vals`

## `account.move.line` (extends)


## `mrp.production` (extends)

- `subcontract_extra_move_id` Many2one → `account.move` “Subcontracting Cost Entry”

Extension points: `_post_inventory`, `_post_subcontract_extra_cost`

## `product.product` (extends)


Extension points: `_get_monthly_demand_moves_location_domain`

## `purchase.order` (extends)

- `subcontracting_resupply_picking_count` Integer “Count of Subcontracting Resupply” (compute=_compute_subcontracting_resupply_picking_count)

Public methods: `action_view_subcontracting_resupply`

Extension points: `_get_mrp_productions`, `_get_subcontracting_resupplies`

## `stock.move` (extends)


Extension points: `_get_value_from_account_move`

## `stock.picking` (extends)

- `subcontracting_source_purchase_count` Integer “Number of subcontracting PO Source” (compute=_compute_subcontracting_source_purchase_count)

Public methods: `action_view_subcontracting_source_purchase`

Extension points: `_get_subcontract_mo_confirmation_ctx`, `_get_subcontracting_source_purchase`

## `stock.rule` (extends)


Extension points: `_get_lead_days`

## `report.mrp.report_bom_structure` (extends)


Extension points: `_get_resupply_availability`

## `report.mrp.report_mo_overview` (extends)


Extension points: `_get_seller_resupply_data`, `_get_subcontracted_bom`
