# survey_crm — Survey CRM

Depends on: survey, crm.

## `crm.lead` (extends)

- `origin_survey_id` Many2one → `survey.survey` “Survey”

## `crm.team` (extends)

- `origin_survey_ids` One2many → `survey.survey` “Survey opportunities related to the sales team”

## `survey.question` (extends)

- `survey_type` Selection (related=survey_id.survey_type)
- `generate_lead` Boolean “Lead Generating” (compute=_compute_generate_lead)

## `survey.question.answer` (extends)

- `generate_lead` Boolean “Lead creation”

## `survey.survey` (extends)

- `generate_lead` Boolean “Lead Generating” (compute=_compute_generate_lead)
- `lead_count` Integer “Leads” (compute=_compute_lead_count)
- `lead_ids` One2many → `crm.lead`
- `team_id` Many2one → `crm.team` “Assign Leads to”

Public methods: `action_end_session`, `action_survey_see_leads`

## `survey.user_input` (extends)

- `lead_id` Many2one → `crm.lead`

Public methods: `action_redirect_lead`

Extension points: `_create_leads_from_generative_answers`, `_prepare_common_survey_lead_values`, `_prepare_lead_values_from_user_input_lines`, `_prepare_user_input_lead_values`

## `survey.survey` (extends)


Public methods: `get_survey_templates_data`

Extension points: `_get_survey_template_values`, `_prepare_lead_qualification_template_values`
