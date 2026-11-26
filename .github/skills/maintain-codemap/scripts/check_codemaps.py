#!/usr/bin/env python3
"""Check CODEMAP.md files for size budget and dangling path references."""

import argparse
import pathlib
import re
import subprocess
import sys

PATH_RE = re.compile(r"`([A-Za-z0-9_.\-]+(?:/[A-Za-z0-9_.\-]+)+/?)`")
LINK_RE = re.compile(r"\]\((?!https?:|#)([^)#\s]+)")


def find_maps(root: pathlib.Path) -> list[pathlib.Path]:
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "*CODEMAP.md"],
        cwd=root, capture_output=True, text=True, check=True,
    ).stdout.split()
    return sorted(root / p for p in out)


def exists(path: str, map_dir: pathlib.Path, root: pathlib.Path) -> bool:
    return any((base / path).exists() for base in (map_dir, root))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=pathlib.Path)
    parser.add_argument("--max-lines", type=int, default=250)
    parser.add_argument("--root-max-lines", type=int, default=100)
    args = parser.parse_args()
    root = args.root.resolve()
    problems: list[str] = []
    for cm in find_maps(root):
        text = cm.read_text(encoding="utf-8")
        rel = cm.relative_to(root)
        limit = args.root_max_lines if cm.parent == root else args.max_lines
        lines = text.count("\n") + 1
        if lines > limit:
            problems.append(f"{rel}: {lines} lines exceeds budget {limit}")
        in_fence = False
        refs: set[str] = set()
        for line in text.splitlines():
            if line.startswith("```"):
                in_fence = not in_fence
                continue
            if not in_fence:
                refs.update(PATH_RE.findall(line))
            refs.update(LINK_RE.findall(line))
        for ref in sorted(refs):
            if "*" in ref or "<" in ref:
                continue
            if not exists(ref, cm.parent, root):
                problems.append(f"{rel}: missing path {ref}")
    print("\n".join(problems) or "CODEMAPs OK")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
