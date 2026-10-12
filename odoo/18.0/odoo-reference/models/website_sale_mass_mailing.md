# website_sale_mass_mailing — Checkout Newsletter

Depends on: website_sale, website_mass_mailing.

## `res.config.settings` (extends)

- `is_newsletter_enabled` Boolean (store, compute=_compute_is_newsletter_enabled)
- `newsletter_id` Many2one (related=website_id.newsletter_id)

Public methods: `set_values`

## `website` (extends)

- `newsletter_id` Many2one → `mailing.list` “Newsletter List”
