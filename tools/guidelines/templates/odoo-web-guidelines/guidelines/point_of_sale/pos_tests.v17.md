- A POS tour is an entry of `registry.category("web_tour.tours")` with
  `url: "/pos/ui"` and `steps: () => [...]`, built from the helpers of
  `@point_of_sale/../tests/tours/helpers/` (`ProductScreen.clickDisplayedProduct(...)`).
- The Python test extends `TestPointOfSaleHttpCommon` and runs
  `self.start_tour("/pos/ui?config_id=%d" % self.main_pos_config.id, "my_module.lend_tour", login="pos_user")`
  after opening a session.