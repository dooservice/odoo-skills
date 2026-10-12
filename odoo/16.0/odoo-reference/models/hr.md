# hr — Employees

Depends on: base_setup, mail, resource, web.

## `hr.contract.type` (defines)

Contract Type

- `name` Char (required)
- `sequence` Integer

## `hr.department` (defines)

Department

Inherits: `mail.thread`

- `name` Char “Department Name” (required)
- `complete_name` Char “Complete Name” (store, compute=_compute_complete_name)
- `active` Boolean “Active”
- `company_id` Many2one → `res.company` “Company” (index)
- `parent_id` Many2one → `hr.department` “Parent Department” (index)
- `child_ids` One2many → `hr.department` “Child Departments”
- `manager_id` Many2one → `hr.employee` “Manager”
- `member_ids` One2many → `hr.employee` “Members” (readonly)
- `total_employee` Integer “Total Employee” (compute=_compute_total_employee)
- `jobs_ids` One2many → `hr.job` “Jobs”
- `plan_ids` One2many → `hr.plan`
- `plans_count` Integer (compute=_compute_plan_count)
- `note` Text “Note”
- `color` Integer “Color Index”
- `parent_path` Char (index)
- `master_department_id` Many2one → `hr.department` (store, compute=_compute_master_department_id)

Public methods: `action_plan_from_department`, `create`, `get_children_department_ids`, `get_formview_action`, `name_create`, `name_get`, `write`

Extension points: `_check_parent_id`

## `hr.departure.reason` (defines)

Departure Reason

- `sequence` Integer “Sequence”
- `name` Char “Reason” (required)

Extension points: `_get_default_departure_reasons`

## `hr.employee` (defines)

Employee

Inherits: `hr.employee.base`, `mail.thread`, `mail.activity.mixin`, `resource.mixin`, `avatar.mixin`

- `name` Char “Employee Name” (store, related=resource_id.name)
- `user_id` Many2one → `res.users` (store, related=resource_id.user_id)
- `user_partner_id` Many2one “User's partner” (related=user_id.partner_id)
- `active` Boolean “Active” (store, related=resource_id.active)
- `company_id` Many2one → `res.company` (required)
- `company_country_id` Many2one → `res.country` (readonly, related=company_id.country_id)
- `company_country_code` Char (readonly, related=company_country_id.code)
- `address_home_id` Many2one → `res.partner`
- `is_address_home_a_company` Boolean “The employee address has a company linked” (compute=_compute_is_address_home_a_company)
- `private_email` Char “Private Email” (related=address_home_id.email)
- `lang` Selection “Lang” (related=address_home_id.lang)
- `country_id` Many2one → `res.country`
- `gender` Selection
- `marital` Selection “Marital Status”
- `spouse_complete_name` Char “Spouse Complete Name”
- `spouse_birthdate` Date “Spouse Birthdate”
- `children` Integer “Number of Dependent Children”
- `place_of_birth` Char “Place of Birth”
- `country_of_birth` Many2one → `res.country` “Country of Birth”
- `birthday` Date “Date of Birth”
- `ssnid` Char “SSN No”
- `sinid` Char “SIN No”
- `identification_id` Char “Identification No”
- `passport_id` Char “Passport No”
- `bank_account_id` Many2one → `res.partner.bank`
- `permit_no` Char “Work Permit No”
- `visa_no` Char “Visa No”
- `visa_expire` Date “Visa Expiration Date”
- `work_permit_expiration_date` Date “Work Permit Expiration Date”
- `has_work_permit` Binary “Work Permit”
- `work_permit_scheduled_activity` Boolean
- `work_permit_name` Char “work_permit_name” (compute=_compute_work_permit_name)
- `additional_note` Text “Additional Note”
- `certificate` Selection
- `study_field` Char “Field of Study”
- `study_school` Char “School”
- `emergency_contact` Char “Contact Name”
- `emergency_phone` Char “Contact Phone”
- `km_home_work` Integer “Home-Work Distance”
- `job_id` Many2one
- `phone` Char “Private Phone” (related=address_home_id.phone)
- `child_ids` One2many → `hr.employee` “Direct subordinates”
- `category_ids` Many2many → `hr.employee.category` “Tags”
- `notes` Text “Notes”
- `color` Integer “Color Index”
- `barcode` Char “Badge ID”
- `pin` Char “PIN”
- `departure_reason_id` Many2one → `hr.departure.reason` “Departure Reason”
- `departure_description` Html “Additional Information”
- `departure_date` Date “Departure Date”
- `message_main_attachment_id` Many2one
- `id_card` Binary “ID Card Copy”
- `driving_license` Binary “Driving License”
- `currency_id` Many2one → `res.currency` (readonly, related=company_id.currency_id)

Public methods: `action_create_user`, `create`, `generate_random_barcode`, `get_formview_action`, `get_formview_id`, `get_import_templates`, `get_view`, `get_views`, `message_post`, `name_get`, `read`, `toggle_active`, `unlink`, `write`

Extension points: `_get_employee_m2o_to_empty_on_archived_employees`, `_get_expected_attendances`, `_get_tz`, `_get_tz_batch`, `_get_unusual_days`, `_get_user_m2o_to_empty_on_archived_employees`, `_post_author`, `_prepare_resource_values`

## `hr.employee.base` (defines)

Basic Employee

- `name` Char
- `active` Boolean “Active”
- `color` Integer “Color Index”
- `department_id` Many2one → `hr.department`
- `member_of_department` Boolean “Member of department” (compute=_compute_part_of_department)
- `job_id` Many2one → `hr.job`
- `job_title` Char “Job Title” (store, compute=_compute_job_title)
- `company_id` Many2one → `res.company`
- `address_id` Many2one → `res.partner` (store, compute=_compute_address_id)
- `work_phone` Char “Work Phone” (store, compute=_compute_phones)
- `mobile_phone` Char “Work Mobile” (store, compute=_compute_work_contact_details)
- `work_email` Char “Work Email” (store, compute=_compute_work_contact_details)
- `work_contact_id` Many2one → `res.partner`
- `related_contact_ids` Many2many → `res.partner` “Related Contacts” (compute=_compute_related_contacts)
- `related_contacts_count` Integer “Number of related contacts” (compute=_compute_related_contacts_count)
- `work_location_id` Many2one → `hr.work.location` (store, compute=_compute_work_location_id)
- `user_id` Many2one → `res.users`
- `resource_id` Many2one → `resource.resource`
- `resource_calendar_id` Many2one → `resource.calendar`
- `parent_id` Many2one → `hr.employee` (store, compute=_compute_parent_id)
- `coach_id` Many2one → `hr.employee` (store, compute=_compute_coach)
- `tz` Selection “Timezone” (related=resource_id.tz)
- `hr_presence_state` Selection (compute=_compute_presence_state)
- `last_activity` Date (compute=_compute_last_activity)
- `last_activity_time` Char (compute=_compute_last_activity)
- `hr_icon_display` Selection (compute=_compute_presence_icon)
- `show_hr_icon_display` Boolean (compute=_compute_presence_icon)
- `employee_type` Selection “Employee Type” (required)

Public methods: `action_related_contacts`

Extension points: `_get_employee_working_now`, `_get_valid_employee_for_user`

## `hr.employee.category` (defines)

Employee Category

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”
- `employee_ids` Many2many → `hr.employee` “Employees”

Extension points: `_get_default_color`

## `hr.employee.public` (defines)

Public Employee

Inherits: `hr.employee.base`

- `create_date` Datetime (readonly)
- `name` Char (readonly)
- `active` Boolean (readonly)
- `department_id` Many2one (readonly)
- `job_id` Many2one (readonly)
- `job_title` Char (readonly)
- `company_id` Many2one (readonly)
- `address_id` Many2one (readonly)
- `mobile_phone` Char (readonly)
- `work_phone` Char (readonly)
- `work_email` Char (readonly)
- `work_contact_id` Many2one (readonly)
- `related_contact_ids` Many2many (readonly)
- `work_location_id` Many2one (readonly)
- `user_id` Many2one (readonly)
- `resource_id` Many2one (readonly)
- `resource_calendar_id` Many2one (readonly)
- `tz` Selection (readonly)
- `color` Integer (readonly)
- `employee_type` Selection (readonly)
- `employee_id` Many2one → `hr.employee` (compute=_compute_employee_id)
- `child_ids` One2many → `hr.employee.public` “Direct subordinates” (readonly)
- `image_1920` Image “Image” (related=employee_id.image_1920)
- `image_1024` Image “Image 1024” (related=employee_id.image_1024)
- `image_512` Image “Image 512” (related=employee_id.image_512)
- `image_256` Image “Image 256” (related=employee_id.image_256)
- `image_128` Image “Image 128” (related=employee_id.image_128)
- `avatar_1920` Image “Avatar” (related=employee_id.avatar_1920)
- `avatar_1024` Image “Avatar 1024” (related=employee_id.avatar_1024)
- `avatar_512` Image “Avatar 512” (related=employee_id.avatar_512)
- `avatar_256` Image “Avatar 256” (related=employee_id.avatar_256)
- `avatar_128` Image “Avatar 128” (related=employee_id.avatar_128)
- `parent_id` Many2one → `hr.employee.public` (readonly)
- `coach_id` Many2one → `hr.employee.public` (readonly)
- `user_partner_id` Many2one “User's partner” (related=user_id.partner_id)

Public methods: `init`

Extension points: `_get_fields`

## `hr.job` (defines)

Job Position

Inherits: `mail.thread`

- `active` Boolean
- `name` Char “Job Position” (required)
- `sequence` Integer
- `expected_employees` Integer “Total Forecasted Employees” (store, compute=_compute_employees)
- `no_of_employee` Integer “Current Number of Employees” (store, compute=_compute_employees)
- `no_of_recruitment` Integer “Target”
- `no_of_hired_employee` Integer “Hired Employees”
- `employee_ids` One2many → `hr.employee` “Employees”
- `description` Html “Job Description”
- `requirements` Text “Requirements”
- `department_id` Many2one → `hr.department` “Department”
- `company_id` Many2one → `res.company` “Company”
- `contract_type_id` Many2one → `hr.contract.type` “Employment Type”

Public methods: `copy`, `create`, `write`

## `hr.plan` (defines)

plan

- `name` Char “Name” (required)
- `company_id` Many2one → `res.company`
- `department_id` Many2one → `hr.department`
- `plan_activity_type_ids` One2many → `hr.plan.activity.type` “Activities”
- `active` Boolean
- `steps_count` Integer (compute=_compute_steps_count)

## `hr.plan.activity.type` (defines)

Plan activity type

- `company_id` Many2one → `res.company`
- `activity_type_id` Many2one → `mail.activity.type`
- `summary` Char “Summary” (store, compute=_compute_default_summary)
- `responsible` Selection “Responsible” (required)
- `responsible_id` Many2one → `res.users`
- `plan_id` Many2one → `hr.plan`
- `note` Html “Note”

Public methods: `get_responsible_id`

## `hr.work.location` (defines)

Work Location

- `active` Boolean
- `name` Char “Work Location” (required)
- `company_id` Many2one → `res.company` (required)
- `address_id` Many2one → `res.partner` “Work Address” (required)
- `location_number` Char

## `ir.ui.menu` (extends)


## `mail.alias` (extends)

- `alias_contact` Selection

Extension points: `_get_alias_contact_description`

## `mail.channel` (extends)

- `subscription_department_ids` Many2many → `hr.department` “HR Departments”

Public methods: `write`

## `base` (extends)


## `res.company` (extends)

- `hr_presence_control_email_amount` Integer “# emails to send”
- `hr_presence_control_ip_list` Char “Valid IP addresses”

## `res.config.settings` (extends)

- `resource_calendar_id` Many2one → `resource.calendar` (related=company_id.resource_calendar_id)
- `module_hr_presence` Boolean “Advanced Presence Control”
- `module_hr_skills` Boolean “Skills Management”
- `module_hr_homeworking` Boolean “Homeworking”
- `hr_presence_control_login` Boolean “Based on user status in system”
- `hr_presence_control_email` Boolean “Based on number of emails sent”
- `hr_presence_control_ip` Boolean “Based on IP Address”
- `module_hr_attendance` Boolean “Based on attendances”
- `hr_presence_control_email_amount` Integer (related=company_id.hr_presence_control_email_amount)
- `hr_presence_control_ip_list` Char (related=company_id.hr_presence_control_ip_list)
- `hr_employee_self_edit` Boolean “Employee Editing”

Extension points: `_check_advanced_presence`

## `res.partner` (extends)

- `employee_ids` One2many → `hr.employee` “Employees”
- `employees_count` Integer (compute=_compute_employees_count)

Public methods: `action_open_employees`, `name_get`

## `res.partner.bank` (extends)


## `res.users` (extends)

- `employee_ids` One2many → `hr.employee` “Related employee”
- `employee_id` Many2one → `hr.employee` “Company employee” (compute=_compute_company_employee)
- `job_title` Char (related=employee_id.job_title)
- `work_phone` Char (related=employee_id.work_phone)
- `mobile_phone` Char (related=employee_id.mobile_phone)
- `employee_phone` Char (related=employee_id.phone)
- `work_email` Char (related=employee_id.work_email)
- `category_ids` Many2many “Employee Tags” (related=employee_id.category_ids)
- `department_id` Many2one (related=employee_id.department_id)
- `address_id` Many2one (related=employee_id.address_id)
- `work_location_id` Many2one (related=employee_id.work_location_id)
- `employee_parent_id` Many2one (related=employee_id.parent_id)
- `coach_id` Many2one (related=employee_id.coach_id)
- `address_home_id` Many2one (related=employee_id.address_home_id)
- `private_street` Char “Private Street” (related=address_home_id.street)
- `private_street2` Char “Private Street2” (related=address_home_id.street2)
- `private_city` Char “Private City” (related=address_home_id.city)
- `private_state_id` Many2one “Private State” (related=address_home_id.state_id)
- `private_zip` Char “Private Zip” (related=address_home_id.zip)
- `private_country_id` Many2one “Private Country” (related=address_home_id.country_id)
- `is_address_home_a_company` Boolean (related=employee_id.is_address_home_a_company)
- `private_email` Char “Private Email” (related=address_home_id.email)
- `private_lang` Selection “Employee Lang” (related=address_home_id.lang)
- `km_home_work` Integer (related=employee_id.km_home_work)
- `employee_bank_account_id` Many2one “Employee's Bank Account Number” (related=employee_id.bank_account_id)
- `employee_country_id` Many2one “Employee's Country” (related=employee_id.country_id)
- `identification_id` Char (related=employee_id.identification_id)
- `passport_id` Char (related=employee_id.passport_id)
- `gender` Selection (related=employee_id.gender)
- `birthday` Date (related=employee_id.birthday)
- `place_of_birth` Char (related=employee_id.place_of_birth)
- `country_of_birth` Many2one (related=employee_id.country_of_birth)
- `marital` Selection (related=employee_id.marital)
- `spouse_complete_name` Char (related=employee_id.spouse_complete_name)
- `spouse_birthdate` Date (related=employee_id.spouse_birthdate)
- `children` Integer (related=employee_id.children)
- `emergency_contact` Char (related=employee_id.emergency_contact)
- `emergency_phone` Char (related=employee_id.emergency_phone)
- `visa_no` Char (related=employee_id.visa_no)
- `permit_no` Char (related=employee_id.permit_no)
- `visa_expire` Date (related=employee_id.visa_expire)
- `additional_note` Text (related=employee_id.additional_note)
- `barcode` Char (related=employee_id.barcode)
- `pin` Char (related=employee_id.pin)
- `certificate` Selection (related=employee_id.certificate)
- `study_field` Char (related=employee_id.study_field)
- `study_school` Char (related=employee_id.study_school)
- `employee_count` Integer (compute=_compute_employee_count)
- `hr_presence_state` Selection (related=employee_id.hr_presence_state)
- `last_activity` Date (related=employee_id.last_activity)
- `last_activity_time` Char (related=employee_id.last_activity_time)
- `employee_type` Selection (related=employee_id.employee_type)
- `employee_resource_calendar_id` Many2one “Employee's Working Hours” (readonly, related=employee_id.resource_calendar_id)
- `create_employee` Boolean “Technical field, whether to create an employee”
- `create_employee_id` Many2one → `hr.employee` “Technical field, bind user to this employee on create”
- `can_edit` Boolean (compute=_compute_can_edit)
- `is_system` Boolean (compute=_compute_is_system)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`, `action_create_employee`, `action_get`, `create`, `get_view`, `get_views`, `write`

Extension points: `_get_employee_fields_to_sync`

## `resource.resource` (extends)

- `user_id` Many2one
- `employee_id` One2many → `hr.employee`

## `hr.department` (extends)


## `hr.job` (extends)


## `hr.work.location` (extends)


## `hr.employee.category` (extends)


## `hr.employee` (extends)


## `hr.departure.wizard` (defines)

Departure Wizard

- `departure_reason_id` Many2one → `hr.departure.reason` (required)
- `departure_description` Html “Additional Information”
- `departure_date` Date “Departure Date” (required)
- `employee_id` Many2one → `hr.employee` “Employee” (required)
- `archive_private_address` Boolean “Archive Private Address”

Public methods: `action_register_departure`

Extension points: `_get_default_departure_date`, `_get_employee_departure_date`

## `hr.plan.wizard` (defines)

Plan Wizard

- `plan_id` Many2one → `hr.plan`
- `department_id` Many2one → `hr.department` (compute=_compute_department_id)
- `employee_ids` Many2many → `hr.employee` “Employee” (required)
- `company_id` Many2one → `res.company` (required, compute=_compute_company_id)
- `warning` Html (compute=_compute_warning)

Public methods: `action_launch`

Extension points: `_check_employee_companies`, `_get_activities_to_schedule`, `_get_warnings`
