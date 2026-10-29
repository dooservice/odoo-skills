Owl renders on the next animation frame, so an assertion written right after an event
reads the old DOM. Use the helpers, which dispatch real events and wait for the render.

- `await click(target, ".o_field_widget input")`, `await editInput(target, "input", "Dune")`
  and `await triggerEvent(target, "input", "keydown", { key: "Enter" })` act and wait;
  `target` is `getFixture()`.
- After a change made outside a helper (a resolved promise, a patched service), add
  `await nextTick()` before asserting.
- Assert on what the user sees (`.o_field_widget`, text, classes), not on component
  internals: internals change between versions, the DOM contract changes less.
