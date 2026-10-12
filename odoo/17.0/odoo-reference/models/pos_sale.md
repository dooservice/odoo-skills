# pos_sale — POS - Sales

Depends on: point_of_sale, sale_management.

## `crm.team` (extends)

- `pos_config_ids` One2many → `pos.config` “Point of Sales”
- `pos_sessions_open_count` Integer “Open POS Sessions” (compute=_compute_pos_sessions_open_count)
- `pos_order_amount_total` Float “Session Sale Amount” (compute=_compute_pos_order_amount_total)

## `pos.config` (extends)

- `crm_team_id` Many2one → `crm.team` “Sales Team”
- `down_payment_product_id` Many2one → `product.product` “Down Payment Product”

Extension points: `_get_available_product_domain`, `_get_special_products`

## `pos.order` (extends)

- `currency_rate` Float (readonly, store, compute=_compute_currency_rate)
- `crm_team_id` Many2one → `crm.team` “Sales Team”
- `sale_order_count` Integer “Sale Order Count” (readonly, compute=_count_sale_order)

Public methods: `action_view_sale_order`, `create_from_ui`

Extension points: `_get_fields_for_order_line`, `_get_invoice_lines_values`, `_prepare_invoice_vals`, `_prepare_order_line`

## `pos.order.line` (extends)

- `sale_order_origin_id` Many2one → `sale.order` “Linked Sale Order”
- `sale_order_line_id` Many2one → `sale.order.line` “Source Sale Order Line”
- `down_payment_details` Text “Down Payment Details”

## `pos.session` (extends)

- `crm_team_id` Many2one → `crm.team` “Sales Team” (readonly, related=config_id.crm_team_id)

## `res.config.settings` (extends)

- `pos_crm_team_id` Many2one “Sales Team (PoS)” (related=pos_config_id.crm_team_id)
- `pos_down_payment_product_id` Many2one (related=pos_config_id.down_payment_product_id)

## `sale.order` (extends)

- `pos_order_line_ids` One2many → `pos.order.line` “Order lines Transfered to Point of Sale” (readonly)
- `pos_order_count` Integer “Pos Order Count” (readonly, compute=_count_pos_order)
- `amount_unpaid` Monetary “Unpaid Amount” (store, compute=_compute_amount_unpaid)

Public methods: `action_view_pos_order`

## `sale.order.line` (extends)

- `pos_order_line_ids` One2many → `pos.order.line` “Order lines Transfered to Point of Sale” (readonly)

Public methods: `read_converted`, `unlink`

Extension points: `_get_downpayment_line_price_unit`, `_get_sale_order_fields`

## `stock.picking` (extends)


Extension points: `_create_move_from_pos_order_lines`

## `sale.report` (extends)

- `state` Selection
- `order_reference` Reference

Extension points: `_get_done_states`
