"""What the reference builder reads and skips, and the shorthands it writes."""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
SKIPPED_PREFIXES = ("test_", "hw_", "theme_")

KINDS = {
    "Many2oneReference": "many2one_reference",
    "PropertiesDefinition": "properties_definition",
    "Image": "binary",
    "Id": "integer",
}

RELATIONAL = {"Many2one", "One2many", "Many2many"}
FLAGS = ("required", "readonly", "store", "index", "company_dependent")
HOOK_PREFIXES = ("_prepare_", "_get_", "_action_", "_create_", "_post_", "_check_")

SETTINGS_MODEL = "res.config.settings"

SHORTHANDS = {"menuitem": "ir.ui.menu", "template": "ir.ui.view"}
