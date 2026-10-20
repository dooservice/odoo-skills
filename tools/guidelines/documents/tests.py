"""`odoo-guidelines/guidelines/tests.md`: test classes, tags and the ways tests are skipped."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Tests(Document):
    path = "odoo-guidelines/guidelines/tests.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "tags": self.default_tags(version),
            "inherited": version.pick(
                v16_17="\n  defines its own.",
                v18_="\n  sets `allow_inherited_tests_method = True`.",
            ),
            "tour": self.tour(version),
        }

    def default_tags(self, version: OdooVersion) -> str:
        return version.pick(
            v16_19=f"""- Tests are tagged `standard` and **`at_install`** by default in {version.name}: they run
  before the other modules are installed. Business tests should run on a fully
  loaded registry: decorate them `@tagged('post_install', '-at_install')`. An
  `HttpCase` (tours) must be `post_install`.""",
            v20="""- Tests are tagged `standard` and `post_install` by default (fully-loaded
  registry); set exactly one of `at_install`/`post_install`. Opt into
  `@tagged('at_install', '-post_install')` only when the test must run before
  other modules load, with a comment justifying it; an `HttpCase` must stay
  `post_install`.""",
        )

    def tour(self, version: OdooVersion) -> str:
        return version.pick(
            v16_17="""- Tours: the last step must leave the client in a stable state (no pending
  edits or in-flight requests), or the teardown races the browser.""",
            v18_="""- Tours: a step that triggers a page unload must set `expectUnloadPage: true`,
  and the last step must leave the client in a stable state (no pending edits
  or in-flight requests).""",
        )
