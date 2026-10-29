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
