The environment is almost empty in this version: plugins replace what it held.
`env.debug` and `env.isSmall` throw when read; use `usePlugin(DebugModePlugin)` (or
`odoo.debug` outside a component) and `useService("ui").isSmall`. `env.bus` and
`env.services` remain as bridges for code not ported. A view still adds `env.config`
and `env.model` for its subtree. Import `_t` from `@web/core/l10n/translation`.

Never assign a key to `env`: it reaches every component and hides where the value
comes from. Share it through a plugin instead.