A patch that survives its test changes every test after it, and the failure shows up in a
test that has nothing to do with it.

- Call `patch(target, { method() { ... } })` from `@web/core/utils/patch` inside the test:
  the test framework undoes every `patch` when the test ends. `patchWithCleanup` is a
  deprecated alias of it.
- Never assign to a prototype or to `browser` directly: only `patch` is undone.
