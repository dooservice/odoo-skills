# note — Notes

Depends on: mail.

## `mail.activity` (extends)

- `note_id` Many2one → `note.note` “Related Note”

## `mail.activity.type` (extends)

- `category` Selection

## `note.stage` (defines)

Note Stage

- `name` Char “Stage Name” (required)
- `sequence` Integer
- `user_id` Many2one → `res.users` “Owner” (required)
- `fold` Boolean “Folded by Default”

## `note.tag` (defines)

Note Tag

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”

## `note.note` (defines)

Note

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Text “Note Summary” (store, compute=_compute_name)
- `company_id` Many2one → `res.company`
- `user_id` Many2one → `res.users` “Owner”
- `memo` Html “Note Content”
- `sequence` Integer “Sequence”
- `stage_id` Many2one → `note.stage` “Stage” (compute=_compute_stage_id)
- `stage_ids` Many2many → `note.stage` “Stages of Users”
- `open` Boolean “Active”
- `date_done` Date “Date done”
- `color` Integer “Color Index”
- `tag_ids` Many2many → `note.tag` “Tags”
- `message_partner_ids` Many2many

Public methods: `action_close`, `action_open`, `name_create`, `read_group`, `write`

Extension points: `_get_default_stage_id`

## `res.users` (extends)


Public methods: `create`, `systray_get_activities`

Extension points: `_create_note_stages`
