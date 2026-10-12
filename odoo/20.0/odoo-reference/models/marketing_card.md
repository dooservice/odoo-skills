# marketing_card — Marketing Card

Depends on: link_tracker, mass_mailing, website, base_report_wkhtmltox.

## `card.campaign` (defines)

Marketing Card Campaign

Inherits: `mail.activity.mixin`, `mail.render.mixin`, `mail.thread`

- `name` Char (required)
- `active` Boolean
- `body_html` Html (related=card_template_id.body)
- `card_count` Integer (compute=_compute_card_stats)
- `card_click_count` Integer (compute=_compute_card_stats)
- `card_share_count` Integer (compute=_compute_card_stats)
- `mailing_ids` One2many → `mailing.mailing`
- `mailing_count` Integer (compute=_compute_mailing_count)
- `card_ids` One2many → `card.card`
- `card_template_id` Many2one → `card.template` “Design” (required)
- `image_preview` Image (readonly, store, compute=_compute_image_preview)
- `link_tracker_id` Many2one → `link.tracker`
- `res_model` Selection “Model Name” (required, readonly, store, compute=_compute_res_model)
- `post_suggestion` Text
- `preview_record_ref` Reference “Preview On” (required)
- `tag_ids` Many2many → `card.campaign.tag` “Tags”
- `target_url` Char “Post Link”
- `target_url_click_count` Integer (related=link_tracker_id.count)
- `target_url_placeholder` Char (compute=_compute_target_url_placeholder)
- `user_id` Many2one → `res.users` “Responsible”
- `reward_message` Html “Thank You Message”
- `reward_target_url` Char “Reward Link”
- `request_title` Char “Request”
- `request_description` Text “Request Description”
- `content_background` Image “Background”
- `content_button` Char “Button”
- `content_header` Char “Header”
- `content_header_dyn` Boolean “Is Dynamic Header”
- `content_header_path` Char “Header Path”
- `content_header_color` Char “Header Color”
- `content_sub_header` Char “Sub-Header”
- `content_sub_header_dyn` Boolean “Is Dynamic Sub-Header”
- `content_sub_header_path` Char “Sub-Header Path”
- `content_sub_header_color` Char “Sub Header Color”
- `content_section` Char “Section”
- `content_section_dyn` Boolean “Is Dynamic Section”
- `content_section_path` Char “Section Path”
- `content_sub_section1` Char “Sub-Section 1”
- `content_sub_section1_dyn` Boolean “Is Dynamic Sub-Section 1”
- `content_sub_section1_path` Char “Sub-Section 1 Path”
- `content_sub_section2` Char “Sub-Section 2”
- `content_sub_section2_dyn` Boolean “Is Dynamic Sub-Section 2”
- `content_sub_section2_path` Char “Sub-Section 2 Path”
- `content_image1_path` Char “Dynamic Image 1”
- `content_image2_path` Char “Dynamic Image 2”

Public methods: `action_preview`, `action_share`, `action_view_cards`, `action_view_cards_clicked`, `action_view_cards_shared`, `action_view_mailings`, `create`, `write`

Extension points: `_action_share_get_default_body`, `_check_access_right_dynamic_template`, `_get_card_element_values`, `_get_image_bin`, `_get_model_dependent_fields`, `_get_model_selection`, `_get_record_url`, `_get_render_fields`, `_get_url_from_res_id`

## `card.campaign.tag` (defines)

Marketing Card Campaign Tag

- `name` Char (required)
- `color` Integer

Extension points: `_get_default_color`

## `card.card` (defines)

Marketing Card

- `active` Boolean “Active”
- `lang` Selection “Language” (required)
- `campaign_id` Many2one → `card.campaign` (required, index)
- `res_model` Selection (related=campaign_id.res_model)
- `res_id` Many2oneReference “Record ID” (required)
- `image` Image
- `requires_sync` Boolean
- `share_status` Selection

Extension points: `_get_card_url`, `_get_path`, `_get_redirect_url`

## `card.template` (defines)

Marketing Card Template

- `name` Char (required)
- `default_background` Image
- `body` Html
- `primary_color` Char (required)
- `secondary_color` Char (required)
- `primary_text_color` Char (required)
- `secondary_text_color` Char (required)

## `ir.model` (extends)


## `mailing.mailing` (extends)

- `card_lang` Selection “Card Language” (store, compute=_compute_card_lang)
- `card_requires_sync_count` Integer (compute=_compute_card_requires_sync_count)
- `card_campaign_id` Many2one → `card.campaign`

Public methods: `action_put_in_queue`, `action_send_mail`, `action_update_cards`

Extension points: `_check_mailing_domain`, `_check_mailing_lang`, `_get_recipients_domain`

## `utm.source` (extends)


## `mail.compose.message` (extends)


Extension points: `_get_done_emails`, `_prepare_mail_values_dynamic`
