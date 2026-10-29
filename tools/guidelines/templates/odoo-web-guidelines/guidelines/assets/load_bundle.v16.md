`await loadBundle(await getBundle("my_module.assets_heavy"))` (both from
  `@web/core/assets`) loads it: `getBundle` returns the description of the files, and
  `loadBundle` takes that description, not the name.