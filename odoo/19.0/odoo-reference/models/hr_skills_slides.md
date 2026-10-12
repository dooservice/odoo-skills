# hr_skills_slides — Skills e-learning

Depends on: hr_skills, website_slides.

## `hr.employee` (extends)

- `subscribed_courses` Many2many → `slide.channel` (related=user_partner_id.slide_channel_ids)
- `has_subscribed_courses` Boolean (compute=_compute_courses_completion_text)
- `courses_completion_text` Char (compute=_compute_courses_completion_text)

Public methods: `action_open_courses`

## `hr.employee.public` (extends)

- `has_subscribed_courses` Boolean (related=employee_id.has_subscribed_courses)
- `courses_completion_text` Char (related=employee_id.courses_completion_text)

Public methods: `action_open_courses`

## `hr.resume.line` (extends)

- `channel_id` Many2one → `slide.channel` “eLearning Course” (readonly, store, compute=_compute_channel_id)
- `course_url` Char (related=channel_id.website_absolute_url)
- `duration` Integer “Duration” (store, compute=_compute_duration)
- `course_type` Selection

## `slide.channel.partner` (extends)


Extension points: `_post_completion_update_hook`

## `slide.channel` (extends)


Extension points: `_action_add_members`
