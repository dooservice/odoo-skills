Components are Owl 3 classes, imported from `@odoo/owl`. Owl 3 builds reactivity on
signals and replaces services with plugins; a compatibility layer (`@web/owl2/utils`)
keeps some Owl 2 code running while it is ported, never for new code.

```js
import { Component, onWillStart, proxy, t, useProps } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class BookCard extends Component {
    static template = "my_module.BookCard";
    static components = { Rating };
    props = useProps({ bookId: t.number(), onLend: t.function().optional() });

    setup() {
        this.orm = useService("orm");
        this.state = proxy({ book: null });
        onWillStart(async () => {
            [this.state.book] = await this.orm.read("library.book", [this.props.bookId], ["name"]);
        });
    }
}
```

- Hooks are called in `setup()` or in field initializers (`props = useProps(...)`);
  never write a `constructor`.
- Owl 3 exports, besides `Component`: `proxy`, `signal`, `computed`, `effect`,
  `useEffect`, `useListener`, `useProps`, `t` (types), `Plugin`, `usePlugin`,
  `useScope`, `onWillStart`, `onMounted`, `onWillUpdateProps`, `onPatched`,
  `onWillUnmount`, `onWillDestroy`, `markup`, `xml`, `EventBus`.
- `useState`, `useRef`, `reactive`, `useExternalListener`, `useChildSubEnv` and
  `useComponent` no longer exist; `this.env.debug` and `this.env.isSmall` throw (use
  `usePlugin(DebugModePlugin)` and the `ui` service's `isSmall`).
