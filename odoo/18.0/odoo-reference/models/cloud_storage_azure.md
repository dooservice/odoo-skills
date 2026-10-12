# cloud_storage_azure — Cloud Storage Azure

Depends on: cloud_storage.

## `ir.attachment` (extends)


Extension points: `_get_cloud_storage_azure_info`

## `res.config.settings` (extends)

- `cloud_storage_provider` Selection
- `cloud_storage_azure_account_name` Char “Azure Account Name”
- `cloud_storage_azure_container_name` Char “Azure Container Name”
- `cloud_storage_azure_tenant_id` Char “Azure Tenant ID”
- `cloud_storage_azure_client_id` Char “Azure Client ID”
- `cloud_storage_azure_client_secret` Char “Azure Client Secret”
- `cloud_storage_azure_invalidate_user_delegation_key` Boolean “Invalidate Cached Azure User Delegation Key”

Public methods: `set_values`

Extension points: `_check_cloud_storage_uninstallable`, `_get_cloud_storage_configuration`
