Options are declared in a template inheriting `website.snippet_options`: a
  `<div data-selector=".s_book_list">` holding `we-*` controls (`<we-select>`,
  `<we-checkbox>`, `<we-colorpicker>`) whose `data-select-class` or
  `data-select-data-attribute` change the block. JavaScript is needed only for an
  option that computes something: `options.registry.BookList = options.Class.extend({...})`
  from the editor's snippet options module, named in `data-js="BookList"`.