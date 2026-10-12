# hr_holidays — Time Off

Depends on: hr_work_entry, hr_calendar, resource.

## `calendar.event` (extends)


## `hr.department` (extends)

- `absence_of_today` Integer “Absence by Today” (compute=_compute_leave_count)
- `leave_to_approve_count` Integer “Time Off to Approve” (compute=_compute_leave_count)
- `allocation_to_approve_count` Integer “Allocation to Approve” (compute=_compute_leave_count)

Public methods: `action_open_allocation_department`, `action_open_leave_department`

Extension points: `_get_action_context`

## `hr.employee` (extends)

- `leave_manager_id` Many2one → `res.users` “Time Off Approver” (store, compute=_compute_leave_manager)
- `current_work_entry_type_id` Many2one → `hr.work.entry.type` “Current Time Type” (compute=_compute_current_work_entry_type_id)
- `current_leave_state` Selection “Current Time Off Status” (compute=_compute_leave_status)
- `leave_date_from` Date “From Date” (compute=_compute_leave_status)
- `leave_date_to` Date “To Date” (compute=_compute_leave_status)
- `allocation_count` Float “Total number of days allocated.” (compute=_compute_allocation_count)
- `allocations_count` Integer “Total number of allocations” (compute=_compute_allocation_count)
- `show_leaves` Boolean “Able to see Remaining Time Off” (compute=_compute_show_leaves)
- `is_absent` Boolean “Absent Today” (compute=_compute_leave_status)
- `allocation_display` Char (compute=_compute_allocation_remaining_display)
- `allocation_remaining_display` Char (compute=_compute_allocation_remaining_display)
- `hr_icon_display` Selection
- `member_of_department` Boolean “Member of Department” (compute=_compute_member_of_department)
- `hr_responsible_id` Many2one
- `leave_ids` One2many → `hr.leave`

Public methods: `action_time_off_dashboard`, `create`, `get_allocations_number`, `get_mandatory_days`, `get_mandatory_days_data`, `get_public_holidays_data`, `get_special_days_data`, `get_time_off_dashboard_data`, `write`

Extension points: `_get_consumed_leaves`, `_get_contextual_employee`, `_get_first_working_interval_batch`, `_get_hours_for_date`, `_get_hours_per_day`, `_get_leave_manager_domain`, `_get_mandatory_days`, `_get_public_holidays`, `_get_user_m2o_to_empty_on_archived_employees`

## `hr.employee.departure` (extends)


Public methods: `action_register`

Extension points: `_check_refuse_future_leaves_condition`

## `hr.employee.public` (extends)

- `leave_manager_id` Many2one → `res.users` “Time Off Approver” (store, compute=_compute_leave_manager)
- `leave_date_to` Date “To Date” (compute=_compute_leave_status)
- `show_leaves` Boolean “Able to see Remaining Time Off” (compute=_compute_show_leaves)
- `is_absent` Boolean “Absent Today” (compute=_compute_leave_status)
- `allocation_display` Char (compute=_compute_allocation_display)
- `allocation_remaining_display` Char (related=employee_id.allocation_remaining_display)

Public methods: `action_open_time_off_calendar`, `action_time_off_dashboard`

## `hr.leave` (defines)

Time Off

Inherits: `mail.thread.main.attachment`, `mail.activity.mixin`, `hr.leave.display.name.mixin`, `hr.time.rule.source.mixin`

- `name` Char “Description” (compute=_compute_description)
- `private_name` Char “Time Off Description”
- `state` Selection “Status” (store)
- `user_id` Many2one → `res.users` “User” (readonly, store, index, related=employee_id.user_id)
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type” (required, index)
- `allowed_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_allowed_work_entry_type_ids)
- `work_entry_type_requires_allocation` Boolean (related=work_entry_type_id.requires_allocation)
- `count_as` Selection (related=work_entry_type_id.count_as)
- `color` Integer “Color” (related=work_entry_type_id.color)
- `validation_type` Selection “Validation Type” (related=work_entry_type_id.leave_validation_type)
- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `employee_company_id` Many2one “Employee Company” (store, related=employee_id.company_id)
- `company_id` Many2one → `res.company` (store, index, compute=_compute_company_id)
- `active_employee` Boolean “Employee Active” (related=employee_id.active)
- `tz_mismatch` Boolean (compute=_compute_tz_mismatch)
- `tz` Selection (compute=_compute_tz)
- `department_id` Many2one → `hr.department` “Department” (store, compute=_compute_department_id)
- `notes` Text “Reasons”
- `resource_calendar_id` Many2one → `resource.calendar` (store, compute=_compute_resource_calendar_id)
- `max_leaves` Float (compute=_compute_leaves)
- `virtual_remaining_leaves` Float “Available Time Off” (compute=_compute_leaves)
- `date_from` Datetime “Start Date” (store, index, compute=_compute_date_from_to)
- `date_to` Datetime “End Date” (store, compute=_compute_date_from_to)
- `number_of_days` Float “Duration (Days)” (store, compute=_compute_duration)
- `number_of_hours` Float “Duration (Hours)” (store, compute=_compute_duration)
- `last_several_days` Boolean “All day” (compute=_compute_last_several_days)
- `duration_display` Char “Requested” (compute=_compute_duration_display)
- `meeting_id` Many2one → `calendar.event` “Meeting”
- `first_approver_id` Many2one → `hr.employee` “First Approval” (readonly)
- `second_approver_id` Many2one → `hr.employee` “Second Approval” (readonly)
- `can_approve` Boolean (compute=_compute_can_approve)
- `can_validate` Boolean (compute=_compute_can_validate)
- `can_refuse` Boolean (compute=_compute_can_refuse)
- `can_cancel` Boolean (compute=_compute_can_cancel)
- `can_back_to_approve` Boolean (compute=_compute_can_back_to_approve)
- `can_reschedule` Boolean (compute=_compute_can_reschedule)
- `attachment_ids` One2many → `ir.attachment` “Attachments”
- `supported_attachment_ids` Many2many → `ir.attachment` “Attach File” (compute=_compute_supported_attachment_ids)
- `supported_attachment_ids_count` Integer (compute=_compute_supported_attachment_ids)
- `attachment_is_visible` Boolean (compute=_compute_attachment_is_visible)
- `work_entry_type_request_unit` Selection (readonly, related=work_entry_type_id.request_unit)
- `work_entry_type_support_document` Boolean (related=work_entry_type_id.support_document)
- `request_date_from` Date “Request Start Date”
- `request_date_to` Date “Request End Date”
- `request_hour_from` Float “Hour from”
- `request_hour_to` Float “Hour to”
- `request_date_hour_from` Datetime (compute=_compute_request_date_hour_from)
- `request_date_hour_to` Datetime (compute=_compute_request_date_hour_to)
- `request_date_from_period` Selection “Date Period Start”
- `request_date_to_period` Selection “Date Period End”
- `is_hatched` Boolean “Hatched” (compute=_compute_is_hatched)
- `is_striked` Boolean “Striked” (compute=_compute_is_hatched)
- `has_mandatory_day` Boolean (compute=_compute_has_mandatory_day)
- `work_entry_type_increases_duration` Char (compute=_compute_work_entry_type_increases_duration)
- `request_duration` Selection “Duration”
- `allowed_request_durations` Json (compute=_compute_allowed_request_durations)
- `dashboard_warning_message` Char (compute=_compute_dashboard_warning_message)
- `allocation_display_warning` Char (compute=_compute_allocation_warning)
- `time_rule_id` Many2one → `hr.time.rule` “Time Rule” (index)
- `source_leave_id` Many2one → `hr.leave` “Source Leave” (index)
- `output_leave_ids` One2many → `hr.leave`
- `is_time_rule_trimmed` Boolean “Trimmed by Time Rule”
- `time_rule_time_range` Char (compute=_compute_time_rule_time_range)

Public methods: `action_approve`, `action_back_to_approval`, `action_cancel`, `action_documents`, `action_open_employee_calendar`, `action_refuse`, `activity_update`, `add_follower`, `copy_data`, `create`, `default_get`, `get_unusual_days`, `message_subscribe`, `onchange`, `open_pending_requests`, `reschedule_from_calendar`, `unlink`, `write`

Extension points: `_action_user_cancel`, `_action_validate`, `_check_approval_update`, `_check_contracts`, `_check_date`, `_check_date_state`, `_check_double_validation_rules`, `_check_executive_employee_type`, `_check_max_absence_per_day`, `_check_validity`, `_create_leaves_from_split`, `_create_resource_leave`, `_get_allowed_request_durations`, `_get_calendar_days`, `_get_calendar_days_between_leaves`, `_get_durations`, `_get_employee_domain`, `_get_extra_default_leave_values_for_split`, `_get_generated_leave_domain`, `_get_hour_from_to`, `_get_leaves_on_public_holiday`, `_get_max_allowed_absence_hours`, `_get_next_states_by_state`, `_get_overlapping_contracts`, `_get_pipeline_intervals_local`, `_get_request_date_hours`, `_get_request_date_to`, `_get_request_date_to_with_period`, `_get_request_duration`, `_get_request_vals_from_date_hours`, `_get_responsible_for_approval`, `_get_search_request_date_hour_from_to_domain`, `_get_source_extra_fields_domain`, `_get_split_hour_vals`, `_get_time_rule_deficit_occupied`, `_get_time_rule_end_write_vals`, `_get_time_rule_output_vals`, `_get_time_rule_remainder_vals`, `_get_to_clean_activities`, `_get_work_entry_type_change_warning`, `_get_write_source_extra_source_fields`, `_post_leave_cancel`, `_prepare_holidays_meeting_values`, `_prepare_leave_unlink`, `_prepare_resource_leave_vals`

## `hr.leave.accrual.plan` (defines)

Accrual Plan

- `active` Boolean
- `name` Char “Name” (required)
- `employees_count` Integer “Employees” (compute=_compute_employee_count)
- `level_ids` One2many → `hr.leave.accrual.level` “Milestones”
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type”
- `allowed_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_allowed_work_entry_type_ids)
- `allocation_ids` One2many → `hr.leave.allocation`
- `company_id` Many2one → `res.company` “Company”
- `transition_mode` Selection (required)
- `show_transition_mode` Boolean (compute=_compute_show_transition_mode)
- `is_based_on_worked_time` Boolean (store, compute=_compute_is_based_on_worked_time)
- `accrued_gain_time` Selection (required)
- `can_be_carryover` Boolean
- `carryover_date` Selection “Carry-Over Time” (required)
- `carryover_day` Selection (store, compute=_compute_carryover_day)
- `carryover_month` Selection
- `added_value_type` Selection (store)
- `level_count` Integer “Levels” (compute=_compute_level_count)

Public methods: `action_create_accrual_plan_level`, `action_open_accrual_plan_employees`, `action_open_accrual_plan_level`, `create`

## `hr.leave.accrual.level` (defines)

Accrual Plan Level

- `sequence` Integer “sequence” (store, compute=_compute_sequence)
- `accrual_plan_id` Many2one → `hr.leave.accrual.plan` (required, index)
- `accrued_gain_time` Selection (related=accrual_plan_id.accrued_gain_time)
- `is_based_on_worked_time` Boolean (related=accrual_plan_id.is_based_on_worked_time)
- `start_count` Integer
- `start_type` Selection (required)
- `milestone_date` Selection (required, store, compute=_compute_milestone_date)
- `added_value` Float (required)
- `added_value_type` Selection (required, store, compute=_compute_added_value_type)
- `frequency` Selection “Frequency” (required)
- `week_day` Selection “Allocation on” (required)
- `first_day` Selection
- `second_day` Selection
- `first_month_day` Selection (store, compute=_compute_first_month_day)
- `first_month` Selection
- `second_month_day` Selection (store, compute=_compute_second_month_day)
- `second_month` Selection
- `yearly_month` Selection
- `yearly_day` Selection (store, compute=_compute_yearly_day)
- `cap_accrued_time` Boolean
- `maximum_leave` Float (store, compute=_compute_maximum_leave)
- `cap_accrued_time_yearly` Boolean (store)
- `maximum_leave_yearly` Float
- `can_be_carryover` Boolean (readonly, related=accrual_plan_id.can_be_carryover)
- `action_with_unused_accruals` Selection (required, store, compute=_compute_action_with_unused_accruals)
- `carryover_options` Selection (required, store, compute=_compute_carryover_options)
- `max_carriedover_duration` Integer
- `can_modify_value_type` Boolean (compute=_compute_can_modify_value_type)
- `accrual_validity` Boolean (store, compute=_compute_accrual_validity)
- `accrual_validity_count` Integer
- `accrual_validity_type` Selection (required)
- `yearly_gain` Float (compute=_compute_yearly_gain)

Public methods: `action_save_new`

Extension points: `_check_dates`, `_check_maximum_leaves`, `_get_hourly_frequencies`, `_get_level_transition_date`, `_get_next_date`, `_get_previous_date`, `_get_start_date`

## `hr.leave.allocation` (defines)

Time Off Allocation

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Description” (store, compute=_compute_description)
- `is_name_custom` Boolean (readonly)
- `name_validity` Char “Description with validity” (compute=_compute_description_validity)
- `state` Selection “Status” (readonly)
- `date_from` Date “Start Date” (required, index)
- `date_to` Date “End Date”
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type” (required, store, index, compute=_compute_work_entry_type_id)
- `allowed_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_allowed_work_entry_type_ids)
- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `employee_company_id` Many2one (readonly, store, related=employee_id.company_id)
- `active_employee` Boolean “Active Employee” (readonly, related=employee_id.active)
- `manager_id` Many2one → `hr.employee` “Manager” (store, compute=_compute_manager_id)
- `notes` Text “Reasons”
- `number_of_days` Float “Number of Days”
- `number_of_days_display` Float “Duration (days)” (compute=_compute_number_of_days_display)
- `number_of_hours` Float “Duration (hours)” (store, compute=_compute_number_of_hours)
- `duration_display` Char “Allocated (Days/Hours)” (compute=_compute_duration_display)
- `approver_id` Many2one → `hr.employee` “First Approval” (readonly)
- `second_approver_id` Many2one → `hr.employee` “Second Approval” (readonly)
- `validation_type` Selection “Validation Type” (readonly, related=work_entry_type_id.allocation_validation_type)
- `can_approve` Boolean “Can Approve” (compute=_compute_can_approve)
- `can_validate` Boolean “Can Validate” (compute=_compute_can_validate)
- `can_refuse` Boolean “Can Refuse” (compute=_compute_can_refuse)
- `type_request_unit` Selection (compute=_compute_type_request_unit)
- `department_id` Many2one → `hr.department` “Department” (store, compute=_compute_department_id)
- `is_officer` Boolean (compute=_compute_is_officer)
- `max_leaves` Float (compute=_compute_leaves)
- `leaves_taken` Float “Time off Taken” (compute=_compute_leaves)
- `virtual_remaining_leaves` Float “Available Time Off” (compute=_compute_leaves)
- `accrual_plan_id` Many2one → `hr.leave.accrual.plan`
- `hide_accrual_plan_id` Boolean (compute=_compute_hide_accrual_plan_id)
- `last_accrual` Date “Date of the last accrual allocation”
- `lastcall` Date “Date of the last executed accrual event (accrual, carryover date, expiring carriedover days, ...)”
- `nextcall` Date “Date of the closest next accrual event (accrual, carryover date, expiring carriedover days, ...)”
- `yearly_accrued_days` Float “Number of accrued days since the last carryover”
- `previous_carryover_number_of_days` Float “The number of days on previous carryover date”
- `carried_over_days_expiration_date` Date “Carried over days expiration date”

Public methods: `action_approve`, `action_refuse`, `activity_update`, `add_follower`, `copy`, `create`, `default_get`, `message_subscribe`, `onchange`, `write`

Extension points: `_action_validate`, `_check_accrual_plan_id`, `_check_accrual_plan_work_entry_type`, `_check_approval_update`, `_check_date_from_date_to`, `_check_negative_allocation`, `_get_accrual_allocation_data`, `_get_accrual_plan_level_work_entry_prorata`, `_get_additionnal_future_leaves_on`, `_get_current_accrual_plan_level_idx`, `_get_current_accrual_plan_level_idx_for_accrual`, `_get_current_accrual_plan_levels`, `_get_days_after_expiration`, `_get_employee_hours_per_day`, `_get_init_accrual_plan_values`, `_get_lvls_boundaries`, `_get_next_carryover_date`, `_get_next_lvl_start`, `_get_next_states_by_state`, `_get_period_added_duration`, `_get_request_unit`, `_get_responsible_for_approval`, `_get_title`, `_get_to_update_accrual_allocations`

## `hr.leave.display.name.mixin` (defines)

Leave Display Name Mixin


Extension points: `_get_leave_display_date`, `_get_leave_duration_display`

## `hr.leave.mandatory.day` (defines)

Mandatory Day

- `name` Char (required)
- `company_id` Many2one → `res.company` (required)
- `start_date` Date (required)
- `end_date` Date (required)
- `color` Integer
- `resource_calendar_id` Many2one → `resource.calendar`
- `department_ids` Many2many → `hr.department` “Departments”
- `job_ids` Many2many → `hr.job` “Job Position”

## `hr.time.rule.source.mixin` (extends)


## `hr.time.rule` (extends)

- `work_entry_type_id` Many2one
- `leave_compensation_rate` Float “Allocate %”
- `allocation_type_id` Many2one → `hr.work.entry.type` “Allocate to”

Extension points: `_get_output_leave_merge_key`, `_get_output_leave_vals`

## `hr.time.rule.allocation.log` (defines)

Time Rule Allocation Credit Log

- `res_model` Char “Model” (required)
- `res_id` Many2oneReference “Record” (required)
- `allocation_id` Many2one → `hr.leave.allocation` (required, index)
- `days` Float (required)

## `hr.version` (extends)

Employee Contract

- `hr_responsible_id` Many2one
- `allocation_from_working_schedule_id` Many2one → `hr.leave.allocation` “Allocation from working schedule”

Public methods: `create`, `write`

Extension points: `_action_trigger_accrual_plan_working_schedule`, `_check_contracts`, `_check_overlapping_contract`, `_create_all_new_leave`, `_get_hr_responsible_domain`, `_get_interval_leave_work_entry_type`, `_get_leave_work_entry_type`, `_get_leaves`, `_get_leaves_from_vals`, `_get_more_vals_leave_interval`, `_get_sub_leave_domain`, `_get_work_entry_source_fields`

## `hr.work.entry.type` (extends)

- `create_calendar_meeting` Boolean “Display Time Off in Calendar”
- `color` Integer “Color”
- `hide_on_dashboard` Boolean “Hide On Dashboard”
- `max_leaves` Float “Maximum Allowed” (compute=_compute_leaves)
- `leaves_taken` Float “Time off Already Taken” (compute=_compute_leaves)
- `virtual_remaining_leaves` Float “Virtual Remaining Time Off” (compute=_compute_leaves)
- `allocation_count` Integer “Allocations” (compute=_compute_allocation_count)
- `group_days_leave` Float “Group Time Off” (compute=_compute_group_days_leave)
- `is_used` Boolean (compute=_compute_is_used)
- `country_id` Many2one → `res.country` “Country”
- `country_code` Char (readonly, related=country_id.code)
- `leave_validation_type` Selection “Time Off Validation”
- `requires_allocation` Boolean “Requires Allocation” (required)
- `employee_requests` Boolean “Allow Employee Requests” (required)
- `allocation_validation_type` Selection “Approval”
- `has_valid_allocation` Boolean (compute=_compute_valid)
- `request_unit` Selection “Duration Type” (required)
- `unit_of_measure` Selection “Unit” (required)
- `unpaid` Boolean “Is Unpaid”
- `include_public_holidays_in_duration` Boolean “Ignore Public Holidays”
- `leave_notif_subtype_id` Many2one → `mail.message.subtype` “Time Off Notification Subtype”
- `allocation_notif_subtype_id` Many2one → `mail.message.subtype` “Allocation Notification Subtype”
- `support_document` Boolean “Supporting Document Expected”
- `allow_request_on_top` Boolean “Allow Request on Top”
- `elligible_for_accrual_rate` Boolean “Eligible for Accrual Rate” (store, compute=_compute_eligible_for_accrual_rate)
- `count_days_as` Selection “Count Days as”
- `allows_negative` Boolean “Allow Negative”
- `max_allowed_negative` Integer “Maximum Excess Amount”
- `time_off_selectable` Boolean “Selectable in Time Off”

Public methods: `action_see_days_allocated`, `action_see_group_leaves`, `check_allocation_requirement_edit_validity`, `get_allocation_data`, `get_allocation_data_request`, `get_work_entry_types_with_valid_allocations`, `has_accrual_allocation`, `has_future_allocation`, `requested_display_name`

Extension points: `_check_allow_request_on_top`, `_check_elligible_for_accrual_rate`, `_check_leaves_for_count_days_as`, `_check_overlapping_public_holidays`, `_get_carried_over_days_expiration_data`, `_get_closest_expiring_leaves_date_and_count`

## `mail.activity.type` (extends)


Extension points: `_get_model_info_by_xmlid`

## `mail.message.subtype` (extends)


Public methods: `create`, `write`

Extension points: `_get_department_subtype`

## `res.company` (extends)


Public methods: `create`

Extension points: `_check_country_change_holidays`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.partner` (extends)

- `leave_date_to` Date (compute=_compute_leave_date_to)

## `res.users` (extends)

- `leave_date_to` Date

Public methods: `create`

## `resource.calendar` (extends)

- `associated_leaves_count` Integer “Time Off Count” (compute=_compute_associated_leaves_count)
- `leave_accrual_plan_id` Many2one → `hr.leave.accrual.plan` “Accrual Plan”

Public methods: `action_open_public_holidays`

## `resource.calendar.leaves` (extends)

- `holiday_id` Many2one → `hr.leave` “Time Off Request”
- `elligible_for_accrual_rate` Boolean “Eligible for Accrual Rate”

Public methods: `create`, `load_public_holidays`, `unlink`, `write`

Extension points: `_check_compare_dates`, `_get_domain`, `_get_time_domain_dict`, `_prepare_public_holidays_data`

## `resource.resource` (extends)

- `leave_date_to` Date (related=user_id.leave_date_to)

## `report.hr_holidays.report_holidayssummary` (defines)

Holidays Summary Report


Extension points: `_get_data_from_report`, `_get_day`, `_get_employees`, `_get_header_info`, `_get_holidays_status`, `_get_leaves`, `_get_leaves_summary`, `_get_months`, `_get_report_values`

## `hr.leave.employee.report` (defines)

Time Off Per Employee Summary / Report

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `leave_id` Many2one → `hr.leave` “Time Off Request” (readonly)
- `working_schedule_aligned_date_from` Datetime “Date From” (readonly, store)
- `number_of_days` Float (readonly, store, compute=_compute_leave_duration)
- `number_of_hours` Float (readonly, store, compute=_compute_leave_duration)
- `description` Char
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type”
- `state` Selection
- `color` Integer “Color” (related=work_entry_type_id.color)

Extension points: `_create_report_records_from_leave_records`

## `hr.leave.employee.type.report` (defines)

Time Off Summary / Report

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `active_employee` Boolean (readonly)
- `number_of_days` Float “Number of Days” (readonly)
- `number_of_hours` Float “Number of Hours” (readonly)
- `department_id` Many2one → `hr.department` “Department” (readonly)
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type” (readonly)
- `holiday_status` Selection
- `state` Selection “Status” (readonly)
- `date_from` Datetime “Start Date” (readonly)
- `date_to` Datetime “End Date” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)

Public methods: `action_time_off_analysis`, `init`

## `hr.leave.report` (defines)

Time Off Summary / Report

Inherits: `hr.manager.department.report`

- `leave_id` Many2one → `hr.leave` “Time Off Request” (readonly)
- `allocation_id` Many2one → `hr.leave.allocation` “Allocation Request” (readonly)
- `name` Char “Description” (readonly)
- `number_of_days` Float “Number of Days” (readonly)
- `number_of_hours` Float “Number of Hours” (readonly)
- `leave_type` Selection “Request Type” (readonly)
- `department_id` Many2one → `hr.department` “Department” (readonly)
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type” (readonly)
- `state` Selection “Status” (readonly)
- `date_from` Datetime “Start Date” (readonly)
- `date_to` Datetime “End Date” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)

Public methods: `action_open_record`, `init`

## `hr.leave.report.calendar` (defines)

Time Off Calendar

Inherits: `hr.leave.display.name.mixin`

- `name` Char “Name” (readonly, compute=_compute_name)
- `request_date_from` Date “Request Start Date” (readonly)
- `request_date_to` Date “Request End Date” (readonly)
- `request_date_hour_from` Datetime (compute=_compute_request_date_hours)
- `request_date_hour_to` Datetime (compute=_compute_request_date_hours)
- `duration_display` Char (readonly, related=leave_id.duration_display)
- `tz` Selection “Timezone” (readonly)
- `duration` Float “Duration” (readonly)
- `employee_id` Many2one → `hr.employee` (required, readonly)
- `user_id` Many2one → `res.users` (readonly)
- `department_id` Many2one → `hr.department` (readonly)
- `job_id` Many2one → `hr.job` (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `state` Selection (readonly)
- `description` Char “Description” (readonly)
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type” (readonly)
- `is_hatched` Boolean “Hatched” (readonly)
- `is_striked` Boolean “Striked” (readonly)
- `is_absent` Boolean (related=employee_id.is_absent)
- `member_of_department` Boolean (related=employee_id.member_of_department)
- `leave_manager_id` Many2one (related=employee_id.leave_manager_id)
- `leave_id` Many2one → `hr.leave` (readonly)
- `is_manager` Boolean “Manager” (compute=_compute_is_manager)

Public methods: `action_approve`, `action_refuse`, `get_unusual_days`, `init`

## `hr.holidays.cancel.leave` (defines)

Cancel Time Off Wizard

- `leave_id` Many2one → `hr.leave` “Time Off Request” (required)
- `reason` Text

Public methods: `action_cancel_leave`

## `hr.holidays.summary.employee` (defines)

HR Time Off Summary Report By Employee

- `date_from` Date “From” (required)
- `emp` Many2many → `hr.employee` “Employee(s)”
- `holiday_type` Selection “Select Time Type” (required)

Public methods: `print_report`

## `hr.leave.allocation.generate.multi.wizard` (defines)

Generate time off allocations for multiple employees

Inherits: `hr.mixin`

- `name` Char “Description” (store, compute=_compute_name)
- `duration` Float “Allocation”
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type” (required)
- `allowed_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_allowed_work_entry_type_ids)
- `unit_of_measure` Selection (related=work_entry_type_id.unit_of_measure)
- `employee_ids` Many2many → `hr.employee` “Employees”
- `company_id` Many2one → `res.company` (required)
- `accrual_plan_id` Many2one → `hr.leave.accrual.plan`
- `date_from` Date “Start Date” (required)
- `date_to` Date “End Date”
- `notes` Text “Reasons”

Public methods: `action_generate_allocations`

Extension points: `_get_employee_domain`, `_get_title`, `_prepare_allocation_values`

## `hr.leave.generate.multi.wizard` (defines)

Generate time off for multiple employees

Inherits: `hr.mixin`

- `name` Char “Description”
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type” (required)
- `allowed_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_allowed_work_entry_type_ids)
- `employee_ids` Many2many → `hr.employee` “Employees”
- `company_id` Many2one → `res.company` (required)
- `date_from` Date “Start Date” (required)
- `date_to` Date “End Date” (required)
- `hour_from` Float “Hour from”
- `hour_to` Float “Hour to”
- `work_entry_type_request_unit` Selection (related=work_entry_type_id.request_unit)
- `date_from_period` Selection “Date Period Start”
- `date_to_period` Selection “Date Period End”
- `valid_work_entry_type_ids` Many2many → `hr.work.entry.type` (compute=_compute_valid_work_entry_type_ids)

Public methods: `action_generate_time_off`

Extension points: `_get_employee_domain`, `_prepare_employees_holiday_values`

## `load.public.holiday.wizard` (defines)

Public Holiday Preview Wizard

- `year` Integer (required)
- `warning_message` Html (compute=_compute_warning_message)
- `line_ids` One2many → `load.public.holiday.wizard.line` “Public Holidays” (store, compute=_compute_line_ids)

Public methods: `action_add_public_holidays`

Extension points: `_get_create_values_by_company`, `_get_warning_messages`

## `load.public.holiday.wizard.line` (defines)

Public Holiday Preview Wizard Line

- `name` Char (required)
- `wizard_id` Many2one → `load.public.holiday.wizard` (required)
- `start_date` Date (required)
- `company_id` Many2one → `res.company` (required)
- `work_entry_type_id` Many2one → `hr.work.entry.type` “Time Type” (store, compute=_compute_work_entry_type)
- `allowed_work_entry_type_ids` Many2many → `hr.work.entry.type` (store, compute=_compute_work_entry_type)
