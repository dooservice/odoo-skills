A component re-renders when reactive state it read changes, and only then. State is
created with `useState({ ... })`; a plain object assigned to `this` does not re-render
anything when it changes.

- Keep state in one `useState` object per component (`this.state`), and mutate it:
  `this.state.count++`. Replacing `this.state` itself is not tracked.
- State shared between components is a `reactive({ ... })` object created once (in a
  service), and each component that reads it wraps it with `useState(sharedState)`.
- `markRaw(object)` keeps a big object (a library instance) out of reactivity.
- Derived values are computed in a method that the template calls; do not store them
  in the state, where they go stale.
