Owl renders on the next animation frame, so an assertion written right after an event
reads the old DOM. Use the helpers, which dispatch the full sequence of real events.

- `@odoo/hoot-dom` acts on selectors: `await click(".o_field_widget input")`,
  `await edit("Dune")` on the focused input, `await press("Enter")`, `check`, `select`,
  `hover`; `queryAll`, `queryOne` and `waitFor` read the DOM.
- After an action, `await animationFrame()` (from `@odoo/hoot-mock`) lets Owl render;
  `contains(".o_field_widget input").click()` from the web helpers waits for the element
  before acting, which suits elements that appear late.
- Time is mocked: `advanceTime(ms)`, `runAllTimers()` and `mockDate("2024-01-01 10:00:00")`
  replace real waiting.
- Assert on what the user sees: `expect(".o_field_widget input").toHaveValue("Dune")`,
  `toHaveCount`, `toHaveClass`, `toBeVisible`. Component internals change between
  versions; the DOM contract changes less.
