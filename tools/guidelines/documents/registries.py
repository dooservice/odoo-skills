"""`odoo-web-guidelines/guidelines/registries*.md`: the registry API and every category of the web client."""

from __future__ import annotations

from .spanned import SpannedDocument


class Registries(SpannedDocument):
    """The registry API, the key prefix, and the categories of views, data and the frontend."""

    path = "odoo-web-guidelines/guidelines/registries.md"


class WebClientRegistries(SpannedDocument):
    """The categories of the web client's shell: navbar, actions, palette, debug, errors, effects."""

    path = "odoo-web-guidelines/guidelines/registries_webclient.md"
