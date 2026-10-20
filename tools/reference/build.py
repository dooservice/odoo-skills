"""Builds `odoo/<version>/odoo-reference` from the Odoo source of each version."""

from __future__ import annotations

import shutil
from pathlib import Path

from .constants import HERE, SKIPPED_PREFIXES
from .manifests import Addons
from .models import ModelScanner
from .settings import SettingsScanner
from .writer import ReferenceWriter
from .xmlids import XmlIdScanner


class ReferenceBuild:
    def __init__(self, sources: Path, repository: Path) -> None:
        self.sources = sources
        self.repository = repository
        self.models = ModelScanner()
        self.settings = SettingsScanner()
        self.xmlids = XmlIdScanner()

    def build(self, version: str) -> int:
        root = self.repository / "odoo" / version / "odoo-reference"
        if root.exists():
            shutil.rmtree(root)
        writer = ReferenceWriter(root)
        index, settings = [], []
        addons = [addon for addon in Addons(self.sources / version).all() if not addon.name.startswith(SKIPPED_PREFIXES)]
        for addon in addons:
            models = self.models.scan(addon)
            declared = self.xmlids.scan(addon)
            settings += self.settings.scan(addon)
            if models:
                writer.models(addon, models)
            if declared:
                writer.xmlids(addon, declared)
            index.append((addon, models))
        writer.index(index)
        writer.settings(settings)
        writer.write("SKILL.md", (HERE / "SKILL.md.in").read_text(encoding="utf-8").format(version=version))
        return len(addons)
