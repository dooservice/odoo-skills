# hr_recruitment_skills — Recruitment - Skills Management

Depends on: hr_skills, hr_recruitment.

## `hr.applicant` (extends)

- `applicant_skill_ids` One2many → `hr.applicant.skill` “Skills”
- `current_applicant_skill_ids` One2many → `hr.applicant.skill` (compute=_compute_current_applicant_skill_ids)
- `skill_ids` Many2many → `hr.skill` (store, compute=_compute_skill_ids)
- `matching_skill_ids` Many2many → `hr.skill` “Matching Skills” (compute=_compute_matching_skill_ids)
- `missing_skill_ids` Many2many → `hr.skill` “Missing Skills” (compute=_compute_matching_skill_ids)
- `matching_score` Integer “Matching Score” (compute=_compute_matching_skill_ids)

Public methods: `action_add_to_job`, `create`, `write`

Extension points: `_get_employee_create_vals`

## `hr.applicant.skill` (defines)

Skill level for an applicant

Inherits: `hr.individual.skill.mixin`

- `applicant_id` Many2one → `hr.applicant` (required, index)

Extension points: `_get_current_skills_by_applicant`

## `hr.job` (extends)

- `applicant_matching_score` Float “Matching Score(%)” (compute=_compute_applicant_matching_score)

Public methods: `action_search_matching_applicants`
