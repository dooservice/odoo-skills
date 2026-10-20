# What Odoo $version has

These skills are for Odoo $version and only $version. Write for it: an API from another version
fails at install or, worse, silently does nothing. Each row was checked against the
$version source.

| Topic | In $version |
| --- | --- |
| Python | $python |
| View modifiers | $view_modifiers |
| List view | $list_view |
| Chatter | $chatter |
| Record display name | $display_name |
| Grouped reads | $grouped_reads |
| Field aggregation | $field_aggregation |
| SQL constraints and indexes | $sql_constraints |
| Domains | $domains |
| Translations in Python | $translations |
| Group categories | $group_categories |
| Access rights | $access_rights |
| Route types | $route_types |
| Route auth | $route_auth |
| Default test tags | $test_tags |
| QWeb output | $qweb_output |
| Owl | $owl |
| JS module header | $js_module_header |
| JS patch | $js_patch |
| JS field registry | $js_field_registry |
| JS RPC | $js_rpc |
| JS tests | $js_tests |

## When unsure

Confirm against the installed source rather than memory:
`grep -rn "<name>" "$$(python3 -c 'import odoo, os; print(os.path.dirname(odoo.__file__))')"`
(the framework and the standard modules are there). A usage in a standard module of the same version is the
best example to follow.
