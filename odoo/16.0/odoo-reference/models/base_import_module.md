# base_import_module — Base import module

Depends on: web.

## `base.import.module` (defines)

Import Module

- `module_file` Binary “Module .ZIP file” (required)
- `state` Selection “Status” (readonly)
- `import_message` Text
- `force` Boolean “Force init”

Public methods: `action_module_open`, `import_module`

## `ir.module.module` (extends)

- `imported` Boolean “Imported Module”

Public methods: `import_zipfile`, `module_uninstall`

Extension points: `_get_latest_version`, `_get_modules_to_load_domain`

## `ir.ui.view` (extends)
