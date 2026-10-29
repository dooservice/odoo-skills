The product screen exposes `ProductScreen.addControlButton({ component, condition,
position })`: `condition()` hides the button when it returns false, and `position`
(`["before", "OtherButton"]`) places it. Add the button through it instead of patching
the screen's template.
