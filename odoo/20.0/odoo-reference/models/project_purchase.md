# project_purchase — Project Purchase

Depends on: purchase, project_account.

## `project.project` (extends)

- `purchase_orders_count` Integer “# Purchase Orders” (compute=_compute_purchase_orders_count)

Public methods: `action_open_project_purchase_orders`

## `purchase.order` (extends)

- `project_id` Many2one → `project.project`

## `purchase.order.line` (extends)


Public methods: `create`

## `purchase.report` (extends)

- `project_id` Many2one → `project.project` (readonly)
