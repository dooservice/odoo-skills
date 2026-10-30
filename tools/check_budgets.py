"""Checks every skill against the size budget of each layer.

Usage: python3 tools/check_budgets.py                 fail if a budget is exceeded
       python3 tools/check_budgets.py --duplicates    list long sentences repeated
                                                      across files of a skill (warning)
"""

import sys

from budgets.catalog import SkillCatalog
from budgets.duplicates import DuplicateFinder
from budgets.table import BudgetTable

catalog = SkillCatalog()
if "--duplicates" in sys.argv:
    for skill in catalog.skills():
        lines = DuplicateFinder(skill).render()
        if lines:
            print(f"\n{skill.folder.parent.name}/{skill.name}:")
            print("\n".join(lines))
    sys.exit(0)
table = BudgetTable(catalog.measures())
print(table.render())
if table.exceeded():
    sys.exit(f"\n{len(table.exceeded())} over budget")
print("\nbudgets ok")
