"""The versions the guideline skills are built for, and where their parts live."""

from __future__ import annotations

from pathlib import Path

#: Odoo's major versions, as numbers: the documents compare against them.
VERSIONS = (16, 17, 18, 19, 20)

#: The skills this builder writes in `odoo/<version>/`; anything else there is left alone.
SKILLS = ("odoo-guidelines", "odoo-web-guidelines", "odoo-review", "odoo-security", "odoo-git")

#: The Markdown each document fills in, laid out as the skills are.
TEMPLATES = Path(__file__).resolve().parent / "templates"

#: Typographic punctuation the skills must not contain: they teach plain ASCII.
TYPOGRAPHIC = ("—", "–", "“", "”", "‘", "’", "…")

#: The one document that shows that punctuation, to say what to avoid.
SHOWS_TYPOGRAPHIC = "comments.md"
