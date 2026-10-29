# Views on the client side in 16.0

A view is an arch from the server turned into components: an `ArchParser` reads the
arch, a `Model` loads the records, a `Renderer` draws them and a `Controller` holds the
control panel and the buttons. Each view type is a descriptor in
`registry.category("views")`, each field widget an entry of
`registry.category("fields")`, and each `<widget>` an entry of
`registry.category("view_widgets")`.

- Change how one field looks or edits: a field widget, named in the arch with
  `widget="my_module_rating"`.
- Add something to a view that is not a field (a banner, a button bar): a view widget,
  `<widget name="my_module_banner"/>`.
- Change how a whole view behaves (a button in the control panel, a different load):
  a new view descriptor, named with `js_class` on the arch root.
- Change one standard widget or view everywhere: `patch` its component, as a last
  resort.

# Write a field widget as a component plus a registry entry

```js
/** @odoo-module **/
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class RatingField extends Component {
    static template = "my_module.RatingField";
    static props = {
        ...standardFieldProps,
        maxStars: { type: Number, optional: true },
    };
    static defaultProps = { maxStars: 5 };
    static supportedTypes = ["integer"];
    static extractProps = ({ attrs }) => ({ maxStars: attrs.options.max_stars });

    onStarClick(value) {
        this.props.update(value);
    }
}

registry.category("fields").add("my_module_rating", RatingField);
```

- The entry is the component class itself, and the class carries the field statics:
  `supportedTypes`, `extractProps`, `displayName`, `isEmpty`.
- The value is `props.value` and the change goes through `props.update(value)`;
  `props.readonly` tells the template whether to allow editing.
- `standardFieldProps` (`@web/views/fields/standard_field_props`) holds the props every
  field receives: `id`, `name`, `readonly`, `record`, `type`, `update`, `value`,
  `decorations`, `setDirty`.

# Read arch attributes and options in `extractProps`

`static extractProps({ attrs, field })` receives the raw arch attributes, with the
evaluated `options` dict as `attrs.options`, and the field description as `field`; it
returns the extra props. It runs when the arch is parsed (at render in kanban), so it
must not read record values.

- Name the options in `snake_case` in the arch (`options="{'max_stars': 3}"`) and turn
  them into `camelCase` props in `extractProps`; the component never reads the arch.
- Give every prop a default, so the widget works without options.
- Declare what the widget accepts, so Studio and the field documentation show it:
  the class statics `supportedTypes` and `displayName`.

# Prefix a widget key with a view type to change it in one view only

The field registry is searched from the most specific key to the least:
`<js_class>.<widget>`, `<view type>.<widget>`, `<widget>`, then, without a
widget, `<view type>.<field type>` and `<field type>`.

Register `list.my_module_rating` to give the list a lighter version of the widget, and
keep `my_module_rating` for the other views.

The list parser does not pass the `js_class`, so a `my_list_class.my_module_rating` key
is never found in a list; the form and kanban parsers pass it.

# Extend a view with `js_class`, never by patching it for one model

```js
/** @odoo-module **/
import { listView } from "@web/views/list/list_view";
import { ListController } from "@web/views/list/list_controller";
import { registry } from "@web/core/registry";

export class BookListController extends ListController {
    static template = "my_module.BookListController";
    async onClickLendAll() {
        ...
    }
}

registry.category("views").add("my_module_book_list", {
    ...listView,
    Controller: BookListController,
});
```

```xml
<tree js_class="my_module_book_list">
```

- Spread the standard descriptor and replace only the part that changes (`Controller`,
  `Renderer`, `Model`, `ArchParser`, `buttonTemplate`); the others stay in sync with
  Odoo's code at each upgrade.
- The controller's template extends the standard one with `t-inherit` and
  `t-inherit-mode="primary"`, so it can add a button next to the standard ones.
- A `js_class` that is not registered is ignored without a warning: the view opens as
  the standard one. Check the key when the custom behaviour does not show.
- Patching `ListController.prototype` instead changes every list of the database; do it
  only when that is the goal.

# Add a `<widget>` to a view through `view_widgets`

A view widget is a component that receives the `record`; it renders in the arch where
`<widget name="my_module_banner"/>` stands, in form, list and kanban views.

```js
/** @odoo-module **/
export class BookBanner extends Component {
    static template = "my_module.BookBanner";
    static props = { ...standardWidgetProps, text: { type: String, optional: true } };
    static extractProps = ({ attrs }) => ({ text: attrs.title });
}
registry.category("view_widgets").add("my_module_banner", BookBanner);
```

`standardWidgetProps` (`@web/views/widgets/standard_widget_props`) holds `record` and
`readonly`.
