"""Writes `.claude-plugin/marketplace.json` from the folders, after checking every localization.

Usage: python3 tools/build_catalog.py            write it
       python3 tools/build_catalog.py --check    fail if a localization is incomplete or the file is stale
"""

import sys

from catalog.localization import Localization
from catalog.marketplace import Marketplace

problems = [problem for localization in Localization.all() for problem in localization.problems()]
marketplace = Marketplace()
if "--check" in sys.argv and not marketplace.is_current():
    problems.append("marketplace.json is stale: run python3 tools/build_catalog.py and commit it")
if problems:
    sys.exit("\n".join(problems))
if "--check" not in sys.argv:
    marketplace.write()
print("catalog ok:", len(marketplace.versions()), "versions,", len(Localization.all()), "localizations")
