# crm — CRM

Depends on: base_setup, sales_team, mail, calendar, resource, utm, web_tour, web_kanban_gauge, contacts, digest, phone_validation.

## `calendar.event` (extends)

- `opportunity_id` Many2one → `crm.lead` (index)

Public methods: `create`, `default_get`

## `crm.lead` (defines)

Lead/Opportunity

Inherits: `mail.thread.cc`, `mail.thread.blacklist`, `mail.thread.phone`, `mail.activity.mixin`, `utm.mixin`, `format.address.mixin`

- `name` Char “Opportunity” (required, store, compute=_compute_name)
- `user_id` Many2one → `res.users` “Salesperson” (index)
- `user_company_ids` Many2many → `res.company` (compute=_compute_user_company_ids)
- `team_id` Many2one → `crm.team` “Sales Team” (store, index, compute=_compute_team_id)
- `lead_properties` Properties “Properties”
- `company_id` Many2one → `res.company` “Company” (store, index, compute=_compute_company_id)
- `referred` Char “Referred By”
- `description` Html “Notes”
- `active` Boolean “Active”
- `type` Selection (required, index)
- `priority` Selection “Priority” (index)
- `stage_id` Many2one → `crm.stage` “Stage” (store, index, compute=_compute_stage_id)
- `kanban_state` Selection “Kanban State” (compute=_compute_kanban_state)
- `tag_ids` Many2many → `crm.tag` “Tags”
- `color` Integer “Color Index”
- `expected_revenue` Monetary “Expected Revenue”
- `prorated_revenue` Monetary “Prorated Revenue” (store, compute=_compute_prorated_revenue)
- `recurring_revenue` Monetary “Recurring Revenues”
- `recurring_plan` Many2one → `crm.recurring.plan` “Recurring Plan”
- `recurring_revenue_monthly` Monetary “Expected MRR” (store, compute=_compute_recurring_revenue_monthly)
- `recurring_revenue_monthly_prorated` Monetary “Prorated MRR” (store, compute=_compute_recurring_revenue_monthly_prorated)
- `company_currency` Many2one → `res.currency` “Currency” (compute=_compute_company_currency)
- `date_closed` Datetime “Closed Date” (readonly)
- `date_action_last` Datetime “Last Action” (readonly)
- `date_open` Datetime “Assignment Date” (readonly, store, compute=_compute_date_open)
- `day_open` Float “Days to Assign” (store, compute=_compute_day_open)
- `day_close` Float “Days to Close” (store, compute=_compute_day_close)
- `date_last_stage_update` Datetime “Last Stage Update” (readonly, store, index, compute=_compute_date_last_stage_update)
- `date_conversion` Datetime “Conversion Date” (readonly)
- `date_deadline` Date “Expected Closing”
- `partner_id` Many2one → `res.partner` “Customer” (index)
- `partner_is_blacklisted` Boolean “Partner is blacklisted” (readonly, related=partner_id.is_blacklisted)
- `contact_name` Char “Contact Name” (store, compute=_compute_contact_name)
- `partner_name` Char “Company Name” (store, compute=_compute_partner_name)
- `function` Char “Job Position” (store, compute=_compute_function)
- `title` Many2one → `res.partner.title` “Title” (store, compute=_compute_title)
- `email_from` Char “Email” (store, compute=_compute_email_from)
- `phone` Char “Phone” (store, compute=_compute_phone)
- `mobile` Char “Mobile” (store, compute=_compute_mobile)
- `phone_state` Selection “Phone Quality” (store, compute=_compute_phone_state)
- `email_state` Selection “Email Quality” (store, compute=_compute_email_state)
- `website` Char “Website” (store, compute=_compute_website)
- `lang_id` Many2one → `res.lang` “Language” (store, compute=_compute_lang_id)
- `lang_code` Char (related=lang_id.code)
- `lang_active_count` Integer (compute=_compute_lang_active_count)
- `street` Char “Street” (store, compute=_compute_partner_address_values)
- `street2` Char “Street2” (store, compute=_compute_partner_address_values)
- `zip` Char “Zip” (store, compute=_compute_partner_address_values)
- `city` Char “City” (store, compute=_compute_partner_address_values)
- `state_id` Many2one → `res.country.state` “State” (store, compute=_compute_partner_address_values)
- `country_id` Many2one → `res.country` “Country” (store, compute=_compute_partner_address_values)
- `probability` Float “Probability” (store, compute=_compute_probabilities)
- `automated_probability` Float “Automated Probability” (readonly, store, compute=_compute_probabilities)
- `is_automated_probability` Boolean “Is automated probability?” (compute=_compute_is_automated_probability)
- `lost_reason_id` Many2one → `crm.lost.reason` “Lost Reason” (index)
- `calendar_event_ids` One2many → `calendar.event` “Meetings”
- `calendar_event_count` Integer “# Meetings” (compute=_compute_calendar_event_count)
- `duplicate_lead_ids` Many2many → `crm.lead` “Potential Duplicate Lead” (compute=_compute_potential_lead_duplicates)
- `duplicate_lead_count` Integer “Potential Duplicate Lead Count” (compute=_compute_potential_lead_duplicates)
- `partner_email_update` Boolean “Partner Email will Update” (compute=_compute_partner_email_update)
- `partner_phone_update` Boolean “Partner Phone will Update” (compute=_compute_partner_phone_update)
- `is_partner_visible` Boolean “Is Partner Visible” (compute=_compute_is_partner_visible)
- `campaign_id` Many2one
- `medium_id` Many2one
- `source_id` Many2one

Public methods: `action_reschedule_meeting`, `action_schedule_meeting`, `action_set_automated_probability`, `action_set_lost`, `action_set_won`, `action_set_won_rainbowman`, `action_show_potential_duplicates`, `action_snooze`, `convert_opportunity`, `copy`, `create`, `get_empty_list_help`, `get_import_templates`, `get_rainbowman_message`, `log_meeting`, `merge_opportunity`, `message_new`, `redirect_lead_opportunity_view`, `search`, `toggle_active`, `unlink`, `write`

Extension points: `_create_customer`, `_get_lead_duplicates`, `_get_opportunity_meeting_view_parameters`, `_get_partner_email_update`, `_get_partner_phone_update`, `_get_rainbowman_message`, `_prepare_address_values_from_partner`, `_prepare_contact_name_from_partner`, `_prepare_customer_values`, `_prepare_partner_name_from_partner`, `_prepare_values_from_partner`

## `crm.lead.scoring.frequency` (defines)

Lead Scoring Frequency

- `variable` Char “Variable” (index)
- `value` Char “Value”
- `won_count` Float “Won Count”
- `lost_count` Float “Lost Count”
- `team_id` Many2one → `crm.team`

## `crm.lead.scoring.frequency.field` (defines)

Fields that can be used for predictive lead scoring computation

- `name` Char (related=field_id.field_description)
- `field_id` Many2one → `ir.model.fields` (required)

## `crm.lost.reason` (defines)

Opp. Lost Reason

- `name` Char “Description” (required)
- `active` Boolean “Active”
- `leads_count` Integer “Leads Count” (compute=_compute_leads_count)

Public methods: `action_lost_leads`

## `crm.recurring.plan` (defines)

CRM Recurring revenue plans

- `name` Char “Plan Name” (required)
- `number_of_months` Integer “# Months” (required)
- `active` Boolean “Active”
- `sequence` Integer “Sequence”

## `crm.stage` (defines)

CRM Stages

- `name` Char “Stage Name” (required)
- `sequence` Integer “Sequence”
- `is_won` Boolean “Is Won Stage?”
- `requirements` Text “Requirements”
- `team_id` Many2one → `crm.team` “Sales Team”
- `fold` Boolean “Folded in Pipeline”
- `team_count` Integer “team_count” (compute=_compute_team_count)

Public methods: `default_get`

## `crm.team` (extends)

Sales Team

Inherits: `mail.alias.mixin`

- `use_leads` Boolean “Leads”
- `use_opportunities` Boolean “Pipeline”
- `alias_id` Many2one → `mail.alias` “Alias” (required)
- `assignment_enabled` Boolean “Lead Assign” (compute=_compute_assignment_enabled)
- `assignment_auto_enabled` Boolean “Auto Assignment” (compute=_compute_assignment_enabled)
- `assignment_optout` Boolean “Skip auto assignment”
- `assignment_max` Integer “Lead Average Capacity” (compute=_compute_assignment_max)
- `assignment_domain` Char “Assignment Domain”
- `lead_unassigned_count` Integer “# Unassigned Leads” (compute=_compute_lead_unassigned_count)
- `lead_all_assigned_month_count` Integer “# Leads/Opps assigned this month” (compute=_compute_lead_all_assigned_month_count)
- `opportunities_count` Integer “# Opportunities” (compute=_compute_opportunities_data)
- `opportunities_amount` Monetary “Opportunities Revenues” (compute=_compute_opportunities_data)
- `opportunities_overdue_count` Integer “# Overdue Opportunities” (compute=_compute_opportunities_overdue_data)
- `opportunities_overdue_amount` Monetary “Overdue Opportunities Revenues” (compute=_compute_opportunities_overdue_data)
- `alias_user_id` Many2one → `res.users` (related=alias_id.alias_user_id)
- `lead_properties_definition` PropertiesDefinition “Lead Properties”

Public methods: `action_assign_leads`, `action_opportunity_forecast`, `action_primary_channel_button`, `action_your_pipeline`, `unlink`, `write`

Extension points: `_action_assign_leads`, `_action_assign_leads_logs`, `_action_update_to_pipeline`

## `crm.team.member` (extends)

- `assignment_enabled` Boolean (related=crm_team_id.assignment_enabled)
- `assignment_domain` Char “Assignment Domain”
- `assignment_optout` Boolean “Skip auto assignment”
- `assignment_max` Integer “Average Leads Capacity (on 30 days)”
- `lead_month_count` Integer “Leads (30 days)” (compute=_compute_lead_month_count)

Extension points: `_get_assignment_quota`, `_get_lead_month_domain`

## `digest.digest` (extends)

- `kpi_crm_lead_created` Boolean “New Leads”
- `kpi_crm_lead_created_value` Integer (compute=_compute_kpi_crm_lead_created_value)
- `kpi_crm_opportunities_won` Boolean “Opportunities Won”
- `kpi_crm_opportunities_won_value` Integer (compute=_compute_kpi_crm_opportunities_won_value)

## `ir.config_parameter` (extends)


Public methods: `create`, `unlink`, `write`

## `mail.activity` (extends)


Public methods: `action_create_calendar_event`

## `res.config.settings` (extends)

- `group_use_lead` Boolean “Leads”
- `group_use_recurring_revenues` Boolean “Recurring Revenues”
- `is_membership_multi` Boolean “Multi Teams”
- `crm_use_auto_assignment` Boolean “Rule-Based Assignment”
- `crm_auto_assignment_action` Selection “Auto Assignment Action” (store, compute=_compute_crm_auto_assignment_data)
- `crm_auto_assignment_interval_type` Selection “Auto Assignment Interval Unit” (store, compute=_compute_crm_auto_assignment_data)
- `crm_auto_assignment_interval_number` Integer “Repeat every” (store, compute=_compute_crm_auto_assignment_data)
- `crm_auto_assignment_run_datetime` Datetime “Auto Assignment Next Execution Date” (store, compute=_compute_crm_auto_assignment_data)
- `module_crm_iap_mine` Boolean “Generate new leads based on their country, industries, size, etc.”
- `module_crm_iap_enrich` Boolean “Enrich your leads automatically with company data based on their email address.”
- `module_website_crm_iap_reveal` Boolean “Create Leads/Opportunities from your website's traffic”
- `lead_enrich_auto` Selection “Enrich lead automatically”
- `lead_mining_in_pipeline` Boolean “Create a lead mining request directly from the opportunity pipeline.”
- `predictive_lead_scoring_start_date` Date “Lead Scoring Starting Date” (compute=_compute_pls_start_date)
- `predictive_lead_scoring_start_date_str` Char “Lead Scoring Starting Date in String”
- `predictive_lead_scoring_fields` Many2many → `crm.lead.scoring.frequency.field` “Lead Scoring Frequency Fields” (compute=_compute_pls_fields)
- `predictive_lead_scoring_fields_str` Char “Lead Scoring Frequency Fields in String”
- `predictive_lead_scoring_field_labels` Char (compute=_compute_predictive_lead_scoring_field_labels)

Public methods: `action_crm_assign_leads`, `set_values`

Extension points: `_get_crm_auto_assignmment_run_datetime`

## `res.partner` (extends)

- `team_id` Many2one → `crm.team` “Sales Team” (store, compute=_compute_team_id)
- `opportunity_ids` One2many → `crm.lead` “Opportunities”
- `opportunity_count` Integer “Opportunity” (compute=_compute_opportunity_count)

Public methods: `action_view_opportunity`, `default_get`

## `res.users` (extends)

- `target_sales_won` Integer “Won in Opportunities Target”
- `target_sales_done` Integer “Activities Done Target”

## `utm.campaign` (extends)

- `use_leads` Boolean “Use Leads” (compute=_compute_use_leads)
- `crm_lead_count` Integer “Leads/Opportunities count” (compute=_compute_crm_lead_count)

Public methods: `action_redirect_to_leads_opportunities`

## `crm.lead` (extends)


## `crm.activity.report` (defines)

CRM Activity Analysis

- `date` Datetime “Completion Date” (readonly)
- `lead_create_date` Datetime “Creation Date” (readonly)
- `date_conversion` Datetime “Conversion Date” (readonly)
- `date_deadline` Date “Expected Closing” (readonly)
- `date_closed` Datetime “Closed Date” (readonly)
- `author_id` Many2one → `res.partner` (readonly)
- `user_id` Many2one → `res.users` (readonly)
- `team_id` Many2one → `crm.team` (readonly)
- `lead_id` Many2one → `crm.lead` (readonly)
- `body` Html “Activity Description” (readonly)
- `subtype_id` Many2one → `mail.message.subtype` (readonly)
- `mail_activity_type_id` Many2one → `mail.activity.type` (readonly)
- `country_id` Many2one → `res.country` (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `stage_id` Many2one → `crm.stage` (readonly)
- `partner_id` Many2one → `res.partner` (readonly)
- `lead_type` Selection “Type”
- `active` Boolean “Active” (readonly)

Public methods: `init`

## `crm.lead.lost` (defines)

Get Lost Reason

- `lost_reason_id` Many2one → `crm.lost.reason`
- `lost_feedback` Html “Closing Note”

Public methods: `action_lost_reason_apply`

## `crm.lead.pls.update` (defines)

Update the probabilities

- `pls_start_date` Date (required)
- `pls_fields` Many2many → `crm.lead.scoring.frequency.field`

Public methods: `action_update_crm_lead_probabilities`

Extension points: `_get_default_pls_fields`, `_get_default_pls_start_date`

## `crm.lead2opportunity.partner` (defines)

Convert Lead to Opportunity (not in mass)

- `name` Selection (store, compute=_compute_name)
- `action` Selection “Related Customer” (store, compute=_compute_action)
- `lead_id` Many2one → `crm.lead` (required)
- `duplicated_lead_ids` Many2many → `crm.lead` “Opportunities” (store, compute=_compute_duplicated_lead_ids)
- `partner_id` Many2one → `res.partner` (store, compute=_compute_partner_id)
- `user_id` Many2one → `res.users` (store, compute=_compute_user_id)
- `team_id` Many2one → `crm.team` (store, compute=_compute_team_id)
- `force_assignment` Boolean “Force assignment”

Public methods: `action_apply`, `default_get`

Extension points: `_action_convert`, `_action_merge`

## `crm.lead2opportunity.partner.mass` (defines)

Convert Lead to Opportunity (in mass)

Inherits: `crm.lead2opportunity.partner`

- `lead_id` Many2one
- `lead_tomerge_ids` Many2many → `crm.lead` “Active Leads”
- `user_ids` Many2many → `res.users` “Salespersons”
- `deduplicate` Boolean “Apply deduplication”
- `action` Selection “Related Customer”
- `force_assignment` Boolean

Public methods: `action_mass_convert`

## `crm.merge.opportunity` (defines)

Merge Opportunities

- `opportunity_ids` Many2many → `crm.lead` “Leads/Opportunities”
- `user_id` Many2one → `res.users`
- `team_id` Many2one → `crm.team` (store, compute=_compute_team_id)

Public methods: `action_merge`, `default_get`
