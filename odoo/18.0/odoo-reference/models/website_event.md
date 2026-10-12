# website_event — Events

Depends on: event, website, website_partner, website_mail.

## `event.event` (extends)

Inherits: `website.seo.metadata`, `website.published.multi.mixin`, `website.cover_properties.mixin`, `website.searchable.mixin`

- `subtitle` Char “Event Subtitle”
- `is_participating` Boolean “Is Participating” (compute=_compute_is_participating)
- `is_visible_on_website` Boolean “Visible On Website” (compute=_compute_is_visible_on_website)
- `event_register_url` Char “Event Registration Link” (compute=_compute_event_register_url)
- `website_visibility` Selection “Website Visibility” (required)
- `website_published` Boolean
- `website_menu` Boolean “Website Menu” (store, compute=_compute_website_menu)
- `menu_id` Many2one → `website.menu`
- `introduction_menu` Boolean “Introduction Menu” (store, compute=_compute_website_menu_data)
- `introduction_menu_ids` One2many → `website.event.menu` “Introduction Menus”
- `location_menu` Boolean “Location Menu” (store, compute=_compute_website_menu_data)
- `location_menu_ids` One2many → `website.event.menu` “Location Menus”
- `address_name` Char (related=address_id.name)
- `register_menu` Boolean “Register Menu” (store, compute=_compute_website_menu_data)
- `register_menu_ids` One2many → `website.event.menu` “Register Menus”
- `community_menu` Boolean “Community Menu” (store, compute=_compute_community_menu)
- `community_menu_ids` One2many → `website.event.menu` “Event Community Menus”
- `is_ongoing` Boolean “Is Ongoing” (compute=_compute_time_data)
- `is_done` Boolean “Is Done” (compute=_compute_time_data)
- `start_today` Boolean “Start Today” (compute=_compute_time_data)
- `start_remaining` Integer “Remaining before start” (compute=_compute_time_data)

Public methods: `create`, `get_backend_menu_id`, `google_map_link`, `toggle_website_menu`, `write`

Extension points: `_check_website_id`, `_create_menu`, `_get_event_resource_urls`, `_get_external_description`, `_get_menu_type_field_matching`, `_get_menu_update_fields`, `_get_menus_update_by_field`, `_get_website_menu_entries`

## `event.registration` (extends)

- `visitor_id` Many2one → `website.visitor` “Visitor”

Public methods: `get_base_url`

Extension points: `_get_website_registration_allowed_fields`

## `event.tag` (extends)

Inherits: `website.published.multi.mixin`


Public methods: `default_get`

## `event.tag.category` (extends)

Inherits: `website.published.multi.mixin`


## `event.type` (extends)

- `website_menu` Boolean “Display a dedicated menu on Website”
- `community_menu` Boolean “Community Menu” (store, compute=_compute_community_menu)

## `website` (extends)


Public methods: `get_cta_data`, `get_suggested_controllers`

## `website.event.menu` (defines)

Website Event Menu

- `menu_id` Many2one → `website.menu` “Menu”
- `event_id` Many2one → `event.event` “Event”
- `view_id` Many2one → `ir.ui.view` “View”
- `menu_type` Selection “Menu Type” (required)

Public methods: `unlink`

## `website.menu` (extends)


Public methods: `unlink`

## `website.snippet.filter` (extends)


Extension points: `_get_hardcoded_sample`

## `website.visitor` (extends)

- `event_registration_ids` One2many → `event.registration` “Event Registrations”
- `event_registration_count` Integer “# Registrations” (compute=_compute_event_registration_count)
- `event_registered_ids` Many2many → `event.event` “Registered Events” (compute=_compute_event_registered_ids)
