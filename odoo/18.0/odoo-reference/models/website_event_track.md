# website_event_track — Advanced Events

Depends on: website_event.

## `event.event` (extends)

- `track_ids` One2many → `event.track`
- `track_count` Integer “Track Count” (compute=_compute_track_count)
- `website_track` Boolean “Tracks on Website” (store, compute=_compute_website_track)
- `website_track_proposal` Boolean “Proposals on Website” (store, compute=_compute_website_track_proposal)
- `track_menu_ids` One2many → `website.event.menu` “Event Tracks Menus”
- `track_proposal_menu_ids` One2many → `website.event.menu` “Event Proposals Menus”
- `allowed_track_tag_ids` Many2many → `event.track.tag` “Available Track Tags”
- `tracks_tag_ids` Many2many → `event.track.tag` “Track Tags” (store, compute=_compute_tracks_tag_ids)

Public methods: `toggle_website_track`, `toggle_website_track_proposal`

Extension points: `_get_menu_type_field_matching`, `_get_menu_update_fields`, `_get_website_menu_entries`

## `event.track` (defines)

Event Track

Inherits: `mail.thread`, `mail.activity.mixin`, `website.seo.metadata`, `website.published.mixin`

- `name` Char “Title” (required)
- `event_id` Many2one → `event.event` (required)
- `active` Boolean
- `user_id` Many2one → `res.users`
- `company_id` Many2one → `res.company` (related=event_id.company_id)
- `tag_ids` Many2many → `event.track.tag` “Tags”
- `description` Html
- `color` Integer “Agenda Color”
- `priority` Selection (required)
- `stage_id` Many2one → `event.track.stage` “Stage” (required, index)
- `legend_blocked` Char “Kanban Blocked Explanation” (readonly, related=stage_id.legend_blocked)
- `legend_done` Char “Kanban Valid Explanation” (readonly, related=stage_id.legend_done)
- `legend_normal` Char “Kanban Ongoing Explanation” (readonly, related=stage_id.legend_normal)
- `kanban_state` Selection “Kanban State” (required)
- `kanban_state_label` Char “Kanban State Label” (store, compute=_compute_kanban_state_label)
- `partner_id` Many2one → `res.partner`
- `partner_name` Char “Name” (store, compute=_compute_partner_name)
- `partner_email` Char “Email” (store, compute=_compute_partner_email)
- `partner_phone` Char “Phone” (store, compute=_compute_partner_phone)
- `partner_biography` Html “Biography” (store, compute=_compute_partner_biography)
- `partner_function` Char “Job Position” (store, compute=_compute_partner_function)
- `partner_company_name` Char “Company Name” (store, compute=_compute_partner_company_name)
- `partner_tag_line` Char “Tag Line” (compute=_compute_partner_tag_line)
- `image` Image “Speaker Photo” (store, compute=_compute_partner_image)
- `contact_email` Char “Contact Email” (store, compute=_compute_contact_email)
- `contact_phone` Char “Contact Phone” (store, compute=_compute_contact_phone)
- `location_id` Many2one → `event.track.location`
- `date` Datetime “Track Date”
- `date_end` Datetime “Track End Date” (store, compute=_compute_end_date)
- `duration` Float “Duration”
- `is_track_live` Boolean “Is Track Live” (compute=_compute_track_time_data)
- `is_track_soon` Boolean “Is Track Soon” (compute=_compute_track_time_data)
- `is_track_today` Boolean “Is Track Today” (compute=_compute_track_time_data)
- `is_track_upcoming` Boolean “Is Track Upcoming” (compute=_compute_track_time_data)
- `is_track_done` Boolean “Is Track Done” (compute=_compute_track_time_data)
- `track_start_remaining` Integer “Minutes before track starts” (compute=_compute_track_time_data)
- `track_start_relative` Integer “Minutes compare to track start” (compute=_compute_track_time_data)
- `website_image` Image “Website Image”
- `website_image_url` Char “Image URL” (compute=_compute_website_image_url)
- `event_track_visitor_ids` One2many → `event.track.visitor` “Track Visitors”
- `is_reminder_on` Boolean “Is Reminder On” (compute=_compute_is_reminder_on)
- `wishlist_visitor_ids` Many2many → `website.visitor` “Visitor Wishlist” (compute=_compute_wishlist_visitor_ids)
- `wishlist_visitor_count` Integer “# Wishlisted” (compute=_compute_wishlist_visitor_ids)
- `wishlisted_by_default` Boolean “Always Wishlisted”
- `website_cta` Boolean “Magic Button”
- `website_cta_title` Char “Button Title”
- `website_cta_url` Char “Button Target URL”
- `website_cta_delay` Integer “Show Button”
- `is_website_cta_live` Boolean “Is CTA Live” (compute=_compute_cta_time_data)
- `website_cta_start_remaining` Integer “Minutes before CTA starts” (compute=_compute_cta_time_data)

Public methods: `create`, `get_backend_menu_id`, `open_track_speakers_list`, `write`

Extension points: `_get_default_stage_id`, `_get_event_track_visitors`, `_get_track_suggestions`

## `event.track.location` (defines)

Event Track Location

- `name` Char “Location” (required)
- `sequence` Integer

## `event.track.stage` (defines)

Event Track Stage

- `name` Char “Stage Name” (required)
- `sequence` Integer “Sequence”
- `mail_template_id` Many2one → `mail.template` “Email Template”
- `color` Integer “Color”
- `description` Text “Description”
- `legend_blocked` Char “Red Kanban Label”
- `legend_done` Char “Green Kanban Label”
- `legend_normal` Char “Grey Kanban Label”
- `fold` Boolean “Folded in Kanban”
- `is_visible_in_agenda` Boolean “Visible in agenda” (store, compute=_compute_is_visible_in_agenda)
- `is_fully_accessible` Boolean “Fully accessible” (store, compute=_compute_is_fully_accessible)
- `is_cancel` Boolean “Cancelled Stage”

## `event.track.tag` (defines)

Event Track Tag

- `name` Char “Tag Name” (required)
- `track_ids` Many2many → `event.track` “Tracks”
- `color` Integer “Color Index”
- `sequence` Integer “Sequence”
- `category_id` Many2one → `event.track.tag.category` “Category”

## `event.track.tag.category` (defines)

Event Track Tag Category

- `name` Char “Name” (required)
- `sequence` Integer “Sequence”
- `tag_ids` One2many → `event.track.tag` “Tags”

## `event.track.visitor` (defines)

Track / Visitor Link

- `partner_id` Many2one → `res.partner` “Partner” (store, index, compute=_compute_partner_id)
- `visitor_id` Many2one → `website.visitor` “Visitor” (index)
- `track_id` Many2one → `event.track` “Track” (required, index)
- `is_wishlisted` Boolean “Is Wishlisted”
- `is_blacklisted` Boolean “Is reminder off”

## `event.type` (extends)

- `website_track` Boolean “Tracks on Website” (store, compute=_compute_website_track_menu_data)
- `website_track_proposal` Boolean “Tracks Proposals on Website” (store, compute=_compute_website_track_menu_data)

## `res.config.settings` (extends)

- `events_app_name` Char “Events App Name” (related=website_id.events_app_name)

## `website` (extends)

- `app_icon` Image “Website App Icon” (readonly, store, compute=_compute_app_icon)
- `events_app_name` Char “Events App Name” (store, compute=_compute_events_app_name)

Extension points: `_check_events_app_name`

## `website.event.menu` (extends)

- `menu_type` Selection

## `website.menu` (extends)


Public methods: `unlink`

## `website.visitor` (extends)

- `event_track_visitor_ids` One2many → `event.track.visitor` “Track Visitors”
- `event_track_wishlisted_ids` Many2many → `event.track` “Wishlisted Tracks” (compute=_compute_event_track_wishlisted_ids)
- `event_track_wishlisted_count` Integer “# Wishlisted” (compute=_compute_event_track_wishlisted_ids)
