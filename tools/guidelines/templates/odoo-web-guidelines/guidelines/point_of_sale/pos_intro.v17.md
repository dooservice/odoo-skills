- The code is ES modules under `point_of_sale/static/src/app/`, in the bundle
  `point_of_sale._assets_pos`; add your files there.
- The state of the session is the `pos` service, a `PosStore`
  (`@point_of_sale/app/store/pos_store`), reached from a component with `usePos()`
  (`@point_of_sale/app/store/pos_hook`); orders and lines are `Order` and `Orderline`
  of `@point_of_sale/app/store/models`.
- Components are Owl components; screens are registered in
  `registry.category("pos_screens")` and shown with `this.pos.showScreen("ProductScreen")`.