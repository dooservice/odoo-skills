"""The calls of `security.md` that test group membership, record access and field access."""

from __future__ import annotations

from ..version import OdooVersion


class AccessCalls:
    """`user_has_groups` and `check_access_rights` gave way to `has_groups` and `check_access` in 18.0."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "group_checks": version.pick(v16_17=self.checks_one(), v18_=self.checks_many()),
            "field_check": version.pick(
                v16_19="To test field access in code, call\n"
                "  `check_field_access_rights('read', ['field_name'])`: it raises\n"
                "  `AccessError` on a refused field, and without names returns the readable ones.",
                v20="To test field access in code, call\n"
                "  `has_field_access(record._fields['field_name'], 'read')` or\n"
                "  `check_field_access(...)`, which take the field object, not its name.",
            ),
            "check_access": version.pick(
                v16_17="`records.check_access_rights('write')` then\n  `records.check_access_rule('write')`",
                v18_="`records.check_access('write')` (or `has_access` for a\n  boolean, `_filtered_access` to keep the allowed records)",
            ),
        }

    @staticmethod
    def checks_one() -> str:
        return """\
- `self.env.user.has_group('library.group_library_manager')` tests one group.
- `self.user_has_groups('library.group_library_manager,!base.group_portal')`
  tests a comma-separated list where `!` negates a group.
- `has_group('base.group_no_one')` is true for every internal user, debug mode
  or not; only `user_has_groups` applies the debug-mode rule of that group."""

    @staticmethod
    def checks_many() -> str:
        return """\
- `self.env.user.has_group('library.group_library_manager')` tests one group.
- `self.env.user.has_groups('library.group_library_manager,!base.group_portal')`
  tests a comma-separated list where `!` negates a group. `user_has_groups` no
  longer exists.
- Both apply the debug-mode rule of `base.group_no_one` (technical features)."""
