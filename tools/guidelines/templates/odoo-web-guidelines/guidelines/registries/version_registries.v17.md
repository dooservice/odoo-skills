- `category("xml_templates")` receives the Owl templates of each bundle as it loads;
  the server fills it. Never add to it: templates go in `.xml` files of the bundle.
- `category("kanban_header_config_items")` holds the entries of the gear menu of a
  kanban column: `{ label, method, isVisible, class }`, where `method` names a method
  of the kanban header and `isVisible` may be a function of `{ permissions, props }`.
