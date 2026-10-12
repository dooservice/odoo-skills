# mrp_landed_costs — Landed Costs On MO

Depends on: stock_landed_costs, mrp.

## `stock.landed.cost` (extends)

- `target_model` Selection
- `mrp_production_ids` Many2many → `mrp.production` “Manufacturing order”

Extension points: `_get_targeted_move_ids`
