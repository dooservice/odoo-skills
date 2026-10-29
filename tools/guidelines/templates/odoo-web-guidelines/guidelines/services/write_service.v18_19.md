A service holds what several components need and what must outlive any one of them: a
cache, a connection, a shared reactive state.

```js
import { reactive } from "@odoo/owl";
import { registry } from "@web/core/registry";

export const libraryService = {
    dependencies: ["orm"],
    start(env, { orm }) {
        const state = reactive({ lentCount: 0 });
        async function refresh() {
            state.lentCount = await orm.searchCount("library.book", [["state", "=", "lent"]]);
        }
        return { state, refresh };
    },
};

registry.category("services").add("my_module.library", libraryService);
```

- `dependencies` lists the services `start` receives; they are started first, and a
  missing one stops the client with an error naming it.
- `start(env, deps)` returns the service's public API; it may be async, and the
  services that depend on it wait.
- `async: ["refresh"]` names the methods that `useService` must protect when a
  component is destroyed.
- Components read shared state with `useState(service.state)`, so they re-render when
  it changes.
- A component that only one screen uses keeps its logic: a service is for what is
  shared.
