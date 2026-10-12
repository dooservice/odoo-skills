# hr_recruitment_skills — Recruitment - Skills Management

Depends on: hr_skills, hr_recruitment.

## `hr.applicant` (extends)

- `candidate_skill_ids` One2many (related=candidate_id.candidate_skill_ids)
- `skill_ids` Many2many (related=candidate_id.skill_ids)

## `hr.candidate` (extends)

- `candidate_skill_ids` One2many → `hr.candidate.skill` “Skills”
- `skill_ids` Many2many → `hr.skill` (store, compute=_compute_skill_ids)
- `matching_skill_ids` Many2many → `hr.skill` “Matching Skills” (compute=_compute_matching_skill_ids)
- `missing_skill_ids` Many2many → `hr.skill` “Missing Skills” (compute=_compute_matching_skill_ids)
- `matching_score` Float “Matching Score(%)” (compute=_compute_matching_skill_ids)

Public methods: `action_create_application`

Extension points: `_get_employee_create_vals`

## `hr.candidate.skill` (defines)

Skill level for a candidate

- `candidate_id` Many2one → `hr.candidate` (required)
- `skill_id` Many2one → `hr.skill` (required, store, compute=_compute_skill_id)
- `skill_level_id` Many2one → `hr.skill.level` (required, store, compute=_compute_skill_level_id)
- `skill_type_id` Many2one → `hr.skill.type` (required)
- `level_progress` Integer (related=skill_level_id.level_progress)

Extension points: `_check_skill_level`, `_check_skill_type`

## `hr.job` (extends)

- `skill_ids` Many2many → `hr.skill` “Expected Skills”

Public methods: `action_search_matching_candidates`
