A step waits until its `trigger` matches a visible element, then runs its `run`. A tour
that acts on an element before it is ready fails at random, so every step targets the
element the user would look at.

- `trigger` is a hoot selector (`:contains(Dune)`, `:iframe`, `:not(:visible)` are
  allowed); to wait for two elements, chain two steps. `extra_trigger` and `in_modal` no
  longer exist: put the dialog in the selector (`.modal .o_field_widget`).
- `run` is a string action or a function: `"click"`, `"edit Dune"`, `"fill Dune"`,
  `"press Enter"`, `"select 2"`, `"check"`, or several joined with `&&`
  (`"edit Dune && press Enter"`); `run(helpers) { ... }` gets the same helpers.
- A step without `run` only waits for its trigger: it no longer clicks by default, so a
  step written for an older version that relied on the implicit click needs
  `run: "click"`.
- `content` is the tooltip text and `tooltipPosition` places it; both matter for
  onboarding tours only.
- `isActive: ["community"]` (or `"enterprise"`, `"mobile"`, `"desktop"`, `"auto"`,
  `"manual"`) limits a step to that edition, layout or mode.
