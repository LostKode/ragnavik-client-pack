#!/usr/bin/env python3
"""Validate the Thunderstore client package and anti-cheat contract."""

from __future__ import annotations

import json
import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPENDENCY = re.compile(
    r"^(?P<namespace>[A-Za-z0-9_]+)-(?P<name>[A-Za-z0-9_]+)-"
    r"(?P<version>[0-9]+\.[0-9]+\.[0-9]+)$"
)
PACKAGE_KEY = re.compile(r"^[A-Za-z0-9_]+-[A-Za-z0-9_]+$")
VERSION = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
REQUIRED = ("manifest.json", "README.md", "icon.png")
FORBIDDEN_PARTS = {
    "node_modules", "serverpack", "server-pack", "src", "source",
    "bin", "obj", "__pycache__",
}
FORBIDDEN_SUFFIXES = {".zip", ".pdb", ".cs", ".csproj", ".sln", ".pyc"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) != 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        fail(f"{path.relative_to(ROOT)} is not a valid PNG")
    return struct.unpack(">II", data[16:24])


def main() -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            fail(f"missing required Thunderstore file: {relative}")

    try:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        contract = json.loads(
            (ROOT / "anti-cheat-contract.json").read_text(encoding="utf-8")
        )
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        fail(f"invalid JSON: {error}")

    for field in ("name", "version_number", "website_url", "description", "dependencies"):
        if field not in manifest:
            fail(f"manifest is missing {field}")
    if not VERSION.fullmatch(manifest["version_number"]):
        fail("manifest version_number must be semantic x.y.z")
    if not isinstance(manifest["dependencies"], list) or not manifest["dependencies"]:
        fail("manifest dependencies must be a nonempty list")
    if len(manifest["dependencies"]) != len(set(manifest["dependencies"])):
        fail("manifest contains duplicate dependencies")

    parsed = []
    for dependency in manifest["dependencies"]:
        match = DEPENDENCY.fullmatch(dependency)
        if not match:
            fail(f"dependency is not parseable: {dependency}")
        parsed.append(match.groupdict())

    server_prefix = contract["server_pack_prefix"]
    server_packs = [dep for dep in manifest["dependencies"] if dep.startswith(server_prefix)]
    if len(server_packs) != 1:
        fail(f"expected exactly one {server_prefix} dependency")

    client_keys = {
        f"{item['namespace']}-{item['name']}"
        for dep, item in zip(manifest["dependencies"], parsed)
        if not dep.startswith(server_prefix)
    }
    mappings = contract["client_only_dependencies"]
    invalid_keys = sorted(key for key in mappings if not PACKAGE_KEY.fullmatch(key))
    if invalid_keys:
        fail(f"invalid package keys in anti-cheat contract: {invalid_keys}")
    if client_keys != set(mappings):
        missing = sorted(client_keys - set(mappings))
        stale = sorted(set(mappings) - client_keys)
        fail(f"anti-cheat mapping mismatch; missing={missing}, stale={stale}")

    guids = list(mappings.values()) + list(contract["bundled_client_plugins"].values())
    if any(not isinstance(guid, str) or not guid.strip() for guid in guids):
        fail("anti-cheat GUIDs must be nonempty strings")
    if len(guids) != len(set(guids)):
        fail("anti-cheat GUIDs must be unique")
    for relative in contract["bundled_client_plugins"]:
        if not (ROOT / relative).is_file():
            fail(f"bundled client plugin is missing: {relative}")

    icon_size = png_dimensions(ROOT / "icon.png")
    if icon_size != (256, 256):
        fail(f"icon.png must be 256x256, got {icon_size[0]}x{icon_size[1]}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or ".github" in path.parts or not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if FORBIDDEN_PARTS.intersection(relative.parts):
            fail(f"forbidden package content: {relative}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            fail(f"forbidden generated or source file: {relative}")

    print(
        f"Validated Ragnavik {manifest['version_number']}: "
        f"{len(manifest['dependencies'])} dependencies, "
        f"{len(guids)} client-only plugin GUIDs."
    )


if __name__ == "__main__":
    main()
