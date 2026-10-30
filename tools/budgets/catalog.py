"""Every skill of every version folder and of the common folder."""

from __future__ import annotations

from .constants import SKILL_FILE, SKILLS_FOLDER
from .measure import Measure
from .skill import Skill


class SkillCatalog:
    """The skills found under `odoo/<version>/` and `odoo/common/`."""

    def skills(self) -> list[Skill]:
        folders = sorted(path.parent for path in SKILLS_FOLDER.glob(f"*/*/{SKILL_FILE}"))
        return [Skill(folder) for folder in folders]

    def measures(self) -> list[Measure]:
        return [measure for skill in self.skills() for measure in skill.measures()]
