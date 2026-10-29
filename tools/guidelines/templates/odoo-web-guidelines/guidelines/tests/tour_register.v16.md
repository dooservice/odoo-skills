This version has no `web_tour.tours` registry yet: a tour is registered through the
legacy `web_tour.tour` module.

```js
/** @odoo-module **/
import tour from "web_tour.tour";

tour.register("my_module.lend_book", { test: true, url: "/web" }, [
    { trigger: ".o_app[data-menu-xmlid='my_module.menu_root']" },
    { trigger: ".o_list_button_add" },
]);
```

- The name is prefixed with the module (`my_module.lend_book`): tour names are global.
- `test: true` keeps the tour out of the onboarding tours a user can start; every test
  tour sets it.
- Steps are a plain array; shared steps come from `tour.stepUtils` (`goToAppSteps`,
  `saveForm`, `discardForm`).
