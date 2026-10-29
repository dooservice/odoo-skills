A unit test never reaches a database: the mock server answers every RPC from the models
the test declares, which keeps the test fast and independent of installed modules.

- Declare a model as a class: `class LibraryBook extends models.Model { _name =
  "library.book"; name = fields.Char(); _records = [{ id: 1, name: "Dune" }]; }`, then
  `defineModels([LibraryBook])` at the top of the file. `_views` holds the archs by type.
  Models of other modules come with their helpers (`defineMailModels()` from
  `@mail/../tests/mail_test_helpers`).
- Mount a view with `await mountView({ type: "form", resModel: "library.book", resId: 1,
  arch })`, a component with `await mountWithCleanup(MyComponent, { props })`, and the
  whole client with `mountWebClient()`.
- Intercept a call with `onRpc("library.book", "action_lend", ({ args }) => ...)`, or a
  route with `onRpc("/my_module/data", async (request) => ...)`: return a value to answer
  it, nothing to let the mock server answer; record it with `expect.step`.
- `serverState` sets the user, company and language the client sees
  (`serverState.userId`, `serverState.lang`); `defineParams` sets session parameters.
