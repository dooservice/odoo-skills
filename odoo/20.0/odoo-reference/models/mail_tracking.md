# mail_tracking — Discuss Tracking

Depends on: mail.

## `ir.model.fields` (extends)


## `mail.message` (extends)

- `source_template_id` Many2one → `mail.template`
- `source_view_id` Many2one → `ir.ui.view`
- `tracking_value_ids` One2many → `mail.tracking.value` “Tracking values”

Public methods: `copy_data`, `create`

Extension points: `_create_tracking_data`

## `mail.thread` (extends)


Extension points: `_check_can_update_message_content`, `_get_log_valid_parameters`, `_get_message_create_valid_field_names`, `_get_message_parameters_updated_for_rendering`

## `mail.tracking.value` (defines)

Mail Tracking Value

- `field_id` Many2one → `ir.model.fields` (readonly, index)
- `field_info` Json “Removed field information”
- `old_value_integer` Integer “Old Value Integer” (readonly)
- `old_value_float` Float “Old Value Float” (readonly)
- `old_value_char` Char “Old Value Char” (readonly)
- `old_value_text` Text “Old Value Text” (readonly)
- `old_value_datetime` Datetime “Old Value DateTime” (readonly)
- `new_value_integer` Integer “New Value Integer” (readonly)
- `new_value_float` Float “New Value Float” (readonly)
- `new_value_char` Char “New Value Char” (readonly)
- `new_value_text` Text “New Value Text” (readonly)
- `new_value_datetime` Datetime “New Value Datetime” (readonly)
- `mail_message_id` Many2one → `mail.message` (required, index)

## `mail.compose.message` (extends)

- `source_view_id` Many2one → `ir.ui.view`

Extension points: `_prepare_mail_values_static`
