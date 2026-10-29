"""Access rows and record rules of `security.md`: two models up to 19.0, one `ir.access` in 20.0."""

from __future__ import annotations

from ..version import OdooVersion
from .security_legacy import LegacyAccess
from .security_unified import UnifiedAccess


class AccessBlocks:
    """Picks the text of the access model the version has."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        if version.number >= 20:
            return {
                "layers": UnifiedAccess.layers,
                "access_file": "`ir.access.csv`",
                "access_rows": UnifiedAccess.rows,
                "record_rules": UnifiedAccess.rules,
            }
        return {
            "layers": LegacyAccess.layers.format(version=version.name),
            "access_file": "`ir.model.access.csv`",
            "access_rows": LegacyAccess.rows,
            "record_rules": LegacyAccess.rules.format(rule_context=self.rule_context(version)),
        }

    @staticmethod
    def rule_context(version: OdooVersion) -> str:
        return version.pick(
            v16_18="`user`, `time`, `company_ids` and `company_id`",
            v19_="`user`, `company_ids` and `company_id` (`time` is not\n  available in this version)",
        )
