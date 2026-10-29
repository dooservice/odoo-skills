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
