"""Cuts markdown prose into normalised sentences, leaving code blocks out."""

from __future__ import annotations

from .constants import BLOCK_STARTS, CODE_FENCE, SENTENCE_ENDS, WORD_PUNCTUATION


class SentenceSplitter:
    """The sentences of a markdown text, each as its lowercase words."""

    def __init__(self, text: str) -> None:
        self.text = text

    def blocks(self) -> list[list[str]]:
        blocks: list[list[str]] = [[]]
        in_code = False
        for line in self.text.splitlines():
            stripped = line.strip()
            if stripped.startswith(CODE_FENCE):
                in_code = not in_code
                blocks.append([])
                continue
            if in_code:
                continue
            if not stripped or stripped.startswith(BLOCK_STARTS):
                blocks.append([])
            blocks[-1].extend(stripped.split())
        return [block for block in blocks if block]

    def sentences(self) -> list[str]:
        found = []
        for block in self.blocks():
            current: list[str] = []
            for word in block:
                cleaned = word.strip(WORD_PUNCTUATION).lower()
                if cleaned:
                    current.append(cleaned)
                if word.endswith(SENTENCE_ENDS):
                    found.append(" ".join(current))
                    current = []
            found.append(" ".join(current))
        return [sentence for sentence in found if sentence]
