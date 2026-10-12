# bus — IM Bus

Depends on: base, web.

## `bus.bus` (defines)

Communication Bus

- `channel` Char “Channel”
- `message` Char “Message”

## `bus.presence` (defines)

User Presence

- `user_id` Many2one → `res.users`
- `last_poll` Datetime “Last Poll”
- `last_presence` Datetime “Last Presence”
- `status` Selection

Public methods: `init`, `update`

## `ir.model` (extends)


Extension points: `_get_model_definitions`

## `ir.websocket` (defines)

websocket message handling


Extension points: `_get_im_status`

## `res.partner` (extends)

- `im_status` Char “IM Status” (compute=_compute_im_status)

## `res.users` (extends)

- `im_status` Char “IM Status” (compute=_compute_im_status)
