"""The Claude Code marketplace, made from the folders: one plugin per version."""

from __future__ import annotations

import json

from .constants import (
    COMMON_FOLDER,
    LICENSE,
    MARKETPLACE,
    MARKETPLACE_FILE,
    VERSIONS_FOLDER,
)


class Marketplace:
    def versions(self) -> list[str]:
        folders = [folder.name for folder in VERSIONS_FOLDER.iterdir() if folder.is_dir()]
        return sorted((name for name in folders if name != COMMON_FOLDER), key=float)

    def version_plugin(self, version: str) -> dict:
        return {
            "name": f"odoo-{version.split('.')[0]}",
            "source": "./",
            "description": (
                f"Odoo {version}: guidelines, web, security, review, git, upgrade, "
                f"functional configuration and the {version} reference"
            ),
            "skills": [f"./odoo/{version}/", f"./odoo/{COMMON_FOLDER}/"],
            "license": LICENSE,
            "keywords": ["odoo", "erp", version],
        }

    def content(self) -> str:
        plugins = [self.version_plugin(version) for version in self.versions()]
        return json.dumps({**MARKETPLACE, "plugins": plugins}, indent=2, ensure_ascii=False) + "\n"

    def is_current(self) -> bool:
        return MARKETPLACE_FILE.read_text(encoding="utf-8") == self.content()

    def write(self) -> None:
        MARKETPLACE_FILE.write_text(self.content(), encoding="utf-8")
