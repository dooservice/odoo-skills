"""Measures what the skills cover of each Odoo version and writes `COVERAGE.md`.

Usage: python3 tools/build_coverage.py            write COVERAGE.md
       python3 tools/build_coverage.py --check    fail if any module or framework item is missing
"""

import sys

from coverage.build import CoverageBuild

sys.exit(CoverageBuild().run("--check" in sys.argv) or None)
