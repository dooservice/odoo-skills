- A POS tour is registered with `Tour.register(name, { test: true, url: "/pos/ui" },
  steps)`, built from the step helpers of `point_of_sale.tour.utils` and the
  `*TourMethods` modules (`ProductScreen.do.clickDisplayedProduct(...)`).
- The Python test extends `TestPointOfSaleHttpCommon` and runs
  `self.start_tour("/pos/ui?config_id=%d" % self.main_pos_config.id, "my_module.lend_tour", login="accountman")`
  after opening a session.