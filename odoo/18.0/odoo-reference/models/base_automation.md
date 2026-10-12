# base_automation — Automation Rules

Depends on: base, digest, resource, mail, sms.

## `base.automation` (defines)

Automation Rule

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
- `trg_date_range` Integer “Delay after trigger date” (store, compute=_compute_trg_date_range_data)
- `trg_date_range_type` Selection “Delay type” (store, compute=_compute_trg_date_range_data)
- `trg_date_calendar_id` Many2one → `resource.calendar` “Use Calendar” (store, compute=_compute_trg_date_calendar_id)
- `filter_pre_domain` Char “Before Update Domain” (store, compute=_compute_filter_pre_domain)
- `filter_domain` Char “Apply on” (store, compute=_compute_filter_domain)
- `last_run` Datetime (readonly)
- `on_change_field_ids` Many2many → `ir.model.fields` “On Change Fields Trigger” (store, compute=_compute_on_change_field_ids)
- `trigger_field_ids` Many2many → `ir.model.fields` “Trigger Fields” (store, compute=_compute_trigger_field_ids)
- `least_delay_msg` Char (compute=_compute_least_delay_msg)

Public methods: `action_rotate_webhook_uuid`, `action_view_webhook_logs`, `copy`, `create`, `unlink`, `write`

Extension points: `_check_action_server_model`, `_check_trigger`, `_check_trigger_fields`, `_check_trigger_state`, `_get_actions`, `_get_calendar`, `_get_cron_interval`, `_get_eval_context`, `_get_filter_domain_fields`, `_get_trigger_specific_field`, `_prepare_loggin_values`

## `ir.actions.server` (extends)

- `name` Char (store, compute=_compute_name)
- `usage` Selection
- `base_automation_id` Many2one → `base.automation` “Automation Rule”

Extension points: `_check_model_coherency_with_automation`, `_get_eval_context`
