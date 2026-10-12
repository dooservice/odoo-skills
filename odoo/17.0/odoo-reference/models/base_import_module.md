# base_import_module — Base import module

Depends on: web.

## `base.import.module` (defines)

Import Module

- `module_file` Binary “Module .ZIP file” (required)
- `state` Selection “Status” (readonly)
- `import_message` Text
- `force` Boolean “Force init”
- `with_demo` Boolean “Import demo data of module”
- `modules_dependencies` Text

Public methods: `action_module_open`, `get_dependencies_to_install_names`, `import_module`

## `ir.module.module` (extends)

- `imported` Boolean “Imported Module”
- `module_type` Selection

Public methods: `button_immediate_install_app`, `module_uninstall`, `more_info`, `search_panel_select_range`, `web_read`, `web_search_read`

Extension points: `_get_icon_image`, `_get_industry_categories_from_apps`, `_get_latest_version`, `_get_missing_dependencies`, `_get_missing_dependencies_modules`, `_get_modules_from_apps`, `_get_modules_to_load_domain`

## `ir.ui.view` (extends)


## `base.module.uninstall` (extends)
