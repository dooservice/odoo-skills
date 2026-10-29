`const rpc = useService("rpc")`, then `await rpc("/my_module/books", { limit: 10 })`;
the third argument takes `silent` (no loading indicator) and `headers`. The `rpc`
service sends a JSON-RPC request to a route of `type='json'`.