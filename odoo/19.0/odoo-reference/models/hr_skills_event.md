# hr_skills_event — Skills Events

Depends on: hr_skills, event.

## `event.event` (extends)


Public methods: `create`

## `hr.resume.line` (extends)

- `event_id` Many2one → `event.event` “Onsite Course” (readonly, store, compute=_compute_event_id)
- `course_type` Selection
