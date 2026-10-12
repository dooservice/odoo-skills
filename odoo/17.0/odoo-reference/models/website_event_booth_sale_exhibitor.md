# website_event_booth_sale_exhibitor — Booths Sale/Exhibitors Bridge

Depends on: website_event_exhibitor, website_event_booth_sale.

## `event.booth.registration` (extends)

- `sponsor_name` Char “Sponsor Name”
- `sponsor_email` Char “Sponsor Email”
- `sponsor_mobile` Char “Sponsor Mobile”
- `sponsor_phone` Char “Sponsor Phone”
- `sponsor_subtitle` Char “Sponsor Slogan”
- `sponsor_website_description` Html “Sponsor Description”
- `sponsor_image_512` Image “Sponsor Logo”

Extension points: `_get_fields_for_booth_confirmation`
