# base_automation — Automated Action Rules

Depends on: base, resource, mail.

## `base.automation` (defines)

Automated Action

- `action_server_id` Many2one → `ir.actions.server` (required)
- `active` Boolean
- `trigger` Selection “Trigger” (required)
- `trg_date_id` Many2one → `ir.model.fields` “Trigger Date” (store, compute=_compute_trg_date_id)
- `trg_date_range` Integer “Delay after trigger date” (store, compute=_compute_trg_date_range_data)
- `trg_date_range_type` Selection “Delay type” (store, compute=_compute_trg_date_range_data)
- `trg_date_calendar_id` Many2one → `resource.calendar` “Use Calendar” (store, compute=_compute_trg_date_calendar_id)
- `filter_pre_domain` Char “Before Update Domain” (store, compute=_compute_filter_pre_domain)
- `filter_domain` Char “Apply on”
- `last_run` Datetime (readonly)
- `on_change_field_ids` Many2many → `ir.model.fields` “On Change Fields Trigger” (store, compute=_compute_on_change_field_ids)
- `trigger_field_ids` Many2many → `ir.model.fields` “Trigger Fields” (store, compute=_compute_trigger_field_ids)
- `least_delay_msg` Char (compute=_compute_least_delay_msg)

Public methods: `create`, `unlink`, `write`

Extension points: `_check_delay`, `_check_trigger_fields`, `_check_trigger_state`, `_get_actions`, `_get_calendar`, `_get_cron_interval`, `_get_eval_context`

## `ir.actions.server` (extends)

- `usage` Selection
