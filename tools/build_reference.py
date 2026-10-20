"""Generates the odoo-reference skill of every version from `.odoo/src/<version>`."""

from pathlib import Path

from reference.build import ReferenceBuild
from reference.constants import VERSIONS

REPOSITORY = Path(__file__).resolve().parent.parent

build = ReferenceBuild(REPOSITORY / ".odoo" / "src", REPOSITORY)
for version in VERSIONS:
    print(version, build.build(version), "addons")
