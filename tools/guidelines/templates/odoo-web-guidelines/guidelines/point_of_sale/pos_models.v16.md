```js
odoo.define("my_module.models", function (require) {
    const { Orderline } = require("point_of_sale.models");
    const Registries = require("point_of_sale.Registries");

    const BookOrderline = (Orderline) => class BookOrderline extends Orderline {
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.book_isbn = this.book_isbn;
            return json;
        }
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.book_isbn = json.book_isbn;
        }
    };
    Registries.Model.extend(Orderline, BookOrderline);
});
```

- Extend through `Registries.Model.extend` (and components through
  `Registries.Component.extend`), never by assigning to the prototype: the registry
  builds the final class from every module's extension.
- A value stored on an order or a line goes in both `export_as_JSON` and
  `init_from_JSON`, or it is lost when the POS reloads the order from the browser
  storage.
