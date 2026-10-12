# html_editor — HTML Editor

Depends on: base, bus, web.

## `ir.attachment` (extends)

- `local_url` Char “Attachment URL” (compute=_compute_local_url)
- `image_src` Char (compute=_compute_image_src)
- `image_width` Integer (compute=_compute_image_size)
- `image_height` Integer (compute=_compute_image_size)
- `original_id` Many2one → `ir.attachment` “Original (unoptimized, unresized) attachment”

Extension points: `_get_media_info`, `_get_mimetype_exempt_groups`
