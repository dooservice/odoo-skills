# project_stock — Project Stock

Depends on: stock, project.

## `project.project` (extends)


Public methods: `action_open_all_pickings`, `action_open_deliveries`, `action_open_receipts`

Extension points: `_get_picking_action`

## `stock.picking` (extends)

- `project_id` Many2one → `project.project`
