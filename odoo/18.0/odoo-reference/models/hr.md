# hr — Employees

Depends on: base_setup, digest, phone_validation, resource_mail, web.

## `discuss.channel` (extends)

- `subscription_department_ids` Many2many → `hr.department` “HR Departments”

Public methods: `write`

## `hr.contract.type` (defines)

Contract Type

- `name` Char (required)
- `code` Char (store, compute=_compute_code)
- `sequence` Integer
- `country_id` Many2one → `res.country`

## `hr.department` (defines)

Department

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Department Name” (required)
- `complete_name` Char “Complete Name” (store, compute=_compute_complete_name)
- `active` Boolean “Active”
- `company_id` Many2one → `res.company` “Company” (index)
- `parent_id` Many2one → `hr.department` “Parent Department” (index)
- `child_ids` One2many → `hr.department` “Child Departments”
- `manager_id` Many2one → `hr.employee` “Manager”
- `member_ids` One2many → `hr.employee` “Members” (readonly)
- `has_read_access` Boolean
- `total_employee` Integer “Total Employee” (compute=_compute_total_employee)
- `jobs_ids` One2many → `hr.job` “Jobs”
- `plan_ids` One2many → `mail.activity.plan`
- `plans_count` Integer (compute=_compute_plan_count)
- `note` Text “Note”
- `color` Integer “Color Index”
- `parent_path` Char (index)
- `master_department_id` Many2one → `hr.department` (store, compute=_compute_master_department_id)

Public methods: `action_employee_from_department`, `action_open_view_child_departments`, `action_plan_from_department`, `create`, `get_children_department_ids`, `get_department_hierarchy`, `get_formview_action`, `name_create`, `write`

Extension points: `_check_parent_id`

## `hr.departure.reason` (defines)

Departure Reason

- `sequence` Integer “Sequence”
- `name` Char “Reason” (required)
- `reason_code` Integer

Extension points: `_get_default_departure_reasons`

## `hr.employee` (defines)

Employee

Inherits: `hr.employee.base`, `mail.thread.main.attachment`, `mail.activity.mixin`, `resource.mixin`, `avatar.mixin`

- `name` Char “Employee Name” (store, related=resource_id.name)
- `user_id` Many2one → `res.users` (store, related=resource_id.user_id)
- `user_partner_id` Many2one “User's partner” (related=user_id.partner_id)
- `active` Boolean “Active” (store, related=resource_id.active)
- `resource_calendar_id` Many2one
- `department_id` Many2one
- `company_id` Many2one → `res.company` (required)
- `company_country_id` Many2one → `res.country` (readonly, related=company_id.country_id)
- `company_country_code` Char (readonly, related=company_country_id.code)
- `private_street` Char “Private Street”
- `private_street2` Char “Private Street2”
- `private_city` Char “Private City”
- `private_state_id` Many2one → `res.country.state` “Private State”
- `private_zip` Char “Private Zip”
- `private_country_id` Many2one → `res.country` “Private Country”
- `private_phone` Char “Private Phone”
- `private_email` Char “Private Email”
- `lang` Selection “Lang”
- `country_id` Many2one → `res.country`
- `gender` Selection
- `marital` Selection “Marital Status” (required)
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
- `distance_home_work` Integer “Home-Work Distance”
- `km_home_work` Integer “Home-Work Distance in Km” (store, compute=_compute_km_home_work)
- `distance_home_work_unit` Selection (required)
- `employee_type` Selection “Employee Type” (required)
- `job_id` Many2one
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
- `private_car_plate` Char
- `currency_id` Many2one → `res.currency` (readonly, related=company_id.currency_id)
- `related_partners_count` Integer (compute=_compute_related_partners_count)
- `employee_properties` Properties “Properties”
- `activity_ids` One2many
- `activity_state` Selection
- `activity_user_id` Many2one
- `activity_type_id` Many2one
- `activity_type_icon` Char
- `activity_date_deadline` Date
- `my_activity_date_deadline` Date
- `activity_summary` Char
- `activity_exception_decoration` Selection
- `activity_exception_icon` Char
- `message_is_follower` Boolean
- `message_follower_ids` One2many
- `message_partner_ids` Many2many
- `message_ids` One2many
- `has_message` Boolean
- `message_needaction` Boolean
- `message_needaction_counter` Integer
- `message_has_error` Boolean
- `message_has_error_counter` Integer
- `message_attachment_count` Integer

Public methods: `action_create_user`, `action_related_contacts`, `check_field_access_rights`, `create`, `fetch`, `filter_valid`, `generate_random_barcode`, `get_formview_action`, `get_formview_id`, `get_import_templates`, `get_view`, `get_views`, `search_fetch`, `toggle_active`, `unlink`, `write`

Extension points: `_check_private_fields`, `_check_ssnid`, `_get_age`, `_get_calendar_attendances`, `_get_employee_m2o_to_empty_on_archived_employees`, `_get_expected_attendances`, `_get_marital_status_selection`, `_get_partner_count_depends`, `_get_related_partners`, `_get_tz`, `_get_tz_batch`, `_get_unusual_days`, `_get_user_m2o_to_empty_on_archived_employees`, `_prepare_resource_values`

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
- `address_id` Many2one → `res.partner` “Work Address” (store, compute=_compute_address_id)
- `work_phone` Char “Work Phone” (store, compute=_compute_phones)
- `phone` Char (related=user_id.phone)
- `mobile_phone` Char “Work Mobile” (store, compute=_compute_work_contact_details)
- `work_email` Char “Work Email” (store, compute=_compute_work_contact_details)
- `email` Char (related=user_id.email)
- `work_contact_id` Many2one → `res.partner`
- `work_location_id` Many2one → `hr.work.location`
- `work_location_name` Char “Work Location Name” (compute=_compute_work_location_name_type)
- `work_location_type` Selection (compute=_compute_work_location_name_type)
- `user_id` Many2one → `res.users`
- `share` Boolean (related=user_id.share)
- `resource_id` Many2one → `resource.resource`
- `resource_calendar_id` Many2one → `resource.calendar`
- `is_flexible` Boolean (store, compute=_compute_is_flexible)
- `is_fully_flexible` Boolean (store, compute=_compute_is_flexible)
- `parent_id` Many2one → `hr.employee` (store, compute=_compute_parent_id)
- `coach_id` Many2one → `hr.employee` (store, compute=_compute_coach)
- `tz` Selection “Timezone” (related=resource_id.tz)
- `hr_presence_state` Selection (compute=_compute_presence_state)
- `last_activity` Date (compute=_compute_last_activity)
- `last_activity_time` Char (compute=_compute_last_activity)
- `hr_icon_display` Selection (compute=_compute_presence_icon)
- `show_hr_icon_display` Boolean (compute=_compute_presence_icon)
- `im_status` Char (related=user_id.im_status)
- `newly_hired` Boolean “Newly Hired” (compute=_compute_newly_hired)

Public methods: `get_avatar_card_data`

Extension points: `_create_work_contacts`, `_get_calendar_periods`, `_get_employee_working_now`, `_get_new_hire_field`, `_get_valid_employee_for_user`

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
- `work_location_id` Many2one (readonly)
- `user_id` Many2one (readonly)
- `resource_id` Many2one (readonly)
- `tz` Selection (readonly)
- `color` Integer (readonly)
- `is_manager` Boolean (compute=_compute_is_manager)
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

Extension points: `_get_fields`, `_get_manager_only_fields`

## `hr.job` (defines)

Job Position

Inherits: `mail.thread`

- `active` Boolean
- `name` Char “Job Position” (required)
- `sequence` Integer
- `expected_employees` Integer “Total Forecasted Employees” (store, compute=_compute_employees)
- `no_of_employee` Integer “Current Number of Employees” (store, compute=_compute_employees)
- `no_of_recruitment` Integer “Target”
- `employee_ids` One2many → `hr.employee` “Employees”
- `description` Html “Job Description”
- `requirements` Text “Requirements”
- `department_id` Many2one → `hr.department` “Department”
- `company_id` Many2one → `res.company` “Company”
- `contract_type_id` Many2one → `hr.contract.type` “Employment Type”

Public methods: `copy_data`, `create`, `write`

## `hr.work.location` (defines)

Work Location

- `active` Boolean
- `name` Char “Work Location” (required)
- `company_id` Many2one → `res.company` (required)
- `location_type` Selection “Cover Image” (required)
- `address_id` Many2one → `res.partner` “Work Address” (required)
- `location_number` Char

## `ir.ui.menu` (extends)


## `mail.activity.plan` (extends)

- `department_id` Many2one → `hr.department` (store, compute=_compute_department_id)
- `department_assignable` Boolean (compute=_compute_department_assignable)

Extension points: `_check_compatibility_with_model`

## `mail.activity.plan.template` (extends)

- `responsible_type` Selection

Extension points: `_check_responsible_hr`, `_get_closest_parent_user`

## `mail.alias` (extends)

- `alias_contact` Selection

Extension points: `_get_alias_contact_description`

## `base` (extends)


## `res.company` (extends)

- `hr_presence_control_email_amount` Integer “# emails to send”
- `hr_presence_control_ip_list` Char “Valid IP addresses”
- `employee_properties_definition` PropertiesDefinition “Employee Properties”
- `hr_presence_control_login` Boolean “Based on user status in system”
- `hr_presence_control_email` Boolean “Based on number of emails sent”
- `hr_presence_control_ip` Boolean “Based on IP Address”
- `hr_presence_control_attendance` Boolean “Based on attendances”

## `res.config.settings` (extends)

- `resource_calendar_id` Many2one → `resource.calendar` (related=company_id.resource_calendar_id)
- `module_hr_presence` Boolean “Advanced Presence Control”
- `module_hr_skills` Boolean “Skills Management”
- `module_hr_homeworking` Boolean “Remote Work”
- `hr_presence_control_login` Boolean (related=company_id.hr_presence_control_login)
- `hr_presence_control_email` Boolean (related=company_id.hr_presence_control_email)
- `hr_presence_control_ip` Boolean (related=company_id.hr_presence_control_ip)
- `module_hr_attendance` Boolean (related=company_id.hr_presence_control_attendance)
- `hr_presence_control_email_amount` Integer (related=company_id.hr_presence_control_email_amount)
- `hr_presence_control_ip_list` Char (related=company_id.hr_presence_control_ip_list)
- `hr_employee_self_edit` Boolean “Employee Editing”

Extension points: `_check_advanced_presence`

## `res.partner` (extends)

- `employee_ids` One2many → `hr.employee` “Employees”
- `employees_count` Integer (compute=_compute_employees_count)

Public methods: `action_open_employees`

Extension points: `_get_all_addr`

## `res.partner.bank` (extends)


## `res.users` (extends)

- `employee_ids` One2many → `hr.employee` “Related employee”
- `employee_id` Many2one → `hr.employee` “Company employee” (compute=_compute_company_employee)
- `job_title` Char (related=employee_id.job_title)
- `work_phone` Char (related=employee_id.work_phone)
- `mobile_phone` Char (related=employee_id.mobile_phone)
- `work_email` Char (related=employee_id.work_email)
- `category_ids` Many2many “Employee Tags” (related=employee_id.category_ids)
- `department_id` Many2one (related=employee_id.department_id)
- `address_id` Many2one (related=employee_id.address_id)
- `work_contact_id` Many2one (related=employee_id.work_contact_id)
- `work_location_id` Many2one (related=employee_id.work_location_id)
- `work_location_name` Char (related=employee_id.work_location_name)
- `work_location_type` Selection (related=employee_id.work_location_type)
- `employee_parent_id` Many2one (related=employee_id.parent_id)
- `coach_id` Many2one (related=employee_id.coach_id)
- `private_street` Char “Private Street” (related=employee_id.private_street)
- `private_street2` Char “Private Street2” (related=employee_id.private_street2)
- `private_city` Char “Private City” (related=employee_id.private_city)
- `private_state_id` Many2one “Private State” (related=employee_id.private_state_id)
- `private_zip` Char “Private Zip” (related=employee_id.private_zip)
- `private_country_id` Many2one “Private Country” (related=employee_id.private_country_id)
- `private_phone` Char (related=employee_id.private_phone)
- `private_email` Char “Private Email” (related=employee_id.private_email)
- `private_lang` Selection “Employee Lang” (related=employee_id.lang)
- `km_home_work` Integer (related=employee_id.km_home_work)
- `distance_home_work` Integer (related=employee_id.distance_home_work)
- `distance_home_work_unit` Selection (related=employee_id.distance_home_work_unit)
- `employee_bank_account_id` Many2one “Employee's Bank Account Number” (related=employee_id.bank_account_id)
- `employee_country_id` Many2one “Employee's Country” (related=employee_id.country_id)
- `employee_country_code` Char “Employee's Country Code” (readonly, related=employee_id.company_country_code)
- `identification_id` Char (related=employee_id.identification_id)
- `ssnid` Char (related=employee_id.ssnid)
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

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`, `action_create_employee`, `action_get`, `action_open_employees`, `create`, `get_view`, `get_views`, `write`

Extension points: `_get_employee_fields_to_sync`, `_get_personal_info_partner_ids_to_notify`

## `resource.resource` (extends)

- `user_id` Many2one
- `employee_id` One2many → `hr.employee`
- `job_title` Char (related=employee_id.job_title)
- `department_id` Many2one (related=employee_id.department_id)
- `work_email` Char (related=employee_id.work_email)
- `work_phone` Char (related=employee_id.work_phone)
- `show_hr_icon_display` Boolean (related=employee_id.show_hr_icon_display)
- `hr_icon_display` Selection (related=employee_id.hr_icon_display)

## `resource.calendar` (extends)


## `hr.manager.department.report` (defines)

Hr Manager Department Report

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `has_department_manager_access` Boolean (compute=_compute_has_department_manager_access)

## `hr.departure.wizard` (defines)

Departure Wizard

- `departure_reason_id` Many2one → `hr.departure.reason` (required)
- `departure_description` Html “Additional Information”
- `departure_date` Date “Departure Date” (required)
- `employee_id` Many2one → `hr.employee` “Employee” (required)

Public methods: `action_register_departure`

Extension points: `_get_default_departure_date`, `_get_employee_departure_date`

## `mail.activity.schedule` (extends)

- `department_id` Many2one → `hr.department` (compute=_compute_department_id)
- `plan_department_filterable` Boolean (compute=_compute_plan_department_filterable)
