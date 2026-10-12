# website_blog — Blog

Depends on: website_mail, website_partner.

## `website` (extends)


Public methods: `configurator_set_menu_links`, `get_suggested_controllers`

## `blog.blog` (defines)

Blog

Inherits: `mail.thread`, `website.seo.metadata`, `website.multi.mixin`, `website.cover_properties.mixin`, `website.searchable.mixin`

- `name` Char “Blog Name” (required)
- `subtitle` Char “Blog Subtitle”
- `active` Boolean “Active”
- `content` Html “Content”
- `blog_post_ids` One2many → `blog.post`
- `blog_post_count` Integer “Posts” (compute=_compute_blog_post_count)

Public methods: `all_tags`, `message_post`, `write`

## `blog.tag.category` (defines)

Blog Tag Category

- `name` Char “Name” (required)
- `tag_ids` One2many → `blog.tag` “Tags”

## `blog.tag` (defines)

Blog Tag

Inherits: `website.seo.metadata`

- `name` Char “Name” (required)
- `category_id` Many2one → `blog.tag.category` (index)
- `color` Integer “Color”
- `post_ids` Many2many → `blog.post` “Posts”

Public methods: `write`

## `blog.post` (defines)

Blog Post

Inherits: `mail.thread`, `website.seo.metadata`, `website.published.multi.mixin`, `website.cover_properties.mixin`, `website.searchable.mixin`

- `name` Char “Title” (required)
- `subtitle` Char “Sub Title”
- `author_id` Many2one → `res.partner`
- `author_avatar` Binary “Avatar” (related=author_id.image_128)
- `author_name` Char “Author Name” (store, related=author_id.display_name)
- `active` Boolean “Active”
- `blog_id` Many2one → `blog.blog` (required)
- `tag_ids` Many2many → `blog.tag` “Tags”
- `content` Html “Content”
- `teaser` Text “Teaser” (compute=_compute_teaser)
- `teaser_manual` Text “Teaser Content”
- `website_message_ids` One2many
- `create_date` Datetime “Created on” (readonly)
- `published_date` Datetime “Published Date”
- `post_date` Datetime “Publishing date” (store, compute=_compute_post_date)
- `create_uid` Many2one → `res.users` (readonly)
- `write_date` Datetime “Last Updated on” (readonly)
- `write_uid` Many2one → `res.users` (readonly)
- `visits` Integer “No of Views” (readonly)
- `website_id` Many2one (readonly, store, related=blog_id.website_id)

Public methods: `copy_data`, `create`, `write`

Extension points: `_check_for_publication`, `_get_access_action`

## `website.snippet.filter` (extends)


Extension points: `_get_hardcoded_sample`
