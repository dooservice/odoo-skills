`import { rpc } from "@web/core/network/rpc"`, then
`await rpc("/my_module/books", { limit: 10 })`. It is a plain function, not a service:
there is no `useService("rpc")` in this version. The third argument takes `silent` and
`headers`, and the returned promise has `abort()`. It calls a route of
`type='json'`.