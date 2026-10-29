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
