# mrp_repair — Mrp Repairs

Depends on: repair, mrp.

## `mrp.production` (extends)

- `repair_count` Integer “Count of source repairs” (compute=_compute_repair_count)

Public methods: `action_view_repair_orders`

## `repair.order` (extends)

- `production_count` Integer “Count of MOs generated” (compute=_compute_production_count)

Public methods: `action_explode`, `action_view_mrp_productions`, `create`, `write`

Extension points: `_get_action_add_from_catalog_extra_context`

## `stock.move` (extends)


Extension points: `_prepare_phantom_line_vals`

## `stock.move` (extends)


Extension points: `_prepare_phantom_move_values`
