#!/usr/bin/env bash
# Installs the odoo-skills of one Odoo version for your coding agents, through `npx skills`.
#
#   curl -fsSL https://raw.githubusercontent.com/dooservice/odoo-skills/main/install.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/dooservice/odoo-skills/main/install.sh | bash -s 17.0
#
# Without a version, it is read from the project's __manifest__.py files (a module version
# such as 18.0.1.0.0 means Odoo 18.0). Extra arguments go to `npx skills add`, e.g. `-g` to
# install for your user instead of this project, or `-a codex` for one agent.
set -euo pipefail

REPOSITORY=dooservice/odoo-skills
SUPPORTED="16.0 17.0 18.0 19.0 20.0"

version="${1:-}"
[[ "$version" == -* ]] && version=""
[[ -n "$version" ]] && shift

detected=$(python3 - <<'PYTHON'
import ast
from pathlib import Path

manifests = sorted(path for path in Path(".").rglob("__manifest__.py") if "node_modules" not in path.parts)
versions = []
for manifest in manifests:
    content = ast.literal_eval(manifest.read_text(encoding="utf-8"))
    module_version = str(content.get("version", ""))
    if module_version.count(".") >= 4:
        versions.append(".".join(module_version.split(".")[:2]))
print(versions[0] if versions else "")
PYTHON
)
version="${version:-$detected}"

if [[ " $SUPPORTED " != *" $version "* ]]; then
  echo "Which Odoo version? Pass one of: $SUPPORTED (found: '${version:-nothing}')." >&2
  exit 1
fi
command -v npx >/dev/null || { echo "npx (Node.js) is needed; or copy the folders by hand, see the README." >&2; exit 1; }

echo "Installing the skills for Odoo $version"
npx -y skills@1 add "$REPOSITORY/odoo/$version" --yes "$@"
npx -y skills@1 add "$REPOSITORY/odoo/common" --yes "$@"

