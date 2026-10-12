# website_slides_survey — Course Certifications

Depends on: website_slides, survey.

## `slide.channel` (extends)

- `nbr_certification` Integer “Number of Certifications” (store, compute=_compute_slides_statistics)

## `slide.slide.partner` (extends)

- `user_input_ids` One2many → `survey.user_input`
- `survey_scoring_success` Boolean “Certification Succeeded” (store, compute=_compute_survey_scoring_success)

## `slide.slide` (extends)

- `name` Char (store, compute=_compute_name)
- `slide_category` Selection
- `slide_type` Selection
- `survey_id` Many2one → `survey.survey`
- `nbr_certification` Integer “Number of Certifications” (store, compute=_compute_slides_statistics)
- `is_preview` Boolean (store, compute=_compute_is_preview)

Public methods: `create`, `unlink`, `write`

## `survey.survey` (extends)

- `slide_ids` One2many → `slide.slide` “Certification Slides”
- `slide_channel_ids` One2many → `slide.channel` “Certification Courses” (compute=_compute_slide_channel_data)
- `slide_channel_count` Integer “Courses Count” (compute=_compute_slide_channel_data)

Public methods: `action_survey_view_slide_channels`

Extension points: `_check_answer_creation`, `_prepare_challenge_category`

## `survey.user_input` (extends)

- `slide_id` Many2one → `slide.slide`
- `slide_partner_id` Many2one → `slide.slide.partner`

Public methods: `create`, `write`

Extension points: `_check_for_failed_attempt`
