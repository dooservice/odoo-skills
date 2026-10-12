# bus — IM Bus

Depends on: base, web.

## `bus.bus` (defines)

Communication Bus

- `channel` Char “Channel”
- `message` Char “Message”
- `create_date` Datetime (index)

Extension points: `_prepare_payload`

## `bus.listener.mixin` (defines)

Can send messages via bus.bus


## `ir.attachment` (extends)

Inherits: `bus.listener.mixin`


## `ir.http` (extends)


Public methods: `get_frontend_session_info`, `session_info`

Extension points: `_get_bus_session_info`

## `ir.model` (extends)


Extension points: `_get_model_definitions`

## `ir.qweb` (extends)


Extension points: `_get_bundles_to_pregenarate`

## `ir.websocket` (defines)

websocket message handling


Extension points: `_prepare_subscribe_data`

## `res.groups` (extends)

Inherits: `bus.listener.mixin`


## `res.partner` (extends)

Inherits: `bus.listener.mixin`


## `res.users` (extends)

Inherits: `bus.listener.mixin`


## `res.users.settings` (extends)

Inherits: `bus.listener.mixin`
