# portal_rating — Portal Rating

Depends on: portal, rating.

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `mail.message` (extends)


## `mail.thread` (extends)


Extension points: `_get_allowed_message_post_params`

## `rating.rating` (extends)

- `publisher_comment` Text “Publisher comment”
- `publisher_id` Many2one → `res.partner` (readonly)
- `publisher_datetime` Datetime “Commented on” (readonly)

Public methods: `create`, `write`

Extension points: `_check_synchronize_publisher_values`
