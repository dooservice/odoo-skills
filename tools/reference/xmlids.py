"""What an addon's data files declare under an XML id: views, actions, menus, groups, data.

Read from the files the manifest loads on install, demo left out, so `env.ref()` and view
inheritance can be written without searching.
"""

from __future__ import annotations

from dataclasses import dataclass
from xml.etree import ElementTree

from .constants import SHORTHANDS
from .manifests import Addon


@dataclass(frozen=True)
class XmlId:
    xmlid: str
    model: str
    detail: str


class XmlIdScanner:
    def scan(self, addon: Addon) -> list[XmlId]:
        found = []
        for path in addon.data_files:
            try:
                root = ElementTree.parse(path).getroot()
            except (ElementTree.ParseError, OSError):
                continue
            for element in self.top_level(root):
                if (declared := self.declared(addon.name, element)) is not None:
                    found.append(declared)
        return found

    @staticmethod
    def top_level(root: ElementTree.Element) -> list[ElementTree.Element]:
        """What the file itself declares: children of `<odoo>` and of its `<data>` blocks,
        never what sits inside a view's architecture."""
        found = []
        for child in root:
            found += list(child) if child.tag == "data" else [child]
        return found

    @staticmethod
    def declared(addon: str, element: ElementTree.Element) -> XmlId | None:
        identifier = element.get("id")
        model = element.get("model") if element.tag == "record" else SHORTHANDS.get(element.tag)
        if not identifier or not model:
            return None
        xmlid = identifier if "." in identifier else f"{addon}.{identifier}"
        detail = element.get("name") or ""
        if model == "ir.ui.view":
            inherited = element.find("field[@name='inherit_id']")
            target = element.find("field[@name='model']")
            detail = " ".join(part for part in (
                f"on {target.text}" if target is not None and target.text else "",
                f"inherits {inherited.get('ref')}" if inherited is not None and inherited.get("ref") else "",
                f"inherits {element.get('inherit_id')}" if element.get("inherit_id") else "",
            ) if part)
        return XmlId(xmlid, model, detail)
