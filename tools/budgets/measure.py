"""One sized piece of a skill and the budget it must fit in."""

from __future__ import annotations

from dataclasses import dataclass

from .constants import CHARS_PER_TOKEN


@dataclass(frozen=True)
class Measure:
    """The size of a description, a body or a file, against its limit."""

    label: str
    size: int
    limit: int

    @property
    def tokens(self) -> int:
        return self.size // CHARS_PER_TOKEN

    @property
    def exceeded(self) -> bool:
        return self.size > self.limit
