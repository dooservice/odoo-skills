# project_mrp — MRP Project

Depends on: mrp_account, project.

## `mrp.production` (extends)


## `project.project` (extends)

- `production_count` Integer (related=analytic_account_id.production_count)
- `workorder_count` Integer (related=analytic_account_id.workorder_count)
- `bom_count` Integer (related=analytic_account_id.bom_count)

Public methods: `action_view_mrp_bom`, `action_view_mrp_production`, `action_view_workorder`

Extension points: `_get_profitability_aal_domain`, `_get_profitability_items`, `_get_profitability_labels`, `_get_profitability_sequence_per_invoice_type`, `_get_stat_buttons`
