# hr_holidays — Time Off

Depends on: hr, calendar, resource.

## `hr.department` (extends)

- `absence_of_today` Integer “Absence by Today” (compute=_compute_leave_count)
- `leave_to_approve_count` Integer “Time Off to Approve” (compute=_compute_leave_count)
- `allocation_to_approve_count` Integer “Allocation to Approve” (compute=_compute_leave_count)

Public methods: `action_open_allocation_department`, `action_open_leave_department`

Extension points: `_get_action_context`

## `hr.employee` (extends)

- `current_leave_id` Many2one → `hr.leave.type` “Current Time Off Type” (compute=_compute_current_leave)

Public methods: `action_time_off_dashboard`, `get_mandatory_days`, `get_mandatory_days_data`, `get_public_holidays_data`, `get_special_days_data`

Extension points: `_get_mandatory_days`, `_get_public_holidays`, `_get_user_m2o_to_empty_on_archived_employees`

## `hr.employee.base` (extends)

- `leave_manager_id` Many2one → `res.users` “Time Off” (store, compute=_compute_leave_manager)
- `remaining_leaves` Float “Remaining Paid Time Off” (compute=_compute_remaining_leaves)
- `current_leave_state` Selection “Current Time Off Status” (compute=_compute_leave_status)
- `leave_date_from` Date “From Date” (compute=_compute_leave_status)
- `leave_date_to` Date “To Date” (compute=_compute_leave_status)
- `leaves_count` Float “Number of Time Off” (compute=_compute_remaining_leaves)
- `allocation_count` Float “Total number of days allocated.” (compute=_compute_allocation_count)
- `allocations_count` Integer “Total number of allocations” (compute=_compute_allocation_count)
- `show_leaves` Boolean “Able to see Remaining Time Off” (compute=_compute_show_leaves)
- `is_absent` Boolean “Absent Today” (compute=_compute_leave_status)
- `allocation_display` Char (compute=_compute_allocation_remaining_display)
- `allocation_remaining_display` Char (compute=_compute_allocation_remaining_display)
- `hr_icon_display` Selection

Public methods: `create`, `write`

Extension points: `_get_consumed_leaves`, `_get_contextual_employee`, `_get_remaining_leaves`

## `hr.leave` (defines)

Time Off

Inherits: `mail.thread.main.attachment`, `mail.activity.mixin`

- `active` Boolean (readonly)
- `name` Char “Description” (compute=_compute_description)
- `private_name` Char “Time Off Description”
- `state` Selection “Status” (store, compute=_compute_state)
- `report_note` Text “HR Comments”
- `user_id` Many2one → `res.users` “User” (readonly, store, index, related=employee_id.user_id)
- `manager_id` Many2one → `hr.employee` (store, compute=_compute_from_employee_id)
- `is_user_only_responsible` Boolean (compute=_compute_is_user_only_responsible)
- `holiday_status_id` Many2one → `hr.leave.type` “Time Off Type” (required, store, compute=_compute_from_employee_id)
- `color` Integer “Color” (related=holiday_status_id.color)
- `validation_type` Selection “Validation Type” (related=holiday_status_id.leave_validation_type)
- `employee_id` Many2one → `hr.employee` “Employee” (store, index, compute=_compute_from_employee_ids)
- `employee_company_id` Many2one “Employee Company” (store, related=employee_id.company_id)
- `company_id` Many2one → `res.company` (store, compute=_compute_company_id)
- `active_employee` Boolean “Employee Active” (related=employee_id.active)
- `tz_mismatch` Boolean (compute=_compute_tz_mismatch)
- `tz` Selection (compute=_compute_tz)
- `department_id` Many2one → `hr.department` “Department” (store, compute=_compute_department_id)
- `notes` Text “Reasons”
- `resource_calendar_id` Many2one → `resource.calendar` (store, compute=_compute_resource_calendar_id)
- `date_from` Datetime “Start Date” (store, index, compute=_compute_date_from_to)
- `date_to` Datetime “End Date” (store, compute=_compute_date_from_to)
- `number_of_days` Float “Duration (Days)” (store, compute=_compute_duration)
- `number_of_hours` Float “Duration (Hours)” (store, compute=_compute_duration)
- `last_several_days` Boolean “All day” (compute=_compute_last_several_days)
- `number_of_days_display` Float “Duration in days” (compute=_compute_number_of_days_display)
- `number_of_hours_display` Float “Duration in hours” (readonly, compute=_compute_number_of_hours_display)
- `number_of_hours_text` Char (compute=_compute_number_of_hours_text)
- `duration_display` Char “Requested (Days/Hours)” (store, compute=_compute_duration_display)
- `meeting_id` Many2one → `calendar.event` “Meeting”
- `parent_id` Many2one → `hr.leave` “Parent”
- `linked_request_ids` One2many → `hr.leave` “Linked Requests”
- `holiday_type` Selection “Allocation Mode” (required)
- `employee_ids` Many2many → `hr.employee` “Employees” (readonly, store, compute=_compute_from_holiday_type)
- `multi_employee` Boolean (store, compute=_compute_from_employee_ids)
- `category_id` Many2one → `hr.employee.category` “Employee Tag” (store, compute=_compute_from_holiday_type)
- `mode_company_id` Many2one → `res.company` “Company Mode” (store, compute=_compute_from_holiday_type)
- `first_approver_id` Many2one → `hr.employee` “First Approval” (readonly)
- `second_approver_id` Many2one → `hr.employee` “Second Approval” (readonly)
- `can_reset` Boolean “Can reset” (compute=_compute_can_reset)
- `can_approve` Boolean “Can Approve” (compute=_compute_can_approve)
- `can_cancel` Boolean “Can Cancel” (compute=_compute_can_cancel)
- `attachment_ids` One2many → `ir.attachment` “Attachments”
- `supported_attachment_ids` Many2many → `ir.attachment` “Attach File” (compute=_compute_supported_attachment_ids)
- `supported_attachment_ids_count` Integer (compute=_compute_supported_attachment_ids)
- `all_employee_ids` Many2many → `hr.employee` (compute=_compute_all_employees)
- `leave_type_request_unit` Selection (readonly, related=holiday_status_id.request_unit)
- `leave_type_support_document` Boolean (related=holiday_status_id.support_document)
- `request_date_from` Date “Request Start Date”
- `request_date_to` Date “Request End Date”
- `request_hour_from` Selection “Hour from”
- `request_hour_to` Selection “Hour to”
- `request_date_from_period` Selection “Date Period Start”
- `request_unit_half` Boolean “Half Day” (store, compute=_compute_request_unit_half)
- `request_unit_hours` Boolean “Custom Hours” (store, compute=_compute_request_unit_hours)
- `is_hatched` Boolean “Hatched” (compute=_compute_is_hatched)
- `is_striked` Boolean “Striked” (compute=_compute_is_hatched)
- `has_mandatory_day` Boolean (compute=_compute_has_mandatory_day)
- `leave_type_increases_duration` Boolean (compute=_compute_leave_type_increases_duration)

Public methods: `action_approve`, `action_cancel`, `action_confirm`, `action_documents`, `action_draft`, `action_open_records`, `action_refuse`, `action_validate`, `activity_update`, `add_follower`, `copy_data`, `create`, `default_get`, `get_unusual_days`, `message_subscribe`, `onchange`, `unlink`, `write`

Extension points: `_action_user_cancel`, `_check_approval_update`, `_check_date`, `_check_date_state`, `_check_double_validation_rules`, `_check_mandatory_day`, `_check_validity`, `_create_resource_leave`, `_get_attendances`, `_get_duration`, `_get_employee_domain`, `_get_employees_from_holiday_type`, `_get_leaves_on_public_holiday`, `_get_mail_redirect_suggested_company`, `_get_responsible_for_approval`, `_prepare_employees_holiday_values`, `_prepare_holidays_meeting_values`, `_prepare_resource_leave_vals`

## `hr.leave.accrual.plan` (defines)

Accrual Plan

- `active` Boolean
- `name` Char “Name” (required)
- `time_off_type_id` Many2one → `hr.leave.type` “Time Off Type”
- `employees_count` Integer “Employees” (compute=_compute_employee_count)
- `level_ids` One2many → `hr.leave.accrual.level` “Milestone”
- `allocation_ids` One2many → `hr.leave.allocation`
- `company_id` Many2one → `res.company` “Company” (compute=_compute_company_id)
- `transition_mode` Selection “Milestone Transition” (required)
- `show_transition_mode` Boolean (compute=_compute_show_transition_mode)
- `is_based_on_worked_time` Boolean “Based on worked time” (store, compute=_compute_is_based_on_worked_time)
- `accrued_gain_time` Selection (required)
- `carryover_date` Selection “Carry-Over Time” (required)
- `carryover_day` Integer
- `carryover_day_display` Selection (compute=_compute_carryover_day_display)
- `carryover_month` Selection
- `added_value_type` Selection (store, compute=_compute_added_value_type)
- `level_count` Integer “Levels” (compute=_compute_level_count)

Public methods: `action_open_accrual_plan_employees`, `copy`

## `hr.leave.accrual.level` (defines)

Accrual Plan Level

- `sequence` Integer “sequence” (store, compute=_compute_sequence)
- `accrual_plan_id` Many2one → `hr.leave.accrual.plan` (required)
- `accrued_gain_time` Selection (related=accrual_plan_id.accrued_gain_time)
- `start_count` Integer “Start after”
- `start_type` Selection “ ” (required)
- `added_value` Float “Rate” (required)
- `added_value_type` Selection (required, store, compute=_compute_added_value_type)
- `frequency` Selection “Frequency” (required)
- `week_day` Selection “Allocation on” (required)
- `first_day` Integer
- `first_day_display` Selection (compute=_compute_days_display)
- `second_day` Integer
- `second_day_display` Selection (compute=_compute_days_display)
- `first_month_day` Integer
- `first_month_day_display` Selection (compute=_compute_days_display)
- `first_month` Selection
- `second_month_day` Integer
- `second_month_day_display` Selection (compute=_compute_days_display)
- `second_month` Selection
- `yearly_month` Selection
- `yearly_day` Integer
- `yearly_day_display` Selection (compute=_compute_days_display)
- `cap_accrued_time` Boolean “Cap accrued time”
- `maximum_leave` Float “Limit to” (store, compute=_compute_maximum_leave)
- `action_with_unused_accruals` Selection “Carry over” (required)
- `postpone_max_days` Integer “Maximum amount of accruals to transfer”
- `can_modify_value_type` Boolean (compute=_compute_can_modify_value_type)

Extension points: `_check_maximum_leave`, `_get_level_transition_date`, `_get_next_date`, `_get_previous_date`

## `hr.leave.allocation` (defines)

Time Off Allocation

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Description” (compute=_compute_description)
- `name_validity` Char “Description with validity” (compute=_compute_description_validity)
- `active` Boolean
- `private_name` Char “Allocation Description”
- `state` Selection “Status” (readonly)
- `date_from` Date “Start Date” (required, index)
- `date_to` Date “End Date”
- `holiday_status_id` Many2one → `hr.leave.type` “Time Off Type” (required, store, compute=_compute_holiday_status_id)
- `employee_id` Many2one → `hr.employee` “Employee” (store, index, compute=_compute_from_employee_ids)
- `employee_company_id` Many2one (readonly, store, related=employee_id.company_id)
- `active_employee` Boolean “Active Employee” (readonly, related=employee_id.active)
- `manager_id` Many2one → `hr.employee` “Manager” (store, compute=_compute_manager_id)
- `notes` Text “Reasons”
- `number_of_days` Float “Number of Days” (store, compute=_compute_from_holiday_status_id)
- `number_of_days_display` Float “Duration (days)” (compute=_compute_number_of_days_display)
- `number_of_hours_display` Float “Duration (hours)” (compute=_compute_number_of_hours_display)
- `duration_display` Char “Allocated (Days/Hours)” (compute=_compute_duration_display)
- `parent_id` Many2one → `hr.leave.allocation` “Parent”
- `linked_request_ids` One2many → `hr.leave.allocation` “Linked Requests”
- `approver_id` Many2one → `hr.employee` “First Approval” (readonly)
- `validation_type` Selection “Validation Type” (readonly, related=holiday_status_id.allocation_validation_type)
- `can_approve` Boolean “Can Approve” (compute=_compute_can_approve)
- `type_request_unit` Selection (compute=_compute_type_request_unit)
- `holiday_type` Selection “Allocation Mode” (required)
- `employee_ids` Many2many → `hr.employee` “Employees” (store, compute=_compute_from_holiday_type)
- `multi_employee` Boolean (store, compute=_compute_from_employee_ids)
- `mode_company_id` Many2one → `res.company` “Company Mode” (store, compute=_compute_from_holiday_type)
- `department_id` Many2one → `hr.department` “Department” (store, compute=_compute_department_id)
- `category_id` Many2one → `hr.employee.category` “Employee Tag” (store, compute=_compute_from_holiday_type)
- `lastcall` Date “Date of the last accrual allocation” (readonly)
- `nextcall` Date “Date of the next accrual allocation” (readonly)
- `already_accrued` Boolean
- `allocation_type` Selection “Allocation Type” (required, readonly)
- `is_officer` Boolean (compute=_compute_is_officer)
- `accrual_plan_id` Many2one → `hr.leave.accrual.plan` (store, compute=_compute_from_holiday_status_id)
- `max_leaves` Float (compute=_compute_leaves)
- `leaves_taken` Float “Time off Taken” (compute=_compute_leaves)
- `has_accrual_plan` Boolean “Accrual Plan Available” (compute=_compute_has_accrual_plan)

Public methods: `action_refuse`, `action_validate`, `activity_update`, `add_follower`, `create`, `message_subscribe`, `onchange`, `write`

Extension points: `_action_validate_create_childs`, `_check_approval_update`, `_check_date_from_date_to`, `_get_accrual_plan_level_work_entry_prorata`, `_get_carryover_date`, `_get_current_accrual_plan_level_id`, `_get_future_leaves_on`, `_get_mail_redirect_suggested_company`, `_get_request_unit`, `_get_responsible_for_approval`, `_prepare_holiday_values`

## `hr.leave.mandatory.day` (defines)

Mandatory Day

- `name` Char (required)
- `company_id` Many2one → `res.company` (required)
- `start_date` Date (required)
- `end_date` Date (required)
- `color` Integer
- `resource_calendar_id` Many2one → `resource.calendar`
- `department_ids` Many2many → `hr.department` “Departments”

## `hr.leave.type` (defines)

Time Off Type

- `name` Char “Time Off Type” (required)
- `sequence` Integer
- `create_calendar_meeting` Boolean “Display Time Off in Calendar”
- `color` Integer “Color”
- `icon_id` Many2one → `ir.attachment` “Cover Image”
- `active` Boolean “Active”
- `max_leaves` Float “Maximum Allowed” (compute=_compute_leaves)
- `leaves_taken` Float “Time off Already Taken” (compute=_compute_leaves)
- `virtual_remaining_leaves` Float “Virtual Remaining Time Off” (compute=_compute_leaves)
- `allocation_count` Integer “Allocations” (compute=_compute_allocation_count)
- `group_days_leave` Float “Group Time Off” (compute=_compute_group_days_leave)
- `company_id` Many2one → `res.company` “Company”
- `responsible_ids` Many2many → `res.users` “Notified Time Off Officer”
- `leave_validation_type` Selection “Time Off Validation”
- `requires_allocation` Selection “Requires allocation” (required)
- `employee_requests` Selection “Employee Requests” (required)
- `allocation_validation_type` Selection “Approval” (store, compute=_compute_allocation_validation_type)
- `has_valid_allocation` Boolean (compute=_compute_valid)
- `time_type` Selection “Kind of Time Off”
- `request_unit` Selection “Take Time Off in” (required)
- `unpaid` Boolean “Is Unpaid”
- `leave_notif_subtype_id` Many2one → `mail.message.subtype` “Time Off Notification Subtype”
- `allocation_notif_subtype_id` Many2one → `mail.message.subtype` “Allocation Notification Subtype”
- `support_document` Boolean “Supporting Document”
- `accruals_ids` One2many → `hr.leave.accrual.plan`
- `accrual_count` Float “Accruals count” (compute=_compute_accrual_count)
- `allows_negative` Boolean “Allow Negative Cap”
- `max_allowed_negative` Integer “Amount in Negative”

Public methods: `action_see_accrual_plans`, `action_see_days_allocated`, `action_see_group_leaves`, `check_allocation_requirement_edit_validity`, `get_allocation_data`, `get_allocation_data_request`, `has_accrual_allocation`, `requested_display_name`

## `mail.activity.type` (extends)


Extension points: `_get_model_info_by_xmlid`

## `mail.message.subtype` (extends)


Public methods: `create`, `write`

Extension points: `_get_department_subtype`

## `res.partner` (extends)


Public methods: `mail_partner_format`

Extension points: `_get_on_leave_ids`

## `res.users` (extends)

- `leave_manager_id` Many2one (related=employee_id.leave_manager_id)
- `show_leaves` Boolean (related=employee_id.show_leaves)
- `allocation_count` Float (related=employee_id.allocation_count)
- `leave_date_to` Date (related=employee_id.leave_date_to)
- `current_leave_state` Selection (related=employee_id.current_leave_state)
- `is_absent` Boolean (related=employee_id.is_absent)
- `allocation_remaining_display` Char (related=employee_id.allocation_remaining_display)
- `allocation_display` Char (related=employee_id.allocation_display)
- `hr_icon_display` Selection (related=employee_id.hr_icon_display)

Public methods: `SELF_READABLE_FIELDS`, `create`

Extension points: `_get_on_leave_ids`

## `resource.calendar.leaves` (extends)

- `holiday_id` Many2one → `hr.leave` “Time Off Request”

Public methods: `create`, `unlink`, `write`

Extension points: `_check_compare_dates`, `_get_domain`, `_get_time_domain_dict`, `_prepare_public_holidays_values`

## `resource.calendar` (extends)

- `associated_leaves_count` Integer “Time Off Count” (compute=_compute_associated_leaves_count)

## `hr.leave.type` (extends)


## `hr.leave` (extends)


## `hr.leave.allocation` (extends)


## `report.hr_holidays.report_holidayssummary` (defines)

Holidays Summary Report


Extension points: `_get_data_from_report`, `_get_day`, `_get_employees`, `_get_header_info`, `_get_holidays_status`, `_get_leaves`, `_get_leaves_summary`, `_get_months`, `_get_report_values`

## `hr.leave.employee.type.report` (defines)

Time Off Summary / Report

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `active_employee` Boolean (readonly)
- `number_of_days` Float “Number of Days” (readonly)
- `department_id` Many2one → `hr.department` “Department” (readonly)
- `leave_type` Many2one → `hr.leave.type` “Time Off Type” (readonly)
- `holiday_status` Selection
- `state` Selection “Status” (readonly)
- `date_from` Datetime “Start Date” (readonly)
- `date_to` Datetime “End Date” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)

Public methods: `action_time_off_analysis`, `init`

## `hr.leave.report` (defines)

Time Off Summary / Report

- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `leave_id` Many2one → `hr.leave` “Time Off Request” (readonly)
- `name` Char “Description” (readonly)
- `number_of_days` Float “Number of Days” (readonly)
- `leave_type` Selection “Request Type” (readonly)
- `department_id` Many2one → `hr.department` “Department” (readonly)
- `category_id` Many2one → `hr.employee.category` “Employee Tag” (readonly)
- `holiday_status_id` Many2one → `hr.leave.type` “Time Off Type” (readonly)
- `state` Selection “Status” (readonly)
- `holiday_type` Selection “Allocation Mode” (readonly)
- `date_from` Datetime “Start Date” (readonly)
- `date_to` Datetime “End Date” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)

Public methods: `action_open_record`, `init`

## `hr.leave.report.calendar` (defines)

Time Off Calendar

- `name` Char “Name” (readonly)
- `start_datetime` Datetime “From” (readonly)
- `stop_datetime` Datetime “To” (readonly)
- `tz` Selection “Timezone” (readonly)
- `duration` Float “Duration” (readonly)
- `employee_id` Many2one → `hr.employee` (readonly)
- `department_id` Many2one → `hr.department` (readonly)
- `job_id` Many2one → `hr.job` (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `state` Selection (readonly)
- `is_hatched` Boolean “Hatched” (readonly)
- `is_striked` Boolean “Striked” (readonly)
- `is_absent` Boolean (related=employee_id.is_absent)

Public methods: `get_unusual_days`, `init`

## `hr.departure.wizard` (extends)

- `cancel_leaves` Boolean “Cancel Future Time Off”
- `archive_allocation` Boolean “Archive Employee Allocations”

Public methods: `action_register_departure`

## `hr.holidays.cancel.leave` (defines)

Cancel Time Off Wizard

- `leave_id` Many2one → `hr.leave` “Time Off Request” (required)
- `reason` Text (required)

Public methods: `action_cancel_leave`

## `hr.holidays.summary.employee` (defines)

HR Time Off Summary Report By Employee

- `date_from` Date “From” (required)
- `emp` Many2many → `hr.employee` “Employee(s)”
- `holiday_type` Selection “Select Time Off Type” (required)

Public methods: `print_report`
