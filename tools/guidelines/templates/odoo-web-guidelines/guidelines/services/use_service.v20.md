- In a component or a plugin, a plugin comes from `usePlugin(ORM)` (the class, imported
  from its module) in a field initializer or `setup`, and a service not converted yet
  from `useService("view")`. Both run in the component's scope: a call made after the
  component is destroyed never resolves.
- Registry functions that the framework calls (systray `isDisplayed`, user menu items,
  command providers, error handlers, effects) run in a scope too: call `useService` or
  `usePlugin` inside them instead of reading `env.services`.
- `env.services` holds only the bridged services, for code not converted yet.
- Never store a plugin or a service on `window` or a module-level variable: tests start
  a fresh application, and a global keeps the old one.
