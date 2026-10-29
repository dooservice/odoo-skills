A tour is an entry of `registry.category("web_tour.tours")`, whose `steps` is a function
returning the steps; a plain array throws when the tour starts.

```js
import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("my_module.lend_book", {
    url: "/odoo",
    steps: () => [
        { trigger: ".o_app[data-menu-xmlid='my_module.menu_root']", run: "click" },
        { trigger: ".o_list_button_add", run: "click" },
    ],
});
```

- The name is prefixed with the module (`my_module.lend_book`): tour names are global.
- The entry takes `steps`, `url`, and `wait_for` (a promise to wait for before the first
  step); the registry validates it in debug mode, so a leftover `test: true` from an older
  version is an error there.
- Shared steps come from `stepUtils` of `@web_tour/tour_service/tour_utils` (`goToAppSteps`, `saveForm`,
  `discardForm`, `showAppsMenuItem`).
