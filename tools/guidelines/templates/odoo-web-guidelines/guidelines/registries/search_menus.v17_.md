- `category("cogMenu")` adds items to the gear menu next to the breadcrumb: `{ Component,
  groupNumber, isDisplayed }`. `isDisplayed(env)` may be async (`env.config.viewType ===
  "list"` is the usual test), and `groupNumber` places the item in a group:
  `STATIC_ACTIONS_GROUP_NUMBER` (1) or `ACTIONS_GROUP_NUMBER` (100), both from
  `@web/search/action_menus/action_menus`. Items are keyed by their component's class
  name, so two entries must not share a component class name.
- `category("favoriteMenu")` adds items to the Favorites part of the search menu:
  `{ Component, groupNumber, isDisplayed }`. Here `isDisplayed(env)` is called without
  `await`: make it synchronous, because a promise always counts as true.