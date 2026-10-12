# mrp_landed_costs — Landed Costs On MO

Depends on: stock_landed_costs, mrp.

## `stock.landed.cost` (extends)

- `target_model` Selection
- `mrp_production_ids` Many2many → `mrp.production` “Manufacturing order”
- `mrp_productions_count` Integer (compute=_compute_mrp_productions_count)

Public methods: `action_view_mrp_productions`

Extension points: `_get_targeted_move_ids`
