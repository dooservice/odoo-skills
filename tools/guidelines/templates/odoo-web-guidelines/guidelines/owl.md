# Owl in $version

$owl_intro

# Declare every prop the component takes

$props

# Keep component state reactive

$state

# Name templates `<module>.<Component>` and keep them in XML files

- The template lives in an `.xml` file next to the component, in the same bundle, as
  `<t t-name="my_module.BookCard">`$owl_attr; the component points at it with
  `static template = "my_module.BookCard"`. An inline `xml` template is for tests and
  tiny internal components only: it cannot be inherited.
- $template_scope
- $escape
- Loops need a key: `t-foreach="books" t-as="book" t-key="book.id"`; an index as key
  breaks when the list is reordered.
- Child components are listed in `static components = { BookCard }` and used as
  `<BookCard book="book"/>`; props are expressions, so a string literal is quoted
  twice (`title="'Books'"`).

# Extend a template with `t-inherit`, never by copying it

```xml
<t t-name="my_module.BookCard" t-inherit="other_module.BookCard" t-inherit-mode="extension">
    <xpath expr="//div[hasclass('o_book_card_footer')]" position="inside">
        <button class="btn btn-secondary" t-on-click="$click_handler">Lend all</button>
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
- $effect
- `onPatched` runs after each re-render; prefer an effect that states what it depends
  on.
- Never call a hook (`useService`, `onMounted`, ...) outside `setup` or a field
  initializer: hooks bind to the component being built.

# Reach the DOM through a ref, and listen outside it through a hook

$refs

# Pass shared values through props or the environment

- Data goes down through props, and events go up through a callback
  prop $bind_note; a child never reaches into its parent.
- $sub_env
- A value many unrelated components need (the current user, a service) comes from
  $shared_source, not from a prop passed through every level.
