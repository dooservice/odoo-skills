# rating — Customer Rating

Depends on: mail.

## `mail.message` (extends)

- `rating_ids` One2many → `rating.rating` “Related ratings”
- `rating_id` Many2one → `rating.rating` (compute=_compute_rating_id)
- `rating_value` Float “Rating Value” (compute=_compute_rating_value)

## `mail.thread` (extends)

- `rating_ids` One2many → `rating.rating` “Ratings”

Public methods: `message_post`, `rating_apply`, `rating_send_request`, `unlink`

Extension points: `_get_allowed_message_update_params`, `_get_message_create_ignore_field_names`

## `rating.rating` (defines)

Rating

- `create_date` Datetime “Submitted on”
- `res_name` Char “Resource name” (store, compute=_compute_res_name)
- `res_model_id` Many2one → `ir.model` (index)
- `res_model` Char “Document Model” (readonly, store, index, related=res_model_id.model)
- `res_id` Many2oneReference “Document” (required, index)
- `resource_ref` Reference “Resource Ref” (readonly, compute=_compute_resource_ref)
- `parent_res_name` Char “Parent Document Name” (store, compute=_compute_parent_res_name)
- `parent_res_model_id` Many2one → `ir.model` (index)
- `parent_res_model` Char “Parent Document Model” (store, index, related=parent_res_model_id.model)
- `parent_res_id` Integer “Parent Document” (index)
- `parent_ref` Reference “Parent Ref” (readonly, compute=_compute_parent_ref)
- `rated_partner_id` Many2one → `res.partner` “Rated Operator”
- `rated_partner_name` Char (related=rated_partner_id.name)
- `partner_id` Many2one → `res.partner` “Customer”
- `rating` Float “Rating Value”
- `rating_image` Binary “Image” (compute=_compute_rating_image)
- `rating_image_url` Char “Image URL” (compute=_compute_rating_image)
- `rating_text` Selection “Rating” (readonly, store, compute=_compute_rating_text)
- `feedback` Text “Comment”
- `message_id` Many2one → `mail.message` “Message” (index)
- `is_internal` Boolean “Visible Internally Only” (store, related=message_id.is_internal)
- `access_token` Char “Security Token”
- `consumed` Boolean “Filled Rating”

Public methods: `action_open_rated_object`, `create`, `reset`, `unlink`, `write`

Extension points: `_get_rating_image_filename`

## `rating.mixin` (defines)

Rating Mixin

Inherits: `mail.thread`

- `rating_last_value` Float “Rating Last Value” (store, compute=_compute_rating_last_value)
- `rating_last_feedback` Text “Rating Last Feedback” (related=rating_ids.feedback)
- `rating_last_image` Binary “Rating Last Image” (related=rating_ids.rating_image)
- `rating_count` Integer “Rating count” (compute=_compute_rating_stats)
- `rating_avg` Float “Average Rating” (compute=_compute_rating_stats)
- `rating_avg_text` Selection (compute=_compute_rating_avg_text)
- `rating_percentage_satisfaction` Float “Rating Satisfaction” (compute=_compute_rating_satisfaction)
- `rating_last_text` Selection “Rating Text” (related=rating_ids.rating_text)

Public methods: `rating_get_grades`, `rating_get_stats`, `write`

## `rating.parent.mixin` (defines)

Rating Parent Mixin

- `rating_ids` One2many → `rating.rating` “Ratings”
- `rating_percentage_satisfaction` Integer “Rating Satisfaction” (compute=_compute_rating_percentage_satisfaction)
- `rating_count` Integer “# Ratings” (compute=_compute_rating_percentage_satisfaction)
- `rating_avg` Float “Average Rating” (compute=_compute_rating_percentage_satisfaction)
- `rating_avg_percentage` Float “Average Rating (%)” (compute=_compute_rating_percentage_satisfaction)
