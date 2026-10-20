"""Builds `odoo/<version>/` guideline skills from Odoo's 20.0 skills, adapted per version."""

from __future__ import annotations

import shutil
from pathlib import Path

from .constants import SKILLS, VERSIONS
from .documents.assets import Assets
from .documents.comments import Comments
from .documents.controllers import Controllers
from .documents.fields import Fields
from .documents.git_skill import GitSkill
from .documents.guidelines_skill import GuidelinesSkill
from .documents.installed import InstalledModules
from .documents.javascript import Javascript
from .documents.manifest import Manifest
from .documents.module_structure import ModuleStructure
from .documents.orm import Orm
from .documents.performance import Performance
from .documents.python_rules import PythonRules
from .documents.reports import Reports
from .documents.review_skill import ReviewSkill
from .documents.scss import Scss
from .documents.security_rules import AccessRights
from .documents.security_skill import SecuritySkill
from .documents.tests import Tests
from .documents.version_notes import VersionNotes
from .documents.web_skill import WebSkill
from .documents.xml_rules import XmlRules
from .version import OdooVersion
from .writer import SkillWriter

DOCUMENTS = (
    GuidelinesSkill, VersionNotes, Comments, Controllers, Fields, Manifest, ModuleStructure, Orm,
    Performance, PythonRules, Reports, AccessRights, InstalledModules, Tests, XmlRules,
    WebSkill, Javascript, Scss, Assets, ReviewSkill, SecuritySkill, GitSkill,
)


class GuidelinesBuild:
    def __init__(self, upstream: Path, repository: Path) -> None:
        self.documents = [document(upstream) for document in DOCUMENTS]
        self.repository = repository

    def build_all(self) -> None:
        for number in VERSIONS:
            self.build(OdooVersion(number))

    def build(self, version: OdooVersion) -> None:
        root = self.repository / "odoo" / version.name
        for skill in SKILLS:
            shutil.rmtree(root / skill, ignore_errors=True)
        writer = SkillWriter(root)
        for document in self.documents:
            writer.write(document.path, document.render(version))
