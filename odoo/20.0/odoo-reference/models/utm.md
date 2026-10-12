# utm — UTM Trackers

Depends on: base, web.

## `ir.http` (extends)


Public methods: `get_utm_domain_cookies`

Extension points: `_post_dispatch`

## `utm.campaign` (defines)

UTM Campaign

- `active` Boolean “Active”
- `name` Char “Campaign Identifier” (required, store, compute=_compute_name)
- `title` Char “Campaign Name” (required)
- `user_id` Many2one → `res.users` “Responsible” (required)
- `stage_id` Many2one → `utm.stage` “Stage” (required)
- `tag_ids` Many2many → `utm.tag` “Tags”
- `is_auto_campaign` Boolean “Automatically Generated Campaign”
- `color` Integer “Color Index”

Public methods: `create`

## `utm.medium` (defines)

UTM Medium

- `name` Char “Medium Name” (required)
- `active` Boolean

Public methods: `create`

## `utm.mixin` (defines)

UTM Mixin

- `campaign_id` Many2one → `utm.campaign`
- `source_id` Many2one → `utm.source`
- `medium_id` Many2one → `utm.medium`
- `utm_reference` Reference “UTM Reference” (index)

Public methods: `SELF_REQUIRED_UTM_REF`, `default_get`, `find_or_create_record`, `tracking_fields`

Extension points: `_get_unique_names`

## `utm.source` (defines)

UTM Source

- `name` Char “Source Name” (required)

Public methods: `create`

## `utm.stage` (defines)

Campaign Stage

- `name` Char (required)
- `sequence` Integer

## `utm.tag` (defines)

UTM Tag

- `name` Char (required)
- `color` Integer “Color Index”
