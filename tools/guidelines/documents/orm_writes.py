"""What differs between versions in writing records, access checks and the cache."""

from __future__ import annotations

from ..version import OdooVersion


class OrmWrites:
    """The template values of the write, archive, lock and cache sections of `orm.md`."""

    def __init__(self, version: OdooVersion) -> None:
        self.version = version

    def records(self) -> dict[str, str]:
        pick = self.version.pick
        return {
            "copy": pick(
                v16="`copy(default)` duplicates one record (it calls `ensure_one()`); loop to "
                "duplicate several.",
                v17="`copy(default)` duplicates one record (it calls `ensure_one()`); "
                "`copy_multi(default)` duplicates several, one `copy` each.",
                v18_="`copy(default)` duplicates every record of `self` with one `create` and "
                "returns the copies in the same order.",
            ),
            "copy_translations": pick(
                v16_19=" `copy` then calls `copy_translations` to copy the translations of "
                "the duplicated fields.",
                v20="",
            ),
            "translation_methods": pick(
                v16_17="`get_field_translations(field_name, langs=None)` and "
                "`update_field_translations(field_name, {lang: value})`",
                v18_="`get_field_translations(field_name, langs=None)` and "
                "`update_field_translations(field_name, {lang: value}, source_lang=...)`",
            ),
            "toggle_active": pick(
                v16_18="`toggle_active()` inverts `active` on each record; call the explicit "
                "methods instead, which say what they do.",
                v19="`toggle_active()` is deprecated: call `action_archive` or "
                "`action_unarchive`.",
                v20="`toggle_active()` no longer exists: call `action_archive` or "
                "`action_unarchive`.",
            ),
            "locking": pick(
                v16_18="run `SELECT id FROM <table> WHERE id IN %s FOR UPDATE NOWAIT` with "
                "`self.env.cr.execute` inside `with self.env.cr.savepoint():`, and turn the "
                "lock error into a retry or a `UserError`. A queue takes only the free rows "
                "with `FOR UPDATE SKIP LOCKED`.",
                v19_="`records.lock_for_update()` locks every row without waiting, or raises "
                "`LockError` (a `UserError`); `records.try_lock_for_update(limit=n)` locks "
                "what it can, skips rows locked elsewhere and returns the locked records, as a "
                "queue needs. `allow_referencing=True` takes a weaker lock that still lets "
                "other transactions create records pointing at these rows: use it when you "
                "change only ordinary values.",
            ),
        }

    def cache(self) -> dict[str, str]:
        pick = self.version.pick
        return {
            "deprecated_cache": pick(
                v16="\n- `flush()`, `invalidate_cache()`, `recompute()` and `refresh()` are "
                "deprecated: use the methods above.",
                v17_="",
            ),
            "clear_caches": pick(
                v16="\n- After changing data that a `tools.ormcache` method caches, call "
                "`self.clear_caches()`; it clears every cache of the registry.",
                v17_18="\n- After changing data that a `tools.ormcache` method caches, call "
                "`self.env.registry.clear_cache()`; `clear_caches()` is deprecated.",
                v19="\n- After changing data that a `tools.ormcache` method caches, call "
                "`self.env.registry.clear_cache()`; `clear_caches()` no longer exists.",
                v20="\n- Cache method results with `@api.ormcache(...)`. After changing data it "
                "caches, call `self.env.transaction.invalidate_ormcache(cache_name)`, or set "
                "`_clear_cache_name` on the model so that its `create`, `write` and `unlink` "
                "invalidate that cache. `clear_caches()` and `registry.clear_cache()` no "
                "longer exist.",
            ),
        }
