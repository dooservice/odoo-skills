# hr_recruitment — Recruitment

Depends on: hr, calendar, utm, attachment_indexation, web_tour, digest.

## `calendar.event` (extends)

- `applicant_id` Many2one → `hr.applicant` “Applicant”

Public methods: `create`, `default_get`

## `digest.digest` (extends)

- `kpi_hr_recruitment_new_colleagues` Boolean “New Employees”
- `kpi_hr_recruitment_new_colleagues_value` Integer (compute=_compute_kpi_hr_recruitment_new_colleagues_value)

## `hr.applicant` (defines)

Applicant

Inherits: `mail.thread.cc`, `mail.thread.main.attachment`, `mail.thread.blacklist`, `mail.thread.phone`, `mail.activity.mixin`, `utm.mixin`, `mail.tracking.duration.mixin`

- `sequence` Integer “Sequence” (index)
- `active` Boolean “Active” (index)
- `partner_id` Many2one → `res.partner`
- `partner_name` Char “Applicant's Name”
- `email_from` Char “Email” (store, compute=_compute_partner_phone_email)
- `email_normalized` Char
- `partner_phone` Char “Phone” (store, compute=_compute_partner_phone_email)
- `partner_phone_sanitized` Char “Sanitized Phone Number” (store, compute=_compute_partner_phone_sanitized)
- `linkedin_profile` Char “LinkedIn Profile”
- `type_id` Many2one → `hr.recruitment.degree`
- `availability` Date “Availability”
- `color` Integer “Color Index”
- `employee_id` Many2one → `hr.employee` “Employee”
- `emp_is_active` Boolean “Employee Active” (related=employee_id.active)
- `employee_name` Char “Employee Name” (related=employee_id.name)
- `probability` Float “Probability”
- `create_date` Datetime “Applied on” (readonly)
- `stage_id` Many2one → `hr.recruitment.stage` (store, index, compute=_compute_stage)
- `last_stage_id` Many2one → `hr.recruitment.stage`
- `categ_ids` Many2many → `hr.applicant.category` “Tags”
- `company_id` Many2one → `res.company` (store, compute=_compute_company)
- `user_id` Many2one → `res.users` (store, compute=_compute_user)
- `date_closed` Datetime “Hire Date” (store, compute=_compute_date_closed)
- `date_open` Datetime “Assigned” (readonly)
- `date_last_stage_update` Datetime “Last Stage Update” (index)
- `priority` Selection
- `job_id` Many2one → `hr.job` (index)
- `salary_proposed_extra` Char “Proposed Salary Extra”
- `salary_expected_extra` Char “Expected Salary Extra”
- `salary_proposed` Float “Proposed”
- `salary_expected` Float “Expected”
- `department_id` Many2one → `hr.department` (store, compute=_compute_department)
- `day_open` Float “Days to Open” (compute=_compute_day)
- `day_close` Float “Days to Close” (compute=_compute_day)
- `delay_close` Float “Delay to Close” (readonly, store, compute=_compute_delay)
- `user_email` Char “User Email” (readonly, related=user_id.email)
- `attachment_number` Integer “Number of Attachments” (compute=_get_attachment_number)
- `attachment_ids` One2many → `ir.attachment` “Attachments”
- `kanban_state` Selection “Kanban State” (required)
- `legend_blocked` Char “Kanban Blocked” (related=stage_id.legend_blocked)
- `legend_done` Char “Kanban Valid” (related=stage_id.legend_done)
- `legend_waiting` Char “Kanban Waiting” (related=stage_id.legend_waiting)
- `legend_normal` Char “Kanban Ongoing” (related=stage_id.legend_normal)
- `refuse_reason_id` Many2one → `hr.applicant.refuse.reason` “Refuse Reason”
- `meeting_ids` One2many → `calendar.event`
- `meeting_display_text` Char (compute=_compute_meeting_display)
- `meeting_display_date` Date (compute=_compute_meeting_display)
- `campaign_id` Many2one
- `medium_id` Many2one
- `source_id` Many2one
- `interviewer_ids` Many2many → `res.users` “Interviewers” (index)
- `application_status` Selection (compute=_compute_application_status)
- `application_count` Integer (compute=_compute_application_count)
- `applicant_properties` Properties “Properties”
- `applicant_notes` Html
- `refuse_date` Datetime “Refuse Date”
- `talent_pool_ids` Many2many → `hr.talent.pool` “Talent Pools”
- `pool_applicant_id` Many2one → `hr.applicant`
- `is_pool_applicant` Boolean (compute=_compute_is_pool)
- `is_applicant_in_pool` Boolean (compute=_compute_is_applicant_in_pool)
- `talent_pool_count` Integer (compute=_compute_talent_pool_count)

Public methods: `action_archive`, `action_create_meeting`, `action_job_add_applicants`, `action_open_applications`, `action_open_attachments`, `action_open_employee`, `action_send_email`, `action_talent_pool_add_applicants`, `action_talent_pool_stat_button`, `action_unarchive`, `archive_applicant`, `copy`, `copy_data`, `create`, `create_employee_from_applicant`, `get_empty_list_help`, `get_view`, `link_applicant_to_talent`, `message_new`, `reset_applicant`, `write`

Extension points: `_check_interviewer_access`, `_check_talent_pool_required`, `_get_attachment_number`, `_get_customer_information`, `_get_duration_from_tracking`, `_get_employee_create_vals`, `_get_rotting_depends_fields`, `_get_rotting_domain`, `_get_similar_applicants_domain`

## `hr.applicant.category` (defines)

Category of applicant

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”

Extension points: `_get_default_color`

## `hr.applicant.refuse.reason` (defines)

Refuse Reason of Applicant

- `sequence` Integer
- `name` Char “Description” (required)
- `template_id` Many2one → `mail.template` “Email Template”
- `active` Boolean “Active”

## `hr.department` (extends)

- `new_applicant_count` Integer “New Applicant” (compute=_compute_new_applicant_count)
- `new_hired_employee` Integer “New Hired Employee” (compute=_compute_recruitment_stats)
- `expected_employee` Integer “Expected Employee” (compute=_compute_recruitment_stats)

## `hr.employee` (extends)

- `applicant_ids` One2many → `hr.applicant`

Public methods: `create`

Extension points: `_get_partner_count_depends`, `_get_related_partners`

## `hr.job` (extends)

Inherits: `mail.alias.mixin`, `mail.activity.mixin`

- `expected_employees` Integer
- `no_of_employee` Integer
- `requirements` Text
- `user_id` Many2one
- `address_id` Many2one → `res.partner`
- `application_ids` One2many → `hr.applicant`
- `application_count` Integer “Application Count” (compute=_compute_application_count)
- `open_application_count` Integer “Open Application Count” (compute=_compute_open_application_count)
- `all_application_count` Integer “All Application Count” (compute=_compute_all_application_count)
- `new_application_count` Integer “New Application” (compute=_compute_new_application_count)
- `old_application_count` Integer “Old Application” (compute=_compute_old_application_count)
- `applicant_hired` Integer “Applicants Hired” (compute=_compute_applicant_hired)
- `manager_id` Many2one → `hr.employee` “Department Manager” (readonly, store, related=department_id.manager_id)
- `document_ids` One2many → `ir.attachment` “Documents” (readonly, compute=_compute_document_ids)
- `documents_count` Integer “Document Count” (compute=_compute_document_ids)
- `employee_count` Integer (compute=_compute_employee_count)
- `alias_id` Many2one
- `color` Integer “Color Index”
- `is_favorite` Boolean (compute=_compute_is_favorite)
- `favorite_user_ids` Many2many → `res.users`
- `interviewer_ids` Many2many → `res.users` “Interviewers”
- `extended_interviewer_ids` Many2many → `res.users` (store, compute=_compute_extended_interviewer_ids)
- `industry_id` Many2one → `res.partner.industry`
- `expected_degree` Many2one → `hr.recruitment.degree`
- `activity_count` Integer (compute=_compute_activities)
- `job_properties` Properties “Properties”
- `applicant_properties_definition` PropertiesDefinition “Applicant Properties”
- `no_of_hired_employee` Integer “Hired” (store, compute=_compute_no_of_hired_employee)
- `job_source_ids` One2many → `hr.recruitment.source`

Public methods: `action_open_activities`, `action_open_attachments`, `action_open_employees`, `create`, `write`

Extension points: `_action_load_recruitment_scenario`, `_get_attachments_domain`, `_get_default_favorite_user_ids`, `_get_first_stage`

## `hr.job.platform` (defines)

Job Platforms

- `name` Char (required)
- `email` Char (required)
- `regex` Char

Public methods: `create`, `write`

## `hr.recruitment.degree` (defines)

Applicant Degree

- `name` Char “Degree Name” (required)
- `score` Float “Score” (required)
- `sequence` Integer “Sequence”

## `hr.recruitment.source` (defines)

Source of Applicants

Inherits: `utm.source.mixin`

- `email` Char “Email” (readonly, related=alias_id.display_name)
- `has_domain` Char (compute=_compute_has_domain)
- `job_id` Many2one → `hr.job` (index)
- `alias_id` Many2one → `mail.alias`
- `medium_id` Many2one → `utm.medium`
- `campaign_id` Many2one → `utm.campaign`

Public methods: `create_alias`, `create_and_get_alias`, `unlink`

## `hr.recruitment.stage` (defines)

Recruitment Stages

- `name` Char “Stage Name” (required)
- `sequence` Integer “Sequence”
- `job_ids` Many2many → `hr.job` “Job Specific”
- `requirements` Text “Requirements”
- `template_id` Many2one → `mail.template`
- `fold` Boolean “Folded in Kanban”
- `hired_stage` Boolean “Hired Stage”
- `rotting_threshold_days` Integer “Days to rot”
- `legend_blocked` Char “Red Kanban Label” (required)
- `legend_waiting` Char “Orange Kanban Label” (required)
- `legend_done` Char “Green Kanban Label” (required)
- `legend_normal` Char “Grey Kanban Label” (required)
- `is_warning_visible` Boolean (compute=_compute_is_warning_visible)

Public methods: `default_get`

## `hr.talent.pool` (defines)

Talent Pool

Inherits: `mail.thread`

- `active` Boolean
- `name` Char “Title” (required)
- `company_id` Many2one → `res.company` “Company”
- `pool_manager` Many2one → `res.users` (store)
- `talent_ids` Many2many → `hr.applicant` “Talent”
- `no_of_talents` Integer “# Talents” (compute=_compute_talent_count)
- `description` Html “Talent Pool Description”
- `color` Integer “Color”
- `categ_ids` Many2many → `hr.applicant.category` “Tags” (store)

Public methods: `action_talent_pool_add_talents`

Extension points: `_get_default_color`

## `ir.attachment` (extends)


Public methods: `init`

## `ir.ui.menu` (extends)


## `mail.activity.plan` (extends)


## `res.company` (extends)

- `job_properties_definition` PropertiesDefinition “Job Properties”

## `res.config.settings` (extends)

- `module_website_hr_recruitment` Boolean “Online Posting”
- `module_hr_recruitment_survey` Boolean “Interview Forms”
- `module_hr_recruitment_extract` Boolean “Send CV to OCR to fill applications”

## `res.partner` (extends)

- `applicant_ids` One2many → `hr.applicant` “Applicants”

## `res.users` (extends)


Extension points: `_create_recruitment_interviewers`

## `utm.campaign` (extends)


## `utm.source` (extends)


## `applicant.get.refuse.reason` (defines)

Get Refuse Reason

Inherits: `mail.composer.mixin`

- `refuse_reason_id` Many2one → `hr.applicant.refuse.reason` (required)
- `applicant_ids` Many2many → `hr.applicant`
- `send_mail` Boolean “Send Email” (store, compute=_compute_send_mail)
- `template_id` Many2one → `mail.template` “Email Template” (store, compute=_compute_template_id)
- `applicant_without_email` Text “Applicant(s) not having email” (compute=_compute_applicant_without_email)
- `duplicates` Boolean “Refuse Duplicate Applications”
- `duplicates_count` Integer “Duplicates Count” (compute=_compute_duplicate_applicant_ids_domain)
- `duplicate_applicant_ids` Many2many → `hr.applicant` “Duplicate Applications” (store, compute=_compute_duplicate_applicant_ids)
- `duplicate_applicant_ids_domain` Binary (compute=_compute_duplicate_applicant_ids_domain)
- `attachment_ids` Many2many → `ir.attachment` “Attachments” (store, compute=_compute_from_template_id)
- `scheduled_date` Char “Scheduled Date” (store, compute=_compute_from_template_id)

Public methods: `action_refuse_reason_apply`

Extension points: `_get_related_original_applicants`, `_prepare_mail_values`, `_prepare_send_refusal_mails`

## `applicant.send.mail` (defines)

Send mails to applicants

Inherits: `mail.composer.mixin`

- `applicant_ids` Many2many → `hr.applicant` “Applications” (required)
- `author_id` Many2one → `res.partner` (required)
- `attachment_ids` Many2many → `ir.attachment` “Attachments” (store)

Public methods: `action_send`

## `job.add.applicants` (defines)

Add applicants to a job

- `applicant_ids` Many2many → `hr.applicant` “Applications” (required)
- `job_ids` Many2many → `hr.job` “Job Positions” (required)

Public methods: `action_add_applicants_to_job`

## `mail.activity.schedule` (extends)


## `talent.pool.add.applicants` (defines)

Add applicants to talent pool

- `applicant_ids` Many2many → `hr.applicant` “Applicants” (required)
- `talent_pool_ids` Many2many → `hr.talent.pool` “Talent Pool”
- `categ_ids` Many2many → `hr.applicant.category` “Tags”

Public methods: `action_add_applicants_to_pool`
