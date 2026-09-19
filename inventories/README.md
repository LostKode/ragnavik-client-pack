# Normalized package inventories

before.json records the exact first-wave source tree at commit 9b39271.
proposed.json is generated from the rebuilt source tree by
scripts/generate_inventory.py. Dependency arrays, DLLs, plugin GUIDs,
patchers, configurations, and assets are sorted and de-duplicated.

The inventory is scoped to the client pack archive itself. Resolver-expanded
package contents are verified separately. The eight Intermission images remain
packaged as preserved loading artwork for the Ragnavik UI loading-screen transition.
Intermission itself is intentionally removed from dependencies.
