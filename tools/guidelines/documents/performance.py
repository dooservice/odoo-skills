"""`odoo-guidelines/guidelines/performance.md`: batched ORM calls and cheap loops."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Performance(Document):
    path = "odoo-guidelines/guidelines/performance.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "grouped_read": version.pick(v16="read_group", v17_="_read_group"),
            "grouped_counts": self.grouped_counts(version),
        }

    def grouped_counts(self, version: OdooVersion) -> str:
        """The grouped query that counts books per author, and the dict built from it."""
        return version.pick(
            v16="""\
groups = Book.read_group([('author_id', 'in', authors.ids)], ['author_id'], ['author_id'])
counts = {group['author_id'][0]: group['author_id_count'] for group in groups}""",
            v17_="""\
counts = {
    author.id: count
    for author, count in Book._read_group(
        [('author_id', 'in', authors.ids)], ['author_id'], ['__count'],
    )
}""",
        )
