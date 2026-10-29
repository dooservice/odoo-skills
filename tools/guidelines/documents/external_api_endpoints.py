"""The endpoints section of `external_api.md`: XML-RPC and JSON-RPC, then JSON-2 from 19.0."""

from __future__ import annotations

from ..version import OdooVersion


class ExternalEndpoints:
    """How a client reaches a model method in each version, with a schematic call."""

    rpc = """\
- XML-RPC: `/xmlrpc/2/common` authenticates with
  `authenticate(db, login, api_key, {{}})`, which returns the user id (`False` when
  the credentials are wrong); `/xmlrpc/2/object` runs
  `execute_kw(db, uid, api_key, model, method, args, kwargs)`. The key is sent
  with every call.
- JSON-RPC: `POST /jsonrpc` with
  `{{"jsonrpc": "2.0", "method": "call", "params": {{"service": "object",
  "method": "execute_kw", "args": [db, uid, api_key, model, method, args, kwargs]}}}}`
  calls the same services.{db_service}

```python
import xmlrpc.client

common = xmlrpc.client.ServerProxy(f"{{url}}/xmlrpc/2/common")
uid = common.authenticate(db, login, api_key, {{}})
models = xmlrpc.client.ServerProxy(f"{{url}}/xmlrpc/2/object")
books = models.execute_kw(
    db, uid, api_key, "library.book", "search_read",
    [[("state", "=", "available")]],
    {{"fields": ["name", "author_id"], "limit": 80, "context": {{"lang": "en_US"}}}},
)
```"""

    json2 = """\
- JSON-2: `POST /json/2/<model>/<method>` with the headers
  `Authorization: bearer <api key>` and `X-Odoo-Database: <db>` (needed when the
  server hosts several databases) and a JSON body. The body holds `ids` (the
  records the method runs on), `context`, and every method argument **by
  name**: `search_read` takes `domain` and `fields`, `create` takes
  `vals_list`. The response body is the return value (recordsets become ids);
  errors come back as JSON with a 4xx/5xx status. Sending `ids` to an
  `@api.model` method is refused with 422.
- The `/doc` page (module `api_doc`, for users in its access group) lists the
  models, fields and methods the current database exposes.
- `/xmlrpc/2/common`, `/xmlrpc/2/object` and `/jsonrpc` still answer, served by
  the auto-installed `rpc` module, but they are deprecated: each call logs a
  warning and they are scheduled for removal in Odoo 22. Write new clients
  against JSON-2 and migrate old ones.{db_service}

```python
import requests

response = requests.post(
    f"{{url}}/json/2/library.book/search_read",
    headers={{"Authorization": f"bearer {{api_key}}", "X-Odoo-Database": db}},
    json={{
        "domain": [["state", "=", "available"]],
        "fields": ["name", "author_id"],
        "limit": 80,
        "context": {{"lang": "en_US"}},
    }},
    timeout=30,
)
response.raise_for_status()
books = response.json()
```"""

    def values(self, version: OdooVersion) -> dict[str, str]:
        db_service = version.pick(
            v16_19="\n- The `db` service (`/xmlrpc/2/db`) creates, duplicates and drops databases\n"
            "  behind the master password; integrations never need it.",
            v20="\n- There is no `db` service any more: databases are managed from the\n"
            "  database manager or the command line, never over RPC.",
        )
        return {
            "external_api_name": version.pick(v16_18="XML-RPC or JSON-RPC", v19_="the JSON-2 API"),
            "endpoints": version.pick(
                v16_18=self.rpc.format(db_service=db_service),
                v19_=self.json2.format(db_service=db_service),
            ),
        }
