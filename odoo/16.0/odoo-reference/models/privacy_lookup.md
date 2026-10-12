# privacy_lookup — Privacy

Depends on: mail.

## `privacy.log` (defines)

Privacy Log

- `date` Datetime (required)
- `anonymized_name` Char (required)
- `anonymized_email` Char (required)
- `user_id` Many2one → `res.users` “Handled By” (required)
- `execution_details` Text
- `records_description` Text “Found Records”
- `additional_note` Text

Public methods: `create`

## `res.partner` (extends)


Public methods: `action_privacy_lookup`

## `privacy.lookup.wizard` (defines)

Privacy Lookup Wizard

- `name` Char (required)
- `email` Char (required)
- `line_ids` One2many → `privacy.lookup.wizard.line`
- `execution_details` Text (store, compute=_compute_execution_details)
- `log_id` Many2one → `privacy.log`
- `records_description` Text (compute=_compute_records_description)
- `line_count` Integer (compute=_compute_line_count)

Public methods: `action_lookup`, `action_open_lines`, `name_get`

Extension points: `_get_query`, `_get_query_models_blacklist`, `_post_log`

## `privacy.lookup.wizard.line` (defines)

Privacy Lookup Wizard Line

- `wizard_id` Many2one → `privacy.lookup.wizard`
- `res_id` Integer “Resource ID” (required)
- `res_name` Char “Resource name” (store, compute=_compute_res_name)
- `res_model_id` Many2one → `ir.model`
- `res_model` Char “Document Model” (readonly, store, related=res_model_id.model)
- `resource_ref` Reference “Record” (compute=_compute_resource_ref)
- `has_active` Boolean (store, compute=_compute_has_active)
- `is_active` Boolean
- `is_unlinked` Boolean
- `execution_details` Char

Public methods: `action_archive_all`, `action_open_record`, `action_unlink`, `action_unlink_all`
