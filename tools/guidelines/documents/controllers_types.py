"""The route types of `controllers.md` and the route arguments that came with later versions."""

from __future__ import annotations

from ..version import OdooVersion


class RouteTypes:
    """`type=` values per version, and the `readonly`, `max_content_length` and `captcha` arguments."""

    http = """\
- `type='http'`: parameters come from the query string and the form body; the
  method returns a page, a file or a redirect, and errors render as HTML pages."""

    jsonrpc = """\
- `type='{name}'`: JSON-RPC 2.0, the protocol of the web client. The body is
  `{{"jsonrpc": "2.0", "method": "call", "params": {{...}}}}`, the keys of `params`
  become the method arguments and the return value comes back in `result`.
  Errors come back in `error` with HTTP status 200: a client tests `error`, not
  the status."""

    json2 = """\
- `type='json'` is a deprecated alias of `'jsonrpc'` that warns at import:
  write `'jsonrpc'`.
- `type='json2'`: the body is a plain JSON object whose keys, merged with the
  path parameters, become the method arguments; the return value is the
  response body as is. Errors are JSON with the exception's HTTP status
  (`UserError` 422, `AccessError` 403, `MissingError` 404). The body must be
  `application/json` or empty."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "route_types": version.pick(
                v16_18=f"{self.http}\n{self.jsonrpc.format(name='json')}",
                v19_=f"{self.http}\n{self.jsonrpc.format(name='jsonrpc')}\n{self.json2}",
            ),
            "machine_type": version.pick(
                v16_17="`type='http'` routes that answer with `request.make_json_response(...)`",
                v18="`type='http'` routes with `auth='bearer'` that answer with\n"
                "`request.make_json_response(...)`",
                v19_="`type='json2'` routes with `auth='bearer'`",
            ),
            "readonly_argument": version.pick(
                v16_17="",
                v18_="\n- `readonly=True` runs the route on a read-only cursor (the replica when\n"
                "  `--db_replica_host` is set). A write there fails and the whole request is\n"
                "  replayed on a read/write cursor, so mark only routes that never write.\n"
                f"  {self.readonly_function(version)}\n"
                "  `auth='none'` routes are read-only unless they set `readonly=False`.",
            ),
            "max_content_length": version.pick(
                v16="",
                v17="\n- `max_content_length=<bytes>` raises the 128 MiB request size limit for an\n"
                "  upload route; set it only where large files are expected.",
                v18_="\n- `max_content_length=<bytes>` (or a function of the controller) raises the\n"
                "  128 MiB request size limit for an upload route; set it only where large\n"
                "  files are expected.",
            ),
            "captcha": version.pick(
                v16_18="\n- A public form that creates records verifies its captcha in the method with\n"
                "  `request.env['ir.http']._verify_request_recaptcha_token('action_name')`,\n"
                "  which does nothing until a captcha module is installed.",
                v19_="\n- `captcha='action_name'` verifies the captcha token of every non-safe\n"
                "  request before the method runs (a no-op until a captcha module is\n"
                "  installed); put it on public forms that create records.",
            ),
        }

    @staticmethod
    def readonly_function(version: OdooVersion) -> str:
        return version.pick(
            v16_17="",
            v18="`readonly` may also be a function `(controller)` that decides per request.",
            v19_="`readonly` may also be a function `(controller, rule, args)` that decides\n"
            "  per request.",
        )
