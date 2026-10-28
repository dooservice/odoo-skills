"""Writes `.claude-plugin/marketplace.json` from the folders.

Usage: python3 tools/build_catalog.py            write it
       python3 tools/build_catalog.py --check    fail if the file is stale
"""

import sys

from catalog.marketplace import Marketplace

marketplace = Marketplace()
if "--check" in sys.argv and not marketplace.is_current():
    sys.exit("marketplace.json is stale: run python3 tools/build_catalog.py and commit it")
if "--check" not in sys.argv:
    marketplace.write()
print("catalog ok:", len(marketplace.versions()), "versions")
