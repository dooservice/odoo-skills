# website_event_booth_exhibitor — Booths/Exhibitors Bridge

Depends on: website_event_exhibitor, website_event_booth.

## `event.booth` (extends)

- `use_sponsor` Boolean (related=booth_category_id.use_sponsor)
- `sponsor_type_id` Many2one (related=booth_category_id.sponsor_type_id)
- `sponsor_id` Many2one → `event.sponsor` “Sponsor”
- `sponsor_name` Char “Sponsor Name” (related=sponsor_id.name)
- `sponsor_email` Char “Sponsor Email” (related=sponsor_id.email)
- `sponsor_phone` Char “Sponsor Phone” (related=sponsor_id.phone)
- `sponsor_subtitle` Char “Sponsor Slogan” (related=sponsor_id.subtitle)
- `sponsor_website_description` Html “Sponsor Description” (related=sponsor_id.website_description)
- `sponsor_image_512` Image “Sponsor Logo” (related=sponsor_id.image_512)

Public methods: `action_view_sponsor`

Extension points: `_action_post_confirm`, `_get_or_create_sponsor`

## `event.booth.category` (extends)

- `use_sponsor` Boolean “Create Sponsor”
- `sponsor_type_id` Many2one → `event.sponsor.type` “Sponsor Level”
- `exhibitor_type` Selection “Sponsor Type”

Extension points: `_get_exhibitor_type`
