#!/usr/bin/env python3
"""Check local Markdown file links and GitHub-style heading anchors.

No third-party packages or network calls. Scans repository-owned documentation
only; vendor Assets/ and Plugin/ trees are intentionally excluded.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DOCUMENTATION_DIRS = (".agents", "docs", "Docs")
ROOT_DOCS = ("README.md", "AGENTS.md")
LINK = re.compile(r"!?(?:\[[^\]\n]*\])\(\s*(<[^>]+>|[^\s)]+)(?:\s+['\"].*?['\"])?\s*\)")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
SCHEMES = ("http:", "https:", "mailto:", "tel:", "data:")


def documents(root: Path) -> list[Path]:
    """Locate our own Markdown; never scan third-party vendor packages."""
    result = [root / name for name in ROOT_DOCS if (root / name).is_file()]
    for name in DOCUMENTATION_DIRS:
        folder = root / name
        if folder.is_dir():
            result.extend(p for p in folder.rglob("*.md") if p.is_file())
    return sorted(set(result))


def visible_markdown_lines(path: Path) -> list[tuple[int, str]]:
    """Ignore fenced code to prevent code examples looking like document links."""
    result = []
    fence_char, fence_len = None, 0
    for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        match = FENCE.match(line)
        if match:
            token = match.group(1)
            if fence_char is None:
                fence_char, fence_len = token[0], len(token)
            elif token[0] == fence_char and len(token) >= fence_len:
                fence_char, fence_len = None, 0
            continue
        if fence_char is None:
            result.append((number, line))
    return result


def github_slug(text: str) -> str:
    """Basic GitHub Markdown heading slug (Unicode letters/numbers retained)."""
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("&amp;", "&").replace("`", "").replace("*", "").replace("_", "_")
    text = "".join(
        char for char in text.lower()
        if char in " -_" or unicodedata.category(char)[0] in ("L", "N")
    )
    return re.sub(r"\s", "-", text.strip())


def anchors(path: Path) -> set[str]:
    counts: dict[str, int] = defaultdict(int)
    found = set()
    for _, line in visible_markdown_lines(path):
        match = HEADING.match(line)
        if not match:
            continue
        base = github_slug(match.group(1))
        occurrence = counts[base]
        counts[base] += 1
        found.add(base if not occurrence else f"{base}-{occurrence}")
    return found


def check(root: Path) -> list[str]:
    problems = []
    allowed_root = root.resolve()
    anchor_cache: dict[Path, set[str]] = {}
    for source in documents(root):
        for line_number, line in visible_markdown_lines(source):
            for match in LINK.finditer(line):
                target = match.group(1).strip("<>")
                if not target or target.lower().startswith(SCHEMES):
                    continue
                parts = urlsplit(target)
                if parts.scheme or parts.netloc:
                    continue
                if parts.path.startswith("/"):
                    problems.append(f"{source.relative_to(root)}:{line_number}: root-absolute link: {target}")
                    continue
                target_path = (source.parent / unquote(parts.path)).resolve() if parts.path else source.resolve()
                try:
                    target_path.relative_to(allowed_root)
                except ValueError:
                    problems.append(f"{source.relative_to(root)}:{line_number}: link escapes repository: {target}")
                    continue
                if not target_path.exists():
                    problems.append(f"{source.relative_to(root)}:{line_number}: missing target: {target}")
                    continue
                if parts.fragment and target_path.is_file() and target_path.suffix.lower() == ".md":
                    if target_path not in anchor_cache:
                        anchor_cache[target_path] = anchors(target_path)
                    anchor = unquote(parts.fragment)
                    if anchor not in anchor_cache[target_path]:
                        problems.append(f"{source.relative_to(root)}:{line_number}: missing heading anchor: {target}")
    return problems


def main() -> int:
    root = ROOT
    errors = check(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"Documentation link check FAILED: {len(errors)} problem(s).", file=sys.stderr)
        return 1
    print(f"Documentation links OK: {len(documents(root))} Markdown files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
