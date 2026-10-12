# event_sale — Events Sales

Depends on: event_product, sale_management.

## `event.event` (extends)

- `sale_order_lines_ids` One2many → `sale.order.line` “All sale order lines pointing to this event”
- `sale_price_total` Monetary “Sales (Tax Included)” (compute=_compute_sale_price_total)

Public methods: `action_view_linked_orders`

## `event.registration` (extends)

- `sale_order_id` Many2one → `sale.order` “Sales Order”
- `sale_order_line_id` Many2one → `sale.order.line` “Sales Order Line”
- `state` Selection (store, compute=_compute_registration_status)
- `utm_campaign_id` Many2one (store, compute=_compute_utm_campaign_id)
- `utm_source_id` Many2one (store, compute=_compute_utm_source_id)
- `utm_medium_id` Many2one (store, compute=_compute_utm_medium_id)

Public methods: `action_view_sale_order`, `create`, `write`

Extension points: `_get_event_registration_ids_from_order`, `_get_registration_summary`

## `event.event.ticket` (extends)


Extension points: `_get_ticket_multiline_description`

## `product.template` (extends)


Extension points: `_prepare_service_tracking_tooltip`

## `sale.order` (extends)

- `attendee_count` Integer “Attendee Count” (compute=_compute_attendee_count)

Public methods: `action_confirm`, `action_view_attendee_list`, `write`

Extension points: `_get_product_catalog_domain`

## `sale.order.line` (extends)

- `event_id` Many2one → `event.event` “Event” (store, compute=_compute_event_id)
- `event_slot_id` Many2one → `event.slot` “Slot” (store, compute=_compute_event_related)
- `event_ticket_id` Many2one → `event.event.ticket` “Ticket Type” (store, compute=_compute_event_related)
- `is_multi_slots` Boolean (related=event_id.is_multi_slots)
- `registration_ids` One2many → `event.registration` “Registrations”

Extension points: `_check_event_registration_ticket`, `_get_display_price`, `_get_sale_order_line_multiline_description_sale`

## `event.sale.report` (defines)

Event Sales Report

- `event_type_id` Many2one → `event.type` “Event Type” (readonly)
- `event_id` Many2one → `event.event` “Event” (readonly)
- `event_date_begin` Date “Event Start Date” (readonly)
- `event_date_end` Date “Event End Date” (readonly)
- `event_slot_id` Many2one → `event.slot` “Event Slot” (readonly)
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
- `sale_status` Selection “Payment Status”
- `company_id` Many2one → `res.company` “Company” (readonly)

Public methods: `init`

## `event.event.configurator` (defines)

Event Configurator

- `product_id` Many2one → `product.product` “Product” (readonly)
- `event_id` Many2one → `event.event` “Event”
- `event_slot_id` Many2one → `event.slot` “Slot” (store, compute=_compute_event_slot_id)
- `event_ticket_id` Many2one → `event.event.ticket` “Ticket Type” (store, compute=_compute_event_ticket_id)
- `is_multi_slots` Boolean (related=event_id.is_multi_slots)
- `has_available_tickets` Boolean “Has Available Tickets” (compute=_compute_has_available_tickets)

Public methods: `check_event_id`

## `registration.editor` (defines)

Edit Attendee Details on Sales Confirmation

- `sale_order_id` Many2one → `sale.order` (required)
- `event_registration_ids` One2many → `registration.editor.line` “Registrations to Edit”

Public methods: `action_make_registration`, `default_get`

## `registration.editor.line` (defines)

Edit Attendee Line on Sales Confirmation

- `editor_id` Many2one → `registration.editor`
- `sale_order_line_id` Many2one → `sale.order.line` “Sales Order Line”
- `event_id` Many2one → `event.event` “Event” (required)
- `company_id` Many2one (related=event_id.company_id)
- `registration_id` Many2one → `event.registration`
- `event_slot_id` Many2one → `event.slot` “Event Slot”
- `event_ticket_id` Many2one → `event.event.ticket` “Event Ticket”
- `email` Char “Email”
- `phone` Char “Phone”
- `name` Char “Name”

Extension points: `_prepare_registration_data`
