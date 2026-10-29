- `category("action_menus")` adds items to the Action menu of a view: `{ Component,
  getProps(props, env) }`, where `getProps` returns the item's props, or a falsy value to
  hide it.
- `category("favoriteMenu")` adds items to the Favorites menu: `{ Component, groupNumber,
  isDisplayed }`. `isDisplayed(env)` is called without `await`: make it synchronous,
  because a promise always counts as true.