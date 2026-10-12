# base_automation — Automation Rules

Depends on: base, digest, resource, mail, sms.

## `base.automation` (defines)

Automation Rule

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Automation Rule Name” (required)
- `description` Html “Description”
- `model_id` Many2one → `ir.model` “Model” (required)
- `model_name` Char “Model Name” (readonly, related=model_id.model)
- `model_is_mail_thread` Boolean (related=model_id.is_mail_thread)
- `action_server_ids` One2many → `ir.actions.server` “Actions” (store, compute=_compute_action_server_ids)
- `url` Char (compute=_compute_url)
- `webhook_uuid` Char “Webhook UUID” (readonly)
- `record_getter` Char
- `log_webhook_calls` Boolean “Log Calls”
- `active` Boolean
- `trigger` Selection “Trigger” (required, store, compute=_compute_trigger)
- `trg_selection_field_id` Many2one → `ir.model.fields.selection` “Trigger Field” (store, compute=_compute_trg_selection_field_id)
- `trg_field_ref_model_name` Char “Trigger Field Model” (compute=_compute_trg_field_ref_model_name)
- `trg_field_ref` Many2oneReference “Trigger Reference” (store, compute=_compute_trg_field_ref)
- `trg_date_id` Many2one → `ir.model.fields` “Trigger Date” (store, compute=_compute_trg_date_id)
- `trg_date_range` Integer “Delay” (store, compute=_compute_trg_date_range_data)
- `trg_date_range_mode` Selection “Delay mode” (store, compute=_compute_trg_date_range_data)
- `trg_date_range_type` Selection “Delay unit” (store, compute=_compute_trg_date_range_data)
- `trg_date_calendar_id` Many2one → `resource.calendar` “Use Calendar” (store, compute=_compute_trg_date_calendar_id)
- `filter_pre_domain` Char “Before Update Domain” (store, compute=_compute_filter_pre_domain)
- `previous_domain` Char (compute=_compute_previous_domain)
- `filter_domain` Char “Apply on” (store, compute=_compute_filter_domain)
- `last_run` Datetime (readonly)
- `on_change_field_ids` Many2many → `ir.model.fields` “On Change Fields Trigger” (store, compute=_compute_on_change_field_ids)
- `trigger_field_ids` Many2many → `ir.model.fields` “Trigger Fields” (store, compute=_compute_trigger_field_ids)

Public methods: `action_open_scheduled_action`, `action_rotate_webhook_uuid`, `action_view_webhook_logs`, `copy`, `create`, `unlink`, `write`

Extension points: `_check_action_server_model`, `_check_time_trigger`, `_check_trigger`, `_check_trigger_fields`, `_check_trigger_state`, `_get_actions`, `_get_calendar`, `_get_cron_interval`, `_get_eval_context`, `_get_trigger_specific_field`, `_prepare_loggin_values`

## `ir.actions.server` (extends)

- `usage` Selection
- `base_automation_id` Many2one → `base.automation` “Automation Rule”

Public methods: `action_open_automation`

Extension points: `_get_children_domain`, `_get_eval_context`, `_get_warning_messages`

## `ir.cron` (extends)


Public methods: `action_open_automation`
