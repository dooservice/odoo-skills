A tour is an entry of `registry.category("web_tour.tours")`, whose `steps` is a function
returning the steps; a plain array throws when the tour starts.

```js
/** @odoo-module **/
import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("my_module.lend_book", {
    test: true,
    url: "/web",
    steps: () => [
        { trigger: ".o_app[data-menu-xmlid='my_module.menu_root']" },
        { trigger: ".o_list_button_add" },
    ],
});
```

- The name is prefixed with the module (`my_module.lend_book`): tour names are global.
- `test: true` keeps the tour out of the onboarding tours a user can start; every test
  tour sets it.
- Shared steps come from `stepUtils` of `@web_tour/tour_service/tour_utils`
  (`goToAppSteps`, `saveForm`, `discardForm`, `showAppsMenuItem`).
