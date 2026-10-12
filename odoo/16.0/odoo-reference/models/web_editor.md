# web_editor — Web Editor

Depends on: bus, web.

## `web_editor.assets` (defines)

Assets Utils


Public methods: `reset_asset`, `save_asset`

Extension points: `_get_content_from_url`, `_get_custom_asset`, `_get_custom_attachment`, `_get_data_from_url`

## `ir.attachment` (extends)

- `local_url` Char “Attachment URL” (compute=_compute_local_url)
- `image_src` Char (compute=_compute_image_src)
- `image_width` Integer (compute=_compute_image_size)
- `image_height` Integer (compute=_compute_image_size)
- `original_id` Many2one → `ir.attachment` “Original (unoptimized, unresized) attachment”

Extension points: `_get_media_info`

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`, `_get_web_editor_context`

## `ir.qweb` (extends)


Extension points: `_get_template_cache_keys`

## `ir.qweb.field` (extends)

Qweb Field


Public methods: `attributes`, `from_html`, `value_from_string`

## `ir.qweb.field.integer` (extends)

Qweb Field Integer


Public methods: `from_html`

## `ir.qweb.field.float` (extends)

Qweb Field Float


Public methods: `from_html`

## `ir.qweb.field.many2one` (extends)

Qweb Field Many to One


Public methods: `attributes`, `from_html`

## `ir.qweb.field.contact` (extends)

Qweb Field Contact


Public methods: `attributes`, `get_record_to_html`

## `ir.qweb.field.date` (extends)

Qweb Field Date


Public methods: `attributes`, `from_html`

## `ir.qweb.field.datetime` (extends)

Qweb Field Datetime


Public methods: `attributes`, `from_html`

## `ir.qweb.field.text` (extends)

Qweb Field Text


Public methods: `from_html`

## `ir.qweb.field.selection` (extends)

Qweb Field Selection


Public methods: `from_html`

## `ir.qweb.field.html` (extends)

Qweb Field HTML


Public methods: `attributes`, `from_html`

## `ir.qweb.field.image` (extends)

Qweb Field Image


Public methods: `from_html`, `load_local_url`, `load_remote_url`

## `ir.qweb.field.monetary` (extends)


Public methods: `from_html`

## `ir.qweb.field.duration` (extends)

Qweb Field Duration


Public methods: `attributes`, `from_html`

## `ir.qweb.field.relative` (extends)

Qweb Field Relative


## `ir.qweb.field.qweb` (extends)

Qweb Field qweb


## `ir.ui.view` (extends)


Public methods: `delete_snippet`, `extract_embedded_fields`, `extract_oe_structures`, `get_default_lang_code`, `get_related_views`, `rename_snippet`, `replace_arch_section`, `save`, `save_embedded_field`, `save_oe_structure`, `save_snippet`, `to_empty_oe_structure`, `to_field_ref`

Extension points: `_get_allowed_root_attrs`, `_get_cleaned_non_editing_attributes`, `_get_snippet_addition_view_key`

## `ir.websocket` (extends)


## `base` (extends)


Extension points: `_get_view_field_attributes`

## `base` (extends)


Public methods: `update_field_translations_sha`

## `web_editor.converter.test` (defines)

Web Editor Converter Test

- `char` Char
- `integer` Integer
- `float` Float
- `numeric` Float
- `many2one` Many2one → `web_editor.converter.test.sub`
- `binary` Binary
- `date` Date
- `datetime` Datetime
- `selection_str` Selection “Lorsqu'un pancake prend l'avion à destination de Toronto et qu'il fait une escale technique à St Claude, on dit:”
- `html` Html
- `text` Text

## `web_editor.converter.test.sub` (defines)

Web Editor Converter Subtest

- `name` Char
