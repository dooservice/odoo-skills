# hr_recruitment — Recruitment

Depends on: hr, calendar, utm, attachment_indexation, web_tour, digest.

## `calendar.event` (extends)

- `applicant_id` Many2one → `hr.applicant` “Applicant”

Public methods: `default_get`

## `digest.digest` (extends)

- `kpi_hr_recruitment_new_colleagues` Boolean “New Employees”
- `kpi_hr_recruitment_new_colleagues_value` Integer (compute=_compute_kpi_hr_recruitment_new_colleagues_value)

## `hr.department` (extends)

- `new_applicant_count` Integer “New Applicant” (compute=_compute_new_applicant_count)
- `new_hired_employee` Integer “New Hired Employee” (compute=_compute_recruitment_stats)
- `expected_employee` Integer “Expected Employee” (compute=_compute_recruitment_stats)

## `hr.employee` (extends)

- `newly_hired_employee` Boolean “Newly hired employee” (compute=_compute_newly_hired_employee)
- `applicant_id` One2many → `hr.applicant`

Public methods: `create`

## `hr.job` (extends)

Inherits: `mail.alias.mixin`

- `address_id` Many2one → `res.partner`
- `application_ids` One2many → `hr.applicant`
- `application_count` Integer “Application Count” (compute=_compute_application_count)
- `all_application_count` Integer “All Application Count” (compute=_compute_all_application_count)
- `new_application_count` Integer “New Application” (compute=_compute_new_application_count)
- `old_application_count` Integer “Old Application” (compute=_compute_old_application_count)
- `applicant_hired` Integer “Applicants Hired” (compute=_compute_applicant_hired)
- `manager_id` Many2one → `hr.employee` “Department Manager” (readonly, store, related=department_id.manager_id)
- `user_id` Many2one → `res.users`
- `hr_responsible_id` Many2one → `res.users`
- `document_ids` One2many → `ir.attachment` “Documents” (readonly, compute=_compute_document_ids)
- `documents_count` Integer “Document Count” (compute=_compute_document_ids)
- `alias_id` Many2one → `mail.alias` (required)
- `color` Integer “Color Index”
- `is_favorite` Boolean (compute=_compute_is_favorite)
- `favorite_user_ids` Many2many → `res.users`
- `interviewer_ids` Many2many → `res.users` “Interviewers”
- `extended_interviewer_ids` Many2many → `res.users` (store, compute=_compute_extended_interviewer_ids)
- `activities_overdue` Integer (compute=_compute_activities)
- `activities_today` Integer (compute=_compute_activities)

Public methods: `action_open_activities`, `action_open_attachments`, `action_open_late_activities`, `action_open_today_activities`, `close_dialog`, `create`, `edit_dialog`, `write`

Extension points: `_get_default_favorite_user_ids`, `_get_first_stage`

## `hr.recruitment.source` (defines)

Source of Applicants

Inherits: `utm.source.mixin`

- `email` Char “Email” (readonly, related=alias_id.display_name)
- `has_domain` Char (compute=_compute_has_domain)
- `job_id` Many2one → `hr.job`
- `alias_id` Many2one → `mail.alias`
- `medium_id` Many2one → `utm.medium`

Public methods: `create_alias`

Extension points: `_get_view`

## `hr.recruitment.stage` (defines)

Recruitment Stages

- `name` Char “Stage Name” (required)
- `sequence` Integer “Sequence”
- `job_ids` Many2many → `hr.job` “Job Specific”
- `requirements` Text “Requirements”
- `template_id` Many2one → `mail.template`
- `fold` Boolean “Folded in Kanban”
- `hired_stage` Boolean “Hired Stage”
- `legend_blocked` Char “Red Kanban Label” (required)
- `legend_done` Char “Green Kanban Label” (required)
- `legend_normal` Char “Grey Kanban Label” (required)
- `is_warning_visible` Boolean (compute=_compute_is_warning_visible)

Public methods: `default_get`

## `hr.recruitment.degree` (defines)

Applicant Degree

- `name` Char “Degree Name” (required)
- `sequence` Integer “Sequence”

## `hr.applicant` (defines)

Applicant

Inherits: `mail.thread.cc`, `mail.activity.mixin`, `utm.mixin`

- `name` Char “Subject / Application” (required)
- `active` Boolean “Active”
- `description` Html “Description”
- `email_from` Char “Email” (store, compute=_compute_partner_phone_email)
- `probability` Float “Probability”
- `partner_id` Many2one → `res.partner`
- `create_date` Datetime “Creation Date” (readonly)
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
- `salary_proposed` Float “Proposed Salary”
- `salary_expected` Float “Expected Salary”
- `availability` Date “Availability”
- `partner_name` Char “Applicant's Name”
- `partner_phone` Char “Phone” (store, compute=_compute_partner_phone_email)
- `partner_mobile` Char “Mobile” (store, compute=_compute_partner_phone_email)
- `type_id` Many2one → `hr.recruitment.degree`
- `department_id` Many2one → `hr.department` (store, compute=_compute_department)
- `day_open` Float “Days to Open” (compute=_compute_day)
- `day_close` Float “Days to Close” (compute=_compute_day)
- `delay_close` Float “Delay to Close” (readonly, store, compute=_compute_day)
- `color` Integer “Color Index”
- `emp_id` Many2one → `hr.employee` “Employee”
- `user_email` Char “User Email” (readonly, related=user_id.email)
- `attachment_number` Integer “Number of Attachments” (compute=_get_attachment_number)
- `employee_name` Char “Employee Name” (related=emp_id.name)
- `attachment_ids` One2many → `ir.attachment` “Attachments”
- `kanban_state` Selection “Kanban State” (required)
- `legend_blocked` Char “Kanban Blocked” (related=stage_id.legend_blocked)
- `legend_done` Char “Kanban Valid” (related=stage_id.legend_done)
- `legend_normal` Char “Kanban Ongoing” (related=stage_id.legend_normal)
- `application_count` Integer (compute=_compute_application_count)
- `refuse_reason_id` Many2one → `hr.applicant.refuse.reason` “Refuse Reason”
- `meeting_ids` One2many → `calendar.event`
- `meeting_display_text` Char (compute=_compute_meeting_display)
- `meeting_display_date` Date (compute=_compute_meeting_display)
- `campaign_id` Many2one
- `medium_id` Many2one
- `source_id` Many2one
- `interviewer_ids` Many2many → `res.users` “Interviewers” (index)
- `linkedin_profile` Char “LinkedIn Profile”
- `application_status` Selection (compute=_compute_application_status)

Public methods: `action_applications_email`, `action_makeMeeting`, `action_open_attachments`, `action_open_employee`, `action_send_email`, `archive_applicant`, `create`, `create_employee_from_applicant`, `get_empty_list_help`, `get_view`, `message_new`, `name_get`, `reset_applicant`, `toggle_active`, `write`

Extension points: `_check_interviewer_access`, `_get_attachment_number`

## `hr.applicant.category` (defines)

Category of applicant

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”

Extension points: `_get_default_color`

## `hr.applicant.refuse.reason` (defines)

Refuse Reason of Applicant

- `name` Char “Description” (required)
- `template_id` Many2one → `mail.template` “Email Template”
- `active` Boolean “Active”

## `ir.ui.menu` (extends)


## `res.config.settings` (extends)

- `module_website_hr_recruitment` Boolean “Online Posting”
- `module_hr_recruitment_survey` Boolean “Interview Forms”
- `group_applicant_cv_display` Boolean
- `module_hr_recruitment_extract` Boolean “Send CV to OCR to fill applications”

## `res.users` (extends)


Extension points: `_create_recruitment_interviewers`

## `utm.campaign` (extends)


## `utm.source` (extends)


## `applicant.get.refuse.reason` (defines)

Get Refuse Reason

- `refuse_reason_id` Many2one → `hr.applicant.refuse.reason` (required)
- `applicant_ids` Many2many → `hr.applicant`
- `send_mail` Boolean “Send Email” (store, compute=_compute_send_mail)
- `template_id` Many2one → `mail.template` “Email Template” (store, compute=_compute_send_mail)
- `applicant_without_email` Text “Applicant(s) not having email” (compute=_compute_applicant_without_email)

Public methods: `action_refuse_reason_apply`

## `applicant.send.mail` (defines)

Send mails to applicants

Inherits: `mail.composer.mixin`

- `applicant_ids` Many2many → `hr.applicant` “Applications” (required)
- `author_id` Many2one → `res.partner` (required)

Public methods: `action_send`
