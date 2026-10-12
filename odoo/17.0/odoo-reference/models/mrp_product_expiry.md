# mrp_product_expiry — Manufacturing Expiry

Depends on: mrp, product_expiry.

## `mrp.production` (extends)


Public methods: `pre_button_mark_done`

Extension points: `_check_expired_lots`, `_get_expired_context`

## `expiry.picking.confirmation` (extends)

- `production_ids` Many2many → `mrp.production` (readonly)
- `workorder_id` Many2one → `mrp.workorder` (readonly)

Public methods: `confirm_produce`, `confirm_workorder`
