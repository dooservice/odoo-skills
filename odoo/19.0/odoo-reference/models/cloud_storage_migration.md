# cloud_storage_migration — Cloud Storage Migration

Depends on: cloud_storage.

## `cloud.storage.migration.report` (defines)

Cloud Storage Migration Report

- `res_model` Char “Model” (readonly)
- `res_model_name` Char “Model Name” (readonly, compute=_compute_res_model_name)
- `message_sum_size` Integer “Message Attachments Size (MB)” (readonly)
- `message_max_size` Integer “Message Largest Attachment (MB)” (readonly)
- `message_count` Integer “Message Attachments Count” (readonly)
- `message_to_migrate` Boolean “Message Attachments Migration” (compute=_compute_message_to_migrate)
- `all_sum_size` Integer “Total Attachments Size (MB)” (readonly)
- `all_max_size` Integer “Largest Attachment (MB)” (readonly)
- `all_count` Integer “Total Attachments Count” (readonly)
- `all_to_migrate` Boolean “All Attachments Migration” (compute=_compute_all_to_migrate)
- `has_attachment_rel` Boolean “Has Attachment Field” (compute=_compute_has_attachment_rel)

Public methods: `get_progress`, `init`

## `ir.attachment` (extends)


## `res.config.settings` (extends)

- `cloud_storage_migration_progress` Integer “Migration Progress”
- `cloud_storage_migration_message_model_ids` One2many → `ir.model` “Message Attachments” (compute=_compute_cloud_storage_migration_message_model_ids)
- `cloud_storage_migration_message_models` Char
- `cloud_storage_migration_all_model_ids` One2many → `ir.model` “All Attachments” (compute=_compute_cloud_storage_migration_all_model_ids)
- `cloud_storage_migration_all_models` Char

Public methods: `action_open_cloud_storage_migration_configurations`, `get_values`
