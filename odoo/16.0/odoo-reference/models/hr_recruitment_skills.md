# hr_recruitment_skills — Recruitment - Skills Management

Depends on: hr_skills, hr_recruitment.

## `hr.applicant` (extends)

- `applicant_skill_ids` One2many → `hr.applicant.skill` “Skills”
- `skill_ids` Many2many → `hr.skill` (store, compute=_compute_skill_ids)
- `is_interviewer` Boolean (compute=_compute_is_interviewer)

Public methods: `create_employee_from_applicant`

## `hr.applicant.skill` (defines)

Skill level for an applicant

- `applicant_id` Many2one → `hr.applicant` (required)
- `skill_id` Many2one → `hr.skill` (required, store, compute=_compute_skill_id)
- `skill_level_id` Many2one → `hr.skill.level` (required, store, compute=_compute_skill_level_id)
- `skill_type_id` Many2one → `hr.skill.type` (required)
- `level_progress` Integer (related=skill_level_id.level_progress)

Extension points: `_check_skill_level`, `_check_skill_type`
