# crm_livechat — CRM Livechat

Depends on: crm, im_livechat.

## `chatbot.script` (extends)

- `lead_count` Integer “Generated Lead Count” (compute=_compute_lead_count)

Public methods: `action_view_leads`

## `chatbot.script.step` (extends)

- `step_type` Selection
- `crm_team_id` Many2one → `crm.team` “Sales Team”

## `discuss.channel` (extends)


Public methods: `execute_command_lead`
