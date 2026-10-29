Options are part of the website builder: a `Plugin` (from `@html_editor/plugin`) with a
  `static id`, whose `resources` declare `builder_options` (an option component
  extending `BaseOptionComponent`, with `static template` and `static selector`) and
  `builder_actions`; it is registered with
  `registry.category("website-plugins").add(MyOptionPlugin.id, MyOptionPlugin)`. The
  option template uses the builder controls (`BuilderSelect`, `BuilderCheckbox`,
  `BuilderColorPicker`) with `classAction` or `dataAttributeAction`.