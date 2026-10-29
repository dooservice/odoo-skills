`patch(target, extension)` from `@web/core/utils/patch` changes `target` in place and
returns a function that removes the patch; there is no patch name in this version (a
string second argument throws). The patched method reaches the original with `super`.

```js
patch(BookCard.prototype, {
    setup() {
        super.setup(...arguments);
        this.notification = useService("notification");
    },
});
```
