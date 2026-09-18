#!/usr/bin/env python3
"""Build a reproducible Thunderstore archive for the client pack."""

from __future__ import annotations

import hashlib
import json
import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCLUDED = (
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "icon.png",
    "config",
    "plugins",
)
FIXED_TIME = (2020, 1, 1, 0, 0, 0)
ADDRESS_TOKEN = b"__RAGNAVIK_SERVER_ADDRESS__"
PORT_TOKEN = b"__RAGNAVIK_SERVER_PORT__"


def package_files() -> list[Path]:
    files: list[Path] = []
    for name in INCLUDED:
        path = ROOT / name
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(item for item in path.rglob("*") if item.is_file())
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def packaged_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if ADDRESS_TOKEN not in data and PORT_TOKEN not in data:
        return data
    address = os.environ.get("RAGNAVIK_SERVER_ADDRESS", "").strip()
    port = os.environ.get("RAGNAVIK_SERVER_PORT", "").strip()
    if not address or not port:
        raise SystemExit(
            "release artifact requires RAGNAVIK_SERVER_ADDRESS and "
            "RAGNAVIK_SERVER_PORT"
        )
    if any(character in address for character in "\r\n\t "):
        raise SystemExit("RAGNAVIK_SERVER_ADDRESS contains invalid whitespace")
    if not port.isdigit() or not 1 <= int(port) <= 65535:
        raise SystemExit("RAGNAVIK_SERVER_PORT must be an integer from 1 to 65535")
    return data.replace(ADDRESS_TOKEN, address.encode()).replace(
        PORT_TOKEN, port.encode()
    )


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    output = ROOT / "dist" / f"LostKode-{manifest['name']}-{manifest['version_number']}.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in package_files():
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, packaged_bytes(path), compresslevel=9)
    print(f"{hashlib.sha256(output.read_bytes()).hexdigest()}  {output}")


if __name__ == "__main__":
    main()
