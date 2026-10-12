# cloud_storage — Cloud Storage

Depends on: base_setup, mail.

## `ir.attachment` (extends)

- `type` Selection

Extension points: `_get_cloud_storage_download_url_time_to_expiry`, `_get_cloud_storage_unsupported_models`, `_post_add_create`

## `ir.http` (extends)


Public methods: `session_info`

## `res.config.settings` (extends)

- `cloud_storage_provider` Selection “Cloud Storage Provider for new attachments”
- `cloud_storage_min_file_size_mb` Float “Minimum File Size (MB)”
- `cloud_storage_min_file_size` Integer “Minimum File Size (bytes)”

Public methods: `get_values`, `set_values`

Extension points: `_check_cloud_storage_uninstallable`, `_get_cloud_storage_configuration`
