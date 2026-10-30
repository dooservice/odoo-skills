Key names in 20.0:

- ES modules in `point_of_sale._assets_pos`; the `pos` service, a `PosStore`, through `usePos()`; data through `PosDataPlugin`.
- Records: `PosOrder`, `PosOrderline`, `registry.category("pos_available_models")`.
- Loading: `pos.load.mixin`, `_load_pos_data_fields(config)`, `_load_pos_data_domain(data)`, `_load_pos_data_dependencies()`.
- Screens: `registry.category("pos_pages")`, `this.pos.navigate`; buttons in `ControlButtons`.
- Tours: `self.start_pos_tour`, `TestPointOfSaleHttpCommon`.

Sections of this file:

- The Point of Sale in 20.0
- Load a field into the Point of Sale from Python
- Extend Point of Sale models and screens without replacing them
- Add a button to the product screen through its extension point
- Keep the Point of Sale working offline
- Test the Point of Sale with tours

# The Point of Sale in 20.0

The Point of Sale is a separate web application (`/pos/ui`), not a view of the backend
client. It loads its data once when a session opens, keeps it in the browser, and works
offline: sales are recorded in the browser and synchronized with the server later.
Every extension has to respect that.

- The code is ES modules under `point_of_sale/static/src/app/`, in the bundle
  `point_of_sale._assets_pos`; add your files there.
- The state of the session is the `pos` service, a `PosStore`
  (`@point_of_sale/app/services/pos_store`), reached from a component with `usePos()`
  (`@point_of_sale/app/hooks/pos_hook`); the store reads its data through the
  `PosDataPlugin` (`usePlugin`), which replaces the `pos_data` service.
- Records are instances of classes generated from the server models: `PosOrder`
  (`@point_of_sale/app/models/pos_order`), `PosOrderline`
  (`@point_of_sale/app/models/pos_order_line`), registered in
  `registry.category("pos_available_models")` under their Python model name;
  `this.pos.models["library.book"]` gives the records of a model.
- Screens are pages of `registry.category("pos_pages")` (`{ name, component, route,
  params }`), shown with `this.pos.navigate("ProductScreen")`.

# Load a field into the Point of Sale from Python

The POS only knows the records and fields that the session loads at start; a field
added to a model is invisible there until the loading code names it.

Models loaded in the POS inherit `pos.load.mixin`. A field of a model already loaded is
added by extending its field list; the JavaScript record then has it, with no client
code.

```python
class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def _load_pos_data_fields(self, config):
        return super()._load_pos_data_fields(config) + ['book_isbn']
```

- `_load_pos_data_fields(config)` (the `pos.config` record) returns the fields to load (an empty list loads
  them all), and `_load_pos_data_domain(data)` the domain, where `data` holds what was
  loaded before.
- A new model inherits `pos.load.mixin` and is added to
  `pos.session._load_pos_data_models(config)`; a model it needs first is named in `_load_pos_data_dependencies()`.
- Load only what the POS uses: every field is sent to every POS at every opening.

# Extend Point of Sale models and screens without replacing them

```js
import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";
import { patch } from "@web/core/utils/patch";

patch(PosOrderline.prototype, {
    setup(vals) {
        super.setup(...arguments);
        this.book_note ||= "";
    },
    getBookLabel() {
        return `${this.product_id.display_name} (${this.book_isbn})`;
    },
});
```

- A field loaded from Python is already a property of the record (`line.book_isbn`),
  and a many2one is the related record (`line.product_id.display_name`): do not copy
  fields in `setup`, and do not write `export_as_JSON` or `init_from_JSON`, which no
  longer exist.
- Patch the prototype of `PosOrder`, `PosOrderline` or `PosStore`; a component is
  patched the same way (`patch(ProductScreen.prototype, { ... })`).
- A model of your own that needs behaviour is a class extending `Base`
  (`@point_of_sale/app/models/related_models`) with `static pythonModel =
  "library.book"`, added to `registry.category("pos_available_models")`.

# Add a button to the product screen through its extension point

The buttons under the order are the `ControlButtons` component
(`@point_of_sale/app/screens/product_screen/control_buttons/control_buttons`). Add a
button by extending its template and patching the component for the handler:

```xml
<t t-name="my_module.ControlButtons" t-inherit="point_of_sale.ControlButtons" t-inherit-mode="extension">
    <xpath expr="//t[@t-if='this.props.showRemainingButtons']" position="inside">
        <button class="btn btn-light" t-on-click="this.onClickLendBook">Lend</button>
    </xpath>
</t>
```

```js
patch(ControlButtons.prototype, {
    async onClickLendBook() {
        ...
    },
});
```

A component the button needs is added with `patch(ControlButtons, { components: {
...ControlButtons.components, LendDialog } })`.

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

- A POS tour is an entry of `registry.category("web_tour.tours")` with
  `steps: () => [...]`, under `static/tests/pos/tours/`, built from the helpers of
  `@point_of_sale/../tests/pos/tours/utils/` (`product_screen_util`,
  `payment_screen_util`) and `@point_of_sale/../tests/generic_helpers/`.
- The Python test extends `TestPointOfSaleHttpCommon` and runs
  `self.start_pos_tour("my_module.lend_tour")`, which opens the session and the POS
  for you.
