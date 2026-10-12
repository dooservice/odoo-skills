# web_tour — Tours

Depends on: web.

## `ir.http` (extends)


Public methods: `session_info`

## `web_tour.tour` (defines)

Tours

- `name` Char “Tour name” (required)
- `user_id` Many2one → `res.users` “Consumed by”

Public methods: `consume`, `get_consumed_tours`
