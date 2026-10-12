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
- `complete_name` Char “Complete Name” (compute=_compute_complete_name)
- `active` Boolean “Active”
- `company_id` Many2one → `res.company` “Company” (store, index, compute=_compute_company_id)
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
- `country_id` Many2one → `res.country` “Country”
- `country_code` Char (related=country_id.code)

Extension points: `_get_default_departure_reasons`

## `hr.employee` (defines)

Employee

Inherits: `mail.thread.main.attachment`, `mail.activity.mixin`, `resource.mixin`, `avatar.mixin`

- `version_id` Many2one → `hr.version` (required, compute=_compute_version_id)
- `current_version_id` Many2one → `hr.version` (store, compute=_compute_current_version_id)
- `current_date_version` Date “Current Date Version” (related=current_version_id.date_version)
- `version_ids` One2many → `hr.version` “Employee Versions” (required)
- `versions_count` Integer (compute=_compute_versions_count)
- `version_revision` Char (compute=_compute_version_revision)
- `name` Char “Employee Name” (store, related=resource_id.name)
- `resource_id` Many2one → `resource.resource` (required)
- `resource_calendar_id` Many2one (related=version_id.resource_calendar_id)
- `user_id` Many2one → `res.users` (store, related=resource_id.user_id)
- `user_partner_id` Many2one “User's partner” (related=user_id.partner_id)
- `share` Boolean (related=user_id.share)
- `phone` Char (related=user_id.phone)
- `im_status` Char (related=user_id.im_status)
- `email` Char (related=user_id.email)
- `hr_presence_state` Selection (compute=_compute_presence_state)
- `last_activity` Date (compute=_compute_last_activity)
- `last_activity_time` Char (compute=_compute_last_activity)
- `hr_icon_display` Selection (compute=_compute_presence_icon)
- `show_hr_icon_display` Boolean (compute=_compute_presence_icon)
- `newly_hired` Boolean “Newly Hired” (compute=_compute_newly_hired)
- `active` Boolean “Active” (store, related=resource_id.active)
- `company_id` Many2one → `res.company` (required)
- `company_country_id` Many2one → `res.country` (readonly, related=company_id.country_id)
- `company_country_code` Char “Company Country Code” (readonly, related=company_country_id.code)
- `work_phone` Char “Work Phone” (store, compute=_compute_work_contact_details)
- `mobile_phone` Char “Work Mobile”
- `work_email` Char “Work Email” (store, compute=_compute_work_contact_details)
- `work_contact_id` Many2one → `res.partner`
- `legal_name` Char (store, compute=_compute_legal_name)
- `is_user_active` Boolean “User's active” (related=user_id.active)
- `private_phone` Char “Private Phone”
- `private_email` Char “Private Email”
- `lang` Selection “Lang”
- `place_of_birth` Char “Place of Birth”
- `country_of_birth` Many2one → `res.country` “Country of Birth”
- `birthday` Date “Birthday”
- `birthday_public_display` Boolean “Show to all employees”
- `birthday_public_display_string` Char “Public Date of Birth” (compute=_compute_birthday_public_display_string)
- `bank_account_ids` Many2many → `res.partner.bank` “Bank Accounts”
- `is_trusted_bank_account` Boolean (compute=_compute_is_trusted_bank_account)
- `primary_bank_account_id` Many2one → `res.partner.bank` (compute=_compute_primary_bank_account_id)
- `has_multiple_bank_accounts` Boolean (compute=_compute_has_multiple_bank_accounts)
- `salary_distribution` Json “Salary Distribution” (store, compute=_sync_salary_distribution)
- `permit_no` Char “Work Permit No”
- `visa_no` Char “Visa No”
- `visa_expire` Date “Visa Expiration Date”
- `work_permit_expiration_date` Date “Work Permit Expiration Date”
- `has_work_permit` Binary “Work Permit”
- `work_permit_scheduled_activity` Boolean
- `work_permit_name` Char “work_permit_name” (compute=_compute_work_permit_name)
- `certificate` Selection “Certificate Level”
- `study_field` Char “Field of Study”
- `study_school` Char “School”
- `emergency_contact` Char
- `emergency_phone` Char
- `work_location_name` Char “Work Location Name” (compute=_compute_work_location_name)
- `work_location_type` Selection (compute=_compute_work_location_type)
- `contract_date_start` Date (related=version_id.contract_date_start)
- `contract_date_end` Date (related=version_id.contract_date_end)
- `trial_date_end` Date (related=version_id.trial_date_end)
- `contract_wage` Monetary (related=version_id.contract_wage)
- `date_start` Date (related=version_id.date_start)
- `date_end` Date (related=version_id.date_end)
- `is_current` Boolean (related=version_id.is_current)
- `is_past` Boolean (related=version_id.is_past)
- `is_future` Boolean (related=version_id.is_future)
- `is_in_contract` Boolean (related=version_id.is_in_contract)
- `structure_type_id` Many2one (related=version_id.structure_type_id)
- `contract_type_id` Many2one (related=version_id.contract_type_id)
- `parent_id` Many2one → `hr.employee` (index)
- `child_ids` One2many → `hr.employee` “Direct subordinates”
- `coach_id` Many2one → `hr.employee` (store, compute=_compute_coach)
- `category_ids` Many2many → `hr.employee.category` “Tags”
- `tz` Selection
- `color` Integer “Color Index”
- `barcode` Char “Badge ID”
- `pin` Char “PIN”
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

Public methods: `action_archive`, `action_create_user`, `action_create_users`, `action_create_users_confirmation`, `action_open_allocation_wizard`, `action_open_versions`, `action_related_contacts`, `action_toggle_primary_bank_account_trust`, `action_unarchive`, `check_field_access_rights`, `check_no_existing_contract`, `create`, `create_contract`, `create_version`, `fetch`, `generate_random_barcode`, `get_accounts_with_fixed_allocations`, `get_avatar_card_data`, `get_bank_account_salary_allocation`, `get_formview_action`, `get_formview_id`, `get_import_templates`, `get_remaining_percentage`, `get_view`, `get_views`, `new`, `notify_expiring_contract_work_permit`, `search_fetch`, `unlink`, `write`

Extension points: `_check_access`, `_check_private_fields`, `_check_salary_distribution`, `_create_work_contacts`, `_get_age`, `_get_all_contract_dates`, `_get_all_versions_with_contract_overlap_with_period`, `_get_calendar_attendances`, `_get_calendar_periods`, `_get_calendar_tz_batch`, `_get_calendars`, `_get_certificate_selection`, `_get_contract_dates`, `_get_contract_versions`, `_get_contracts`, `_get_departure_date`, `_get_employee_m2o_to_empty_on_archived_employees`, `_get_employee_unavailable_intervals`, `_get_employee_working_now`, `_get_expected_attendances`, `_get_first_contract_date`, `_get_first_version_date`, `_get_first_versions`, `_get_first_versions_filtered`, `_get_new_hire_field`, `_get_partner_count_depends`, `_get_related_partners`, `_get_store_avatar_card_fields`, `_get_tz`, `_get_tz_batch`, `_get_unusual_days`, `_get_user_m2o_to_empty_on_archived_employees`, `_get_version`, `_get_version_periods`, `_get_versions_with_contract_overlap_with_period`, `_prepare_create_values`, `_prepare_resource_values`

## `hr.employee.category` (defines)

Employee Category

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”
- `employee_ids` Many2many → `hr.employee` “Employees”

Extension points: `_get_default_color`

## `hr.employee.public` (defines)

Public Employee

- `create_date` Datetime (readonly)
- `name` Char (readonly)
- `active` Boolean (readonly)
- `department_id` Many2one → `hr.department` (readonly)
- `member_of_department` Boolean (compute=_compute_member_of_department)
- `job_id` Many2one → `hr.job` (readonly)
- `job_title` Char (related=employee_id.job_title)
- `company_id` Many2one → `res.company` (readonly)
- `address_id` Many2one → `res.partner` (readonly)
- `mobile_phone` Char (readonly)
- `work_phone` Char (readonly)
- `work_email` Char (readonly)
- `share` Boolean (related=employee_id.share)
- `phone` Char (related=employee_id.phone)
- `im_status` Char (related=employee_id.im_status)
- `email` Char (related=employee_id.email)
- `work_contact_id` Many2one → `res.partner` (readonly)
- `work_location_id` Many2one → `hr.work.location` (readonly)
- `work_location_name` Char (related=employee_id.work_location_name)
- `work_location_type` Selection (related=employee_id.work_location_type)
- `user_id` Many2one → `res.users` (readonly)
- `resource_id` Many2one → `resource.resource` (readonly)
- `tz` Selection (related=resource_id.tz)
- `color` Integer (readonly)
- `hr_presence_state` Selection (compute=_compute_presence_state)
- `hr_icon_display` Selection (compute=_compute_presence_icon)
- `show_hr_icon_display` Boolean (compute=_compute_presence_icon)
- `last_activity` Date (compute=_compute_last_activity)
- `last_activity_time` Char (compute=_compute_last_activity)
- `resource_calendar_id` Many2one → `resource.calendar` (readonly)
- `country_code` Char (compute=_compute_country_code)
- `is_manager` Boolean (compute=_compute_is_manager)
- `is_user` Boolean (compute=_compute_is_user)
- `employee_id` Many2one → `hr.employee` (readonly)
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
- `birthday_public_display_string` Char “Public Date of Birth” (related=employee_id.birthday_public_display_string)
- `newly_hired` Boolean “Newly Hired” (compute=_compute_newly_hired)

Public methods: `get_avatar_card_data`, `init`

Extension points: `_get_fields`, `_get_manager_only_fields`, `_get_selection_hr_icon_display`, `_get_valid_employee_for_user`

## `hr.job` (defines)

Job Position

Inherits: `mail.thread`

- `active` Boolean
- `name` Char “Job Position” (required)
- `sequence` Integer
- `expected_employees` Integer “Total Forecasted Employees” (compute=_compute_employees)
- `no_of_employee` Integer “Current Number of Employees” (compute=_compute_employees)
- `no_of_recruitment` Integer “Target”
- `employee_ids` One2many → `hr.employee` “Employees”
- `description` Html “Job Description”
- `requirements` Text “Requirements”
- `user_id` Many2one → `res.users`
- `allowed_user_ids` Many2many → `res.users` (readonly, compute=_compute_allowed_user_ids)
- `department_id` Many2one → `hr.department` “Department”
- `company_id` Many2one → `res.company` “Company”
- `contract_type_id` Many2one → `hr.contract.type` “Employment Type”

Public methods: `copy_data`, `create`, `write`

## `hr.mixin` (defines)

hr.mixin


Public methods: `create`, `write`

## `hr.payroll.structure.type` (defines)

Salary Structure Type

- `name` Char “Salary Structure Type”
- `default_resource_calendar_id` Many2one → `resource.calendar`
- `country_id` Many2one → `res.country` “Country”
- `country_code` Char (related=country_id.code)

## `hr.version` (defines)

Version

Inherits: `mail.thread`, `mail.activity.mixin`

- `company_id` Many2one → `res.company` (store, compute=_compute_company_id)
- `employee_id` Many2one → `hr.employee` “Employee” (index)
- `name` Char
- `display_name` Char (compute=_compute_display_name)
- `active` Boolean
- `date_version` Date (required)
- `last_modified_uid` Many2one → `res.users` “Last Modified by” (required)
- `last_modified_date` Datetime “Last Modified on” (required)
- `country_id` Many2one → `res.country`
- `identification_id` Char “Identification No”
- `ssnid` Char “SSN No”
- `passport_id` Char “Passport No”
- `passport_expiration_date` Date “Passport Expiration Date”
- `sex` Selection “Gender”
- `private_street` Char “Private Street”
- `private_street2` Char “Private Street2”
- `private_city` Char “Private City”
- `allowed_country_state_ids` Many2many → `res.country.state` (compute=_compute_allowed_country_state_ids)
- `private_state_id` Many2one → `res.country.state` “Private State”
- `private_zip` Char “Private Zip”
- `private_country_id` Many2one → `res.country` “Private Country”
- `distance_home_work` Integer “Home-Work Distance”
- `km_home_work` Integer “Home-Work Distance in Km” (store, compute=_compute_km_home_work)
- `distance_home_work_unit` Selection (required)
- `marital` Selection “Marital Status” (required)
- `spouse_complete_name` Char “Spouse Legal Name”
- `spouse_birthdate` Date “Spouse Birthdate”
- `children` Integer “Dependent Children”
- `employee_type` Selection “Employee Type” (required)
- `department_id` Many2one → `hr.department` (index)
- `member_of_department` Boolean “Member of department” (compute=_compute_part_of_department)
- `job_id` Many2one → `hr.job` (index)
- `job_title` Char “Job Title” (store, compute=_compute_job_title)
- `is_custom_job_title` Boolean (store, compute=_compute_is_custom_job_title)
- `address_id` Many2one → `res.partner` “Work Address” (store)
- `work_location_id` Many2one → `hr.work.location`
- `departure_reason_id` Many2one → `hr.departure.reason` “Departure Reason”
- `departure_description` Html “Additional Information”
- `departure_date` Date “Departure Date”
- `resource_calendar_id` Many2one → `resource.calendar` “Working Hours”
- `is_flexible` Boolean (store, compute=_compute_is_flexible)
- `is_fully_flexible` Boolean (store, compute=_compute_is_flexible)
- `tz` Selection (related=employee_id.tz)
- `contract_date_start` Date “Contract Start Date”
- `contract_date_end` Date “Contract End Date”
- `trial_date_end` Date “End of Trial Period”
- `date_start` Date (compute=_compute_dates)
- `date_end` Date (compute=_compute_dates)
- `is_current` Boolean (compute=_compute_is_current)
- `is_past` Boolean (compute=_compute_is_past)
- `is_future` Boolean (compute=_compute_is_future)
- `is_in_contract` Boolean (compute=_compute_is_in_contract)
- `contract_template_id` Many2one → `hr.version` “Contract Template”
- `structure_type_id` Many2one → `hr.payroll.structure.type` “Salary Structure Type” (store, compute=_compute_structure_type_id)
- `active_employee` Boolean “Active Employee” (related=employee_id.active)
- `currency_id` Many2one “Currency” (readonly, related=company_id.currency_id)
- `wage` Monetary “Wage”
- `contract_wage` Monetary “Contract Wage” (compute=_compute_contract_wage)
- `company_country_id` Many2one → `res.country` “Company country” (readonly, related=company_id.country_id)
- `country_code` Char (readonly, related=company_country_id.code)
- `contract_type_id` Many2one → `hr.contract.type`
- `additional_note` Text “Additional Note”
- `hr_responsible_id` Many2one → `res.users` (required)

Public methods: `action_open_version`, `action_open_version_form_view`, `check_contract_finished`, `create`, `get_formview_action`, `get_values_from_contract_template`, `write`

Extension points: `_check_dates`, `_check_ssnid`, `_get_contract_wage`, `_get_contract_wage_field`, `_get_default_address_id`, `_get_hr_responsible_domain`, `_get_marital_status_selection`, `_get_normalized_wage`, `_get_salary_costs_factor`, `_get_tz`, `_get_valid_employee_for_user`, `_get_whitelist_fields_from_template`

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
- `contract_expiration_notice_period` Integer “Contract Expiry Notice Period”
- `work_permit_expiration_notice_period` Integer “Work Permit Expiry Notice Period”

## `res.config.settings` (extends)

- `resource_calendar_id` Many2one → `resource.calendar` (related=company_id.resource_calendar_id)
- `module_hr_presence` Boolean “Advanced Presence Control”
- `module_hr_skills` Boolean “Skills Management”
- `hr_presence_control_login` Boolean (related=company_id.hr_presence_control_login)
- `hr_presence_control_email` Boolean (related=company_id.hr_presence_control_email)
- `hr_presence_control_ip` Boolean (related=company_id.hr_presence_control_ip)
- `module_hr_attendance` Boolean (related=company_id.hr_presence_control_attendance)
- `hr_presence_control_email_amount` Integer (related=company_id.hr_presence_control_email_amount)
- `hr_presence_control_ip_list` Char (related=company_id.hr_presence_control_ip_list)
- `contract_expiration_notice_period` Integer “Contract Expiry Notice Period” (related=company_id.contract_expiration_notice_period)
- `work_permit_expiration_notice_period` Integer “Work Permit Expiry Notice Period” (related=company_id.work_permit_expiration_notice_period)

## `res.partner` (extends)

- `employee_ids` One2many → `hr.employee` “Employees”
- `employees_count` Integer (compute=_compute_employees_count)
- `employee` Boolean (store, compute=_compute_employee)

Public methods: `action_open_employees`

Extension points: `_action_show`, `_get_all_addr`, `_get_store_avatar_card_fields`

## `res.partner.bank` (extends)

- `bank_street` Char (related=bank_id.street)
- `bank_street2` Char (related=bank_id.street2)
- `bank_zip` Char (related=bank_id.zip)
- `bank_city` Char (related=bank_id.city)
- `bank_state` Many2one (related=bank_id.state)
- `bank_country` Many2one (related=bank_id.country)
- `bank_email` Char (related=bank_id.email)
- `bank_phone` Char (related=bank_id.phone)
- `employee_id` Many2many → `hr.employee` (compute=_compute_employee_id)
- `employee_salary_amount` Float “Salary Allocation” (readonly, compute=_compute_salary_amount)
- `employee_salary_amount_is_percentage` Boolean (readonly, compute=_compute_salary_amount)
- `currency_symbol` Char (related=currency_id.symbol)
- `employee_has_multiple_bank_accounts` Boolean (related=employee_id.has_multiple_bank_accounts)

Public methods: `action_open_allocation_wizard`

## `res.users` (extends)

- `employee_ids` One2many → `hr.employee` “Related employee”
- `employee_id` Many2one → `hr.employee` “Company employee” (compute=_compute_company_employee)
- `job_title` Char (related=employee_id.job_title)
- `work_phone` Char (related=employee_id.work_phone)
- `mobile_phone` Char (related=employee_id.mobile_phone)
- `work_email` Char (related=employee_id.work_email)
- `category_ids` Many2many “Employee Tags” (related=employee_id.category_ids)
- `work_contact_id` Many2one (related=employee_id.work_contact_id)
- `work_location_id` Many2one (related=employee_id.work_location_id)
- `work_location_name` Char (related=employee_id.work_location_name)
- `work_location_type` Selection (related=employee_id.work_location_type)
- `private_street` Char “Private Street” (related=employee_id.private_street)
- `private_street2` Char “Private Street2” (related=employee_id.private_street2)
- `private_city` Char “Private City” (related=employee_id.private_city)
- `private_state_id` Many2one “Private State” (related=employee_id.private_state_id)
- `private_zip` Char “Private Zip” (related=employee_id.private_zip)
- `private_country_id` Many2one “Private Country” (related=employee_id.private_country_id)
- `private_phone` Char (related=employee_id.private_phone)
- `private_email` Char “Private Email” (related=employee_id.private_email)
- `km_home_work` Integer (related=employee_id.km_home_work)
- `employee_bank_account_ids` Many2many → `res.partner.bank` “Employee's Bank Accounts” (related=employee_id.bank_account_ids)
- `emergency_contact` Char (related=employee_id.emergency_contact)
- `emergency_phone` Char (related=employee_id.emergency_phone)
- `visa_expire` Date (related=employee_id.visa_expire)
- `additional_note` Text (related=employee_id.additional_note)
- `barcode` Char (related=employee_id.barcode)
- `pin` Char (related=employee_id.pin)
- `employee_count` Integer (compute=_compute_employee_count)
- `employee_resource_calendar_id` Many2one “Employee's Working Hours” (readonly, related=employee_id.resource_calendar_id)
- `bank_account_ids` Many2many (related=employee_id.bank_account_ids)
- `create_employee` Boolean “Technical field, whether to create an employee”
- `create_employee_id` Many2one → `hr.employee` “Technical field, bind user to this employee on create”
- `is_system` Boolean (compute=_compute_is_system)
- `is_hr_user` Boolean (compute=_compute_is_hr_user)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`, `action_create_employee`, `action_get`, `action_open_employees`, `action_related_contact`, `create`, `get_formview_action`, `get_view`, `get_views`, `write`

Extension points: `_get_employee_fields_to_sync`, `_get_personal_info_partner_ids_to_notify`

## `resource.resource` (extends)

- `user_id` Many2one
- `employee_id` One2many → `hr.employee`
- `job_title` Char (compute=_compute_job_title)
- `department_id` Many2one → `hr.department` (compute=_compute_department_id)
- `work_location_id` Many2one (related=employee_id.work_location_id)
- `work_email` Char (related=employee_id.work_email)
- `work_phone` Char (related=employee_id.work_phone)
- `show_hr_icon_display` Boolean (related=employee_id.show_hr_icon_display)
- `hr_icon_display` Selection (related=employee_id.hr_icon_display)
- `calendar_id` Many2one

Extension points: `_get_calendar_at`, `_get_calendars_validity_within_period`, `_get_contracts_valid_periods`, `_get_flexible_resources_calendars_validity_within_period`, `_get_resource_without_contract`

## `resource.calendar` (extends)


Public methods: `transfer_leaves_to`

## `resource.calendar.leaves` (extends)


## `hr.manager.department.report` (defines)

Hr Manager Department Report

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `has_department_manager_access` Boolean (compute=_compute_has_department_manager_access)

## `hr.bank.account.allocation.wizard.line` (defines)

Bank Account Allocation Line (Wizard)

- `wizard_id` Many2one → `hr.bank.account.allocation.wizard` (required)
- `bank_account_id` Many2one → `res.partner.bank` (required, readonly)
- `acc_number` Char (readonly, related=bank_account_id.acc_number)
- `amount` Float “Amount”
- `amount_type` Selection
- `symbol` Char (readonly, compute=_compute_symbol)
- `trusted` Boolean “Trusted”
- `sequence` Integer

Extension points: `_get_amount_type_selection_vals`

## `hr.bank.account.allocation.wizard` (defines)

Bank Account Allocation Wizard

- `employee_id` Many2one → `hr.employee` (required)
- `allocation_ids` One2many → `hr.bank.account.allocation.wizard.line` “Allocations”

Public methods: `action_save`, `create`

Extension points: `_prepare_allocations_from_employee`

## `hr.version.wizard` (defines)

Contract Template Wizard

- `contract_template_id` Many2one → `hr.version` “Contract Template” (required)

Public methods: `action_load_template`

## `hr.departure.wizard` (defines)

Departure Wizard

- `departure_reason_id` Many2one → `hr.departure.reason` (required)
- `departure_description` Html “Additional Information”
- `departure_date` Date “Contract End Date” (required)
- `employee_ids` Many2many → `hr.employee` “Employees” (required)
- `is_user_employee` Boolean “User Employee” (compute=_compute_is_user_employee)
- `remove_related_user` Boolean “Related User”
- `set_date_end` Boolean “Set Contract End Date”

Public methods: `action_register_departure`

Extension points: `_get_default_departure_date`, `_get_default_employee_ids`, `_get_domain_employee_ids`

## `mail.activity.schedule` (extends)

- `department_id` Many2one → `hr.department` (compute=_compute_department_id)
- `plan_department_filterable` Boolean (compute=_compute_plan_department_filterable)
