"""`odoo-review/SKILL.md`: Odoo's review skill's description, with our own process."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class ReviewSkill(Document):
    """The front matter and introduction come from Odoo's skill; `## Process` on is ours."""

    path = "odoo-review/SKILL.md"

    def render(self, version: OdooVersion) -> str:
        return self.introduction(version) + super().render(version)

    def introduction(self, version: OdooVersion) -> str:
        introduction = self.read_upstream(self.path).split("## Process", 1)[0]
        introduction = introduction.replace(
            "  Review Odoo addon code against the house rules,",
            f"  Review Odoo {version.name} addon code against the house rules,",
        )
        if version.number < 20:
            introduction = introduction.replace("`ir.access` rows", "`ir.model.access` rows, `ir.rule`")
        return introduction
