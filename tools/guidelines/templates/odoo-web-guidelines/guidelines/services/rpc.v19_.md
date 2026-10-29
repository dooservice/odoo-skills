`import { rpc } from "@web/core/network/rpc"`, then
`await rpc("/my_module/books", { limit: 10 })`. It is a plain function, not a service:
there is no `useService("rpc")`. The third argument takes `silent`, `headers` and
`cache`, and the returned promise has `abort()`. It calls a route of
`type='jsonrpc'`.