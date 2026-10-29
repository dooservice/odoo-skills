"""What differs between versions in checking access from code."""

from __future__ import annotations

from ..version import OdooVersion


class OrmAccess:
    """The template values of the "Check access rights in code" section of `orm.md`."""

    #: How the model and record checks work from 18.0 on.
    CHECK_ACCESS = (
        "- `records.check_access('write')` checks the access list of the model and the "
        "record rules on the records, and raises `AccessError`; `records.has_access('write')` "
        "returns a boolean instead, and `records._filtered_access('write')` the accessible "
        "subset. On an empty recordset they check the model only."
    )

    def __init__(self, version: OdooVersion) -> None:
        self.version = version

    def values(self) -> dict[str, str]:
        pick = self.version.pick
        return {
            "access_checks": pick(
                v16_17="- `records.check_access_rights('write')` checks the access list "
                "(`ir.model.access`) of the model; `records.check_access_rule('write')` checks "
                "the record rules on the records: call both. With "
                "`raise_exception=False`, `check_access_rights` returns a boolean instead of "
                "raising.\n- `records._filter_access_rules('write')` returns the accessible "
                "subset.",
                v18_19=self.CHECK_ACCESS + "\n- `check_access_rights` and `check_access_rule` "
                "are deprecated: replace them with `check_access`.",
                v20=self.CHECK_ACCESS + "\n- `check_access_rights` and `check_access_rule` no "
                "longer exist.",
            ),
            "field_access": pick(
                v16_18="`check_field_access_rights(operation, field_names)` raises "
                "`AccessError` when a field of the list is restricted by `groups`; without "
                "names it returns the fields the user may access.",
                v19="`check_field_access_rights` is deprecated: `fields_get` lists the fields "
                "the user may access.",
                v20="`self.check_field_access(field, 'read')` raises and "
                "`self.has_field_access(field, 'write')` returns a boolean, for one `Field` "
                "object (`self._fields['isbn']`); both check the field's `groups`. "
                "`check_field_access_rights` no longer exists.",
            ),
            "user_groups": pick(
                v16_17="Test the user's groups with `self.env.user.has_group('base.group_system')`; "
                "`self.user_has_groups('base.group_user,!base.group_portal')` takes the "
                "comma-separated syntax of `groups`.",
                v18_="Test the user's groups with `self.env.user.has_group('base.group_system')`, "
                "or `self.env.user.has_groups('base.group_user,!base.group_portal')` for the "
                "comma-separated syntax of `groups`. `user_has_groups` no longer exists.",
            ),
        }
