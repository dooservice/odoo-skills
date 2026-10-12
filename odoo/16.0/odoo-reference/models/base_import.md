# base_import — Base import

Depends on: web.

## `base` (extends)


Public methods: `get_import_templates`

## `base_import.mapping` (defines)

Base Import Mapping

- `res_model` Char (index)
- `column_name` Char
- `field_name` Char

## `res.users` (extends)


## `base_import.import` (defines)

Base Import

- `res_model` Char “Model”
- `file` Binary “File”
- `file_name` Char “File Name”
- `file_type` Char “File Type”

Public methods: `execute_import`, `get_fields_tree`, `parse_preview`

Extension points: `_get_distance`, `_get_mapping_suggestion`, `_get_mapping_suggestions`
