# hr_recruitment_survey — Hr Recruitment Interview Forms

Depends on: survey, hr_recruitment.

## `hr.applicant` (extends)

- `survey_id` Many2one → `survey.survey` “Survey” (readonly, related=job_id.survey_id)
- `response_ids` One2many → `survey.user_input` “Responses”

Public methods: `action_archive`, `action_print_survey`, `action_send_survey`, `write`

## `hr.job` (extends)

- `survey_id` Many2one → `survey.survey`

Public methods: `action_new_survey`, `action_test_survey`

## `survey.survey` (extends)

- `survey_type` Selection
- `hr_job_ids` One2many → `hr.job` “Job Position”
- `job_count` Integer “Job Count” (compute=_compute_job_count)

Public methods: `action_open_jobs`, `action_survey_user_input_completed`, `get_formview_id`

## `survey.user_input` (extends)

- `applicant_id` Many2one → `hr.applicant` “Applicant”

## `hr.recruitment.survey.invite` (defines)

Wizard for sending interview invitations to job applicants during recruitment process

Inherits: `survey.invite`

- `applicant_ids` Many2many → `hr.applicant` “Applicant”
- `survey_ids` Many2many → `survey.survey` “Surveys”
- `single_survey_id` Many2one → `survey.survey` (compute=_compute_single_survey)
- `has_many_applicants` Boolean (compute=_compute_has_many_applicants)
- `hide_url` Boolean (compute=_compute_hide_url)
- `survey_id` Many2one → `survey.survey`
- `survey_access_mode` Char (compute=_compute_survey_access_mode)
- `survey_start_url` Char “Survey URL” (compute=_compute_survey_start_url)
- `attachment_ids` Many2many → `ir.attachment` “Attachments” (store, compute=_compute_attachment_ids)
- `partner_ids` Many2many → `res.partner` “Recipients”
- `accessible_by_current_user` Boolean (compute=_compute_accessible_by_current_user)
- `accessible_by_interviewer_user` Boolean (compute=_compute_accessible_by_interviewer_user)
- `all_surveys_are_recruitment` Boolean (compute=_compute_all_surveys_are_recruitment)

Public methods: `action_invite`

Extension points: `_check_partners_access`, `_prepare_answers`
