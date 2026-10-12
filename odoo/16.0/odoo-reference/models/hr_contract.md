# hr_contract — Employee Contracts

Depends on: hr.

## `hr.contract` (defines)

Contract

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Contract Reference” (required)
- `active` Boolean
- `structure_type_id` Many2one → `hr.payroll.structure.type` “Salary Structure Type”
- `employee_id` Many2one → `hr.employee` “Employee”
- `department_id` Many2one → `hr.department` “Department” (store, compute=_compute_employee_contract)
- `job_id` Many2one → `hr.job` “Job Position” (store, compute=_compute_employee_contract)
- `date_start` Date “Start Date” (required, index)
- `date_end` Date “End Date”
- `trial_date_end` Date “End of Trial Period”
- `resource_calendar_id` Many2one → `resource.calendar` (store, index, compute=_compute_employee_contract)
- `wage` Monetary “Wage” (required)
- `contract_wage` Monetary “Contract Wage” (compute=_compute_contract_wage)
- `notes` Html “Notes”
- `state` Selection “Status”
- `company_id` Many2one → `res.company` (required, store, compute=_compute_employee_contract)
- `company_country_id` Many2one → `res.country` “Company country” (readonly, related=company_id.country_id)
- `country_code` Char (readonly, related=company_country_id.code)
- `contract_type_id` Many2one → `hr.contract.type`
- `kanban_state` Selection “Kanban State”
- `currency_id` Many2one “Currency” (readonly, related=company_id.currency_id)
- `permit_no` Char “Work Permit No” (related=employee_id.permit_no)
- `visa_no` Char “Visa No” (related=employee_id.visa_no)
- `visa_expire` Date “Visa Expiration Date” (related=employee_id.visa_expire)
- `hr_responsible_id` Many2one → `res.users`
- `calendar_mismatch` Boolean (compute=_compute_calendar_mismatch)
- `first_contract_date` Date (related=employee_id.first_contract_date)

Public methods: `action_open_contract_form`, `create`, `update_state`, `write`

Extension points: `_check_current_contract`, `_check_dates`, `_get_contract_wage`, `_get_contract_wage_field`, `_get_employee_vals_to_update`, `_get_hr_responsible_domain`

## `hr.employee` (extends)

- `vehicle` Char “Company Vehicle”
- `contract_ids` One2many → `hr.contract` “Employee Contracts”
- `contract_id` Many2one → `hr.contract` “Current Contract”
- `calendar_mismatch` Boolean (related=contract_id.calendar_mismatch)
- `contracts_count` Integer “Contract Count” (compute=_compute_contracts_count)
- `contract_warning` Boolean “Contract Warning” (store, compute=_compute_contract_warning)
- `first_contract_date` Date (store, compute=_compute_first_contract_date)

Public methods: `action_open_contract_history`, `write`

Extension points: `_get_all_contracts`, `_get_contracts`, `_get_expected_attendances`, `_get_first_contract_date`, `_get_first_contracts`, `_get_incoming_contracts`

## `hr.employee.public` (extends)

- `first_contract_date` Date (readonly)

## `hr.payroll.structure.type` (defines)

Salary Structure Type

- `name` Char “Salary Structure Type”
- `default_resource_calendar_id` Many2one → `resource.calendar`
- `country_id` Many2one → `res.country` “Country”

## `res.users` (extends)

- `vehicle` Char (related=employee_id.vehicle)
- `bank_account_id` Many2one (related=employee_id.bank_account_id)

Public methods: `SELF_READABLE_FIELDS`

## `resource.calendar` (extends)

- `contracts_count` Integer “# Contracts using it” (compute=_compute_contracts_count)

Public methods: `action_open_contracts`, `transfer_leaves_to`

## `resource.calendar.leaves` (extends)


## `resource.resource` (extends)


Extension points: `_get_calendars_validity_within_period`

## `hr.contract.history` (defines)

Contract history

- `contract_id` Many2one → `hr.contract` (readonly)
- `display_name` Char (compute=_compute_display_name)
- `name` Char “Contract Name” (readonly)
- `date_hired` Date “Hire Date” (readonly)
- `date_start` Date “Start Date” (readonly)
- `date_end` Date “End Date” (readonly)
- `employee_id` Many2one → `hr.employee` “Employee” (readonly)
- `active_employee` Boolean “Active Employee” (readonly)
- `is_under_contract` Boolean “Is Currently Under Contract” (readonly)
- `department_id` Many2one → `hr.department` “Department” (readonly)
- `structure_type_id` Many2one → `hr.payroll.structure.type` “Salary Structure Type” (readonly)
- `hr_responsible_id` Many2one → `res.users` “HR Responsible” (readonly)
- `job_id` Many2one → `hr.job` “Job Position” (readonly)
- `state` Selection “Status” (readonly)
- `resource_calendar_id` Many2one → `resource.calendar` “Working Schedule” (readonly)
- `wage` Monetary “Wage” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `company_country_id` Many2one → `res.country` “Company country” (readonly, related=company_id.country_id)
- `country_code` Char (readonly, related=company_country_id.code)
- `currency_id` Many2one “Currency” (readonly, related=company_id.currency_id)
- `contract_type_id` Many2one → `hr.contract.type` (readonly)
- `contract_ids` One2many → `hr.contract` “Contracts” (readonly, compute=_compute_contract_ids)
- `contract_count` Integer “# Contracts” (compute=_compute_contract_count)
- `under_contract_state` Selection “Contractual Status” (compute=_compute_under_contract_state)
- `activity_state` Selection (related=contract_id.activity_state)

Public methods: `hr_contract_view_form_new_action`, `init`

Extension points: `_get_fields`

## `hr.departure.wizard` (extends)

- `set_date_end` Boolean “Set Contract End Date”

Public methods: `action_register_departure`

Extension points: `_get_employee_departure_date`
