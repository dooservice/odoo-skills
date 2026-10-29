A patch that survives its test changes every test after it, and the failure shows up in a
test that has nothing to do with it.

- Patch through `patchWithCleanup(target, { method() { ... } })` (from
  `@web/../tests/helpers/utils`); it is undone when the test ends.
- Never call `patch` from `@web/core/utils/patch` in a test, nor assign to a prototype
  or to `browser` directly.
