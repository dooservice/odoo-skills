#!/usr/bin/env bash
# Installs the odoo-skills of one Odoo version for your coding agents, through `npx skills`.
#
#   curl -fsSL https://raw.githubusercontent.com/dooservice/odoo-skills/main/install.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/dooservice/odoo-skills/main/install.sh | bash -s 17.0
#
# Without a version, it is read from the first __manifest__.py under the current directory
# (a module version such as 18.0.1.0.0 means Odoo 18.0). Extra arguments go to `npx skills
# add`, e.g. `-g` to install for your user instead of this project, or `-a codex`.
set -euo pipefail

REPO=dooservice/odoo-skills
SUPPORTED="16.0 17.0 18.0 19.0 20.0"

version="${1:-}"
[[ "$version" == -* ]] && version=""
[[ -n "$version" ]] && shift

if [[ -z "$version" ]]; then
  manifest=$(find . -name __manifest__.py -not -path "*/node_modules/*" -print -quit)
  if [[ -n "$manifest" ]]; then
    version=$(python3 -c 'import ast, sys; v = ast.literal_eval(open(sys.argv[1]).read()).get("version", ""); print(".".join(v.split(".")[:2]) if v.count(".") >= 4 else "")' "$manifest")
  fi
fi

if [[ " $SUPPORTED " != *" $version "* ]]; then
  echo "Which Odoo version? Pass one of: $SUPPORTED (found: '${version:-nothing}')." >&2
  exit 1
fi
command -v npx >/dev/null || { echo "npx (Node.js) is needed; or copy the folders by hand, see the README." >&2; exit 1; }

echo "Installing the skills for Odoo $version"
npx -y skills@1 add "$REPO/odoo/$version" --yes "$@"
npx -y skills@1 add "$REPO/odoo/common" --yes "$@"
