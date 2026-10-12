# base — Base

Depends on: nothing.

## `avatar.mixin` (defines)

Avatar Mixin

Inherits: `image.mixin`

- `avatar_1920` Image “Avatar” (compute=_compute_avatar_1920)
- `avatar_1024` Image “Avatar 1024” (compute=_compute_avatar_1024)
- `avatar_512` Image “Avatar 512” (compute=_compute_avatar_512)
- `avatar_256` Image “Avatar 256” (compute=_compute_avatar_256)
- `avatar_128` Image “Avatar 128” (compute=_compute_avatar_128)

Extension points: `_get_avatar_128_access_token`

## `clearing.label` (defines)

Bank Account Clearing Number Label

- `name` Char (required)
- `country_id` Many2one → `res.country`
- `country_code` Char (related=country_id.code)

## `decimal.precision` (defines)

Decimal Precision

- `name` Char “Usage” (required)
- `digits` Integer “Digits” (required)

Public methods: `precision_get`

## `image.mixin` (defines)

Image Mixin

- `image_1920` Image “Image”
- `image_1024` Image “Image 1024” (store, related=image_1920)
- `image_512` Image “Image 512” (store, related=image_1920)
- `image_256` Image “Image 256” (store, related=image_1920)
- `image_128` Image “Image 128” (store, related=image_1920)

## `ir.access` (defines)

Access

- `name` Char (required)
- `active` Boolean
- `model_id` Many2one → `ir.model` “Model” (required, index)
- `group_id` Many2one → `res.groups` “Group” (index)
- `operation` Selection (required)
- `domain` Char
- `kind` Selection (compute=_compute_kind)
- `is_standard` Boolean (compute=_compute_is_standard)
- `for_read` Boolean “Read”
- `for_write` Boolean “Update”
- `for_create` Boolean “Create”
- `for_unlink` Boolean “Delete”
- `note` Html “Note”

Public methods: `create`, `customize`, `unlink`, `write`

Extension points: `_check_domain`, `_check_model_name`, `_get_access_context`, `_get_all_access`, `_get_failed_accesses`, `_get_groups_with_access`

## `ir.actions.actions` (defines)

Action

- `name` Char “Action Name” (required)
- `type` Char “Action Type” (required)
- `xml_id` Char “External ID” (compute=_compute_xml_id)
- `path` Char “Path to show in the URL”
- `help` Html “Action Description”
- `explanation` Text “Explanation”
- `binding_model_id` Many2one → `ir.model`
- `binding_type` Selection (required)
- `binding_view_types` Char

Public methods: `get_bindings`, `unlink`

Extension points: `_check_path`, `_get_action_dict`, `_get_bindings`, `_get_eval_context`, `_get_readable_fields`

## `ir.actions.act_window` (defines)

Action Window

Inherits: `ir.actions.actions`

- `type` Char
- `view_id` Many2one → `ir.ui.view` “View Ref.”
- `domain` Char “Domain Value”
- `context` Char “Context Value” (required)
- `res_id` Integer “Record ID”
- `res_model` Char “Destination Model” (required)
- `target` Selection “Target Window”
- `view_mode` Char (required)
- `mobile_view_mode` Char
- `usage` Char “Action Usage”
- `view_ids` One2many → `ir.actions.act_window.view` “No of Views”
- `views` Json (compute=_compute_views)
- `limit` Integer
- `group_ids` Many2many → `res.groups` “Groups”
- `search_view_id` Many2one → `ir.ui.view` “Search View Ref.”
- `embedded_action_ids` One2many → `ir.embedded.actions` (compute=_compute_embedded_actions)
- `filter` Boolean
- `cache` Boolean “Data Caching”

Public methods: `create`, `exists`, `read`

Extension points: `_check_model`, `_check_view_mode`, `_get_action_dict`, `_get_readable_fields`

## `ir.actions.act_window.view` (defines)

Action Window View

- `sequence` Integer
- `view_id` Many2one → `ir.ui.view` “View”
- `view_mode` Selection “View Type” (required)
- `act_window_id` Many2one → `ir.actions.act_window` “Action”
- `multi` Boolean “On Multiple Doc.”

## `ir.actions.act_window_close` (defines)

Action Window Close

Inherits: `ir.actions.actions`

- `type` Char

Extension points: `_get_readable_fields`

## `ir.actions.act_url` (defines)

Action URL

Inherits: `ir.actions.actions`

- `type` Char
- `url` Text “Action URL” (required)
- `target` Selection “Action Target” (required)

Extension points: `_get_readable_fields`

## `server.action.history.wizard` (defines)

Server Action History Wizard

- `action_id` Many2one → `ir.actions.server`
- `code_diff` Html (compute=_compute_code_diff)
- `current_code` Text (readonly, related=action_id.code)
- `revision` Many2one → `ir.actions.server.history` (required)

Public methods: `restore_revision`

## `ir.actions.server.history` (defines)

Server Action History

- `action_id` Many2one → `ir.actions.server` (required)
- `code` Text

## `ir.actions.server` (defines)

Server Action

Inherits: `ir.actions.actions`

- `name` Char (store, compute=_compute_name)
- `automated_name` Char (store, compute=_compute_name)
- `type` Char
- `usage` Selection “Usage” (required)
- `state` Selection “Type” (required)
- `allowed_states` Json “Allowed states” (compute=_compute_allowed_states)
- `sequence` Integer
- `model_id` Many2one → `ir.model` “Model” (required, index)
- `available_model_ids` Many2many → `ir.model` “Available Models” (compute=_compute_available_model_ids)
- `model_name` Char “Model Name” (related=model_id.model)
- `warning` Text “Warning” (compute=_compute_warning)
- `ir_cron_ids` One2many → `ir.cron`
- `code` Text “Python Code”
- `show_code_history` Boolean (compute=_compute_show_code_history)
- `parent_id` Many2one → `ir.actions.server` “Parent Action” (index)
- `child_ids` One2many → `ir.actions.server` “Child Actions”
- `crud_model_id` Many2one → `ir.model` “Record to Create” (store, compute=_compute_crud_relations)
- `crud_model_name` Char “Target Model Name” (readonly, related=crud_model_id.model)
- `link_field_id` Many2one → `ir.model.fields` “Link Field”
- `group_ids` Many2many → `res.groups` “Allowed Groups”
- `update_field_id` Many2one → `ir.model.fields` “Field to Update” (store, compute=_compute_crud_relations)
- `update_field_name` Char (related=update_field_id.name)
- `update_property` Char “Property to Update” (store, compute=_compute_crud_relations)
- `update_path` Char “Field to Update Path”
- `update_related_model_id` Many2one → `ir.model` (store, compute=_compute_crud_relations)
- `update_field_type` Selection (readonly, related=update_field_id.ttype)
- `update_m2m_operation` Selection “Many2many Operations”
- `update_boolean_value` Selection “Boolean Value”
- `value` Text
- `evaluation_type` Selection
- `html_value` Html
- `sequence_id` Many2one → `ir.sequence` “Sequence to use”
- `resource_ref` Reference “Record”
- `selection_value` Many2one → `ir.model.fields.selection` “Custom Value”
- `property_selection` Char
- `value_field_to_show` Selection (compute=_compute_value_field_to_show)
- `webhook_url` Char “Webhook URL”
- `webhook_field_ids` Many2many → `ir.model.fields` “Webhook Fields”
- `webhook_sample_payload` Text “Sample Payload” (compute=_compute_webhook_sample_payload)

Public methods: `action_open_parent_action`, `action_open_scheduled_action`, `create`, `create_action`, `history_wizard_action`, `run`, `unlink_action`, `write`

Extension points: `_check_children`, `_check_python_code`, `_get_children_domain`, `_get_eval_context`, `_get_readable_fields`, `_get_relation_chain`, `_get_runner`, `_get_warning_messages`

## `ir.actions.todo` (defines)

Configuration Wizard

- `action_id` Many2one → `ir.actions.actions` “Action” (required, index)
- `sequence` Integer
- `state` Selection “Status” (required)
- `name` Char

Public methods: `action_launch`, `action_open`, `create`, `ensure_one_open_todo`, `unlink`, `write`

## `ir.actions.client` (defines)

Client Action

Inherits: `ir.actions.actions`

- `type` Char
- `tag` Char “Client action tag” (required)
- `target` Selection “Target Window”
- `res_model` Char “Destination Model”
- `context` Char “Context Value” (required)
- `params` Json “Supplementary arguments” (compute=_compute_params)
- `params_store` Text “Params storage” (readonly)

Extension points: `_get_readable_fields`

## `ir.actions.report` (defines)

Report Action

Inherits: `ir.actions.actions`

- `type` Char
- `binding_type` Selection
- `model` Char “Model Name” (required)
- `model_id` Many2one → `ir.model` “Model” (compute=_compute_model_id)
- `report_type` Selection “Format” (required)
- `report_name` Char “Technical Name” (required)
- `group_ids` Many2many → `res.groups` “Groups”
- `multi` Boolean “On Multiple Doc.”
- `paperformat_id` Many2one → `report.paperformat`
- `print_report_name` Char “Printed Report Name”
- `save_as_attachment` Boolean
- `attachment_use` Boolean “Generate new file each time the report is printed”
- `attachment` Char “Attachment Name”
- `domain` Char “Domain”
- `linked_view_ids` Many2many → `ir.ui.view` (compute=_compute_linked_view_ids)
- `linked_view_count` Integer (compute=_compute_linked_view_ids)

Public methods: `associated_view`, `barcode`, `create_action`, `get_available_barcode_masks`, `get_paperformat`, `get_paperformat_by_xmlid`, `get_pdf_engine_state`, `get_valid_action_reports`, `report_action`, `retrieve_attachment`, `unlink_action`

Extension points: `_action_configure_external_report_layout`, `_get_layout`, `_get_pdf_engine`, `_get_readable_fields`, `_get_rendering_context`, `_get_rendering_context_model`, `_get_report`, `_get_report_from_name`, `_get_report_url`, `_prepare_html`, `_prepare_local_attachments`, `_prepare_pdf_report_attachment_vals_list`

## `ir.asset` (defines)

Asset

- `name` Char “Name” (required)
- `bundle` Char “Bundle name” (required)
- `directive` Selection “Directive”
- `path` Char “Path (or glob pattern)” (required)
- `target` Char “Target”
- `active` Boolean “active”
- `sequence` Integer “Sequence” (required)

Extension points: `_get_active_addons_list`, `_get_asset_bundle_url`, `_get_asset_params`, `_get_asset_paths`, `_get_installed_addons_list`, `_get_paths`, `_get_related_assets`, `_get_related_bundle`

## `ir.attachment` (defines)

Attachment

- `name` Char “Name” (required)
- `description` Text “Description”
- `res_name` Char “Resource Name” (compute=_compute_res_name)
- `res_model` Char “Resource Model”
- `res_field` Char “Resource Field”
- `res_id` Many2oneReference “Resource ID”
- `company_id` Many2one → `res.company` “Company”
- `type` Selection “Type” (required)
- `url` Char “Url”
- `public` Boolean “Is public document”
- `res_access_read` Boolean
- `res_access_write` Boolean
- `access_token` Char “Access Token”
- `raw` Binary “File Content (raw)” (compute=_compute_raw)
- `db_datas` Binary “Database Data”
- `store_fname` Char “Stored Filename” (index)
- `file_size` Integer “File Size” (readonly)
- `checksum` Char “Checksum/SHA1” (readonly)
- `mimetype` Char “Mime Type” (readonly)
- `index_content` Text “Indexed Content” (readonly)

Public methods: `action_get`, `check`, `copy_data`, `create`, `create_unique`, `force_storage`, `generate_access_token`, `get_serving_groups`, `regenerate_assets_bundles`, `unlink`, `write`

Extension points: `_check_circular_attachment`, `_check_contents`, `_check_serving_attachments`, `_get_datas_related_values`, `_get_pdf_raw`, `_get_raw_access_token`, `_get_serve_attachment`, `_get_storage_domain`, `_post_add_create`

## `ir.autovacuum` (defines)

Automatic Vacuum


## `ir.binary` (defines)

File streaming helper model for controllers


Extension points: `_get_image_stream_from`, `_get_placeholder_stream`, `_get_stream_from`

## `ir.config_parameter` (defines)

System Parameter

- `key` Char (required)
- `value` Text

Public methods: `get_bool`, `get_float`, `get_int`, `get_str`, `init`, `set_bool`, `set_float`, `set_int`, `set_str`, `unlink_default_parameters`, `write`

## `ir.cron` (defines)

Scheduled Action

- `ir_actions_server_id` Many2one → `ir.actions.server` (required, index)
- `cron_name` Char “Name” (store, compute=_compute_cron_name)
- `user_id` Many2one → `res.users` “Scheduler User” (required)
- `active` Boolean
- `interval_number` Integer (required)
- `interval_type` Selection “Interval Unit” (required)
- `nextcall` Datetime “Next Execution Date” (required)
- `lastcall` Datetime “Last Execution Date”
- `priority` Integer
- `failure_count` Integer
- `first_failure_date` Datetime “First Failure Date”

Public methods: `action_open_parent_action`, `action_open_scheduled_action`, `create`, `default_get`, `method_direct_trigger`, `toggle`, `write`

Extension points: `_check_modules_state`, `_check_version`, `_get_all_ready_jobs`, `_get_ready_sql_condition`

## `ir.cron.trigger` (defines)

Triggered Action

- `cron_id` Many2one → `ir.cron` (required, index)
- `call_at` Datetime (required, index)

## `ir.cron.progress` (defines)

Progress of Scheduled Action

- `cron_id` Many2one → `ir.cron` (required, index)
- `remaining` Integer
- `done` Integer
- `deactivate` Boolean
- `timed_out_counter` Integer

## `ir.default` (defines)

Default Value

- `field_id` Many2one → `ir.model.fields` “Field” (required, index)
- `user_id` Many2one → `res.users` “User” (index)
- `company_id` Many2one → `res.company` “Company” (index)
- `condition` Char “Condition”
- `json_value` Char “Default Value (JSON format)” (required)

Public methods: `create`, `discard_records`, `discard_values`, `set`, `unlink`, `write`

Extension points: `_check_accessible_field_id`, `_check_json_format`, `_get_field_column_fallbacks`, `_get_model_defaults`

## `ir.demo` (defines)

Demo


Public methods: `install_demo`

## `ir.demo_failure` (defines)

Demo failure

- `module_id` Many2one → `ir.module.module` “Module” (required)
- `error` Char “Error”
- `wizard_id` Many2one → `ir.demo_failure.wizard`

## `ir.demo_failure.wizard` (defines)

Demo Failure wizard

- `failure_ids` One2many → `ir.demo_failure` “Demo Installation Failures” (readonly)
- `failures_count` Integer (compute=_compute_failures_count)

Public methods: `done`

## `ir.embedded.actions` (defines)

Embedded Action

- `name` Char
- `sequence` Integer
- `parent_action_id` Many2one → `ir.actions.act_window` “Parent Action” (required)
- `parent_res_id` Integer “Active Parent Id”
- `parent_res_model` Char “Active Parent Model” (required)
- `action_id` Many2one → `ir.actions.actions` “Action”
- `python_method` Char
- `user_id` Many2one → `res.users` “User”
- `is_deletable` Boolean (compute=_compute_is_deletable)
- `default_view_mode` Char “Default View”
- `filter_ids` One2many → `ir.filters`
- `is_visible` Boolean “Embedded visibility” (compute=_compute_is_visible)
- `domain` Char
- `context` Char
- `groups_ids` Many2many → `res.groups`

Public methods: `create`

Extension points: `_get_readable_fields`

## `ir.exports` (defines)

Exports

- `name` Char “Export Name”
- `resource` Char (index)
- `export_fields` One2many → `ir.exports.line` “Export ID”
- `export_language_ids` Many2many → `res.lang` “Languages”

Extension points: `_get_fields_info`, `_get_property_fields`

## `ir.exports.line` (defines)

Exports Line

- `sequence` Integer
- `name` Char “Field Name”
- `export_id` Many2one → `ir.exports` “Export” (index)

## `ir.fields.converter` (defines)

Fields Converter


Public methods: `db_id_for`, `for_model`, `to_field`

Extension points: `_get_boolean_translations`, `_get_import_field_path`, `_get_selection_translations`

## `ir.filters` (defines)

Filter

- `name` Char “Filter Name” (required)
- `user_ids` Many2many → `res.users` “Users”
- `domain` Text (required)
- `context` Text (required)
- `sort` Char (required)
- `model_id` Selection “Model” (required)
- `is_default` Boolean “Default Filter”
- `action_id` Many2one → `ir.actions.actions` “Action”
- `embedded_action_id` Many2one → `ir.embedded.actions`
- `embedded_parent_res_id` Integer
- `active` Boolean

Public methods: `copy_data`, `create`, `create_filter`, `get_filters`, `write`

Extension points: `_get_action_domain`, `_get_eval_domain`

## `ir.http` (defines)

HTTP Routing


Public methods: `routing_map`

Extension points: `_check_identity`, `_get_converters`, `_get_host_id_from_domain`, `_get_public_users`, `_get_translations_for_webclient`, `_get_web_translations_hash`, `_post_dispatch`, `_post_logout`

## `ir.logging` (defines)

Logging

- `create_uid` Integer “Created by” (readonly)
- `create_date` Datetime “Created on” (readonly)
- `write_uid` Integer “Last Updated by” (readonly)
- `write_date` Datetime “Last Updated on” (readonly)
- `name` Char (required)
- `type` Selection (required, index)
- `dbname` Char “Database Name” (index)
- `level` Char (index)
- `message` Text (required)
- `path` Char (required)
- `func` Char “Function” (required)
- `line` Char (required)

Public methods: `init`

## `ir.mail_server` (defines)

Mail Server

- `name` Char “Name” (required, index)
- `from_filter` Char “FROM Filtering”
- `smtp_host` Char “SMTP Server”
- `smtp_port` Integer “SMTP Port”
- `smtp_authentication` Selection “Authenticate with” (required)
- `smtp_authentication_info` Text “Authentication Info” (compute=_compute_smtp_authentication_info)
- `smtp_user` Char “Username”
- `smtp_pass` Char “Password”
- `smtp_encryption` Selection “Connection Encryption” (required)
- `smtp_ssl_certificate` Binary “SSL Certificate”
- `smtp_ssl_private_key` Binary “SSL Private Key”
- `smtp_debug` Boolean “Debugging”
- `sequence` Integer “Priority”
- `active` Boolean

Public methods: `send_email`, `test_smtp_connection`, `write`

Extension points: `_check_forced_mail_server`, `_check_smtp_ssl_files`, `_get_default_bounce_address`, `_get_default_from_address`, `_get_default_from_filter`, `_get_max_email_size`, `_get_test_email_from`, `_get_test_email_to`, `_prepare_email_message__`, `_prepare_smtp_to_list`

## `base` (defines)

Base


## `_unknown` (defines)

Unknown


## `ir.model` (defines)

Model

- `name` Char “Model Description” (required)
- `model` Char (required)
- `order` Char “Order” (required)
- `info` Text “Information”
- `explanation` Text “Explanation”
- `field_id` One2many → `ir.model.fields` “Fields” (required)
- `inherited_model_ids` Many2many → `ir.model` “Inherited models” (compute=_inherited_models)
- `state` Selection “Type” (readonly)
- `access_ids` One2many → `ir.access` “Access”
- `abstract` Boolean “Abstract Model”
- `transient` Boolean “Transient Model”
- `modules` Char “In Apps” (compute=_in_modules)
- `view_ids` One2many → `ir.ui.view` “Views” (compute=_view_ids)
- `count` Integer “Count (Incl. Archived)” (compute=_compute_count)
- `fold_name` Char “Fold Field”

Public methods: `create`, `name_create`, `unlink`, `write`

Extension points: `_check_fold_name`, `_check_manual_name`, `_check_model_name`, `_check_order`, `_get_id`

## `ir.model.fields` (defines)

Field

- `name` Char “Field Name” (required, index)
- `model` Char “Model Name” (required, index)
- `relation` Char “Related Model”
- `relation_field` Char
- `relation_model_field` Char
- `relation_field_id` Many2one → `ir.model.fields` “Relation field” (store, compute=_compute_relation_field_id)
- `model_id` Many2one → `ir.model` “Model” (required, index)
- `field_description` Char “Field Label” (required)
- `help` Text “Field Help”
- `ttype` Selection “Field Type” (required)
- `selection` Char “Selection Options (Deprecated)” (compute=_compute_selection)
- `selection_ids` One2many → `ir.model.fields.selection` “Selection Options”
- `copied` Boolean “Copied” (store, compute=_compute_copied)
- `related` Char “Related Field Definition”
- `related_field_id` Many2one → `ir.model.fields` “Related Field” (store, compute=_compute_related_field_id)
- `required` Boolean
- `readonly` Boolean
- `index` Selection “Index”
- `allowed_index_types` Json (compute=_compute_allowed_index_types)
- `translate` Selection “Translatable”
- `company_dependent` Boolean “Company Dependent” (readonly)
- `size` Integer
- `state` Selection “Type” (required, readonly, index)
- `on_delete` Selection “On Delete”
- `domain` Char
- `groups` Many2many → `res.groups`
- `group_expand` Boolean “Expand Groups”
- `selectable` Boolean
- `modules` Char “In Apps” (compute=_in_modules)
- `relation_table` Char
- `column1` Char “Column 1”
- `column2` Char “Column 2”
- `compute` Text
- `depends` Char “Dependencies”
- `store` Boolean “Stored”
- `currency_field` Char “Currency field”
- `sanitize` Boolean “Sanitize HTML”
- `sanitize_overridable` Boolean “Sanitize HTML overridable”
- `sanitize_tags` Boolean “Sanitize HTML Tags”
- `sanitize_attributes` Boolean “Sanitize HTML Attributes”
- `sanitize_style` Boolean “Sanitize HTML Style”
- `sanitize_form` Boolean “Sanitize HTML Form”
- `strip_style` Boolean “Strip Style Attribute”
- `strip_classes` Boolean “Strip Class Attribute”

Public methods: `create`, `get_field_help`, `get_field_selection`, `get_field_string`, `unlink`, `write`

Extension points: `_check_currency_field`, `_check_depends`, `_check_domain`, `_check_index`, `_check_name`, `_check_on_delete_required_m2o`, `_check_related`, `_check_relation`, `_check_relation_field`, `_check_relation_table`, `_get_allowed_index_types`, `_get_fields_cached`, `_get_ids`, `_get_manual_field_data`, `_get_writable_properties`, `_prepare_update`

## `ir.model.inherit` (defines)

Model Inheritance Tree

- `model_id` Many2one → `ir.model` (required)
- `parent_id` Many2one → `ir.model` (required)
- `parent_field_id` Many2one → `ir.model.fields`

## `ir.model.fields.selection` (defines)

Fields Selection

- `field_id` Many2one → `ir.model.fields` (required, index)
- `value` Char (required)
- `name` Char (required)
- `sequence` Integer

Public methods: `create`, `unlink`, `write`

Extension points: `_get_records`, `_get_selection`, `_get_selection_data`

## `ir.model.constraint` (defines)

Model Constraint

- `name` Char “Constraint” (required, readonly, index)
- `definition` Char (readonly)
- `message` Char
- `model` Many2one → `ir.model` (required, readonly, index)
- `module` Many2one → `ir.module.module` (required, readonly, index)
- `type` Char “Constraint Type” (required, readonly)

Public methods: `unlink`

## `ir.model.relation` (defines)

Relation Model

- `name` Char “Relation Name” (required, index)
- `model` Many2one → `ir.model` (required, index)
- `module` Many2one → `ir.module.module` (required, index)
- `write_date` Datetime
- `create_date` Datetime

## `ir.model.data` (defines)

Model Data

- `name` Char “External Identifier” (required)
- `complete_name` Char “Complete ID” (compute=_compute_complete_name)
- `model` Char “Model Name” (required)
- `module` Char (required)
- `res_id` Many2oneReference “Record ID”
- `noupdate` Boolean “Non Updatable”
- `reference` Char “Reference” (readonly, compute=_compute_reference)

Public methods: `check_object_reference`, `copy_data`, `create`, `toggle_noupdate`, `unlink`, `write`

## `ir.module.category` (defines)

Application

- `name` Char “Name” (required)
- `parent_id` Many2one → `ir.module.category` “Parent Application” (index)
- `child_ids` One2many → `ir.module.category` “Child Applications”
- `module_ids` One2many → `ir.module.module` “Modules”
- `privilege_ids` One2many → `res.groups.privilege` “Privileges”
- `description` Text “Description”
- `sequence` Integer “Sequence”
- `visible` Boolean “Visible”
- `exclusive` Boolean “Exclusive”
- `xml_id` Char “External ID” (compute=_compute_xml_id)

Extension points: `_check_parent_not_circular`

## `ir.module.module` (defines)

Module

- `name` Char “Technical Name” (required, readonly)
- `category_id` Many2one → `ir.module.category` “Category” (readonly, index)
- `shortdesc` Char “Module Name” (readonly)
- `summary` Char “Summary” (readonly)
- `description` Text “Description” (readonly)
- `description_html` Html “Description HTML” (compute=_get_desc)
- `author` Char “Author” (readonly)
- `maintainer` Char “Maintainer” (readonly)
- `contributors` Text “Contributors” (readonly)
- `website` Char “Website” (readonly)
- `installed_version` Char “Latest Version” (compute=_get_latest_version)
- `latest_version` Char “Installed Version” (readonly)
- `published_version` Char “Published Version” (readonly)
- `url` Char “URL” (readonly)
- `sequence` Integer “Sequence”
- `dependencies_id` One2many → `ir.module.module.dependency` “Dependencies” (readonly)
- `country_ids` Many2many → `res.country`
- `exclusion_ids` One2many → `ir.module.module.exclusion` “Exclusions” (readonly)
- `auto_install` Boolean “Automatic Installation”
- `state` Selection “Status” (readonly, index)
- `demo` Boolean “Demo Data” (readonly)
- `test_data` Boolean “Test Data” (readonly)
- `license` Selection “License” (readonly)
- `menus_by_module` Text “Menus” (store, compute=_get_views)
- `reports_by_module` Text “Reports” (store, compute=_get_views)
- `views_by_module` Text “Views” (store, compute=_get_views)
- `application` Boolean “Application” (readonly)
- `icon` Char “Icon URL”
- `icon_image` Binary “Icon” (compute=_get_icon_image)
- `icon_flag` Char “Flag” (compute=_get_icon_image)
- `to_buy` Boolean “Odoo Enterprise Module”
- `iap_paid_service` Boolean “Contains In-App Purchases”

Public methods: `button_immediate_install`, `button_immediate_uninstall`, `button_immediate_upgrade`, `button_install`, `button_reset_state`, `button_uninstall`, `button_uninstall_wizard`, `button_upgrade`, `check_external_dependencies`, `check_module_update`, `create`, `downstream_dependencies`, `get_module_info`, `get_values_from_terp`, `module_uninstall`, `next`, `search_panel_select_range`, `update_list`, `upstream_dependencies`

Extension points: `_get_desc`, `_get_icon_image`, `_get_id`, `_get_latest_version`, `_get_modules_to_load_domain`, `_get_views`

## `ir.module.module.dependency` (defines)

Module dependency

- `name` Char (index)
- `module_id` Many2one → `ir.module.module`
- `depend_id` Many2one → `ir.module.module` (compute=_compute_depend)
- `state` Selection “Status” (compute=_compute_state)
- `auto_install_required` Boolean

Public methods: `all_dependencies`

## `ir.module.module.exclusion` (defines)

Module exclusion

- `name` Char (index)
- `module_id` Many2one → `ir.module.module`
- `exclusion_id` Many2one → `ir.module.module` (compute=_compute_exclusion)
- `state` Selection “Status” (compute=_compute_state)

## `ir.profile` (defines)

Profiling Result

- `create_date` Datetime “Creation Date”
- `session` Char “Session” (index)
- `name` Char “Description”
- `duration` Float “Duration”
- `cpu_duration` Float “CPU Duration”
- `init_stack_trace` Text “Initial stack trace”
- `sql` Text “Sql”
- `sql_count` Integer “Queries Count”
- `traces_async` Text “Traces Async”
- `others` Text “others”
- `qweb` Text “Qweb”
- `entry_count` Integer “Entry count”
- `profile_query_ids` One2many → `ir.profile.query`
- `speedscope` Binary “Speedscope” (compute=_compute_speedscope)
- `speedscope_url` Text “Open” (compute=_compute_speedscope_url)
- `config_url` Text “Open profiles config” (compute=_compute_config_url)

Public methods: `action_open_sql_queries`, `action_view_speedscope`, `set_profiling`

Extension points: `_get_memory_data`

## `base.enable.profiling.wizard` (defines)

Enable profiling for some time

- `duration` Selection “Enable profiling for”
- `expiration` Datetime “Enable profiling until” (store, compute=_compute_expiration)

Public methods: `submit`

## `ir.profile.query` (defines)

Profiling Query

- `profile_id` Many2one → `ir.profile` (required, index)
- `time` Float “Time”
- `query` Text (readonly)
- `full_query` Text (required)
- `query_preview` Text (compute=_compute_query_preview)
- `formatted_query` Text (compute=_compute_formatted_query)
- `plan` Text “Query Plan”

Public methods: `action_explain_analyse`

## `ir.qweb` (defines)

Qweb


Extension points: `_get_asset_bundle`, `_get_asset_content`, `_get_asset_link_urls`, `_get_asset_links`, `_get_asset_nodes`, `_get_bundles_from_views`, `_get_bundles_to_pregenarate`, `_get_converted_image_data_uri`, `_get_error_info`, `_get_field`, `_get_lazy_bundles_from_js`, `_get_preload_attribute_xmlids`, `_get_template`, `_get_template_cache_keys`, `_get_template_info`, `_get_widget`, `_post_processing_att`, `_prepare_environment`

## `ir.qweb.field` (defines)

Qweb Field


Public methods: `attributes`, `get_available_options`, `record_to_html`, `user_lang`, `value_to_html`

## `ir.qweb.field.integer` (defines)

Qweb Field Integer

Inherits: `ir.qweb.field`


Public methods: `get_available_options`, `value_to_html`

## `ir.qweb.field.float` (defines)

Qweb Field Float

Inherits: `ir.qweb.field`


Public methods: `get_available_options`, `record_to_html`, `value_to_html`

## `ir.qweb.field.date` (defines)

Qweb Field Date

Inherits: `ir.qweb.field`


Public methods: `get_available_options`, `value_to_html`

## `ir.qweb.field.datetime` (defines)

Qweb Field Datetime

Inherits: `ir.qweb.field`


Public methods: `get_available_options`, `value_to_html`

## `ir.qweb.field.text` (defines)

Qweb Field Text

Inherits: `ir.qweb.field`


Public methods: `attributes`, `value_to_html`

## `ir.qweb.field.selection` (defines)

Qweb Field Selection

Inherits: `ir.qweb.field`


Public methods: `get_available_options`, `record_to_html`, `value_to_html`

## `ir.qweb.field.many2one` (defines)

Qweb Field Many to One

Inherits: `ir.qweb.field`


Public methods: `value_to_html`

## `ir.qweb.field.many2many` (defines)

Qweb field many2many

Inherits: `ir.qweb.field`


Public methods: `value_to_html`

## `ir.qweb.field.one2many` (defines)

Qweb field one2many

Inherits: `ir.qweb.field`


Public methods: `value_to_html`

## `ir.qweb.field.html` (defines)

Qweb Field HTML

Inherits: `ir.qweb.field`


Public methods: `value_to_html`

Extension points: `_post_processing_att`

## `ir.qweb.field.image` (defines)

Qweb Field Image

Inherits: `ir.qweb.field`


Public methods: `value_to_html`

Extension points: `_get_src_data_b64`

## `ir.qweb.field.image_url` (defines)

Qweb Field Image

Inherits: `ir.qweb.field.image`


Public methods: `value_to_html`

## `ir.qweb.field.monetary` (defines)

Qweb Field Monetary

Inherits: `ir.qweb.field`


Public methods: `get_available_options`, `record_to_html`, `value_to_html`

## `ir.qweb.field.float_time` (defines)

Qweb Field Float Time

Inherits: `ir.qweb.field`


Public methods: `value_to_html`

## `ir.qweb.field.time` (defines)

QWeb Field Time

Inherits: `ir.qweb.field`


Public methods: `value_to_html`

## `ir.qweb.field.duration` (defines)

Qweb Field Duration

Inherits: `ir.qweb.field`


Public methods: `get_available_options`, `value_to_html`

## `ir.qweb.field.relative` (defines)

Qweb Field Relative

Inherits: `ir.qweb.field`


Public methods: `get_available_options`, `record_to_html`, `value_to_html`

## `ir.qweb.field.barcode` (defines)

Qweb Field Barcode

Inherits: `ir.qweb.field`


Public methods: `get_available_options`, `value_to_html`

## `ir.qweb.field.contact` (defines)

Qweb Field Contact

Inherits: `ir.qweb.field.many2one`


Public methods: `get_available_options`, `value_to_html`

## `ir.qweb.field.qweb` (defines)

Qweb Field qweb

Inherits: `ir.qweb.field.many2one`


Public methods: `record_to_html`

## `ir.sequence` (defines)

Sequence

- `name` Char (required)
- `code` Char “Sequence Code”
- `implementation` Selection “Implementation” (required)
- `active` Boolean
- `prefix` Char
- `suffix` Char
- `number_next` Integer “Next Number” (required)
- `number_next_actual` Integer “Actual Next Number” (compute=_get_number_next_actual)
- `number_increment` Integer “Step” (required)
- `padding` Integer “Sequence Size” (required)
- `company_id` Many2one → `res.company` “Company”
- `use_date_range` Boolean “Use subsequences per date_range”
- `date_range_ids` One2many → `ir.sequence.date_range` “Subsequences”

Public methods: `create`, `get_next_char`, `next_by_code`, `next_by_id`, `unlink`, `write`

Extension points: `_create_date_range_seq`, `_get_current_sequence`, `_get_number_next_actual`, `_get_prefix_suffix`

## `ir.sequence.date_range` (defines)

Sequence Date Range

- `date_from` Date “From” (required)
- `date_to` Date “To” (required)
- `sequence_id` Many2one → `ir.sequence` “Main Sequence” (required)
- `number_next` Integer “Next Number” (required)
- `number_next_actual` Integer “Actual Next Number” (compute=_get_number_next_actual)

Public methods: `create`, `default_get`, `unlink`, `write`

Extension points: `_get_number_next_actual`

## `ir.ui.menu` (defines)

Menu

- `name` Char “Menu” (required)
- `active` Boolean
- `sequence` Integer
- `child_id` One2many → `ir.ui.menu` “Child IDs”
- `parent_id` Many2one → `ir.ui.menu` “Parent Menu” (index)
- `parent_path` Char (index)
- `group_ids` Many2many → `res.groups` “Groups”
- `complete_name` Char “Full Path” (compute=_compute_complete_name)
- `web_icon` Char “Web Icon File”
- `action` Reference
- `web_icon_data` Binary “Web Icon Image”

Public methods: `copy`, `create`, `get_user_roots`, `load_menus`, `load_menus_root`, `unlink`, `write`

Extension points: `_get_full_name`, `_get_menuitems_xmlids`

## `ir.ui.view.custom` (defines)

Custom View

- `ref_id` Many2one → `ir.ui.view` “Original View” (required, index)
- `user_id` Many2one → `res.users` “User” (required, index)
- `arch` Text “View Architecture” (required)

## `ir.ui.view` (defines)

View

- `name` Char “View Name” (required)
- `model` Char (index)
- `key` Char
- `priority` Integer “Sequence” (required)
- `type` Selection “View Type”
- `arch` Text “View Architecture” (compute=_compute_arch)
- `arch_base` Text “Base View Architecture” (compute=_compute_arch_base)
- `arch_db` Text “Arch Blob”
- `arch_fs` Char “Arch Filename”
- `arch_updated` Boolean “Modified Architecture”
- `arch_prev` Text “Previous View Architecture”
- `inherit_id` Many2one → `ir.ui.view` “Inherited View” (index)
- `inherit_children_ids` One2many → `ir.ui.view` “Views which inherit from this one”
- `model_data_id` Many2one → `ir.model.data` “Model Data” (compute=_compute_model_data_id)
- `xml_id` Char “External ID” (compute=_compute_xml_id)
- `group_ids` Many2many → `res.groups` “Groups”
- `mode` Selection “View inheritance mode” (required)
- `warning_info` Html “Warning information” (compute=_compute_warning_info)
- `notes` Html “Notes”
- `active` Boolean
- `model_id` Many2one → `ir.model` “Model of the view” (compute=_compute_model_id)
- `invalid_locators` Json (compute=_compute_invalid_locators)
- `technical_usage` Selection “Technical Usage”

Public methods: `apply_inheritance_specs`, `copy_data`, `create`, `default_view`, `distribute_branding`, `get_combined_arch`, `inherit_branding`, `is_node_branded`, `locate_node`, `postprocess_and_fields`, `render_public_asset`, `reset_arch`, `unlink`, `write`

Extension points: `_check_000_inheritance`, `_check_dropdown_menu`, `_check_field_paths`, `_check_groups`, `_check_progress_bar`, `_check_view_access`, `_check_xml`, `_create_all_specific_views`, `_get_access_groups`, `_get_cached_template_info`, `_get_cached_template_prefetched_keys`, `_get_combined_arch`, `_get_combined_archs`, `_get_default_view_domain`, `_get_filter_xmlid_query`, `_get_inheriting_views`, `_get_inheriting_views_domain`, `_get_specific_views`, `_get_template_domain`, `_get_template_minimal_cache_keys`, `_get_template_order`, `_get_template_view`, `_get_view_etrees`, `_get_view_refs`, `_get_x2many_missing_view_archs`

## `reset.view.arch.wizard` (defines)

Reset View Architecture Wizard

- `view_id` Many2one → `ir.ui.view` “View”
- `view_name` Char “View Name” (related=view_id.name)
- `has_diff` Boolean (compute=_compute_arch_diff)
- `arch_diff` Html “Architecture Diff” (readonly, compute=_compute_arch_diff)
- `reset_mode` Selection “Reset Mode” (required)
- `compare_view_id` Many2one → `ir.ui.view` “Compare To View”
- `arch_to_compare` Text “Arch To Compare To” (compute=_compute_arch_diff)

Public methods: `default_get`, `reset_view_button`

## `base` (extends)


Public methods: `get_empty_list_help`, `get_formview_id`, `get_record_default_action`, `get_view`, `get_views`, `view_header_get`

Extension points: `_get_access_action`, `_get_default_calendar_view`, `_get_default_form_view`, `_get_default_graph_view`, `_get_default_kanban_view`, `_get_default_list_view`, `_get_default_pivot_view`, `_get_default_search_view`, `_get_fields_spec`, `_get_records_action`, `_get_view`, `_get_view_cache`, `_get_view_cache_key`, `_get_view_field_attributes`, `_get_view_fields`, `_get_view_postprocessed`

## `properties.base.definition` (defines)

Properties Base Definition

- `properties_field_id` Many2one → `ir.model.fields` (required)
- `properties_definition` PropertiesDefinition “Properties Definition”

Public methods: `write`

Extension points: `_check_properties_field_id`, `_get_definition_for_property_field`, `_get_definition_id_for_property_field`

## `properties.base.definition.mixin` (defines)

Properties Base Definition Mixin

- `properties` Properties “Properties”
- `properties_base_definition_id` Many2one → `properties.base.definition` (compute=_compute_properties_base_definition_id)

Public methods: `create`

## `report.layout` (defines)

Report Layout

- `view_id` Many2one → `ir.ui.view` (required)
- `image` Char “Preview image src”
- `pdf` Char “Preview pdf src”
- `sequence` Integer
- `name` Char

## `report.paperformat` (defines)

Paper Format Config

- `name` Char “Name” (required)
- `default` Boolean “Default paper format?”
- `format` Selection
- `margin_top` Float “Top Margin (mm)”
- `margin_bottom` Float “Bottom Margin (mm)”
- `margin_left` Float “Left Margin (mm)”
- `margin_right` Float “Right Margin (mm)”
- `page_height` Integer “Page height (mm)”
- `page_width` Integer “Page width (mm)”
- `orientation` Selection
- `header_line` Boolean “Display a header line”
- `header_spacing` Integer “Header spacing”
- `disable_shrinking` Boolean “Disable smart shrinking”
- `dpi` Integer “Output DPI” (required)
- `report_ids` One2many → `ir.actions.report`
- `print_page_width` Float “Print page width (mm)” (compute=_compute_print_page_size)
- `print_page_height` Float “Print page height (mm)” (compute=_compute_print_page_size)
- `css_margins` Boolean “Use css margins”

Extension points: `_check_format_or_page`

## `res.company` (defines)

Company

Inherits: `format.address.mixin`, `format.vat.label.mixin`

- `name` Char “Company Name” (required, store, related=partner_id.name)
- `active` Boolean
- `sequence` Integer
- `parent_id` Many2one → `res.company` “Parent Company” (index)
- `child_ids` One2many → `res.company` “Branches”
- `all_child_ids` One2many → `res.company`
- `parent_path` Char (index)
- `parent_ids` Many2many → `res.company` (compute=_compute_parent_ids)
- `root_id` Many2one → `res.company` (compute=_compute_parent_ids)
- `partner_id` Many2one → `res.partner` “Partner” (required, index)
- `report_header` Html “Company Tagline”
- `report_footer` Html “Report Footer”
- `company_details` Html “Company Details” (store, compute=_compute_parent_fields)
- `is_company_details_empty` Boolean (compute=_compute_empty_company_details)
- `logo` Binary “Company Logo” (related=partner_id.image_1920)
- `logo_web` Binary (store, compute=_compute_logo_web)
- `uses_default_logo` Boolean (store, compute=_compute_uses_default_logo)
- `currency_id` Many2one → `res.currency` “Currency” (required)
- `user_ids` Many2many → `res.users` “Accepted Users”
- `street` Char (compute=_compute_address)
- `street2` Char (compute=_compute_address)
- `zip` Char (compute=_compute_address)
- `city` Char (compute=_compute_address)
- `state_id` Many2one → `res.country.state` “Fed. State” (compute=_compute_address)
- `bank_ids` One2many (related=partner_id.bank_ids)
- `country_id` Many2one → `res.country` “Country” (compute=_compute_address)
- `country_code` Char (related=country_id.code)
- `email` Char (store, related=partner_id.email)
- `phone` Char (store, related=partner_id.phone)
- `website` Char (related=partner_id.website)
- `vat` Char “Tax ID” (related=partner_id.vat)
- `has_vat` Boolean (related=partner_id.has_vat)
- `additional_identifiers` Json (related=partner_id.additional_identifiers)
- `available_additional_identifiers_metadata` Json (related=partner_id.available_additional_identifiers_metadata)
- `paperformat_id` Many2one → `report.paperformat`
- `external_report_layout_id` Many2one → `ir.ui.view`
- `report_tables_id` Selection “Table Design”
- `font` Selection
- `primary_color` Char
- `secondary_color` Char
- `color` Integer (compute=_compute_color)
- `uninstalled_l10n_module_ids` Many2many → `ir.module.module` (compute=_compute_uninstalled_l10n_module_ids)

Public methods: `action_all_company_branches`, `copy`, `create`, `init`, `install_l10n_modules`, `write`

Extension points: `_check_active`, `_check_root_delegated_fields`, `_get_company_address_field_names`, `_get_company_address_update`, `_get_company_root_delegated_field_names`, `_get_logo`, `_get_main_company`, `_get_public_user`, `_get_view`, `_get_zeep_cache__`, `_get_zeep_client__`

## `res.config` (defines)

Config


Public methods: `action_cancel`, `action_next`, `action_skip`, `cancel`, `execute`, `next`, `start`

## `res.config.settings` (defines)

Config Settings


Public methods: `action_open_template_user`, `cancel`, `copy`, `create`, `default_get`, `execute`, `get_config_warning`, `get_option_name`, `get_option_path`, `get_values`, `set_values`

Extension points: `_get_classified_fields`

## `res.country` (defines)

Country

- `name` Char “Country Name” (required)
- `code` Char “Country Code” (required)
- `address_format` Text “Layout in Reports”
- `address_view_id` Many2one → `ir.ui.view` “Input View”
- `currency_id` Many2one → `res.currency` “Currency”
- `image_url` Char “Flag” (compute=_compute_image_url)
- `phone_code` Integer “Phone Prefix”
- `country_group_ids` Many2many → `res.country.group` “Country Groups”
- `country_group_codes` Json (compute=_compute_country_group_codes)
- `state_ids` One2many → `res.country.state` “States”
- `name_position` Selection “Customer Name Position”
- `vat_label` Char “Vat Label”
- `state_required` Boolean
- `zip_applicability` Selection “Zip” (required)

Public methods: `create`, `get_address_fields`, `name_search`, `write`

Extension points: `_check_address_format`

## `res.country.group` (defines)

Country Group

- `name` Char (required)
- `code` Char “Code”
- `country_ids` Many2many → `res.country` “Countries”

Public methods: `create`, `write`

## `res.country.state` (defines)

Country state

- `country_id` Many2one → `res.country` “Country” (required, index)
- `name` Char “State Name” (required)
- `code` Char “State Code” (required)

Public methods: `name_search`

Extension points: `_get_name_search_domain`

## `res.currency` (defines)

Currency

- `name` Char “Currency” (required)
- `iso_numeric` Integer “Currency numeric code.”
- `full_name` Char “Name”
- `symbol` Char (required)
- `rate` Float “Current Rate” (compute=_compute_current_rate)
- `inverse_rate` Float (readonly, compute=_compute_current_rate)
- `rate_string` Char (compute=_compute_current_rate)
- `rate_date` Date “Last Rate Update” (compute=_compute_current_rate)
- `rate_ids` One2many → `res.currency.rate` “Rates”
- `rounding` Float “Rounding Factor”
- `decimal_places` Integer (store, compute=_compute_decimal_places)
- `active` Boolean
- `position` Selection “Symbol Position”
- `currency_unit_label` Char “Currency Unit”
- `currency_subunit_label` Char “Currency Subunit”
- `is_current_company_currency` Boolean (compute=_compute_is_current_company_currency)

Public methods: `amount_to_text`, `compare_amounts`, `create`, `format`, `get_all_currencies`, `is_zero`, `round`, `unlink`, `write`

Extension points: `_check_company_currency_stays_active`, `_get_conversion_rate`, `_get_rates`

## `res.currency.rate` (defines)

Currency Rate

- `name` Date “Date” (required, index)
- `rate` Float “Technical Rate”
- `company_rate` Float (compute=_compute_company_rate)
- `inverse_company_rate` Float (compute=_compute_inverse_company_rate)
- `currency_id` Many2one → `res.currency` “Currency” (required, readonly, index)
- `company_id` Many2one → `res.company` “Company”
- `company_currency_id` Many2one → `res.currency` “Company Currency” (compute=_compute_company_currency_id)

Public methods: `create`, `write`

Extension points: `_check_company_id`, `_get_last_rates_for_companies`, `_get_latest_rate`

## `res.device.log` (defines)

Device Log

- `session_identifier` Char “Session Identifier” (required)
- `user_id` Integer “User” (required)
- `ip_address` Char “IP Address” (required)
- `user_agent` Char “User Agent” (required)
- `country` Char “Country”
- `city` Char “City”
- `first_activity` Datetime “First Activity” (required)
- `last_activity` Datetime “Last Activity” (required)
- `revoked` Boolean “Revoked”

## `res.device` (defines)

Device

- `session_identifier` Char “Session identifier” (readonly)
- `user_id` Many2one → `res.users` “User” (readonly)
- `ip_address` Char “IP Address” (readonly)
- `country` Char “Country” (readonly)
- `city` Char “City” (readonly)
- `user_agent` Char “User Agent” (readonly)
- `first_activity` Datetime “First Activity” (readonly)
- `last_activity` Datetime “Last Activity” (readonly)
- `revoked` Boolean “Revoked” (readonly)
- `platform` Char “Platform” (readonly, compute=_compute_device_info)
- `browser` Char “Browser” (readonly, compute=_compute_device_info)
- `browser_version` Char “Browser Version” (readonly, compute=_compute_device_info)
- `browser_language` Char “Browser Language” (readonly, compute=_compute_device_info)
- `device_type` Char “Type” (readonly, compute=_compute_device_info)
- `is_current` Boolean “Current” (readonly, compute=_compute_is_current)

Public methods: `init`

## `res.session` (defines)

Session

Inherits: `res.device`

- `device_ids` One2many → `res.device` (readonly, compute=_compute_session_info)
- `ip_address` Char “IP Address” (readonly, compute=_compute_session_info)
- `user_agent` Char “User Agent” (readonly, compute=_compute_session_info)
- `country` Char “Country” (readonly, compute=_compute_session_info)
- `city` Char “City” (readonly, compute=_compute_session_info)
- `first_activity` Datetime “First Activity” (readonly, compute=_compute_session_info)
- `is_current` Boolean “Current” (readonly, compute=_compute_is_current)

Public methods: `revoke`

## `res.groups` (defines)

Access Groups

- `name` Char (required)
- `user_ids` Many2many → `res.users`
- `all_user_ids` Many2many → `res.users` “Users and implied users” (compute=_compute_all_user_ids)
- `all_users_count` Integer “# Users” (compute=_compute_all_users_count)
- `access_ids` One2many → `ir.access` “Access Rules”
- `access_count` Integer (compute=_compute_access_count)
- `menu_access` Many2many → `ir.ui.menu` “Access Menu”
- `view_access` Many2many → `ir.ui.view` “Views”
- `comment` Text “Notes”
- `full_name` Char “Group Name” (compute=_compute_full_name)
- `share` Boolean “Share Group”
- `api_key_duration` Float “API Keys maximum duration days”
- `sequence` Integer “Sequence”
- `privilege_id` Many2one → `res.groups.privilege` “Scope” (index)
- `view_group_hierarchy` Json “Technical field for default group setting” (compute=_compute_view_group_hierarchy)
- `implied_ids` Many2many → `res.groups` “Implied Groups”
- `implied_count` Integer (compute=_compute_implied_count)
- `all_implied_ids` Many2many → `res.groups` “Transitively Implied Groups” (compute=_compute_all_implied_ids)
- `implied_by_ids` Many2many → `res.groups` “Implying Groups”
- `implied_by_count` Integer (compute=_compute_implied_by_count)
- `all_implied_by_ids` Many2many → `res.groups` “Transitively Implying Groups” (compute=_compute_all_implied_by_ids)
- `disjoint_ids` Many2many → `res.groups` “Disjoint Groups” (compute=_compute_disjoint_ids)

Public methods: `action_show_all_users`, `action_view_access_ids`, `action_view_implied_by_ids`, `action_view_implied_ids`, `create`, `unlink`, `write`

Extension points: `_check_disjoint_groups`, `_check_inherited_view_groups`, `_check_user_disjoint_groups`, `_get_group_definitions`, `_get_internal_group_ids`, `_get_light_group_xmlids`, `_get_user_type_groups`, `_get_view_group_hierarchy`

## `res.groups.privilege` (defines)

Privilege

- `name` Char “Name” (required)
- `description` Text “Description”
- `placeholder` Char “No group label”
- `sequence` Integer “Sequence”
- `category_id` Many2one → `ir.module.category` “Category” (index)
- `group_ids` One2many → `res.groups` “Groups”

## `res.lang` (defines)

Language

- `name` Char (required)
- `code` Char “Locale Code” (required)
- `iso_code` Char “ISO code”
- `url_code` Char “URL Code” (required)
- `active` Boolean
- `direction` Selection (required)
- `date_format` Selection “Date Format” (required)
- `time_format` Selection “Time Format” (required)
- `week_start` Selection “First Day of Week” (required)
- `grouping` Selection “Separator Format” (required)
- `decimal_point` Char “Decimal Separator” (required)
- `thousands_sep` Char “Thousands Separator”
- `flag_image` Image “Image”
- `flag_image_url` Char (compute=_compute_field_flag_image_url)

Public methods: `action_activate_langs`, `action_unarchive`, `create`, `format`, `get_installed`, `install_lang`, `write`

Extension points: `_check_active`, `_check_format`, `_create_lang`, `_get_active_by`, `_get_active_langs`, `_get_code`, `_get_data`, `_get_date_format_selection`

## `format.vat.label.mixin` (defines)

Country Specific VAT Label


Public methods: `fields_get`

## `format.address.mixin` (defines)

Address Format


Extension points: `_get_view`, `_get_view_cache_key`

## `res.partner.category` (defines)

Partner Tag

- `name` Char “Name” (required)
- `color` Integer “Color”
- `active` Boolean
- `parent_path` Char (index)

Extension points: `_get_default_color`

## `res.partner` (defines)

Contact

Inherits: `format.address.mixin`, `format.vat.label.mixin`, `avatar.mixin`, `properties.base.definition.mixin`

- `name` Char (index)
- `complete_name` Char (store, index, compute=_compute_complete_name)
- `parent_name` Char “Parent name” (readonly, related=parent_id.name)
- `ref` Char “Reference” (index)
- `lang` Selection “Language” (store, compute=_compute_lang)
- `active_lang_count` Integer (compute=_compute_active_lang_count)
- `tz` Selection “Timezone”
- `tz_offset` Char “Timezone offset” (compute=_compute_tz_offset)
- `vat` Char “Tax ID”
- `has_vat` Boolean “Has Tax ID” (compute=_compute_has_vat)
- `additional_identifiers` Json “Additional Identifiers”
- `available_additional_identifiers_metadata` Json (compute=_compute_available_additional_identifiers_metadata)
- `vat_label` Char “Tax ID Label” (compute=_compute_vat_label)
- `website` Char “Website Link”
- `comment` Html “Notes”
- `active` Boolean
- `employee` Boolean
- `function` Char “Job Position”
- `type` Selection “Address Type”
- `type_address_label` Char “Address Type Description” (compute=_compute_type_address_label)
- `street` Char
- `street2` Char
- `zip` Char
- `city` Char
- `country_code` Char “Country Code” (related=country_id.code)
- `partner_latitude` Float “Latitude”
- `partner_longitude` Float “Longitude”
- `email` Char
- `email_formatted` Char “Formatted Email” (compute=_compute_email_formatted)
- `phone` Char
- `is_company` Boolean “Is a Company” (store, compute=_compute_is_company)
- `is_public` Boolean (compute=_compute_is_public)
- `color` Integer “Color Index”
- `partner_share` Boolean “Share Partner” (store, compute=_compute_partner_share)
- `contact_address` Char “Complete Address” (compute=_compute_address)
- `address` Char “Address (without name)” (compute=_compute_address)
- `contact_address_inline` Char “Complete Address inline” (compute=_compute_address)
- `address_inline` Char “Address inline (without name)” (compute=_compute_address)
- `commercial_company_name` Char “Company Name Entity” (store, related=commercial_partner_id.name)
- `barcode` Char (company_dependent)
- `application_statistics` Json “Stats” (compute=_compute_application_statistics)

Public methods: `address_get`, `check_vat_al`, `check_vat_br`, `check_vat_ch`, `check_vat_cr`, `check_vat_de`, `check_vat_do`, `check_vat_ec`, `check_vat_gr`, `check_vat_gt`, `check_vat_hu`, `check_vat_id`, `check_vat_ie`, `check_vat_il`, `check_vat_in`, `check_vat_jp`, `check_vat_ma`, `check_vat_mx`, `check_vat_no`, `check_vat_pe`, `check_vat_ph`, `check_vat_pk`, `check_vat_ro`, `check_vat_rs`, `check_vat_sa`, `check_vat_th`, `check_vat_tr`, `check_vat_tw`, `check_vat_ua`, `check_vat_uy`, `check_vat_uz`, `check_vat_ve`, `check_vat_vn`, `country_name`, `create`, `default_get`, `find_or_create`, `format_vat_al`, `format_vat_ca`, `format_vat_ch`, `format_vat_cl`, `format_vat_co`, `format_vat_eu`, `format_vat_hu`, `format_vat_is`, `format_vat_pk`, `format_vat_sm`, `format_vat_vn`, `get_import_templates`, `is_valid_ruc_ec`, `name_create`, `onchange_parent_id`, `open_commercial_entity`, `view_header_get`, `write`

Extension points: `_check_additional_identifiers`, `_check_barcode_unicity`, `_check_import_consistency`, `_check_parent_id`, `_check_partner_company`, `_check_vat`, `_check_vat_number`, `_create_contact_parent_company`, `_create_parent_from_name`, `_get_additional_identifier`, `_get_address_format`, `_get_address_values`, `_get_all_additional_identifiers_metadata`, `_get_all_addr`, `_get_all_identifiers`, `_get_all_identifiers_metadata`, `_get_all_identifiers_metadata_by_scheme`, `_get_allowed_identifier_metadata_keys`, `_get_commercial_values`, `_get_complete_name`, `_get_country_specific_vat_variants`, `_get_default_address_format`, `_get_identifier_fields`, `_get_identifier_label`, `_get_legal_entity_category_priority`, `_get_preferred_legal_entity_identifier_vals`, `_get_preferred_tax_identifier_vals`, `_get_res_city_by_name`, `_get_street_split`, `_get_synced_commercial_values`, `_get_tax_category_priority`, `_prepare_display_address`

## `res.partner.industry` (defines)

Industry

- `name` Char “Name”
- `full_name` Char “Full Name”
- `active` Boolean “Active”

## `res.partner.bank` (defines)

Bank Account

- `active` Boolean
- `account_type` Selection “Type” (compute=_compute_account_type)
- `account_number` Char “Account Number” (required)
- `sanitized_account_number` Char “Sanitized Account Number” (readonly, store, compute=_compute_sanitized_account_number)
- `holder_name` Char “Holder Name” (store, compute=_compute_account_holder_name)
- `partner_id` Many2one → `res.partner` “Partner” (required, index)
- `allow_out_payment` Boolean “Send Money”
- `bank_name` Char
- `street` Char
- `street2` Char
- `zip` Char
- `city` Char
- `state_id` Many2one → `res.country.state` “Fed. State”
- `country_id` Many2one → `res.country` (store, compute=_compute_country_id)
- `country_code` Char (related=country_id.code)
- `bank_bic` Char “BIC/SWIFT” (index)
- `clearing_label_id` Many2one → `clearing.label` (required, store, compute=_compute_clearing_label_id)
- `clearing_number` Char “Clearing Number”
- `show_clearing_number` Boolean (compute=_compute_show_clearing_number)
- `sequence` Integer
- `company_id` Many2one → `res.company` (index)
- `note` Text “Notes”
- `color` Integer (compute=_compute_color)

Public methods: `create`, `open_linked_partner_id`, `retrieve_account_type`, `write`

Extension points: `_check_clearing_number`, `_get_clearing_number`

## `res.users.log` (defines)

Users Log

- `create_uid` Many2one → `res.users` “Created by” (readonly, index)

## `res.users` (defines)

User

- `partner_id` Many2one → `res.partner` “Related Partner” (required, index)
- `login` Char (required)
- `password` Char (compute=_compute_password)
- `new_password` Char “Set Password” (compute=_compute_password)
- `api_key_ids` One2many → `res.users.apikeys` “API Keys”
- `signature` Html “Email Signature” (store, compute=_compute_signature)
- `active` Boolean
- `active_partner` Boolean “Partner is Active” (readonly, related=partner_id.active)
- `action_id` Many2one → `ir.actions.actions` “Home Action”
- `log_ids` One2many → `res.users.log` “User log entries”
- `device_ids` One2many → `res.device` “User devices”
- `session_ids` One2many → `res.session` “User sessions”
- `login_date` Datetime “Latest Login” (related=log_ids.create_date)
- `share` Boolean “Share User” (store, compute=_compute_share)
- `companies_count` Integer “Number of Companies” (compute=_compute_companies_count)
- `tz_offset` Char “Timezone offset” (compute=_compute_tz_offset)
- `res_users_settings_ids` One2many → `res.users.settings`
- `res_users_settings_id` Many2one → `res.users.settings` “Settings” (compute=_compute_res_users_settings_id)
- `company_id` Many2one → `res.company` “Company” (required)
- `company_ids` Many2many → `res.company` “Companies”
- `name` Char (related=partner_id.name)
- `email` Char (related=partner_id.email)
- `email_domain_placeholder` Char (compute=_compute_email_domain_placeholder)
- `phone` Char (related=partner_id.phone)
- `image_1920` Binary (related=partner_id.image_1920)
- `lang` Selection (related=partner_id.lang)
- `tz` Selection (related=partner_id.tz)
- `group_ids` Many2many → `res.groups` “Groups”
- `all_group_ids` Many2many → `res.groups` “Groups and implied groups” (compute=_compute_all_group_ids)
- `accesses_count` Integer “# Access Rights” (compute=_compute_accesses_count)
- `groups_count` Integer “# Groups” (compute=_compute_accesses_count)
- `view_group_hierarchy` Json “Technical field for user group setting”
- `role` Selection “Role” (compute=_compute_role)

Public methods: `action_change_password_wizard`, `action_get`, `action_revoke_all_devices`, `action_show_accesses`, `action_show_groups`, `api_key_wizard`, `authenticate`, `change_password`, `context_get`, `copy_data`, `create`, `get_company_currency_id`, `has_group`, `has_groups`, `init`, `name_search`, `on_change_login`, `onchange_parent_id`, `preference_change_password`, `preference_save`, `write`

Extension points: `_action_revoke_all_devices`, `_action_show`, `_check_action_id`, `_check_at_least_one_administrator`, `_check_company_domain`, `_check_credentials`, `_check_disjoint_groups`, `_check_uid_passwd`, `_check_user_company`, `_get_auth_methods`, `_get_company_ids`, `_get_email_domain`, `_get_group_ids`, `_get_invalidation_fields`, `_get_login_domain`, `_get_login_order`, `_get_session_token_fields`, `_get_session_token_query_params`

## `res.users` (extends)


Public methods: `create`, `new`, `write`

## `res.users.identitycheck` (defines)

Password Check Wizard

- `request` Char (readonly)
- `auth_method` Selection
- `password` Char

Public methods: `run_check`

Extension points: `_check_identity`, `_get_default_auth_method`

## `change.password.wizard` (defines)

Change Password Wizard

- `user_ids` One2many → `change.password.user` “Users”

Public methods: `change_password_button`

## `change.password.user` (defines)

User, Change Password Wizard

- `wizard_id` Many2one → `change.password.wizard` “Wizard” (required)
- `user_id` Many2one → `res.users` “User” (required)
- `user_login` Char “User Login” (readonly)
- `new_passwd` Char “New Password”

Public methods: `change_password_button`

## `change.password.own` (defines)

User, change own password wizard

- `new_password` Char “New Password”
- `confirm_password` Char “New Password (Confirmation)”

Public methods: `change_password`

Extension points: `_check_password_confirmation`

## `res.users.apikeys` (defines)

User API Key

- `name` Char “Description” (required, readonly)
- `user_id` Many2one → `res.users` (required, readonly, index)
- `scope` Char “Scope” (required, readonly)
- `create_date` Datetime “Creation Date” (readonly)
- `expiration_date` Datetime “Expiration Date” (readonly)

Public methods: `generate`, `init`, `remove`, `revoke`

Extension points: `_check_credentials`, `_check_expiration_date`

## `res.users.apikeys.description` (defines)

API Key Description

- `name` Char “Description” (required)
- `scope` Selection “Scope” (required)
- `available_scopes_count` Integer (compute=_compute_available_scopes_count)
- `duration` Selection “Duration” (required)
- `expiration_date` Datetime “Expiration Date” (store, compute=_compute_expiration_date)

Public methods: `check_access_make_key`, `create`, `make_key`

## `res.users.apikeys.show` (defines)

Show API Key

- `id` Id
- `key` Char (readonly)
- `scope` Char (readonly)
- `base_url` Char (readonly)

## `res.users.deletion` (defines)

Users Deletion Request

- `user_id` Many2one → `res.users` “User”
- `user_id_int` Integer “User Id” (store, compute=_compute_user_id_int)
- `state` Selection “State” (required)

## `res.users.settings` (defines)

User Settings

- `user_id` Many2one → `res.users` “User” (required)

Public methods: `set_res_users_settings`

Extension points: `_get_fields_blacklist`

## `website` (defines)

Website

- `name` Char “Website Name” (required)
- `sequence` Integer
- `user_id` Many2one → `res.users` “Public User” (required)
- `company_id` Many2one → `res.company` “Company” (required)
- `domain` Char “Website Domain”
- `domain_punycode` Char “Punycode Domain” (readonly, store, compute=_compute_domain_punycode)

## `report.base.report_irmodulereference` (defines)

Module Reference Report (base)


Extension points: `_get_report_values`

## `base.language.export` (defines)

Language Export

- `name` Char “File Name” (readonly)
- `lang` Selection “Language” (required)
- `format` Selection “File Format” (required)
- `export_type` Selection “Export Type” (required)
- `modules` Many2many → `ir.module.module` “Apps To Export”
- `model_id` Many2one → `ir.model` “Model to Export”
- `model_name` Char “Model Name” (related=model_id.model)
- `domain` Char “Model Domain”
- `data` Binary “File” (readonly)
- `state` Selection

Public methods: `act_getfile`

Extension points: `_get_languages`

## `base.language.import` (defines)

Language Import

- `name` Char “Language Name” (required)
- `code` Char “ISO Code” (required)
- `data` Binary “File” (required)
- `filename` Char “File Name” (required)
- `overwrite` Boolean “Overwrite Existing Terms”

Public methods: `import_lang`

## `base.language.install` (defines)

Install Language

- `lang_ids` Many2many → `res.lang` (required)
- `overwrite` Boolean “Overwrite Existing Terms”
- `first_lang_id` Many2one → `res.lang` (compute=_compute_first_lang_id)

Public methods: `lang_install`, `reload`, `switch_lang`

## `base.module.uninstall` (defines)

Module Uninstall

- `module_ids` Many2many → `ir.module.module` “Module(s)” (required, readonly)
- `impacted_application_count` Integer (compute=_compute_impacted_module_ids)
- `impacted_application_ids` Many2many → `ir.module.module` “Impacted applications” (compute=_compute_impacted_module_ids)
- `impacted_module_count` Integer (compute=_compute_impacted_module_ids)
- `impacted_module_ids` Many2many → `ir.module.module` “Impacted modules” (compute=_compute_impacted_module_ids)
- `model_count` Integer (compute=_compute_model_ids)
- `model_ids` Many2many → `ir.model` “Models to be deleted” (compute=_compute_model_ids)

Public methods: `action_uninstall`

Extension points: `_get_models`, `_get_modules`

## `base.module.update` (defines)

Update Module

- `updated` Integer “Number of modules updated” (readonly)
- `added` Integer “Number of modules added” (readonly)
- `state` Selection (readonly)

Public methods: `action_module_open`, `update_module`

## `base.module.upgrade` (defines)

Upgrade Module

- `module_info` Text “Apps to Update” (readonly)

Public methods: `config`, `get_module_list`, `get_view`, `upgrade_module`, `upgrade_module_cancel`

## `base.partner.merge.line` (defines)

Merge Partner Line

- `wizard_id` Many2one → `base.partner.merge.automatic.wizard`
- `min_id` Integer “MinID”
- `aggr_ids` Char “Ids” (required)

## `base.partner.merge.automatic.wizard` (defines)

Merge Partner Wizard

- `group_by_email` Boolean “Email”
- `group_by_name` Boolean “Name”
- `group_by_is_company` Boolean “Is Company”
- `group_by_vat` Boolean “VAT”
- `group_by_parent_id` Boolean “Parent Company”
- `state` Selection “State” (required, readonly)
- `number_group` Integer “Group of Contacts” (readonly)
- `current_line_id` Many2one → `base.partner.merge.line` “Current Line”
- `line_ids` One2many → `base.partner.merge.line` “Lines”
- `partner_ids` Many2many → `res.partner` “Contacts”
- `dst_partner_id` Many2one → `res.partner` “Destination Contact”
- `exclude_contact` Boolean “A user associated to the contact”
- `exclude_journal_item` Boolean “Journal Items associated to the contact”
- `maximum_group` Integer “Maximum of Group of Contacts”

Public methods: `action_merge`, `action_skip`, `action_start_automatic_process`, `action_start_manual_process`, `action_update_all_process`, `default_get`, `parent_migration_process_cb`

Extension points: `_action_next_screen`, `_get_fk_on`, `_get_ordered_partner`, `_get_summable_fields`

## `wizard.ir.model.menu.create` (defines)

Create Menu Wizard

- `menu_id` Many2one → `ir.ui.menu` “Parent Menu” (required)
- `name` Char “Menu Name” (required)

Public methods: `menu_create`
