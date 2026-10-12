# website_blog — Blog

Depends on: website_mail, website_partner, html_builder.

## `res.partner` (extends)

- `blog_post_ids` One2many → `blog.post` “Blog Posts”

## `website` (extends)


Public methods: `configurator_set_menu_links`, `get_suggested_controllers`

Extension points: `_get_search_scopes`

## `blog.blog` (defines)

Blog

Inherits: `mail.thread`, `website.seo.metadata`, `website.multi.mixin`, `website.located.mixin`, `website.cover_properties.mixin`, `website.searchable.mixin`, `website.structured_data.mixin`

- `sequence` Integer “Sequence”
- `name` Char “Blog Name” (required)
- `subtitle` Char “Blog Subtitle”
- `active` Boolean “Active”
- `content` Html “Content”
- `blog_post_ids` One2many → `blog.post`
- `blog_post_count` Integer “Posts” (compute=_compute_blog_post_count)

Public methods: `all_tags`, `message_post`, `write`

Extension points: `_get_breadcrumb_items`, `_prepare_jsonld_vals`

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

## `blog.post` (defines)

Blog Post

Inherits: `mail.thread`, `website.seo.metadata`, `website.published.multi.mixin`, `website.page_visibility_options.mixin`, `website.cover_properties.mixin`, `website.searchable.mixin`, `website.structured_data.mixin`, `website.trackable.mixin`

- `name` Char “Title” (required)
- `subtitle` Char “Sub Title”
- `author_id` Many2one → `res.partner`
- `author_avatar` Binary “Avatar” (related=author_id.image_128)
- `author_name` Char “Author Name” (store, related=author_id.display_name)
- `active` Boolean “Active”
- `blog_id` Many2one → `blog.blog` (required, index)
- `recommended_next_post_id` Many2one → `blog.post` “Recommended Next Post”
- `tag_ids` Many2many → `blog.tag` “Tags”
- `content` Html “Content”
- `teaser` Text “Teaser” (compute=_compute_teaser)
- `teaser_manual` Text “Teaser Content”
- `create_date` Datetime “Created on” (readonly)
- `create_uid` Many2one → `res.users` (readonly)
- `write_date` Datetime “Last Updated on” (readonly)
- `write_uid` Many2one → `res.users` (readonly)
- `visits` Integer “No of Views” (readonly)
- `website_id` Many2one (readonly, store, related=blog_id.website_id)

Public methods: `create`, `write`

Extension points: `_check_for_action_post_publish`, `_get_access_action`, `_get_breadcrumb_items`, `_get_customer_portal_message_types`, `_get_jsonld_dict`, `_prepare_jsonld_vals`

## `website.snippet.filter` (extends)


Public methods: `default_get`

Extension points: `_get_hardcoded_sample`

## `website.track` (extends)

- `blog_post_id` Many2one → `blog.post` (readonly)

## `website.visitor` (extends)

- `visitor_blog_post_count` Integer “Blog Post Views” (compute=_compute_blog_post_statistics)
- `blog_post_ids` Many2many → `blog.post` “Blog Posts” (compute=_compute_blog_post_statistics)
