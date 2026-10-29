"""The parts of `tests.md` that differ per version: test classes, collection and test tools."""

from __future__ import annotations

from ..version import OdooVersion


class TestClasses:
    """Which test classes exist, their default tags, and how the runner collects them."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "classes": "\n".join((
                ("- `TransactionCase`: the default. `setUpClass` runs once, each test runs in a\n"
                "  savepoint rolled back after it."),
                ("- `HttpCase`: a `TransactionCase` with a test HTTP server and a headless Chrome,\n"
                "  for routes, controllers and tours."),
                version.pick(
                    v16_19="- `SingleTransactionCase`: all tests of the class share one transaction, rolled back\n"
                    "  after the last one, so each test sees what the previous ones wrote and the\n"
                    "  result depends on their order. Keep it for read-only checks of a costly setup.",
                    v20="- There is no `SingleTransactionCase`: build what the tests share in the\n"
                    "  `setUpClass` of a `TransactionCase`.",
                ),
                ("- `BaseCase`: the base of the classes above, with Odoo's assertions and no cursor of\n"
                "  its own. Derive from it directly only for tests that never touch the database."),
                ("- `TestCase` (`odoo.tests.case`): Odoo's rewrite of `unittest.TestCase` under\n"
                "  `BaseCase`. Never derive from it directly: it carries no test tags."),
                version.pick(
                    v16="- `SavepointCase` and `HttpSavepointCase` are deprecated aliases of `TransactionCase`\n"
                    "  and `HttpCase` (subclassing them warns): write the new names.",
                    v17="- `SavepointCase` and `HttpSavepointCase` no longer exist: `TransactionCase` and\n"
                    "  `HttpCase` replace them.",
                    v18_="",
                ),
            )).rstrip(),
            "default_tags": version.pick(
                v16_19="- Tests are tagged `standard` and `at_install` by default: they run before the\n"
                "  modules that depend on theirs are loaded. Business tests need the full registry:\n"
                "  decorate them `@tagged('post_install', '-at_install')`.",
                v20="- Tests are tagged `standard` and `post_install` by default (fully loaded\n"
                "  registry). Opt into `@tagged('at_install', '-post_install')` only when the test\n"
                "  must run before the modules that depend on yours load, with a comment saying why.",
            ),
            "collection": version.pick(
                v16_17="- Every test class reachable from the file is collected, imported ones included:\n"
                "  a test class imported into a second test file runs twice, and inherited `test_*`\n"
                "  methods run in every subclass. Put shared base classes in a file that is not a\n"
                "  `test_*.py` (`tests/common.py`) and give them no `test_*` method.",
                v18_="- The class must be defined in the file: a class imported into it is not\n"
                "  collected. Inherited `test_*` methods are not collected either: a subclass runs\n"
                "  only the tests it defines, unless it sets `allow_inherited_tests_method = True`.",
            ),
            "base_common": self.base_common(version),
        }

    def base_common(self, version: OdooVersion) -> str:
        common = (
            "- `BaseCommon` (from `odoo.addons.base.tests.common`) is a ready `TransactionCase`:\n"
            "  mail tracking and notifications off in the `cls.env` context"
        )
        usd = ", the main company's currency\n  set to USD"
        later = (
            f"{usd}, and `cls.partner`, `cls.company`, `cls.currency` and\n"
            "  `cls.group_user`."
        )
        return common + version.pick(
            v16=f"{usd}, and a `cls.partner`. Start business tests from it, or\n"
            "  from a common class of your module built on it.",
            v17=", a `cls.partner` and `cls.currency`. Start business tests\n"
            "  from it, or from a common class of your module built on it.",
            v18_19=f"{later} Override `setup_independent_user()` or\n"
            "  `setup_independent_company()` to run the class as its own user or company, and\n"
            "  `default_env_context()` to turn mail tracking back on.",
            v20=f"{later} Each test runs as `cls._test_user`, an internal user\n"
            "  with the groups of `_test_user_groups` (`base.group_user` by default), not as the\n"
            "  superuser: add the groups the test needs, or set `_test_user_groups = ()` to keep\n"
            "  the superuser. Override `setup_independent_company()` to run the class in its own\n"
            "  company.",
        )
