"""Where the skills live in the repository, and what the catalog says about them."""

from __future__ import annotations

from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent.parent
MARKETPLACE_FILE = REPOSITORY / ".claude-plugin" / "marketplace.json"
VERSIONS_FOLDER = REPOSITORY / "odoo"
COMMON_FOLDER = "common"
LOCALIZATIONS_FOLDER = REPOSITORY / "localization"
#: The folder a country copies; it is not a localization itself.
TEMPLATE_FOLDER = "template"
LICENSE = "LGPL-3.0-only"

MARKETPLACE = {
    "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
    "name": "odoo-skills",
    "description": (
        "Agent skills for Odoo 16.0 to 20.0, each checked against its version's source. "
        "Install the plugin of the version you run, and the one of your country if there is one."
    ),
    "owner": {"name": "dooservice", "url": "https://dooservice.sh"},
}

#: The sections every localization's SKILL.md has, in this order.
LOCALIZATION_SECTIONS = (
    "## Modules",
    "## Chart of accounts and taxes",
    "## Contacts",
    "## Electronic invoicing",
    "## Legal reports",
    "## Pitfalls",
    "## Sources",
)
#: The files every localization has next to its SKILL.md.
LOCALIZATION_FILES = ("SKILL.md", "versions.md", "MAINTAINERS.md")
