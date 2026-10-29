A component re-renders when reactive values it read change, and only then. Owl 3 has
two kinds:

- `proxy({ ... })` makes a deep reactive object, the replacement of `useState` and
  `reactive`: `this.state = proxy({ count: 0 })`, then `this.state.count++`.
- `signal(value)` holds one value, read by calling it and written with `set`:
  `count = signal(0)`, `this.count()`, `this.count.set(1)`. `signal.Array`,
  `signal.Map`, `signal.Object` and `signal.Set` hold collections.
- `computed(() => ...)` derives a value from signals and proxies and recomputes only
  when one of them changes: `total = computed(() => this.lines().length)`, read as
  `this.total()`. Prefer it to a getter for derived state.
- `markRaw(object)` keeps a big object (a library instance) out of reactivity, and
  `untrack(fn)` reads without subscribing.
- In a template, `t-model.proxy="this.state.value"` binds an input to a proxy field;
  `t-model` takes a signal.
