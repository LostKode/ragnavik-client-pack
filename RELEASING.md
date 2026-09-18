# Release process

This repository is the release source for the `LostKode-Ragnavik` Hexium client pack. It does not contain the server pack or custom-mod source.

## Prepare a release

1. Start from a clean default branch.
2. Update `manifest.json` with the intended client-pack version and exact dependency pins.
3. Update `CHANGELOG.md`. Keep `README.md` focused on the current package details shown by Hexium.
4. Update `anti-cheat-contract.json` for every added, removed, or renamed client-only dependency or bundled client plugin.
5. Rebuild the effective client and server manifests. Shared mods must use exact version checks. Every client-only plugin GUID must appear in `CatosAntiCheat_ExtraWhitelist.txt`. Every genuinely server-only plugin GUID must appear in `CatosAntiCheat_ServerOnly.txt`.
6. Run `python3 scripts/validate_package.py`.
7. Confirm that only `manifest.json`, `README.md`, `CHANGELOG.md`, `icon.png`, `config/`, and `plugins/` enter the Hexium archive. Do not include repository metadata, release ZIPs, caches, dependency folders, secrets, or source projects.
8. Create and publish a corresponding Ragnavik website blog post. The client-pack release must not be published without its blog post.
9. Run **Prepare Hexium package** with `publish` disabled. Automated upload remains fail closed until Hexium documents a publication endpoint; publication still requires explicit approval.

## Deployment verification

When a release is paired with server changes, follow the server repository's rollback and deployment procedure. Before any replacement or restart, save the world and create and verify a separate rollback backup. After deployment, verify the actual node and readiness, BepInEx startup logs, loaded plugin count, compatibility errors, and source/runtime plugin parity. A service showing one desired replica is not sufficient evidence.

Record the Hexium version and URL, website blog-post URL, effective client and server manifest revisions, anti-cheat file revisions, loaded plugin count, and source/runtime parity result in the release record.
