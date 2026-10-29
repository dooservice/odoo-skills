"""The `auth=` values of `controllers.md`: which exist, and how an API key authenticates a route."""

from __future__ import annotations

from ..version import OdooVersion


class RouteAuth:
    """`auth='bearer'` came in 18.0; 20.0 ties each bearer route to a key scope."""

    no_bearer = """
- There is no bearer authentication in this version. A machine endpoint is
  `auth='public'` with `csrf=False` and `save_session=False`: it reads the key from
  the `Authorization` header, resolves it with
  `request.env['res.users.apikeys']._check_credentials(scope='rpc', key=key)`,
  raises `werkzeug.exceptions.Unauthorized` when that returns nothing, and calls
  `request.update_env(user=uid)` before any ORM call."""

    bearer = """
- `auth='bearer'`: the client sends `Authorization: Bearer <api key>` and the
  request runs as the key's user. Without the header, only a browser navigation
  carrying a session is accepted (checked through its `Sec-Fetch-*` headers);
  anything else gets 401. {scope}
  A `type='http'` bearer route that accepts `POST` also needs `csrf=False`."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "auth_modes": version.pick(
                v16_17="`user`, `public`, or `none`",
                v18_="`user`, `bearer`, `public`, or `none`",
            ),
            "bearer": version.pick(
                v16_17=self.no_bearer,
                v18_=self.bearer.format(scope=self.scope(version)),
            ),
            "save_session_default": version.pick(
                v16_18="",
                v19_="\n  `auth='bearer'` routes default to it.",
            ),
        }

    @staticmethod
    def scope(version: OdooVersion) -> str:
        return version.pick(
            v16_17="",
            v18="Keys of scope `rpc` and keys\n  without scope are accepted. Set `save_session=False` yourself: this\n"
            "  version does not default it for bearer routes.",
            v19="Keys of scope `rpc` and keys\n  without scope are accepted.",
            v20="The route must set\n  `bearer_scope='rpc'` or another scope (the import fails without it, and\n"
            "  it means nothing on other auth values): only keys created with that\n"
            "  exact scope authenticate.",
        )
