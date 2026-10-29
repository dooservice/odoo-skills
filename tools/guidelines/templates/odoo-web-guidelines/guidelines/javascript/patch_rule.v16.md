`patch(target, name, extension)` from `@web/core/utils/patch` changes `target` in
place; `name` identifies the patch (`"my_module.BookCard"`) and must be unique, and
`unpatch(target, name)` removes it. The patched method reaches the original with
`this._super(...arguments)`.

```js
patch(BookCard.prototype, "my_module.BookCard", {
    setup() {
        this._super(...arguments);
        this.notification = useService("notification");
    },
});
```
