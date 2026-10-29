`static extractProps({ attrs, field })` receives the raw arch attributes, with the
evaluated `options` dict as `attrs.options`, and the field description as `field`; it
returns the extra props. It runs when the arch is parsed (at render in kanban), so it
must not read record values.