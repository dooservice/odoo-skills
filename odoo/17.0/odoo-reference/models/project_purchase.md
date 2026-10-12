# project_purchase — Project Purchase

Depends on: purchase, project_account.

## `project.project` (extends)

- `purchase_orders_count` Integer “# Purchase Orders” (compute=_compute_purchase_orders_count)

Public methods: `action_open_project_purchase_orders`, `action_profitability_items`

Extension points: `_get_profitability_aal_domain`, `_get_profitability_items`, `_get_profitability_labels`, `_get_profitability_sequence_per_invoice_type`, `_get_stat_buttons`

## `purchase.order.line` (extends)


Public methods: `create`
