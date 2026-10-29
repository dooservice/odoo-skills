An Owl component in a QWeb page is declared in the HTML and mounted by the
`public_component` service:

```xml
<owl-component name="my_module.book_card" t-att-props="json.dumps({'bookId': book.id})"/>
```

```js
registry.category("public_components").add("my_module.book_card", BookCard);
```

- The `name` attribute is the registry key; `props` is JSON, so pass ids and plain
  values, never records.
- Each component is its own small Owl application: it does not share state with
  another `<owl-component>` of the page. Use one when a block is truly interactive (a
  configurator, a live search); simple behaviour stays a public widget.
