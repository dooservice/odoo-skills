- A POS tour is an entry of `registry.category("web_tour.tours")` with
  `steps: () => [...]`, under `static/tests/pos/tours/`, built from the helpers of
  `@point_of_sale/../tests/pos/tours/utils/` (`product_screen_util`,
  `payment_screen_util`) and `@point_of_sale/../tests/generic_helpers/`.
- The Python test extends `TestPointOfSaleHttpCommon` and runs
  `self.start_pos_tour("my_module.lend_tour")`, which opens the session and the POS
  for you.