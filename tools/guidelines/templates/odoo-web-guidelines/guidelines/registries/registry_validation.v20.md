
- `addValidation(schema)` sets an Owl 3 type (`t.object({ component: t.component() })`)
  that every entry must match; it is checked only in debug mode, so run with `?debug=1`
  while developing. The categories `services`, `main_components`, `fields`, `views` and
  `view_widgets` have one.
- `useRegistry(category)` (`@web/core/registry_hook`) gives a component a reactive
  `{ entries }` that follows additions and removals, but not a replaced key.