# fleet — Fleet

Depends on: base, mail.

## `fleet.service.type` (defines)

Fleet Service Type

- `name` Char (required)
- `category` Selection (required)

## `fleet.vehicle` (defines)

Vehicle

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char (store, compute=_compute_vehicle_name)
- `description` Html “Vehicle Description”
- `active` Boolean “Active”
- `manager_id` Many2one → `res.users`
- `company_id` Many2one → `res.company`
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `country_id` Many2one → `res.country` (related=company_id.country_id)
- `country_code` Char (related=country_id.code)
- `license_plate` Char
- `vin_sn` Char “Chassis Number”
- `trailer_hook` Boolean “Trailer Hitch” (store, compute=_compute_model_fields)
- `driver_id` Many2one → `res.partner`
- `future_driver_id` Many2one → `res.partner`
- `model_id` Many2one → `fleet.vehicle.model` (required)
- `brand_id` Many2one → `fleet.vehicle.model.brand` (store, related=model_id.brand_id)
- `log_drivers` One2many → `fleet.vehicle.assignation.log` “Assignment Logs”
- `log_services` One2many → `fleet.vehicle.log.services`
- `log_contracts` One2many → `fleet.vehicle.log.contract`
- `contract_count` Integer “Contract Count” (compute=_compute_count_all)
- `service_count` Integer “Services” (compute=_compute_count_all)
- `odometer_count` Integer “Odometer” (compute=_compute_count_all)
- `history_count` Integer “Drivers History Count” (compute=_compute_count_all)
- `next_assignation_date` Date “Assignment Date”
- `acquisition_date` Date “Registration Date”
- `write_off_date` Date “Cancellation Date”
- `first_contract_date` Date “First Contract Date”
- `color` Char (store, compute=_compute_model_fields)
- `state_id` Many2one → `fleet.vehicle.state`
- `location` Char
- `seats` Integer “Seats Number” (store, compute=_compute_model_fields)
- `model_year` Char “Model Year” (store, compute=_compute_model_fields)
- `doors` Integer “Doors Number” (store, compute=_compute_model_fields)
- `tag_ids` Many2many → `fleet.vehicle.tag`
- `odometer` Float “Last Odometer” (compute=_get_odometer)
- `odometer_unit` Selection (required)
- `transmission` Selection (store, compute=_compute_model_fields)
- `fuel_type` Selection (store, compute=_compute_model_fields)
- `horsepower` Integer (store, compute=_compute_model_fields)
- `horsepower_tax` Float “Horsepower Taxation” (store, compute=_compute_model_fields)
- `power` Integer “Power” (store, compute=_compute_model_fields)
- `co2` Float “CO2 Emissions” (store, compute=_compute_model_fields)
- `co2_standard` Char “CO2 Standard” (store, compute=_compute_model_fields)
- `category_id` Many2one → `fleet.vehicle.model.category` (store, compute=_compute_model_fields)
- `image_128` Image (readonly, related=model_id.image_128)
- `contract_renewal_due_soon` Boolean “Has Contracts to renew” (compute=_compute_contract_reminder)
- `contract_renewal_overdue` Boolean “Has Contracts Overdue” (compute=_compute_contract_reminder)
- `contract_renewal_name` Text “Name of contract to renew soon” (compute=_compute_contract_reminder)
- `contract_renewal_total` Text “Total of contracts due or overdue minus one” (compute=_compute_contract_reminder)
- `contract_state` Selection “Last Contract State” (compute=_compute_contract_reminder)
- `car_value` Float “Catalog Value (VAT Incl.)”
- `net_car_value` Float “Purchase Value”
- `residual_value` Float
- `plan_to_change_car` Boolean (store, related=driver_id.plan_to_change_car)
- `plan_to_change_bike` Boolean (store, related=driver_id.plan_to_change_bike)
- `vehicle_type` Selection (related=model_id.vehicle_type)
- `frame_type` Selection “Bike Frame Type”
- `electric_assistance` Boolean (store, compute=_compute_model_fields)
- `frame_size` Float
- `service_activity` Selection (compute=_compute_service_activity)

Public methods: `act_show_log_cost`, `action_accept_driver_change`, `create`, `create_driver_history`, `open_assignation_logs`, `read_group`, `return_action_to_open`, `write`

Extension points: `_get_analytic_name`, `_get_default_state`, `_get_driver_history_data`, `_get_odometer`

## `fleet.vehicle.assignation.log` (defines)

Drivers history on a vehicle

- `vehicle_id` Many2one → `fleet.vehicle` “Vehicle” (required)
- `driver_id` Many2one → `res.partner` “Driver” (required)
- `date_start` Date “Start Date”
- `date_end` Date “End Date”

## `fleet.vehicle.log.contract` (defines)

Vehicle Contract

Inherits: `mail.thread`, `mail.activity.mixin`

- `vehicle_id` Many2one → `fleet.vehicle` (required)
- `cost_subtype_id` Many2one → `fleet.service.type`
- `amount` Monetary “Cost”
- `date` Date
- `company_id` Many2one → `res.company`
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `name` Char “Name” (store, compute=_compute_contract_name)
- `active` Boolean
- `user_id` Many2one → `res.users` (index)
- `start_date` Date “Contract Start Date”
- `expiration_date` Date “Contract Expiration Date”
- `days_left` Integer “Warning Date” (compute=_compute_days_left)
- `expires_today` Boolean (compute=_compute_days_left)
- `insurer_id` Many2one → `res.partner`
- `purchaser_id` Many2one “Driver” (related=vehicle_id.driver_id)
- `ins_ref` Char “Reference”
- `state` Selection (readonly)
- `notes` Html “Terms and Conditions”
- `cost_generated` Monetary “Recurring Cost”
- `cost_frequency` Selection (required)
- `service_ids` Many2many → `fleet.service.type` “Included Services”

Public methods: `action_close`, `action_draft`, `action_expire`, `action_open`, `compute_next_year_date`, `run_scheduler`, `scheduler_manage_contract_expiration`, `write`

## `fleet.vehicle.log.services` (defines)

Services for vehicles

Inherits: `mail.thread`, `mail.activity.mixin`

- `active` Boolean
- `vehicle_id` Many2one → `fleet.vehicle` (required)
- `manager_id` Many2one → `res.users` (store, related=vehicle_id.manager_id)
- `amount` Monetary “Cost”
- `description` Char “Description”
- `odometer_id` Many2one → `fleet.vehicle.odometer`
- `odometer` Float “Odometer Value” (compute=_get_odometer)
- `odometer_unit` Selection “Unit” (readonly, related=vehicle_id.odometer_unit)
- `date` Date
- `company_id` Many2one → `res.company`
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `purchaser_id` Many2one → `res.partner` “Driver” (store, compute=_compute_purchaser_id)
- `inv_ref` Char “Vendor Reference”
- `vendor_id` Many2one → `res.partner`
- `notes` Text
- `service_type_id` Many2one → `fleet.service.type` (required)
- `state` Selection “Stage”

Public methods: `create`

Extension points: `_get_odometer`

## `fleet.vehicle.model` (defines)

Model of a vehicle

- `name` Char “Model name” (required)
- `brand_id` Many2one → `fleet.vehicle.model.brand` (required)
- `category_id` Many2one → `fleet.vehicle.model.category`
- `vendors` Many2many → `res.partner` “Vendors”
- `image_128` Image (readonly, related=brand_id.image_128)
- `active` Boolean
- `vehicle_type` Selection (required)
- `transmission` Selection
- `vehicle_count` Integer (compute=_compute_vehicle_count)
- `model_year` Integer
- `color` Char
- `seats` Integer “Seats Number”
- `doors` Integer “Doors Number”
- `trailer_hook` Boolean “Trailer Hitch”
- `default_co2` Float “CO2 Emissions”
- `co2_standard` Char
- `default_fuel_type` Selection
- `power` Integer “Power”
- `horsepower` Integer
- `horsepower_tax` Float “Horsepower Taxation”
- `electric_assistance` Boolean

Public methods: `action_model_vehicle`, `name_get`

## `fleet.vehicle.model.brand` (defines)

Brand of the vehicle

- `name` Char “Name” (required)
- `image_128` Image “Logo”
- `model_count` Integer (store, compute=_compute_model_count)
- `model_ids` One2many → `fleet.vehicle.model`

Public methods: `action_brand_model`

## `fleet.vehicle.model.category` (defines)

Category of the model

- `name` Char (required)
- `sequence` Integer

## `fleet.vehicle.odometer` (defines)

Odometer log for a vehicle

- `name` Char (store, compute=_compute_vehicle_log_name)
- `date` Date
- `value` Float “Odometer Value”
- `vehicle_id` Many2one → `fleet.vehicle` (required)
- `unit` Selection “Unit” (readonly, related=vehicle_id.odometer_unit)
- `driver_id` Many2one “Driver” (related=vehicle_id.driver_id)

## `fleet.vehicle.state` (defines)

Vehicle Status

- `name` Char (required)
- `sequence` Integer

## `fleet.vehicle.tag` (defines)

Vehicle Tag

- `name` Char “Tag Name” (required)
- `color` Integer “Color”

## `res.config.settings` (extends)

- `delay_alert_contract` Integer “Delay alert contract outdated”

## `res.partner` (extends)

- `plan_to_change_car` Boolean “Plan To Change Car”
- `plan_to_change_bike` Boolean “Plan To Change Bike”

## `fleet.vehicle.cost.report` (defines)

Fleet Analysis Report

- `company_id` Many2one → `res.company` (readonly)
- `vehicle_id` Many2one → `fleet.vehicle` (readonly)
- `name` Char “Vehicle Name” (readonly)
- `driver_id` Many2one → `res.partner` (readonly)
- `fuel_type` Char “Fuel” (readonly)
- `date_start` Date “Date” (readonly)
- `vehicle_type` Selection (readonly)
- `cost` Float “Cost” (readonly)
- `cost_type` Selection “Cost Type” (readonly)

Public methods: `init`
