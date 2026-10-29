A plugin holds what several components need and what must outlive any one of them: a
cache, a connection, a shared reactive state.

```js
import { Plugin, signal, usePlugin } from "@odoo/owl";
import { ORM } from "@web/core/orm_plugin";
import { services } from "@web/core/services";

export class LibraryPlugin extends Plugin {
    orm = usePlugin(ORM);
    lentCount = signal(0);

    async refresh() {
        this.lentCount.set(await this.orm.searchCount("library.book", [["state", "=", "lent"]]));
    }
}

services.add(LibraryPlugin);
```

- A plugin is a class: its fields and `setup()` run once, and its methods are its API.
  It reaches other plugins with `usePlugin` in a field or in `setup`, which also orders
  their start.
- State is made of signals and proxies, so a component that reads
  `this.library.lentCount()` re-renders when it changes.
- `static sequence` (default 50) orders the start of plugins that do not depend on each
  other.
- Do not register a new `registry.category("services")` entry: that registry is the
  bridge for code written before plugins, and it goes away.
- A component that only one screen uses keeps its logic: a plugin is for what is
  shared.
