#!/usr/bin/env python3
"""Validate and publish the client release entry to the Ragnavik website."""

from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$")
MAX_BYTES = 12_000


def fail(message: str) -> None:
    raise SystemExit(message)


def load_entry(manifest_path: Path, changelog_path: Path) -> tuple[dict, bytes]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entry = json.loads(changelog_path.read_text(encoding="utf-8"))
    if set(entry) != {"version", "publishedAt", "title", "changes"}:
        fail("release changelog must contain version, publishedAt, title, and changes")
    version = entry.get("version")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        fail("release changelog version must be semantic versioning")
    if version != manifest.get("version_number"):
        fail(f"release changelog version {version} does not match manifest version {manifest.get('version_number')}")
    if not isinstance(entry.get("publishedAt"), str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", entry["publishedAt"]):
        fail("release changelog publishedAt must use YYYY-MM-DD")
    if not isinstance(entry.get("title"), str) or not 1 <= len(entry["title"]) <= 120 or entry["title"] != entry["title"].strip():
        fail("release changelog title must be 1 to 120 trimmed characters")
    changes = entry.get("changes")
    if not isinstance(changes, list) or not 1 <= len(changes) <= 20:
        fail("release changelog must contain 1 to 20 changes")
    if any(not isinstance(change, str) or not 1 <= len(change) <= 400 or change != change.strip() for change in changes):
        fail("each release changelog change must be 1 to 400 trimmed characters")
    payload = json.dumps(entry, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    if len(payload) > MAX_BYTES:
        fail("release changelog exceeds the 12000 byte endpoint limit")
    return entry, payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("validate", "publish"))
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument("--changelog", type=Path, default=Path("release/changelog.json"))
    parser.add_argument("--endpoint")
    parser.add_argument("--api-key")
    args = parser.parse_args()
    entry, payload = load_entry(args.manifest, args.changelog)
    if args.command == "validate":
        print(f"validated website changelog for {entry['version']}")
        return
    if not args.endpoint or not args.api_key:
        fail("publish requires --endpoint and --api-key")
    request = urllib.request.Request(
        args.endpoint,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {args.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "Ragnavik client release workflow",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read())
            if response.status not in (200, 201):
                fail(f"website changelog returned HTTP {response.status}")
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:500]
        fail(f"website changelog returned HTTP {error.code}: {detail}")
    print(f"website changelog {result.get('status', 'accepted')} for {entry['version']}")


if __name__ == "__main__":
    main()
