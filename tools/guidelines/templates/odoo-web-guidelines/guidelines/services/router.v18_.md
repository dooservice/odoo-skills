`import { router } from "@web/core/browser/router"` gives `router.current`, the
state of the URL as a flat object, and `router.pushState(state, { replace, reload })`.
There is no `router` service. The action service keeps the URL (`/odoo/...`) in sync
with the action; change it yourself only for state of your own client action (a
selected tab), with keys prefixed by your module.