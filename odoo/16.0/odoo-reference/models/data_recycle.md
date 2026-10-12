# data_recycle — Data Recycle

Depends on: mail.

## `data_recycle.model` (defines)

Recycling Model

- `active` Boolean
- `name` Char “Name” (required, store, compute=_compute_name)
- `res_model_id` Many2one → `ir.model` “Model” (required)
- `res_model_name` Char “Model Name” (readonly, store, related=res_model_id.model)
- `recycle_record_ids` One2many → `data_recycle.record`
- `recycle_mode` Selection “Recycle Mode” (required)
- `recycle_action` Selection “Recycle Action” (required)
- `domain` Char “Filter” (store, compute=_compute_domain)
- `time_field_id` Many2one → `ir.model.fields` “Time Field”
- `time_field_delta` Integer “Delta”
- `time_field_delta_unit` Selection “Delta Unit”
- `include_archived` Boolean
- `records_to_recycle_count` Integer “Records To Recycle” (compute=_compute_records_to_recycle_count)
- `notify_user_ids` Many2many → `res.users` “Notify Users”
- `notify_frequency` Integer “Notify”
- `notify_frequency_period` Selection “Notify Frequency Period”
- `last_notification` Datetime (readonly)

Public methods: `action_recycle_records`, `open_records`, `write`

Extension points: `_check_recycle_action`

## `data_recycle.record` (defines)

Recycling Record

- `active` Boolean “Active”
- `name` Char “Record Name” (compute=_compute_values)
- `recycle_model_id` Many2one → `data_recycle.model` “Recycle Model”
- `res_id` Integer “Record ID” (index)
- `res_model_id` Many2one (readonly, store, related=recycle_model_id.res_model_id)
- `res_model_name` Char (readonly, store, related=recycle_model_id.res_model_name)
- `company_id` Many2one → `res.company` (store, compute=_compute_values)

Public methods: `action_discard`, `action_validate`

Extension points: `_get_company_id`
