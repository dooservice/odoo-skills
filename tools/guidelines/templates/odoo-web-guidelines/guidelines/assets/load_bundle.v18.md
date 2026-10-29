`await loadBundle("my_module.assets_heavy")` (from `@web/core/assets`) loads it, once;
  later calls return at once. It takes the bundle name only.