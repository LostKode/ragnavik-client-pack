#!/usr/bin/env python3
"""Generate the normalized proposed client-package inventory."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def files_under(name: str, suffix: str | None = None) -> list[str]:
    root = ROOT / name
    if not root.exists():
        return []
    items = (
        path.relative_to(ROOT).as_posix()
        for path in root.rglob("*")
        if path.is_file() and (suffix is None or path.suffix.lower() == suffix)
    )
    return sorted(items)


manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
shared_manifest = json.loads(
    (ROOT / "inventories" / "shared-manifest.json").read_text(encoding="utf-8")
)
shared_pin = (
    f"LostKode-{shared_manifest['name']}-{shared_manifest['version_number']}"
)
if shared_pin not in manifest["dependencies"]:
    raise SystemExit(f"client manifest must depend on {shared_pin}")
direct_dependencies = sorted(set(manifest["dependencies"]))
shared_dependencies = sorted(set(shared_manifest["dependencies"]))
effective_dependencies = sorted(
    (set(direct_dependencies) - {shared_pin}) | set(shared_dependencies)
)
contract = json.loads((ROOT / "anti-cheat-contract.json").read_text(encoding="utf-8"))
configs = [
    path
    for path in files_under("config")
    if Path(path).suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}
]
assets = [
    path
    for path in files_under("config")
    if Path(path).suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
]
assets.append("icon.png")
inventory = {
    "direct_dependencies": direct_dependencies,
    "shared_dependencies": shared_dependencies,
    "effective_dependencies": effective_dependencies,
    "bundled_dlls": files_under("plugins", ".dll"),
    "bundled_plugin_guids": sorted(
        set(contract["bundled_client_plugins"].values())
    ),
    "verified_dependency_plugin_guids": sorted(
        set(contract["client_only_dependencies"].values())
    ),
    "patchers": files_under("patchers"),
    "configs": configs,
    "assets": sorted(set(assets)),
}
(ROOT / "inventories" / "proposed.json").write_text(
    json.dumps(inventory, indent=2) + "\n", encoding="utf-8"
)
