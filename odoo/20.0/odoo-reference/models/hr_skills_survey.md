# hr_skills_survey — Skills Certification

Depends on: hr_skills, survey.

## `hr.resume.line` (extends)

- `department_id` Many2one (store, related=employee_id.department_id)
- `survey_id` Many2one → `survey.survey` “Certification” (readonly)
- `expiration_status` Selection (store, compute=_compute_expiration_status)

## `survey.survey` (extends)

- `certification_validity_months` Integer “Validity”

## `survey.user_input` (extends)
