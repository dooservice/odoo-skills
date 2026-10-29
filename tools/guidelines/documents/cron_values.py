"""The values of `actions.md` about `ir.cron`."""

from __future__ import annotations

from ..version import OdooVersion


class CronValues:
    """Fields, progress reporting and failure handling of scheduled actions per version."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "cron_fields": version.pick(
                v16_17='\n    <field name="numbercall">-1</field>',
                v18_="",
            ),
            "cron_removed": version.pick(
                v16_17="\n- `numbercall` is the number of runs left (`-1` for ever, the usual value);\n"
                "  `doall` replays the runs missed while the server was down: leave it\n"
                "  `False`, a batch method catches up on its own.",
                v18_="\n- A cron runs until deactivated; it has no `numbercall` or `doall`.",
            ),
            "cron_progress": version.pick(
                v16_17="process a limited batch (`search(..., limit=...)`), then call\n"
                "  `self.env.ref(...)._trigger()` when records remain, so one run never holds\n"
                "  the cron lock for long.",
                v18="process a limited batch, report it with\n"
                "  `self.env['ir.cron']._notify_progress(done=..., remaining=...)`: the cron\n"
                "  reruns itself while `remaining` is not zero and a run that reports progress\n"
                "  does not count as a failure.",
                v19_="loop over batches and call\n"
                "  `self.env['ir.cron']._commit_progress(len(batch), remaining=...)` after each:\n"
                "  it commits, returns the seconds left in the run (stop at `0`), and the\n"
                "  cron reruns itself while work remains. `_notify_progress` is deprecated.",
            ),
            "cron_failures": version.pick(
                v16_17="\n- A failing run rolls back and is retried at the next interval, without limit:\n"
                "  log and skip a bad record rather than raise on it.",
                v18_19="\n- A failing run rolls back; after 5 consecutive failures spanning at least\n"
                "  7 days the cron deactivates itself (`failure_count`, `first_failure_date`).\n"
                "  Log and skip a bad record rather than raise on it.",
                v20="\n- A failing run rolls back; after 5 consecutive failures spanning at least\n"
                "  7 days the cron deactivates itself (`failure_count`, `first_failure_date`),\n"
                "  after a warning. Log and skip a bad record rather than raise on it.",
            ),
        }
