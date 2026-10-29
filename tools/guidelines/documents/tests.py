"""`odoo-guidelines/guidelines/tests.md`: test classes, tags, collection, tools and selection."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .tests_tools import TestTools
from .tests_values import TestClasses


class Tests(Document):
    path = "odoo-guidelines/guidelines/tests.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            **TestClasses().values(version),
            **TestTools().values(version),
            "demo_default": version.pick(
                v16_18=" (a database created with\n  `--without-demo` has none)",
                v19_=" (a new database has none\n  unless created with `--with-demo`)",
            ),
            "commit": version.pick(
                v16_17="the changes would stay in the test database and\n"
                "  break the rollback that isolates each test.",
                v18_="it raises `AssertionError`.",
            ),
            "file_filter": version.pick(
                v16_18="A module part ending in `.py` selects the tests of one file:\n"
                "  `/library/tests/test_lending.py`.",
                v19_="A path ending in `.py` selects the tests of one file:\n"
                "  `/library/tests/test_lending.py`, or an absolute path; `--test-file <path>` adds\n"
                "  such a filter to the spec.",
            ),
        }
