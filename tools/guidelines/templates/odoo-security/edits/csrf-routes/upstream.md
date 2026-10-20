  keep CSRF on (never `csrf=False`, except dedicated webhooks);
  `jsonrpc`/`json2` routes have no token check by design, their protection is
  the JSON content type.
