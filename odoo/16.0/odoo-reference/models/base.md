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

## `decimal.precision` (defines)

Decimal Precision

- `name` Char “Usage” (required)
- `digits` Integer “Digits” (required)

Public methods: `create`, `precision_get`, `unlink`, `write`

## `image.mixin` (defines)

Image Mixin

- `image_1920` Image “Image”
- `image_1024` Image “Image 1024” (store, related=image_1920)
- `image_512` Image “Image 512” (store, related=image_1920)
- `image_256` Image “Image 256” (store, related=image_1920)
- `image_128` Image “Image 128” (store, related=image_1920)

## `ir.actions.actions` (defines)

Actions

- `name` Char “Action Name” (required)
- `type` Char “Action Type” (required)
- `xml_id` Char “External ID” (compute=_compute_xml_id)
- `help` Html “Action Description”
- `binding_model_id` Many2one → `ir.model`
- `binding_type` Selection (required)
- `binding_view_types` Char

Public methods: `create`, `get_bindings`, `unlink`, `write`

Extension points: `_get_action_dict`, `_get_bindings`, `_get_eval_context`, `_get_readable_fields`

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
- `usage` Char “Action Usage”
- `view_ids` One2many → `ir.actions.act_window.view` “No of Views”
- `views` Binary (compute=_compute_views)
- `limit` Integer
- `groups_id` Many2many → `res.groups` “Groups”
- `search_view_id` Many2one → `ir.ui.view` “Search View Ref.”
- `filter` Boolean
- `search_view` Text (compute=_compute_search_view)

Public methods: `create`, `exists`, `read`, `unlink`

Extension points: `_check_model`, `_check_view_mode`, `_get_readable_fields`

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

## `ir.actions.server` (defines)

Server Actions

Inherits: `ir.actions.actions`

- `type` Char
- `usage` Selection “Usage” (required)
- `state` Selection “Action To Do” (required)
- `sequence` Integer
- `model_id` Many2one → `ir.model` “Model” (required, index)
- `model_name` Char “Model Name” (readonly, store, related=model_id.model)
- `code` Text “Python Code”
- `child_ids` Many2many → `ir.actions.server` “Child Actions”
- `crud_model_id` Many2one → `ir.model` “Target Model” (store, compute=_compute_crud_model_id)
- `crud_model_name` Char “Target Model Name” (readonly, related=crud_model_id.model)
- `link_field_id` Many2one → `ir.model.fields` “Link Field” (store, compute=_compute_link_field_id)
- `fields_lines` One2many → `ir.server.object.lines` “Value Mapping”
- `groups_id` Many2many → `res.groups` “Groups”

Public methods: `create_action`, `run`, `unlink_action`

Extension points: `_check_python_code`, `_check_recursion`, `_get_eval_context`, `_get_readable_fields`, `_get_runner`

## `ir.server.object.lines` (defines)

Server Action value mapping

- `server_id` Many2one → `ir.actions.server` “Related Server Action”
- `col1` Many2one → `ir.model.fields` “Field” (required)
- `value` Text (required)
- `evaluation_type` Selection (required)
- `resource_ref` Reference “Record” (compute=_compute_resource_ref)

Public methods: `eval_value`

## `ir.actions.todo` (defines)

Configuration Wizards

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
- `params` Binary “Supplementary arguments” (compute=_compute_params)
- `params_store` Binary “Params storage” (readonly)

Extension points: `_get_readable_fields`

## `ir.actions.report` (defines)

Report Action

Inherits: `ir.actions.actions`

- `type` Char
- `binding_type` Selection
- `model` Char “Model Name” (required)
- `model_id` Many2one → `ir.model` “Model” (compute=_compute_model_id)
- `report_type` Selection (required)
- `report_name` Char “Template Name” (required)
- `report_file` Char “Report File” (store)
- `groups_id` Many2many → `res.groups` “Groups”
- `multi` Boolean “On Multiple Doc.”
- `paperformat_id` Many2one → `report.paperformat`
- `print_report_name` Char “Printed Report Name”
- `attachment_use` Boolean “Reload from Attachment”
- `attachment` Char “Save as Attachment Prefix”

Public methods: `associated_view`, `barcode`, `create_action`, `datamatrix_available`, `get_available_barcode_masks`, `get_paperformat`, `get_wkhtmltopdf_state`, `report_action`, `retrieve_attachment`, `unlink_action`

Extension points: `_action_configure_external_report_layout`, `_get_layout`, `_get_readable_fields`, `_get_rendering_context`, `_get_rendering_context_model`, `_get_report`, `_get_report_from_name`, `_get_report_url`, `_prepare_html`, `_prepare_pdf_report_attachment_vals_list`

## `ir.asset` (defines)

Asset

- `name` Char “Name” (required)
- `bundle` Char “Bundle name” (required)
- `directive` Selection “Directive”
- `path` Char “Path (or glob pattern)” (required)
- `target` Char “Target”
- `active` Boolean “active”
- `sequence` Integer “Sequence” (required)

Public methods: `create`, `unlink`, `write`

Extension points: `_get_active_addons_list`, `_get_asset_paths`, `_get_installed_addons_list`, `_get_paths`, `_get_related_assets`, `_get_related_bundle`

## `ir.attachment` (defines)

Attachment

- `name` Char “Name” (required)
- `description` Text “Description”
- `res_name` Char “Resource Name” (compute=_compute_res_name)
- `res_model` Char “Resource Model” (readonly)
- `res_field` Char “Resource Field” (readonly)
- `res_id` Many2oneReference “Resource ID” (readonly)
- `company_id` Many2one → `res.company` “Company”
- `type` Selection “Type” (required)
- `url` Char “Url”
- `public` Boolean “Is public document”
- `access_token` Char “Access Token”
- `raw` Binary “File Content (raw)” (compute=_compute_raw)
- `datas` Binary “File Content (base64)” (compute=_compute_datas)
- `db_datas` Binary “Database Data”
- `store_fname` Char “Stored Filename” (index)
- `file_size` Integer “File Size” (readonly)
- `checksum` Char “Checksum/SHA1” (readonly, index)
- `mimetype` Char “Mime Type” (readonly)
- `index_content` Text “Indexed Content” (readonly)

Public methods: `action_get`, `check`, `copy`, `create`, `force_storage`, `generate_access_token`, `get_serving_groups`, `read_group`, `regenerate_assets_bundles`, `unlink`, `validate_access`, `write`

Extension points: `_check_contents`, `_check_serving_attachments`, `_get_datas_related_values`, `_get_path`, `_get_serve_attachment`, `_get_storage_domain`, `_post_add_create`

## `ir.autovacuum` (defines)

Automatic Vacuum


Public methods: `power_on`

## `ir.binary` (defines)

File streaming helper model for controllers


Extension points: `_get_image_stream_from`, `_get_placeholder_stream`, `_get_stream_from`

## `ir.config_parameter` (defines)

System Parameter

- `key` Char (required)
- `value` Text (required)

Public methods: `create`, `get_param`, `init`, `set_param`, `unlink`, `unlink_default_parameters`, `write`

Extension points: `_get_param`

## `ir.cron` (defines)

Scheduled Actions

- `ir_actions_server_id` Many2one → `ir.actions.server` (required)
- `cron_name` Char “Name” (store, related=ir_actions_server_id.name)
- `user_id` Many2one → `res.users` “Scheduler User” (required)
- `active` Boolean
- `interval_number` Integer
- `interval_type` Selection “Interval Unit”
- `numbercall` Integer “Number of Calls”
- `doall` Boolean “Repeat Missed”
- `nextcall` Datetime “Next Execution Date” (required)
- `lastcall` Datetime “Last Execution Date”
- `priority` Integer

Public methods: `create`, `default_get`, `method_direct_trigger`, `toggle`, `try_write`, `unlink`, `write`

Extension points: `_check_modules_state`, `_check_version`, `_get_all_ready_jobs`

## `ir.cron.trigger` (defines)

Triggered actions

- `cron_id` Many2one → `ir.cron` (index)
- `call_at` Datetime

## `ir.default` (defines)

Default Values

- `field_id` Many2one → `ir.model.fields` “Field” (required, index)
- `user_id` Many2one → `res.users` “User” (index)
- `company_id` Many2one → `res.company` “Company” (index)
- `condition` Char “Condition”
- `json_value` Char “Default Value (JSON format)” (required)

Public methods: `create`, `discard_records`, `discard_values`, `get`, `get_model_defaults`, `set`, `unlink`, `write`

Extension points: `_check_accessible_field_id`, `_check_json_format`

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

## `ir.exports` (defines)

Exports

- `name` Char “Export Name”
- `resource` Char (index)
- `export_fields` One2many → `ir.exports.line` “Export ID”

## `ir.exports.line` (defines)

Exports Line

- `name` Char “Field Name”
- `export_id` Many2one → `ir.exports` “Export” (index)

## `ir.fields.converter` (defines)

Fields Converter


Public methods: `db_id_for`, `for_model`, `to_field`

Extension points: `_get_boolean_translations`, `_get_import_field_path`, `_get_selection_translations`

## `base` (extends)


Public methods: `create`

## `ir.filters` (defines)

Filters

- `name` Char “Filter Name” (required)
- `user_id` Many2one → `res.users` “User”
- `domain` Text (required)
- `context` Text (required)
- `sort` Text (required)
- `model_id` Selection “Model” (required)
- `is_default` Boolean “Default Filter”
- `action_id` Many2one → `ir.actions.actions` “Action”
- `active` Boolean

Public methods: `copy`, `create`, `create_or_replace`, `get_filters`, `write`

Extension points: `_check_global_default`, `_get_action_domain`, `_get_eval_domain`

## `ir.http` (defines)

HTTP Routing


Public methods: `get_translations_for_webclient`, `get_web_translations_hash`, `routing_map`

Extension points: `_get_converters`, `_get_public_users`, `_post_dispatch`

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
- `smtp_host` Char “SMTP Server” (required)
- `smtp_port` Integer “SMTP Port” (required)
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

Public methods: `build_email`, `connect`, `send_email`, `test_smtp_connection`, `write`

Extension points: `_check_smtp_ssl_files`, `_get_default_bounce_address`, `_get_default_from_address`, `_get_test_email_addresses`, `_prepare_email_message`

## `base` (defines)

Base


## `_unknown` (defines)

Unknown


## `ir.model` (defines)

Models

- `name` Char “Model Description” (required)
- `model` Char (required)
- `order` Char “Order” (required)
- `info` Text “Information”
- `field_id` One2many → `ir.model.fields` “Fields” (required)
- `inherited_model_ids` Many2many → `ir.model` “Inherited models” (compute=_inherited_models)
- `state` Selection “Type” (readonly)
- `access_ids` One2many → `ir.model.access` “Access”
- `rule_ids` One2many → `ir.rule` “Record Rules”
- `transient` Boolean “Transient Model”
- `modules` Char “In Apps” (compute=_in_modules)
- `view_ids` One2many → `ir.ui.view` “Views” (compute=_view_ids)
- `count` Integer “Count (Incl. Archived)” (compute=_compute_count)

Public methods: `create`, `name_create`, `unlink`, `write`

Extension points: `_check_model_name`, `_check_order`, `_get_id`

## `ir.model.fields` (defines)

Fields

- `name` Char “Field Name” (required, index)
- `complete_name` Char (index)
- `model` Char “Model Name” (required, index)
- `relation` Char “Related Model”
- `relation_field` Char
- `relation_field_id` Many2one → `ir.model.fields` “Relation field” (store, compute=_compute_relation_field_id)
- `model_id` Many2one → `ir.model` “Model” (required, index)
- `field_description` Char “Field Label” (required)
- `help` Text “Field Help”
- `ttype` Selection “Field Type” (required)
- `selection` Char “Selection Options (Deprecated)” (compute=_compute_selection)
- `selection_ids` One2many → `ir.model.fields.selection` “Selection Options”
- `copied` Boolean “Copied” (store, compute=_compute_copied)
- `related` Char “Related Field”
- `related_field_id` Many2one → `ir.model.fields` “Related field” (store, compute=_compute_related_field_id)
- `required` Boolean
- `readonly` Boolean
- `index` Boolean “Indexed”
- `translate` Boolean “Translatable”
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

Public methods: `create`, `get_field_help`, `get_field_selection`, `get_field_string`, `name_get`, `unlink`, `write`

Extension points: `_check_depends`, `_check_domain`, `_check_name`, `_check_related`, `_check_relation`, `_check_relation_table`, `_get_ids`, `_get_manual_field_data`, `_prepare_update`

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

- `name` Char “Constraint” (required, index)
- `definition` Char
- `message` Char
- `model` Many2one → `ir.model` (required, index)
- `module` Many2one → `ir.module.module` (required, index)
- `type` Char “Constraint Type” (required, index)
- `write_date` Datetime
- `create_date` Datetime

Public methods: `copy`, `unlink`

## `ir.model.relation` (defines)

Relation Model

- `name` Char “Relation Name” (required, index)
- `model` Many2one → `ir.model` (required, index)
- `module` Many2one → `ir.module.module` (required, index)
- `write_date` Datetime
- `create_date` Datetime

## `ir.model.access` (defines)

Model Access

- `name` Char (required, index)
- `active` Boolean
- `model_id` Many2one → `ir.model` “Model” (required, index)
- `group_id` Many2one → `res.groups` “Group” (index)
- `perm_read` Boolean “Read Access”
- `perm_write` Boolean “Write Access”
- `perm_create` Boolean “Create Access”
- `perm_unlink` Boolean “Delete Access”

Public methods: `call_cache_clearing_methods`, `check`, `check_group`, `check_groups`, `create`, `group_names_with_access`, `register_cache_clearing_method`, `unlink`, `unregister_cache_clearing_method`, `write`

Extension points: `_get_allowed_models`

## `ir.model.data` (defines)

Model Data

- `name` Char “External Identifier” (required)
- `complete_name` Char “Complete ID” (compute=_compute_complete_name)
- `model` Char “Model Name” (required)
- `module` Char (required)
- `res_id` Many2oneReference “Record ID”
- `noupdate` Boolean “Non Updatable”
- `reference` Char “Reference” (readonly, compute=_compute_reference)

Public methods: `check_object_reference`, `copy`, `name_get`, `toggle_noupdate`, `unlink`

## `wizard.ir.model.menu.create` (defines)

Create Menu Wizard

- `menu_id` Many2one → `ir.ui.menu` “Parent Menu” (required)
- `name` Char “Menu Name” (required)

Public methods: `menu_create`

## `ir.module.category` (defines)

Application

- `name` Char “Name” (required, index)
- `parent_id` Many2one → `ir.module.category` “Parent Application” (index)
- `child_ids` One2many → `ir.module.category` “Child Applications”
- `module_nr` Integer “Number of Apps” (compute=_compute_module_nr)
- `module_ids` One2many → `ir.module.module` “Modules”
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
- `exclusion_ids` One2many → `ir.module.module.exclusion` “Exclusions” (readonly)
- `auto_install` Boolean “Automatic Installation”
- `state` Selection “Status” (readonly, index)
- `demo` Boolean “Demo Data” (readonly)
- `license` Selection “License” (readonly)
- `menus_by_module` Text “Menus” (store, compute=_get_views)
- `reports_by_module` Text “Reports” (store, compute=_get_views)
- `views_by_module` Text “Views” (store, compute=_get_views)
- `application` Boolean “Application” (readonly)
- `icon` Char “Icon URL”
- `icon_image` Binary “Icon” (compute=_get_icon_image)
- `to_buy` Boolean “Odoo Enterprise Module”
- `has_iap` Boolean (compute=_compute_has_iap)

Public methods: `button_immediate_install`, `button_immediate_uninstall`, `button_immediate_upgrade`, `button_install`, `button_install_cancel`, `button_uninstall`, `button_uninstall_cancel`, `button_uninstall_wizard`, `button_upgrade`, `button_upgrade_cancel`, `check_external_dependencies`, `create`, `download`, `downstream_dependencies`, `get_apps_server`, `get_module_info`, `get_values_from_terp`, `get_views`, `install_from_urls`, `module_uninstall`, `next`, `search_panel_select_range`, `unlink`, `update_list`, `upstream_dependencies`

Extension points: `_get_desc`, `_get_icon_image`, `_get_id`, `_get_latest_version`, `_get_modules_to_load_domain`, `_get_views`

## `ir.module.module.dependency` (defines)

Module dependency

- `name` Char (index)
- `module_id` Many2one → `ir.module.module`
- `depend_id` Many2one → `ir.module.module` (compute=_compute_depend)
- `state` Selection “Status” (compute=_compute_state)
- `auto_install_required` Boolean

## `ir.module.module.exclusion` (defines)

Module exclusion

- `name` Char (index)
- `module_id` Many2one → `ir.module.module`
- `exclusion_id` Many2one → `ir.module.module` (compute=_compute_exclusion)
- `state` Selection “Status” (compute=_compute_state)

## `ir.profile` (defines)

Profiling results

- `create_date` Datetime “Creation Date”
- `session` Char “Session” (index)
- `name` Char “Description”
- `duration` Float “Duration”
- `init_stack_trace` Text “Initial stack trace”
- `sql` Text “Sql”
- `sql_count` Integer “Queries Count”
- `traces_async` Text “Traces Async”
- `traces_sync` Text “Traces Sync”
- `qweb` Text “Qweb”
- `entry_count` Integer “Entry count”
- `speedscope` Binary “Speedscope” (compute=_compute_speedscope)
- `speedscope_url` Text “Open” (compute=_compute_speedscope_url)

Public methods: `set_profiling`

## `base.enable.profiling.wizard` (defines)

Enable profiling for some time

- `duration` Selection “Enable profiling for”
- `expiration` Datetime “Enable profiling until” (store, compute=_compute_expiration)

Public methods: `submit`

## `ir.property` (defines)

Company Property

- `name` Char (index)
- `res_id` Char “Resource” (index)
- `company_id` Many2one → `res.company` “Company” (index)
- `fields_id` Many2one → `ir.model.fields` “Field” (required)
- `value_float` Float
- `value_integer` Integer
- `value_text` Text
- `value_binary` Binary
- `value_reference` Char
- `value_datetime` Datetime
- `type` Selection (required, index)

Public methods: `create`, `get_by_record`, `init`, `search_multi`, `unlink`, `write`

Extension points: `_get_default_property`, `_get_domain`, `_get_multi`, `_get_property`

## `ir.qweb` (defines)

Qweb


Extension points: `_get_asset_bundle`, `_get_asset_content`, `_get_asset_link_urls`, `_get_asset_nodes`, `_get_cache_key`, `_get_cached_values`, `_get_field`, `_get_template`, `_get_template_cache_keys`, `_get_view_id`, `_get_widget`, `_post_processing_att`, `_prepare_environment`

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


Public methods: `value_to_html`

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

## `ir.qweb.field.html` (defines)

Qweb Field HTML

Inherits: `ir.qweb.field`


Public methods: `value_to_html`

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

## `ir.rule` (defines)

Record Rule

- `name` Char (index)
- `active` Boolean
- `model_id` Many2one → `ir.model` “Model” (required, index)
- `groups` Many2many → `res.groups`
- `domain_force` Text “Domain”
- `perm_read` Boolean “Apply for Read”
- `perm_write` Boolean “Apply for Write”
- `perm_create` Boolean “Apply for Create”
- `perm_unlink` Boolean “Apply for Delete”

Public methods: `clear_cache`, `create`, `unlink`, `write`

Extension points: `_check_domain`, `_check_model_name`, `_get_failing`, `_get_rules`

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

Public methods: `create`, `get`, `get_id`, `get_next_char`, `next_by_code`, `next_by_id`, `unlink`, `write`

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
- `groups_id` Many2many → `res.groups` “Groups”
- `complete_name` Char “Full Path” (compute=_compute_complete_name)
- `web_icon` Char “Web Icon File”
- `action` Reference
- `web_icon_data` Binary “Web Icon Image”

Public methods: `copy`, `create`, `get_user_roots`, `load_menus`, `load_menus_root`, `name_get`, `read_image`, `unlink`, `write`

Extension points: `_check_parent_id`, `_get_full_name`, `_get_menuitems_xmlids`

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
- `field_parent` Char “Child Field”
- `model_data_id` Many2one → `ir.model.data` “Model Data” (compute=_compute_model_data_id)
- `xml_id` Char “External ID” (compute=_compute_xml_id)
- `groups_id` Many2many → `res.groups` “Groups”
- `mode` Selection “View inheritance mode” (required)
- `active` Boolean

Public methods: `apply_inheritance_specs`, `clear_cache`, `copy`, `create`, `default_view`, `distribute_branding`, `get_combined_arch`, `inherit_branding`, `is_node_branded`, `locate_node`, `postprocess_and_fields`, `read_combined`, `render_public_asset`, `reset_arch`, `unlink`, `write`

Extension points: `_check_000_inheritance`, `_check_dropdown_menu`, `_check_field_paths`, `_check_groups`, `_check_progress_bar`, `_check_view_access`, `_check_xml`, `_create_all_specific_views`, `_get_combined_arch`, `_get_domain_identifiers`, `_get_filter_xmlid_query`, `_get_inheriting_views`, `_get_inheriting_views_domain`, `_get_specific_views`, `_get_view_id`, `_get_view_refs`, `_get_x2many_missing_view_archs`

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


Public methods: `fields_view_get`, `get_empty_list_help`, `get_formview_action`, `get_formview_id`, `get_view`, `get_views`, `load_views`, `view_header_get`

Extension points: `_get_access_action`, `_get_default_calendar_view`, `_get_default_form_view`, `_get_default_graph_view`, `_get_default_kanban_view`, `_get_default_pivot_view`, `_get_default_search_view`, `_get_default_tree_view`, `_get_view`, `_get_view_cache`, `_get_view_cache_key`, `_get_view_field_attributes`, `_get_view_fields`

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
- `default` Boolean “Default paper format ?”
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

Extension points: `_check_format_or_page`

## `res.bank` (defines)

Bank

- `name` Char (required)
- `street` Char
- `street2` Char
- `zip` Char
- `city` Char
- `state` Many2one → `res.country.state`
- `country` Many2one → `res.country`
- `email` Char
- `phone` Char
- `active` Boolean
- `bic` Char “Bank Identifier Code” (index)

Public methods: `name_get`

## `res.partner.bank` (defines)

Bank Accounts

- `active` Boolean
- `acc_type` Selection “Type” (compute=_compute_acc_type)
- `acc_number` Char “Account Number” (required)
- `sanitized_acc_number` Char “Sanitized Account Number” (readonly, store, compute=_compute_sanitized_acc_number)
- `acc_holder_name` Char “Account Holder Name”
- `partner_id` Many2one → `res.partner` (required, index)
- `allow_out_payment` Boolean “Send Money”
- `bank_id` Many2one → `res.bank` “Bank”
- `bank_name` Char (related=bank_id.name)
- `bank_bic` Char (related=bank_id.bic)
- `sequence` Integer
- `currency_id` Many2one → `res.currency` “Currency”
- `company_id` Many2one → `res.company` (readonly, store, related=partner_id.company_id)

Public methods: `get_supported_account_types`, `name_get`, `retrieve_acc_type`

Extension points: `_get_supported_account_types`

## `res.company` (defines)

Companies

- `name` Char “Company Name” (required, store, related=partner_id.name)
- `active` Boolean
- `sequence` Integer
- `parent_id` Many2one → `res.company` “Parent Company” (index)
- `child_ids` One2many → `res.company` “Child Companies”
- `partner_id` Many2one → `res.partner` “Partner” (required)
- `report_header` Html “Company Tagline”
- `report_footer` Html “Report Footer”
- `company_details` Html “Company Details”
- `is_company_details_empty` Boolean (compute=_compute_empty_company_details)
- `logo` Binary “Company Logo” (related=partner_id.image_1920)
- `logo_web` Binary (store, compute=_compute_logo_web)
- `currency_id` Many2one → `res.currency` “Currency” (required)
- `user_ids` Many2many → `res.users` “Accepted Users”
- `street` Char (compute=_compute_address)
- `street2` Char (compute=_compute_address)
- `zip` Char (compute=_compute_address)
- `city` Char (compute=_compute_address)
- `state_id` Many2one → `res.country.state` “Fed. State” (compute=_compute_address)
- `bank_ids` One2many (related=partner_id.bank_ids)
- `country_id` Many2one → `res.country` “Country” (compute=_compute_address)
- `email` Char (store, related=partner_id.email)
- `phone` Char (store, related=partner_id.phone)
- `mobile` Char (store, related=partner_id.mobile)
- `website` Char (related=partner_id.website)
- `vat` Char “Tax ID” (related=partner_id.vat)
- `company_registry` Char “Company ID” (related=partner_id.company_registry)
- `paperformat_id` Many2one → `report.paperformat`
- `external_report_layout_id` Many2one → `ir.ui.view`
- `base_onboarding_company_state` Selection “State of the onboarding company step”
- `favicon` Binary “Company Favicon”
- `font` Selection
- `primary_color` Char
- `secondary_color` Char
- `layout_background` Selection (required)
- `layout_background_image` Binary “Background Image”

Public methods: `action_open_base_onboarding_company`, `action_save_onboarding_company_step`, `cache_restart`, `copy`, `create`, `init`, `open_company_edit_report`, `set_onboarding_step_done`, `write`, `write_company_and_print_report`

Extension points: `_check_active`, `_check_parent_id`, `_get_and_update_onboarding_state`, `_get_company_address_field_names`, `_get_company_address_update`, `_get_default_favicon`, `_get_logo`, `_get_main_company`

## `res.config` (defines)

Config


Public methods: `action_cancel`, `action_next`, `action_skip`, `cancel`, `execute`, `next`, `start`

## `res.config.installer` (defines)

Config Installer

Inherits: `res.config`


Public methods: `already_installed`, `default_get`, `execute`, `fields_get`, `modules_to_install`

## `res.config.settings` (defines)

Config Settings


Public methods: `action_open_template_user`, `cancel`, `copy`, `create`, `default_get`, `execute`, `get_config_warning`, `get_option_name`, `get_option_path`, `get_values`, `name_get`, `onchange_module`, `set_values`

Extension points: `_get_classified_fields`

## `res.country` (defines)

Country

- `name` Char “Country Name” (required)
- `code` Char “Country Code”
- `address_format` Text “Layout in Reports”
- `address_view_id` Many2one → `ir.ui.view` “Input View”
- `currency_id` Many2one → `res.currency` “Currency”
- `image_url` Char “Flag” (compute=_compute_image_url)
- `phone_code` Integer “Country Calling Code”
- `country_group_ids` Many2many → `res.country.group` “Country Groups”
- `state_ids` One2many → `res.country.state` “States”
- `name_position` Selection “Customer Name Position”
- `vat_label` Char “Vat Label”
- `state_required` Boolean
- `zip_required` Boolean

Public methods: `create`, `get_address_fields`, `write`

Extension points: `_check_address_format`, `_check_country_code`

## `res.country.group` (defines)

Country Group

- `name` Char (required)
- `country_ids` Many2many → `res.country` “Countries”

## `res.country.state` (defines)

Country state

- `country_id` Many2one → `res.country` “Country” (required)
- `name` Char “State Name” (required)
- `code` Char “State Code” (required)

Public methods: `name_get`

Extension points: `_get_name_search_domain`

## `res.currency` (defines)

Currency

- `name` Char “Currency” (required)
- `full_name` Char “Name”
- `symbol` Char (required)
- `rate` Float “Current Rate” (compute=_compute_current_rate)
- `inverse_rate` Float (readonly, compute=_compute_current_rate)
- `rate_string` Char (compute=_compute_current_rate)
- `rate_ids` One2many → `res.currency.rate` “Rates”
- `rounding` Float “Rounding Factor”
- `decimal_places` Integer (store, compute=_compute_decimal_places)
- `active` Boolean
- `position` Selection “Symbol Position”
- `date` Date (compute=_compute_date)
- `currency_unit_label` Char “Currency Unit”
- `currency_subunit_label` Char “Currency Subunit”
- `is_current_company_currency` Boolean (compute=_compute_is_current_company_currency)

Public methods: `amount_to_text`, `compare_amounts`, `compute`, `create`, `format`, `is_zero`, `name_get`, `round`, `unlink`, `write`

Extension points: `_check_company_currency_stays_active`, `_get_conversion_rate`, `_get_rates`, `_get_view`, `_get_view_cache_key`

## `res.currency.rate` (defines)

Currency Rate

- `name` Date “Date” (required, index)
- `rate` Float “Technical Rate”
- `company_rate` Float (compute=_compute_company_rate)
- `inverse_company_rate` Float (compute=_compute_inverse_company_rate)
- `currency_id` Many2one → `res.currency` “Currency” (required, readonly)
- `company_id` Many2one → `res.company` “Company”

Public methods: `create`, `write`

Extension points: `_get_last_rates_for_companies`, `_get_latest_rate`, `_get_view`, `_get_view_cache_key`

## `res.lang` (defines)

Languages

- `name` Char (required)
- `code` Char “Locale Code” (required)
- `iso_code` Char “ISO code”
- `url_code` Char “URL Code” (required)
- `active` Boolean
- `direction` Selection (required)
- `date_format` Char “Date Format” (required)
- `time_format` Char “Time Format” (required)
- `week_start` Selection “First Day of Week” (required)
- `grouping` Char “Separator Format” (required)
- `decimal_point` Char “Decimal Separator” (required)
- `thousands_sep` Char “Thousands Separator”
- `flag_image` Image “Image”
- `flag_image_url` Char

Public methods: `action_activate_langs`, `copy_data`, `create`, `format`, `get_available`, `get_installed`, `get_sorted`, `install_lang`, `load_lang`, `toggle_active`, `unlink`, `write`

Extension points: `_check_active`, `_check_format`, `_check_grouping`, `_create_lang`, `_get_cached`, `_get_cached_values`

## `format.address.mixin` (defines)

Address Format


Extension points: `_get_view`, `_get_view_cache_key`

## `res.partner.category` (defines)

Partner Tags

- `name` Char “Tag Name” (required)
- `color` Integer “Color”
- `parent_id` Many2one → `res.partner.category` “Parent Category” (index)
- `child_ids` One2many → `res.partner.category` “Child Tags”
- `active` Boolean
- `parent_path` Char (index)
- `partner_ids` Many2many → `res.partner` “Partners”

Public methods: `name_get`

Extension points: `_check_parent_id`, `_get_default_color`

## `res.partner.title` (defines)

Partner Title

- `name` Char “Title” (required)
- `shortcut` Char “Abbreviation”

## `res.partner` (defines)

Contact

Inherits: `format.address.mixin`, `avatar.mixin`

- `name` Char (index)
- `display_name` Char (store, index, compute=_compute_display_name)
- `translated_display_name` Char (compute=_compute_translated_display_name)
- `date` Date (index)
- `title` Many2one → `res.partner.title`
- `parent_id` Many2one → `res.partner` “Related Company” (index)
- `parent_name` Char “Parent name” (readonly, related=parent_id.name)
- `child_ids` One2many → `res.partner` “Contact”
- `ref` Char “Reference” (index)
- `lang` Selection “Language”
- `active_lang_count` Integer (compute=_compute_active_lang_count)
- `tz` Selection “Timezone”
- `tz_offset` Char “Timezone offset” (compute=_compute_tz_offset)
- `user_id` Many2one → `res.users` “Salesperson” (store, compute=_compute_user_id)
- `vat` Char “Tax ID” (index)
- `same_vat_partner_id` Many2one → `res.partner` “Partner with same Tax ID” (compute=_compute_same_vat_partner_id)
- `same_company_registry_partner_id` Many2one → `res.partner` “Partner with same Company Registry” (compute=_compute_same_vat_partner_id)
- `company_registry` Char “Company ID” (store, compute=_compute_company_registry)
- `bank_ids` One2many → `res.partner.bank` “Banks”
- `website` Char “Website Link”
- `comment` Html “Notes”
- `category_id` Many2many → `res.partner.category` “Tags”
- `active` Boolean
- `employee` Boolean
- `function` Char “Job Position”
- `type` Selection “Address Type”
- `street` Char
- `street2` Char
- `zip` Char
- `city` Char
- `state_id` Many2one → `res.country.state` “State”
- `country_id` Many2one → `res.country` “Country”
- `country_code` Char “Country Code” (related=country_id.code)
- `partner_latitude` Float “Geo Latitude”
- `partner_longitude` Float “Geo Longitude”
- `email` Char
- `email_formatted` Char “Formatted Email” (compute=_compute_email_formatted)
- `phone` Char
- `mobile` Char
- `is_company` Boolean “Is a Company”
- `is_public` Boolean (compute=_compute_is_public)
- `industry_id` Many2one → `res.partner.industry`
- `company_type` Selection “Company Type” (compute=_compute_company_type)
- `company_id` Many2one → `res.company` (index)
- `color` Integer “Color Index”
- `user_ids` One2many → `res.users` “Users”
- `partner_share` Boolean “Share Partner” (store, compute=_compute_partner_share)
- `contact_address` Char “Complete Address” (compute=_compute_contact_address)
- `commercial_partner_id` Many2one → `res.partner` “Commercial Entity” (store, index, compute=_compute_commercial_partner)
- `commercial_company_name` Char “Company Name Entity” (store, compute=_compute_commercial_company_name)
- `company_name` Char “Company Name”
- `barcode` Char (company_dependent)
- `self` Many2one (compute=_compute_get_ids)

Public methods: `address_get`, `copy`, `create`, `create_company`, `default_get`, `find_or_create`, `get_import_templates`, `main_partner`, `name_create`, `name_get`, `onchange_company_type`, `onchange_email`, `onchange_parent_id`, `open_commercial_entity`, `open_parent`, `update_address`, `view_header_get`, `write`

Extension points: `_check_barcode_unicity`, `_check_import_consistency`, `_check_parent_id`, `_get_address_format`, `_get_contact_name`, `_get_country_name`, `_get_default_address_format`, `_get_gravatar_image`, `_get_name`, `_get_street_split`, `_get_view`, `_prepare_display_address`

## `res.partner.industry` (defines)

Industry

- `name` Char “Name”
- `full_name` Char “Full Name”
- `active` Boolean “Active”

## `res.groups` (defines)

Access Groups

- `name` Char (required)
- `users` Many2many → `res.users`
- `model_access` One2many → `ir.model.access` “Access Controls”
- `rule_groups` Many2many → `ir.rule` “Rules”
- `menu_access` Many2many → `ir.ui.menu` “Access Menu”
- `view_access` Many2many → `ir.ui.view` “Views”
- `comment` Text
- `category_id` Many2one → `ir.module.category` “Application” (index)
- `color` Integer “Color Index”
- `full_name` Char “Group Name” (compute=_compute_full_name)
- `share` Boolean “Share Group”

Public methods: `copy`, `write`

Extension points: `_check_one_user_type`

## `res.users.log` (defines)

Users Log


## `res.users` (defines)

User

- `partner_id` Many2one → `res.partner` “Related Partner” (required, index)
- `login` Char (required)
- `password` Char (compute=_compute_password)
- `new_password` Char “Set Password” (compute=_compute_password)
- `signature` Html “Email Signature” (store, compute=_compute_signature)
- `active` Boolean
- `active_partner` Boolean “Partner is Active” (readonly, related=partner_id.active)
- `action_id` Many2one → `ir.actions.actions` “Home Action”
- `groups_id` Many2many → `res.groups` “Groups”
- `log_ids` One2many → `res.users.log` “User log entries”
- `login_date` Datetime “Latest authentication” (related=log_ids.create_date)
- `share` Boolean “Share User” (store, compute=_compute_share)
- `companies_count` Integer “Number of Companies” (compute=_compute_companies_count)
- `tz_offset` Char “Timezone offset” (compute=_compute_tz_offset)
- `company_id` Many2one → `res.company` “Company” (required)
- `company_ids` Many2many → `res.company` “Companies”
- `name` Char (related=partner_id.name)
- `email` Char (related=partner_id.email)
- `accesses_count` Integer “# Access Rights” (compute=_compute_accesses_count)
- `rules_count` Integer “# Record Rules” (compute=_compute_accesses_count)
- `groups_count` Integer “# Groups” (compute=_compute_accesses_count)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`, `action_get`, `action_show_accesses`, `action_show_groups`, `action_show_rules`, `authenticate`, `change_password`, `check`, `check_super`, `context_get`, `copy`, `create`, `get_company_currency_id`, `has_group`, `init`, `on_change_login`, `onchange_parent_id`, `preference_change_password`, `preference_save`, `read`, `read_group`, `toggle_active`, `write`

Extension points: `_action_show`, `_check_action_id`, `_check_company`, `_check_credentials`, `_check_one_user_type`, `_get_company_ids`, `_get_email_domain`, `_get_invalidation_fields`, `_get_login_domain`, `_get_login_order`, `_get_session_token_fields`

## `res.groups` (extends)

- `implied_ids` Many2many → `res.groups` “Inherits”
- `trans_implied_ids` Many2many → `res.groups` “Transitively inherits” (compute=_compute_trans_implied)

Public methods: `create`, `write`

## `res.users` (extends)


Public methods: `create`, `write`

## `res.groups` (extends)


Public methods: `create`, `get_application_groups`, `get_groups_by_application`, `unlink`, `write`

Extension points: `_get_hidden_extra_categories`

## `ir.module.category` (extends)


Public methods: `unlink`, `write`

## `res.users` (extends)

- `user_group_warning` Text “User Group Warning” (compute=_compute_user_group_warning)

Public methods: `create`, `default_get`, `fields_get`, `new`, `onchange`, `read`, `read_group`, `write`

Extension points: `_prepare_warning_for_group_inheritance`

## `res.users.identitycheck` (defines)

Password Check Wizard

- `request` Char (readonly)
- `password` Char

Public methods: `run_check`

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

## `res.users` (extends)

- `api_key_ids` One2many → `res.users.apikeys` “API Keys”

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`, `api_key_wizard`

Extension points: `_check_credentials`

## `res.users.apikeys` (defines)

Users API Keys

- `name` Char “Description” (required, readonly)
- `user_id` Many2one → `res.users` (required, readonly, index)
- `scope` Char “Scope” (readonly)
- `create_date` Datetime “Creation Date” (readonly)

Public methods: `init`, `remove`

Extension points: `_check_credentials`

## `res.users.apikeys.description` (defines)

API Key Description

- `name` Char “Description” (required)

Public methods: `check_access_make_key`, `make_key`

## `res.users.apikeys.show` (defines)

Show API Key

- `id` Id
- `key` Char (readonly)

## `res.users.deletion` (defines)

Users Deletion Request

- `user_id` Many2one → `res.users` “User”
- `user_id_int` Integer “User Id” (store, compute=_compute_user_id_int)
- `state` Selection “State” (required)

## `ir.filters` (extends)


## `res.company` (extends)


## `res.currency.rate` (extends)


## `res.partner` (extends)


## `res.partner.industry` (extends)


## `res.users` (extends)


## `report.base.report_irmodulereference` (defines)

Module Reference Report (base)


Extension points: `_get_report_values`

## `base.language.export` (defines)

Language Export

- `name` Char “File Name” (readonly)
- `lang` Selection “Language” (required)
- `format` Selection “File Format” (required)
- `modules` Many2many → `ir.module.module` “Apps To Export”
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

- `show_all` Boolean
- `module_id` Many2one → `ir.module.module` “Module” (required, readonly)
- `module_ids` Many2many → `ir.module.module` “Impacted modules” (compute=_compute_module_ids)
- `model_ids` Many2many → `ir.model` “Impacted data models” (compute=_compute_model_ids)

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
