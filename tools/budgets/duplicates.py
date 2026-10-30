"""Finds long sentences that two files of the same skill both hold."""

from __future__ import annotations

from .constants import DUPLICATE_WORDS
from .sentences import SentenceSplitter
from .skill import Skill


class DuplicateFinder:
    """Sentences of DUPLICATE_WORDS words or more repeated across files of a skill."""

    def __init__(self, skill: Skill) -> None:
        self.skill = skill

    def owners(self) -> dict[str, set[str]]:
        owners: dict[str, set[str]] = {}
        for label, text in self.skill.texts().items():
            for sentence in SentenceSplitter(text).sentences():
                if len(sentence.split()) >= DUPLICATE_WORDS:
                    owners.setdefault(sentence, set()).add(label)
        return owners

    def repeated(self) -> dict[str, list[str]]:
        found = self.owners().items()
        return {sentence: sorted(labels) for sentence, labels in found if len(labels) > 1}

    def render(self) -> list[str]:
        lines = []
        for sentence, labels in sorted(self.repeated().items()):
            lines.append(f"- {sentence}")
            lines += [f"    {label}" for label in labels]
        return lines
