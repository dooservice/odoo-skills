# portal_rating — Portal Rating

Depends on: portal, rating.

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `mail.message` (extends)


## `rating.rating` (extends)

- `publisher_comment` Text “Publisher comment”
- `publisher_id` Many2one → `res.partner` (readonly)
- `publisher_datetime` Datetime “Commented on” (readonly)

Public methods: `write`
