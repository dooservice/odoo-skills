# website_event_exhibitor — Event Exhibitors

Depends on: website_event_jitsi.

## `event.event` (extends)

- `sponsor_ids` One2many → `event.sponsor`
- `sponsor_count` Integer “Sponsor Count” (compute=_compute_sponsor_count)
- `exhibitor_menu` Boolean “Showcase Exhibitors” (store, compute=_compute_exhibitor_menu)
- `exhibitor_menu_ids` One2many → `website.event.menu` “Exhibitors Menus”

Public methods: `toggle_exhibitor_menu`

Extension points: `_get_menu_type_field_matching`, `_get_menu_update_fields`, `_get_website_menu_entries`

## `event.sponsor` (defines)

Event Sponsor

Inherits: `mail.thread`, `mail.activity.mixin`, `website.published.mixin`, `chat.room.mixin`

- `event_id` Many2one → `event.event` (required)
- `sponsor_type_id` Many2one → `event.sponsor.type` (required)
- `url` Char “Sponsor Website” (store, compute=_compute_url)
- `sequence` Integer “Sequence”
- `active` Boolean
- `subtitle` Char “Slogan”
- `exhibitor_type` Selection “Sponsor Type”
- `website_description` Html “Description” (store, compute=_compute_website_description)
- `partner_id` Many2one → `res.partner` (required)
- `partner_name` Char “Name” (related=partner_id.name)
- `partner_email` Char “Email” (related=partner_id.email)
- `partner_phone` Char “Phone” (related=partner_id.phone)
- `partner_mobile` Char “Mobile” (related=partner_id.mobile)
- `name` Char “Sponsor Name” (store, compute=_compute_name)
- `email` Char “Sponsor Email” (store, compute=_compute_email)
- `phone` Char “Sponsor Phone” (store, compute=_compute_phone)
- `mobile` Char “Sponsor Mobile” (store, compute=_compute_mobile)
- `image_512` Image “Logo” (store, compute=_compute_image_512)
- `image_256` Image “Image 256” (related=image_512)
- `image_128` Image “Image 128” (related=image_512)
- `website_image_url` Char “Image URL” (compute=_compute_website_image_url)
- `hour_from` Float “Opening hour”
- `hour_to` Float “End hour”
- `event_date_tz` Selection “Timezone” (readonly, related=event_id.date_tz)
- `is_in_opening_hours` Boolean “Within opening hours” (compute=_compute_is_in_opening_hours)
- `chat_room_id` Many2one
- `room_name` Char
- `country_id` Many2one → `res.country` “Country” (readonly, related=partner_id.country_id)
- `country_flag_url` Char “Country Flag” (compute=_compute_country_flag_url)

Public methods: `create`, `get_backend_menu_id`, `open_website_url`, `write`

## `event.sponsor.type` (defines)

Event Sponsor Level

- `name` Char “Sponsor Level” (required)
- `sequence` Integer “Sequence”
- `display_ribbon_style` Selection “Ribbon Style”

## `event.type` (extends)

- `exhibitor_menu` Boolean “Showcase Exhibitors” (store, compute=_compute_exhibitor_menu)

## `website.event.menu` (extends)

- `menu_type` Selection
