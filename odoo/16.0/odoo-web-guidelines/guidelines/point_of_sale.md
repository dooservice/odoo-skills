# The Point of Sale in 16.0

The Point of Sale is a separate web application (`/pos/ui`), not a view of the backend
client. It loads its data once when a session opens, keeps it in the browser, and works
offline: sales are recorded in the browser and synchronized with the server later.
Every extension has to respect that.

- The code is legacy `odoo.define` modules under `point_of_sale/static/src/js/`, in the
  bundle `point_of_sale.assets`; add your files there.
- The state of the session is `PosGlobalState`, reached from a component as
  `this.env.pos`; orders and lines are the classes `Order` and `Orderline` of
  `point_of_sale.models`.
- Components extend `PosComponent` and are registered with `Registries.Component.add`;
  screens are such components, shown with `this.showScreen("ProductScreen")`.

# Load a field into the Point of Sale from Python

The POS only knows the records and fields that the session loads at start; a field
added to a model is invisible there until the loading code names it.

- A field of a model already loaded: extend the loader parameters of that model on
  `pos.session`.

  ```python
  def _loader_params_product_product(self):
      params = super()._loader_params_product_product()
      params['search_params']['fields'].append('book_isbn')
      return params
  ```

- A new model: add it to `_pos_ui_models_to_load()`, and define
  `_loader_params_<model>()` (the `search_params` with `domain` and `fields`) and
  `_get_pos_ui_<model>(params)` on `pos.session`; the data then arrives in the
  `loadedData` the store processes at start.
- A value the order sends back: read it in `pos.order._order_line_fields` (lines) or
  `pos.order._order_fields` (orders), and export it in `export_as_JSON` on the client.

# Extend Point of Sale models and screens without replacing them

```js
odoo.define("my_module.models", function (require) {
    const { Orderline } = require("point_of_sale.models");
    const Registries = require("point_of_sale.Registries");

    const BookOrderline = (Orderline) => class BookOrderline extends Orderline {
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.book_isbn = this.book_isbn;
            return json;
        }
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.book_isbn = json.book_isbn;
        }
    };
    Registries.Model.extend(Orderline, BookOrderline);
});
```

- Extend through `Registries.Model.extend` (and components through
  `Registries.Component.extend`), never by assigning to the prototype: the registry
  builds the final class from every module's extension.
- A value stored on an order or a line goes in both `export_as_JSON` and
  `init_from_JSON`, or it is lost when the POS reloads the order from the browser
  storage.

# Add a button to the product screen through its extension point

The product screen exposes `ProductScreen.addControlButton({ component, condition,
position })`: `condition()` hides the button when it returns false, and `position`
(`["before", "OtherButton"]`) places it. Add the button through it instead of patching
the screen's template.

# Keep the Point of Sale working offline

- Never call the server in the middle of a sale (on a click of the product screen, on
  each order line): the session may be offline, and every call slows the cashier down.
  Load what the sale needs at start, and compute in the browser.
- A call to the server is for an action that needs it anyway (validating a payment
  with a terminal, printing to an IoT box), and its error path tells the cashier what
  happened instead of losing the sale.
- Business rules that must hold (taxes, stock, accounting) are enforced on the server
  when the order is synchronized; the browser only previews them.

# Test the Point of Sale with tours

- A POS tour is registered with `Tour.register(name, { test: true, url: "/pos/ui" },
  steps)`, built from the step helpers of `point_of_sale.tour.utils` and the
  `*TourMethods` modules (`ProductScreen.do.clickDisplayedProduct(...)`).
- The Python test extends `TestPointOfSaleHttpCommon` and runs
  `self.start_tour("/pos/ui?config_id=%d" % self.main_pos_config.id, "my_module.lend_tour", login="accountman")`
  after opening a session.
