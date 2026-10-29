`static props` lists every prop with its type; Owl checks them in debug mode
(`?debug=1`) and reports a missing, unknown or mistyped prop at the call site.

```js
static props = {
    bookId: Number,
    title: { type: String, optional: true },
    tags: { type: Array, element: String },
    onLend: { type: Function, optional: true },
    slots: { type: Object, optional: true },
};
static defaultProps = { title: "" };
```

- Every optional prop that the code reads without a check has a `defaultProps` entry.
- A component that takes a slot declares `slots`.
- Spread the shared shapes instead of retyping them: `...standardFieldProps` and
  `...standardWidgetProps`.
- `static props = ["*"]` accepts anything; it is for wrappers that pass props through,
  never for a component that reads them.
