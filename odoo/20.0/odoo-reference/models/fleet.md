# fleet — Fleet

Depends on: base, mail.

## `fleet.service.type` (defines)

Fleet Service Type

- `name` Char (required)
- `category` Selection (required)
- `company_id` Many2one → `res.company` “Company”

## `fleet.vehicle` (defines)

Vehicle

Inherits: `mail.thread`, `mail.activity.mixin`, `avatar.mixin`

- `name` Char (store, compute=_compute_vehicle_name)
- `description` Html “Vehicle Description”
- `active` Boolean “Active”
- `manager_id` Many2one → `res.users`
- `company_id` Many2one → `res.company` (index)
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `country_id` Many2one → `res.country` (related=company_id.country_id)
- `country_code` Char (related=country_id.code)
- `license_plate` Char
- `vin_sn` Char “Chassis Number”
- `trailer_hook` Boolean “Trailer Hitch”
- `driver_id` Many2one → `res.partner`
- `future_driver_id` Many2one → `res.partner`
- `model_id` Many2one → `fleet.vehicle.model` (index)
- `brand_id` Many2one → `fleet.vehicle.model.brand` (store, related=model_id.brand_id)
- `log_drivers` One2many → `fleet.vehicle.assignation.log` “Assignment Logs”
- `log_services` One2many → `fleet.vehicle.log.services`
- `log_contracts` One2many → `fleet.vehicle.log.contract`
- `contract_count` Integer “Contract Count” (compute=_compute_count_all)
- `service_count` Integer “Services” (compute=_compute_count_all)
- `odometer_count` Integer “Odometer” (compute=_compute_count_all)
- `history_count` Integer “Drivers History Count” (compute=_compute_count_all)
- `next_assignation_date` Date “Available From”
- `order_date` Date “Order Date”
- `acquisition_date` Date “Registration Date”
- `write_off_date` Date “Cancellation Date”
- `contract_date_start` Date “First Contract Date”
- `color` Char
- `state_id` Many2one → `fleet.vehicle.state`
- `location` Char
- `seats` Integer “Seating Capacity” (store, compute=_compute_seats)
- `model_year` Selection “Model Year” (store, compute=_compute_model_year)
- `doors` Integer “Number of Doors” (store, compute=_compute_doors)
- `tag_ids` Many2many → `fleet.vehicle.tag`
- `odometer` Float “Last Odometer” (compute=_get_odometer)
- `odometer_unit` Selection (required)
- `transmission` Selection (store, compute=_compute_transmission)
- `fuel_type` Selection (store, compute=_compute_fuel_type)
- `power_unit` Selection (required)
- `horsepower` Float (store, compute=_compute_horsepower)
- `power` Float “Power” (store, compute=_compute_power)
- `co2` Float “CO₂ Emissions” (store, compute=_compute_co2)
- `co2_emission_unit` Selection (required, store, compute=_compute_co2_emission_unit)
- `co2_standard` Char “Emission Standard” (store, compute=_compute_co2_standard)
- `category_id` Many2one → `fleet.vehicle.model.category` (store, compute=_compute_category)
- `image_128` Image (readonly, related=model_id.image_128)
- `contract_renewal_due_soon` Boolean “Has Contracts to renew” (compute=_compute_contract_reminder)
- `contract_renewal_overdue` Boolean “Has Contracts Overdue” (compute=_compute_contract_reminder)
- `contract_state` Selection “Last Contract State” (compute=_compute_contract_reminder)
- `car_value` Float “Catalog Value (Tax Incl.)”
- `net_car_value` Float “Purchase Value”
- `residual_value` Float
- `plan_to_change_vehicle` Boolean
- `vehicle_type` Selection (related=model_id.vehicle_type)
- `frame_type` Selection “Bike Frame Type”
- `electric_assistance` Boolean (store, compute=_compute_electric_assistance)
- `frame_size` Float
- `service_activity` Selection (compute=_compute_service_activity)
- `vehicle_properties` Properties “Properties”
- `vehicle_range` Integer “Range”
- `range_unit` Selection (required, store, compute=_compute_range_unit)

Public methods: `act_show_log_cost`, `action_accept_driver_change`, `action_open_odometer_report`, `action_send_email`, `create`, `create_driver_history`, `default_get`, `open_assignation_logs`, `return_action_to_open`, `write`

Extension points: `_get_analytic_name`, `_get_default_state`, `_get_driver_history_data`, `_get_odometer`, `_get_year_selection`

## `fleet.vehicle.assignation.log` (defines)

Drivers history on a vehicle

- `vehicle_id` Many2one → `fleet.vehicle` “Vehicle” (required, index)
- `driver_id` Many2one → `res.partner` “Driver” (required)
- `date_start` Date “Start Date”
- `date_end` Date “End Date”

## `fleet.vehicle.log.contract` (defines)

Vehicle Contract

Inherits: `mail.thread`, `mail.activity.mixin`

- `vehicle_id` Many2one → `fleet.vehicle` (required, index)
- `cost_subtype_id` Many2one → `fleet.service.type`
- `amount` Monetary “Cost”
- `date` Date
- `company_id` Many2one → `res.company` (index)
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `name` Char “Name” (store, compute=_compute_contract_name)
- `active` Boolean
- `user_id` Many2one → `res.users` “Responsible” (index)
- `start_date` Date “Contract Start Date”
- `expiration_date` Date “Contract Expiration Date”
- `days_left` Integer “Warning Date” (compute=_compute_days_left)
- `expires_today` Boolean (compute=_compute_days_left)
- `has_open_contract` Boolean (compute=_compute_has_open_contract)
- `insurer_id` Many2one → `res.partner`
- `purchaser_id` Many2one “Driver” (related=vehicle_id.driver_id)
- `ins_ref` Char “Reference”
- `state` Selection
- `notes` Html “Terms and Conditions”
- `cost_generated` Monetary “Recurring Cost”
- `cost_frequency` Selection (required)
- `service_ids` Many2many → `fleet.service.type` “Included Services”

Public methods: `action_close`, `action_done`, `action_draft`, `action_expire`, `action_open`, `action_reactivate`, `compute_next_year_date`, `create`, `run_scheduler`, `scheduler_manage_contract_expiration`, `write`

## `fleet.vehicle.log.services` (defines)

Services for vehicles

Inherits: `mail.thread`, `mail.activity.mixin`

- `active` Boolean
- `vehicle_id` Many2one → `fleet.vehicle` (required, index)
- `model_id` Many2one → `fleet.vehicle.model` (store, related=vehicle_id.model_id)
- `brand_id` Many2one → `fleet.vehicle.model.brand` (store, related=vehicle_id.model_id.brand_id)
- `manager_id` Many2one → `res.users` (store, related=vehicle_id.manager_id)
- `amount` Monetary “Cost”
- `description` Char “Description”
- `odometer_id` Many2one → `fleet.vehicle.odometer`
- `odometer` Float “Odometer Value” (compute=_get_odometer)
- `odometer_unit` Selection “Unit” (readonly, related=vehicle_id.odometer_unit)
- `date_from` Date “Start of Service”
- `date_to` Date “End of Service”
- `company_id` Many2one → `res.company` (index)
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

Inherits: `mail.thread`, `mail.activity.mixin`, `avatar.mixin`

- `name` Char “Model name” (required)
- `company_id` Many2one → `res.company` “Company”
- `brand_id` Many2one → `fleet.vehicle.model.brand` (required)
- `category_id` Many2one → `fleet.vehicle.model.category`
- `vendors` Many2many → `res.partner` “Vendors”
- `image_128` Image (readonly, related=brand_id.image_128)
- `active` Boolean
- `vehicle_type` Selection (required)
- `transmission` Selection “Transmission”
- `vehicle_count` Integer (compute=_compute_vehicle_count)
- `model_year` Selection
- `seats` Integer “Seating Capacity”
- `doors` Integer “Number of Doors”
- `default_co2` Float “CO₂ Emissions”
- `co2_emission_unit` Selection (required, compute=_compute_co2_emission_unit)
- `co2_standard` Char “Emission Standard”
- `default_fuel_type` Selection
- `power` Float “Power”
- `horsepower` Float
- `electric_assistance` Boolean
- `power_unit` Selection (required)
- `vehicle_properties_definition` PropertiesDefinition “Vehicle Properties”
- `vehicle_range` Integer “Range”
- `range_unit` Selection (required)
- `drive_type` Selection

Public methods: `action_model_vehicle`

Extension points: `_get_year_selection`

## `fleet.vehicle.model.brand` (defines)

Brand of the vehicle

- `name` Char “Name” (required)
- `active` Boolean
- `image_128` Image “Logo”
- `model_count` Integer (store, compute=_compute_model_count)
- `model_ids` One2many → `fleet.vehicle.model`

Public methods: `action_brand_model`, `action_open_brand_form`

## `fleet.vehicle.model.category` (defines)

Category of the model

- `name` Char (required)
- `sequence` Integer

## `fleet.vehicle.odometer` (defines)

Odometer log for a vehicle

- `name` Char (store, compute=_compute_vehicle_log_name)
- `date` Date
- `value` Float “Odometer Value”
- `vehicle_id` Many2one → `fleet.vehicle` (required, index)
- `unit` Selection “Unit” (readonly, related=vehicle_id.odometer_unit)
- `driver_id` Many2one → `res.partner` “Driver” (store, compute=_compute_driver_id)

## `fleet.vehicle.state` (defines)

Vehicle Status

- `name` Char (required)
- `sequence` Integer
- `fold` Boolean “Folded in Kanban”

## `fleet.vehicle.tag` (defines)

Vehicle Tag

- `name` Char “Tag Name” (required)
- `color` Integer “Color”

## `mail.activity.type` (extends)


Extension points: `_get_model_info_by_xmlid`

## `res.config.settings` (extends)

- `delay_alert_contract` Integer “Delay alert contract outdated”

## `res.partner` (extends)

- `partner_cars_count` Integer “Cars Count” (compute=_compute_partner_cars_count)

Public methods: `action_open_partner_cars`

## `fleet.vehicle.cost.report` (defines)

Fleet Analysis Report

- `company_id` Many2one → `res.company` (readonly)
- `vehicle_id` Many2one → `fleet.vehicle` (readonly)
- `name` Char “Vehicle Name” (readonly)
- `driver_id` Many2one → `res.partner` (readonly)
- `fuel_type` Char “Fuel” (readonly)
- `date_start` Date “Date” (readonly)
- `vehicle_type` Selection (readonly)
- `service_type` Many2one → `fleet.service.type` (readonly)
- `cost` Float “Cost” (readonly)
- `cost_type` Selection “Cost Type” (readonly)

Public methods: `init`

## `fleet.vehicle.odometer.report` (defines)

Fleet Odometer Analysis Report

- `vehicle_id` Many2one → `fleet.vehicle` (readonly)
- `category_id` Many2one (related=vehicle_id.category_id)
- `model_id` Many2one (related=vehicle_id.model_id)
- `fuel_type` Selection (related=vehicle_id.fuel_type)
- `mileage_delta` Float “Mileage Delta” (readonly)
- `odometer_value` Float “Odometer Value” (readonly)
- `recorded_date` Date “Date” (readonly)

Public methods: `init`

## `fleet.vehicle.send.mail` (defines)

Send mails to Drivers

Inherits: `mail.composer.mixin`

- `vehicle_ids` Many2many → `fleet.vehicle` “Vehicles” (required)
- `author_id` Many2one → `res.partner` (required)
- `template_id` Many2one
- `attachment_ids` Many2many → `ir.attachment` “Attachments”

Public methods: `action_save_as_template`, `action_send`
