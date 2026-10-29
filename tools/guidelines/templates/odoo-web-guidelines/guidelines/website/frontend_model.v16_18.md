Behaviour is written as a public widget: `publicWidget.Widget.extend({...})` from
`@web/legacy/js/public/public_widget`, registered in `publicWidget.registry`. It is the
legacy widget class, not Owl: no templates, no reactivity, `this._super` for overrides.