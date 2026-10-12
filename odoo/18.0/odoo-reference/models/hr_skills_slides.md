# hr_skills_slides — Skills e-learning

Depends on: hr_skills, website_slides.

## `hr.employee` (extends)

- `subscribed_courses` Many2many → `slide.channel` (related=user_partner_id.slide_channel_ids)
- `has_subscribed_courses` Boolean (compute=_compute_courses_completion_text)
- `courses_completion_text` Char (compute=_compute_courses_completion_text)

Public methods: `action_open_courses`

## `hr.resume.line` (extends)

- `display_type` Selection
- `channel_id` Many2one → `slide.channel` “Course” (readonly)
- `course_url` Char (compute=_compute_course_url)

## `slide.channel.partner` (extends)


## `slide.channel` (extends)


Extension points: `_action_add_members`
