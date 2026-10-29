"""The parts of `tests.md` about test tools that differ per version: Form, time, HTTP, XSD."""

from __future__ import annotations

from ..version import OdooVersion


class TestTools:
    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "form_import": version.pick(
                v16="Import it with `from odoo.tests import Form`.",
                v17_="Import it with `from odoo.tests import Form`; `odoo.tests.common.Form` is\n  deprecated.",
            ),
            "from_action": version.pick(
                v16_17="",
                v18_="\n- `Form.from_action(self.env, action)` opens the form that a window action returned\n"
                "  by a button describes, to go on as the user would.",
            ),
            "freeze": version.pick(
                v16_17="Use `freezegun`, a dependency of Odoo: `from freezegun import freeze_time`, then\n"
                "`@freeze_time('2024-01-31')` on a test method, or `with freeze_time('2024-01-31'):`\n"
                "around the code that reads the date.",
                v18_="Use `from odoo.tests import freeze_time`, then `@freeze_time('2024-01-31')` on a test\n"
                "method, or `with freeze_time('2024-01-31'):` around the code that reads the date. On a\n"
                "`TransactionCase` class it freezes `setUpClass` and every test of the class.",
            ),
            "jsonrpc": version.pick(
                v16="",
                v17_="\n  `self.make_jsonrpc_request('/library/lend', {'book_id': book.id})` calls a JSON-RPC\n"
                "  route and returns its `result`.",
            ),
            "tour_url": version.pick(v16_17="/web", v18_="/odoo"),
            "tour_js": version.pick(
                v16="`tour.register('library_lend_tour', {test: true, url: ...}, [...])` (from\n  `web_tour.tour`)",
                v17_='`registry.category("web_tour.tours").add(\'library_lend_tour\', {steps: () => [...]})`',
            ),
            "tour": version.pick(
                v16_17="- A tour's last step leaves the client stable (no pending edit, no request in\n"
                "  flight), or the teardown races the browser.",
                v18_="- A tour step that unloads the page sets `expectUnloadPage: true`, and the last step\n"
                "  leaves the client stable (no pending edit, no request in flight), or the teardown\n"
                "  races the browser.",
            ),
            "xsd": version.pick(
                v16_17="",
                v18_="\n- `@test_xsd(path='library/data/book.xsd')` (or `url=...`) on a method that returns\n"
                "  XML documents validates each of them against that XSD schema.",
            ),
        }
