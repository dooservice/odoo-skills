# website_event_booth — Online Event Booths

Depends on: website_event, event_booth.

## `event.event` (extends)

- `exhibition_map` Image “Exhibition Map”
- `booth_menu` Boolean “Booth Register” (store, compute=_compute_booth_menu)
- `booth_menu_ids` One2many → `website.event.menu` “Event Booths Menus”

Public methods: `copy_event_menus`, `toggle_booth_menu`

Extension points: `_get_menu_type_field_matching`, `_get_menu_update_fields`, `_get_website_menu_entries`

## `event.type` (extends)

- `booth_menu` Boolean “Booths on Website” (store, compute=_compute_booth_menu)

## `website.event.menu` (extends)

- `menu_type` Selection
