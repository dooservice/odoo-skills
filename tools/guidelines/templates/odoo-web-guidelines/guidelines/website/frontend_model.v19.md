Behaviour is written as an interaction: a class extending `Interaction` from
`@web/public/interaction`, registered in `registry.category("public.interactions")`.
Public widgets (`@web/legacy/js/public/public_widget`) still load for code not ported
yet; never write a new one.