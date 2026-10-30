Key names in 17.0:

- Owl 2 from `@odoo/owl`; hooks in `setup()`; services in `this.env.services`.
- Props: `static props` with types, `static defaultProps`; `...standardActionServiceProps` in a client action.
- State: `useState`, shared `reactive`, `markRaw`.
- Templates: expressions read the component directly (`props.title`); `t-esc` or `t-out`, no `t-raw`.
- Effects and DOM: `useEffect` with a dependency list, `useRef` with `t-ref`, `useExternalListener`.
- Context: `useSubEnv`, `useChildSubEnv`.

Sections of this file:

- Owl in 17.0
- Declare every prop the component takes
- Keep component state reactive
- Name templates `<module>.<Component>` and keep them in XML files
- Extend a template with `t-inherit`, never by copying it
- Load data in `onWillStart`, not in `setup`
- Reach the DOM through a ref, and listen outside it through a hook
- Pass shared values through props or the environment

# Owl in 17.0

Components are Owl 2 classes, imported from `@odoo/owl`:

```js
/** @odoo-module **/
import { Component, onWillStart, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class BookCard extends Component {
    static template = "my_module.BookCard";
    static components = { Rating };
    static props = { bookId: Number, onLend: { type: Function, optional: true } };

    setup() {
        this.orm = useService("orm");
        this.state = useState({ book: null });
        onWillStart(async () => {
            [this.state.book] = await this.orm.read("library.book", [this.props.bookId], ["name"]);
        });
    }
}
```

- `setup()` is where hooks are called; never write a `constructor`.
- Import Owl from `@odoo/owl` and Odoo's hooks from `@web/core/utils/hooks`
  (`useService`, `useBus`, `useAutofocus`, `useOwnedDialogs`).
- The environment is `this.env` (services in `this.env.services`), shared by every
  component of the application.

# Declare every prop the component takes

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
- Spread the shared shapes instead of retyping them: `...standardFieldProps`,
  `...standardWidgetProps`, and in a client action
  `...standardActionServiceProps`.
- `static props = ["*"]` accepts anything; it is for wrappers that pass props through,
  never for a component that reads them.

# Keep component state reactive

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

# Name templates `<module>.<Component>` and keep them in XML files

- The template lives in an `.xml` file next to the component, in the same bundle, as
  `<t t-name="my_module.BookCard">`; the component points at it with
  `static template = "my_module.BookCard"`. An inline `xml` template is for tests and
  tiny internal components only: it cannot be inherited.
- Template expressions read the component directly: `props.title`, `state.count`,
  `t-on-click="onLend"`; `t-on-click="() => this.lend(book)"` passes an argument.
- Escape by default: `t-esc` and `t-out` escape strings, and `t-out` renders a `markup`
  value as HTML. Never `t-raw`: Owl does not have it.
- Loops need a key: `t-foreach="books" t-as="book" t-key="book.id"`; an index as key
  breaks when the list is reordered.
- Child components are listed in `static components = { BookCard }` and used as
  `<BookCard book="book"/>`; props are expressions, so a string literal is quoted
  twice (`title="'Books'"`).

# Extend a template with `t-inherit`, never by copying it

```xml
<t t-name="my_module.BookCard" t-inherit="other_module.BookCard" t-inherit-mode="extension">
    <xpath expr="//div[hasclass('o_book_card_footer')]" position="inside">
        <button class="btn btn-secondary" t-on-click="onClickLendAll">Lend all</button>
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
- `useEffect(() => { ...; return cleanup; }, () => [this.state.bookId])` runs after
  render when one of the listed dependencies changed, and runs the cleanup first; it is
  the place for DOM work that depends on state.
- `onPatched` runs after each re-render; prefer an effect that states what it depends
  on.
- Never call a hook (`useService`, `onMounted`, ...) outside `setup` or a field
  initializer: hooks bind to the component being built.

# Reach the DOM through a ref, and listen outside it through a hook

- `t-ref="input"` in the template and `this.input = useRef("input")` in `setup` give
  `this.input.el`, which is `null` until mounted; read it in `onMounted`, an effect or
  an event handler, never in `setup`.
- A listener outside the component's own element (on `window`, `document`, `body`) is
  added with `useExternalListener(window, "resize", this.onResize)`, which removes it
  when the component is destroyed. A raw `addEventListener` leaks.
- Odoo's `useBus(bus, "EVENT", callback)` does the same for an event bus.
- Never query the document (`document.querySelector`) for an element of a component:
  another instance or another component may match.

# Pass shared values through props or the environment

- Data goes down through props, and events go up through a callback
  prop (`onLend.bind="onLend"`, where `.bind` keeps `this`); a child never reaches into its parent.
- `useSubEnv({ bookModel })` adds keys to the environment of the component and its
  children, and `useChildSubEnv` to its children only. Use it for a context a whole
  subtree needs, such as the model of a view.
- A value many unrelated components need (the current user, a service) comes from
  a service, through `useService`, not from a prop passed through every level.
