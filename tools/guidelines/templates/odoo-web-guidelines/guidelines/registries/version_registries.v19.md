- `category("group_config_items")` holds the entries of the gear menu of a group header,
  in kanban columns and in grouped lists: `{ label, method, isVisible, class, icon }`,
  where `method` is a function or the name of a method of the menu, and `isVisible` may
  be a function of `{ permissions }`.
- `category("color_picker_tabs")` holds the tabs of the color picker:
  `{ id, name, component }`; a picker shows the tabs whose `id` is in its `enabledTabs`.
