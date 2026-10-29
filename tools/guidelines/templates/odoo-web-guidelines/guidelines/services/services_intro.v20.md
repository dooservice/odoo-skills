Shared logic lives in plugins: Owl 3 classes extending `Plugin`, registered in the
`services` resource of `@web/core/services` and started once for the application. The
`orm` (`ORM`), `action` (`ActionPlugin`), `notification` (`NotificationPlugin`),
`dialog` (`DialogPlugin`), `effect`, `title`, `ui`, `hotkey`, `localization`,
`overlay` and `popover` are plugins in this version.

`registry.category("services")` still exists as a temporary bridge: a plugin that
replaced a service also registers a service of the old name that returns the plugin,
and services not converted yet (`field`, `name`, `view`, `menu`, `command`, `http`) are
still registry entries, started after the plugins. Use `usePlugin(X)` for a plugin and
`useService("name")` only for a service with no plugin yet.
