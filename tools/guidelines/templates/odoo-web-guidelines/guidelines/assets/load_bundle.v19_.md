`await loadBundle("my_module.assets_heavy")` (from `@web/core/assets`) loads it, once;
  later calls return at once. Options `{ css: false }` or `{ js: false }` load half of
  it, and `targetDoc` loads it into an iframe.