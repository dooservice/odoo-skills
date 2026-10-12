# website_event_meet — Event Meeting / Rooms

Depends on: website_event_jitsi.

## `event.event` (extends)

- `meeting_room_ids` One2many → `event.meeting.room` “Meeting rooms”
- `meeting_room_count` Integer “Room count” (compute=_compute_meeting_room_count)
- `meeting_room_allow_creation` Boolean “Allow Room Creation” (store, compute=_compute_meeting_room_allow_creation)

## `event.meeting.room` (defines)

Event Meeting Room

Inherits: `chat.room.mixin`, `website.published.mixin`

- `name` Char “Topic” (required)
- `active` Boolean “Active”
- `is_published` Boolean
- `event_id` Many2one → `event.event` “Event” (required)
- `is_pinned` Boolean “Is Pinned”
- `chat_room_id` Many2one → `chat.room` (required)
- `room_max_capacity` Selection
- `summary` Char “Summary”
- `target_audience` Char “Audience”

Public methods: `create`, `open_website_url`

## `event.type` (extends)

- `meeting_room_allow_creation` Boolean “Allow Room Creation” (store, compute=_compute_meeting_room_allow_creation)

## `website.event.menu` (extends)

- `menu_type` Selection
