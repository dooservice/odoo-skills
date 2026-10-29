- The code is ES modules under `point_of_sale/static/src/app/`, in the bundle
  `point_of_sale._assets_pos`; add your files there.
- The state of the session is the `pos` service, a `PosStore`
  (`@point_of_sale/app/store/pos_store`), reached from a component with `usePos()`
  (`@point_of_sale/app/store/pos_hook`).
- Records are instances of classes generated from the server models: `PosOrder`
  (`@point_of_sale/app/models/pos_order`), `PosOrderline`
  (`@point_of_sale/app/models/pos_order_line`), registered in
  `registry.category("pos_available_models")` under their Python model name. The
  `pos_data` service loads and stores them; `this.pos.models["library.book"]` gives the
  records of a model.
- Screens are registered in `registry.category("pos_screens")` and shown with
  `this.pos.showScreen("ProductScreen")`.