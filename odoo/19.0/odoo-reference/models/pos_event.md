# pos_event — POS - Event

Depends on: point_of_sale, event_product.

## `event.event` (extends)

Inherits: `pos.load.mixin`

- `image_1024` Image “PoS Image”

Public methods: `get_slot_tickets_availability_pos`

## `event.question` (extends)

Inherits: `pos.load.mixin`


## `event.question.answer` (extends)

Inherits: `pos.load.mixin`


## `event.registration` (extends)

Inherits: `pos.load.mixin`

- `pos_order_id` Many2one “PoS Order” (related=pos_order_line_id.order_id)
- `pos_order_line_id` Many2one → `pos.order.line` “PoS Order Line”

Public methods: `action_view_pos_order`, `create`, `write`

## `event.registration.answer` (extends)

Inherits: `pos.load.mixin`


## `event.slot` (extends)

Inherits: `pos.load.mixin`


## `event.event.ticket` (extends)

Inherits: `pos.load.mixin`


## `pos.config` (extends)


## `pos.order` (extends)

- `attendee_count` Integer “Attendee Count” (compute=_compute_attendee_count)

Public methods: `action_pos_order_paid`, `action_view_attendee_list`, `print_event_badges`, `print_event_tickets`, `read_pos_data`, `send_paid_order_mail`

## `pos.order.line` (extends)

- `event_ticket_id` Many2one → `event.event.ticket` “Event Ticket”
- `event_registration_ids` One2many → `event.registration` “Event Registrations”

## `pos.session` (extends)
