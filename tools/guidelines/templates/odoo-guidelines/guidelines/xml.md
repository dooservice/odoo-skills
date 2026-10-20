# Views, actions and data records

- Record format: put `id` before `model`; inside a `field`, `name` first, then
  the value (tag body or `eval`), then other attributes by importance. Group
  records by model.
- Prefer the syntactic-sugar tags `<menuitem>` and `<template>` over raw
  `<record>`. Trap: an `active` attribute on `<template>` is applied at record
  creation and module *install* only; a module **update** never changes `active`.
- `<data noupdate="1">` only for non-updatable data; if the whole file is
  noupdate, set `noupdate="1"` on `<odoo>` and drop `<data>`.
- The list view is `<$list_tag>` and its view_mode is `$list_tag`.
$modifiers
$chatter
- XML id patterns: view `<model>_view_<type>` (`form`/`$list_tag`/`kanban`/`search`),
  action `<model>_action[_<detail>]`, menu `<model>_menu[_<do_stuff>]`, group
  `<module>_group_<name>`, rule `<model>_rule_<group>`. The record `name` mirrors
  the id with dots instead of underscores; actions get a real display name.
- CSS classes in views and templates: prefix with `o_<module>` (`o_` alone is
  reserved for the web client), never style through ids.
- Inheriting a view: see
  [Anchor view inheritance on names, never on position](#anchor-view-inheritance-on-names-never-on-position).

$anchor
