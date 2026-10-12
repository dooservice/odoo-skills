# cloud_storage_google — Cloud Storage Google

Depends on: cloud_storage.

## `ir.attachment` (extends)


Extension points: `_get_cloud_storage_google_info`

## `res.config.settings` (extends)

- `cloud_storage_provider` Selection
- `cloud_storage_google_bucket_name` Char “Google Bucket Name”
- `cloud_storage_google_service_account_key` Binary “Google Service Account Key”
- `cloud_storage_google_account_info` Char “Google Service Account Info” (store, compute=_compute_cloud_storage_google_account_info)

Public methods: `get_values`

Extension points: `_check_cloud_storage_uninstallable`, `_get_cloud_storage_configuration`
