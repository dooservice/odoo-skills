"""The rows of `version.md` about the user interface: views, QWeb, Owl and JavaScript."""

from __future__ import annotations

from ..version import OdooVersion


class InterfaceVersionNotes:
    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **self.views(version),
            "qweb_output": version.pick(
                v16_19="`t-out`; `t-esc` still works, `t-raw` logs a deprecation warning",
                v20="`t-out` only; `t-esc` and `t-raw` are gone from server QWeb",
            ),
            "owl": version.pick(v16_19="Owl 2", v20="Owl 3 (`signal`, `computed`)"),
            "js_module_header": version.pick(
                v16_17="every file under `static/src` starts with `/** @odoo-module **/`",
                v18_="none needed",
            ),
            "js_patch": version.pick(
                v16='`patch(Target.prototype, "module.name", { ... })`',
                v17_="`patch(Target.prototype, { ... })`",
            ),
            "js_field_registry": version.pick(
                v16='`registry.category("fields").add("x", MyField)`, the component itself',
                v17_='`registry.category("fields").add("x", { component: MyField, ... })`',
            ),
            "js_rpc": version.pick(
                v16_17='`this.rpc = useService("rpc")`; `this.orm = useService("orm")`',
                v18_19='`import { rpc } from "@web/core/network/rpc"`; `useService("orm")`',
                v20='`import { rpc } from "@web/core/network/rpc"`; `usePlugin(ORM)`, `ORM` from `@web/core/orm_plugin`',
            ),
            "js_shared_logic": version.pick(
                v16_19='services: `registry.category("services").add("x", { dependencies, start })`, used with `useService("x")`',
                v20='plugins: `class X extends Plugin` (`@odoo/owl`), `services.add(X)` (`@web/core/services`), used with '
                '`usePlugin(X)`; the `services` registry still starts, after the plugins, for code not moved yet',
            ),
            "js_tests": version.pick(
                v16_17="QUnit, under `static/tests/`, in the `web.qunit_suite_tests` bundle",
                v18="hoot (`@odoo/hoot`), `*.test.js` in `web.assets_unit_tests`; QUnit only for legacy suites",
                v19_="hoot (`@odoo/hoot`), `*.test.js` in `web.assets_unit_tests`",
            ),
        }

    def views(self, version: OdooVersion) -> dict[str, str]:
        return {
            "view_modifiers": version.pick(
                v16="`attrs=\"{'invisible': [('state', '!=', 'draft')]}\"` and `states=\"draft,sent\"`",
                v17_="Python expressions on the attribute itself: `invisible=\"state != 'draft'\"`, "
                "`readonly=`, `required=`, `column_invisible=`. `attrs` and `states` are refused "
                "with a ValidationError",
            ),
            "list_view": version.pick(
                v16_17="`<tree>`, view_mode `tree`, xml id `<model>_view_tree`",
                v18_="`<list>`, view_mode `list`, xml id `<model>_view_list`. `<tree>` and `tree` are gone",
            ),
            "chatter": version.pick(
                v16_17='`<div class="oe_chatter">` with `message_follower_ids`, `activity_ids`, `message_ids`',
                v18_="`<chatter/>` at the end of the form",
            ),
        }
