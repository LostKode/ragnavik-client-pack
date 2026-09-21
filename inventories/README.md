# Normalized package inventories

before.json records the exact first-wave source tree at commit 9b39271.
shared-manifest.json records the exact Ragnavik Shared version consumed by the
Client Pack. proposed.json is generated from the rebuilt source tree by
scripts/generate_inventory.py. It distinguishes direct, Shared, and effective
dependencies so moving packages behind the Shared metapackage cannot look like
a removal. DLLs, plugin GUIDs, patchers, configurations, and assets are sorted
and de-duplicated.

The inventory is scoped to the client pack archive itself. Resolver-expanded
dependencies are recorded in effective_dependencies. The eight Intermission images remain
packaged as preserved loading artwork for the Ragnavik UI loading-screen transition.
Intermission itself is intentionally removed from dependencies.
