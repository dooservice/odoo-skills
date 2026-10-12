# event_sale — Events Sales

Depends on: event, sale_management.

## `account.move` (extends)


## `event.event` (extends)

- `sale_order_lines_ids` One2many → `sale.order.line` “All sale order lines pointing to this event”
- `sale_price_subtotal` Monetary “Sales (Tax Excluded)” (compute=_compute_sale_price_subtotal)
- `currency_id` Many2one → `res.currency` “Currency” (readonly, related=company_id.currency_id)

Public methods: `action_view_linked_orders`

## `event.registration` (extends)

- `is_paid` Boolean “Is Paid”
- `sale_order_id` Many2one → `sale.order` “Sales Order”
- `sale_order_line_id` Many2one → `sale.order.line` “Sales Order Line”
- `payment_status` Selection “Payment Status” (compute=_compute_payment_status)
- `utm_campaign_id` Many2one (store, compute=_compute_utm_campaign_id)
- `utm_source_id` Many2one (store, compute=_compute_utm_source_id)
- `utm_medium_id` Many2one (store, compute=_compute_utm_medium_id)

Public methods: `action_view_sale_order`, `create`, `write`

Extension points: `_action_set_paid`, `_get_registration_summary`

## `event.type.ticket` (extends)

- `description` Text (store, compute=_compute_description)
- `product_id` Many2one → `product.product` “Product” (required)
- `price` Float “Price” (store, compute=_compute_price)
- `price_reduce` Float “Price Reduce” (compute=_compute_price_reduce)

Extension points: `_get_event_ticket_fields_whitelist`

## `event.event.ticket` (extends)

- `price_reduce_taxinc` Float “Price Reduce Tax inc” (compute=_compute_price_reduce_taxinc)

Extension points: `_get_ticket_multiline_description`

## `product.template` (extends)

- `detailed_type` Selection

## `product.product` (extends)

- `event_ticket_ids` One2many → `event.event.ticket` “Event Tickets”

## `sale.order` (extends)

- `attendee_count` Integer “Attendee Count” (compute=_compute_attendee_count)

Public methods: `action_confirm`, `action_view_attendee_list`, `unlink`, `write`

Extension points: `_action_cancel`

## `sale.order.line` (extends)

- `event_id` Many2one → `event.event` “Event” (store, compute=_compute_event_id)
- `event_ticket_id` Many2one → `event.event.ticket` “Event Ticket” (store, compute=_compute_event_ticket_id)
- `event_ok` Boolean (compute=_compute_event_ok)

Public methods: `unlink`

Extension points: `_get_display_price`, `_get_sale_order_line_multiline_description_sale`

## `sale.order.template.line` (extends)

- `product_id` Many2one

## `sale.order.template.option` (extends)

- `product_id` Many2one

## `event.sale.report` (defines)

Event Sales Report

- `event_type_id` Many2one → `event.type` “Event Type” (readonly)
- `event_id` Many2one → `event.event` “Event” (readonly)
- `event_date_begin` Date “Event Start Date” (readonly)
- `event_date_end` Date “Event End Date” (readonly)
- `event_ticket_id` Many2one → `event.event.ticket` “Event Ticket” (readonly)
- `event_ticket_price` Float “Ticket price” (readonly)
- `event_registration_create_date` Date “Registration Date” (readonly)
- `event_registration_state` Selection “Registration Status” (readonly)
- `active` Boolean “Is registration active (not archived)?”
- `event_registration_id` Many2one → `event.registration` (readonly)
- `event_registration_name` Char “Attendee Name” (readonly)
- `product_id` Many2one → `product.product` “Product” (readonly)
- `sale_order_id` Many2one → `sale.order` (readonly)
- `sale_order_date` Datetime “Order Date” (readonly)
- `sale_order_partner_id` Many2one → `res.partner` “Customer” (readonly)
- `sale_order_state` Selection “Sale Order Status” (readonly)
- `sale_order_user_id` Many2one → `res.users` “Salesperson” (readonly)
- `sale_order_line_id` Many2one → `sale.order.line` (readonly)
- `sale_price` Float “Revenues” (readonly)
- `sale_price_untaxed` Float “Untaxed Revenues” (readonly)
- `invoice_partner_id` Many2one → `res.partner` “Invoice Address” (readonly)
- `is_paid` Boolean “Is Paid” (readonly)
- `payment_status` Selection “Payment Status”
- `company_id` Many2one → `res.company` “Company” (readonly)

Public methods: `init`

## `event.event.configurator` (defines)

Event Configurator

- `product_id` Many2one → `product.product` “Product” (readonly)
- `event_id` Many2one → `event.event` “Event”
- `event_ticket_id` Many2one → `event.event.ticket` “Event Ticket”

Public methods: `check_event_id`

## `registration.editor` (defines)

Edit Attendee Details on Sales Confirmation

- `sale_order_id` Many2one → `sale.order` (required)
- `event_registration_ids` One2many → `registration.editor.line` “Registrations to Edit”
- `seats_available_insufficient` Boolean “Not enough seats for all registrations” (readonly, compute=_compute_seats_available_insufficient)

Public methods: `action_make_registration`, `default_get`

## `registration.editor.line` (defines)

Edit Attendee Line on Sales Confirmation

- `editor_id` Many2one → `registration.editor`
- `sale_order_line_id` Many2one → `sale.order.line` “Sales Order Line”
- `event_id` Many2one → `event.event` “Event” (required)
- `registration_id` Many2one → `event.registration`
- `event_ticket_id` Many2one → `event.event.ticket` “Event Ticket”
- `email` Char “Email”
- `phone` Char “Phone”
- `mobile` Char “Mobile”
- `name` Char “Name”

Public methods: `get_registration_data`
