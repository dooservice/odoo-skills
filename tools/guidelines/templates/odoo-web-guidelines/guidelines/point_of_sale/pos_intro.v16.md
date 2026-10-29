- The code is legacy `odoo.define` modules under `point_of_sale/static/src/js/`, in the
  bundle `point_of_sale.assets`; add your files there.
- The state of the session is `PosGlobalState`, reached from a component as
  `this.env.pos`; orders and lines are the classes `Order` and `Orderline` of
  `point_of_sale.models`.
- Components extend `PosComponent` and are registered with `Registries.Component.add`;
  screens are such components, shown with `this.showScreen("ProductScreen")`.