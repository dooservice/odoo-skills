- A ref is a signal: `input = signal.ref()` in the class, `t-ref="this.input"` in the
  template, and `this.input()` returns the element, or `null` until mounted. Read it in
  `onMounted`, an effect or an event handler, never in `setup`.
- A listener outside the component's own element (on `window`, `document`, `body`) is
  added with `useListener(window, "resize", this.onResize)`, which removes it when the
  component is destroyed. A raw `addEventListener` leaks.
- Odoo's `useBus(bus, "EVENT", callback)` does the same for an event bus.
- Never query the document (`document.querySelector`) for an element of a component:
  another instance or another component may match.
