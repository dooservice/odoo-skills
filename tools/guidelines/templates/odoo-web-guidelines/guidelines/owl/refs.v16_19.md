- `t-ref="input"` in the template and `this.input = useRef("input")` in `setup` give
  `this.input.el`, which is `null` until mounted; read it in `onMounted`, an effect or
  an event handler, never in `setup`.
- A listener outside the component's own element (on `window`, `document`, `body`) is
  added with `useExternalListener(window, "resize", this.onResize)`, which removes it
  when the component is destroyed. A raw `addEventListener` leaks.
- Odoo's `useBus(bus, "EVENT", callback)` does the same for an event bus.
- Never query the document (`document.querySelector`) for an element of a component:
  another instance or another component may match.
