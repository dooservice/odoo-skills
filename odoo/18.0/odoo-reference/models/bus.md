# bus — IM Bus

Depends on: base, web.

## `bus.bus` (defines)

Communication Bus

- `channel` Char “Channel”
- `message` Char “Message”

## `bus.listener.mixin` (defines)

Can send messages via bus.bus


## `bus.presence` (defines)

User Presence

- `user_id` Many2one → `res.users`
- `last_poll` Datetime “Last Poll”
- `last_presence` Datetime “Last Presence”
- `status` Selection

Public methods: `create`, `init`, `unlink`, `update_presence`, `write`

Extension points: `_get_bus_target`, `_get_identity_data`, `_get_identity_field_name`

## `ir.attachment` (extends)

Inherits: `bus.listener.mixin`


## `ir.http` (extends)


Public methods: `get_frontend_session_info`, `session_info`

## `ir.model` (extends)


Extension points: `_get_model_definitions`

## `ir.qweb` (extends)


Extension points: `_get_bundles_to_pregenarate`

## `ir.websocket` (defines)

websocket message handling


Extension points: `_get_missed_presences_bus_target`, `_get_missed_presences_identity_domains`, `_prepare_subscribe_data`

## `res.groups` (extends)

Inherits: `bus.listener.mixin`


## `res.partner` (extends)

Inherits: `bus.listener.mixin`

- `im_status` Char “IM Status” (compute=_compute_im_status)

## `res.users` (extends)

Inherits: `bus.listener.mixin`

- `im_status` Char “IM Status” (compute=_compute_im_status)

## `res.users.settings` (extends)

Inherits: `bus.listener.mixin`
