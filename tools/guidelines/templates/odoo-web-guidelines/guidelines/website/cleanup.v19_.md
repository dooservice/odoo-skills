An interaction is destroyed when the editor enters edit mode, when a part of the page is
re-rendered, and when it is restarted; anything it left behind then runs twice or
leaks. Use the helpers that undo themselves:

- `this.addListener(target, "scroll", handler)` for a listener outside the
  `dynamicContent` selectors, `this.insert(el)` for an element added to the page,
  `this.mountComponent(el, Component, props)` for an Owl component; all are removed on
  destroy.
- `this.waitFor(promise)` around every awaited call, and `this.protectSyncAfterAsync(fn)`
  for code that runs after one: they stop the code when the interaction was destroyed
  while waiting.
- `this.waitForTimeout(fn, delay)` and `this.waitForAnimationFrame(fn)` instead of
  `setTimeout` and `requestAnimationFrame`; `this.debounced(fn, delay)` and
  `this.throttled(fn)` for handlers.
- `this.registerCleanup(fn)` for anything else. `destroy()` is for the rare case left.
