"""Generates the odoo-reference skill of every version from `.odoo/src/<version>`."""

from pathlib import Path

from reference.build import ReferenceBuild

ROOT = Path(__file__).resolve().parent
VERSIONS = ("16.0", "17.0", "18.0", "19.0", "20.0")

build = ReferenceBuild(ROOT / ".odoo" / "src", ROOT)
for version in VERSIONS:
    print(version, build.build(version), "addons")
