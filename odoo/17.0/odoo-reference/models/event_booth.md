# event_booth — Events Booths

Depends on: event.

## `event.booth` (defines)

Event Booth

Inherits: `event.type.booth`, `mail.thread`, `mail.activity.mixin`

- `event_type_id` Many2one
- `event_id` Many2one → `event.event` “Event” (required)
- `partner_id` Many2one → `res.partner` “Renter”
- `contact_name` Char “Renter Name” (store, compute=_compute_contact_name)
- `contact_email` Char “Renter Email” (store, compute=_compute_contact_email)
- `contact_phone` Char “Renter Phone” (store, compute=_compute_contact_phone)
- `state` Selection “Status” (required)
- `is_available` Boolean (compute=_compute_is_available)

Public methods: `action_confirm`, `create`, `write`

Extension points: `_action_post_confirm`, `_post_confirmation_message`

## `event.booth.category` (defines)

Event Booth Category

Inherits: `image.mixin`

- `active` Boolean
- `name` Char “Name” (required)
- `sequence` Integer “Sequence”
- `description` Html “Description”
- `booth_ids` One2many → `event.booth` “Booths”

## `event.event` (extends)

- `event_booth_ids` One2many → `event.booth` “Booths” (store, compute=_compute_event_booth_ids)
- `event_booth_count` Integer “Total Booths” (compute=_compute_event_booth_count)
- `event_booth_count_available` Integer “Available Booths” (compute=_compute_event_booth_count)
- `event_booth_category_ids` Many2many → `event.booth.category` (compute=_compute_event_booth_category_ids)
- `event_booth_category_available_ids` Many2many → `event.booth.category` (compute=_compute_event_booth_category_available_ids)

Extension points: `_get_booth_stat_count`

## `event.type` (extends)

- `event_type_booth_ids` One2many → `event.type.booth` “Booths” (store)

## `event.type.booth` (defines)

Event Booth Template

- `name` Char “Name” (required)
- `event_type_id` Many2one → `event.type` “Event Category” (required)
- `booth_category_id` Many2one → `event.booth.category` “Booth Category” (required)

Extension points: `_get_default_booth_category`, `_get_event_booth_fields_whitelist`
