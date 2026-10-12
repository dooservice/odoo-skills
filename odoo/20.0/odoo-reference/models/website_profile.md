# website_profile — Website profile

Depends on: html_editor, website_partner, gamification.

## `gamification.badge` (extends)

Inherits: `website.published.mixin`


## `res.users` (extends)

- `country_id` Many2one (related=partner_id.country_id)
- `city` Char (related=partner_id.city)
- `website` Char (related=partner_id.website)
- `website_description` Html (related=partner_id.website_description)
- `website_published` Boolean (related=partner_id.website_published)

## `website` (extends)

- `karma_profile_min` Integer “Minimal karma to see other user's profile”
