"""The values of `actions.md` about server actions and scheduled actions."""

from __future__ import annotations

from ..version import OdooVersion
from .cron_values import CronValues


class ServerActionValues:
    """What `ir.actions.server` offers in each version, and its eval context."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **CronValues().values(version),
            "server_states": version.pick(
                v16="`code`, `object_create`, `object_write` (the default) or `multi`; `mail`\n"
                "adds `mail_post`, `followers` and `next_activity`, `sms` adds `sms`.",
                v17_18="`object_write` (the default), `object_create`, `code`, `webhook` or `multi`;\n"
                "`mail` adds `next_activity`, `mail_post`, `followers` and `remove_followers`,\n"
                "`sms` adds `sms`.",
                v19="`object_write`, `object_create`, `object_copy`, `code`, `webhook` or `multi`,\n"
                "with no default: always set `state`; `mail` adds `next_activity`,\n"
                "`mail_post`, `followers` and `remove_followers`, `sms` adds `sms`.",
                v20="`object_write`, `object_create`, `object_copy`, `code`, `webhook` or `multi`,\n"
                "with no default: always set `state`; `mail` adds `next_activity`,\n"
                "`mail_post`, `log_note`, `followers` and `remove_followers`, `sms` adds `sms`.",
            ),
            "code_state": self.code_state(version),
            "object_write": version.pick(
                v16="one `fields_lines` row (`ir.server.object.lines`) per field, its\n"
                "  `value` a constant (`evaluation_type` `value`), an xml id (`reference`) or\n"
                "  a Python expression (`equation`).",
                v17_18="`update_path` names the field (`partner_id.name` follows relations),\n"
                "  `value` with `evaluation_type` `value` or `equation` (a Python expression),\n"
                "  `update_m2m_operation` (`add`, `remove`, `set`, `clear`) for many2many, and\n"
                "  `update_boolean_value` for booleans. One field per action: chain several\n"
                "  with `multi`.",
                v19_="`update_path` names the field (`partner_id.name` follows relations),\n"
                "  `value` with `evaluation_type` `value`, `equation` (a Python expression)\n"
                "  or `sequence` (next number of `sequence_id`), `update_m2m_operation` (`add`,\n"
                "  `remove`, `set`, `clear`) for many2many, and `update_boolean_value` for\n"
                "  booleans. One field per action: chain several with `multi`.",
            ),
            "object_copy": version.pick(
                v16_18="",
                v19_="\n- `object_copy` duplicates the `resource_ref` record and links the copy like\n"
                "  `object_create`.",
            ),
            "children": version.pick(
                v16_18="(`child_ids`, a many2many)",
                v19_="(`child_ids`, a one2many on `parent_id`; children take the\n  parent's model and groups)",
            ),
            "webhook": version.pick(
                v16="",
                v17_="\n- `webhook` POSTs `_model`, `_id` and the `webhook_field_ids` of the active\n"
                "  record as JSON to `webhook_url`.",
            ),
            "history": version.pick(
                v16_18="",
                v19_="\n\nEach change of `code` is saved in `ir.actions.server.history` (the last 100\n"
                "per action), and the action form compares and restores versions: a\n"
                "migration that rewrites `code` leaves a restorable trace.",
            ),
        }

    def code_state(self, version: OdooVersion) -> str:
        """The names a `code` server action can use."""
        logger = version.pick(v16="", v17_=", `_logger`")
        warning = version.pick(v16=", `Warning`", v17_="")
        timezone = version.pick(v16_19="`timezone` (pytz)", v20="`timezone` (`ZoneInfo`)")
        return (
            "- `code` runs Python (`code`, editable by `base.group_system` only) with\n"
            "  `env`, `model` (empty recordset of `model_id`), `record` and `records` (from\n"
            "  `active_id`/`active_ids`), `log(message, level)`" + logger + ", `UserError`"
            + warning + ",\n  `Command`, `time`, `datetime`, `dateutil`, " + timezone
            + ", `float_compare`,\n  `b64encode`, `b64decode`, `uid` and `user`. Assign `action = {...}` to"
            " return\n  an action. No `import`: `safe_eval` refuses it."
        )
