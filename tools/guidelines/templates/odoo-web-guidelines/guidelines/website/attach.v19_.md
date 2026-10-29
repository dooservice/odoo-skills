An interaction is started on every element that matches its `selector`, and only there:
code that queries `document` runs on pages that do not have the element and breaks them.

```js
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

export class BookList extends Interaction {
    static selector = ".o_my_module_book_list";
    dynamicContent = {
        ".o_my_module_lend": { "t-on-click": this.onLendClick },
        ".o_my_module_counter": { "t-out": () => this.count },
        _root: { "t-att-class": () => ({ o_my_module_empty: !this.count }) },
    };

    setup() {
        this.count = 0;
    }

    async willStart() {
        this.count = await this.waitFor(rpc("/my_module/book_count"));
    }

    onLendClick() {
        this.count--;
    }
}

registry.category("public.interactions").add("my_module.book_list", BookList);
```

- `static selector` scopes it; `static selectorHas` and `static selectorNotHas` start it
  only when the element contains, or does not contain, a match.
- `dynamicContent` maps selectors inside the element (and `_root`, `_body`, `_window`,
  `_document`) to `t-on-<event>`, `t-att-<attribute>`, `t-att-class`, `t-att-style` and
  `t-out`. It is not Owl: after a handler runs, the interaction re-applies the values,
  and after changing state elsewhere (a timer, a promise) call `this.updateContent()`.
- The lifecycle is `setup()`, `async willStart()`, `start()`, `destroy()`; never
  override the constructor. Handlers are bound to the interaction, and services are in
  `this.services`.
