# Owl in 20.0

Components are Owl 3 classes, imported from `@odoo/owl`. Owl 3 builds reactivity on
signals and replaces services with plugins; a compatibility layer (`@web/owl2/utils`)
keeps some Owl 2 code running while it is ported, never for new code.

```js
import { Component, onWillStart, proxy, t, useProps } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class BookCard extends Component {
    static template = "my_module.BookCard";
    static components = { Rating };
    props = useProps({ bookId: t.number(), onLend: t.function().optional() });

    setup() {
        this.orm = useService("orm");
        this.state = proxy({ book: null });
        onWillStart(async () => {
            [this.state.book] = await this.orm.read("library.book", [this.props.bookId], ["name"]);
        });
    }
}
```

- Hooks are called in `setup()` or in field initializers (`props = useProps(...)`);
  never write a `constructor`.
- Owl 3 exports, besides `Component`: `proxy`, `signal`, `computed`, `effect`,
  `useEffect`, `useListener`, `useProps`, `t` (types), `Plugin`, `usePlugin`,
  `useScope`, `onWillStart`, `onMounted`, `onWillUpdateProps`, `onPatched`,
  `onWillUnmount`, `onWillDestroy`, `markup`, `xml`, `EventBus`.
- `useState`, `useRef`, `reactive`, `useExternalListener`, `useChildSubEnv` and
  `useComponent` no longer exist; `this.env.debug` and `this.env.isSmall` throw (use
  `usePlugin(DebugModePlugin)` and the `ui` service's `isSmall`).

# Declare every prop the component takes

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

# Keep component state reactive

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

# Name templates `<module>.<Component>` and keep them in XML files

- The template lives in an `.xml` file next to the component, in the same bundle, as
  `<t t-name="my_module.BookCard">`; the component points at it with
  `static template = "my_module.BookCard"`. An inline `xml` template is for tests and
  tiny internal components only: it cannot be inherited.
- Template expressions reach the component through `this`: `this.props.title`,
  `this.state.count`, `t-on-click="this.onLend"`; a bare `props.title` is not the
  component's prop. `t-on-click="() => this.lend(book)"` passes an argument.
- Escape by default: `t-out` escapes strings and renders a `markup` value as HTML.
  `t-esc` is deprecated (Owl 3 warns) and `t-raw` does not exist.
- Loops need a key: `t-foreach="books" t-as="book" t-key="book.id"`; an index as key
  breaks when the list is reordered.
- Child components are listed in `static components = { BookCard }` and used as
  `<BookCard book="book"/>`; props are expressions, so a string literal is quoted
  twice (`title="'Books'"`).

# Extend a template with `t-inherit`, never by copying it

```xml
<t t-name="my_module.BookCard" t-inherit="other_module.BookCard" t-inherit-mode="extension">
    <xpath expr="//div[hasclass('o_book_card_footer')]" position="inside">
        <button class="btn btn-secondary" t-on-click="this.onClickLendAll">Lend all</button>
    </xpath>
</t>
```

- `t-inherit-mode="extension"` changes the original template in place, for every
  component that uses it; `t-inherit-mode="primary"` makes a new template, named by the
  `t-name`, for a subclass that sets `static template` to it.
- The `xpath` targets classes (`hasclass(...)`) or `t-name`d nodes, never positions such as
  `div[3]`, which break when the original template changes.
- The parent template must be in the same bundle or a bundle loaded before.

# Load data in `onWillStart`, not in `setup`

`setup()` is synchronous and runs once, before the first render. Data the first render
needs is loaded in `onWillStart(async () => { ... })`: the component is not rendered
until the promise resolves, so the template never sees a half-loaded state. Data that
depends on props is reloaded in `onWillUpdateProps(async (nextProps) => { ... })`, which
receives the new props before they are applied.

- `onMounted` runs once the element is in the DOM: measure, focus, or start a
  third-party library there.
- `onWillUnmount` and `onWillDestroy` undo what `onMounted` and `setup` started (a
  timer, a listener on `window`, a library instance).
- `useEffect(() => { ... })` runs again whenever a signal or proxy value it read
  changes, with no dependency list; it is the place for work that follows state. The
  Owl 2 form with a dependency list is `useLayoutEffect(fn, () => [deps])` from
  `@web/owl2/utils`, kept only for code not ported yet.
- `onPatched` runs after each re-render; prefer an effect that states what it depends
  on.
- Never call a hook (`useService`, `onMounted`, ...) outside `setup` or a field
  initializer: hooks bind to the component being built.

# Reach the DOM through a ref, and listen outside it through a hook

- A ref is a signal: `input = signal.ref()` in the class, `t-ref="this.input"` in the
  template, and `this.input()` returns the element, or `null` until mounted. Read it in
  `onMounted`, an effect or an event handler, never in `setup`.
- A listener outside the component's own element (on `window`, `document`, `body`) is
  added with `useListener(window, "resize", this.onResize)`, which removes it when the
  component is destroyed. A raw `addEventListener` leaks.
- Odoo's `useBus(bus, "EVENT", callback)` does the same for an event bus.
- Never query the document (`document.querySelector`) for an element of a component:
  another instance or another component may match.

# Pass shared values through props or the environment

- Data goes down through props, and events go up through a callback
  prop (`onLend.bind="this.onLend"`, where `.bind` keeps `this`); a child never reaches into its parent.
- Owl 3 has no sub-environment: a context a whole subtree needs is a plugin provided
  to that subtree (`providePlugins`), read with `usePlugin`. `useSubEnv` of
  `@web/owl2/utils` remains for code not ported yet.
- A value many unrelated components need (the current user, a service) comes from
  a plugin through `usePlugin`, or a service not ported yet through `useService`, not from a prop passed through every level.
