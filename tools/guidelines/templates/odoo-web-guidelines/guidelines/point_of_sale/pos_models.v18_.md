```js
import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";
import { patch } from "@web/core/utils/patch";

patch(PosOrderline.prototype, {
    setup(vals) {
        super.setup(...arguments);
        this.book_note ||= "";
    },
    getBookLabel() {
        return `${this.product_id.display_name} (${this.book_isbn})`;
    },
});
```

- A field loaded from Python is already a property of the record (`line.book_isbn`),
  and a many2one is the related record (`line.product_id.display_name`): do not copy
  fields in `setup`, and do not write `export_as_JSON` or `init_from_JSON`, which no
  longer exist.
- Patch the prototype of `PosOrder`, `PosOrderline` or `PosStore`; a component is
  patched the same way (`patch(ProductScreen.prototype, { ... })`).
- A model of your own that needs behaviour is a class extending `Base`
  (`@point_of_sale/app/models/related_models`) with `static pythonModel =
  "library.book"`, added to `registry.category("pos_available_models")`.
