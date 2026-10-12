# crm_livechat — CRM Livechat

Depends on: crm, im_livechat.

## `chatbot.script` (extends)

- `lead_count` Integer “Generated Lead Count” (compute=_compute_lead_count)

Public methods: `action_view_leads`

## `chatbot.script.step` (extends)

- `step_type` Selection
- `crm_team_id` Many2one → `crm.team` “Sales Team”

## `crm.lead` (extends)

- `origin_channel_id` Many2one → `discuss.channel` (readonly)

Public methods: `action_open_livechat`, `create`, `write`

## `discuss.channel` (extends)

- `lead_ids` One2many → `crm.lead` “Leads”
- `has_crm_lead` Boolean (store, compute=_compute_has_crm_lead)

Public methods: `execute_command_lead`

Extension points: `_prepare_lead_create_values`

## `res.users` (extends)


## `im_livechat.report.channel` (extends)

- `leads_created` Integer “Leads created” (readonly)
