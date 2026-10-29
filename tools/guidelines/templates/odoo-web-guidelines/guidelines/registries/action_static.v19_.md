 A component can set `static target = "new"` to open in a
  dialog, `static path = "my-dashboard"` to get a readable URL (`/odoo/my-dashboard`)
  that reopens it, `static displayName` for the breadcrumb, and
  `static extractProps(action)` to turn the action into props.