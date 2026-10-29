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
