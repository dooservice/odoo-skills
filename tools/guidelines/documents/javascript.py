"""`odoo-web-guidelines/guidelines/javascript.md`: the web framework of each version."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Javascript(Document):
    path = "odoo-web-guidelines/guidelines/javascript.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {**super().values(version), **self.framework(version), **self.safety(version)}

    def framework(self, version: OdooVersion) -> dict[str, str]:
        return {
            "header": version.pick(
                v16_17="- Every JavaScript file under `static/src` starts with `/** @odoo-module **/`;\n"
                "  without it the file is not transpiled and its `import`s fail.",
                v18_="- Files under `static/src` are ES modules; no `@odoo-module` header is needed.",
            ),
            "owl": version.pick(
                v16_19="Owl 2: state with `useState`, lifecycle with `onWillStart`/`onMounted`/`onWillUnmount`",
                v20="Owl 3: reactive `signal` and `computed` next to `useState`; lifecycle with `onWillStart`/`onMounted`/`onWillUnmount`",
            ),
            "field": version.pick(
                v16='`registry.category("fields").add("my_widget", MyField)` registers the component',
                v17_='`registry.category("fields").add("my_widget", { component: MyField, supportedTypes: [...] })` registers a descriptor',
            ),
            "rpc": version.pick(
                v16_17='`useService("rpc")` for a route, `useService("orm")` for model methods',
                v18_='`import { rpc } from "@web/core/network/rpc"` for a route, `useService("orm")` for model methods',
            ),
            "patch": version.pick(
                v16='`patch(Target.prototype, "my_module.Target", { setup() { super.setup(); ... } })`',
                v17_="`patch(Target.prototype, { setup() { super.setup(...arguments); ... } })`",
            ),
        }

    def safety(self, version: OdooVersion) -> dict[str, str]:
        return {
            "html": version.pick(
                v16_17="escape with `escape` from `@web/core/utils/strings` or render through `t-out`",
                v18="escape with `htmlEscape` and set content with `setElementContent` (`@web/core/utils/html`), or render through `t-out`",
                v19_="escape with `htmlEscape`, build with `htmlJoin`/`htmlSprintf`, and set content with `setElementContent` (`@web/core/utils/html`), or render through `t-out`",
            ),
            "tests": version.pick(
                v16_17="QUnit, under `static/tests/`, added to `web.qunit_suite_tests`; run in the browser at `/web/tests`",
                v18="hoot (`@odoo/hoot`): `*.test.js` under `static/tests/`, added to `web.assets_unit_tests`; QUnit is only for legacy suites",
                v19_="hoot (`@odoo/hoot`): `*.test.js` under `static/tests/`, added to `web.assets_unit_tests`",
            ),
        }
