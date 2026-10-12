# cloud_storage — Cloud Storage

Depends on: mail.

## `ir.attachment` (extends)

- `type` Selection

Extension points: `_get_cloud_storage_download_url_time_to_expiry`, `_get_cloud_storage_unsupported_models`, `_post_add_create`

## `ir.http` (extends)


Public methods: `session_info`

## `res.config.settings` (extends)

- `cloud_storage_provider` Selection “Cloud Storage Provider for new attachments”
- `cloud_storage_min_file_size` Integer “Minimum File Size (bytes)”

Public methods: `set_values`

Extension points: `_check_cloud_storage_uninstallable`, `_get_cloud_storage_configuration`
