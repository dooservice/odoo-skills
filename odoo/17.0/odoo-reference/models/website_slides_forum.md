# website_slides_forum — Forum on Courses

Depends on: website_slides, website_forum.

## `forum.forum` (extends)

- `slide_channel_ids` One2many → `slide.channel`
- `slide_channel_id` Many2one → `slide.channel` (store, compute=_compute_slide_channel_id)
- `visibility` Selection (related=slide_channel_id.visibility)
- `image_1920` Image “Image” (store, compute=_compute_image_1920)

## `slide.channel` (extends)

- `forum_id` Many2one → `forum.forum`
- `forum_total_posts` Integer “Number of active forum posts” (related=forum_id.total_posts)

Public methods: `action_redirect_to_forum`, `create`, `write`

## `forum.forum` (extends)
