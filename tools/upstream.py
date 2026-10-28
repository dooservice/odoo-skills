"""Says whether Odoo's skills changed since the guidelines were generated.

Usage: python3 tools/upstream.py <odoo 20.0 clone> [<ref>]            list what changed
       python3 tools/upstream.py <odoo 20.0 clone> [<ref>] --record   record <ref> as the source

<ref> defaults to FETCH_HEAD: run `git fetch origin 20.0` in the clone first. Record the
ref the guidelines were just generated from, and commit `tools/guidelines/UPSTREAM`.
"""

import sys
from pathlib import Path

from guidelines.upstream import UpstreamClone, UpstreamRecord

arguments = [argument for argument in sys.argv[1:] if argument != "--record"]
clone = UpstreamClone(Path(arguments[0]), arguments[1] if len(arguments) > 1 else "FETCH_HEAD")
record = UpstreamRecord()
if "--record" in sys.argv:
    record.write(clone)
print(record.report(clone))
