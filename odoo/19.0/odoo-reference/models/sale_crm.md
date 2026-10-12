# sale_crm — Opportunity to Quotation

Depends on: sale, crm.

## `crm.lead` (extends)

- `sale_amount_total` Monetary “Sum of Orders” (compute=_compute_sale_data)
- `quotation_count` Integer “Number of Quotations” (compute=_compute_sale_data)
- `sale_order_count` Integer “Number of Sale Orders” (compute=_compute_sale_data)
- `order_ids` One2many → `sale.order` “Orders”

Public methods: `action_new_quotation`, `action_sale_quotations_new`, `action_view_sale_order`, `action_view_sale_quotation`

Extension points: `_get_action_view_sale_quotation_domain`, `_get_lead_quotation_domain`, `_get_lead_sale_order_domain`, `_prepare_opportunity_quotation_context`

## `crm.team` (extends)


Public methods: `action_primary_channel_button`

## `sale.order` (extends)

- `opportunity_id` Many2one → `crm.lead` “Opportunity”

Public methods: `action_confirm`

## `crm.quotation.partner` (defines)

Create new or use existing Customer on new Quotation

- `action` Selection “Quotation Customer” (required)
- `lead_id` Many2one → `crm.lead` (required)
- `partner_id` Many2one → `res.partner`

Public methods: `action_apply`, `default_get`
