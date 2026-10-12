# html_editor — HTML Editor

Depends on: base, bus, web.

## `html.field.history.mixin` (defines)

Field html History

- `html_field_history` Json “History data” (readonly)
- `html_field_history_metadata` Json “History metadata” (compute=_compute_metadata)

Public methods: `create`, `html_field_history_get_comparison_at_revision`, `html_field_history_get_content_at_revision`, `html_field_history_get_unified_diff_at_revision`, `write`

Extension points: `_get_versioned_fields`

## `ir.attachment` (extends)

- `local_url` Char “Attachment URL” (compute=_compute_local_url)
- `image_src` Char (compute=_compute_image_src)
- `image_width` Integer (compute=_compute_image_size)
- `image_height` Integer (compute=_compute_image_size)
- `original_id` Many2one → `ir.attachment` “Original (unoptimized, unresized) attachment”

Extension points: `_get_media_fields`, `_get_media_info`, `_get_mimetype_exempt_groups`

## `ir.http` (extends)


Extension points: `_get_editor_context`

## `ir.qweb` (extends)


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

## `ir.ui.view` (extends)


Public methods: `get_related_views`

## `ir.websocket` (extends)


## `base` (extends)


Extension points: `_get_view_field_attributes`

## `html_editor.converter.test` (defines)

Html Editor Converter Test

- `char` Char
- `integer` Integer
- `float` Float
- `numeric` Float
- `many2one` Many2one → `html_editor.converter.test.sub`
- `binary` Binary
- `date` Date
- `datetime` Datetime
- `selection_str` Selection “Lorsqu'un pancake prend l'avion à destination de Toronto et qu'il fait une escale technique à St Claude, on dit:”
- `html` Html
- `text` Text

## `html_editor.converter.test.sub` (defines)

Html Editor Converter Subtest

- `name` Char
