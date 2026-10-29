Props are declared with `useProps` in a field initializer, with `t` types and the
default inside `.optional(value)`. A `static props` or `static defaultProps` throws in
this version: Owl 3 ignores them, and the compatibility layer refuses them so they are
not left behind silently.

```js
props = useProps({
    bookId: t.number(),
    title: t.string().optional(""),
    tags: t.array(t.string()).optional([]),
    onLend: t.function().optional(),
});
```

- Types are `t.string()`, `t.number()`, `t.boolean()`, `t.object()`, `t.array(type)`,
  `t.function()`, `t.or([...])`, `t.literal(value)`, `t.instanceOf(Class)`,
  `t.component()`, `t.signal()`, `t.any()`.
- The schema is checked in debug mode (`?debug=1`), and again when props
  change.
- Spread the shared shapes, which are `t` schemas too: `...standardFieldProps`,
  `...standardWidgetProps`.
- `useProps()` without a schema accepts anything; it is for wrappers that pass props
  through, never for a component that reads them.
- `this.props` is reactive: a value read from it in a `computed` or an effect is
  tracked.
