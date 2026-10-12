# purchase_mrp — Purchase and MRP Management

Depends on: mrp, purchase_stock.

## `mrp.bom` (extends)


Extension points: `_check_bom_lines`

## `mrp.bom.line` (extends)

- `cost_share` Float “Cost Share (%)”

Extension points: `_get_cost_share`, `_get_line_cost_share`, `_prepare_bom_done_values`, `_prepare_line_done_values`

## `mrp.production` (extends)

- `purchase_order_count` Integer “Count of generated PO” (compute=_compute_purchase_order_count)

Public methods: `action_view_purchase_orders`

Extension points: `_get_document_iterate_key`, `_get_purchase_orders`, `_prepare_merge_orig_links`

## `purchase.order` (extends)

- `mrp_production_count` Integer “Count of MO Source” (compute=_compute_mrp_production_count)

Public methods: `action_view_mrp_productions`

Extension points: `_get_mrp_productions`

## `purchase.order.line` (extends)


Extension points: `_get_move_dests_initial_demand`, `_get_qty_procurement`, `_get_sale_order_line_product`, `_get_upstream_documents_and_responsibles`, `_prepare_qty_received`, `_prepare_stock_moves`

## `stock.move` (extends)


Extension points: `_get_cost_ratio`, `_get_quantity_from_bill`, `_get_value_from_bill`, `_prepare_phantom_move_values`

## `stock.rule` (extends)


## `report.mrp.report_bom_structure` (extends)


Extension points: `_get_resupply_availability`

## `report.mrp.report_mo_overview` (extends)


Extension points: `_get_extra_replenishments`, `_get_origin`, `_get_replenishment_mo_cost`, `_get_replenishment_receipt`, `_get_resupply_data`, `_get_seller_resupply_data`
