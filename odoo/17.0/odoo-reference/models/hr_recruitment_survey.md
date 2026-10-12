# hr_recruitment_survey — Hr Recruitment Interview Forms

Depends on: survey, hr_recruitment.

## `hr.applicant` (extends)

- `survey_id` Many2one → `survey.survey` “Survey” (readonly, related=job_id.survey_id)
- `response_ids` One2many → `survey.user_input` “Responses”

Public methods: `action_print_survey`, `action_send_survey`

## `hr.job` (extends)

- `survey_id` Many2one → `survey.survey`

Public methods: `action_new_survey`, `action_test_survey`

## `survey.user_input` (extends)

- `applicant_id` Many2one → `hr.applicant` “Applicant”

## `survey.invite` (extends)

- `applicant_id` Many2one → `hr.applicant` “Applicant”

Public methods: `action_invite`

Extension points: `_get_done_partners_emails`
