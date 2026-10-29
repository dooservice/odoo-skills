Behaviour is written as an interaction: a class extending `Interaction` from
`@web/public/interaction`, registered in `registry.category("public.interactions")`.
Public widgets no longer exist: code written with `publicWidget` must be ported to an
interaction.