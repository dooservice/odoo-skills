"""Generates the guideline skills of every version from Odoo's 20.0 skills.

Usage: python3 tools/build_guidelines.py <odoo 20.0 skills directory> <this repository>
"""

import sys
from pathlib import Path

from guidelines.build import GuidelinesBuild

GuidelinesBuild(Path(sys.argv[1]), Path(sys.argv[2])).build_all()
