"""One Odoo version, and how a document picks what differs between versions."""

from __future__ import annotations


class OdooVersion:
    """A major version, such as 18, that documents compare against and pick from.

    `pick` takes one value per range of versions, named `v16` (one version), `v17_18`
    (from 17 to 18) or `v19_` (19 and later):

        version.pick(v16_17="`attrs`", v18_="expressions")
    """

    def __init__(self, number: int) -> None:
        self.number = number

    @property
    def name(self) -> str:
        return f"{self.number}.0"

    @property
    def translate(self) -> str:
        """The translation call in model code."""
        return "self.env._" if self.number >= 18 else "_"

    def pick(self, **values_by_span: str) -> str:
        for span, value in values_by_span.items():
            if self.within(span.removeprefix("v")):
                return value
        raise KeyError(f"no value for {self.name} in {sorted(values_by_span)}")

    def within(self, span: str) -> bool:
        first, separator, last = span.partition("_")
        if not separator:
            return self.number == int(first)
        return int(first) <= self.number and (not last or self.number <= int(last))
