A widget is destroyed when the editor enters edit mode, when a part of the page is
re-rendered, and when it is restarted; anything it left behind (a listener on
`window`, an interval, an element appended to `body`) then runs twice or leaks.

- Bind handlers through `events`, which are unbound for you; a listener on `window` or
  `document` is added in `start` and removed in `destroy`.
- Clear intervals and timeouts in `destroy`, and remove elements the widget inserted
  outside its own element.
- `destroy` calls `this._super(...arguments)`.
- Code that must not run while the page is edited checks
  `this.options.editableMode`, which the website editor sets when it starts the
  widget, and returns early.
