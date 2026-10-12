# mass_mailing_crm — Mass mailing on lead / opportunities

Depends on: crm, mass_mailing.

## `crm.lead` (extends)


## `mailing.mailing` (extends)

- `use_leads` Boolean “Use Leads” (compute=_compute_use_leads)
- `crm_lead_count` Integer “Leads/Opportunities Count” (compute=_compute_crm_lead_count)

Public methods: `action_create_mailing_template_with_leads`, `action_redirect_to_leads_and_opportunities`

Extension points: `_prepare_statistics_email_values`

## `utm.campaign` (extends)

- `ab_testing_winner_selection` Selection
