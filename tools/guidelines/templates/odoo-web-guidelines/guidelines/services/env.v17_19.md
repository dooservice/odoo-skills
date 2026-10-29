Every component has `this.env`, the same object for the whole client:
`env.services` (the started services), `env.bus` (the client-wide event bus),
`env.debug` (the debug mode string) and `env.isSmall` (mobile layout). `env._t` no
longer exists: import `_t` from `@web/core/l10n/translation`. A view adds `env.config`
(its type, the breadcrumbs) and `env.model` for its own subtree.

Never assign a key to `env`: it reaches every component and hides where the value
comes from. Share it through a service instead.