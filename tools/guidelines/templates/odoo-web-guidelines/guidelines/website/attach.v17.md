A public widget is started on every element that matches its `selector`, and only
there: code that queries `document` runs on pages that do not have the element and
breaks them.

```js
/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.BookList = publicWidget.Widget.extend({
    selector: ".o_my_module_book_list",
    events: {
        "click .o_my_module_lend": "_onLendClick",
    },
    async start() {
        await this._super(...arguments);
        this.counterEl = this.el.querySelector(".o_my_module_counter");
    },
    _onLendClick(ev) {
        this.counterEl.textContent = ...;
    },
});
```

- `selector` scopes the widget, `events` binds handlers on elements inside it, and
  `start` runs once the widget is attached; it returns a promise and calls `_super`.
- Services are bound in `init` with `this.rpc = this.bindService("rpc")`, then
  `this.rpc("/my_module/books", { limit: 10 })` calls a route.
