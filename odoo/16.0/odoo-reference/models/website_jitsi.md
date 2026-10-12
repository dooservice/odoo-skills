# website_jitsi — Website Jitsi

Depends on: website.

## `chat.room` (defines)

Chat Room

- `name` Char “Room Name” (required)
- `is_full` Boolean “Full” (compute=_compute_is_full)
- `jitsi_server_domain` Char “Jitsi Server Domain” (compute=_compute_jitsi_server_domain)
- `lang_id` Many2one → `res.lang`
- `max_capacity` Selection “Max capacity” (required)
- `participant_count` Integer “Participant count”
- `last_activity` Datetime “Last Activity” (readonly)
- `max_participant_reached` Integer “Max participant reached” (readonly)

## `chat.room.mixin` (defines)

Chat Room Mixin

- `chat_room_id` Many2one → `chat.room` (readonly)
- `room_name` Char “Room Name” (related=chat_room_id.name)
- `room_is_full` Boolean “Room Is Full” (related=chat_room_id.is_full)
- `room_lang_id` Many2one → `res.lang` (related=chat_room_id.lang_id)
- `room_max_capacity` Selection “Max capacity” (required, related=chat_room_id.max_capacity)
- `room_participant_count` Integer “Participant count” (related=chat_room_id.participant_count)
- `room_last_activity` Datetime “Last activity” (related=chat_room_id.last_activity)
- `room_max_participant_reached` Integer “Peak participants” (related=chat_room_id.max_participant_reached)

Public methods: `copy_data`, `create`, `unlink`, `write`
