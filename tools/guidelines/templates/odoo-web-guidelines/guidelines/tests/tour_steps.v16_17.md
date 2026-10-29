A step waits until its `trigger` matches a visible element, then runs its `run`. A tour
that acts on an element before it is ready fails at random, so every step targets the
element the user would look at.

- `trigger` is a jQuery selector (`:contains("Dune")` is allowed); `extra_trigger` adds a
  second element that must be present, and `in_modal: true` restricts the search to the
  open dialog.
- `run` is a string action or a function: `"click"` (the default when `run` is absent,
  except on the last step), `"text Dune"` to type, `"drag_and_drop_native .o_target"`,
  or `run(actions) { ... }`.
- A step that only checks the page, without acting, says `run: () => {}`.
- `content` is the tooltip text; `position` places it. Both matter for onboarding tours
  only.
- `edition: "community"` or `mobile: true` limit a step to that edition or layout.
