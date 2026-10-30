"""Splits a SKILL.md into its description and its body."""

from __future__ import annotations

from .constants import BLOCK_MARKERS, DESCRIPTION_KEY, FRONT_MATTER_FENCE, VALUE_QUOTES


class SkillText:
    """The front matter and body of one SKILL.md."""

    def __init__(self, text: str) -> None:
        self.lines = text.splitlines()

    def closing_line(self) -> int:
        if not self.lines or self.lines[0].strip() != FRONT_MATTER_FENCE:
            return -1
        rest = [line.strip() for line in self.lines[1:]]
        return rest.index(FRONT_MATTER_FENCE) + 1 if FRONT_MATTER_FENCE in rest else -1

    def front_matter(self) -> list[str]:
        return self.lines[1 : self.closing_line()] if self.closing_line() > 0 else []

    def body(self) -> str:
        return "\n".join(self.lines[self.closing_line() + 1 :]).strip()

    def description(self) -> str:
        lines = self.front_matter()
        starts = [index for index, line in enumerate(lines) if line.startswith(DESCRIPTION_KEY)]
        if not starts:
            return ""
        value = lines[starts[0]].removeprefix(DESCRIPTION_KEY).strip()
        if value not in BLOCK_MARKERS:
            return value.strip(VALUE_QUOTES)
        following = []
        for line in lines[starts[0] + 1 :]:
            if line and not line.startswith(" "):
                break
            following.append(line.strip())
        return " ".join(part for part in following if part)
