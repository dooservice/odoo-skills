```js
/** @odoo-module **/
import { Orderline } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Orderline.prototype, {
    export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.book_isbn = this.book_isbn;
        return json;
    },
    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.book_isbn = json.book_isbn;
    },
});
```

- Patch the prototype of `Order`, `Orderline` or `PosStore`; a component is patched
  the same way (`patch(ProductScreen.prototype, { ... })`).
- A value stored on an order or a line goes in both `export_as_JSON` and
  `init_from_JSON`, or it is lost when the POS reloads the order from the browser
  storage.
