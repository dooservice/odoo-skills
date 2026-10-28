"""The two inventories of a version: its modules, and the framework items its guidelines name."""

from __future__ import annotations

from pathlib import Path

from reference.manifests import Addon

from .client import TestTools, WebRegistries
from .constants import COVERED, MISSING, TECHNICAL
from .declared import RecipeMap, TechnicalList
from .guidelines import GuidelineText
from .orm import ApiDecorators, FieldTypes, OrmMethods
from .results import ItemsCoverage, ModuleCoverage
from .server import ActionTypes, AuthValues, RouteTypes, ViewTypes


class FunctionalInventory:
    """Covered when a recipe declares the module, technical when the technical list does."""

    def __init__(self, recipes: RecipeMap, technical: TechnicalList) -> None:
        self.recipes = recipes
        self.technical = technical

    def classify(self, addons: list[Addon]) -> list[ModuleCoverage]:
        return [self.status(addon) for addon in addons]

    def status(self, addon: Addon) -> ModuleCoverage:
        if recipes := self.recipes.recipes_of(addon.name):
            return ModuleCoverage(addon, COVERED, ", ".join(recipes))
        if reason := self.technical.reason_of(addon.name):
            return ModuleCoverage(addon, TECHNICAL, reason)
        return ModuleCoverage(addon, MISSING, "")


class DevelopmentInventory:
    """Each framework category's items, split by whether the guidelines name them."""

    def __init__(self) -> None:
        self.categories = [
            FieldTypes(),
            ApiDecorators(),
            ViewTypes(),
            ActionTypes(),
            RouteTypes(),
            AuthValues(),
            OrmMethods(),
            WebRegistries(),
            TestTools(),
        ]

    def measure(self, source: Path, text: GuidelineText) -> list[ItemsCoverage]:
        found = []
        for category in self.categories:
            items = category.items(source)
            covered = [name for name in items if category.covered(name, text)]
            found.append(ItemsCoverage(category.title, covered, [name for name in items if name not in covered]))
        return found
