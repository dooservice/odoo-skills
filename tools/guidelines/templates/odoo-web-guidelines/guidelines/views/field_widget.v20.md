```js
import { Component, t, useProps } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class RatingField extends Component {
    static template = "my_module.RatingField";
    props = useProps({
        ...standardFieldProps,
        maxStars: t.number().optional(5),
    });

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
- Props are declared with `useProps` and `t` types, defaults inside `.optional(value)`;
  a `static props` throws in this version (see [owl.md](owl.md)).
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
