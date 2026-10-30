"""Builds `odoo/<version>/` guideline skills from Odoo's 20.0 skills, adapted per version."""

from __future__ import annotations

import shutil
from pathlib import Path

from .constants import SKILLS, VERSIONS
from .documents.actions import ActionRules
from .documents.api import Api
from .documents.assets import Assets
from .documents.authoring import GuidelinesAuthoring, WebAuthoring
from .documents.command_line import CommandLine
from .documents.comments import Comments
from .documents.controllers import Controllers
from .documents.external_api import ExternalApi
from .documents.fields import ComputedFields, Fields
from .documents.git_skill import GitSkill
from .documents.guidelines_skill import GuidelinesSkill
from .documents.installed import InstalledModules
from .documents.javascript import Javascript
from .documents.mail import Mail
from .documents.manifest import Manifest
from .documents.migrations import Migrations
from .documents.models import Models
from .documents.module_structure import ModuleStructure
from .documents.multi_company import MultiCompany
from .documents.orm import Orm, OrmAdvanced
from .documents.owl import Owl
from .documents.performance import Performance
from .documents.point_of_sale import PointOfSale
from .documents.python_rules import PythonRules
from .documents.registries import Registries, WebClientRegistries
from .documents.reports import Reports
from .documents.review_skill import ReviewSkill
from .documents.scss import Scss
from .documents.security_rules import AccessRights
from .documents.security_skill import SecuritySkill
from .documents.services import Services
from .documents.stable import StableVersion
from .documents.tests import Tests
from .documents.translations import Translations
from .documents.version_notes import VersionNotes
from .documents.view_rules import ViewRules
from .documents.views import Views
from .documents.web_skill import WebSkill
from .documents.web_tests import WebTests
from .documents.website import Website
from .documents.xml_rules import XmlRules
from .version import OdooVersion
from .writer import SkillWriter

DOCUMENTS = (
    GuidelinesSkill, GuidelinesAuthoring, VersionNotes, Comments, Controllers, ExternalApi, Mail,
    MultiCompany, Fields, ComputedFields, Manifest, ModuleStructure, Orm, OrmAdvanced, Api, Models, Performance, PythonRules,
    Reports, AccessRights, InstalledModules, StableVersion, Tests, Migrations, Translations,
    CommandLine, XmlRules, ViewRules, ActionRules, WebSkill, WebAuthoring, Javascript, Scss,
    Assets, Owl, Registries, WebClientRegistries, Services, Views, Website, PointOfSale, WebTests, ReviewSkill,
    SecuritySkill, GitSkill,
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
