"""`odoo-web-guidelines/SKILL.md`: the web guidelines skill and its table of sections.

The description carries the web framework names that change most between versions, for
an agent that writes from memory without loading the skill.
"""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class WebSkill(Document):
    path = "odoo-web-guidelines/SKILL.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        """`major` is the version as in a heading's anchor: `#the-web-framework-in-180`."""
        return {**super().values(version), "major": str(version.number), "names": self.names(version)}

    @staticmethod
    def names(version: OdooVersion) -> str:
        return version.pick(
            v16=(
                "Owl 2; `odoo.define` modules or ES modules with `/** @odoo-module **/`; "
                "`patch(object, name, extension)` with `this._super`; the `rpc` and `orm` "
                "services; QUnit tests; tours with `tour.register`."
            ),
            v17=(
                "Owl 2; ES modules need `/** @odoo-module **/`; `patch(object, extension)` "
                "with `super`; `useService(\"rpc\")` and `useService(\"orm\")`; QUnit tests; "
                "tours in `registry.category(\"web_tour.tours\")`."
            ),
            v18=(
                "Owl 2; the `@odoo-module` header is optional; `patch(object, extension)` with "
                "`super`; `rpc` is a function from `@web/core/network/rpc` (no rpc service); "
                "hoot tests, `*.test.js` with `@odoo/hoot`."
            ),
            v19=(
                "Owl 2; `patch(object, extension)` with `super`; `rpc` function; frontend code "
                "as Interactions in `public.interactions` (`publicWidget` is legacy); hoot "
                "tests, `*.test.js` with `@odoo/hoot`."
            ),
            v20=(
                "Owl 3: no `useState`, use `proxy`, `signal` and `computed`, props through "
                "`useProps`; plugins with `usePlugin` (the ORM is `usePlugin(ORM)`); no "
                "`publicWidget`, frontend code as Interactions; hoot tests."
            ),
        )
