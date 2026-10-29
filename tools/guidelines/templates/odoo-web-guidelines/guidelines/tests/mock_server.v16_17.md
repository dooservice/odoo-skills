A unit test never reaches a database: the mock server answers every RPC from the
`serverData` the test declares, which keeps the test fast and independent of installed
modules.

- Declare models in `serverData.models`: `{ "library.book": { fields: { name: { string:
  "Name", type: "char" } }, records: [{ id: 1, name: "Dune" }] } }`, and views in
  `serverData.views` keyed `"library.book,false,form"`.
- Mount a view with `makeView({ type: "form", resModel: "library.book", resId: 1,
  serverData, arch })`, after `setupViewRegistries()` in `beforeEach`.
- Intercept a call with `mockRPC(route, args, performRPC)`: return a value to answer it,
  return nothing to let the mock server answer, and call `assert.step(args.method)` to
  check that it happened.
