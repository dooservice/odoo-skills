# hr — Employees

Depends on: auth_signup, base_setup, digest, phone_validation, resource_mail, web_hierarchy.

## `discuss.channel` (extends)

- `subscription_department_ids` Many2many → `hr.department` “HR Departments”

Public methods: `write`

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

Public methods: `action_employee_from_department`, `action_open_view_child_departments`, `action_plan_from_department`, `create`, `get_children_department_ids`, `get_department_hierarchy`, `get_record_default_action`, `name_create`, `write`

## `hr.departure.reason` (defines)

Departure Reason

- `active` Boolean
- `sequence` Integer “Sequence”
- `name` Char “Reason” (required)
- `country_id` Many2one → `res.country` “Country”
- `country_code` Char (related=country_id.code)

Extension points: `_get_default_departure_reasons`

## `hr.employee` (defines)

Employee

Inherits: `mail.thread.main.attachment`, `mail.thread.phone`, `mail.activity.mixin`, `resource.mixin`, `avatar.mixin`

- `version_id` Many2one → `hr.version` “Employee Record” (required, compute=_compute_version_id)
- `current_version_id` Many2one → `hr.version` “Current Employee Record” (store, index, compute=_compute_current_version_id)
- `current_date_version` Date “Current Date Employee Record” (related=current_version_id.date_version)
- `version_ids` One2many → `hr.version` “Employee Records” (required)
- `versions_count` Integer “Employee Records Count” (compute=_compute_versions_count)
- `version_revision` Char (compute=_compute_version_revision)
- `contract_template_id` Many2one → `hr.version`
- `hr_responsible_id` Many2one (related=version_id.hr_responsible_id)
- `name` Char “Employee Name” (store, related=resource_id.name)
- `resource_id` Many2one → `resource.resource` (required)
- `resource_calendar_id` Many2one (related=version_id.resource_calendar_id)
- `user_id` Many2one → `res.users` (store, related=resource_id.user_id)
- `user_partner_id` Many2one “User's partner” (related=user_id.partner_id)
- `share` Boolean (related=user_id.share)
- `phone` Char (related=user_id.phone)
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
- `parent_company_id` Many2one (readonly, related=company_id.parent_id)
- `work_phone` Char “Work Phone” (store, compute=_compute_work_contact_details)
- `mobile_phone` Char “Work Mobile”
- `work_phone_sanitized` Char (compute=_compute_phone_companion_fields)
- `work_phone_formatted` Char (compute=_compute_phone_companion_fields)
- `mobile_phone_sanitized` Char (compute=_compute_phone_companion_fields)
- `mobile_phone_formatted` Char (compute=_compute_phone_companion_fields)
- `phone_blacklisted` Boolean
- `phone_sanitized_blacklisted` Boolean
- `phone_mobile_search` Char
- `work_email` Char “Work Email” (store, compute=_compute_work_contact_details)
- `work_contact_id` Many2one → `res.partner`
- `legal_name` Char (store, compute=_compute_legal_name)
- `split_legal_name` Boolean (compute=_compute_split_legal_name)
- `private_phone` Char “Private Phone”
- `private_phone_sanitized` Char (compute=_compute_restricted_phone_companion_fields)
- `private_phone_formatted` Char (compute=_compute_restricted_phone_companion_fields)
- `private_email` Char “Private Email”
- `lang` Selection “Lang”
- `place_of_birth` Char “Place of Birth”
- `country_of_birth` Many2one → `res.country` “Country of Birth”
- `birthday` Date “Birthday”
- `birthday_public_display` Boolean “Show Birthday To Employees”
- `birthday_public_display_string` Char “Public Date of Birth” (compute=_compute_birthday_public_display_string)
- `age` Integer “Age” (compute=_compute_age)
- `birthday_month` Selection “Birthday Month” (store, compute=_compute_birthday_month)
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
- `emergency_contact` Char
- `emergency_phone` Char
- `emergency_phone_sanitized` Char (compute=_compute_restricted_phone_companion_fields)
- `emergency_phone_formatted` Char (compute=_compute_restricted_phone_companion_fields)
- `additional_note` Text “Additional Note”
- `work_location_name` Char “Work Location Name” (compute=_compute_work_location_name)
- `work_location_type` Selection (compute=_compute_work_location_type)
- `first_contract_date` Date (store, compute=_compute_first_contract_date)
- `contract_date_start` Date (related=version_id.contract_date_start)
- `contract_date_end` Date (related=version_id.contract_date_end)
- `fixed_term` Boolean (related=version_id.fixed_term)
- `trial_date_end` Date (related=version_id.trial_date_end)
- `date_start` Date (related=version_id.date_start)
- `date_end` Date (related=version_id.date_end)
- `is_current` Boolean (related=version_id.is_current)
- `is_past` Boolean (related=version_id.is_past)
- `is_future` Boolean (related=version_id.is_future)
- `is_in_contract` Boolean (related=version_id.is_in_contract)
- `structure_type_id` Many2one (related=version_id.structure_type_id)
- `employee_type_id` Many2one (related=version_id.employee_type_id)
- `hourly_cost` Monetary “Hourly Cost”
- `nationality_country_code` Char “Nationality” (related=version_id.country_id.code)
- `parent_id` Many2one → `hr.employee` (index)
- `child_ids` One2many → `hr.employee` “Direct subordinates”
- `child_count` Integer “Direct Subordinates Count” (compute=_compute_child_count)
- `subordinate_ids` One2many → `hr.employee` “Subordinates” (compute=_compute_subordinates)
- `is_subordinate` Boolean (compute=_compute_is_subordinate)
- `child_all_count` Integer “Indirect Subordinates Count” (compute=_compute_subordinates)
- `department_color` Integer “Department Color” (related=department_id.color)
- `coach_id` Many2one → `hr.employee` (store, compute=_compute_coach)
- `category_ids` Many2many → `hr.employee.category` “Tags”
- `tz` Selection (related=version_id.tz)
- `color` Integer “Color Index”
- `barcode` Char “Badge ID”
- `pin` Char “PIN”
- `message_main_attachment_id` Many2one
- `id_card` Binary “ID Card Copy”
- `driving_license` Binary “Driving License”
- `id_card_name` Char
- `driving_license_name` Char
- `currency_id` Many2one → `res.currency` (readonly, related=company_id.currency_id)
- `related_partners_count` Integer (compute=_compute_related_partners_count)
- `employee_properties` Properties “Properties”
- `departure_id` Many2one (related=version_id.departure_id)
- `departure_reason_id` Many2one (related=version_id.departure_reason_id)
- `departure_description` Html (related=version_id.departure_description)
- `dismissal_date` Date (related=version_id.dismissal_date)
- `departure_date` Date (related=version_id.departure_date)
- `departure_action_date` Date (related=version_id.departure_action_date)
- `departure_apply_immediately` Boolean (related=version_id.departure_apply_immediately)
- `departure_apply_date` Date (related=version_id.departure_apply_date)
- `activity_ids` One2many
- `activity_state` Selection
- `activity_user_id` Many2one
- `activity_type_id` Many2one
- `activity_type_icon` Char
- `activity_plans_ids` Many2many
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
- `monday_location_id` Many2one → `hr.work.location` “Monday”
- `tuesday_location_id` Many2one → `hr.work.location` “Tuesday”
- `wednesday_location_id` Many2one → `hr.work.location` “Wednesday”
- `thursday_location_id` Many2one → `hr.work.location` “Thursday”
- `friday_location_id` Many2one → `hr.work.location` “Friday”
- `saturday_location_id` Many2one → `hr.work.location` “Saturday”
- `sunday_location_id` Many2one → `hr.work.location` “Sunday”
- `exceptional_location_id` Many2one → `hr.work.location` “Current” (compute=_compute_exceptional_location_id)
- `today_location_name` Char
- `user_state` Selection “User Status” (related=user_id.state)

Public methods: `action_archive`, `action_cancel_departure`, `action_copy_invitation_link`, `action_deactivate_user_and_depart`, `action_new_departure`, `action_open_allocation_wizard`, `action_open_versions`, `action_related_contacts`, `action_reset_password`, `action_send_invitation`, `action_toggle_primary_bank_account_trust`, `action_toggle_user_active`, `check_no_existing_contract`, `create`, `create_contract`, `create_version`, `cycles_in_hierarchy_read`, `fetch`, `formatted_employee_attendance_intervals`, `generate_random_barcode`, `get_accounts_with_fixed_allocations`, `get_bank_account_salary_allocation`, `get_formview_id`, `get_import_templates`, `get_multi_version_changes`, `get_record_default_action`, `get_remaining_percentage`, `get_view`, `get_views`, `is_onboarding`, `load_demo_data`, `new`, `notify_expiring_contract_work_permit`, `search_fetch`, `unlink`, `write`

Extension points: `_check_private_fields`, `_check_salary_distribution`, `_create_work_contacts`, `_get_age`, `_get_all_contract_dates`, `_get_all_versions_with_contract_overlap_with_period`, `_get_calendar_attendances`, `_get_calendar_periods`, `_get_calendars`, `_get_certificate_selection`, `_get_contract_dates`, `_get_contract_versions`, `_get_contracts`, `_get_current_day_location_field`, `_get_employee_m2o_to_empty_on_archived_employees`, `_get_employee_unavailable_intervals`, `_get_employee_working_now`, `_get_expected_attendances`, `_get_first_contract_date`, `_get_first_contract_version_at`, `_get_first_version_date`, `_get_first_versions`, `_get_hours_per_day_batch`, `_get_hours_per_week_batch`, `_get_hr_responsible_domain`, `_get_last_consecutive_versions`, `_get_new_hire_field`, `_get_or_create_light_user`, `_get_partner_count_depends`, `_get_related_partners`, `_get_resources_per_tz`, `_get_splitting_legal_name_countries`, `_get_subordinates`, `_get_tz`, `_get_tz_batch`, `_get_unusual_days`, `_get_user_m2o_to_empty_on_archived_employees`, `_get_version`, `_get_version_periods`, `_get_versions_with_contract_overlap_with_period`, `_get_working_periods_by_field`, `_prepare_create_values`, `_prepare_resource_values`

## `hr.employee.category` (defines)

Employee Category

- `name` Char “Tag Name” (required)
- `color` Integer “Color Index”
- `employee_ids` Many2many → `hr.employee` “Employees”

Extension points: `_get_default_color`

## `hr.employee.departure` (defines)

Employee Departure

- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `country_code` Char (related=employee_id.company_id.partner_id.country_id.code)
- `departure_reason_id` Many2one → `hr.departure.reason` “End Reason” (required, index)
- `departure_description` Html “Additional Information”
- `dismissal_date` Date “Dismissal Date” (required)
- `departure_date` Date “Departure Date” (store, compute=_compute_departure_date)
- `action_date` Date “Archive Employee On” (store, compute=_compute_action_date)
- `is_user_employee` Boolean (compute=_compute_is_user_employee)
- `apply_immediately` Boolean (compute=_compute_apply_immediately)
- `apply_date` Date (readonly)
- `last_contract_date_end` Date

Public methods: `action_register`, `action_schedule`, `create`

Extension points: `_check_departure_validity`, `_get_default_departure_reason`, `_get_default_employee_id`, `_get_departure_reason_domain`, `_get_departures_to_archive`, `_get_domain_employee_id`

## `hr.employee.location` (defines)

Employee Location

- `work_location_id` Many2one → `hr.work.location` “Location” (required, index)
- `work_location_name` Char “Location name” (related=work_location_id.name)
- `work_location_type` Selection (related=work_location_id.location_type)
- `employee_id` Many2one → `hr.employee` (required)
- `employee_name` Char (related=employee_id.name)
- `date` Date “Date”
- `day_week_string` Char (compute=_compute_day_week_string)

## `hr.employee.public` (defines)

Public Employee

- `create_date` Datetime (readonly)
- `name` Char (readonly)
- `active` Boolean (readonly)
- `department_id` Many2one → `hr.department` (readonly)
- `member_of_department` Boolean (compute=_compute_member_of_department)
- `job_id` Many2one → `hr.job` (readonly)
- `job_title` Char (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `address_id` Many2one → `res.partner` (readonly)
- `mobile_phone` Char (readonly)
- `work_phone` Char (readonly)
- `phone_sanitized` Char (readonly)
- `phone_formatted` Char (related=employee_id.phone_formatted)
- `work_phone_sanitized` Char (related=employee_id.work_phone_sanitized)
- `work_phone_formatted` Char (related=employee_id.work_phone_formatted)
- `mobile_phone_sanitized` Char (related=employee_id.mobile_phone_sanitized)
- `mobile_phone_formatted` Char (related=employee_id.mobile_phone_formatted)
- `work_email` Char (readonly)
- `share` Boolean (related=employee_id.share)
- `phone` Char (related=employee_id.phone)
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
- `hours_per_week` Float (compute=_compute_hours_per_week)
- `hours_per_day` Float (compute=_compute_hours_per_day)
- `country_code` Char (compute=_compute_country_code)
- `is_manager` Boolean (compute=_compute_is_manager)
- `is_user` Boolean (compute=_compute_is_user)
- `employee_id` Many2one → `hr.employee` (readonly)
- `child_ids` One2many → `hr.employee.public` “Direct subordinates” (readonly)
- `child_count` Integer (compute=_compute_child_count)
- `subordinate_ids` One2many (related=employee_id.subordinate_ids)
- `is_subordinate` Boolean (related=employee_id.is_subordinate)
- `child_all_count` Integer (compute=_compute_child_all_count)
- `department_color` Integer (compute=_compute_department_color)
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
- `monday_location_id` Many2one → `hr.work.location` “Monday”
- `tuesday_location_id` Many2one → `hr.work.location` “Tuesday”
- `wednesday_location_id` Many2one → `hr.work.location` “Wednesday”
- `thursday_location_id` Many2one → `hr.work.location` “Thursday”
- `friday_location_id` Many2one → `hr.work.location` “Friday”
- `saturday_location_id` Many2one → `hr.work.location` “Saturday”
- `sunday_location_id` Many2one → `hr.work.location` “Sunday”
- `today_location_name` Char

Public methods: `init`

Extension points: `_get_fields`, `_get_manager_only_fields`, `_get_selection_hr_icon_display`, `_get_valid_employee_for_user`

## `hr.employee.type` (defines)

Employee Type

- `name` Char (required)
- `code` Char (store, compute=_compute_code)
- `country_id` Many2one → `res.country`
- `country_code` Char (related=country_id.code)
- `company_id` Many2one → `res.company` “Company”
- `employees_count` Integer “Employees” (compute=_compute_employee_count)
- `employee_ids` One2many → `hr.employee` “Related Employees”
- `sequence` Integer

Public methods: `action_open_employees`

Extension points: `_check_country_id`

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
- `recruiter_id` Many2one → `hr.employee` (index)
- `department_id` Many2one → `hr.department` “Department”
- `company_id` Many2one → `res.company` “Company” (required, index)
- `employee_type_id` Many2one → `hr.employee.type` “Employee Type”
- `company_country_code` Char (related=company_id.country_id.code)

Public methods: `create`, `write`

## `hr.mixin` (defines)

hr.mixin


Public methods: `create`, `write`

## `hr.payroll.structure.type` (defines)

Salary Structure Type

- `name` Char “Salary Structure Type”
- `default_resource_calendar_id` Many2one → `resource.calendar` “Working Hours”
- `country_id` Many2one → `res.country` “Country”
- `country_code` Char (related=country_id.code)

## `hr.version` (defines)

Employee Record

Inherits: `mail.thread`, `mail.activity.mixin`

- `company_id` Many2one → `res.company` (store, index, compute=_compute_company_id)
- `employee_id` Many2one → `hr.employee` “Employee” (index)
- `name` Char
- `display_name` Char (compute=_compute_display_name)
- `active` Boolean
- `date_version` Date “Effective Date” (required)
- `last_modified_uid` Many2one → `res.users` “Last Modified by” (required)
- `last_modified_date` Datetime “Last Modified on” (required)
- `country_id` Many2one → `res.country`
- `identification_id` Char “Identification No”
- `passport_id` Char “Passport No”
- `passport_expiration_date` Date “Passport Expiration Date”
- `sex` Selection
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
- `department_id` Many2one → `hr.department` (index)
- `member_of_department` Boolean “Member of department” (compute=_compute_part_of_department)
- `job_id` Many2one → `hr.job` (index)
- `job_title` Char “Job Title” (store, compute=_compute_job_title)
- `is_custom_job_title` Boolean (store, compute=_compute_is_custom_job_title)
- `address_id` Many2one → `res.partner` “Work Address” (store)
- `work_location_id` Many2one → `hr.work.location` (store, index, compute=_compute_work_location_id)
- `departure_id` Many2one → `hr.employee.departure` “Departure”
- `departure_reason_id` Many2one (related=departure_id.departure_reason_id)
- `departure_description` Html (related=departure_id.departure_description)
- `dismissal_date` Date (related=departure_id.dismissal_date)
- `departure_date` Date (related=departure_id.departure_date)
- `departure_action_date` Date (related=departure_id.action_date)
- `departure_apply_immediately` Boolean (related=departure_id.apply_immediately)
- `departure_apply_date` Date (related=departure_id.apply_date)
- `resource_calendar_id` Many2one → `resource.calendar` “Working Hours” (required)
- `tz` Selection “Timezone” (required)
- `contract_date_start` Date “Contract Start Date”
- `contract_date_end` Date “Contract End Date”
- `fixed_term` Boolean “Fixed Term”
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
- `company_country_id` Many2one → `res.country` “Company country” (readonly, related=company_id.country_id)
- `country_code` Char (readonly, related=company_country_id.code)
- `employee_type_id` Many2one → `hr.employee.type` (index)
- `hr_responsible_id` Many2one → `res.users` (required)

Public methods: `action_open_version`, `action_open_version_form_view`, `check_contract_finished`, `create`, `get_record_default_action`, `get_values_from_contract_template`, `write`

Extension points: `_check_dates`, `_get_contract_wage`, `_get_contract_wage_field`, `_get_current_versions_domain`, `_get_default_address_id`, `_get_field_block_start_date`, `_get_hr_responsible_domain`, `_get_marital_status_selection`, `_get_normalized_wage`, `_get_reference_calendar`, `_get_resources_per_tz`, `_get_salary_costs_factor`, `_get_tz`, `_get_valid_employee_for_user`, `_get_whitelist_fields_from_template`

## `hr.work.location` (defines)

Work Location

- `active` Boolean
- `name` Char “Work Location” (required)
- `company_id` Many2one → `res.company` (required, index)
- `location_type` Selection “Location Type” (required)
- `icon` Char (compute=_compute_icon)
- `address_id` Many2one → `res.partner` “Work Address”
- `location_number` Char
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `country_code` Char (related=company_id.country_id.code)

## `ir.ui.menu` (extends)


## `mail.activity` (extends)

- `technical_usage` Selection

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
- `company_tz` Selection “Company Timezone” (related=company_id.tz)
- `module_hr_presence` Boolean “Advanced Presence Control”
- `module_hr_skills` Boolean “Skills Management”
- `hr_presence_control_login` Boolean (related=company_id.hr_presence_control_login)
- `hr_presence_control_email` Boolean (related=company_id.hr_presence_control_email)
- `hr_presence_control_ip` Boolean (related=company_id.hr_presence_control_ip)
- `hr_presence_control_attendance` Boolean (related=company_id.hr_presence_control_attendance)
- `hr_presence_control_email_amount` Integer (related=company_id.hr_presence_control_email_amount)
- `hr_presence_control_ip_list` Char (related=company_id.hr_presence_control_ip_list)
- `contract_expiration_notice_period` Integer “Contract Expiry Notice Period” (related=company_id.contract_expiration_notice_period)
- `work_permit_expiration_notice_period` Integer “Work Permit Expiry Notice Period” (related=company_id.work_permit_expiration_notice_period)

Public methods: `set_values`

## `res.partner` (extends)

- `employee_ids` One2many → `hr.employee` “Employees”
- `employees_count` Integer (compute=_compute_employees_count)
- `employee` Boolean (store, compute=_compute_employee)

Public methods: `action_open_employees`

Extension points: `_action_show`, `_get_all_addr`

## `res.partner.bank` (extends)

- `employee_id` Many2many → `hr.employee` (compute=_compute_employee_id)
- `employee_salary_amount` Float “Salary Allocation” (readonly, compute=_compute_salary_amount)
- `employee_salary_amount_is_percentage` Boolean (readonly, compute=_compute_salary_amount)
- `currency_symbol` Char (related=employee_id.currency_id.symbol)
- `employee_has_multiple_bank_accounts` Boolean (related=employee_id.has_multiple_bank_accounts)

Public methods: `action_open_allocation_wizard`

## `res.users` (extends)

- `employee_ids` One2many → `hr.employee` “Related employee”
- `all_employee_ids` One2many → `hr.employee` “Related employees from all companies”
- `employee_public_ids` One2many → `hr.employee.public` “Related employee (public)” (readonly)
- `employee_id` Many2one → `hr.employee` “Company employee” (readonly, compute=_compute_company_employee)
- `department_id` Many2one “Department” (related=employee_id.department_id)
- `job_title` Char
- `work_phone` Char
- `mobile_phone` Char
- `work_email` Char
- `category_ids` Many2many → `hr.employee.category`
- `work_contact_id` Many2one → `res.partner`
- `work_location_id` Many2one → `hr.work.location`
- `work_location_name` Char (related=employee_id.work_location_name)
- `work_location_type` Selection (related=employee_id.work_location_type)
- `private_street` Char
- `private_street2` Char
- `private_city` Char
- `private_state_id` Many2one → `res.country.state`
- `private_zip` Char
- `private_country_id` Many2one → `res.country`
- `private_phone` Char
- `private_email` Char
- `km_home_work` Integer
- `employee_bank_account_ids` Many2many → `res.partner.bank`
- `emergency_contact` Char
- `emergency_phone` Char
- `visa_expire` Date
- `additional_note` Text
- `barcode` Char
- `pin` Char
- `employee_count` Integer (compute=_compute_employee_count)
- `employee_resource_calendar_id` Many2one “Employee's Working Hours” (readonly, related=employee_id.resource_calendar_id)
- `bank_account_ids` Many2many → `res.partner.bank`
- `birthday` Date
- `birthday_public_display` Boolean
- `create_employee` Boolean “Technical field, whether to create an employee”
- `create_employee_id` Many2one → `hr.employee` “Technical field, bind user to this employee on create”
- `is_system` Boolean (compute=_compute_is_system)
- `is_hr_user` Boolean (compute=_compute_is_hr_user)
- `monday_location_id` Many2one → `hr.work.location`
- `tuesday_location_id` Many2one → `hr.work.location`
- `wednesday_location_id` Many2one → `hr.work.location`
- `thursday_location_id` Many2one → `hr.work.location`
- `friday_location_id` Many2one → `hr.work.location`
- `saturday_location_id` Many2one → `hr.work.location`
- `sunday_location_id` Many2one → `hr.work.location`

Public methods: `action_create_employee`, `action_get`, `action_open_employees`, `action_related_contact`, `create`, `get_record_default_action`, `write`

Extension points: `_get_employee_fields_to_sync`, `_get_personal_info_partner_ids_to_notify`, `_post_model_setup__`

## `resource.resource` (extends)

- `user_id` Many2one
- `employee_id` One2many → `hr.employee`
- `tz` Selection (store, compute=_compute_tz)
- `job_title` Char (compute=_compute_job_title)
- `department_id` Many2one → `hr.department` (compute=_compute_department_id)
- `work_location_id` Many2one (related=employee_id.work_location_id)
- `work_email` Char (related=employee_id.work_email)
- `work_phone` Char (related=employee_id.work_phone)
- `show_hr_icon_display` Boolean (related=employee_id.show_hr_icon_display)
- `hr_icon_display` Selection (related=employee_id.hr_icon_display)
- `calendar_id` Many2one

Extension points: `_get_calendar_data_at`, `_get_calendars_validity_within_period`, `_get_contracts_valid_periods`, `_get_flexible_resources_calendars_validity_within_period`, `_get_resource_without_contract`

## `resource.calendar` (extends)

- `version_ids` One2many → `hr.version` (readonly)
- `employees_count` Integer “Employees Count” (compute=_compute_employees_count)
- `material_resources_count` Integer “Material Resources Count” (compute=_compute_material_resources_count)

Public methods: `action_duplicate_and_apply_to_employee`, `action_view_employees`, `transfer_leaves_to`, `write`

Extension points: `_check_company_id`

## `resource.calendar.leaves` (extends)


## `publisher_warranty.contract` (extends)


Extension points: `_get_message`

## `hr.manager.department.report` (defines)

Hr Manager Department Report

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `has_department_manager_access` Boolean (compute=_compute_has_department_manager_access)

## `hr.bank.account.allocation.wizard.line` (defines)

Bank Account Allocation Line (Wizard)

- `wizard_id` Many2one → `hr.bank.account.allocation.wizard` (required)
- `bank_account_id` Many2one → `res.partner.bank` (required, readonly)
- `account_number` Char (readonly, related=bank_account_id.account_number)
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

## `hr.employee.create.version.wizard` (defines)

Create New Employee Version Wizard

- `date_version` Date “Start Date” (required)
- `employee_count` Integer (readonly, compute=_compute_employee_count)

Public methods: `action_create_versions`

## `mail.activity.schedule` (extends)

- `department_id` Many2one → `hr.department` (compute=_compute_department_id)
- `plan_department_filterable` Boolean (compute=_compute_plan_department_filterable)
