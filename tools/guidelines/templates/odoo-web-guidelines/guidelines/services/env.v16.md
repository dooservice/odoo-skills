Every component has `this.env`, the same object for the whole client:
`env.services` (the started services), `env.bus` (the client-wide event bus),
`env.debug` (the debug mode string), `env.isSmall` (mobile layout) and `env._t`.
Prefer `_t` from `@web/core/l10n/translation` to `env._t`. A view adds `env.config`
(its type, the breadcrumbs) and `env.model` for its own subtree.

Never assign a key to `env`: it reaches every component and hides where the value
comes from. Share it through a service instead.