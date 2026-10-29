
- `addValidation(schema)` sets an Owl props-style schema that every entry must match
  (`{ component: { type: Function }, ... }`); it is checked only in debug mode, so run
  with `?debug=1` while developing. The categories `services`, `main_components`,
  `fields`, `views` and `view_widgets` have one.
- `useRegistry(category)` (`@web/core/registry_hook`) gives a component a reactive
  `{ entries }` that follows additions and removals, but not a replaced key.