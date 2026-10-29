- `category("fields")` maps a field widget name (the `widget` of `<field>`) or a field
  type to the component class that renders it; the class carries its own statics
  (`supportedTypes`, `extractProps`, `displayName`).
- `category("views")` maps a view type, or a `js_class` named on the arch root, to the
  view descriptor (`type`, `Controller`, `Renderer`, `Model`, `ArchParser`, `props`, ...).
  A `js_class` that is not registered is ignored without a warning.
- `category("view_widgets")` maps the `name` of a `<widget name="..."/>` to its component
  class, which may carry a static `extractProps({ attrs })`.