# project_mrp — MRP Project

Depends on: mrp, project.

## `mrp.bom` (extends)

- `project_id` Many2one → `project.project`

## `mrp.production` (extends)

- `project_id` Many2one → `project.project` (store, compute=_compute_project_id)

Public methods: `action_generate_bom`, `action_open_project`

## `project.project` (extends)

- `bom_count` Integer (compute=_compute_bom_count)
- `production_count` Integer (compute=_compute_production_count)

Public methods: `action_view_mrp_bom`, `action_view_mrp_production`

Extension points: `_get_stat_buttons`

## `stock.rule` (extends)


Extension points: `_prepare_mo_vals`

## `stock.move` (extends)


Extension points: `_prepare_procurement_values`
