Key names in 18.0:

- `registry.category("fields")` takes a descriptor (`component`, `supportedTypes`, `extractProps`).
- `extractProps(fieldInfo, dynamicInfo)`; a field widget writes with `props.record.update`; `standardFieldProps`, `standardWidgetProps`.
- Lookup keys: `<js_class>.<widget>`, `<view type>.<widget>`, `<widget>`.
- `js_class` on the arch root, a view descriptor of `registry.category("views")`; the list arch tag is `list`, and an unknown `js_class` throws after `web.assets_backend_lazy`.
- `<widget name="my_module_banner"/>` through `registry.category("view_widgets")`.

Sections of this file:

- Views on the client side in 18.0
- Write a field widget as a component plus a registry entry
- Read arch attributes and options in `extractProps`
- Prefix a widget key with a view type to change it in one view only
- Extend a view with `js_class`, never by patching it for one model
- Add a `<widget>` to a view through `view_widgets`

# Views on the client side in 18.0

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
import { Component } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class RatingField extends Component {
    static template = "my_module.RatingField";
    static props = {
        ...standardFieldProps,
        maxStars: { type: Number, optional: true },
    };
    static defaultProps = { maxStars: 5 };

    onStarClick(value) {
        this.props.record.update({ [this.props.name]: value });
    }
}

export const ratingField = {
    component: RatingField,
    displayName: _t("Rating"),
    supportedTypes: ["integer"],
    extractProps: ({ options }) => ({ maxStars: options.max_stars }),
};

registry.category("fields").add("my_module_rating", ratingField);
```

- The entry is a descriptor; the component holds only rendering and events.
- The value is `props.record.data[props.name]` and the change goes through
  `props.record.update({ [props.name]: value })`: the record is the single source of
  truth, so never copy the value into the component's state except while the user is
  typing.
- `standardFieldProps` (`@web/views/fields/standard_field_props`) holds the props every
  field receives: `id`, `name`, `readonly`, `record`.
- Other descriptor keys: `isEmpty(record, fieldName)`, `isValid`, `additionalClasses`,
  `fieldDependencies` (other fields the widget reads, loaded with the record),
  `relatedFields` (fields to load on the related records of a relational field),
  `listViewWidth`, `label`.

# Read arch attributes and options in `extractProps`

`extractProps(fieldInfo, dynamicInfo)` receives the parsed `<field>` node as
`fieldInfo` (`attrs`, `options`, `string`, `widget`, `context`, `domain`, ...) and the
values that depend on the record as `dynamicInfo` (`readonly`, `required`, `context`,
`domain()`); it returns the extra props. It is called again when the record changes,
so read record-dependent values from `dynamicInfo`, never from the arch.

- Name the options in `snake_case` in the arch (`options="{'max_stars': 3}"`) and turn
  them into `camelCase` props in `extractProps`; the component never reads the arch.
- Give every prop a default, so the widget works without options.
- Declare what the widget accepts, so Studio and the field documentation show it:
  `supportedTypes`, `supportedOptions` and `supportedAttributes` (each
  option `{ label, name, type }`).

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
<list js_class="my_module_book_list">
```

- Spread the standard descriptor and replace only the part that changes (`Controller`,
  `Renderer`, `Model`, `ArchParser`, `buttonTemplate`); the others stay in sync with
  Odoo's code at each upgrade.
- The controller's template extends the standard one with `t-inherit` and
  `t-inherit-mode="primary"`, so it can add a button next to the standard ones.
- A `js_class` that is not registered is looked up again after loading
  `web.assets_backend_lazy`, then throws: a typo fails loudly.
- Patching `ListController.prototype` instead changes every list of the database; do it
  only when that is the goal.

# Add a `<widget>` to a view through `view_widgets`

A view widget is a component that receives the `record`; it renders in the arch where
`<widget name="my_module_banner"/>` stands, in form, list and kanban views.

```js
export class BookBanner extends Component {
    static template = "my_module.BookBanner";
    static props = { ...standardWidgetProps, text: { type: String, optional: true } };
}
registry.category("view_widgets").add("my_module_banner", {
    component: BookBanner,
    extractProps: ({ attrs }) => ({ text: attrs.title }),
});
```

`standardWidgetProps` (`@web/views/widgets/standard_widget_props`) holds `record` and
`readonly`. The descriptor also takes `fieldDependencies` for the fields the widget
reads, which are then loaded even when the arch does not show them.
