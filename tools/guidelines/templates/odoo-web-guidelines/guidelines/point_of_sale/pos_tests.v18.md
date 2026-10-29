- A POS tour is an entry of `registry.category("web_tour.tours")` with
  `steps: () => [...]`, built from the helpers of
  `@point_of_sale/../tests/tours/utils/` (`product_screen_util`, `payment_screen_util`).
- The Python test extends `TestPointOfSaleHttpCommon` and runs
  `self.start_pos_tour("my_module.lend_tour")`, which opens the session and the POS
  for you.